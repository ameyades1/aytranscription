---
name: seo_blog
description: Write an SEO report for one talk's blog (output/<name>/<name>_blog.txt and _blog_en.txt) as a Senior SEO Blog Specialist for Indian spirituality, following tools/prompts/seo_blog_specialist.txt, and save it to output/<name>/blog/seo_report.md, plus output/<name>/blog/seo.json for the page generator (title tag, image alt text and captions, internal links, Also read, Further reading, and the WordPress slug, keywords, meta description, category and tags). The blog text is not edited.
argument-hint: <talk name> [--no-rebuild]
model: claude-opus-5-5
effort: medium
---

# SEO report for a blog

This command runs on Claude Opus 5.5 at medium effort (the `model` and `effort` fields above).

Arguments: `$ARGUMENTS`. The first word is the talk name (`<name>` below). With
`--no-rebuild` (used by `batch_seo.sh`, which rebuilds all pages once at the end), skip step 6.

1. Read `tools/prompts/seo_blog_specialist.txt` and follow it exactly.
2. Read the Hindi blog `output/<name>/<name>_blog.txt`, then the English blog
   `output/<name>/<name>_blog_en.txt`. If `output/<name>/blog/image_plan.txt` or
   `tools/review/<name>.md` exist, read them too: use the image plan for file names and alt
   text, and carry any Sanskrit review issues into the authenticity flags.
3. For internal links, list the other talks with `ls output/` and link only to blogs that
   exist there. Never invent a post.
4. Write the report to `output/<name>/blog/seo_report.md` in the prompt's 11-section output format
   (section 11 is written in step 5, section 12 in step 8).
   The first line is `<name>: SEO report`, with the talk name written exactly as given and
   no escaped underscores.
   Section 8 (Schema) is for later use in WordPress and is never added to the page. Give one
   complete JSON-LD block for each language (Hindi, then English), each a single `@graph` with:
   BlogPosting (headline = that language's H1, alternativeHeadline = the recommended title,
   description = that language's meta description, inLanguage `hi`/`en`, keywords, about,
   image, datePublished, dateModified, author, publisher, mainEntityOfPage, video,
   translationOfWork/workTranslation linking the two), Person (Acharya Ji), Organization
   (Antar Yog Foundation), VideoObject (only if the page has a YouTube video) and BreadcrumbList.
   Take facts only from sources: dates from `git log --format=%ad --date=short --
   output/<name>/<name>_blog.txt` (oldest = published, newest = modified); the video's upload
   date, duration and title from yt-dlp (`yt-dlp --skip-download --print
   "%(upload_date)s %(duration)s %(title)s" <ID>`), the ID from the page's YouTube link.
   Anything unknown, such as the WordPress URLs, stays a clearly marked `{{PLACEHOLDER}}`.
   After the blocks, add a short note mapping the fields to the WordPress SEO plugin (which
   ones it fills itself, which must be entered by hand).
5. Write `output/<name>/blog/seo.json` from the report, in the format described at the top of
   `tools/template/blog_page.py` (only these keys):
   - `title`: the recommended title tag for each language (section 3, the option marked
     recommended), at most 60 characters. This is the `<title>` tag only; the H1 in the blog
     text is not changed.
   - `alt`: alt text for each language for the images in `output/<name>/blog/assets/` that the
     page shows (`hero.jpg`, `inline.jpg` and the video thumbnail `<video ID>.jpg`), keyed by
     the existing file name (section 9). Look at
     each image before describing it. Never rename image files: the image tools, the gallery
     and the generator all rely on these names.
   - `caption`: a short visible caption for each language for `hero.jpg` and `inline.jpg`
     (section 9), keyed by file name. A few words that tie the image to the talk's message
     (for example "एक ज्योति, अनेक दीप" / "One flame, many lamps"), not a repeat of the alt text
     or the title. Leave an image out if no caption adds meaning.
   - `links`: the in-text links (section 7). Each phrase must be copied exactly from a paragraph
     or list item of that language's blog text (not a heading or verse), and should appear
     there before any other occurrence you don't want linked. 3 to 5 links per language.
   - `also_read`: one talk, placed after the `##` heading (copied exactly, per language) of the
     section it extends best.
   - `related`: the 3 talks that suit a reader of this blog best.
   - `wordpress`: the values to enter in WordPress (the page generator ignores this key):
     - `category`: the talk's topic key in `gallery_topics.txt`, copied as is (the
       `topic <key> | <English> | <Hindi>` lines give the WordPress category names). These 14
       categories are the approved list; never invent or rename one. If the talk is not listed
       there, choose one by the rules below and say so in the reply, so it can be added to
       `gallery_topics.txt`:
       - One category per post: the main thing the post is about.
       - `festivals` only when the post is about the festival itself (how and why it is
         observed). When a festival is just the occasion, use the topic's category and add the
         festival as a tag (for example, why Ganesha loves red flowers → `deities`, tag Ganesh
         Chaturthi).
       - Pitru Paksha, shraddha and pind daan go to `pitru`, not `festivals`.
     - `hi` and `en`, each with:
       - `slug`: section 3's slug without the `/hi/` or `/en/` prefix: short, lowercase,
         Latin letters, words joined by hyphens, at most 55 characters (SureRank warns when the
         page URL is over 90 characters).
       - `focus_keyword`: the primary keyword for that language (section 2). It must pass
         SureRank's keyword checks (see "SureRank checks" below).
       - `secondary_keywords`: 2 to 4 more keywords for that language (section 2).
       - `meta_description`: section 3's meta description, 140 to 155 characters for English
         and at most 160 for Hindi. It contains the focus keyword.
       - `tags`: 3 to 6 tags in that language, naming the talk's main concepts, deities,
         festivals or texts (Ganesh, Pitru Paksha, Bhagavad Gita, Advaita Vedanta). Series
         such as Ganesh Vidya are tags, not categories. Reuse a tag already used in another
         talk's seo.json when it means the same thing
         (`grep -h -A8 '"tags"' output/*/blog/seo.json`); never create near-duplicates
         (Self Control / Sense Control, Ganesh / Lord Ganesha). A tag should be one that at
         least 3 posts can share.
         - Never use a category name, or a broad label that only restates a category, as a
           tag (Festivals, Hindu Festivals, Deities, Ancestors & Shraddha): the category
           already groups those posts.
         - A series tag uses the series' own name exactly as the video title or thumbnail
           gives it (for example Ganesh Series), written the same way in every post of the
           series. Don't also add a separate deity tag unless the post is about that deity.
       - The focus keyword must not be another talk's focus keyword
         (`grep -h '"focus_keyword"' output/*/blog/seo.json`). If two talks would target the
         same query, pick the narrower query this talk answers best, and note the overlap in
         section 7 (cannibalization).
   Use only talks whose `output/<talk>/blog/index.html` exists. Add nothing else to seo.json:
   the FAQ and the schema stay in the report only.
   Then add section 11 to the report: `## 11. seo.json`, a one-line note, and the complete
   seo.json in a single ```json block, exactly as written. Whenever seo.json changes later
   (for example while fixing step 6 or 7), update this block too; the check compares them.
6. If `output/<name>/blog/index.html` exists, rebuild it with `tools/rebuild_blogs.sh <name>`
   (it keeps the page's YouTube video and also rebuilds the pages that link to this talk and
   the blog index). Any "Note:" line means a phrase, heading or talk
   was not found: fix seo.json and rebuild until there are none.
7. Run `python3 tools/check_seo.py <name>`. Fix every error it lists in seo.json or the report
   and run it again until the talk passes. Warnings may stay, but fix them if you can.
8. Add the SEO checklist as the report's last section: copy `tools/prompts/seo_checklist.md`
   to the end of the report (after section 11) and mark each item for this talk: `[x]` when it
   is met, `[ ]` when not, with a short reason after any unmet item (for example "focus keyword
   not in the first 100 words"). Base the marks on what was actually written and on the check
   in step 7, not on intent. Keep the "Not covered" list as it is.

SureRank checks (the WordPress SEO plugin; `tools/check_seo.py` checks all of these):
- The focus keyword must appear, for each language, in that language's:
  - title tag (`title`),
  - meta description,
  - blog body text (the paragraphs, lists and headings below the H1; the H1 itself does not
    count),
  - slug, for an English keyword (a Hindi keyword in Devanagari is not checked in the slug).
- SureRank's matching: whole words, any case, accents ignored; the keyword's words may also be
  run together ("house keeper" = "housekeeper") or have one other word between them. Nothing
  else counts: "33" is not "thirty-three", "god" is not "gods", and a synonym is not the keyword.
  A Hindi keyword has to appear exactly as written.
- The blog text is never changed to fit a keyword, so choose the focus keyword from wording the
  body already uses. Before settling on one, search both blog texts for it (for example
  `grep -ic "<keyword>" output/<name>/<name>_blog_en.txt`). If the query people search for
  is worded differently from the body (for example "33 crore gods" when the body only says
  "thirty-three crore gods"), use the body's wording as the focus keyword, put the searched
  wording in `secondary_keywords`, and note the mismatch in the report's section 2 so the blog
  can be edited later if wanted.
- Meta descriptions are at most 160 characters; the slug at most 55 characters.
- The blog has at least one `##` subheading in each language (if not, say so in the report).

Rules:
- Do not edit the blog texts, rename images or change any other file; write only the report,
  seo.json and the rebuilt page.
- Do not invent search volumes, rankings or difficulty numbers. Give priority as
  High / Medium / Low and base it on your judgement of intent and competition.
- Titles, meta descriptions, FAQ answers and snippets must be faithful to the talk. Never add
  a scriptural claim that the blog does not support.

Reply with one line: the recommended primary keyword in each language, the number of
authenticity flags, the number of links placed, and the number of unmet checklist items.
