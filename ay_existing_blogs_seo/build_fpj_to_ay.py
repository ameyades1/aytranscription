"""Build fpj_to_ay.json: the FPJ SEO data and "Also Read" boxes to apply to each AY blog copy.

Reads identical_blogs.json, fpj_blogs/ and ay_blogs/ (never writes them). For each of the AY posts
that has an FPJ original, the record holds:
  - seo: FPJ's SEO title, meta description, Open Graph and Twitter text, keywords, H2 subheading and
    hero alt text, copied word for word
  - canonical_options: the AY page itself and the FPJ article (the plugin lets the user choose)
  - also_read: FPJ's "Also Read" boxes, each pointing to the AY copy of its target, placed after the
    AY paragraph that matches the paragraph the box follows on FPJ
  - skipped_also_read: boxes whose target has no AY copy (left out, per the plan)
Run from this folder: python3 build_fpj_to_ay.py
"""
import difflib
import json
import re

MIN_MATCH = 0.8  # how closely an AY paragraph must match the FPJ text a box follows


def load(path):
    return json.load(open(path, encoding='utf-8'))


def slug_of(link):
    return link.rstrip('/').rsplit('/', 1)[1]


def norm(text):
    """Text for matching: no Markdown, quotes or dashes unified, spaces collapsed, lowercase."""
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'[*_#>]|<[^>]+>', '', text)
    text = text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    text = re.sub(r'[–—-]', '-', text)
    return re.sub(r'\s+', ' ', text).strip().lower()


def ay_paragraphs(slug):
    """The AY post's body paragraphs, in order, as in its .md (headings, images and the byline left out)."""
    lines = open(f'ay_blogs/{slug}/{slug}.md', encoding='utf-8').read().split('\n')
    lines = lines[next(i for i, l in enumerate(lines) if l.startswith('*By ')) + 1:]
    return [l for l in lines if l.strip() and not l.startswith(('#', '!['))]


def place(snippet, paras, start):
    """(index after which the box goes, score): the paragraph at or after start whose end best matches snippet."""
    want = norm(snippet)
    best, score = None, 0.0
    for i in range(start, len(paras)):
        tail = norm(paras[i])[-len(want):]
        r = 1.0 if want in norm(paras[i]) else difflib.SequenceMatcher(None, want, tail, autojunk=False).ratio()
        if r > score:
            best, score = i, r
    return best, score


def main():
    pairs = load('identical_blogs.json')
    fpj = {f['link']: f for f in load('fpj_blogs/fpj_articles.json')}
    ay = {a['link']: a for a in load('ay_blogs/ay_articles.json')}
    to_ay = {p['fpj_link']: p['ay_link'] for p in pairs}

    records, warnings = [], []
    for p in pairs:
        f, a = fpj[p['fpj_link']], ay[p['ay_link']]
        fs, slug = f['seo'], slug_of(p['ay_link'])
        meta = fs['meta']
        seo = {
            'seo_title': fs['title_tag'],
            'meta_description': meta.get('description'),
            'og_title': meta.get('og:title'),
            'og_description': meta.get('og:description'),
            'twitter_title': meta.get('twitter:title'),
            'twitter_description': meta.get('twitter:description'),
            'keywords': meta.get('keywords'),
            'subheading': next((h['text'] for h in fs['headings'] if h['tag'] == 'h2'), None),
            'featured_image_alt': fs['images'][0]['alt'] if fs['images'] else None,
        }

        paras = ay_paragraphs(slug)
        boxes, skipped, start = [], [], 0
        for n, link in enumerate(fs['also_read_links'], 1):
            pos = link['position']
            target = to_ay.get(link['href'])
            if not target:
                skipped.append({'fpj_title': link['text'], 'fpj_link': link['href'],
                                'reason': 'no AY copy of the target article'})
                continue
            if pos['preceding_paragraph_end'] is None:  # the box opens the article
                after, score = -1, 1.0
            elif pos['following_paragraph_start'] is None:  # the box closes the article (on FPJ often after
                after, score = len(paras) - 1, 1.0          # an author note the AY copy doesn't have)
            else:
                after, score = place(pos['preceding_paragraph_end'], paras, start)
            box = {
                'box_number': n,
                'label': pos['box_label'],
                'target_title': ay[target]['title'],
                'target_link': target,
                'target_slug': slug_of(target),
                'target_featured_image': next((i['src'] for i in ay[target]['seo']['images'] if i['role'] == 'featured'), None),
                'after_ay_paragraph': after + 1,  # 1-based; 0 = before the first paragraph
                'ay_paragraph_count': len(paras),
                'ay_paragraph_end': norm(paras[after])[-120:] if after >= 0 else None,
                'match_score': round(score, 3),
                'fpj_after_paragraph': pos['after_paragraph'],
                'fpj_paragraph_end': pos['preceding_paragraph_end'],
            }
            if score < MIN_MATCH:
                warnings.append(f'{slug}: box {n} ("{link["text"]}") matched only {score:.2f}')
            else:
                start = after  # boxes keep FPJ's order
            boxes.append(box)

        records.append({
            'ay_slug': slug,
            'ay_link': p['ay_link'],
            'ay_title': a['title'],
            'fpj_link': p['fpj_link'],
            'fpj_title': f['title'],
            'canonical_options': {'ay': p['ay_link'], 'fpj': p['fpj_link']},
            'seo': seo,
            'also_read': boxes,
            'skipped_also_read': skipped,
        })

    json.dump(records, open('fpj_to_ay.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'{len(records)} posts, {sum(len(r["also_read"]) for r in records)} Also Read boxes, '
          f'{sum(len(r["skipped_also_read"]) for r in records)} skipped')
    for w in warnings:
        print('Check:', w)


if __name__ == '__main__':
    main()
