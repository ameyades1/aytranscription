#!/usr/bin/env python3
"""A talk's text diagram, from output/<talk>/blog/diagram.json.

The diagram is text, not an image: boxes and lists styled by the .ay-diagram rules (in
tools/template/blog.css for the blog pages, and printed by the importer plugin on WordPress).
- blog_page.py puts html(spec, lang) at the end of the spec's section;
- make_post_zip.py puts markdown(spec, lang) there: ::: fences that the importer plugin turns into
  native WordPress blocks (Group, Columns, Column, Paragraph, List) with the same class names, so a
  reviewer can edit the text in the block editor.
Both have the same structure, so one stylesheet fits both.

Usage: python3 tools/diagram.py <talk> [hi|en]   prints the Markdown (to check a spec)

The spec; every text is {"hi": ..., "en": ...}, taken from the blog itself (never anything the
talk does not say); "note", "sub", "footer" and "vs" are optional; there is no caption:
  {"type": "combine" | "compare" | "triad",
   "section": {hi, en}   the ORIGINAL blog's ## heading the diagram goes after (as in images.txt),
   "title": {hi, en}, "footer": {hi, en}   (one closing line; only when it adds what the boxes do not say),
   combine: "parts": [{"label", "note"}, {"label", "note"}], "result": {"label", "note"}
   compare: "columns": [{"label", "note", "items": [...]}, {...}], "vs": true (an "or" between them)
   triad:   "items": [{"label", "note", "sub", "color": "white|red|black"}, x3]}

Structure (Markdown fence = HTML element):
  ::: ay-diagram ay-<type>              <div class="wp-block-group ay-diagram ay-<type>">
    **title**                             <p><strong>title</strong></p>
    ::: columns                           <div class="wp-block-columns">
      ::: column ay-box [c-<color>]         <div class="wp-block-column ay-box ...">
        **label** / note / sub / - items      <p>, <p>, <p>, <ul>
    ::: ay-result (combine)               <div class="wp-block-group ay-result">
    ::: ay-footer                         <div class="wp-block-group ay-footer"><p>
"""
import html as H
import json
import os
import sys

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')


def load(talk):
    """The talk's spec, or None."""
    path = os.path.join(OUT, talk, 'blog', 'diagram.json')
    return json.load(open(path, encoding='utf-8')) if os.path.exists(path) else None


def tree(spec, lang):
    """The diagram as nested (kind, classes, children) nodes: kinds group, columns, column,
    p (text, bold?), ul (items)."""
    t = lambda v: v[lang] if isinstance(v, dict) else v

    def box(n, cls='ay-box'):
        kids = [('p', '', (t(n['label']), True))]
        if n.get('note'):
            kids.append(('p', '', (t(n['note']), False)))
        if n.get('sub'):
            kids.append(('p', '', (t(n['sub']), False)))
        if n.get('items'):
            kids.append(('ul', '', [t(x) for x in n['items']]))
        return kids

    k = spec['type']
    kids = [('p', '', (t(spec['title']), True))]
    if k == 'combine':
        kids.append(('columns', '', [('column', 'ay-box', box(n)) for n in spec['parts']]))
        kids.append(('group', 'ay-result', box(spec['result'])))
    elif k == 'compare':
        cols = [('column', 'ay-box' + (' ay-alt' if i else ''), box(c)) for i, c in enumerate(spec['columns'])]
        if spec.get('vs'):
            cols.insert(1, ('column', 'ay-vs', [('p', '', ('या' if lang == 'hi' else 'or', False))]))
        kids.append(('columns', '', cols))
    elif k == 'triad':
        kids.append(('columns', '', [('column', f'ay-box c-{n["color"]}' if n.get('color') else 'ay-box', box(n))
                                      for n in spec['items']]))
    else:
        sys.exit(f'unknown diagram type {k}')
    if spec.get('footer'):
        kids.append(('group', 'ay-footer', [('p', '', (t(spec['footer']), False))]))
    return ('group', f'ay-diagram ay-{k}', kids)


def html(spec, lang):
    def out(node):
        kind, cls, kids = node
        if kind == 'p':
            text, bold = kids
            return f'<p><strong>{H.escape(text)}</strong></p>' if bold else f'<p>{H.escape(text)}</p>'
        if kind == 'ul':
            return '<ul>' + ''.join(f'<li>{H.escape(x)}</li>' for x in kids) + '</ul>'
        base = {'group': 'wp-block-group', 'columns': 'wp-block-columns', 'column': 'wp-block-column'}[kind]
        return f'<div class="{base}{" " + cls if cls else ""}">' + ''.join(out(c) for c in kids) + '</div>'
    return out(tree(spec, lang))


def markdown(spec, lang):
    md = lambda s: s.replace('*', '\\*')
    lines = []

    def out(node):
        kind, cls, kids = node
        if kind == 'p':
            text, bold = kids
            lines.extend([f'**{md(text)}**' if bold else md(text), ''])
        elif kind == 'ul':
            lines.extend([f'- {md(x)}' for x in kids] + [''])
        else:
            name = {'group': '', 'columns': 'columns', 'column': 'column'}[kind]
            lines.extend([f'::: {" ".join(x for x in (name, cls) if x)}', ''])
            for c in kids:
                out(c)
            lines.extend([':::', ''])
    out(tree(spec, lang))
    return '\n'.join(lines).rstrip()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    spec = load(sys.argv[1]) or sys.exit(f'{sys.argv[1]}: no blog/diagram.json')
    print(markdown(spec, sys.argv[2] if len(sys.argv) > 2 else 'en'))
