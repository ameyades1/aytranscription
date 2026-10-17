#!/usr/bin/env python3
"""Check each talk's SEO files written by /seo_blog: tools/seo/<name>.md and output/<name>/blog/seo.json.

Usage: check_seo.py [<talk> ...]   (default: every talk that has a seo.json)

Errors make the check fail; warnings are printed but allowed. Exit code 1 if any talk has errors.
Checks:
  - the report exists and its first line is "<name>: SEO report"
  - seo.json has only the allowed keys
  - title tags are given for both languages and are at most 60 characters
  - alt text and captions name images that exist in the talk's blog/assets/
  - every linked talk (links, also_read, related) exists, has a blog page and is not the talk itself
  - every link phrase is in that language's blog text, outside headings, verses and other links
    (as the page generator places them), and every also_read heading exists
  - related has 3 talks
  - the report's section 11 holds a JSON block equal to seo.json
  - wordpress: category is the talk's key in gallery_topics.txt; slugs are lowercase-hyphenated and
    unique across all talks; focus keywords are unique across all talks; no tag repeats a category
    name; focus keyword, 2-4 secondary keywords, meta description
    (English 140-155 characters) and 3-6 tags for each language
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'template'))
from blog_page import esc  # noqa: E402
from md_to_html import convert  # noqa: E402

OUT = os.path.join(ROOT, 'output')
KEYS = {'title', 'alt', 'caption', 'links', 'also_read', 'related', 'wordpress'}
LANGS = ('hi', 'en')
SLUG = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')


def blog_txt(talk, lang):
    return os.path.join(OUT, talk, f'{talk}_blog{"_en" if lang == "en" else ""}.txt')


def has_page(talk):
    return os.path.isfile(os.path.join(OUT, talk, 'blog', 'index.html'))


def read_topics():
    keys, names, assign = set(), set(), {}
    for line in open(os.path.join(ROOT, 'gallery_topics.txt'), encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('topic '):
            parts = [p.strip() for p in line[6:].split('|')]
            keys.add(parts[0])
            names.update(p.casefold() for p in parts)  # key, English and Hindi names
        else:
            name, key = line.split()
            assign[name] = key
    return keys, names, assign


def body_html(talk, lang):
    path = blog_txt(talk, lang)
    return convert(open(path, encoding='utf-8').read().splitlines())[1] if os.path.exists(path) else None


def phrase_linkable(body, phrase):
    """True if the generator would find the phrase in plain text (not in a heading, quote or link)."""
    skip = 0
    for part in re.split(r'(<[^>]+>)', body):
        if part.startswith('<'):
            m = re.match(r'<(/?)(h1|h2|h3|a|blockquote)\b', part)
            if m:
                skip += -1 if m.group(1) else 1
        elif not skip and esc(phrase) in part:
            return True
    return False


def h2s(talk, lang):
    path = blog_txt(talk, lang)
    if not os.path.exists(path):
        return []
    return [re.sub(r'[*_`]', '', l[3:]).strip() for l in open(path, encoding='utf-8') if l.startswith('## ')]


def report_json(text):
    """The JSON block in the report's section 11, or None."""
    m = re.search(r'^## 11\..*?```json\n(.*?)\n```', text, re.S | re.M)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def check(talk, seo, topic_keys, assign, slugs, keywords, category_names):
    err, warn = [], []
    report = os.path.join(ROOT, 'tools', 'seo', f'{talk}.md')
    if not os.path.exists(report):
        err.append(f'no report tools/seo/{talk}.md')
    else:
        text = open(report, encoding='utf-8').read()
        if text.split('\n', 1)[0].strip().replace('\\_', '_') != f'{talk}: SEO report':
            err.append('report first line is not "<name>: SEO report"')
        if report_json(text) != seo:
            err.append('report section 11 has no JSON block equal to seo.json')

    extra = set(seo) - KEYS
    if extra:
        err.append(f'keys not allowed: {", ".join(sorted(extra))}')

    for lang in LANGS:
        t = seo.get('title', {}).get(lang)
        if not t:
            err.append(f'title ({lang}) missing')
        elif len(t) > 60:
            err.append(f'title ({lang}) is {len(t)} characters, over 60')

    assets = os.path.join(OUT, talk, 'blog', 'assets')
    for key in ('alt', 'caption'):
        for f, texts in seo.get(key, {}).items():
            if not os.path.exists(os.path.join(assets, f)):
                err.append(f'{key}: image {f} not in blog/assets/')
            if key == 'caption' and f not in ('hero.jpg', 'hero.png', 'inline.jpg'):
                warn.append(f'caption for {f} is not shown (only hero and inline images have captions)')
            for lang in LANGS:
                if not texts.get(lang):
                    err.append(f'{key}: {f} has no {lang} text')

    def check_talk(t, where):
        if t == talk:
            err.append(f'{where} links the talk to itself')
        elif not has_page(t):
            err.append(f'{where}: talk {t} has no blog page')

    bodies = {lang: body_html(talk, lang) for lang in LANGS}
    for link in seo.get('links', []):
        check_talk(link.get('talk'), 'links')
        for lang in LANGS:
            phrase = link.get(lang)
            if phrase and bodies[lang] is not None and not phrase_linkable(bodies[lang], phrase):
                err.append(f"links: phrase '{phrase}' ({lang}) not found in plain text")
    for lang in LANGS:
        n = sum(1 for l in seo.get('links', []) if l.get(lang))
        if seo.get('links') and not 3 <= n <= 5:
            warn.append(f'links: {n} {lang} links (3 to 5 expected)')

    also = seo.get('also_read')
    if also:
        check_talk(also.get('talk'), 'also_read')
        hi_heads = h2s(talk, 'hi')
        after = also.get('after', {})
        for lang in LANGS:
            heads = h2s(talk, lang)
            if after.get(lang) in heads:
                continue
            if lang == 'en' and after.get('hi') in hi_heads and hi_heads.index(after['hi']) < len(heads):
                warn.append('also_read: English heading not found, the Hindi heading position is used')
            else:
                err.append(f"also_read: heading '{after.get(lang)}' ({lang}) not found")

    related = seo.get('related', [])
    for t in related:
        check_talk(t, 'related')
    if related and len(related) != 3:
        warn.append(f'related has {len(related)} talks (3 expected)')

    wp = seo.get('wordpress')
    if wp is None:
        err.append('wordpress section missing')
        return err, warn
    cat = wp.get('category')
    if cat not in topic_keys:
        err.append(f'wordpress: category {cat!r} is not in gallery_topics.txt')
    elif talk in assign and assign[talk] != cat:
        err.append(f'wordpress: category {cat} differs from gallery_topics.txt ({assign[talk]})')
    elif talk not in assign:
        warn.append(f'talk not in gallery_topics.txt; add: {talk} {cat}')
    for lang in LANGS:
        w = wp.get(lang, {})
        slug = w.get('slug', '')
        if not SLUG.match(slug):
            err.append(f'wordpress {lang}: slug {slug!r} is not lowercase-hyphenated')
        elif slug in slugs:
            err.append(f'wordpress {lang}: slug {slug} also used by {slugs[slug]}')
        else:
            slugs[slug] = f'{talk} ({lang})'
        focus = w.get('focus_keyword', '')
        if not focus:
            err.append(f'wordpress {lang}: focus_keyword missing')
        elif focus.casefold() in keywords:
            err.append(f'wordpress {lang}: focus keyword {focus!r} also used by {keywords[focus.casefold()]}')
        else:
            keywords[focus.casefold()] = f'{talk} ({lang})'
        if not 2 <= len(w.get('secondary_keywords', [])) <= 4:
            err.append(f'wordpress {lang}: {len(w.get("secondary_keywords", []))} secondary keywords (2 to 4)')
        meta = w.get('meta_description', '')
        if not meta:
            err.append(f'wordpress {lang}: meta_description missing')
        elif lang == 'en' and not 140 <= len(meta) <= 155:
            warn.append(f'wordpress en: meta description is {len(meta)} characters (140 to 155)')
        elif lang == 'hi' and len(meta) > 160:
            warn.append(f'wordpress hi: meta description is {len(meta)} characters (over 160)')
        tags = w.get('tags', [])
        if not 3 <= len(tags) <= 6:
            err.append(f'wordpress {lang}: {len(tags)} tags (3 to 6)')
        for tag in tags:
            if tag.casefold() in category_names:
                err.append(f'wordpress {lang}: tag {tag!r} repeats a category name')
    return err, warn


def main():
    talks = sys.argv[1:] or sorted(d for d in os.listdir(OUT) if os.path.isfile(os.path.join(OUT, d, 'blog', 'seo.json')))
    topic_keys, category_names, assign = read_topics()

    # slugs and focus keywords of talks not being checked still count for uniqueness
    slugs, keywords = {}, {}
    for d in sorted(os.listdir(OUT)):
        path = os.path.join(OUT, d, 'blog', 'seo.json')
        if d not in talks and os.path.isfile(path):
            for lang in LANGS:
                w = json.load(open(path, encoding='utf-8')).get('wordpress', {}).get(lang, {})
                if w.get('slug'):
                    slugs[w['slug']] = f'{d} ({lang})'
                if w.get('focus_keyword'):
                    keywords[w['focus_keyword'].casefold()] = f'{d} ({lang})'

    failed = 0
    for talk in talks:
        path = os.path.join(OUT, talk, 'blog', 'seo.json')
        if not os.path.isfile(path):
            print(f'{talk}: FAIL\n  - no output/{talk}/blog/seo.json')
            failed += 1
            continue
        try:
            seo = json.load(open(path, encoding='utf-8'))
        except json.JSONDecodeError as e:
            print(f'{talk}: FAIL\n  - seo.json is not valid JSON ({e})')
            failed += 1
            continue
        err, warn = check(talk, seo, topic_keys, assign, slugs, keywords, category_names)
        if err or warn:
            print(f'{talk}: {"FAIL" if err else "ok, with warnings"}')
            for e in err:
                print(f'  - {e}')
            for w in warn:
                print(f'  ~ {w}')
        failed += bool(err)
    print(f'\nChecked {len(talks)} talk(s): {len(talks) - failed} passed, {failed} failed')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
