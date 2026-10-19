#!/bin/bash

# Run /seo_blog on every talk's blog, one fresh `claude -p` session per talk, writing
# output/<name>/blog/seo_report.md and output/<name>/blog/seo.json. Talks run one at a time, in order, so each
# can reuse the tags of the talks before it. Talks that already pass tools/check_seo.py are
# skipped, so the script can be stopped and re-run at any time. When Claude hits a usage limit,
# it waits and retries. Pages are not rebuilt per talk; at the end every page and the blog index
# are rebuilt once (tools/rebuild_blogs.sh --all) and every talk is checked again.
# Nothing is committed.
#
# Usage: ./batch_seo.sh [talk_name ...]   (default: every talk with a blog page)
#
# Settings (environment variables):
#   LIMIT            stop after this many talks (default: no limit)
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level (default: medium)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     other failures allowed per talk before skipping it (default: 2)
#   REBUILD          set to 0 to skip the final rebuild (default: 1)
#   PAUSE            seconds to wait after each talk, to leave usage for other work (default: 0)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
REBUILD="${REBUILD:-1}"
PAUSE="${PAUSE:-0}"
LOG_DIR="tools/batch_logs/seo"

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

# A talk is done when its report and seo.json pass the check
is_done() {
    python3 tools/check_seo.py "$1" > /dev/null 2>&1
}

if [ $# -gt 0 ]; then
    talks=("$@")
else
    talks=()
    for d in output/*/; do
        n="$(basename "$d")"
        [ -f "output/$n/blog/index.html" ] && [ -f "output/$n/${n}_blog.txt" ] &&
            [ -f "output/$n/${n}_blog_en.txt" ] && talks+=("$n")
    done
fi

done_count=0
skipped=()

for name in "${talks[@]}"; do
    is_done "$name" && continue
    if [ "$LIMIT" -gt 0 ] && [ "$done_count" -ge "$LIMIT" ]; then
        break
    fi

    failures=0
    while true; do
        log_info "$name: writing SEO report and seo.json ($MODEL, effort $EFFORT)"
        log="$LOG_DIR/$name.log"
        claude -p "/seo_blog $name --no-rebuild" --permission-mode "$PERMISSION_MODE" \
            --model "$MODEL" --effort "$EFFORT" \
            < /dev/null > "$log" 2>&1

        is_done "$name" && break
        if is_usage_limit "$log"; then
            log_warn "$name: usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        failures=$((failures + 1))
        log_error "$name: check failed (attempt $failures/$MAX_FAILURES), see $log"
        python3 tools/check_seo.py "$name" | sed 's/^/    /' >&2
        if [ "$failures" -ge "$MAX_FAILURES" ]; then
            skipped+=("$name (see $log)")
            continue 2
        fi
    done

    done_count=$((done_count + 1))
    log_info "$name: done ($(tail -1 "$log" | cut -c1-150))"
    [ "$PAUSE" -gt 0 ] && sleep "$PAUSE"
done

echo
log_info "Finished: $done_count talk(s) written."

if [ "$REBUILD" = 1 ]; then
    log_info "Rebuilding every blog page and the index"
    tools/rebuild_blogs.sh --all > "$LOG_DIR/_rebuild.log" 2>&1 || log_error "Rebuild failed, see $LOG_DIR/_rebuild.log"
    notes=$(grep -c '^Note:' "$LOG_DIR/_rebuild.log")
    [ "$notes" -gt 0 ] && log_error "$notes 'Note:' line(s) in $LOG_DIR/_rebuild.log: a phrase, heading or talk was not found"
fi

log_info "Checking every talk with a seo.json"
python3 tools/check_seo.py > "$LOG_DIR/_check.log" 2>&1
tail -1 "$LOG_DIR/_check.log"
grep -q 'FAIL' "$LOG_DIR/_check.log" && log_error "Failures listed in $LOG_DIR/_check.log"

if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
