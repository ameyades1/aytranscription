#!/bin/bash

# Build the uploadable zip of the FPJ SEO Sync plugin from wordpress-plugin/fpj-seo-sync/.
#   Usage: wordpress-plugin/build_fpj_seo_sync_zip.sh [output dir]
# Writes fpj-seo-sync-<version>.zip to the output dir (default: your Windows Downloads folder,
# else the current directory). The files sit in an fpj-seo-sync/ folder.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/fpj-seo-sync"
OUT="${1:-}"
if [ -z "$OUT" ]; then
    OUT="$PWD"
    for dir in "/mnt/c/Users/$USER/Downloads" /mnt/c/Users/*/Downloads; do
        case "$dir" in */Public/*|*/Default*) continue ;; esac
        if [ -w "$dir" ]; then OUT="$dir"; break; fi
    done
fi

VERSION=$(sed -n 's/^ \* Version: *//p' "$SRC/fpj-seo-sync.php" | head -1)
[ -n "$VERSION" ] || { echo "No Version: line in the plugin header" >&2; exit 1; }
ZIP="$OUT/fpj-seo-sync-$VERSION.zip"

rm -f "$ZIP"
(cd "$HERE" && python3 -I -c "
import os, sys, zipfile
with zipfile.ZipFile(sys.argv[1], 'w', zipfile.ZIP_DEFLATED) as z:
    for name in sorted(os.listdir('fpj-seo-sync')):
        z.write(os.path.join('fpj-seo-sync', name))
" "$ZIP")
echo "$ZIP"
