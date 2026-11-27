#!/bin/bash

# Run /hindi_register on every talk whose Hindi blog still has words to review
# (tools/check_hindi_register.py --total > 0) and no record yet (output/<name>/blog/hindi_register.md),
# one fresh `claude -p` session per talk. The skill edits the text, checks SEO and rebuilds the pages.
# Done talks are skipped, so the script can be stopped and re-run at any time.
# When Claude hits a usage limit, it waits and retries.
#
# Usage: ./batch_hindi_register.sh [talk_name ...]   (default: every talk, most words per 1000 first)
#
# Settings (environment variables):
#   LIMIT            stop after this many talks (default: no limit)
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level (default: medium)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     other failures allowed per talk before skipping it (default: 2)
#   PUSH             1 = commit the talk's changes and push after each talk (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
PUSH="${PUSH:-1}"
LOG_DIR="tools/batch_logs/hindi_register"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M') $1"; }
log_warn()  { echo -e "${YELLOW}[WAIT]${NC} $(date '+%H:%M') $1"; }
log_error() { echo -e "${RED}[FAIL]${NC} $(date '+%H:%M') $1" >&2; }

mkdir -p "$LOG_DIR"

to_review() { python3 tools/check_hindi_register.py --total "$1" 2>/dev/null; }
recorded()  { [ -s "output/$1/blog/hindi_register.md" ]; }
seo_ok()    { [ ! -f "output/$1/blog/seo.json" ] || python3 tools/check_seo.py "$1" > /dev/null 2>&1; }
done_ok()   { recorded "$1" && seo_ok "$1"; }

is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

if [ $# -gt 0 ]; then
    talks=("$@")
else
    # every talk with a Hindi blog, most Rule 1 words per 1000 first
    mapfile -t talks < <(python3 tools/check_hindi_register.py | awk 'NR > 1 && NF == 6 { print $1 }')
fi

done_count=0
skipped=()

for name in "${talks[@]}"; do
    recorded "$name" && continue
    [ "$(to_review "$name")" = "0" ] && continue
    if [ "$LIMIT" -gt 0 ] && [ "$done_count" -ge "$LIMIT" ]; then
        break
    fi

    failures=0
    while true; do
        log_info "$name: $(to_review "$name") word(s) to review, running /hindi_register ($MODEL, effort $EFFORT)"
        log="$LOG_DIR/$name.log"
        claude -p "/hindi_register $name" --permission-mode "$PERMISSION_MODE" \
            --model "$MODEL" --effort "$EFFORT" \
            < /dev/null > "$log" 2>&1

        if done_ok "$name"; then
            break
        fi
        if is_usage_limit "$log"; then
            log_warn "$name: usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        failures=$((failures + 1))
        log_error "$name: no record or SEO check failing (attempt $failures/$MAX_FAILURES), see $log"
        if [ "$failures" -ge "$MAX_FAILURES" ]; then
            skipped+=("$name (see $log)")
            continue 2
        fi
    done

    if [ "$PUSH" = "1" ]; then
        # the talk's Hindi text and record, and every page the rebuild changed
        git add "output/$name/blog/hindi_register.md" &&
            git add -u output &&
            git commit -q -m "Hindi register: $name" &&
            git push -q ||
            log_error "$name: git commit/push failed"
    fi
    done_count=$((done_count + 1))
    log_info "$name: done ($(tail -1 "$log" | cut -c1-150))"
done

echo
log_info "Finished: $done_count talk(s) edited."
if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
