#!/usr/bin/env python3
"""Count speaker quotes left in a talk's blog texts.

Usage: count_quotes.py <name>   (prints the number; exit 0)

A speaker quote is a `> "..."` line in a quote block whose first line is not `**bold**`;
blocks starting with a bold line are scripture verses and are not counted.
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def count(path):
    n, block = 0, []
    for line in open(path, encoding='utf-8').read().splitlines() + ['']:
        if line.startswith('>'):
            block.append(line.lstrip('>').strip())
            continue
        if block and not block[0].startswith('**'):
            n += sum(1 for b in block if b.startswith('"'))
        block = []
    return n


name = sys.argv[1]
print(sum(count(os.path.join(REPO, 'output', name, f'{name}_{k}.txt'))
          for k in ('blog', 'blog_en') if os.path.exists(os.path.join(REPO, 'output', name, f'{name}_{k}.txt'))))
