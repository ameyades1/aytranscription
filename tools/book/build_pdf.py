#!/usr/bin/env python3
"""Assemble a book's chapters (and front and back matter, if written) into one HTML file, print it to PDF
and write an EPUB.

Usage: python3 build_pdf.py books/<book>
Reads books/<book>/book.json (title, subtitle, author, parts) and chapters/NN_chapter.txt, plus
front_matter.txt and back_matter.txt when they exist, and intro/intro_pages.html (designed opening
pages: title page, imprint, photos, profiles; its images sit next to it) in place of the plain cover.
Writes books/<book>/book/<book>.html, .pdf and .epub. The EPUB is plain Unicode text, for e-readers and read-aloud apps; Chrome's PDF does not map
Devanagari vowel signs back to text, so text copied or read aloud from the PDF is garbled.
Chapters follow the repo text format: one # title, ## sections, > quote and verse blocks,
- and numbered lists, **bold** and *italics*.
"""
import html
import json
import re
import subprocess
import sys
import uuid
import zipfile
from datetime import datetime, timezone
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
    """Split a front or back matter file at its # titles; returns [(title, html)]."""
    if not path.exists():
        return []
    sections, current = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and current:
            sections.append(current)
            current = []
        current.append(line)
    if current:
        sections.append(current)
    return [chapter_html(s, "%s%d" % (anchor, i)) for i, s in enumerate(sections)]


def scope_css(css):
    """Prefix every rule of a stylesheet with .intro, so the intro pages keep their own styles
    inside the book. Its @page rules become the named page "intro", so they keep their margins."""
    css, out, i = re.sub(r"/\*.*?\*/", "", css, flags=re.S), [], 0
    while True:
        j = css.find("{", i)
        if j < 0:
            return "\n".join(out)
        depth, k = 0, j
        while True:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            if depth == 0:
                break
            k += 1
        sel, block, i = css[i:j].strip(), css[j:k + 1], k + 1
        if sel.startswith("@page"):
            out.append("@page intro" + sel[5:].replace(" :", ":") + " " + block)
        elif not sel.startswith("@"):
            out.append(",".join(".intro" if s.strip() == "body" else ".intro " + s.strip()
                                for s in sel.split(",")) + " " + block)


def load_intro(book):
    """The designed opening pages in intro/intro_pages.html (title page, imprint, photos,
    profiles), if the book has them: (scoped CSS, body HTML, {image file name: Path})."""
    page = book / "intro" / "intro_pages.html"
    if not page.exists():
        return None
    text = page.read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", text, re.S).group(1)
    body = re.sub(r"<!--.*?-->", "", re.search(r"<body>(.*?)</body>", text, re.S).group(1), flags=re.S)
    images = {name: page.parent / name for name in re.findall(r'src="([^":/]+)"', body)}
    return scope_css(css), body, images


EPUB_CSS = """body { font-family: 'Noto Serif Devanagari', serif; line-height: 1.7; }
h1 { text-align: center; font-size: 1.5em; }
h1.part { margin-top: 30%; }
h2 { font-size: 1.2em; }
blockquote { margin: 1em 1.5em; padding-left: 0.8em; border-left: 2px solid #999; }
.cover { text-align: center; margin-top: 25%; }
"""


def xhtml(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
            'xml:lang="hi" lang="hi"><head><meta charset="utf-8"/><title>%s</title>'
            '<link rel="stylesheet" href="style.css"/></head><body>%s</body></html>'
            % (html.escape(title), body))


def write_epub(path, book_name, cfg, title, docs, intro=None):
    """Write an EPUB 3: the intro pages (or a plain cover page), the contents, then one file per
    entry of docs [(title, html)], in order."""
    author = cfg.get("author", "")
    css, images = EPUB_CSS, {}
    if intro:
        intro_css, intro_body, images = intro
        css += intro_css
        intro_body = re.sub(r"<br\s*>", "<br/>", intro_body)
        intro_body = re.sub(r"<img([^>]*?)\s*/?>", r"<img\1/>", intro_body)
        files = [("intro", xhtml(title, '<div class="intro">%s</div>' % intro_body))]
    else:
        cover = ('<div class="cover"><h1>%s</h1><p>%s</p><p>%s</p></div>'
                 % (html.escape(title), html.escape(cfg.get("subtitle", "")), html.escape(author)))
        files = [("cover", xhtml(title, cover))]
    nav = []
    for i, (t, body) in enumerate(docs, 1):
        name = "s%03d" % i
        files.append((name, xhtml(t or title, body)))
        nav.append('<li><a href="%s.xhtml">%s</a></li>' % (name, inline(t or title)))
    files.insert(1, ("nav", xhtml("विषय-सूची", '<nav epub:type="toc" id="toc"><h1>विषय-सूची</h1>'
                                  '<ol>%s</ol></nav>' % "".join(nav))))
    manifest = "".join('<item id="%s" href="%s.xhtml" media-type="application/xhtml+xml"%s/>'
                       % (n, n, ' properties="nav"' if n == "nav" else "") for n, _ in files)
    manifest += "".join('<item id="img%d" href="%s" media-type="image/%s"/>'
                        % (i, name, "png" if name.endswith(".png") else "jpeg")
                        for i, name in enumerate(images))
    opf = """<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="hi">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">urn:uuid:%s</dc:identifier><dc:title>%s</dc:title><dc:creator>%s</dc:creator>
<dc:language>hi</dc:language><meta property="dcterms:modified">%s</meta></metadata>
<manifest><item id="css" href="style.css" media-type="text/css"/>%s</manifest>
<spine>%s</spine></package>""" % (
        uuid.uuid5(uuid.NAMESPACE_URL, "antaryog/book/" + book_name), html.escape(title),
        html.escape(author), datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), manifest,
        "".join('<itemref idref="%s"/>' % n for n, _ in files))
    container = ('<?xml version="1.0"?><container version="1.0" '
                 'xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles>'
                 '<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
                 '</rootfiles></container>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container)
        z.writestr("OEBPS/style.css", css)
        z.writestr("OEBPS/content.opf", opf)
        for name, data in files:
            z.writestr("OEBPS/%s.xhtml" % name, data)
        for name, src in images.items():
            z.write(src, "OEBPS/" + name)


def build(book):
    book = Path(book).resolve()
    cfg = json.loads((book / "book.json").read_text(encoding="utf-8"))
    cfg.setdefault("font", FONT)
    parts = {int(k): v for k, v in cfg.get("parts", {}).items()}
    files = sorted((book / "chapters").glob("[0-9][0-9]_chapter.txt"))
    if not files:
        sys.exit("no chapters in %s" % (book / "chapters"))
    front = matter(book / "front_matter.txt", "front")
    toc = []
    body = ['<section class="chapter">%s</section>' % h for _, h in front]
    docs = list(front)
    for f in files:
        n = int(f.name[:2])
        if n in parts:
            toc.append('<div class="part">%s</div>' % html.escape(parts[n]))
            body.append('<div class="partpage">%s</div>' % html.escape(parts[n]))
            docs.append((parts[n], '<h1 class="part">%s</h1>' % html.escape(parts[n])))
        anchor = "ch%02d" % n
        title, text = chapter_html(f.read_text(encoding="utf-8").splitlines(), anchor)
        toc.append('<div class="ch"><a href="#%s">%s</a></div>' % (anchor, inline(title)))
        body.append('<section class="chapter">%s</section>' % text)
        docs.append((title, text))
    back = matter(book / "back_matter.txt", "back")
    body += ['<section class="chapter">%s</section>' % h for _, h in back]
    docs += back
    title = cfg.get("title") or book.name
    intro = load_intro(book)
    if intro:
        css = CSS % cfg + intro[0] + "\n.intro { page: intro; page-break-after: always; }\n"
        opening = '<div class="intro">%s</div>' % re.sub(r'src="([^":/]+)"', r'src="../intro/\1"', intro[1])
    else:
        css = CSS % cfg
        opening = '<div class="cover"><h1>%s</h1><div class="sub">%s</div><div class="author">%s</div></div>' % (
            html.escape(title), html.escape(cfg.get("subtitle", "")), html.escape(cfg.get("author", "")))
    doc = """<!doctype html><html lang="hi"><head><meta charset="utf-8">
<title>%s</title><style>%s</style></head><body>
%s
<div class="toc"><h2>विषय-सूची</h2>%s</div>
%s
</body></html>""" % (html.escape(title), css, opening, "\n".join(toc), "\n".join(body))
    out = book / "book"
    out.mkdir(exist_ok=True)
    page, pdf = out / (book.name + ".html"), out / (book.name + ".pdf")
    page.write_text(doc, encoding="utf-8")
    subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=%s" % pdf, page.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    epub = out / (book.name + ".epub")
    write_epub(epub, book.name, cfg, title, docs, intro)
    print("%d chapters -> %s, %s" % (len(files), pdf, epub))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
