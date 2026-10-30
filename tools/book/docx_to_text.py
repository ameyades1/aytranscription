#!/usr/bin/env python3
"""Convert human-typed .docx transcripts to plain text, one file per session.

Usage: python3 docx_to_text.py <transcript dir> <out dir>
Every .docx under the transcript dir becomes <out dir>/DayNN_PartNN.txt, with the day and part
read from the path (e.g. "Day01/Ashma Gita Day 01 Part 03.docx" -> Day01_Part03.txt).
Files whose name has no day and part keep their own name. Existing outputs are kept.
"""
import html
import re
import sys
import zipfile
from pathlib import Path


def docx_text(path):
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    lines = []
    for para in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        text = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", para, re.S))
        if text.strip():
            lines.append(html.unescape(text))
    return "\n".join(lines)


def session_name(path):
    day = re.search(r"day\s*0*(\d+)", str(path), re.I)
    part = re.search(r"part\s*0*(\d+)", path.name, re.I)
    if day and part:
        return "Day%02d_Part%02d" % (int(day.group(1)), int(part.group(1)))
    return re.sub(r"\W+", "_", path.stem).strip("_")


def main(src, dst):
    dst = Path(dst)
    dst.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in Path(src).rglob("*.docx") if not p.name.startswith("~$"))
    if not files:
        sys.exit("no .docx files under %s" % src)
    for path in files:
        out = dst / (session_name(path) + ".txt")
        if out.exists() and out.stat().st_size:
            continue
        out.write_text(docx_text(path), encoding="utf-8")
        print("%s -> %s" % (path, out))
    print("%d sessions in %s" % (len(list(dst.glob("*.txt"))), dst))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
