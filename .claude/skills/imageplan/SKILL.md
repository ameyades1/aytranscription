---
name: imageplan
description: Write ready-to-paste image prompts (a 16:9 hero and one inline image) for one or more blogs, into output/<name>/blog/image_plan.txt.
argument-hint: <talk name> [talk name ...]
model: claude-opus-5-5
effort: low
---

# Image prompts for blogs

This command runs on Claude Opus 5.5 at low effort (the `model` and `effort` fields above).

Talks: `$ARGUMENTS`. For each talk `<name>`, read `output/<name>/<name>_blog_en.txt` and the `##`
headings of `output/<name>/<name>_blog.txt`, then write `output/<name>/blog/image_plan.txt`
in exactly this format (one field per line, no blank lines, no other text):

```
hero_title: <2-5 word English title for the image>
hero: <ready-to-paste prompt>
hero_alt: <one-line English description of the image, for screen readers>
inline_title: <2-5 word English title>
inline: <ready-to-paste prompt>
inline_alt: <one-line English description>
inline_after_hi: <the Hindi ## heading the inline image follows, copied exactly, without "## ">
inline_after_en: <the matching English ## heading, copied exactly, without "## ">
```

Do not touch any other file.

## How to choose the images

- **Hero:** the mood and central idea of the whole blog.
- **Inline:** one concrete visual metaphor, example or story from a specific section (the canal
  and the stone, durva bending in the wind). Pick a section from the first two-thirds of the blog,
  never the takeaways section. The section's own headings must match the files exactly.
- Base both on what the blog actually says; never invent a story it does not contain.

## How to write each prompt

Each prompt is a single paragraph that can be pasted into an image generator as it is:

- Describe the scene concretely: subject, setting, composition, light, colours.
- Indian settings and people, shown authentically; warm natural light; cinematic, high detail.
- End every prompt with: `16:9 aspect ratio. No text, letters or writing anywhere in the image.`
- Deities and murtis: respectful, traditional iconography, restrained ornamentation.
- Avoid clichés: no neon or "New Age" glow, no stock-photo poses, no piles of gold coins.
- Never show death, suffering, violence or crime literally; use symbols instead.
- Prefer scenes without a recognisable face of Acharya Ji or any real person.
