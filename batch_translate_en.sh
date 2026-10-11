#!/bin/bash

# Retranslate every talk's English blog (<name>_blog_en.txt) from its Hindi blog (<name>_blog.txt)
# with tools/prompts/hindi_to_english.txt, one fresh `claude -p` session per talk, then rebuild
# that blog page. Finished talks are listed in $LOG_DIR/done.txt and skipped, so the script can be
# stopped and re-run at any time. When Claude hits a usage limit, it waits and retries.
# A result is kept only if it has the same number of ## sections as the Hindi, no Devanagari,
# and is not much shorter than the old English; otherwise the old file is restored.
#
# Usage: ./batch_translate_en.sh [talk_name ...]   (default: every talk in output/)
#
# Settings (environment variables):
#   LIMIT            stop after this many talks (default: no limit)
#   MODEL            claude model (default: claude-opus-5-5)
#   EFFORT           claude effort level (default: medium)
#   PERMISSION_MODE  claude permission mode (default: auto)
#   LIMIT_WAIT       seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_FAILURES     other failures allowed per talk before skipping it (default: 2)
#   PUSH             1 = commit the talk's English blog and page and push after each talk (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

LIMIT="${LIMIT:-0}"
MODEL="${MODEL:-claude-opus-5-5}"
EFFORT="${EFFORT:-medium}"
PERMISSION_MODE="${PERMISSION_MODE:-auto}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"
MAX_FAILURES="${MAX_FAILURES:-2}"
PUSH="${PUSH:-1}"
LOG_DIR="tools/batch_logs/translate_en"
DONE_FILE="$LOG_DIR/done.txt"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $(date '+%H:%M') $1"; }
log_warn()  { echo -e "${YELLOW}[WAIT]${NC} $(date '+%H:%M') $1"; }
log_error() { echo -e "${RED}[FAIL]${NC} $(date '+%H:%M') $1" >&2; }

mkdir -p "$LOG_DIR"
touch "$DONE_FILE"

is_usage_limit() {
    grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit will reset|limit resets|out of extra usage|429" "$1"
}

# YouTube ID from the thumbnail in blog/assets (the .jpg that is not the photo or a blog image)
video_id() {
    ls "output/$1/blog/assets" 2>/dev/null | grep '\.jpg$' |
        grep -vE '^(acharya-ji|hero|inline)\.jpg$' | head -1 | sed 's/\.jpg$//'
}

# Prints a reason and fails if the new English text does not pass the checks
check_result() {
    local hi="$1" en="$2" old="$3"
    python3 - "$hi" "$en" "$old" <<'EOF'
import re, sys
hi, en, old = (open(p, encoding='utf-8').read() for p in sys.argv[1:])
if en == old:
    sys.exit('English file was not rewritten')
h = lambda t: len(re.findall(r'^## ', t, re.M))
if h(hi) != h(en):
    sys.exit(f'{h(en)} sections in English, {h(hi)} in Hindi')
if re.search(r'[ऀ-ॿ]', en):
    sys.exit('Devanagari left in the English')
if len(en) < 0.7 * len(old):
    sys.exit(f'English is {len(en)} chars, old was {len(old)}')
EOF
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
    grep -qxF "$name" "$DONE_FILE" && continue
    if [ "$LIMIT" -gt 0 ] && [ "$done_count" -ge "$LIMIT" ]; then
        break
    fi

    hi="output/$name/${name}_blog.txt"
    en="output/$name/${name}_blog_en.txt"
    old="$LOG_DIR/$name.old_en.txt"
    cp "$en" "$old"

    failures=0
    while true; do
        log_info "$name: translating ($MODEL, effort $EFFORT)"
        log="$LOG_DIR/$name.log"
        claude -p "Read tools/prompts/hindi_to_english.txt and follow it exactly to translate the Hindi blog $hi into English. Overwrite $en with the result (the current file is an older translation; do not reuse its wording). Keep this repo's blog format: '# <Title>' on the first line, only '## ' section headings (no '###'), the same sections in the same order as the Hindi, scripture verses as '>' blocks (bold IAST lines, quoted English meaning, reference line), reflective questions as italic paragraphs, and the closing '## Key Takeaways' bullet list. Write only that one file; do not edit any other file and do not run git." \
            --permission-mode "$PERMISSION_MODE" --model "$MODEL" --effort "$EFFORT" \
            < /dev/null > "$log" 2>&1

        if reason="$(check_result "$hi" "$en" "$old" 2>&1)"; then
            break
        fi
        cp "$old" "$en"
        if is_usage_limit "$log"; then
            log_warn "$name: usage limit reached, retrying in $((LIMIT_WAIT / 60)) min"
            sleep "$LIMIT_WAIT"
            continue
        fi
        failures=$((failures + 1))
        log_error "$name: $reason (attempt $failures/$MAX_FAILURES), see $log"
        if [ "$failures" -ge "$MAX_FAILURES" ]; then
            skipped+=("$name: $reason (see $log)")
            continue 2
        fi
    done

    vid="$(video_id "$name")"
    python3 tools/template/blog_page.py "$hi" "$en" ${vid:+--video="$vid"} > "$LOG_DIR/$name.page.log" 2>&1 ||
        log_error "$name: page rebuild failed, see $LOG_DIR/$name.page.log"
    grep -q "not found for" "$LOG_DIR/$name.page.log" &&
        log_error "$name: an image was left out of the page, see $LOG_DIR/$name.page.log"

    if [ "$PUSH" = "1" ]; then
        files=("$en" "output/$name/blog/index.html")
        git add "${files[@]}" &&
            git commit -q -m "Retranslate English blog: $name" -- "${files[@]}" &&
            git push -q ||
            log_error "$name: git commit/push failed"
    fi
    echo "$name" >> "$DONE_FILE"
    done_count=$((done_count + 1))
    log_info "$name: done"
done

python3 tools/template/gallery_page.py > /dev/null || log_error "gallery rebuild failed"

echo
log_info "Finished: $done_count talk(s) retranslated. Done so far: $(wc -l < "$DONE_FILE")"
if [ ${#skipped[@]} -gt 0 ]; then
    log_error "Skipped ${#skipped[@]}:"
    printf '  - %s\n' "${skipped[@]}" >&2
    exit 1
fi
