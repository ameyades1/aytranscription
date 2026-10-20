#!/bin/bash

# Build the uploadable zip of the Markdown importer plugin from wordpress-plugin/smd-importer/.
#   Usage: wordpress-plugin/build_zip.sh [output dir]
# Writes surerank-markdown-importer-<version>.zip, the version taken from the plugin header, to
# the output dir (default: the Windows Downloads folder, else the current directory). The files
# sit in an smd-importer/ folder, so uploading it over an installed copy replaces that plugin.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/smd-importer"
OUT="${1:-}"
if [ -z "$OUT" ]; then
    OUT="$PWD"
    for dir in /mnt/c/Users/*/Downloads; do
        if [ -w "$dir" ]; then OUT="$dir"; break; fi
    done
fi

VERSION=$(sed -n 's/^ \* Version: *//p' "$SRC/surerank-markdown-importer.php" | head -1)
[ -n "$VERSION" ] || { echo "No Version: line in the plugin header" >&2; exit 1; }
ZIP="$OUT/surerank-markdown-importer-$VERSION.zip"

rm -f "$ZIP"
python3 -I - "$HERE" "$ZIP" <<'EOF'
import os, sys, zipfile
here, zip_path = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(os.path.join(here, 'smd-importer')):
        for f in sorted(files):
            path = os.path.join(root, f)
            z.write(path, os.path.relpath(path, here))
EOF
echo "$ZIP"
