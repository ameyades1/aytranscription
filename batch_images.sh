#!/bin/bash

# Generate hero and inline images with AI Horde for every blog in tools/image_plan.md that has
# no assets/hero.jpg yet, then rebuild its page and the gallery, commit and push.
# Blogs that already have images are skipped, so the script can be stopped and re-run.
#
# Usage: ./batch_images.sh
#
# Settings (environment variables):
#   MODEL          flux or juggernaut (default: juggernaut)
#   HORDE_API_KEY  AI Horde account key (default: the key in tools/.horde_key, else anonymous)
#   PUSH           1 = commit and push after each blog (default: 1)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

MODEL="${MODEL:-juggernaut}"
PUSH="${PUSH:-1}"
PY=tools/image-env/bin/python
LOG_DIR="tools/batch_logs/images"
mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%m-%d %H:%M')] $1"; }

if [ -n "$HORDE_API_KEY" ] || [ -s tools/.horde_key ]; then log "Using an AI Horde account key"; else log "Using the anonymous AI Horde key (slow)"; fi

talks=$(grep -oE '^\[[0-9]+\]: \S+/aytranscription/[^/]+/blog/' tools/image_plan.md | sed -E 's|.*/aytranscription/([^/]+)/blog/|\1|')
done_count=0
failed=()

for name in $talks; do
    [ -f "output/$name/blog/assets/hero.jpg" ] && continue
    [ -f "output/$name/${name}_blog.txt" ] || continue
    log "$name: generating ($MODEL)"
    start=$(date +%s)
    # Full output to the blog's log; the TIMING lines (queue, eta, time taken) also to this log
    $PY tools/horde_image.py "$name" --model "$MODEL" 2>&1 | tee "$LOG_DIR/$name.log" |
        grep --line-buffered -E "^(hero|inline) |TIMING|no worker|note:" | sed -u 's/^/    /'
    if [ "${PIPESTATUS[0]}" -ne 0 ] ||
       [ ! -f "output/$name/blog/assets/inline.jpg" ]; then
        log "$name: FAILED, see $LOG_DIR/$name.log"
        rm -f "output/$name/blog/assets/hero.jpg"   # so a re-run retries this blog
        failed+=("$name")
        sleep 60
        continue
    fi

    vid=$(ls "output/$name/blog/assets" | grep '\.jpg$' | grep -vE '^(acharya-ji|hero|inline)\.jpg$' | sed 's/\.jpg$//' | head -1)
    python3 tools/template/blog_page.py "output/$name/${name}_blog.txt" "output/$name/${name}_blog_en.txt" \
        ${vid:+--video="$vid"} > /dev/null 2>&1 &&
        python3 tools/template/gallery_page.py > /dev/null 2>&1 ||
        log "$name: page or gallery rebuild failed"

    if [ "$PUSH" = "1" ]; then
        files=("output/$name/blog" output/index.html)
        git add "${files[@]}" &&
            git commit -q -m "Add hero and inline images: $name" -- "${files[@]}" &&
            { git pull -q --rebase --autostash origin main; git push -q; } ||
            log "$name: git commit/push failed"
    fi
    done_count=$((done_count + 1))
    log "$name: done in $(( ($(date +%s) - start) / 60 )) min"
done

log "Finished: $done_count blog(s) with new images."
if [ ${#failed[@]} -gt 0 ]; then
    log "Failed (re-run to retry): ${failed[*]}"
    exit 1
fi
