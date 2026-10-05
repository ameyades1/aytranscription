---
name: dequote
description: Rewrite Acharya Ji's direct quotes in one talk's blog texts (output/<name>/<name>_blog.txt and _blog_en.txt) as ordinary text, keeping scripture verses. Blog texts only; chapters are not touched.
argument-hint: <talk name>
model: claude-opus-5-5
effort: low
---

# Remove direct quotes from a blog

This command runs on Claude Opus 5.5 at low effort (the `model` and `effort` fields above).

Talk: `$ARGUMENTS`. Edit exactly two files: `output/<name>/<name>_blog.txt` (Hindi) and
`output/<name>/<name>_blog_en.txt` (English). Do not touch any other file.

## What to change

A **speaker quote** is a `>` block whose lines are `> "..."` and whose first line is not
`**bold**`. Rewrite every speaker quote as ordinary text:

- Turn it into indirect speech in a normal paragraph, e.g. `> "आप कुछ समय के लिए चीनी भोजन चख
  सकते हैं..."` becomes `आचार्य जी कहते हैं कि हम कुछ समय के लिए चीनी भोजन चख सकते हैं...`.
  Attribution such as "Acharya Ji explains that" / "आचार्य जी बताते हैं कि" is fine.
- Keep the meaning exactly; add nothing the quote did not say. Shorten only filler.
- Merge it smoothly with the sentence before or after it, so no line like "Acharya Ji says:"
  is left introducing a quote that is gone. Avoid repeating what the next paragraph says.
- Keep the Hindi and English files parallel: the same quotes rewritten the same way.
- No em dashes (—).

## What to keep exactly as it is

- **Scripture verses:** any `>` block whose first line is `**bold**`, including its quoted
  meaning line and its `> (source)` line.
- Headings, reflective questions in `*italics*`, bullet lists, bold terms, and all other text.

## Check

When done, run `python3 tools/count_quotes.py <name>`; it must print `0`. Then reply with one
line: the number of quotes rewritten in each file.
