---
name: diagram
description: Decide whether one talk's blog needs a small text diagram and, if it does, write output/<name>/blog/diagram.json (combine, compare, triad or steps; every label taken from the blog in Hindi and English), check it and rebuild the page; record the decision in output/<name>/blog/diagram.md either way. Most talks get none. The blog texts are not edited.
argument-hint: <talk name>
model: claude-opus-5-5
effort: medium
---

# Text diagram for one blog

This command runs on Claude Opus 5.5 at medium effort (the `model` and `effort` fields above).

Talk: `$ARGUMENTS` (`<name>`). All paths are relative to the repo root. Write only
`output/<name>/blog/diagram.json` (when there is a diagram) and `output/<name>/blog/diagram.md`;
the rebuild changes the generated pages. Never edit the blog texts, `seo.json` or `images.txt`.

## Step 1: Read

- The published texts: `output/<name>/<name>_blog_seo.txt` and `_blog_seo_en.txt` (else
  `_blog.txt` and `_blog_en.txt`).
- The `##` headings of the **original** texts `<name>_blog.txt` and `<name>_blog_en.txt` (the
  diagram is placed by these, as `images.txt` places the inline image).
- `output/<name>/blog/images.txt`: the section that already has the inline image.
- The spec format at the top of `tools/diagram.py`, and one example spec, for instance
  `output/three_gunas_karma/blog/diagram.json`.

## Step 2: Decide

A diagram is worth it only when the talk **teaches a structure** that the boxes make clearer than
the prose does. Most talks get none; when in doubt, none.

| Type | Use when the blog has | Example |
|---|---|---|
| `combine` | two things that together produce a third | inner guna + outer guna → action |
| `compare` | two paths, causes or kinds set against each other, with points for each | shreya vs preya |
| `triad` | three parallel parts of one whole (colours: `white`, `red`, `black` only when the blog gives them) | sattva, rajas, tamas |
| `steps` | a sequence of 2 to 5 stages or a chain of cause and effect, in order | desire → anger → delusion |

**No diagram** when the talk is mainly a story, an anecdote, devotion or exhortation; when the
structure is only a list of tips (the Key Takeaways already do that); when it would need more than
about 5 boxes or 8 list items; or when it would only restate a single sentence.

## Step 3: Write the spec (only if there is a diagram)

`output/<name>/blog/diagram.json`, in the format of `tools/diagram.py`:

- **Faithful.** Every label, note and item says only what the blog says, in its own words where
  possible; never a teaching, term or verse number the blog does not have. The Hindi labels come
  from the Hindi text, the English ones from the English text, and they match each other.
- **Short.** Labels of 1 to 4 words; notes and items under about 10 words. The title names what the
  diagram shows (under about 8 words); a scripture reference in it only when the section cites it.
- **Footer**: one closing line, only when it adds the takeaway the boxes cannot show. No caption,
  no alt text.
- **Section**: the original `##` heading (both languages, exactly as in the original texts) of the
  section that teaches the structure. Not the Key Takeaways section. Avoid the section of the
  inline image when another section fits as well.
- Hindi follows `tools/prompts/hindi_register.md` and says "आचार्य जी"; English says "Shibir" for
  शिविर. No em dashes.

## Step 4: Check and rebuild (only if there is a diagram)

```bash
python3 tools/diagram.py <name> hi        # prints the diagram as Markdown: read it once more
python3 tools/diagram.py <name> en
python3 tools/verify_seo_fix.py <name>    # must pass (it checks the diagram's section)
tools/rebuild_blogs.sh <name>
```

Fix the spec if a check fails.

## Step 5: Record

Write `output/<name>/blog/diagram.md` (replace it if it exists); it marks the talk as decided, so
batch runs skip it:

```
# <name>: diagram

Decision: <type> | none
Reason: <one sentence: the structure it shows, or why the talk gets none>
Section: <original English heading>   (only with a diagram)
```

Reply with one line: the decision and, with a diagram, its type and section.
