#!/bin/bash

# Write image prompts for every blog that has none yet, GROUP blogs per `claude -p "/imageplan ..."`
# session, then rebuild tools/image_plan.md (all blogs) and each new blog's images.txt.
# Blogs with prompts (blog/image_plan.txt) or already in image_plan.md are skipped, so the
# script can be stopped and re-run at any time. When Claude hits a usage limit, it waits.
#
# Usage: ./batch_imageplan.sh
#
# Settings (environment variables):
#   GROUP            blogs per session (default: 10)
#   LIMIT            stop after this many sessions (default: no limit)
#   MODEL / EFFORT / PERMISSION_MODE   (default: claude-opus-5-5 / low / auto)
#   LIMIT_WAIT       seconds to wait after a usage limit (default: 1800)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

GROUP="${GROUP:-10}"
LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-low}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
LOG_DIR="tools/batch_logs/imageplan"
mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%H:%M')] $1"; }

is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

# Blogs without prompts that are not already rows of image_plan.md
todo() {
    for d in output/*/; do
        n="$(basename "$d")"
        [ -f "output/$n/${n}_blog.txt" ] || continue
        [ -f "output/$n/blog/image_plan.txt" ] && continue
        grep -q "/aytranscription/$n/blog/" tools/image_plan.md 2>/dev/null && continue
        echo "$n"
    done
}

sessions=0
while true; do
    mapfile -t group < <(todo | head -n "$GROUP")
    [ ${#group[@]} -eq 0 ] && break
    if [ "$LIMIT" -gt 0 ] && [ "$sessions" -ge "$LIMIT" ]; then
        break
    fi
    log "Writing prompts for ${#group[@]} blogs: ${group[*]}"
    logf="$LOG_DIR/session_$(date +%s).log"
    claude -p "/imageplan ${group[*]}" --permission-mode "$PERMISSION_MODE" \
        --model "$MODEL" --effort "$EFFORT" < /dev/null > "$logf" 2>&1
    left=$(for n in "${group[@]}"; do [ -f "output/$n/blog/image_plan.txt" ] || echo "$n"; done)
    if [ -n "$left" ]; then
        if is_usage_limit "$logf"; then
            log "Usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        log "No prompts written for: $left (see $logf); stopping so it can be checked"
        break
    fi
    sessions=$((sessions + 1))
done

python3 tools/build_image_plan.py
