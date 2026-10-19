#!/usr/bin/env python3
"""Build the SEO-optimized English blog gallery: output/seo/index.html.

Usage: seo_gallery_page.py [--output DIR] [--topics FILE] [--site URL]

  --output   Folder holding one subfolder per talk and the static WordPress export in wp/
             (default: output/ in the repo)
  --topics   Topic definitions (default: gallery_topics.txt in the repo)
  --site     The published URL of the output folder, for the canonical and Open Graph links
             (default: https://ameyades1.github.io/aytranscription)

Lists every talk whose WordPress post has been exported as a static page (output/wp/<slug>/,
written by ~/wordpress/export_static.sh), with the slug from the talk's blog/seo.json. Each card
uses the SEO fields of seo.json: the title tag, the meta description, the category, the hero
image with its alt text, and links to the static post. The page itself carries a meta description,
a canonical link, Open Graph and Twitter tags, and JSON-LD (CollectionPage with an ItemList of
BlogPosting entries). English only for now.
"""
import argparse
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_page import HERE, TEXT, esc, read_minutes, site_footer, site_header  # noqa: E402
from gallery_page import GALLERY_CSS, read_topics  # noqa: E402
from md_to_html import FONTS  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
TITLE = 'SEO-Optimized Blogs on Sanatan Dharma | Antar Yog Foundation'
H1 = 'Blogs on Sanatan Dharma'
DESC = ('Blogs on Hindu deities, karma, scripture and spiritual practice, based on the discourses '
        'of Brahmrishi Acharya Upendra Ji, optimized for search.')

SEO_CSS = """
.tile .desc { margin: 0; font-size: .92rem; line-height: 1.65; color: var(--muted); }
.tile h2 { margin: 0; font-family: var(--serif); font-size: 1.15rem; line-height: 1.5; color: var(--ink-strong); }
"""

SEO_JS = """
(function () {
  var tiles = [].slice.call(document.querySelectorAll('.tile')), search = document.querySelector('.search');
  var empty = document.querySelector('.empty'), topic = 'all';
  function filter() {
    var q = search.value.trim().toLowerCase(), shown = 0;
    tiles.forEach(function (t) {
      var ok = (topic === 'all' || t.dataset.topic === topic) && (!q || t.dataset.search.indexOf(q) >= 0);
      t.parentNode.hidden = !ok;
      if (ok) shown++;
    });
    empty.hidden = shown > 0;
  }
  document.addEventListener('click', function (e) {
    var chip = e.target.closest('.chip');
    if (!chip) return;
    topic = chip.dataset.topic;
    document.querySelectorAll('.chip').forEach(function (c) { c.setAttribute('aria-pressed', c === chip); });
    filter();
  });
  search.addEventListener('input', filter);
})();
"""


def collect(out_dir):
    """Talks with an exported static WordPress post, newest blog first."""
    talks = []
    for name in sorted(os.listdir(out_dir)):
        path = os.path.join(out_dir, name, 'blog', 'seo.json')
        if not os.path.isfile(path):
            continue
        seo = json.load(open(path, encoding='utf-8'))
        en = seo.get('wordpress', {}).get('en', {})
        slug = en.get('slug')
        if not slug or not os.path.isfile(os.path.join(out_dir, 'wp', slug, 'index.html')):
            continue
        text = next((os.path.join(out_dir, name, f'{name}_blog{s}_en.txt') for s in ('_seo', '')
                     if os.path.exists(os.path.join(out_dir, name, f'{name}_blog{s}_en.txt'))), None)
        hero = os.path.join(out_dir, name, 'blog', 'assets', 'hero.jpg')
        talks.append({
            'name': name, 'slug': slug, 'title': seo['title']['en'], 'desc': en.get('meta_description', ''),
            'topic': seo['wordpress'].get('category', 'other'), 'keyword': en.get('focus_keyword', ''),
            'img': f'../{name}/blog/assets/hero.jpg' if os.path.exists(hero) else '',
            'alt': seo.get('alt', {}).get('hero.jpg', {}).get('en', ''),
            'minutes': read_minutes(open(text, encoding='utf-8').read(), 'en') if text else 0,
            'mtime': os.path.getmtime(path),
        })
    talks.sort(key=lambda t: -t['mtime'])
    return talks


def tile(t, topic_names):
    search = f"{t['title']} {t['desc']} {t['keyword']}".lower()
    img = (f'<img src="{esc(t["img"])}" alt="{esc(t["alt"])}" width="640" height="360" loading="lazy">'
           if t['img'] else '')
    return (f'<article><a class="tile" href="../wp/{t["slug"]}/index.html" data-topic="{t["topic"]}" '
            f'data-search="{esc(search)}"><div class="thumb">{img}</div><div class="body">'
            f'<span class="topic">{topic_names.get(t["topic"], "Other")}</span>'
            f'<h2>{esc(t["title"])}</h2><p class="desc">{esc(t["desc"])}</p>'
            f'<div class="meta">{t["minutes"]} min read</div></div></a></article>')


def json_ld(talks, site, topic_names):
    page = f'{site}/seo/'
    items = [{
        '@type': 'ListItem', 'position': i + 1,
        'item': {
            '@type': 'BlogPosting', 'headline': t['title'], 'description': t['desc'],
            'url': f'{site}/wp/{t["slug"]}/', 'inLanguage': 'en', 'keywords': t['keyword'],
            'articleSection': topic_names.get(t['topic'], 'Other'),
            **({'image': f'{site}/{t["name"]}/blog/assets/hero.jpg'} if t['img'] else {}),
            'author': {'@type': 'Person', 'name': TEXT['en']['author']},
        },
    } for i, t in enumerate(talks)]
    data = {
        '@context': 'https://schema.org', '@type': 'CollectionPage', 'name': H1, 'description': DESC,
        'url': page, 'inLanguage': 'en',
        'publisher': {'@type': 'Organization', 'name': 'Antar Yog Foundation', 'url': 'https://antaryogfoundation.in'},
        'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(talks), 'itemListElement': items},
    }
    return json.dumps(data, ensure_ascii=False, indent=1).replace('</', '<\\/')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--output', default=os.path.join(REPO, 'output'))
    ap.add_argument('--topics', default=os.path.join(REPO, 'gallery_topics.txt'))
    ap.add_argument('--site', default='https://ameyades1.github.io/aytranscription')
    a = ap.parse_args()

    topics, _ = read_topics(a.topics)
    topic_names = {k: esc(en) for k, en, _ in topics}
    talks = collect(a.output)

    counts = {}
    for t in talks:
        counts[t['topic']] = counts.get(t['topic'], 0) + 1
    chip = lambda key, label, n, on=False: (  # noqa: E731
        f'<button class="chip" type="button" data-topic="{key}" aria-pressed="{"true" if on else "false"}">'
        f'{label}<small>{n}</small></button>')
    chips = chip('all', 'All', len(talks), True) + ''.join(
        chip(k, topic_names[k], counts[k]) for k, _, _ in topics if counts.get(k))

    folder = os.path.join(a.output, 'seo')
    os.makedirs(os.path.join(folder, 'assets'), exist_ok=True)
    shutil.copy2(os.path.join(HERE, 'assets', 'logo.png'), os.path.join(folder, 'assets'))
    css = open(os.path.join(HERE, 'blog.css'), encoding='utf-8').read() + GALLERY_CSS + SEO_CSS
    page_url = f'{a.site}/seo/'
    image = next((f'{a.site}/{t["name"]}/blog/assets/hero.jpg' for t in talks if t['img']), '')

    page = f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{esc(DESC)}">
<link rel="canonical" href="{page_url}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Antar Yog Foundation">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{esc(DESC)}">
<meta property="og:url" content="{page_url}">
<meta property="og:locale" content="en_IN">
{f'<meta property="og:image" content="{image}">' if image else ''}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{esc(DESC)}">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}&family=Noto+Sans:wght@400;500;600" rel="stylesheet">
<style>{css}</style>
<script type="application/ld+json">
{json_ld(talks, a.site, topic_names)}
</script>
</head><body>

{site_header(blog='../index.html')}

<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="https://antaryogfoundation.in">Home</a> › <a href="../index.html">Blog</a> › SEO-optimized</nav>
  <div class="label">The Wisdom Library</div>
  <h1>{H1}</h1>
  <div class="orn">❖</div>
  <p class="sub">{len(talks)} blog{"s" if len(talks) != 1 else ""} based on the discourses of {TEXT['en']['author']}, written and optimized for search, as they will appear on the website.</p>
</div></section>

<section class="tools"><div class="wrap">
  <input class="search" type="search" placeholder="Search…" aria-label="Search the blogs">
  <div class="chips">{chips}</div>
</div></section>

<main class="wrap">
  <div class="grid">{''.join(tile(t, topic_names) for t in talks)}</div>
  <p class="empty" hidden>No blogs match this search.</p>
</main>

{site_footer(TEXT['en']['motto'], blog='../index.html')}
<script>{SEO_JS}</script>
</body></html>
'''
    out = os.path.join(folder, 'index.html')
    open(out, 'w', encoding='utf-8').write(page)
    print(f'SEO gallery: {out} ({len(talks)} blogs)')


if __name__ == '__main__':
    main()
