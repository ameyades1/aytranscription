#!/usr/bin/env python3
"""Build the blog gallery: one landing page listing every blog in output/.

Usage: gallery_page.py [--output DIR] [--topics FILE]

  --output   Folder holding one subfolder per talk (default: output/ in the repo)
  --topics   Topic definitions and assignments (default: gallery_topics.txt in the repo)

Writes <output>/index.html. Each talk with <name>/blog/index.html gets a card with its video
thumbnail, title, topic, read time and one quote from the blog text (or the chapter), in Hindi and English with a
language switch (#hi / #en opens one directly). Search and topic chips filter the cards.
"""
import argparse
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_page import (HERE, SITE, TEXT, esc, local_digits, read_minutes,  # noqa: E402
                       site_footer, site_header)
from md_to_html import FONTS  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))

UI = {
    'hi': {
        'label': 'ज्ञान-संग्रह', 'h1': 'प्रवचनों से अध्याय',
        'sub': '{author} के प्रवचनों पर आधारित {n} अध्याय, हिन्दी और English में, मूल वीडियो के साथ।',
        'search': 'खोजें…', 'all': 'सभी', 'other': 'अन्य', 'read': '{m} मिनट में पढ़ें',
        'empty': 'इस खोज से कोई अध्याय नहीं मिला।', 'title': 'प्रवचनों से अध्याय',
    },
    'en': {
        'label': 'The Wisdom Library', 'h1': 'Chapters from the Discourses',
        'sub': '{n} chapters based on the discourses of {author}, in Hindi and English, with the original video.',
        'search': 'Search…', 'all': 'All', 'other': 'Other', 'read': '{m} min read',
        'empty': 'No chapters match this search.', 'title': 'Chapters from the Discourses',
    },
}

GALLERY_CSS = """
.hero .sub { max-width: 40rem; margin: .4rem auto 0; color: var(--muted); line-height: 1.7; }
.tools { position: sticky; top: 4.5rem; z-index: 5; background: rgba(255,253,249,.96); backdrop-filter: blur(6px);
         border-bottom: 1px solid var(--rule); }
.tools .wrap { display: flex; flex-direction: column; gap: .8rem; padding-block: 1rem; }
.search { width: 100%; max-width: 28rem; margin: 0 auto; font: inherit; font-size: 1rem; padding: .7rem 1.1rem;
          border: 1px solid var(--rule); border-radius: 999px; background: #fff; color: var(--ink); }
.search:focus { outline: 2px solid var(--gold); outline-offset: 1px; }
.chips { display: flex; gap: .5rem; flex-wrap: wrap; justify-content: center; }
.chip { font: inherit; font-size: .85rem; font-weight: 500; padding: .4rem .9rem; border-radius: 999px; cursor: pointer;
        border: 1px solid var(--rule); background: #fff; color: var(--ink-strong); white-space: nowrap; }
.chip:hover { border-color: var(--gold); }
.chip[aria-pressed="true"] { background: var(--brown); border-color: var(--brown); color: #fff; }
.chip small { opacity: .7; margin-left: .25rem; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(16.5rem, 1fr)); gap: 1.5rem; padding-block: 2.5rem 3.5rem; }
.tile { display: flex; flex-direction: column; background: #fff; border: 1px solid var(--rule); border-radius: 14px;
        overflow: hidden; text-decoration: none; transition: box-shadow .2s, transform .2s; }
.tile:hover { box-shadow: 0 10px 28px rgba(46,33,24,.12); transform: translateY(-2px); }
.tile:focus-visible { outline: 3px solid var(--gold); outline-offset: 2px; }
.tile .thumb { aspect-ratio: 16 / 9; background: var(--panel); overflow: hidden; }
.tile .thumb img { width: 100%; height: 100%; object-fit: cover; transition: transform .3s; }
.tile:hover .thumb img { transform: scale(1.03); }
.tile .body { display: flex; flex-direction: column; gap: .55rem; padding: 1rem 1.15rem 1.15rem; flex: 1; }
.tile .topic { font-size: .75rem; font-weight: 600; letter-spacing: .04em; color: var(--accent); }
.tile h3 { margin: 0; font-family: var(--serif); font-size: 1.15rem; line-height: 1.5; color: var(--ink-strong); }
.tile .quote { margin: 0; font-family: var(--serif); font-size: .93rem; line-height: 1.7; color: var(--muted);
               border-left: 2px solid var(--gold); padding-left: .7rem;
               display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.tile .meta { margin-top: auto; padding-top: .3rem; font-size: .8rem; color: var(--muted); }
.empty { text-align: center; color: var(--muted); padding: 3rem 0 4rem; }
html[lang="hi"] [data-l="en"], html[lang="en"] [data-l="hi"] { display: none; }
@media (max-width: 820px) { .tools { top: 4.5rem; } }
@media (max-width: 560px) {
  .tools .wrap { padding-block: .8rem; }
  .chips { flex-wrap: nowrap; justify-content: flex-start; overflow-x: auto; margin-inline: -1.25rem; padding-inline: 1.25rem;
           scrollbar-width: none; }
  .chips::-webkit-scrollbar { display: none; }
  .grid { gap: 1.1rem; padding-block: 1.5rem 2.5rem; }
}
"""

GALLERY_JS = """
(function () {
  var root = document.documentElement, tiles = [].slice.call(document.querySelectorAll('.tile'));
  var search = document.querySelector('.search'), empty = document.querySelector('.empty');
  var topic = 'all';
  function setLang(lang) {
    root.lang = lang;
    document.title = root.dataset['title' + lang];
    search.placeholder = search.dataset[lang];
    document.querySelectorAll('.lang-switch [data-switch]').forEach(function (a) {
      a.classList.toggle('active', a.dataset.switch === lang);
    });
    tiles.forEach(function (t) {
      var langs = t.dataset.langs.split(' ');
      t.href = t.dataset.href + '#' + (langs.indexOf(lang) >= 0 ? lang : langs[0]);
    });
  }
  function filter() {
    var q = search.value.trim().toLowerCase(), shown = 0;
    tiles.forEach(function (t) {
      var ok = (topic === 'all' || t.dataset.topic === topic) && (!q || t.dataset.search.indexOf(q) >= 0);
      t.hidden = !ok;
      if (ok) shown++;
    });
    empty.hidden = shown > 0;
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-switch]');
    if (a) {
      e.preventDefault();
      setLang(a.dataset.switch);
      history.replaceState(null, '', '#' + a.dataset.switch);
      return;
    }
    var chip = e.target.closest('.chip');
    if (chip) {
      topic = chip.dataset.topic;
      document.querySelectorAll('.chip').forEach(function (c) { c.setAttribute('aria-pressed', c === chip); });
      filter();
    }
  });
  search.addEventListener('input', filter);
  var hash = location.hash.slice(1);
  setLang(hash === 'en' || hash === 'hi' ? hash : root.lang);
})();
"""


def read_topics(path):
    """Topic list [(key, en, hi)] and {talk name: key} from the topics file."""
    topics, assign = [], {}
    if not os.path.exists(path):
        return topics, assign
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('topic '):
            key, en, hi = (p.strip() for p in line[6:].split('|'))
            topics.append((key, en, hi))
        else:
            name, key = line.split()
            assign[name] = key
    return topics, assign


def plain(t):
    return re.sub(r'\*+', '', t).strip()


def chapter_info(path):
    text = open(path, encoding='utf-8').read()
    lang = 'hi' if re.search(r'[ऀ-ॿ]', text) else 'en'
    m = re.search(r'^# (.+)$', text, re.M)
    title = plain(m.group(1).split(':', 1)[-1]) if m else ''
    quotes = [plain(q).strip('"“”') for q in re.findall(r'^> "(.+)"\s*$', text, re.M)]
    return lang, {'title': title, 'quotes': quotes, 'minutes': read_minutes(text, lang)}


def pick_quote(quotes):
    """Index of the first quote of a readable card length, else 0."""
    for i, q in enumerate(quotes):
        if 50 <= len(q) <= 220:
            return i
    return 0


def collect(out_dir, assign):
    talks = []
    for name in sorted(os.listdir(out_dir)):
        folder = os.path.join(out_dir, name)
        if not os.path.isfile(os.path.join(folder, 'blog', 'index.html')):
            continue
        # The blog text when there is one, else the book chapter
        kind = 'blog' if os.path.exists(os.path.join(folder, f'{name}_blog.txt')) else 'chapter'
        langs = {}
        for f in sorted(os.listdir(folder)):
            if re.fullmatch(re.escape(name) + rf'_{kind}(_en|_hi)?\.txt', f):
                lang, info = chapter_info(os.path.join(folder, f))
                langs.setdefault(lang, info)
        if not langs:
            continue
        main = os.path.join(folder, f'{name}_{kind}.txt')
        primary = next(iter(langs)) if not os.path.exists(main) else chapter_info(main)[0]
        assets = os.path.join(folder, 'blog', 'assets')
        thumbs = [f for f in os.listdir(assets) if f.endswith('.jpg') and f not in ('acharya-ji.jpg', 'hero.jpg', 'inline.jpg')] if os.path.isdir(assets) else []
        hero = next((f for f in ('hero.jpg', 'hero.png') if os.path.exists(os.path.join(assets, f))), None)
        qi = pick_quote(langs[primary]['quotes'])
        for info in langs.values():
            info['quote'] = info['quotes'][qi] if qi < len(info['quotes']) else (info['quotes'] or [''])[0]
        talks.append({
            'name': name, 'langs': [primary] + [l for l in langs if l != primary], 'text': langs,
            'topic': assign.get(name, 'other'),
            'thumb': f'{name}/blog/assets/{hero}' if hero else f'{name}/blog/assets/{thumbs[0]}' if thumbs else '',
            'mtime': os.path.getmtime(main if os.path.exists(main) else os.path.join(folder, 'blog', 'index.html')),
        })
    talks.sort(key=lambda t: -t['mtime'])
    return talks


def both(values, cls=''):
    """One span per language; CSS shows the one matching <html lang>."""
    c = f' class="{cls}"' if cls else ''
    return ''.join(f'<span data-l="{l}"{c}>{v}</span>' for l, v in values.items())


def tile(t, topic_names):
    text = {l: t['text'].get(l) or t['text'][t['langs'][0]] for l in ('hi', 'en')}
    names = topic_names.get(t['topic'], topic_names['other'])
    search = ' '.join(f"{i['title']} {i['quote']}" for i in t['text'].values()).lower()
    img = f'<img src="{esc(t["thumb"])}" alt="" loading="lazy">' if t['thumb'] else ''
    quote = both({l: esc(f'“{text[l]["quote"]}”') for l in text}) if any(i['quote'] for i in text.values()) else ''
    return (f'<a class="tile" href="{t["name"]}/blog/index.html#{t["langs"][0]}" data-href="{t["name"]}/blog/index.html" '
            f'data-langs="{" ".join(t["langs"])}" data-topic="{t["topic"]}" data-search="{esc(search)}">'
            f'<div class="thumb">{img}</div><div class="body">'
            f'<span class="topic">{both(names)}</span>'
            f'<h3>{both({l: esc(text[l]["title"]) for l in text})}</h3>'
            + (f'<p class="quote">{quote}</p>' if quote else '') +
            f'<div class="meta">{both({l: UI[l]["read"].format(m=local_digits(text[l]["minutes"], l)) for l in text})}</div>'
            f'</div></a>')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--output', default=os.path.join(REPO, 'output'))
    ap.add_argument('--topics', default=os.path.join(REPO, 'gallery_topics.txt'))
    a = ap.parse_args()

    topics, assign = read_topics(a.topics)
    talks = collect(a.output, assign)
    topic_names = {k: {'hi': esc(hi), 'en': esc(en)} for k, en, hi in topics}
    topic_names['other'] = {l: UI[l]['other'] for l in UI}

    counts = {}
    for t in talks:
        counts[t['topic']] = counts.get(t['topic'], 0) + 1
    chip = lambda key, label, n, on=False: (  # noqa: E731
        f'<button class="chip" type="button" data-topic="{key}" aria-pressed="{"true" if on else "false"}">'
        + both({l: f'{label[l]}<small>{local_digits(n, l)}</small>' for l in label}) + '</button>')
    chips = chip('all', {l: UI[l]['all'] for l in UI}, len(talks), True) + ''.join(
        chip(k, topic_names[k], counts[k]) for k in [*(k for k, _, _ in topics), 'other'] if counts.get(k))

    assets = os.path.join(a.output, 'assets')
    os.makedirs(assets, exist_ok=True)
    shutil.copy2(os.path.join(HERE, 'assets', 'logo.png'), assets)

    n = {l: local_digits(len(talks), l) for l in UI}
    author = {l: TEXT[l]['author'] for l in UI}
    switch = ('<div class="lang-switch"><a href="#hi" data-switch="hi" class="active">हिन्दी</a>'
              '<a href="#en" data-switch="en">English</a></div>')
    css = open(os.path.join(HERE, 'blog.css'), encoding='utf-8').read() + GALLERY_CSS

    page = f'''<!doctype html>
<html lang="hi" data-titlehi="{UI['hi']['title']} | Antar Yog Foundation" data-titleen="{UI['en']['title']} | Antar Yog Foundation">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{UI['hi']['title']} | Antar Yog Foundation</title>
<meta name="description" content="{esc(UI['en']['sub'].format(n=len(talks), author=author['en']))}">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}&family=Noto+Sans:wght@400;500;600&family=Noto+Sans+Devanagari:wght@400;500;600" rel="stylesheet">
<style>{css}</style>
</head><body>

{site_header(switch)}

<section class="hero"><div class="wrap">
  <div class="crumbs"><a href="{SITE['home']}">Home</a> › <a href="https://blogs.antaryogfoundation.in">Blog</a></div>
  <div class="label">{both({l: UI[l]['label'] for l in UI})}</div>
  <h1>{both({l: UI[l]['h1'] for l in UI})}</h1>
  <div class="orn">❖</div>
  <p class="sub">{both({l: UI[l]['sub'].format(n=n[l], author=author[l]) for l in UI})}</p>
</div></section>

<section class="tools"><div class="wrap">
  <input class="search" type="search" placeholder="{UI['hi']['search']}" data-hi="{UI['hi']['search']}"
         data-en="{UI['en']['search']}" aria-label="Search">
  <div class="chips">{chips}</div>
</div></section>

<main class="wrap">
  <div class="grid">{''.join(tile(t, topic_names) for t in talks)}</div>
  <p class="empty" hidden>{both({l: UI[l]['empty'] for l in UI})}</p>
</main>

{site_footer(TEXT['hi']['motto'])}
<script>{GALLERY_JS}</script>
</body></html>
'''
    out = os.path.join(a.output, 'index.html')
    open(out, 'w', encoding='utf-8').write(page)
    untagged = [t['name'] for t in talks if t['topic'] not in topic_names or t['topic'] == 'other']
    print(f'Gallery: {out} ({len(talks)} blogs)')
    if untagged:
        print(f'Not in {os.path.basename(a.topics)} (shown under Other): {", ".join(untagged)}')


if __name__ == '__main__':
    main()
