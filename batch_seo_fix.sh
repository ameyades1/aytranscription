#!/bin/bash

# Run /seo_blog_fix on talks whose SEO is not fixed and consistent, one fresh `claude -p` session
# per talk: it writes <name>_blog_seo.txt and _blog_seo_en.txt, updates seo.json and the report
# to them, and rebuilds the talk's page. A talk is done when tools/verify_seo_fix.py --strict
# passes (fixed copies current, check_seo.py passing, page and seo_fix.md current, every report
# section matching seo.json), so the script can be stopped and re-run at any time.
# Each talk is committed and pushed as soon as it is done (set PUSH=0 to only commit, COMMIT=0 to
# do neither): its fixed texts, seo.json, report, seo_fix.md, and every blog page and the blog
# index that the rebuild changed. Nothing else in the working tree is committed.
# Talks without a seo.json are skipped (run /seo_blog first). When Claude hits a usage limit, it
# waits and retries. At the end every talk is checked again. No WordPress work; nothing is committed.
#
# Usage: ./batch_seo_fix.sh [talk_name ...]   (default: every talk with a seo.json not yet done)
#
# Settings (environment variables):
#   LIMIT            stop after this many talks (default: no limit)
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level (default: medium)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     other failures allowed per talk before skipping it (default: 2)
#   PAUSE            seconds to wait after each talk, to leave usage for other work (default: 3600)
#   COMMIT           set to 0 to not commit finished talks (default: 1)
#   PUSH             set to 0 to commit without pushing (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
PAUSE="${PAUSE:-3600}"
COMMIT="${COMMIT:-1}"
PUSH="${PUSH:-1}"
LOG_DIR="tools/batch_logs/seo_fix"

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

# commit_talk <name>: commit the talk's SEO files and the rebuilt pages, then push
commit_talk() {
    local n="$1" d="output/$1"
    [ "$COMMIT" = 1 ] || return 0
    git add -- "$d/${n}_blog_seo.txt" "$d/${n}_blog_seo_en.txt" "$d/blog/seo.json" \
        "$d/blog/seo_report.md" "$d/blog/seo_fix.md" "$d/blog/index.html" &&
    git add -u -- 'output/*/blog/index.html' output/index.html || return 1
    git diff --cached --quiet && return 0
    git commit -q -m "SEO fix: $n

Written by /seo_blog_fix (batch_seo_fix.sh); every change is listed in
$d/blog/seo_fix.md. Pages rebuilt from the fixed texts.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" || return 1
    [ "$PUSH" = 1 ] || return 0
    git pull -q --rebase --autostash && git push -q
}

# A talk is done when its fix is current and consistent, with no warnings
is_done() {
    python3 tools/verify_seo_fix.py --strict "$1" > /dev/null 2>&1
}

if [ $# -gt 0 ]; then
    talks=("$@")
else
    # every talk with a seo.json (talks already done are skipped below)
    talks=()
    for f in output/*/blog/seo.json; do
        talks+=("$(basename "$(dirname "$(dirname "$f")")")")
    done
fi

done_count=0
skipped=()

for name in "${talks[@]}"; do
    is_done "$name" && continue
    if [ ! -f "output/$name/blog/seo.json" ]; then
        log_error "$name: no seo.json (run /seo_blog $name first), skipped"
        continue
    fi
    if [ "$LIMIT" -gt 0 ] && [ "$done_count" -ge "$LIMIT" ]; then
        break
    fi

    failures=0
    while true; do
        log_info "$name: fixing the blog texts for SEO ($MODEL, effort $EFFORT)"
        log="$LOG_DIR/$name.log"
        claude -p "/seo_blog_fix $name" --permission-mode "$PERMISSION_MODE" \
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
    if commit_talk "$name"; then
        log_info "$name: committed$([ "$PUSH" = 1 ] && echo ' and pushed')"
    else
        log_error "$name: commit or push failed; the talk's files are left for a manual commit"
    fi
    log_info "$name: done ($(tail -1 "$log" | cut -c1-150))"
    [ "$PAUSE" -gt 0 ] && sleep "$PAUSE"
done

echo
log_info "Finished: $done_count talk(s) fixed."

log_info "Verifying every fixed talk"
python3 tools/verify_seo_fix.py --strict > "$LOG_DIR/_check.log" 2>&1
tail -1 "$LOG_DIR/_check.log"
grep -q 'FAIL' "$LOG_DIR/_check.log" && log_error "Failures listed in $LOG_DIR/_check.log"

if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
