#!/usr/bin/env python3
"""Convert a chapter in simple Markdown to a self-contained styled HTML page.

Usage: md_to_html.py <chapter.txt> <output.html>
"""
import html
import os
import re
import sys

FONTS = ('https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@400;600;700'
         '&family=Noto+Serif:ital,wght@0,400;0,600;1,400&display=block')
NUMBERED = re.compile(r'^[०-९0-9]+\. ')


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)


def convert(lines):
    out, title, i = [], 'Chapter', 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('# '):
            title = line[2:]
            if ':' in title:
                label, name = title.split(':', 1)
                out.append(f'<header><div class="label">{inline(label)}</div>'
                           f'<h1>{inline(name.strip())}</h1><div class="orn">❖</div></header>')
            else:
                out.append(f'<header><h1>{inline(title)}</h1><div class="orn">❖</div></header>')
        elif line.startswith('## '):
            out.append(f'<h2>{inline(line[3:])}</h2>')
        elif line.startswith('### '):
            out.append(f'<h3>{inline(line[4:])}</h3>')
        elif line.startswith('>'):
            block = []
            while i < len(lines) and lines[i].startswith('>'):
                block.append(lines[i].lstrip('>').strip())
                i += 1
            paras, cur = [], []
            for b in block:
                if b:
                    cur.append(inline(b))
                elif cur:
                    paras.append(cur)
                    cur = []
            if cur:
                paras.append(cur)
            # A quote whose first line is bold is treated as a scripture verse
            cls = ' class="verse"' if block[0].startswith('**') else ''
            out.append(f'<blockquote{cls}>' + ''.join('<p>' + '<br>'.join(p) + '</p>' for p in paras) + '</blockquote>')
            continue
        elif line.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(f'<li>{inline(lines[i][2:])}</li>')
                i += 1
            out.append('<ul>' + ''.join(items) + '</ul>')
            continue
        elif NUMBERED.match(line):
            items = []
            while i < len(lines) and NUMBERED.match(lines[i]):
                num, txt = lines[i].split('. ', 1)
                items.append(f'<li><span class="num">{num}</span><div>{inline(txt)}</div></li>')
                i += 1
            out.append('<ol class="takeaways">' + ''.join(items) + '</ol>')
            continue
        elif line.strip():
            out.append(f'<p>{inline(line)}</p>')
        i += 1
    return title, ''.join(out)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]
    text = open(src, encoding='utf-8').read()
    title, body = convert(text.splitlines())
    lang = 'hi' if re.search(r'[ऀ-ॿ]', text) else 'en'
    css = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chapter.css'), encoding='utf-8').read()
    page = f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<style>{css}</style></head>
<body>{body}</body></html>
'''
    open(dst, 'w', encoding='utf-8').write(page)


if __name__ == '__main__':
    main()
