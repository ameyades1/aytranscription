#!/usr/bin/env python3
"""Build one talk's upload zip for the WordPress Markdown importer plugin (wordpress-plugin/).

Usage: python3 tools/make_post_zip.py <talk> [output dir] [--lang en|hi]

Builds the English post by default; --lang hi builds the Hindi one from the Hindi text and seo.json's
Hindi fields (slug, title, keywords, tags, alt text, captions, link phrases, category name), with
links and "Also read" pointing to the linked talks' Hindi posts.

Reads (never writes) output/<talk>/: <talk>_blog_seo_en.txt (the SEO-fixed text from /seo_blog_fix)
or else <talk>_blog_en.txt (for Hindi, _blog_seo.txt or else _blog.txt), blog/seo.json, blog/images.txt, blog/index.html (for the video) and
blog/assets/. Writes <slug>.zip, holding <slug>.md and assets/hero.jpg and assets/inline.jpg, to the
output dir (default: your Windows Downloads folder, else the current directory). The .md has:
  - front matter: title (the H1), slug, excerpt and meta description, category (English name from
    gallery_topics.txt), tags, SEO title, focus keyword, and the hero with its alt text and caption
  - the body, with each link phrase from seo.json linked to /<slug of the linked talk>/, the inline
    image at the end of its section (images.txt), an "Also read:" line after its section, and the
    YouTube video under "Watch the Discourse"
Uploading the zip again with "update" ticked replaces a pending or draft post's text and SEO; the
importer reuses images it already has.
"""
import argparse
import glob
import json
import os
import re
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = f'{REPO}/output'


def blog_path(talk, lang='en', original=False):
    """The SEO-fixed text if /seo_blog_fix has written one (and original is False), else the original."""
    suffix = '_en' if lang == 'en' else ''
    fixed = f'{OUT}/{talk}/{talk}_blog_seo{suffix}.txt'
    return fixed if os.path.exists(fixed) and not original else f'{OUT}/{talk}/{talk}_blog{suffix}.txt'


def h1(talk, lang='en'):
    return open(blog_path(talk, lang), encoding='utf-8').readline().lstrip('# ').strip()


def seo_of(talk):
    path = f'{OUT}/{talk}/blog/seo.json'
    return json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def post_slug(talk, lang='en'):
    """The slug the talk's post gets: seo.json's, else the English H1's (as ~/wordpress/import_post.py);
    a Hindi post without one gets the English H1's with -hi, since a Devanagari H1 gives no Latin slug."""
    slug = seo_of(talk).get('wordpress', {}).get(lang, {}).get('slug')
    return slug or slugify(h1(talk)) + ('-hi' if lang == 'hi' else '')


def h2s(talk, lang, original=False):
    return [l[3:].strip() for l in open(blog_path(talk, lang, original), encoding='utf-8') if l.startswith('## ')]


def section_index(talk, en, hi, original):
    """Which ## section (0-based) a heading names, by its English text, else by the Hindi one's position."""
    en_heads, hi_heads = h2s(talk, 'en', original), h2s(talk, 'hi', original)
    if en in en_heads:
        return en_heads.index(en)
    return hi_heads.index(hi) if hi in hi_heads else None


def category_name(key, lang='en'):
    for line in open(f'{REPO}/gallery_topics.txt', encoding='utf-8'):
        if line.startswith(f'topic {key} '):
            return line.split('|')[1 if lang == 'en' else 2].strip()
    return key


def video(talk):
    """(YouTube URL, its title) from the talk's blog page, or None."""
    page = f'{OUT}/{talk}/blog/index.html'
    if not os.path.exists(page):
        return None
    text = open(page, encoding='utf-8').read()
    m = re.search(r'youtube\.com/watch\?v=([A-Za-z0-9_-]{11})', text)
    if not m:
        return None
    cap = re.search(r'<div class="caption">([^<]+)<small>', text)
    return f'https://www.youtube.com/watch?v={m.group(1)}', cap.group(1).strip() if cap else ''


def q(text):
    """A double-quoted front-matter value."""
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'


def md_text(text):
    """Text safe inside a Markdown link's [...] or an image's alt."""
    return text.replace('[', '(').replace(']', ')')


LABELS = {'en': {'also_read': 'Also read', 'video': 'Watch the Discourse'},
          'hi': {'also_read': 'यह भी पढ़ें', 'video': 'प्रवचन देखें'}}


def build(talk, lang='en'):
    """Returns (slug, Markdown text, {path in zip: file})."""
    seo = seo_of(talk)
    if lang not in seo.get('wordpress', {}):
        sys.exit(f'{talk}: seo.json has no wordpress.{lang} section')
    w = seo['wordpress'][lang]
    slug = post_slug(talk, lang)
    lines = open(blog_path(talk, lang), encoding='utf-8').read().splitlines()
    title = lines[0].lstrip('# ').strip()
    links = [(l[lang], f'/{post_slug(l["talk"], lang)}/') for l in seo.get('links', []) if l.get(lang)]
    files = {}

    # what goes at the end of each section, by section index
    after = {}
    imgs = f'{OUT}/{talk}/blog/images.txt'
    if os.path.exists(imgs):
        for line in open(imgs, encoding='utf-8'):
            if not line.strip() or line.startswith('#'):
                continue
            f, hi, en, desc = (p.strip() for p in line.split('|'))
            i = section_index(talk, en, hi, original=True)  # images.txt names the original headings
            src = f'{OUT}/{talk}/blog/assets/{f}'
            if i is None or not os.path.exists(src):
                print(f'Note: no place for {f}', file=sys.stderr)
                continue
            alt = seo.get('alt', {}).get(f, {}).get(lang, desc)
            cap = seo.get('caption', {}).get(f, {}).get(lang, '')
            files[f'assets/{f}'] = src
            after.setdefault(i, []).append(f'![{md_text(alt)}](assets/{f}' + (f' {q(cap)})' if cap else ')'))
    also = seo.get('also_read')
    if also:
        i = section_index(talk, also['after'].get('en'), also['after'].get('hi'), original=False)
        if i is None:
            print(f'Note: no place for the Also read box', file=sys.stderr)
        else:
            after.setdefault(i, []).append(f'{LABELS[lang]["also_read"]}: [{md_text(h1(also["talk"], lang))}]'
                                           f'(/{post_slug(also["talk"], lang)}/)')

    body, section = [], -1

    def close_section():
        for item in after.get(section, []):
            while body and not body[-1].strip():
                body.pop()
            body.extend(['', item, ''])

    for line in lines[1:]:
        if line.startswith('## '):
            close_section()
            section += 1
        elif line.strip() and not line.startswith('>'):
            for phrase, href in list(links):  # the first occurrence of each phrase, as import_post.py
                if phrase in line:
                    line = line.replace(phrase, f'[{phrase}]({href})', 1)
                    links.remove((phrase, href))
        body.append(line)
    close_section()
    for phrase, _ in links:
        print(f"Note: link phrase '{phrase}' not found", file=sys.stderr)
    vid = video(talk)
    if vid:
        url, vtitle = vid
        body += ['', f'## {LABELS[lang]["video"]}', '', f'[{md_text(vtitle)}]({url})' if vtitle else url]

    front = ['---', f'title: {q(title)}', f'slug: {q(slug)}', f'excerpt: {q(w["meta_description"])}',
             'categories:', f'  - {category_name(w.get("category") or seo["wordpress"]["category"], lang)}', 'tags:']
    front += [f'  - {t}' for t in w.get('tags', [])]
    front += [f'seo_title: {q(seo.get("title", {}).get(lang, title))}',
              f'meta_description: {q(w["meta_description"])}',
              f'focus_keyword: {q(w.get("focus_keyword", ""))}',
              'robots: "index,follow"']
    hero = f'{OUT}/{talk}/blog/assets/hero.jpg'
    if os.path.exists(hero):
        files['assets/hero.jpg'] = hero
        front += ['featured_image: "assets/hero.jpg"',
                  f'featured_image_alt: {q(seo.get("alt", {}).get("hero.jpg", {}).get(lang, title))}',
                  f'featured_image_caption: {q(seo.get("caption", {}).get("hero.jpg", {}).get(lang, ""))}']
    front.append('---')
    text = '\n'.join(front) + '\n\n' + re.sub(r'\n{3,}', '\n\n', '\n'.join(body)).strip() + '\n'
    return slug, text, files


def downloads():
    for d in [f'/mnt/c/Users/{os.environ.get("USER", "")}/Downloads'] + sorted(glob.glob('/mnt/c/Users/*/Downloads')):
        if '/Public/' not in d and '/Default' not in d and os.access(d, os.W_OK):
            return d
    return os.getcwd()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('talk')
    ap.add_argument('out', nargs='?', help='output dir (default: your Windows Downloads folder)')
    ap.add_argument('--lang', choices=['en', 'hi'], default='en', help='the post\'s language (default: en)')
    args = ap.parse_args()
    talk = args.talk.rstrip('/').split('/')[-1]
    out = args.out or downloads()
    slug, text, files = build(talk, args.lang)
    path = os.path.join(out, f'{slug}.zip')
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(f'{slug}.md', text)
        for arc, src in files.items():
            z.write(src, arc)
    print(path)


if __name__ == '__main__':
    main()
