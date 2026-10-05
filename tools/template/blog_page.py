#!/usr/bin/env python3
"""Build an Antar Yog Foundation blog page from a chapter .txt.

Usage: blog_page.py <blog.txt> [<other_language_blog.txt>] [--video YOUTUBE_ID] [--out FILE]

  blog.txt      The blog text (or a chapter); its language is the page's default.
  other ...     The same chapter in the other language (Hindi/English). Both languages go on
                the same page with a language switch; open a language directly with #hi / #en.
  --video       YouTube ID of the original discourse (adds a "watch" button and video card)
  --out         Output HTML (default: blog/index.html in the chapter's folder)

Site links, contact details and the founder description come from antaryogfoundation.in
and are kept in SITE below.
"""
import argparse
import html
import os
import re
import shutil
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from md_to_html import FONTS, convert  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

SITE = {
    'home': 'https://antaryogfoundation.in',
    'nav': [
        ('Home', 'https://antaryogfoundation.in/'),
        ('Our Work', 'https://antaryogfoundation.in/our-work'),
        ('Events', 'https://antaryogfoundation.in/events'),
        ('Discourses', 'https://learn.antaryogfoundation.in/courses'),
        ('Blog', 'https://blogs.antaryogfoundation.in'),
        ('Shop', 'https://wellness.antaryogfoundation.in'),
        ('Contact Us', 'https://antaryogfoundation.in/contact-us'),
    ],
    'donate': 'https://payment.antaryogfoundation.in/donation',
    'explore': [
        ('Our Work', 'https://antaryogfoundation.in/our-work'),
        ('Current and Upcoming Events', 'https://antaryogfoundation.in/events'),
        ('Discourses', 'https://learn.antaryogfoundation.in/courses'),
        ('Blog', 'https://blogs.antaryogfoundation.in'),
        ('Newsroom', 'https://antaryogfoundation.in/newsroom'),
        ('Letters of Distinction', 'https://antaryogfoundation.in/letters-of-distinction'),
    ],
    'services': [
        ('Naadi Jyotish', 'https://naadijyotish.antaryogfoundation.in'),
        ('Horoscope', 'https://naadijyotish.antaryogfoundation.in/kundali'),
        ('Vastu Rupantaran', 'https://vasturupantaran.antaryogfoundation.in'),
        ('Shop', 'https://wellness.antaryogfoundation.in'),
        ('Donate', 'https://payment.antaryogfoundation.in/donation'),
    ],
    'phone': ('+91 77109 48461', 'tel:+917710948461'),
    'email': 'antaryog.foundation@gmail.com',
    'address': '2nd Floor, Chemco House, D. Sukhadwala Road, Fort, Mumbai - 400001, Maharashtra, India',
    'hours': 'Monday - Saturday, 10:00 AM - 6:00 PM',
    'youtube': 'https://youtube.com/@AntarYogFoundationOfficial',
    'instagram': 'https://www.instagram.com/antaryogfoundation',
    'courses': 'https://learn.antaryogfoundation.in/courses',
    'signup': 'https://learn.antaryogfoundation.in/sign_up',
    'privacy': 'https://antaryogfoundation.in/privacy',
    'terms': 'https://antaryogfoundation.in/terms',
}

TEXT = {
    'hi': {
        'author': 'ब्रह्मर्षि आचार्य उपेंद्र जी',
        'bio': 'अंतर योग के संस्थापक, राष्ट्र के पुनरुत्थान के लिए सनातन धर्म के शाश्वत ज्ञान का प्रसार कर रहे हैं।',
        'about': 'आचार्य जी के बारे में',
        'about_url': 'https://antaryogfoundation.in/hi',
        'meta': 'प्रवचन पर आधारित · {m} मिनट में पढ़ें',
        'alt': 'Read in English', 'watch': 'मूल प्रवचन देखें',
        'toc': 'इस लेख में', 'author_h': 'वक्ता', 'video_h': 'मूल प्रवचन',
        'cta_h': 'आचार्य जी के और प्रवचन सुनें',
        'cta_p': 'जीवन परिवर्तन करने वाले ज्ञान-सत्र और शक्तिशाली साधनाओं का लाभ लें।',
        'cta_1': 'प्रवचन देखें', 'cta_2': 'Sign Up',
        'motto': 'जनहिताय स्वयम् मोक्षाय च',
    },
    'en': {
        'author': 'Brahmarshi Acharya Upendra Ji',
        'bio': 'The founder of Antar Yog, teaching the timeless wisdom of Sanatan Dharma for the revival of a nation.',
        'about': 'About Acharya Ji',
        'about_url': 'https://antaryogfoundation.in',
        'meta': 'Based on a discourse · {m} min read',
        'alt': 'हिन्दी में पढ़ें', 'watch': 'Watch the discourse',
        'toc': 'In this article', 'author_h': 'Speaker', 'video_h': 'Original discourse',
        'cta_h': 'Listen to more discourses by Acharya Ji',
        'cta_p': 'Join life-transforming knowledge sessions and powerful sadhanas.',
        'cta_1': 'Explore discourses', 'cta_2': 'Sign Up',
        'motto': 'जनहिताय स्वयम् मोक्षाय च',
    },
}

ICON = {
    'phone': 'M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2zm0 3v13h10V5H7zm5 14a1 1 0 1 0 0 2 1 1 0 0 0 0-2z',
    'mail': 'M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm1 2.6V17h16V7.6l-8 5.3-8-5.3zM5.8 7l6.2 4.1L18.2 7H5.8z',
    'pin': 'M12 2a7 7 0 0 1 7 7c0 5.2-7 13-7 13S5 14.2 5 9a7 7 0 0 1 7-7zm0 4.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z',
    'clock': 'M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20zm0 2a8 8 0 1 0 0 16 8 8 0 0 0 0-16zm1 3v4.6l3.2 1.9-1 1.7-4.2-2.5V7h2z',
    'youtube': 'M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4a2.5 2.5 0 0 0-1.8 1.8A26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.8 1.8c1.6.4 7.8.4 7.8.4s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8zM10 15V9l5.2 3L10 15z',
    'instagram': 'M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm0 2a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3H7zm5 3.5a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm0 2a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zm5.3-3.8a1 1 0 1 1 0 2 1 1 0 0 1 0-2z',
    'play': 'M8 5v14l11-7z',
}


def icon(name, fill=None):
    f = f' fill="{fill}"' if fill else ''
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"{f}><path fill-rule="evenodd" d="{ICON[name]}"/></svg>'


def esc(t):
    return html.escape(t, quote=True)


def video_info(vid, assets_dir):
    """Title/duration via yt-dlp and a local thumbnail; best effort."""
    title, duration = '', ''
    try:
        import yt_dlp
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'skip_download': True}) as y:
            info = y.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False)
            title, duration = info.get('title', ''), info.get('duration_string', '')
    except Exception as e:  # network or extraction problem: page still builds
        print(f'Note: could not read video details ({e})', file=sys.stderr)
    thumb = f'{vid}.jpg'
    path = os.path.join(assets_dir, thumb)
    if not os.path.exists(path):
        for size in ('maxresdefault', 'hqdefault'):
            try:
                urllib.request.urlretrieve(f'https://i.ytimg.com/vi/{vid}/{size}.jpg', path)
                break
            except Exception:
                continue
    return title, duration, thumb if os.path.exists(path) else None


def read_minutes(text, lang):
    words = len(re.sub(r'[#>*\-]', ' ', text).split())
    return max(1, round(words / (180 if lang == 'hi' else 200)))


def local_digits(n, lang):
    return str(n).translate(str.maketrans('0123456789', '०१२३४५६७८९')) if lang == 'hi' else str(n)


def read_images(out_dir):
    """Inline images from <blog>/images.txt: one line per image,
    file | Hindi section heading | English section heading | description.
    Each image goes at the end of that section (before the next ## heading)."""
    path = os.path.join(out_dir, 'images.txt')
    images = []
    if os.path.exists(path):
        for line in open(path, encoding='utf-8'):
            if line.strip() and not line.startswith('#'):
                f, hi, en, alt = (p.strip() for p in line.split('|'))
                images.append({'file': f, 'hi': hi, 'en': en, 'alt': alt})
    return images


def hero_image(out_dir):
    """assets/hero.jpg (or .png) if there is one."""
    return next((f for f in ('hero.jpg', 'hero.png') if os.path.exists(os.path.join(out_dir, 'assets', f))), None)


def place_images(body, lang, out_dir):
    for img in read_images(out_dir):
        if not os.path.exists(os.path.join(out_dir, 'assets', img['file'])):
            print(f"Note: assets/{img['file']} not found, left out", file=sys.stderr)
            continue
        heads = list(re.finditer(r'<h2>(.*?)</h2>', body))
        at = next((i for i, h in enumerate(heads) if re.sub('<[^>]+>', '', h.group(1)).strip() == img[lang]), None)
        if at is None:
            print(f"Note: section '{img[lang]}' not found for {img['file']} ({lang}), left out", file=sys.stderr)
            continue
        pos = heads[at + 1].start() if at + 1 < len(heads) else len(body)
        fig = f'<figure class="figure"><img src="assets/{esc(img["file"])}" alt="{esc(img["alt"])}" loading="lazy"></figure>'
        body = body[:pos] + fig + body[pos:]
    return body


def build_lang(path, out_dir, video, other_lang):
    """Hero, article+sidebar and call-to-action for one language."""
    text = open(path, encoding='utf-8').read()
    lang = 'hi' if re.search(r'[ऀ-ॿ]', text) else 'en'
    T = TEXT[lang]

    title_line, body = convert(text.splitlines())
    body = re.sub(r'<header>.*?</header>', '', body, count=1, flags=re.S)
    label, title = title_line.split(':', 1) if ':' in title_line else ('', title_line)
    label, title = label.strip(), title.strip()

    body = place_images(body, lang, out_dir)
    hero = hero_image(out_dir)
    toc = []

    def number_h2(m):
        toc.append(m.group(1))
        return f'<h2 id="{lang}-s{len(toc)}">{m.group(1)}</h2>'
    body = re.sub(r'<h2>(.*?)</h2>', number_h2, body)

    minutes = local_digits(read_minutes(text, lang), lang)

    actions = []
    if other_lang:
        actions.append(f'<a class="btn btn-ghost" href="#{other_lang}" data-switch="{other_lang}">{T["alt"]}</a>')

    video_html = ''
    if video:
        url = f'https://www.youtube.com/watch?v={video["id"]}'
        actions.append(f'<a class="btn btn-ghost" href="{url}" target="_blank" rel="noopener">'
                       f'{icon("youtube", "#6b3d22")}{T["watch"]}</a>')
        if video['thumb']:
            cap = esc(video['title']) + (f'<small>YouTube · {esc(video["duration"])}</small>' if video['duration'] else '')
            video_html = (f'<section class="video"><a href="{url}" target="_blank" rel="noopener">'
                          f'<img src="assets/{video["thumb"]}" alt="{esc(video["title"] or T["video_h"])}" loading="lazy">'
                          f'<div class="play"><span>{icon("play", "#6b3d22")}</span></div>'
                          f'<div class="caption">{cap}</div></a></section>')

    toc_html = ''.join(f'<li><a href="#{lang}-s{i}">{t}</a></li>' for i, t in enumerate(toc, 1))
    html_ = f'''<div class="lang-block" data-lang="{lang}" data-title="{esc(title)} | Antar Yog Foundation" lang="{lang}">
<section class="hero"><div class="wrap">
  <div class="crumbs"><a href="{SITE['home']}">Home</a> › <a href="https://blogs.antaryogfoundation.in">Blog</a></div>
  {f'<div class="label">{esc(label)}</div>' if label else ''}
  <h1>{esc(title)}</h1>
  <div class="orn">❖</div>
  <div class="byline"><img src="assets/acharya-ji.jpg" alt="{esc(T['author'])}">
    <div class="who"><strong>{T['author']}</strong><span>{T['meta'].format(m=minutes)}</span></div></div>
  <div class="actions">{''.join(actions)}</div>
</div></section>
{f'<div class="wrap hero-img"><img src="assets/{hero}" alt="{esc(title)}"></div>' if hero else ''}

<main class="wrap layout">
  <article class="article">{body}{video_html}</article>
  <aside class="aside"><div class="sticky">
    <nav class="card toc"><h3>{T['toc']}</h3><ol>{toc_html}</ol></nav>
    <div class="card author"><img src="assets/acharya-ji.jpg" alt="{esc(T['author'])}">
      <div><strong>{T['author']}</strong><p>{T['bio']}</p><a class="more" href="{T['about_url']}">{T['about']} →</a></div></div>
  </div></aside>
</main>

<section class="cta"><div class="wrap">
  <h2>{T['cta_h']}</h2><p>{T['cta_p']}</p>
  <div class="actions"><a class="btn btn-solid" href="{SITE['courses']}">{T['cta_1']}</a>
  <a class="btn btn-ghost" href="{SITE['signup']}">{T['cta_2']}</a></div>
</div></section>
</div>'''
    return {'lang': lang, 'title': title, 'author': T['author'], 'html': html_}


def site_header(switch=''):
    """Site header with logo, optional language switch and navigation (assets/ next to the page)."""
    nav = ''.join(f'<a href="{u}"{" class=active" if n == "Blog" else ""}>{n}</a>' for n, u in SITE['nav'])
    return f'''<header class="site-header"><div class="wrap">
  <a class="logo" href="{SITE['home']}"><img src="assets/logo.png" alt="Antar Yog Foundation"></a>
  {switch}
  <input type="checkbox" id="menu" class="menu-toggle"><label for="menu" class="menu-btn" aria-label="Menu"><span></span></label>
  <nav class="nav">{nav}<a class="btn btn-solid" href="{SITE['donate']}">Donate</a></nav>
</div></header>'''


def site_footer(motto):
    """Site footer with links and contact details."""
    links = lambda items: ''.join(f'<li><a href="{u}">{n}</a></li>' for n, u in items)  # noqa: E731
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div class="brand"><img src="assets/logo.png" alt="Antar Yog Foundation"><p>{motto}</p>
      <div class="social"><a href="{SITE['youtube']}" aria-label="YouTube">{icon('youtube')}</a>
      <a href="{SITE['instagram']}" aria-label="Instagram">{icon('instagram')}</a></div></div>
    <div><h4>Explore</h4><ul>{links(SITE['explore'])}</ul></div>
    <div><h4>Services</h4><ul>{links(SITE['services'])}</ul></div>
    <div><h4>Contact</h4><ul class="contact">
      <li>{icon('phone')}<a href="{SITE['phone'][1]}">{SITE['phone'][0]}</a></li>
      <li>{icon('mail')}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
      <li>{icon('pin')}<span>{SITE['address']}</span></li>
      <li>{icon('clock')}<span>{SITE['hours']}</span></li></ul></div>
  </div>
  <div class="legal"><span>© 2026 Antar Yog Foundation</span>
    <nav><a href="{SITE['privacy']}">Privacy Policy</a><a href="{SITE['terms']}">Terms</a></nav></div>
</div></footer>'''


SWITCH_JS = """
(function () {
  var blocks = document.querySelectorAll('[data-lang]');
  function show(lang) {
    var block = document.querySelector('[data-lang="' + lang + '"]');
    if (!block) return false;
    blocks.forEach(function (b) { b.hidden = b !== block; });
    document.documentElement.lang = lang;
    document.title = block.dataset.title;
    document.querySelectorAll('.lang-switch [data-switch]').forEach(function (a) {
      a.classList.toggle('active', a.dataset.switch === lang);
    });
    return true;
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-switch]');
    if (!a) return;
    e.preventDefault();
    if (show(a.dataset.switch)) {
      history.replaceState(null, '', '#' + a.dataset.switch);
      window.scrollTo(0, 0);
    }
  });
  var hash = location.hash.slice(1);
  var lang = hash.split('-')[0];
  if (lang && show(lang) && hash.indexOf('-') > 0) {
    var target = document.getElementById(hash);
    if (target) target.scrollIntoView();
  }
})();
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('chapters', nargs='+', metavar='chapter.txt')
    ap.add_argument('--video')
    ap.add_argument('--out')
    a = ap.parse_args()
    if len(a.chapters) > 2:
        ap.error('give at most two chapters (one per language)')

    out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.chapters[0])), 'blog', 'index.html')
    out_dir = os.path.dirname(os.path.abspath(out))
    assets = os.path.join(out_dir, 'assets')
    os.makedirs(assets, exist_ok=True)
    for f in ('logo.png', 'acharya-ji.jpg'):
        shutil.copy2(os.path.join(HERE, 'assets', f), assets)

    video = None
    if a.video:
        vtitle, vdur, thumb = video_info(a.video, assets)
        video = {'id': a.video, 'title': vtitle, 'duration': vdur, 'thumb': thumb}

    langs = ['hi' if re.search(r'[ऀ-ॿ]', open(c, encoding='utf-8').read()) else 'en' for c in a.chapters]
    if len(langs) == 2 and langs[0] == langs[1]:
        ap.error('the two chapters must be in different languages (one Hindi, one English)')
    blocks = [build_lang(c, out_dir, video, langs[1 - i] if len(langs) == 2 else None)
              for i, c in enumerate(a.chapters)]
    first = blocks[0]
    content = '\n'.join(b['html'].replace('<div class="lang-block"', '<div class="lang-block" hidden', 1) if i else b['html']
                        for i, b in enumerate(blocks))

    switch = ''
    if len(blocks) == 2:
        names = {'hi': 'हिन्दी', 'en': 'English'}
        switch = '<div class="lang-switch">' + ''.join(
            f'<a href="#{b["lang"]}" data-switch="{b["lang"]}"{" class=active" if i == 0 else ""}>{names[b["lang"]]}</a>'
            for i, b in enumerate(blocks)) + '</div>'


    page = f'''<!doctype html>
<html lang="{first['lang']}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(first['title'])} | Antar Yog Foundation</title>
<meta name="description" content="{esc(first['author'])} — {esc(first['title'])}">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}&family=Noto+Sans:wght@400;500;600&family=Noto+Sans+Devanagari:wght@400;500;600" rel="stylesheet">
<style>{open(os.path.join(HERE, 'blog.css'), encoding='utf-8').read()}</style>
</head><body>

{site_header(switch)}

{content}

{site_footer(TEXT[first['lang']]['motto'])}
{'<script>' + SWITCH_JS + '</script>' if switch else ''}
</body></html>
'''
    open(out, 'w', encoding='utf-8').write(page)
    print(f'Blog page: {out} ({", ".join(b["lang"] for b in blocks)})')


if __name__ == '__main__':
    main()
