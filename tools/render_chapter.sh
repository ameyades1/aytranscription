#!/bin/bash
# Render a chapter .txt into a styled web page (.html) and A5 book PDF (.pdf) next to it.
# Usage: tools/render_chapter.sh output/my_chapter.txt

set -e

if [ $# -ne 1 ] || [ ! -f "$1" ]; then
    echo "Usage: $0 <chapter.txt>" >&2
    exit 1
fi

TOOLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
BASE="${SRC%.*}"
CHROME="${CHROME:-google-chrome}"

python3 "${TOOLS_DIR}/template/md_to_html.py" "$SRC" "${BASE}.html"
echo "Web page: ${BASE}.html"

# Chrome shapes Devanagari correctly; the time budget lets the web fonts load
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
    --print-to-pdf="${BASE}.pdf" "file://${BASE}.html" > /dev/null 2>&1
echo "PDF:      ${BASE}.pdf"
