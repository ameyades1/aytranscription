#!/usr/bin/env python3
"""Build the SEO comparison page: output/seo-diff/index.html.

Usage: seo_diff_page.py [--output DIR] [--topics FILE]

  --output   Folder holding one subfolder per talk (default: output/ in the repo)
  --topics   Topic definitions, for the category names (default: gallery_topics.txt in the repo)

One page for every talk that has an SEO-fixed blog text, with a dropdown for the blog and one for
the language. Picking them loads the original text (<name>_blog.txt or _blog_en.txt) and the
SEO-fixed copy (<name>_blog_seo.txt or _blog_seo_en.txt) from the published site and shows them
side by side, paragraphs aligned, with removed words marked on the left and added words on the
right. Above the texts, an SEO details table shows the talk's blog/seo.json for the language, and a
panel shows blog/seo_fix.md: the language's change table (Where, Before, After, Why) and the other
sections. Each change's reason is also shown under its paragraph in the diff, and the focus
keyword is underlined wherever it appears. Only the list of talks and topic names is written into
the page; the texts, seo.json and seo_fix.md are fetched when picked, so the page must be served
over HTTP.
"""
import argparse
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blog_page import HERE, TEXT, esc, site_footer, site_header  # noqa: E402
from gallery_page import read_topics  # noqa: E402
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
.diff del, .legend del { background: #f6c9c2; color: #7a1d10; text-decoration: line-through; text-decoration-color: rgba(122,29,16,.5);
            border-radius: 3px; }
.diff ins, .legend ins { background: #c6e8c4; color: #164d14; text-decoration: none; border-radius: 3px; }
.diff.only .same { display: none; }
.blog-link { margin: 1.2rem 0 0; text-align: center; }
.blog-link a { display: inline-block; font-size: .92rem; font-weight: 600; color: var(--accent); text-decoration: none;
               padding: .45rem 1rem; border: 1px solid var(--rule); border-radius: 999px; background: #fff; }
.blog-link a:hover { background: var(--panel); }
.panel { margin: 1.2rem 0 0; border: 1px solid var(--rule); border-radius: .8rem; background: var(--paper); }
.panel > summary { cursor: pointer; padding: .8rem 1rem; font-family: var(--serif); font-weight: 600; font-size: 1.05rem;
                   color: var(--ink-strong); }
.panel > .in { padding: 0 1rem 1rem; overflow-x: auto; }
.panel .missing { color: var(--muted); font-size: .9rem; }
.kv { width: 100%; border-collapse: collapse; font-size: .92rem; }
.kv th, .kv td { text-align: left; vertical-align: top; padding: .55rem .7rem; border-top: 1px solid var(--rule); line-height: 1.6; }
.kv th { width: 11rem; color: var(--muted); font-weight: 600; white-space: nowrap; }
.kv a { color: var(--accent); }
.kv .len { margin-left: .5rem; font-size: .78rem; color: var(--muted); white-space: nowrap; }
.kv .len.over { color: #9a5b00; font-weight: 600; }
.kv .sub { display: block; color: var(--muted); font-size: .85rem; }
.pill { display: inline-block; margin: 0 .3rem .3rem 0; padding: .1rem .6rem; border-radius: 999px; background: var(--panel);
        border: 1px solid var(--rule); font-size: .85rem; }
.md table { width: 100%; border-collapse: collapse; font-size: .9rem; margin: .4rem 0 .8rem; }
.md th, .md td { text-align: left; vertical-align: top; padding: .5rem .6rem; border: 1px solid var(--rule); line-height: 1.6; }
.md th { background: var(--panel); color: var(--ink-strong); }
.md code { font-size: .85em; background: var(--panel); padding: 0 .25rem; border-radius: 3px; }
.md p, .md ul { margin: .5rem 0; line-height: 1.65; font-size: .92rem; }
.changes tbody tr { cursor: pointer; }
.changes tbody tr:hover td { background: #fbf6ec; }
.md details { border-top: 1px solid var(--rule); padding: .5rem 0; }
.md details summary { cursor: pointer; font-weight: 600; color: var(--ink-strong); }
.legend { text-align: center; font-size: .82rem; color: var(--muted); margin: -.4rem 0 .9rem; }
.legend span { margin: 0 .5rem; }
.why { display: block; margin-top: .5rem; padding: .4rem .6rem; border-left: 3px solid var(--gold); background: var(--panel);
       font-size: .82rem; line-height: 1.55; color: var(--muted); white-space: normal; }
.why b { color: var(--ink-strong); }
mark.kw { background: none; color: inherit; text-decoration: underline; text-decoration-color: var(--gold);
          text-decoration-thickness: 3px; text-underline-offset: 3px; }
.diff .cell.flash { animation: flash 1.6s ease-out; }
@keyframes flash { from { box-shadow: inset 0 0 0 3px var(--gold); } to { box-shadow: inset 0 0 0 3px transparent; } }
@media (max-width: 760px) {
  .kv th, .kv td { display: block; width: auto; border-top: 0; padding: .2rem .2rem; }
  .kv tr { display: block; border-top: 1px solid var(--rule); padding: .4rem 0; }
}
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
  var DATA = JSON.parse(document.getElementById('data').textContent);
  var blogSel = document.getElementById('blog'), langSel = document.getElementById('lang');
  var onlySel = document.getElementById('only'), out = document.getElementById('out'), stats = document.querySelector('.stats');
  var details = document.getElementById('details'), fix = document.getElementById('fix');
  var cache = {}, run = 0;

  function load(url, optional) {
    if (!cache[url]) cache[url] = fetch(url).then(function (r) {
      if (!r.ok) throw new Error(url + ': ' + r.status);
      return r.text();
    });
    return optional ? cache[url].catch(function () { return null; }) : cache[url];
  }
  function paras(text) {
    return text.replace(/\\r/g, '').trim().split(/\\n\\s*\\n/).map(function (p) { return p.trim(); });
  }
  function html(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function words(s) { return s.split(/(\\s+)/).filter(Boolean); }
  function count(tokens) { return tokens.filter(function (t) { return /\\S/.test(t); }).length; }
  // plain comparable text: no markdown marks, quotes or extra spaces
  function norm(s) { return String(s).replace(/[*_`#>"“”‘’']/g, '').replace(/\\s+/g, ' ').trim().toLowerCase(); }
  function title(name, lang) { return (DATA.titles[name] || {})[lang] || name; }
  function talkLink(name, lang) {
    return '<a href="../' + name + '/blog/index.html#' + lang + '">' + html(title(name, lang)) + '</a>';
  }

  // ---- seo_fix.md: sections, and the change rows of each language ----
  function parseFix(md) {
    var parts = md.replace(/\\r/g, '').split(/^## /m), fixd = {intro: parts[0], hi: null, en: null, rest: []};
    parts.slice(1).forEach(function (p) {
      var nl = p.indexOf('\\n'), head = nl < 0 ? p : p.slice(0, nl), body = nl < 0 ? '' : p.slice(nl + 1);
      var lang = /^hindi/i.test(head) ? 'hi' : /^english/i.test(head) ? 'en' : null;
      if (lang && !fixd[lang]) fixd[lang] = {head: head, body: body, rows: rows(body)};
      else fixd.rest.push({head: head, body: body});
    });
    return fixd;
  }
  function cells(line) {
    return line.trim().replace(/^\\|/, '').replace(/\\|$/, '').split('|').map(function (c) { return c.trim(); });
  }
  function rows(body) {
    var lines = body.split('\\n').filter(function (l) { return /^\\s*\\|/.test(l); }), head = null, list = [];
    lines.forEach(function (l) {
      var c = cells(l);
      if (!head) { head = c.map(function (h) { return h.toLowerCase(); }); return; }
      if (c.every(function (x) { return /^:?-+:?$/.test(x); })) return;
      var row = {};
      head.forEach(function (h, i) { row[h] = c[i] || ''; });
      list.push(row);
    });
    return list;
  }
  function md(s) { return marked.parse(s); }

  function renderFix(text, lang) {
    if (text === null) { fix.innerHTML = '<p class="missing">No seo_fix.md for this blog.</p>'; return null; }
    var f = parseFix(text), mine = f[lang];
    if (!mine && !f.rest.length) {
      fix.innerHTML = '<p class="missing">seo_fix.md is not in the expected form; shown as written.</p><div class="md">' + md(text) + '</div>';
      return null;
    }
    var h = '<div class="md">';
    if (mine) {
      h += '<h3>' + html(mine.head) + '</h3>';
      if (mine.rows.length) {
        h += '<table class="changes"><thead><tr><th>Where</th><th>Before</th><th>After</th><th>Why</th></tr></thead><tbody>' +
          mine.rows.map(function (r, i) {
            return '<tr data-fix="' + i + '"><td>' + marked.parseInline(r.where || '') + '</td><td>' + marked.parseInline(r.before || '') +
              '</td><td>' + marked.parseInline(r.after || '') + '</td><td>' + marked.parseInline(r.why || '') + '</td></tr>';
          }).join('') + '</tbody></table>';
        var extra = mine.body.split('\\n').filter(function (l) { return !/^\\s*\\|/.test(l); }).join('\\n').trim();
        if (extra) h += md(extra);
      } else h += md(mine.body);
    } else h += '<p class="missing">No ' + (lang === 'hi' ? 'Hindi' : 'English') + ' changes section in seo_fix.md.</p>';
    h += f.rest.map(function (s) { return '<details><summary>' + html(s.head) + '</summary>' + md(s.body) + '</details>'; }).join('');
    fix.innerHTML = h + '</div>';
    return mine ? mine.rows : null;
  }

  // ---- seo.json: details table for the language ----
  function pills(list) { return (list || []).map(function (t) { return '<span class="pill">' + html(t) + '</span>'; }).join(''); }
  function len(s, max) {
    var n = Array.from(s || '').length;
    return '<span class="len' + (n > max ? ' over' : '') + '">' + n + '/' + max + '</span>';
  }
  function renderDetails(text, lang) {
    if (text === null) { details.innerHTML = '<p class="missing">No seo.json for this blog.</p>'; return ''; }
    var seo = JSON.parse(text), wp = (seo.wordpress || {})[lang] || {}, rowsH = [];
    var add = function (k, v) { if (v) rowsH.push('<tr><th>' + k + '</th><td>' + v + '</td></tr>'); };
    var t = (seo.title || {})[lang] || '';
    add('Title tag', html(t) + len(t, 60));
    add('Slug', wp.slug ? '<code>' + html(wp.slug) + '</code>' : '');
    add('Focus keyword', html(wp.focus_keyword || ''));
    add('Secondary keywords', pills(wp.secondary_keywords));
    add('Meta description', html(wp.meta_description || '') + len(wp.meta_description, 160));
    var cat = (seo.wordpress || {}).category;
    add('Category', cat ? html(((DATA.topics[cat] || {})[lang]) || cat) : '');
    add('Tags', pills(wp.tags));
    add('Internal links', (seo.links || []).map(function (l) {
      return '“' + html(l[lang] || '') + '” → ' + talkLink(l.talk, lang);
    }).join('<br>'));
    var also = seo.also_read || {};
    add('Also read', also.talk ? talkLink(also.talk, lang) +
      (also.after && also.after[lang] ? '<span class="sub">after “' + html(also.after[lang]) + '”</span>' : '') : '');
    add('Related', (seo.related || []).map(function (n) { return talkLink(n, lang); }).join(' · '));
    var imgs = Object.keys(Object.assign({}, seo.alt || {}, seo.caption || {}));
    add('Images', imgs.map(function (f) {
      var alt = ((seo.alt || {})[f] || {})[lang], cap = ((seo.caption || {})[f] || {})[lang];
      return '<code>' + html(f) + '</code>' + (alt ? '<span class="sub">alt: ' + html(alt) + '</span>' : '') +
        (cap ? '<span class="sub">caption: ' + html(cap) + '</span>' : '');
    }).join('<br>'));
    details.innerHTML = '<table class="kv"><tbody>' + rowsH.join('') + '</tbody></table>';
    return wp.focus_keyword || '';
  }

  // ---- the diff ----
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
  // index of the change row whose After text is in this paragraph, else -1
  function matchFix(text, fixRows) {
    if (!fixRows || !text) return -1;
    var p = norm(text);
    for (var i = 0; i < fixRows.length; i++) {
      var a = norm(fixRows[i].after || '');
      if (a && p.indexOf(a) >= 0) return i;
    }
    for (i = 0; i < fixRows.length; i++) {  // a long After may have been shortened in the table
      a = norm(fixRows[i].after || '');
      if (a.length > 24 && p.indexOf(a.slice(0, 24)) >= 0) return i;
    }
    return -1;
  }

  function render(a, b, fixRows, keyword) {
    var rows = [], changed = 0, del = 0, add = 0;
    var parts = Diff.diffArrays(paras(a), paras(b));
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      if (!p.added && !p.removed) {
        p.value.forEach(function (v) { rows.push(['same', html(v), html(v), null]); });
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
          rows.push(['changed', w[0], w[1], ins[k]]); del += w[2]; add += w[3];
        } else if (k < rem.length) {
          rows.push(['changed', '<del>' + html(rem[k]) + '</del>', null, null]); del += count(words(rem[k]));
        } else {
          rows.push(['changed', null, '<ins>' + html(ins[k]) + '</ins>', ins[k]]); add += count(words(ins[k]));
        }
      }
    }
    var cell = function (cls, side, v, extra) {
      return '<div class="cell ' + side + ' ' + cls + (v === null ? ' gap' : '') + '"' + (extra || '') + '>' + (v === null ? '' : v) + '</div>';
    };
    out.innerHTML = '<div class="head l">Original</div><div class="head r">SEO-optimized</div>' +
      rows.map(function (r) {
        var right = r[2], m = r[0] === 'changed' ? matchFix(r[3], fixRows) : -1, extra = '';
        if (m >= 0) {
          var f = fixRows[m];
          right += '<span class="why"><b>' + html(f.where || 'Change') + ':</b> ' + marked.parseInline(f.why || '') + '</span>';
          extra = ' data-fix="' + m + '"';
        }
        return cell(r[0], 'l', r[1], extra) + cell(r[0], 'r', right, extra);
      }).join('');
    if (keyword) highlight(keyword);
    stats.innerHTML = changed
      ? '<b>' + changed + '</b> paragraph' + (changed === 1 ? '' : 's') + ' changed · <b>+' + add + '</b> words · <b>−' + del + '</b> words'
      : 'No differences.';
  }

  // underline the focus keyword in the text of both columns (not in the reason notes)
  function highlight(keyword) {
    var re = new RegExp(keyword.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'), 'gi');
    var walker = document.createTreeWalker(out, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        return n.parentNode.closest('.cell') && !n.parentNode.closest('.why, .head') ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (n) {
      var t = n.nodeValue, last = 0, m, frag = null;
      re.lastIndex = 0;
      while ((m = re.exec(t))) {
        frag = frag || document.createDocumentFragment();
        frag.appendChild(document.createTextNode(t.slice(last, m.index)));
        var mk = document.createElement('mark');
        mk.className = 'kw';
        mk.textContent = m[0];
        frag.appendChild(mk);
        last = m.index + m[0].length;
      }
      if (frag) {
        frag.appendChild(document.createTextNode(t.slice(last)));
        n.parentNode.replaceChild(frag, n);
      }
    });
  }

  function show() {
    var name = blogSel.value, lang = langSel.value, sfx = lang === 'en' ? '_en' : '', me = ++run;
    history.replaceState(null, '', '#' + name + '/' + lang);
    document.getElementById('blog-link').href = '../' + name + '/blog/index.html#' + lang;
    stats.textContent = 'Loading…';
    Promise.all([load('../' + name + '/' + name + '_blog' + sfx + '.txt'),
                 load('../' + name + '/' + name + '_blog_seo' + sfx + '.txt'),
                 load('../' + name + '/blog/seo.json', true),
                 load('../' + name + '/blog/seo_fix.md', true)]).then(function (t) {
      if (me !== run) return;
      var keyword = renderDetails(t[2], lang), fixRows = renderFix(t[3], lang);
      render(t[0], t[1], fixRows, keyword);
    }).catch(function (e) {
      if (me !== run) return;
      out.innerHTML = '';
      stats.textContent = 'Could not load the texts (' + e.message + '). This page must be opened over HTTP.';
    });
  }

  // a change row in the seo_fix table jumps to its paragraph in the diff
  fix.addEventListener('click', function (e) {
    var tr = e.target.closest('tr[data-fix]');
    if (!tr || e.target.closest('a')) return;
    var cells = out.querySelectorAll('.cell[data-fix="' + tr.dataset.fix + '"]');
    if (!cells.length) return;
    if (onlySel.checked === false && cells[0].classList.contains('same')) return;
    cells[0].scrollIntoView({behavior: 'smooth', block: 'center'});
    cells.forEach(function (c) { c.classList.remove('flash'); void c.offsetWidth; c.classList.add('flash'); });
  });

  // remember which panels are collapsed
  document.querySelectorAll('details.panel').forEach(function (d) {
    try { if (localStorage.getItem('seo-diff-' + d.id) === 'closed') d.open = false; } catch (e) {}
    d.addEventListener('toggle', function () {
      try { localStorage.setItem('seo-diff-' + d.id, d.open ? 'open' : 'closed'); } catch (e) {}
    });
  });

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
        titles = {}
        seo = os.path.join(folder, 'blog', 'seo.json')
        if os.path.isfile(seo):
            titles = json.load(open(seo, encoding='utf-8')).get('title', {})
        fallback = name.replace('_', ' ')
        talks.append({'name': name, 'title': titles.get('en') or fallback, 'hi': titles.get('hi') or fallback})
    talks.sort(key=lambda t: t['title'].lower())
    return talks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--output', default=os.path.join(REPO, 'output'))
    ap.add_argument('--topics', default=os.path.join(REPO, 'gallery_topics.txt'))
    a = ap.parse_args()

    talks = collect(a.output)
    folder = os.path.join(a.output, 'seo-diff')
    os.makedirs(os.path.join(folder, 'assets'), exist_ok=True)
    shutil.copy2(os.path.join(HERE, 'assets', 'logo.png'), os.path.join(folder, 'assets'))
    css = open(os.path.join(HERE, 'blog.css'), encoding='utf-8').read() + DIFF_CSS
    topics, _ = read_topics(a.topics)
    data = {'titles': {t['name']: {'en': t['title'], 'hi': t['hi']} for t in talks},
            'topics': {k: {'en': en, 'hi': hi} for k, en, hi in topics}}
    data = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
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
  <p class="sub">Compare the original text of each of {len(talks)} blogs with its SEO-optimized version. Removed words are marked in red, added words in green, with the SEO details and the reason for each change.</p>
</div></section>

<section class="picker"><div class="wrap">
  <label class="blog">Blog<select id="blog">{options}</select></label>
  <label>Language<select id="lang"><option value="hi">हिन्दी</option><option value="en">English</option></select></label>
  <label class="only"><input type="checkbox" id="only"> Changes only</label>
</div></section>

<main class="wrap">
  <p class="blog-link"><a id="blog-link" href="#" target="_blank" rel="noopener">Open the blog page ↗</a></p>
  <details class="panel" id="p-details" open><summary>SEO details</summary><div class="in" id="details"></div></details>
  <details class="panel" id="p-fix" open><summary>What the SEO fix changed</summary><div class="in" id="fix"></div></details>
  <p class="stats"></p>
  <p class="legend"><span><del>removed</del></span><span><ins>added</ins></span><span><mark class="kw">focus keyword</mark></span></p>
  <div class="diff" id="out"></div>
</main>

{site_footer(TEXT['en']['motto'], blog='../index.html')}
<script type="application/json" id="data">{data}</script>
<script src="https://cdn.jsdelivr.net/npm/diff@5.2.0/dist/diff.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script>{DIFF_JS}</script>
</body></html>
'''
    out = os.path.join(folder, 'index.html')
    open(out, 'w', encoding='utf-8').write(page)
    print(f'SEO comparison: {out} ({len(talks)} blogs)')


if __name__ == '__main__':
    main()
