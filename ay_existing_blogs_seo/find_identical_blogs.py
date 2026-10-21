"""Match FPJ articles with their copies on the AY blog by comparing article text.

Writes identical_blogs.json: one entry per pair, with titles, links and text similarity (0-1).
Run from this folder: python3 find_identical_blogs.py
"""
import json, re, difflib

THRESHOLD = 0.6


def body_words(article, folder):
    slug = article['link'].rstrip('/').rsplit('/', 1)[1]
    lines = open(f'{folder}/{slug}/{slug}.md', encoding='utf-8').read().split('\n')
    lines = lines[next(i for i, l in enumerate(lines) if l.startswith('*By ')) + 1:]
    text = ' '.join(l for l in lines if not l.startswith('> **'))  # drop "Read Also" boxes
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)|[*#]', r'\1', text)
    return text.lower().split()


fpj = json.load(open('fpj_blogs/fpj_articles.json', encoding='utf-8'))
ay = json.load(open('ay_blogs/ay_articles.json', encoding='utf-8'))
fpj_words = {f['link']: body_words(f, 'fpj_blogs') for f in fpj}
fpj_titles = {f['link']: f['title'] for f in fpj}

pairs = []
for a in ay:
    words = body_words(a, 'ay_blogs')
    scores = {u: difflib.SequenceMatcher(None, words, w, autojunk=False).ratio() for u, w in fpj_words.items()}
    best = max(scores, key=scores.get)
    if scores[best] >= THRESHOLD:
        pairs.append({'fpj_title': fpj_titles[best], 'fpj_link': best,
                      'ay_title': a['title'], 'ay_link': a['link'],
                      'text_similarity': round(scores[best], 3)})

json.dump(pairs, open('identical_blogs.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'{len(pairs)} pairs written to identical_blogs.json')
