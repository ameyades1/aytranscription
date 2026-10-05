#!/bin/bash

# Run /dequote on every talk whose blog texts still contain direct quotes from Acharya Ji,
# one fresh `claude -p` session per talk, then rebuild that blog page and the gallery.
# Talks with no quotes left are skipped, so the script can be stopped and re-run at any time.
# When Claude hits a usage limit, it waits and retries.
#
# Usage: ./batch_dequote.sh [talk_name ...]   (default: every talk in output/)
#
# Settings (environment variables):
#   LIMIT            stop after this many talks (default: no limit)
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level (default: low)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     other failures allowed per talk before skipping it (default: 2)
#   PUSH             1 = commit the talk's blog and the gallery and push after each talk (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-low}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
PUSH="${PUSH:-1}"
LOG_DIR="tools/batch_logs/dequote"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M') $1"; }
log_warn()  { echo -e "${YELLOW}[WAIT]${NC} $(date '+%H:%M') $1"; }
log_error() { echo -e "${RED}[FAIL]${NC} $(date '+%H:%M') $1" >&2; }

mkdir -p "$LOG_DIR"

quotes_left() { python3 tools/count_quotes.py "$1"; }

is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

# YouTube ID from the thumbnail in blog/assets (the .jpg that is not the photo or a blog image)
video_id() {
    ls "output/$1/blog/assets" 2>/dev/null | grep '\.jpg$' |
        grep -vE '^(acharya-ji|hero|inline)\.jpg$' | head -1 | sed 's/\.jpg$//'
}

if [ $# -gt 0 ]; then
    talks=("$@")
else
    talks=()
    for d in output/*/; do
        n="$(basename "$d")"
        [ -f "output/$n/${n}_blog.txt" ] && talks+=("$n")
    done
fi

done_count=0
skipped=()

for name in "${talks[@]}"; do
    [ "$(quotes_left "$name")" = "0" ] && continue
    if [ "$LIMIT" -gt 0 ] && [ "$done_count" -ge "$LIMIT" ]; then
        break
    fi

    failures=0
    while true; do
        log_info "$name: $(quotes_left "$name") quotes, running /dequote ($MODEL, effort $EFFORT)"
        log="$LOG_DIR/$name.log"
        claude -p "/dequote $name" --permission-mode "$PERMISSION_MODE" \
            --model "$MODEL" --effort "$EFFORT" \
            < /dev/null > "$log" 2>&1

        if [ "$(quotes_left "$name")" = "0" ]; then
            break
        fi
        if is_usage_limit "$log"; then
            log_warn "$name: usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        failures=$((failures + 1))
        log_error "$name: $(quotes_left "$name") quotes still left (attempt $failures/$MAX_FAILURES), see $log"
        if [ "$failures" -ge "$MAX_FAILURES" ]; then
            skipped+=("$name (see $log)")
            continue 2
        fi
    done

    vid="$(video_id "$name")"
    python3 tools/template/blog_page.py "output/$name/${name}_blog.txt" "output/$name/${name}_blog_en.txt" \
        ${vid:+--video="$vid"} > /dev/null 2>&1 &&
        python3 tools/template/gallery_page.py > /dev/null ||
        log_error "$name: page or gallery rebuild failed"

    if [ "$PUSH" = "1" ]; then
        files=("output/$name/${name}_blog.txt" "output/$name/${name}_blog_en.txt"
               "output/$name/blog/index.html" output/index.html)
        git add "${files[@]}" &&
            git commit -q -m "Rewrite quotes as text: $name" -- "${files[@]}" &&
            git push -q ||
            log_error "$name: git commit/push failed"
    fi
    done_count=$((done_count + 1))
    log_info "$name: done"
done

echo
log_info "Finished: $done_count talk(s) rewritten. Quotes left in all blogs: $(
    t=0; for d in output/*/; do n=$(basename "$d"); [ -f "output/$n/${n}_blog.txt" ] && t=$((t + $(quotes_left "$n"))); done; echo $t)"
if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
