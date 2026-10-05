#!/usr/bin/env python3
"""Generate a blog's hero and inline image with AI Horde (free, crowdsourced), from tools/image_plan.md.

Usage: python3 tools/horde_image.py <talk_name> [--model flux|juggernaut] [--out DIR]

  --model   flux (Flux.1-Schnell, default) or juggernaut (Juggernaut XL)
  --out     folder to save into (default: output/<talk>/blog/assets); files are hero.jpg, inline.jpg

Set HORDE_API_KEY for an account key; without it the anonymous key is used (lowest priority).
"""
import argparse
import io
import os
import re
import sys
import time
import urllib.request
import json

from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(REPO, 'tools', 'image_plan.md')
API = 'https://aihorde.net/api/v2'
UA = 'aytranscription/1.0 (github.com/ameyades1/aytranscription)'
STYLE = 'Warm natural light, cinematic, high detail, authentic Indian setting. No text or lettering.'
NEGATIVE = 'text, letters, watermark, signature, blurry, deformed hands, extra limbs, nsfw'
MODELS = {
    'flux': {'name': 'Flux.1-Schnell fp8 (Compact)', 'steps': 4, 'cfg_scale': 1, 'sampler_name': 'k_euler'},
    'juggernaut': {'name': 'Juggernaut XL', 'steps': 30, 'cfg_scale': 6, 'sampler_name': 'k_dpmpp_2m'},
}


def plan_prompts(talk):
    text = open(PLAN, encoding='utf-8').read()
    ref = re.search(rf'^\[(\d+)\]: \S+/aytranscription/{re.escape(talk)}/blog/', text, re.M)
    if not ref:
        sys.exit(f'{talk} is not in image_plan.md')
    for line in text.splitlines():
        if line.startswith(f'| **{ref.group(1)}** |'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            return {'hero': clean(cells[2]), 'inline': clean(cells[3])}
    sys.exit(f'No row for {talk}')


def clean(cell):
    cell = re.sub(r'\(\[[^\]]*\]\[\d+\]\)', '', cell)
    cell = re.sub(r'Place after .*', '', cell)
    cell = re.sub(r'\*\*“[^”]*”\*\*\s*—\s*', '', cell)    # leading "Title" —
    cell = cell.replace('**', '').replace('*', '').replace('16:9.', '')
    return ' '.join(cell.split())


def call(method, path, body=None):
    req = urllib.request.Request(
        API + path, method=method, data=json.dumps(body).encode() if body else None,
        headers={'apikey': os.environ.get('HORDE_API_KEY', '0000000000'),
                 'Client-Agent': 'aytranscription:1.0:github.com/ameyades1',
                 'Content-Type': 'application/json', 'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def generate(prompt, model):
    m = MODELS[model]
    job = call('POST', '/generate/async', {
        'prompt': f'{prompt} {STYLE} ### {NEGATIVE}',
        'params': {'width': 1024, 'height': 576, 'steps': m['steps'], 'cfg_scale': m['cfg_scale'],
                   'sampler_name': m['sampler_name'], 'n': 1},
        'models': [m['name']], 'nsfw': False, 'censor_nsfw': True, 'r2': True,
    })
    jid = job['id']
    while True:
        time.sleep(10)
        s = call('GET', f'/generate/check/{jid}')
        if s.get('done'):
            break
        if not s.get('is_possible', True):
            sys.exit(f'No worker can run {m["name"]} right now')
        print(f'  waiting: queue position {s.get("queue_position")}, eta {s.get("wait_time")}s', flush=True)
    gen = call('GET', f'/generate/status/{jid}')['generations'][0]
    if gen.get('censored'):
        print('  note: image was censored by the safety filter')
    with urllib.request.urlopen(urllib.request.Request(gen['img'], headers={'User-Agent': UA}), timeout=120) as r:
        return Image.open(io.BytesIO(r.read())).convert('RGB')


def write_images_txt(talk):
    """blog/images.txt for the inline image: the plan names the English section; the Hindi one is
    the heading at the same position in the Hindi blog. Not overwritten if it exists."""
    blog = os.path.join(REPO, 'output', talk, 'blog')
    path = os.path.join(blog, 'images.txt')
    if os.path.exists(path):
        return
    text = open(PLAN, encoding='utf-8').read()
    ref = re.search(rf'^\[(\d+)\]: \S+/aytranscription/{re.escape(talk)}/blog/', text, re.M).group(1)
    row = next(l for l in text.splitlines() if l.startswith(f'| **{ref}** |'))
    m = re.search(r'Place after \*\*“(.+?)”\*\*', row)
    heads = lambda k: [l[3:].strip() for l in open(os.path.join(REPO, 'output', talk, f'{talk}_{k}.txt'),
                                                    encoding='utf-8') if l.startswith('## ')]
    en, hi = heads('blog_en'), heads('blog')
    if not m or m.group(1) not in en or len(en) != len(hi):
        print(f'  note: could not place the inline image for {talk}; add blog/images.txt by hand')
        return
    i = en.index(m.group(1))
    alt = re.sub(r'\*\*“[^”]*”\*\*\s*—\s*', '', row.split('|')[4]).split('.')[0].strip()
    open(path, 'w', encoding='utf-8').write(
        '# file | Hindi section heading | English section heading | description\n'
        f'inline.jpg | {hi[i]} | {en[i]} | {alt}\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('talk')
    ap.add_argument('--model', choices=MODELS, default='flux')
    ap.add_argument('--out')
    a = ap.parse_args()
    out = a.out or os.path.join(REPO, 'output', a.talk, 'blog', 'assets')
    os.makedirs(out, exist_ok=True)
    for kind, prompt in plan_prompts(a.talk).items():
        print(f'{kind} ({a.model}): {prompt[:90]}...', flush=True)
        img = generate(prompt, a.model)
        path = os.path.join(out, f'{kind}.jpg')
        img.save(path, 'JPEG', quality=88, optimize=True, progressive=True)
        print(f'  wrote {os.path.relpath(path, REPO)} {img.size}', flush=True)
    if not a.out:
        write_images_txt(a.talk)


if __name__ == '__main__':
    main()
