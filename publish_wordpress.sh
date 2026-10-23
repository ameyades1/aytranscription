#!/bin/bash

# Publish talks to the local WordPress, after ./publish_blog.sh has written and checked their SEO
# files. For each talk that passes tools/check_seo.py (and, when it has SEO-fixed texts,
# tools/verify_seo_fix.py, so nothing stale is imported):
#   1. import  tools/make_post_zip.py builds the talk's zip (English and Hindi, from the SEO-fixed
#              texts when they exist) and the Markdown importer plugin imports it with
#              `wp smd import --update`, linking the two posts as translations; the posts are then
#              published (the plugin itself only creates Pending Review posts, as on the live site)
#   2. relink  re-imports the already imported talks that link to this talk but not to its
#              current slugs, so their links point straight to the new URLs
# Once at the end, when at least one talk was imported:
#   3. static  ~/wordpress/export_static.sh exports the local WordPress with Simply Static to
#              output/wp/, then tools/template/seo_gallery_page.py writes the English SEO gallery
#              (output/seo/index.html) and gallery_page.py the main gallery that links to it.
#              Commit and push output/ to publish them on GitHub Pages.
# No Claude steps. Nothing is committed and nothing goes to the live site.
#
# Usage: ./publish_wordpress.sh [talk_name ...]   (default: every talk with a seo.json)
#
# Settings (environment variables):
#   WP_DIR           the local WordPress folder with docker-compose.yml (default: ~/wordpress)
#   WP_USER          the WordPress user the import runs as (default: admin)
#   STATIC           set to 0 to skip step 3 (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

WP_DIR="${WP_DIR:-$HOME/wordpress}"
STATIC="${STATIC:-1}"
WP_USER="${WP_USER:-admin}"
ZIP_DIR=$(mktemp -d)
chmod 755 "$ZIP_DIR"  # readable by the container's web server user
trap 'rm -rf "$ZIP_DIR"' EXIT
LOG_DIR="tools/batch_logs/wordpress"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M') $1"; }
log_error() { echo -e "${RED}[FAIL]${NC} $(date '+%H:%M') $1" >&2; }

mkdir -p "$LOG_DIR"

wp() {
    (cd "$WP_DIR" && docker compose run --rm -T cli wp "$@" 2>/dev/null)
}

# The importer plugin's WP-CLI command, with the talks' zips mounted at /zips, run as the import user
wp_import() {
    (set -o pipefail; cd "$WP_DIR" && docker compose run --rm -T -v "$ZIP_DIR:/zips:ro" cli wp --user="$WP_USER" smd import "$@" 2>&1 | { grep -v ' Container ' || true; })
}

# "<lang> <slug>" for each language in the talk's seo.json
talk_slugs() {
    python3 -c '
import json, sys
w = json.load(open(f"output/{sys.argv[1]}/blog/seo.json", encoding="utf-8")).get("wordpress", {})
for lang in ("en", "hi"):
    if w.get(lang, {}).get("slug"):
        print(lang, w[lang]["slug"])' "$1"
}

# Runs PHP in WordPress with JSON input as $a. Each wp call starts a container (about 1.5 s), so the
# checks below are one call each rather than one per post.
wp_php() {
    wp eval "\$a = json_decode(base64_decode('$(printf '%s' "$2" | base64 -w0)'), true); $1"
}

# The IDs of the published posts with these slugs (any language)
published_ids() {
    wp_php 'foreach ($a as $s) foreach (get_posts(["name" => $s, "post_type" => "post", "post_status" => "publish", "lang" => "", "numberposts" => 1, "fields" => "ids"]) as $id) echo $id, " ";' \
        "$(printf '%s\n' "$@" | python3 -c 'import json, sys; print(json.dumps(sys.stdin.read().split()))')"
}

# Imports one talk with the plugin and publishes its posts; the plugin's output goes to its log
import_talk() {
    local name="$1" log="$LOG_DIR/${1}_import.log" langs=both zip published ids
    mkdir -p "$ZIP_DIR/$name"
    talk_slugs "$name" | grep -q '^hi ' || langs=en
    zip=$(python3 tools/make_post_zip.py "$name" "$ZIP_DIR/$name" --lang "$langs" 2> "$log") || return 1
    # the plugin updates only pending and draft posts: put this talk's published posts back to draft
    # shellcheck disable=SC2046
    published=$(published_ids $(talk_slugs "$name" | cut -d' ' -f2))
    # shellcheck disable=SC2086
    [ -n "$published" ] && wp post update $published --post_status=draft > /dev/null
    if ! wp_import "/zips/$name/$(basename "$zip")" --update >> "$log"; then
        # shellcheck disable=SC2086
        [ -n "$published" ] && wp post update $published --post_status=publish > /dev/null
        return 1
    fi
    ids=$(grep -E '^[0-9]+ ' "$log" | cut -d' ' -f1)
    # shellcheck disable=SC2086
    [ -n "$ids" ] && wp post update $ids --post_status=publish > /dev/null
    return 0
}

# Of the given talks (linking to talk $1), those with an imported post that does not link to $1's
# current URL in the post's language
stale_links() {
    local target="$1"; shift
    [ $# -gt 0 ] || return 0
    wp_php 'foreach ($a["others"] as $talk => $slugs) foreach ($slugs as $lang => $slug) {
        $p = get_posts(["name" => $slug, "post_type" => "post", "post_status" => ["publish", "pending", "draft", "future", "private"], "lang" => "", "numberposts" => 1]);
        if ($p && !empty($a["urls"][$lang]) && strpos($p[0]->post_content, "href=\"" . $a["urls"][$lang] . "\"") === false) { echo $talk, "\n"; break; }
    }' "$(python3 -c '
import json, sys
def slugs(t):
    w = json.load(open(f"output/{t}/blog/seo.json", encoding="utf-8")).get("wordpress", {})
    return {l: w[l]["slug"] for l in ("en", "hi") if w.get(l, {}).get("slug")}
target, others = sys.argv[1], sys.argv[2:]
urls = {l: f"/{s}/" if l == "en" else f"/{l}/{s}/" for l, s in slugs(target).items()}
print(json.dumps({"urls": urls, "others": {o: slugs(o) for o in others}}))' "$target" "$@")"
}

seo_passes() {
    python3 tools/check_seo.py "$1" > /dev/null 2>&1
}

# The talks already imported whose seo.json links to this talk (links, also_read or related)
linking_talks() {
    python3 - "$1" <<'EOF'
import glob, json, os, sys
talk = sys.argv[1]
for path in sorted(glob.glob('output/*/blog/seo.json')):
    other = path.split(os.sep)[1]
    if other == talk:
        continue
    seo = json.load(open(path, encoding='utf-8'))
    targets = [l.get('talk') for l in seo.get('links', [])] + seo.get('related', []) + \
              [(seo.get('also_read') or {}).get('talk')]
    if talk in targets:
        print(other)
EOF
}

publish() {
    local name="$1"
    if ! seo_passes "$name"; then
        log_error "$name: fails tools/check_seo.py (run ./publish_blog.sh $name first)"
        return 1
    fi
    # a talk with SEO-fixed texts must have nothing stale (texts, seo.json, page, images)
    if [ -f "output/$name/${name}_blog_seo_en.txt" ] &&
        ! python3 tools/verify_seo_fix.py "$name" > "$LOG_DIR/${name}_verify.log" 2>&1; then
        log_error "$name: fails tools/verify_seo_fix.py, see $LOG_DIR/${name}_verify.log"
        return 1
    fi

    # 1. import
    if ! import_talk "$name"; then
        log_error "$name: import failed, see $LOG_DIR/${name}_import.log"
        return 1
    fi
    log_info "$name: imported $(grep -E '^[0-9]+ ' "$LOG_DIR/${name}_import.log" | cut -d' ' -f2- | paste -sd' ')"

    # 2. relink: imported talks that link here but not to the current slugs
    local other
    # shellcheck disable=SC2046
    for other in $(stale_links "$name" $(linking_talks "$name")); do
        if import_talk "$other"; then
            log_info "$name: re-imported $other to update its links"
        else
            log_error "$name: re-import of $other failed, see $LOG_DIR/${other}_import.log"
        fi
    done

    return 0
}

if [ $# -gt 0 ]; then
    talks=("$@")
else
    talks=()
    for f in output/*/blog/seo.json; do
        talks+=("$(basename "$(dirname "$(dirname "$f")")")")
    done
fi

done_count=0
skipped=()
for name in "${talks[@]}"; do
    if publish "$name"; then
        done_count=$((done_count + 1))
    else
        skipped+=("$name")
    fi
done

# 3. static site and galleries
if [ "$STATIC" = 1 ] && [ "$done_count" -gt 0 ]; then
    log_info "Exporting the static site and building the galleries"
    if "$WP_DIR/export_static.sh" > "$LOG_DIR/_static.log" 2>&1 &&
        python3 tools/template/seo_gallery_page.py >> "$LOG_DIR/_static.log" 2>&1 &&
        python3 tools/template/gallery_page.py >> "$LOG_DIR/_static.log" 2>&1; then
        grep -E "^Static site|^SEO gallery|^Gallery" "$LOG_DIR/_static.log" | sed 's/^/    /'
    else
        log_error "Static export or gallery failed, see $LOG_DIR/_static.log"
    fi
fi

echo
log_info "Finished: $done_count talk(s) published to the local WordPress."
if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
