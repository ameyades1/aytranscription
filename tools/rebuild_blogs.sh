#!/usr/bin/env bash
# Rebuild blog pages and the blog index (output/index.html).
#
# Usage: tools/rebuild_blogs.sh <talk> [<talk> ...]   rebuild these talks, every page that links to
#                                                      them (Further reading, Also read, in-text links)
#                                                      and the index
#        tools/rebuild_blogs.sh --all                 rebuild every blog page and the index
#
# A talk is a folder name under output/. Pages that link to a talk are found through their
# blog/seo.json. The YouTube ID is taken from each existing page, so the video card is kept.
# Pages are built from the SEO-fixed texts (<name>_blog_seo.txt, _blog_seo_en.txt) when they exist.
set -u
cd "$(dirname "$0")/.."

build() {  # build <talk>: rebuild one talk's page; returns non-zero on failure
  local n=$1 page=output/$1/blog/index.html files=() id=''
  # the SEO-fixed copies (from /seo_blog_fix) when they exist, else the original texts
  for s in '' _en; do
    if [ -f "output/$n/${n}_blog_seo$s.txt" ]; then files+=("output/$n/${n}_blog_seo$s.txt")
    elif [ -f "output/$n/${n}_blog$s.txt" ]; then files+=("output/$n/${n}_blog$s.txt"); fi
  done
  if [ ${#files[@]} -eq 0 ]; then echo "Skipped $n: no blog text" >&2; return 1; fi
  [ -f "$page" ] && id=$(grep -o 'youtube\.com/watch?v=[A-Za-z0-9_-]\{11\}' "$page" | head -1 | cut -d= -f2)
  python3 tools/template/blog_page.py "${files[@]}" ${id:+--video=$id}
}

if [ $# -eq 0 ]; then
  sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

if [ "$1" = --all ]; then
  talks=$(for p in output/*/blog/index.html; do basename "$(dirname "$(dirname "$p")")"; done)
else
  for t in "$@"; do
    [ -d "output/$t" ] || { echo "No talk folder output/$t" >&2; exit 1; }
  done
  talks=$(
    for t in "$@"; do
      echo "$t"
      # pages whose seo.json names this talk (as a JSON string)
      grep -l "\"$t\"" output/*/blog/seo.json 2>/dev/null | while read -r f; do
        basename "$(dirname "$(dirname "$f")")"
      done
    done | sort -u
  )
fi

ok=0 failed=()
for n in $talks; do
  if build "$n"; then ok=$((ok + 1)); else failed+=("$n"); fi
done
python3 tools/template/gallery_page.py | head -1

echo "Rebuilt $ok page(s)${failed:+; failed: ${failed[*]}}"
[ ${#failed[@]} -eq 0 ]
