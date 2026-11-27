---
name: hindi_register
description: Bring one talk's Hindi blog text into the tatsama-leaning register of tools/prompts/hindi_register.md, replacing only the flagged words that read naturally replaced (Rule 1 words, archaic words, speaker-name variants), keeping idioms, Acharya Ji's catchphrases and SEO text, and record every decision in output/<name>/blog/hindi_register.md. Hindi only; English is not touched.
argument-hint: <talk name>
model: claude-opus-5-5
effort: medium
---

# Hindi register edit for one blog

This command runs on Claude Opus 5.5 at medium effort (the `model` and `effort` fields above).

Talk: `$ARGUMENTS` (`<name>`). All paths are relative to the repo root.

**The text to edit** is the Hindi text that gets published: `output/<name>/<name>_blog_seo.txt`
when it exists (after `/seo_blog_fix`), else `output/<name>/<name>_blog.txt` (a new blog, before
the SEO steps). Edit only that file, and write the record file below. Do not touch the English
text, `seo.json`, the chapter or anything else.

## Step 1: Find the words

Read `tools/prompts/hindi_register.md` (the rules) and run:

```bash
python3 tools/check_hindi_register.py --detail <name>
```

It lists each flagged word with its suggested replacement and line numbers: `R1` (Rule 1 words),
`R3` (archaic words), `Names` (speaker-name variants). `R2` words are allowed; leave them alone.

## Step 2: Decide each one, in context

Read each flagged line in full and decide **replace** or **keep**. Make the smallest faithful
change: the word itself, plus any grammar its replacement needs (for example "असर नहीं करता" →
"प्रभाव नहीं डालता"). Do not rewrite or improve anything else.

Keep the word when:
- it is part of a **fixed idiom** (दुनिया भर, खुद-ब-खुद, दिल से), where the replacement reads oddly;
- it is part of **Acharya Ji's own challenge or catchphrase**, a phrase he uses as a direct appeal
  (for example "खुद को खाकर दिखाओ");
- it is in the **title, a heading that matches the focus keyword or how people search, or an SEO
  link phrase**: when `output/<name>/blog/seo.json` exists, keep any word inside its `title.hi`,
  `wordpress.hi.focus_keyword`, a `links[].hi` phrase or `also_read.after.hi`;
- the replacement would repeat a word already in the same sentence, or would sound stilted.

When in doubt, keep.

**Name variants:** replace गुरुजी, गुरु जी, गुरुदेव or आचार्य श्री with "आचार्य जी" only when it means
Acharya Upendra Ji. Keep it when it is someone else (his own Guru, a Guru in general) or a
disciple's own words of address. Always replace "आचार्यजी" with "आचार्य जी".

## Step 3: Check

```bash
python3 tools/check_hindi_register.py --detail <name>
python3 tools/check_seo.py <name>      # only when output/<name>/blog/seo.json exists
```

`check_seo.py` must pass. If it fails because of your edit, undo that edit (keep the word) and run
it again. What the register check still lists must be exactly the words you decided to keep.

Then rebuild the page and those that link to it, if the page exists:
`tools/rebuild_blogs.sh <name>`.

## Step 4: Record

Write `output/<name>/blog/hindi_register.md` (replace it if it exists):

```
# <name>: Hindi register

File: <the file edited>

## Replaced
- line <n>: <old phrase> → <new phrase>

## Kept
- line <n>: <word> in "<short phrase>": <reason (idiom / catchphrase / SEO title / repeats / stilted / another Guru)>
```

Write "- none" under an empty section. This file marks the talk as done, so batch runs skip it.

Reply with one line: the number of words replaced and kept, and whether `check_seo.py` passed.
