#!/bin/bash

# Publish talks to the local WordPress, after ./publish_blog.sh has written and checked their SEO
# files. For each talk that passes tools/check_seo.py (and, when it has SEO-fixed texts,
# tools/verify_seo_fix.py, so nothing stale is imported):
#   1. import  ~/wordpress/import_post.py   creates or updates the talk's post (from the SEO-fixed
#              texts when they exist)
#   2. relink  re-imports the already imported posts that link to this talk but not to its
#              current slug, so their links point straight to the new URL
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
#   WP_DIR           the local WordPress folder with import_post.py (default: ~/wordpress)
#   STATIC           set to 0 to skip step 3 (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

WP_DIR="${WP_DIR:-$HOME/wordpress}"
STATIC="${STATIC:-1}"
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
    local old_slug new_slug
    old_slug=$(wp post list --post_type=post --meta_key=_antaryog_talk --meta_value="$name" --post_status=any --field=post_name)
    if ! python3 "$WP_DIR/import_post.py" "$name" > "$LOG_DIR/${name}_import.log" 2>&1; then
        log_error "$name: import failed, see $LOG_DIR/${name}_import.log"
        return 1
    fi
    grep '^Note:' "$LOG_DIR/${name}_import.log" | sed "s/^/    /" >&2
    log_info "$name: imported $(grep '^http' "$LOG_DIR/${name}_import.log")"
    new_slug=$(wp post list --post_type=post --meta_key=_antaryog_talk --meta_value="$name" --post_status=any --field=post_name)
    [ -n "$old_slug" ] && [ "$old_slug" != "$new_slug" ] && log_info "$name: slug changed, $old_slug → $new_slug"

    # 2. relink: imported posts that link here but not to the current slug
    local other pid
    for other in $(linking_talks "$name"); do
        pid=$(wp post list --post_type=post --meta_key=_antaryog_talk --meta_value="$other" --post_status=any --field=ID)
        [ -n "$pid" ] || continue
        if ! wp post get "$pid" --field=post_content | grep -q "href=\"/$new_slug/\""; then
            if python3 "$WP_DIR/import_post.py" "$other" > "$LOG_DIR/${other}_import.log" 2>&1; then
                log_info "$name: re-imported $other to update its link"
            else
                log_error "$name: re-import of $other failed, see $LOG_DIR/${other}_import.log"
            fi
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
