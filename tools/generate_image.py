#!/usr/bin/env python3
"""Generate each blog's hero and inline image with Gemini (gemini-3.1-flash-image), from tools/image_plan.md.

Usage: GEMINI_API_KEY=... tools/image-env/bin/python tools/generate_image.py [talk_name ...] [--force]

  talk_name   Only these talks (default: every talk in the plan)
  --force     Generate again even if the image already exists

Images are written to output/<talk>/blog/assets/hero.jpg and inline.jpg. The talk name comes
from the blog link in the plan; the prompt is the plan's description, without its
"Place after ..." note.
"""
import io
import os
import re
import sys

from google import genai
from google.genai import types
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(REPO, 'tools', 'image_plan.md')
MODEL = 'gemini-3.1-flash-image'
STYLE = 'Cinematic, high detail, cultural authenticity, warm natural light. No text or lettering in the image.'


def clean(cell):
    """Plan cell -> prompt text."""
    cell = re.sub(r'\(\[[^\]]*\]\[\d+\]\)', '', cell)    # ([Ameya Desai][n])
    cell = re.sub(r'Place after .*', '', cell)          # placement note and what follows
    cell = cell.replace('**', '').replace('*', '')
    cell = re.sub(r'\b16:9\.?', '', cell)
    return ' '.join(cell.split()).strip(' —')


def read_plan():
    text = open(PLAN, encoding='utf-8').read()
    links = dict(re.findall(r'^\[(\d+)\]: https://\S+/aytranscription/([^/]+)/blog/', text, re.M))
    plan = []
    for line in text.splitlines():
        m = re.match(r'\|\s*\*\*(\d+)\*\*\s*\|', line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        ref = re.search(r'\]\[(\d+)\]\)', cells[3])
        talk = links.get(ref.group(1)) if ref else None
        if talk:
            plan.append((talk, {'hero': clean(cells[2]), 'inline': clean(cells[3])}))
    return plan


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    force = '--force' in sys.argv
    key = os.environ.get('GEMINI_API_KEY')
    if not key:
        sys.exit('Set GEMINI_API_KEY first.')
    client = genai.Client(api_key=key)

    for talk, prompts in read_plan():
        if args and talk not in args:
            continue
        assets = os.path.join(REPO, 'output', talk, 'blog', 'assets')
        os.makedirs(assets, exist_ok=True)
        for kind, prompt in prompts.items():
            out = os.path.join(assets, f'{kind}.jpg')
            if os.path.exists(out) and not force:
                print(f'skip   {talk}/{kind}.jpg (exists)')
                continue
            response = client.models.generate_content(
                model=MODEL,
                contents=f'{prompt} {STYLE}',
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE'],
                    image_config=types.ImageConfig(aspect_ratio='16:9'),
                ),
            )
            parts = response.candidates[0].content.parts if response.candidates else []
            data = next((p.inline_data.data for p in parts or [] if p.inline_data), None)
            if not data:
                print(f'FAILED {talk}/{kind}.jpg (no image returned)')
                continue
            Image.open(io.BytesIO(data)).convert('RGB').save(out, 'JPEG', quality=85, optimize=True, progressive=True)
            print(f'wrote  {os.path.relpath(out, REPO)}')


if __name__ == '__main__':
    main()
