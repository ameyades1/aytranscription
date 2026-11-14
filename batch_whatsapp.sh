#!/bin/bash

# Write a WhatsApp message (output/<name>/<name>_whatsapp_en.txt) for every talk with an English
# blog and no message yet, GROUP talks per `claude -p "/whatsapp ..."` session. Talks with a
# message are skipped, so the script can be stopped and re-run. When Claude hits a usage limit,
# it waits.
#
# Usage: ./batch_whatsapp.sh
#
# Settings (environment variables):
#   GROUP            talks per session (default: 10)
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
LOG_DIR="tools/batch_logs/whatsapp"
mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%H:%M')] $1"; }

is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

SKIP="$LOG_DIR/skipped.txt"
: > "$SKIP"
todo() {
    for d in output/*/; do
        n="$(basename "$d")"
        [ -f "output/$n/${n}_blog_en.txt" ] || continue
        [ -f "output/$n/${n}_whatsapp_en.txt" ] && continue
        grep -qxF "$n" "$SKIP" && continue
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
    log "Writing messages for ${#group[@]} talks: ${group[*]}"
    logf="$LOG_DIR/session_$(date +%s).log"
    claude -p "/whatsapp ${group[*]}" --permission-mode "$PERMISSION_MODE" \
        --model "$MODEL" --effort "$EFFORT" < /dev/null > "$logf" 2>&1
    done_any=0
    for n in "${group[@]}"; do
        if [ -f "output/$n/${n}_whatsapp_en.txt" ]; then done_any=1; else echo "$n" >> "$SKIP"; fi
    done
    if [ "$done_any" -eq 0 ]; then
        if is_usage_limit "$logf"; then
            for n in "${group[@]}"; do sed -i "/^$n\$/d" "$SKIP"; done
            log "Usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        log "No messages written (see $logf); stopping so it can be checked"
        break
    fi
    sessions=$((sessions + 1))
done

[ -s "$SKIP" ] && log "No message for (no video id?): $(tr '\n' ' ' < "$SKIP")"
log "Done"
