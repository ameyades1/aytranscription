#!/usr/bin/env python3
"""Verify that a talk fixed by /seo_blog_fix has no stale files before it goes to WordPress.

Usage: verify_seo_fix.py [--strict] [<talk> ...]   (default: every talk with SEO-fixed texts)

--strict makes warnings fail too (batch_seo_fix.sh uses it to decide a talk is done).

The WordPress importer (~/wordpress/import_post.py) reads the SEO-fixed texts
(<name>_blog_seo[_en].txt), blog/seo.json, blog/images.txt and blog/assets/; the blog page is
built from the same texts. Errors make the talk fail (exit code 1); warnings are printed.
Errors:
  - tools/check_seo.py fails (it checks seo.json against the fixed texts: link phrases, Also read
    headings, focus keyword in title, meta description, body and slug, unique slugs, and the
    report's section 11 copy of seo.json)
  - a fixed text is missing or older than its original (the fix is stale)
  - seo_fix.md is missing or older than the fixed texts
  - the blog page is older than the fixed texts or seo.json (not rebuilt after the fix)
  - a fixed text has a different number of ## sections from its original (the page generator and
    the importer place images and the Also read box by section position when a heading is reworded)
  - an inline image's section heading (images.txt) is in neither original text, so the importer
    would leave the image out of the WordPress post
Warnings (the report and seo_fix.md must agree with seo.json, which is what gets published):
  - the report's section 3 or section 8 (schema) does not show seo.json's slug, title or meta
    description, for each language
  - seo_fix.md has no "Final seo.json values" section, or it does not show seo.json's slug,
    focus keyword, title or meta description, for each language
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'output')


def h2s(path):
    return [l[3:].strip() for l in open(path, encoding='utf-8') if l.startswith('## ')]


def verify(talk):
    err, warn = [], []
    d = os.path.join(OUT, talk)
    blog = os.path.join(d, 'blog')
    texts = {}
    for suffix in ('', '_en'):
        orig = os.path.join(d, f'{talk}_blog{suffix}.txt')
        fixed = os.path.join(d, f'{talk}_blog_seo{suffix}.txt')
        if not os.path.exists(fixed):
            err.append(f'{os.path.basename(fixed)} missing')
        elif os.path.exists(orig) and os.path.getmtime(fixed) < os.path.getmtime(orig):
            err.append(f'{os.path.basename(fixed)} is older than {os.path.basename(orig)} (stale fix)')
        else:
            texts['en' if suffix else 'hi'] = fixed
    if err:
        return err, warn

    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'check_seo.py'), talk],
                       capture_output=True, text=True)
    if r.returncode:
        err += ['check_seo: ' + l.strip(' -') for l in r.stdout.splitlines() if l.startswith('  - ')]

    newest_text = max(os.path.getmtime(p) for p in texts.values())
    fix_md = os.path.join(blog, 'seo_fix.md')
    if not os.path.exists(fix_md):
        err.append('blog/seo_fix.md missing')
    elif os.path.getmtime(fix_md) < newest_text:
        err.append('blog/seo_fix.md is older than the fixed texts')

    page = os.path.join(blog, 'index.html')
    seo_path = os.path.join(blog, 'seo.json')
    if os.path.getmtime(page) < max(newest_text, os.path.getmtime(seo_path)):
        err.append('blog page is older than the fixed texts or seo.json (run tools/rebuild_blogs.sh)')

    # sections: same number and order as the original, so placement by position works
    orig = {lang: h2s(os.path.join(d, f'{talk}_blog{"_en" if lang == "en" else ""}.txt')) for lang in texts}
    for lang, p in texts.items():
        if len(h2s(p)) != len(orig[lang]):
            err.append(f'{os.path.basename(p)} has {len(h2s(p))} ## sections, the original {len(orig[lang])}')

    # inline images: the importer looks up images.txt's headings in the original texts
    # (English, else Hindi) and places the image at that section's position
    imgs = os.path.join(blog, 'images.txt')
    if os.path.exists(imgs):
        for line in open(imgs, encoding='utf-8'):
            if line.strip() and not line.startswith('#'):
                f, hi, en, _ = (p.strip() for p in line.split('|'))
                if en not in orig['en'] and hi not in orig['hi']:
                    err.append(f'images.txt: no original heading for {f} (English "{en}", Hindi "{hi}"); '
                               'WordPress would leave it out')

    seo = json.load(open(seo_path, encoding='utf-8'))
    report = open(os.path.join(blog, 'seo_report.md'), encoding='utf-8').read()

    def section(text, start, end):
        m = re.search(rf'^## {start}\..*?(?=^## {end}\.|\Z)', text, re.S | re.M)
        return m.group(0) if m else ''

    def shows(text, value):  # as written, or as escaped inside a JSON string
        return value in text or json.dumps(value, ensure_ascii=False)[1:-1] in text

    fix_text = open(fix_md, encoding='utf-8').read() if os.path.exists(fix_md) else ''
    m = re.search(r'^## Final seo\.json values.*?(?=^## |\Z)', fix_text, re.S | re.M)
    final = m.group(0) if m else None
    if final is None and fix_text:
        warn.append('seo_fix.md has no "## Final seo.json values" section')
    places = {'report section 3': section(report, 3, 4), 'report section 8': section(report, 8, 9)}
    for lang in ('hi', 'en'):
        w = seo.get('wordpress', {}).get(lang, {})
        values = {'slug': w.get('slug'), 'title': seo.get('title', {}).get(lang),
                  'meta description': w.get('meta_description')}
        for place, text in places.items():
            for field, value in values.items():
                if value and not shows(text, value):
                    warn.append(f'{place} does not show the {lang} {field} in seo.json')
        if final is not None:
            for field, value in dict(values, **{'focus keyword': w.get('focus_keyword')}).items():
                if value and not shows(final, value):
                    warn.append(f'seo_fix.md final values do not show the {lang} {field} in seo.json')
    return err, warn


def main():
    args = sys.argv[1:]
    strict = '--strict' in args
    args = [a for a in args if a != '--strict']
    talks = args or sorted(t for t in os.listdir(OUT)
                                   if os.path.exists(os.path.join(OUT, t, f'{t}_blog_seo_en.txt')))
    failed = 0
    for talk in talks:
        err, warn = verify(talk)
        if err or warn:
            print(f'{talk}: {"FAIL" if err else "ok, with warnings"}')
            for e in err:
                print(f'  - {e}')
            for w in warn:
                print(f'  ~ {w}')
        failed += bool(err or (strict and warn))
    print(f'\nVerified {len(talks)} fixed talk(s): {len(talks) - failed} passed, {failed} failed')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
