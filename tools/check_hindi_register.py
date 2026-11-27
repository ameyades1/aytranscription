#!/usr/bin/env python3
"""Count the Hindi register words and speaker-name variants in each talk's Hindi blog.

Usage: check_hindi_register.py [--detail | --total] [--file <path>] [<talk> ...]
       (default: every talk with a Hindi blog)

Reads the word lists from tools/prompts/hindi_register.md (the same rules the blog and chapter
prompts follow) and counts, per blog:
  R1     Rule 1 words to review for replacement (ज़िंदगी, दुनिया, दिल, सिर्फ, खुद ...); the rules
         list exceptions (idioms, Acharya Ji's own catchphrases, SEO title and link phrases)
  R2     Rule 2 everyday words, allowed where natural (तरह, शायद, हमेशा ...): for information
  R3     Rule 3 archaic words that should not be used (कदाचित्, अतः, तथापि ...)
  Names  speaker-name variants other than "आचार्य जी" (आचार्यजी, गुरुजी, गुरुदेव ...); गुरुजी /
         गुरुदेव can be correct when they mean someone else, so check each one in context
  R1/1k  Rule 1 words per 1000 words

The text checked is <talk>_blog_seo.txt when /seo_blog_fix has written it (that is what gets
published), else <talk>_blog.txt. Verse blocks (lines starting with ">") are skipped. It only
reads; nothing is changed. --detail lists every word found, with its line numbers. --total
prints only one number, R1 + R3 + Names over the talks given (for scripts: 0 means nothing to
review).
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / 'tools' / 'prompts' / 'hindi_register.md'
OUTPUT = ROOT / 'output'
DEV = 'ऀ-ॿ'
SUFFIX = '(?:ों|ें)?'          # plural / oblique endings: दिलों, कोशिशें


def load_rules():
    """{group: {word: replacement}} from the markdown lists, by section heading."""
    groups, group = defaultdict(dict), None
    for line in RULES.read_text(encoding='utf-8').splitlines():
        if line.startswith('## '):
            h = line[3:]
            group = ('R1' if 'Rule 1' in h else 'R2' if 'Rule 2' in h else
                     'R3' if 'Rule 3' in h else 'Names' if 'name' in h else None)
        elif group and line.startswith('- ') and '→' in line:
            word, repl = (s.strip() for s in line[2:].split('→', 1))
            groups[group][word] = repl
    return groups


def pattern(word):
    return re.compile(f'(?<![{DEV}]){re.escape(word)}{SUFFIX}(?![{DEV}])')


def blog_file(talk):
    d = OUTPUT / talk
    for name in (f'{talk}_blog_seo.txt', f'{talk}_blog.txt'):
        if (d / name).is_file():
            return d / name
    return None


def check(path, rules):
    """{group: Counter(word)}, {word: [line numbers]}, word count."""
    counts, where, words = defaultdict(Counter), defaultdict(list), 0
    pats = {g: [(w, pattern(w)) for w in ws] for g, ws in rules.items()}
    for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if line.lstrip().startswith('>'):
            continue
        words += len(line.split())
        for g, plist in pats.items():
            for w, p in plist:
                k = len(p.findall(line))
                if k:
                    counts[g][w] += k
                    where[w].append(n)
    return counts, where, words


def main(argv):
    detail, total = '--detail' in argv, '--total' in argv
    argv = [a for a in argv if a not in ('--detail', '--total')]
    files = []
    if '--file' in argv:
        i = argv.index('--file')
        files.append((Path(argv[i + 1]).stem, Path(argv[i + 1])))
        del argv[i:i + 2]
    talks = argv or ([] if files else sorted(p.name for p in OUTPUT.iterdir() if blog_file(p.name)))
    for t in talks:
        f = blog_file(t)
        if f:
            files.append((t, f))
        else:
            print(f'{t}: no Hindi blog found', file=sys.stderr)

    rules = load_rules()
    groups = ['R1', 'R2', 'R3', 'Names']
    totals = defaultdict(Counter)
    rows = []
    for talk, f in files:
        counts, where, words = check(f, rules)
        for g in groups:
            totals[g].update(counts[g])
        r1 = sum(counts['R1'].values())
        rows.append((talk, *(sum(counts[g].values()) for g in groups), r1 * 1000 / max(words, 1)))
        if detail:
            print(f'\n{talk}  ({f.name}, {words} words)')
            for g in groups:
                for w, k in counts[g].most_common():
                    lines = ', '.join(map(str, sorted(set(where[w]))))
                    print(f'  {g:5} {w} ×{k} → {rules[g][w]}   (lines {lines})')

    if total:
        print(sum(sum(totals[g].values()) for g in ('R1', 'R3', 'Names')))
        return
    if not detail:
        width = max([len(r[0]) for r in rows] + [4])
        print(f'{"Talk":{width}}  {"R1":>4} {"R2":>4} {"R3":>4} {"Names":>5} {"R1/1k":>6}')
        for r in sorted(rows, key=lambda r: -r[5]):
            print(f'{r[0]:{width}}  {r[1]:4} {r[2]:4} {r[3]:4} {r[4]:5} {r[5]:6.1f}')
    print(f'\n{len(rows)} blog(s). Totals:')
    for g in groups:
        top = ', '.join(f'{w} {k}' for w, k in totals[g].most_common(8))
        print(f'  {g:5} {sum(totals[g].values()):5}   {top}')


if __name__ == '__main__':
    main(sys.argv[1:])
