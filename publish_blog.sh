#!/bin/bash

# Take talks all the way from discourse to the local WordPress, skipping every step that is
# already done, so the script can be stopped and re-run at any time:
#   1. blog    /chapter <url>         output/<name>/<name>_blog.txt and _blog_en.txt (URL input only)
#   2. SEO     /seo_blog <name>       blog/seo_report.md and blog/seo.json
#   3. fix     /seo_blog_fix <name>   <name>_blog_seo.txt and _blog_seo_en.txt; seo.json updated to them
#   4. check   tools/check_seo.py     stops the talk if it fails
#   5. import  ~/wordpress/import_post.py   creates or updates the talk's post
#   6. relink  re-imports the already imported posts that link to this talk but not to its
#              current slug, so their links point straight to the new URL
# Once at the end, when at least one talk was imported:
#   7. static  ~/wordpress/export_static.sh exports the local WordPress with Simply Static to
#              output/wp/, then tools/template/seo_gallery_page.py writes the English SEO gallery
#              (output/seo/index.html) and gallery_page.py the main gallery that links to it.
#              Commit and push output/ to publish them on GitHub Pages.
# Each Claude step is a fresh `claude -p` session. When Claude hits a usage limit, it waits and
# retries. Nothing is committed and nothing goes to the live site.
#
# Usage: ./publish_blog.sh [talk_name | youtube_url ...]   (default: every talk with a blog page)
#
# Settings (environment variables):
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level for SEO and fix (default: medium)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     failed attempts allowed per step before skipping the talk (default: 2)
#   PAUSE            seconds to wait after each talk that ran a Claude step (default: 0)
#   WP_DIR           the local WordPress folder with import_post.py (default: ~/wordpress)
#   STATIC           set to 0 to skip step 7 (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
PAUSE="${PAUSE:-0}"
WP_DIR="${WP_DIR:-$HOME/wordpress}"
STATIC="${STATIC:-1}"
LOG_DIR="tools/batch_logs/publish"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M') $1"; }
log_warn()  { echo -e "${YELLOW}[WAIT]${NC} $(date '+%H:%M') $1"; }
log_error() { echo -e "${RED}[FAIL]${NC} $(date '+%H:%M') $1" >&2; }

mkdir -p "$LOG_DIR"

is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

wp() {
    (cd "$WP_DIR" && docker compose run --rm -T cli wp "$@" 2>/dev/null)
}

# The talk whose blog page embeds this YouTube video, if any
talk_for_video() {
    local id
    id=$(python3 -c 'import re,sys; m=re.search(r"(?:v=|youtu\.be/|shorts/|live/)([A-Za-z0-9_-]{11})", sys.argv[1]); print(m.group(1) if m else "")' "$1")
    [ -n "$id" ] || return 1
    grep -l "youtube.com/watch?v=$id" output/*/blog/index.html 2>/dev/null | head -1 | cut -d/ -f2
}

# The SEO-fixed copies exist and are newer than the original blog texts
fix_current() {
    local n="$1" d="output/$1"
    [ -f "$d/${n}_blog_seo.txt" ] && [ -f "$d/${n}_blog_seo_en.txt" ] &&
        [ "$d/${n}_blog_seo.txt" -nt "$d/${n}_blog.txt" ] && [ "$d/${n}_blog_seo_en.txt" -nt "$d/${n}_blog_en.txt" ]
}

seo_passes() {
    python3 tools/check_seo.py "$1" > /dev/null 2>&1
}

# run_claude <step> <name> <prompt> <effort> <done-test...>: retries on usage limits and failures
run_claude() {
    local step="$1" name="$2" prompt="$3" effort="$4"
    shift 4
    local log="$LOG_DIR/${name}_$step.log" failures=0
    while true; do
        log_info "$name: $step ($MODEL, effort $effort)"
        claude -p "$prompt" --permission-mode "$PERMISSION_MODE" --model "$MODEL" --effort "$effort" \
            < /dev/null > "$log" 2>&1
        "$@" && { log_info "$name: $step done ($(tail -1 "$log" | cut -c1-150))"; return 0; }
        if is_usage_limit "$log"; then
            log_warn "$name: usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        failures=$((failures + 1))
        log_error "$name: $step failed (attempt $failures/$MAX_FAILURES), see $log"
        [ "$failures" -ge "$MAX_FAILURES" ] && return 1
    done
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
    local input="$1" name ran_claude=0

    # 1. blog
    if [[ "$input" == http* ]]; then
        name=$(talk_for_video "$input")
        if [ -z "$name" ]; then
            run_claude blog "$(date +%s)" "/chapter $input" low talk_for_video "$input" || return 1
            name=$(talk_for_video "$input")
            ran_claude=1
        fi
        log_info "$input → $name"
    else
        name="$input"
    fi
    local d="output/$name"
    if [ ! -f "$d/${name}_blog.txt" ] || [ ! -f "$d/${name}_blog_en.txt" ] || [ ! -f "$d/blog/index.html" ]; then
        log_error "$name: no blog texts or blog page in $d (run /chapter first)"
        return 1
    fi

    # 2. SEO and 3. fix: done when the fixed copies are current and pass the check
    if fix_current "$name" && seo_passes "$name"; then
        log_info "$name: SEO and fix already done"
    else
        if [ -f "$d/${name}_blog_seo.txt" ] || [ -f "$d/${name}_blog_seo_en.txt" ]; then
            log_info "$name: SEO-fixed copies are stale or fail the check; redoing SEO and fix"
            rm -f "$d/${name}_blog_seo.txt" "$d/${name}_blog_seo_en.txt"
        fi
        if seo_passes "$name"; then
            log_info "$name: SEO report already done"
        else
            run_claude seo "$name" "/seo_blog $name" "$EFFORT" seo_passes "$name" || return 1
            ran_claude=1
        fi
        fix_done() { fix_current "$1" && seo_passes "$1"; }
        run_claude fix "$name" "/seo_blog_fix $name" "$EFFORT" fix_done "$name" || return 1
        ran_claude=1
    fi

    # 4. check
    if ! python3 tools/check_seo.py "$name" > "$LOG_DIR/${name}_check.log" 2>&1; then
        log_error "$name: check failed, see $LOG_DIR/${name}_check.log"
        return 1
    fi

    # 5. import
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

    # 6. relink: imported posts that link here but not to the current slug
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

    [ "$ran_claude" = 1 ] && [ "$PAUSE" -gt 0 ] && sleep "$PAUSE"
    return 0
}

if [ $# -gt 0 ]; then
    inputs=("$@")
else
    inputs=()
    for d in output/*/; do
        n="$(basename "$d")"
        [ -f "output/$n/blog/index.html" ] && [ -f "output/$n/${n}_blog.txt" ] &&
            [ -f "output/$n/${n}_blog_en.txt" ] && inputs+=("$n")
    done
fi

done_count=0
skipped=()
for input in "${inputs[@]}"; do
    if publish "$input"; then
        done_count=$((done_count + 1))
    else
        skipped+=("$input")
    fi
done

# 7. static site and galleries
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
