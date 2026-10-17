---
name: seo_blog
description: Write an SEO report for one talk's blog (output/<name>/<name>_blog.txt and _blog_en.txt) as a Senior SEO Blog Specialist for Indian spirituality, following tools/prompts/seo_blog_specialist.txt, and save it to tools/seo/<name>.md, plus output/<name>/blog/seo.json for the page generator (title tag, image alt text, internal links, Also read and Further reading). The blog text is not edited.
argument-hint: <talk name>
model: claude-opus-5-5
effort: medium
---

# SEO report for a blog

This command runs on Claude Opus 5.5 at medium effort (the `model` and `effort` fields above).

Talk: `$ARGUMENTS`.

1. Read `tools/prompts/seo_blog_specialist.txt` and follow it exactly.
2. Read the Hindi blog `output/<name>/<name>_blog.txt`, then the English blog
   `output/<name>/<name>_blog_en.txt`. If `output/<name>/blog/image_plan.txt` or
   `tools/review/<name>.md` exist, read them too: use the image plan for file names and alt
   text, and carry any Sanskrit review issues into the authenticity flags.
3. For internal links, list the other talks with `ls output/` and link only to blogs that
   exist there. Never invent a post.
4. Write the report to `tools/seo/<name>.md` in the prompt's 10-section output format.
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
   - `links`: the in-text links (section 7). Each phrase must be copied exactly from a paragraph
     or list item of that language's blog text (not a heading or verse), and should appear
     there before any other occurrence you don't want linked. 3 to 5 links per language.
   - `also_read`: one talk, placed after the `##` heading (copied exactly, per language) of the
     section it extends best.
   - `related`: the 3 talks that suit a reader of this blog best.
   Use only talks whose `output/<talk>/blog/index.html` exists. Add nothing else to seo.json:
   meta descriptions, the FAQ and the schema stay in the report only.
6. If `output/<name>/blog/index.html` exists, rebuild it with the same command as the
   /chapter skill (`python3 tools/template/blog_page.py output/<name>/<name>_blog.txt
   output/<name>/<name>_blog_en.txt --video=<ID>`, the ID taken from the existing page's
   YouTube link; no --video if it has none). Any "Note:" line means a phrase, heading or talk
   was not found: fix seo.json and rebuild until there are none.

Rules:
- Do not edit the blog texts, rename images or change any other file; write only the report,
  seo.json and the rebuilt page.
- Do not invent search volumes, rankings or difficulty numbers. Give priority as
  High / Medium / Low and base it on your judgement of intent and competition.
- Titles, meta descriptions, FAQ answers and snippets must be faithful to the talk. Never add
  a scriptural claim that the blog does not support.

Reply with one line: the recommended primary keyword in each language, the number of
authenticity flags, and the number of links placed.
