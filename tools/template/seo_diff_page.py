#!/usr/bin/env python3
"""Build the SEO comparison page: output/seo-diff/index.html.

Usage: seo_diff_page.py [--output DIR]

  --output   Folder holding one subfolder per talk (default: output/ in the repo)

One page for every talk that has an SEO-fixed blog text, with a dropdown for the blog and one for
the language. Picking them loads the original text (<name>_blog.txt or _blog_en.txt) and the
SEO-fixed copy (<name>_blog_seo.txt or _blog_seo_en.txt) from the published site and shows them
side by side, paragraphs aligned, with removed words marked on the left and added words on the
right. Only the list of talks is written into the page; the texts are fetched when picked, so the
page must be served over HTTP.
"""
import argparse
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_page import HERE, TEXT, esc, site_footer, site_header  # noqa: E402
from md_to_html import FONTS  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))
TITLE = 'Original vs SEO-Optimized Blogs | Antar Yog Foundation'
SUFFIX = {'hi': '', 'en': '_en'}

DIFF_CSS = """
.hero .sub { max-width: 40rem; margin: .4rem auto 0; color: var(--muted); line-height: 1.7; }
.picker { position: sticky; top: 4.5rem; z-index: 5; background: rgba(255,253,249,.96); backdrop-filter: blur(6px);
          border-bottom: 1px solid var(--rule); }
.picker .wrap { display: flex; flex-wrap: wrap; gap: .8rem 1.2rem; align-items: end; justify-content: center; padding-block: 1rem; }
.picker label { display: flex; flex-direction: column; gap: .3rem; font-size: .8rem; font-weight: 600; color: var(--muted); }
.picker select { font: inherit; font-size: .95rem; padding: .55rem .9rem; border: 1px solid var(--rule); border-radius: .6rem;
                 background: #fff; color: var(--ink); max-width: 100%; }
.picker label.blog { flex: 1 1 22rem; max-width: 36rem; }
.picker select:focus { outline: 2px solid var(--gold); outline-offset: 1px; }
.picker .only { flex-direction: row; align-items: center; gap: .45rem; padding-bottom: .6rem; font-size: .9rem; color: var(--ink); }
.stats { margin: 1.2rem 0 .8rem; text-align: center; font-size: .9rem; color: var(--muted); }
.stats b { color: var(--ink-strong); }
.diff { display: grid; grid-template-columns: 1fr 1fr; border: 1px solid var(--rule); border-radius: .8rem;
        overflow: hidden; background: var(--paper); margin-bottom: 3rem; }
.diff .head { position: sticky; top: 0; padding: .7rem 1rem; font-weight: 600; font-size: .9rem; background: var(--panel);
              color: var(--ink-strong); border-bottom: 1px solid var(--rule); }
.diff .cell { padding: .7rem 1rem; white-space: pre-wrap; overflow-wrap: anywhere; line-height: 1.75; font-size: .95rem;
              border-bottom: 1px solid var(--rule); color: var(--ink); }
.diff .cell.l { border-right: 1px solid var(--rule); }
.diff .cell.changed.l { background: #fdf3f1; }
.diff .cell.changed.r { background: #f1f8f1; }
.diff .cell.gap { background: repeating-linear-gradient(135deg, var(--panel) 0 6px, #f3ebdd 6px 12px); }
.diff del { background: #f6c9c2; color: #7a1d10; text-decoration: line-through; text-decoration-color: rgba(122,29,16,.5);
            border-radius: 3px; }
.diff ins { background: #c6e8c4; color: #164d14; text-decoration: none; border-radius: 3px; }
.diff.only .same { display: none; }
.note { text-align: center; color: var(--muted); padding: 3rem 1rem; }
@media (max-width: 760px) {
  .diff { grid-template-columns: 1fr; }
  .diff .cell.l { border-right: 0; }
  .diff .head { position: static; }
  .diff .head.r { order: 0; }
}
"""

DIFF_JS = """
(function () {
  var blogSel = document.getElementById('blog'), langSel = document.getElementById('lang');
  var onlySel = document.getElementById('only'), out = document.getElementById('out'), stats = document.querySelector('.stats');
  var cache = {}, run = 0;

  function load(url) {
    if (!cache[url]) cache[url] = fetch(url).then(function (r) {
      if (!r.ok) throw new Error(url + ': ' + r.status);
      return r.text();
    });
    return cache[url];
  }
  function paras(text) {
    return text.replace(/\\r/g, '').trim().split(/\\n\\s*\\n/).map(function (p) { return p.trim(); });
  }
  function html(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function words(s) { return s.split(/(\\s+)/).filter(Boolean); }
  function count(tokens) { return tokens.filter(function (t) { return /\\S/.test(t); }).length; }

  // Word diff of one changed paragraph pair: [left html, right html, words removed, words added]
  function wordDiff(a, b) {
    var l = '', r = '', del = 0, add = 0;
    Diff.diffArrays(words(a), words(b)).forEach(function (part) {
      var t = html(part.value.join(''));
      if (part.added) { r += '<ins>' + t + '</ins>'; add += count(part.value); }
      else if (part.removed) { l += '<del>' + t + '</del>'; del += count(part.value); }
      else { l += t; r += t; }
    });
    return [l, r, del, add];
  }

  function render(a, b) {
    var rows = [], changed = 0, del = 0, add = 0;
    var parts = Diff.diffArrays(paras(a), paras(b));
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      if (!p.added && !p.removed) {
        p.value.forEach(function (v) { rows.push(['same', html(v), html(v)]); });
        continue;
      }
      // a removed run followed by an added run: pair them up paragraph by paragraph
      var rem = p.removed ? p.value : [], ins = [];
      if (p.removed && parts[i + 1] && parts[i + 1].added) ins = parts[++i].value;
      else if (p.added) ins = p.value;
      for (var k = 0; k < Math.max(rem.length, ins.length); k++) {
        changed++;
        if (k < rem.length && k < ins.length) {
          var w = wordDiff(rem[k], ins[k]);
          rows.push(['changed', w[0], w[1]]); del += w[2]; add += w[3];
        } else if (k < rem.length) {
          rows.push(['changed', '<del>' + html(rem[k]) + '</del>', null]); del += count(words(rem[k]));
        } else {
          rows.push(['changed', null, '<ins>' + html(ins[k]) + '</ins>']); add += count(words(ins[k]));
        }
      }
    }
    var cell = function (cls, side, v) {
      return '<div class="cell ' + side + ' ' + cls + (v === null ? ' gap' : '') + '">' + (v === null ? '' : v) + '</div>';
    };
    out.innerHTML = '<div class="head l">Original</div><div class="head r">SEO-optimized</div>' +
      rows.map(function (r) { return cell(r[0], 'l', r[1]) + cell(r[0], 'r', r[2]); }).join('');
    stats.innerHTML = changed
      ? '<b>' + changed + '</b> paragraph' + (changed === 1 ? '' : 's') + ' changed · <b>+' + add + '</b> words · <b>−' + del + '</b> words'
      : 'No differences.';
  }

  function show() {
    var name = blogSel.value, lang = langSel.value, sfx = lang === 'en' ? '_en' : '', me = ++run;
    history.replaceState(null, '', '#' + name + '/' + lang);
    stats.textContent = 'Loading…';
    Promise.all([load('../' + name + '/' + name + '_blog' + sfx + '.txt'),
                 load('../' + name + '/' + name + '_blog_seo' + sfx + '.txt')]).then(function (t) {
      if (me === run) render(t[0], t[1]);
    }).catch(function (e) {
      if (me !== run) return;
      out.innerHTML = '';
      stats.textContent = 'Could not load the texts (' + e.message + '). This page must be opened over HTTP.';
    });
  }

  var hash = decodeURIComponent(location.hash.slice(1)).split('/');
  if (hash[0] && blogSel.querySelector('option[value="' + hash[0] + '"]')) blogSel.value = hash[0];
  if (hash[1] === 'hi' || hash[1] === 'en') langSel.value = hash[1];
  blogSel.addEventListener('change', show);
  langSel.addEventListener('change', show);
  onlySel.addEventListener('change', function () { out.classList.toggle('only', onlySel.checked); });
  show();
})();
"""


def collect(out_dir):
    """Talks with an SEO-fixed blog text in both languages, sorted by English title."""
    talks = []
    for name in sorted(os.listdir(out_dir)):
        folder = os.path.join(out_dir, name)
        if not all(os.path.isfile(os.path.join(folder, f'{name}_blog{s}{SUFFIX[l]}.txt'))
                   for s in ('', '_seo') for l in SUFFIX):
            continue
        title = ''
        seo = os.path.join(folder, 'blog', 'seo.json')
        if os.path.isfile(seo):
            title = json.load(open(seo, encoding='utf-8')).get('title', {}).get('en', '')
        talks.append({'name': name, 'title': title or name.replace('_', ' ')})
    talks.sort(key=lambda t: t['title'].lower())
    return talks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--output', default=os.path.join(REPO, 'output'))
    a = ap.parse_args()

    talks = collect(a.output)
    folder = os.path.join(a.output, 'seo-diff')
    os.makedirs(os.path.join(folder, 'assets'), exist_ok=True)
    shutil.copy2(os.path.join(HERE, 'assets', 'logo.png'), os.path.join(folder, 'assets'))
    css = open(os.path.join(HERE, 'blog.css'), encoding='utf-8').read() + DIFF_CSS
    options = ''.join(f'<option value="{t["name"]}">{esc(t["title"])}</option>' for t in talks)

    page = f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}&family=Noto+Sans:wght@400;500;600&family=Noto+Sans+Devanagari:wght@400;500;600" rel="stylesheet">
<style>{css}</style>
</head><body>

{site_header(blog='../index.html')}

<section class="hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="https://antaryogfoundation.in">Home</a> › <a href="../index.html">Blog</a> › Compare</nav>
  <div class="label">The Wisdom Library</div>
  <h1>Original vs SEO-Optimized</h1>
  <div class="orn">❖</div>
  <p class="sub">Compare the original text of each of {len(talks)} blogs with its SEO-optimized version. Removed words are marked in red, added words in green.</p>
</div></section>

<section class="picker"><div class="wrap">
  <label class="blog">Blog<select id="blog">{options}</select></label>
  <label>Language<select id="lang"><option value="hi">हिन्दी</option><option value="en">English</option></select></label>
  <label class="only"><input type="checkbox" id="only"> Changes only</label>
</div></section>

<main class="wrap">
  <p class="stats"></p>
  <div class="diff" id="out"></div>
</main>

{site_footer(TEXT['en']['motto'], blog='../index.html')}
<script src="https://cdn.jsdelivr.net/npm/diff@5.2.0/dist/diff.min.js"></script>
<script>{DIFF_JS}</script>
</body></html>
'''
    out = os.path.join(folder, 'index.html')
    open(out, 'w', encoding='utf-8').write(page)
    print(f'SEO comparison: {out} ({len(talks)} blogs)')


if __name__ == '__main__':
    main()
