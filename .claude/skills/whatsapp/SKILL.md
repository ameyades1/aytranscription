---
name: whatsapp
description: Write a short English WhatsApp message for one or more talks, linking only to the talk's YouTube video, into output/<name>/<name>_whatsapp_en.txt, following tools/prompts/whatsapp_template.md.
argument-hint: <talk name> [talk name ...]
model: claude-opus-5-5
effort: low
---

# WhatsApp messages for talks

Talks: `$ARGUMENTS`. For each talk `<name>`:

1. Read `tools/prompts/whatsapp_template.md` once and follow it exactly.
2. Read `output/<name>/<name>_blog_seo_en.txt`, or `output/<name>/<name>_blog_en.txt` if there
   is no SEO copy.
3. Find the video id: the `https://www.youtube.com/watch?v=<id> <name>` line in
   `batch_chapters.txt`, else the `watch?v=<id>` in `output/<name>/blog/index.html`. If neither
   has one, skip the talk and say so; never guess an id or use any other link.
4. Write `output/<name>/<name>_whatsapp_en.txt` with only the message text.

Check before saving: 40 to 60 words counted with `wc -w` (60 is a hard cap; trim and recount if over),
the reflection question makes sense to someone who has not read the blog (no undefined terms or
references like "the other" or "such questions"), five parts in the template's order, the only link is
`https://youtu.be/<id>`, no blog link, no direct quotes from Acharya Ji, nothing not in the blog,
no em dashes. If the talk is a testimonial or someone other than Acharya Ji speaks, say who
(e.g. "A seeker shares...") instead of "Acharya Upendra Ji explains". Do not touch any other file.
