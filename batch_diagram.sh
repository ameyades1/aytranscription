#!/bin/bash

# Run /diagram on every talk with a blog page and no decision yet (output/<name>/blog/diagram.md),
# one fresh `claude -p` session per talk, in publishing order (the waves of category_mapping.xlsx).
# The skill decides whether the talk needs a text diagram; with one, it writes blog/diagram.json,
# checks it and rebuilds the page. Decided talks are skipped, so the script can be stopped and
# re-run at any time. When Claude hits a usage limit, it waits and retries.
#
# Usage: ./batch_diagram.sh [talk_name ...]       (default: every talk, wave by wave)
#        ./batch_diagram.sh $(python3 tools/wave_order.py --waves 1-5)
#
# Settings (environment variables):
#   LIMIT            stop after this many talks (default: no limit)
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level (default: medium)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     other failures allowed per talk before skipping it (default: 2)
#   PUSH             1 = commit and push after each talk; end = commit after each talk and push
#                    once at the end (one Pages deploy); 0 = no commit (default: end)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
PUSH="${PUSH:-end}"
LOG_DIR="tools/batch_logs/diagram"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M') $1"; }
log_warn()  { echo -e "${YELLOW}[WAIT]${NC} $(date '+%H:%M') $1"; }
log_error() { echo -e "${RED}[FAIL]${NC} $(date '+%H:%M') $1" >&2; }

mkdir -p "$LOG_DIR"

decided()  { [ -s "output/$1/blog/diagram.md" ]; }
has_page() { [ -f "output/$1/blog/index.html" ]; }
# done: decided, and a diagram (if any) passes the checks
done_ok()  { decided "$1" && { [ ! -f "output/$1/blog/diagram.json" ] || python3 tools/verify_seo_fix.py "$1" > /dev/null 2>&1; }; }
is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

if [ $# -gt 0 ]; then
    talks=("$@")
else
    mapfile -t talks < <(python3 tools/wave_order.py)
fi

done_count=0
with_diagram=0
skipped=()

for name in "${talks[@]}"; do
    decided "$name" && continue
    has_page "$name" || continue
    if [ "$LIMIT" -gt 0 ] && [ "$done_count" -ge "$LIMIT" ]; then
        break
    fi

    failures=0
    while true; do
        log_info "$name: running /diagram ($MODEL, effort $EFFORT)"
        log="$LOG_DIR/$name.log"
        claude -p "/diagram $name" --permission-mode "$PERMISSION_MODE" \
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
        log_error "$name: no decision or the check failing (attempt $failures/$MAX_FAILURES), see $log"
        if [ "$failures" -ge "$MAX_FAILURES" ]; then
            skipped+=("$name (see $log)")
            continue 2
        fi
    done

    [ -f "output/$name/blog/diagram.json" ] && with_diagram=$((with_diagram + 1))
    if [ "$PUSH" = "1" ] || [ "$PUSH" = "end" ]; then
        # the decision, the spec, and every page the rebuild changed
        git add "output/$name/blog/diagram.md" &&
            { [ ! -f "output/$name/blog/diagram.json" ] || git add "output/$name/blog/diagram.json"; } &&
            git add -u output &&
            git commit -q -m "Diagram: $name ($(sed -n 's/^Decision: //p' "output/$name/blog/diagram.md"))" &&
            { [ "$PUSH" = "end" ] || git push -q; } ||
            log_error "$name: git commit/push failed"
    fi
    done_count=$((done_count + 1))
    log_info "$name: $(sed -n 's/^Decision: //p' "output/$name/blog/diagram.md") ($(tail -1 "$log" | cut -c1-150))"
done

echo
if [ "$PUSH" = "end" ] && [ "$done_count" -gt 0 ]; then
    git push -q && log_info "Pushed $done_count commit(s)" || log_error "git push failed"
fi
log_info "Finished: $done_count talk(s) decided, $with_diagram with a diagram."
if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
