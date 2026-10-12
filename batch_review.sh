#!/bin/bash

# Run /review_blog on every talk's blog, one fresh `claude -p` session per talk, writing
# tools/review/<name>.md. Talks that already have a review are skipped, so the script can be
# stopped and re-run at any time. When Claude hits a usage limit, it waits and retries.
# At the end, tools/review/SUMMARY.md lists every talk's verdict, worst first.
#
# Usage: ./batch_review.sh [talk_name ...]   (default: every talk in output/)
#
# Settings (environment variables):
#   LIMIT            stop after this many talks (default: no limit)
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level (default: medium)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     other failures allowed per talk before skipping it (default: 2)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
REVIEW_DIR="tools/review"
LOG_DIR="tools/batch_logs/review"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M') $1"; }
log_warn()  { echo -e "${YELLOW}[WAIT]${NC} $(date '+%H:%M') $1"; }
log_error() { echo -e "${RED}[FAIL]${NC} $(date '+%H:%M') $1" >&2; }

mkdir -p "$REVIEW_DIR" "$LOG_DIR"

is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

# A review is valid when its first line is "<name>: <verdict>" (Markdown-escaped \_ allowed)
has_review() {
    head -1 "$REVIEW_DIR/$1.md" 2>/dev/null | sed 's/\\_/_/g' |
        grep -qE "^$1: (No issues|Minor issues|Needs correction)"
}

if [ $# -gt 0 ]; then
    talks=("$@")
else
    talks=()
    for d in output/*/; do
        n="$(basename "$d")"
        [ -f "output/$n/${n}_blog.txt" ] && [ -f "output/$n/${n}_blog_en.txt" ] && talks+=("$n")
    done
fi

done_count=0
skipped=()

for name in "${talks[@]}"; do
    has_review "$name" && continue
    if [ "$LIMIT" -gt 0 ] && [ "$done_count" -ge "$LIMIT" ]; then
        break
    fi

    failures=0
    while true; do
        log_info "$name: reviewing ($MODEL, effort $EFFORT)"
        log="$LOG_DIR/$name.log"
        claude -p "/review_blog $name" --permission-mode "$PERMISSION_MODE" \
            --model "$MODEL" --effort "$EFFORT" \
            < /dev/null > "$log" 2>&1

        has_review "$name" && break
        if is_usage_limit "$log"; then
            log_warn "$name: usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        failures=$((failures + 1))
        log_error "$name: no valid review written (attempt $failures/$MAX_FAILURES), see $log"
        if [ "$failures" -ge "$MAX_FAILURES" ]; then
            skipped+=("$name (see $log)")
            continue 2
        fi
    done

    done_count=$((done_count + 1))
    log_info "$name: $(head -1 "$REVIEW_DIR/$name.md" | cut -d: -f2-)"
done

# Summary of all reviews, worst verdict first
{
    echo "# Blog review summary"
    echo
    for v in "Needs correction" "Minor issues" "No issues"; do
        files=$(grep -lE "^[^ ]+: $v" "$REVIEW_DIR"/*.md 2>/dev/null | grep -v SUMMARY.md)
        echo "## $v ($(echo -n "$files" | grep -c .))"
        echo
        for f in $files; do echo "- [$(basename "$f" .md)]($(basename "$f"))"; done
        echo
    done
} > "$REVIEW_DIR/SUMMARY.md"

echo
log_info "Finished: $done_count talk(s) reviewed. Summary: $REVIEW_DIR/SUMMARY.md"
if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
