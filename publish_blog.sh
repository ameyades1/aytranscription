#!/bin/bash

# Take talks from discourse to checked, SEO-fixed blog pages, skipping every step that is already
# done, so the script can be stopped and re-run at any time:
#   1. blog    /chapter <url>         output/<name>/<name>_blog.txt and _blog_en.txt (URL input only)
#   2. SEO     /seo_blog <name>       blog/seo_report.md and blog/seo.json
#   3. fix     /seo_blog_fix <name>   <name>_blog_seo.txt and _blog_seo_en.txt; seo.json updated to them
#   4. check   tools/check_seo.py     stops the talk if it fails
# Once at the end:
#   5. rebuild tools/rebuild_blogs.sh  the talks' pages (from the SEO-fixed texts), the pages that
#              link to them and the blog index
# No WordPress work: ./publish_wordpress.sh imports the talks into the local WordPress afterwards.
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

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
PAUSE="${PAUSE:-0}"
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

    PUBLISHED="$name"
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
done_names=()
skipped=()
for input in "${inputs[@]}"; do
    if publish "$input"; then
        done_count=$((done_count + 1))
        done_names+=("$PUBLISHED")
    else
        skipped+=("$input")
    fi
done

# 5. rebuild: the pages of the talks done (from the SEO-fixed texts), the pages that link to
#    them and the blog index (/seo_blog_fix rebuilds each talk too; this makes sure)
if [ "$done_count" -gt 0 ]; then
    log_info "Rebuilding the blog pages"
    tools/rebuild_blogs.sh "${done_names[@]}" > "$LOG_DIR/_rebuild.log" 2>&1 || log_error "Rebuild failed, see $LOG_DIR/_rebuild.log"
    notes=$(grep '^Note:' "$LOG_DIR/_rebuild.log" | grep -vc 'video details')
    [ "$notes" -gt 0 ] && log_error "$notes 'Note:' line(s) in $LOG_DIR/_rebuild.log: a phrase, heading or talk was not found"
fi

echo
log_info "Finished: $done_count talk(s) ready. Next: ./publish_wordpress.sh <talks> to import them into the local WordPress."
if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi

