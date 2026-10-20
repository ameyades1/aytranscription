---
name: seo_blog_fix
description: Write SEO-improved copies of one talk's blog texts, output/<name>/<name>_blog_seo.txt (Hindi) and output/<name>/<name>_blog_seo_en.txt (English), fixing the unmet items of its SEO report's checklist with the smallest faithful edits, following tools/prompts/seo_blog_specialist.txt, then updates seo.json (focus keyword, slug, title, meta description) to match the fixed texts and rebuilds the talk's blog page from them. The original blog texts are not changed. No WordPress work.
argument-hint: <talk name>
model: claude-opus-5-5
effort: medium
---

# SEO-improved copy of a blog

This command runs on Claude Opus 5.5 at medium effort (the `model` and `effort` fields above).

Arguments: `$ARGUMENTS`. The first word is the talk name (`<name>` below).

1. Read `tools/prompts/seo_blog_specialist.txt` and follow its rules, above all the guiding
   principles: truth comes before traffic, no clickbait, and Hindi and English are optimized
   separately.
2. Read the SEO report `output/<name>/blog/seo_report.md` (its keyword table, section 2's
   keyword notes and section 12, the SEO checklist), `output/<name>/blog/seo.json`, and both
   blog texts: `output/<name>/<name>_blog.txt` and `output/<name>/<name>_blog_en.txt`. If
   there is no report or seo.json, stop and say to run `/seo_blog <name>` first. If
   `tools/review/<name>.md` exists, read it too.
3. Copy each blog text to its `_seo` file (`<name>_blog.txt` → `<name>_blog_seo.txt`,
   `<name>_blog_en.txt` → `<name>_blog_seo_en.txt`), then edit only the copies. Fix what the
   report found, for each language:
   - Searched wording missing from the body (section 2's mismatch note, for example
     "33 crore gods" when the body only says "thirty-three crore gods"): use the searched
     wording naturally once in the first 100 words, and where it reads well, once in a `##`
     heading or a later paragraph.
   - Focus keyword not in the first 100 words: work it into the opening paragraph.
   - Headings: rephrase one or two `##` headings as the natural questions readers search for,
     when the section answers that question. Keep their number and order.
   - No direct answer early: if the opening does not answer the main question, add a short
     answer (40–60 words) built only from what the blog already says.
   - Any other unmet checklist item that the blog text itself can fix.
4. Edit as little as possible:
   - Never change a teaching, an example, the order of ideas or Acharya Ji's meaning. Add no
     claim, scripture or fact that the blog does not already contain.
   - Never touch scripture verses, their translations or references, or the H1.
   - Keep the Markdown format of the original (headings, bold, lists, blockquotes, italics).
   - Keep every phrase in seo.json's `links` and every `also_read` heading word for word, so
     the links still work with the new text.
   - No keyword stuffing: a keyword appears where it reads naturally, at most about once per
     section.
   - Hindi stays natural Hindi and English natural English; don't translate a keyword from one
     language into the other.
5. Check the copies:
   - Compare each copy with its original (`diff output/<name>/<name>_blog_en.txt
     output/<name>/<name>_blog_seo_en.txt`) and read every change: each must be needed for SEO
     and faithful to the talk. Undo anything that is not.
   - Confirm with `grep` that the searched wording and the focus keyword now appear in the body,
     and that every `links` phrase and `also_read` heading is still there.
6. Update `output/<name>/blog/seo.json` to the `_seo` texts (they are what gets published to
   WordPress), for each language, following the `/seo_blog` rules
   (`.claude/skills/seo_blog/SKILL.md`, "SureRank checks" and step 5):
   - `focus_keyword`: the searched wording if the `_seo` text now uses it, else keep it. Move
     the old focus keyword into `secondary_keywords` if it is still worth targeting (2 to 4).
     It must stay unique across all talks.
   - `slug` (English): built from the English focus keyword, short (at most 55 characters),
     lowercase and hyphenated, unique across all talks (for example `33-crore-gods-one-god`).
     The Hindi slug follows the same idea in Latin letters.
   - `title` and `meta_description`: rewrite only if they no longer contain the focus keyword,
     keeping the limits (60; 140–155 English, at most 160 Hindi).
   - `links` and `also_read`: unchanged unless an edit touched a phrase or heading; then copy
     the new wording exactly.
   Then put the same JSON in the report's section 11 block (the check compares them), and
   update the report to match, so no part of it is stale:
   - section 2's keyword note;
   - section 3: mark the title, meta description and slug now in seo.json as the recommended
     ones, for each language, copied exactly (add them if the fix wrote new ones);
   - section 8: the schema's headline/alternativeHeadline, description, keywords and URL slugs;
   - the section 12 checklist marks.
7. Run `python3 tools/check_seo.py <name>` (it checks against the `_seo` texts when they
   exist). Fix every error in the `_seo` texts or seo.json, within the rules above, and run it
   again until the talk passes.
8. Rebuild the blog page from the `_seo` texts with `tools/rebuild_blogs.sh <name>` (it uses the
   `_seo` copies when they exist, and also rebuilds the pages that link to this talk and the
   blog index). Any "Note:" line other than "could not read video details" means a link phrase,
   heading or talk was not found: fix the `_seo` text or seo.json within the rules above, run the
   check again and rebuild until there are none.
9. Write `output/<name>/blog/seo_fix.md` (after the last edit to the `_seo` texts, so it lists
   every change):
   - First line: `<name>: SEO fix`.
   - For each language, a table of every change (where | before | after | why).
   - The checklist items now met, and those still unmet with the reason.
   - Every seo.json change (field | before | after), including the old and new slug.
   - Last, a `## Final seo.json values` section: a table (field | Hindi | English) with the
     slug, focus keyword, title and meta description exactly as they are in seo.json at the
     end, whether or not they changed. `tools/verify_seo_fix.py` compares it with seo.json.

10. Run `python3 tools/verify_seo_fix.py <name>`: it checks that nothing is stale (fixed texts,
    seo_fix.md, the page, report section 3) and that WordPress would place every image. Fix every
    error and warning, then run it again until the talk passes with no warnings.

Rules:
- Write only the two `_seo` text files, seo.json, the report (sections 2, 3, 8, 11 and 12) and
  `seo_fix.md`, and rebuild pages only with `tools/rebuild_blogs.sh`. Never change the original
  blog texts or the images.
- No WordPress work: never import, export or touch the local WordPress. That is
  `publish_wordpress.sh`'s job, later in the pipeline.
- If nothing in a language needs fixing, still write its `_seo` copy (unchanged) and say so in
  seo_fix.md.

Reply with one line: the number of changes in each language, the new focus keyword and slug
(English), and the number of checklist items still unmet.
