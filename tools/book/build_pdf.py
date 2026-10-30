#!/usr/bin/env python3
"""Assemble a book's chapters (and front and back matter, if written) into one HTML file and print it to PDF.

Usage: python3 build_pdf.py books/<book>
Reads books/<book>/book.json (title, subtitle, author, parts) and chapters/NN_chapter.txt, plus
front_matter.txt and back_matter.txt when they exist. Writes books/<book>/book/<book>.html and .pdf.
Chapters follow the repo text format: one # title, ## sections, > quote and verse blocks,
- and numbered lists, **bold** and *italics*.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

FONT = "'Noto Serif Devanagari', 'Noto Sans Devanagari', serif"

CSS = """
@page { size: A5; margin: 18mm 15mm 20mm 15mm;
        @bottom-center { content: counter(page); font-size: 9pt; } }
body { font-family: %(font)s; font-size: 11pt; line-height: 1.65; color: #111; }
.cover { page-break-after: always; text-align: center; padding-top: 45mm; }
.cover h1 { font-size: 22pt; line-height: 1.4; margin: 0 0 8mm; }
.cover .sub { font-size: 13pt; margin-bottom: 25mm; }
.cover .author { font-size: 14pt; }
.toc { page-break-after: always; }
.toc h2 { text-align: center; }
.toc .part { font-weight: bold; margin-top: 4mm; }
.toc a { color: inherit; text-decoration: none; }
.toc div.ch { margin-left: 5mm; }
.partpage { page-break-before: always; page-break-after: always; text-align: center;
            padding-top: 60mm; font-size: 18pt; font-weight: bold; }
.chapter { page-break-before: always; }
.chapter h1 { font-size: 17pt; text-align: center; line-height: 1.4; margin: 6mm 0 8mm; }
h2 { font-size: 13pt; margin: 7mm 0 2mm; page-break-after: avoid; }
p { margin: 0 0 3mm; text-align: justify; }
blockquote { margin: 4mm 6mm; padding: 2mm 4mm; border-left: 2px solid #999;
             page-break-inside: avoid; }
blockquote p { text-align: left; margin: 0 0 1mm; }
ul, ol { margin: 0 0 3mm; padding-left: 7mm; }
li { margin-bottom: 1mm; }
"""


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return text


def chapter_html(lines, anchor):
    """Convert one chapter's text to HTML; returns (title, html)."""
    out, title = [], ""
    para, quote, items, kind = [], [], [], None

    def flush():
        nonlocal para, quote, items, kind
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
        if quote:
            out.append("<blockquote>%s</blockquote>"
                       % "".join("<p>%s</p>" % inline(q) for q in quote if q))
        if items:
            out.append("<%s>%s</%s>" % (kind, "".join("<li>%s</li>" % inline(i) for i in items), kind))
        para, quote, items, kind = [], [], [], None

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if line.startswith("# "):
            flush()
            title = line[2:].strip()
            out.append('<h1 id="%s">%s</h1>' % (anchor, inline(title)))
        elif line.startswith("## ") or line.startswith("### "):
            flush()
            out.append("<h2>%s</h2>" % inline(line.lstrip("#").strip()))
        elif line.startswith(">"):
            if para or items:
                flush()
            quote.append(line[1:].strip())
        elif re.match(r"^\s*[-*] ", line):
            if kind != "ul":
                flush()
                kind = "ul"
            items.append(re.sub(r"^\s*[-*] ", "", line))
        elif re.match(r"^\s*[0-9०-९]+[.)] ", line):
            if kind != "ol":
                flush()
                kind = "ol"
            items.append(re.sub(r"^\s*[0-9०-९]+[.)] ", "", line))
        elif line.strip() in ("***", "---"):
            flush()
        else:
            if quote or items:
                flush()
            para.append(line.strip())
    flush()
    return title, "\n".join(out)


def matter(path, anchor):
    if not path.exists():
        return ""
    sections, current = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and current:
            sections.append(current)
            current = []
        current.append(line)
    if current:
        sections.append(current)
    return "\n".join('<section class="chapter">%s</section>' % chapter_html(s, "%s%d" % (anchor, i))[1]
                     for i, s in enumerate(sections))


def build(book):
    book = Path(book).resolve()
    cfg = json.loads((book / "book.json").read_text(encoding="utf-8"))
    cfg.setdefault("font", FONT)
    parts = {int(k): v for k, v in cfg.get("parts", {}).items()}
    files = sorted((book / "chapters").glob("[0-9][0-9]_chapter.txt"))
    if not files:
        sys.exit("no chapters in %s" % (book / "chapters"))
    toc, body = [], [matter(book / "front_matter.txt", "front")]
    for f in files:
        n = int(f.name[:2])
        if n in parts:
            toc.append('<div class="part">%s</div>' % html.escape(parts[n]))
            body.append('<div class="partpage">%s</div>' % html.escape(parts[n]))
        anchor = "ch%02d" % n
        title, text = chapter_html(f.read_text(encoding="utf-8").splitlines(), anchor)
        toc.append('<div class="ch"><a href="#%s">%s</a></div>' % (anchor, inline(title)))
        body.append('<section class="chapter">%s</section>' % text)
    body.append(matter(book / "back_matter.txt", "back"))
    title = cfg.get("title") or book.name
    doc = """<!doctype html><html lang="hi"><head><meta charset="utf-8">
<title>%s</title><style>%s</style></head><body>
<div class="cover"><h1>%s</h1><div class="sub">%s</div><div class="author">%s</div></div>
<div class="toc"><h2>विषय-सूची</h2>%s</div>
%s
</body></html>""" % (html.escape(title), CSS % cfg, html.escape(title),
                     html.escape(cfg.get("subtitle", "")), html.escape(cfg.get("author", "")),
                     "\n".join(toc), "\n".join(body))
    out = book / "book"
    out.mkdir(exist_ok=True)
    page, pdf = out / (book.name + ".html"), out / (book.name + ".pdf")
    page.write_text(doc, encoding="utf-8")
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=%s" % pdf, page.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("%d chapters -> %s" % (len(files), pdf))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
