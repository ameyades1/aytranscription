---
name: blog
description: Turn a spiritual discourse (local audio file, YouTube URL, or existing raw transcript .txt) into an Antar Yog Foundation blog in Hindi and English (texts and blog page), in a folder per talk under output/<name>/. The blog follows tools/prompts/transcript_to_blog.txt and the English version tools/prompts/hindi_to_english.txt. Uses the video's YouTube transcript when one exists, otherwise transcribes locally with WhisperX. No book chapter (that is /chapter).
argument-hint: <audio.mp3 | youtube_url | raw_transcript.txt> [name]
model: claude-opus-5-5
effort: low
---

# Discourse → blog

This command runs on Claude Opus 5.5 at low effort (set in the `model` and `effort` fields
above), whichever model and effort the session uses. Change those two fields to change it.

Arguments: `$ARGUMENTS`. The first is the input; the optional second is the output name.
If no name is given, use the input's file name without extension and without a trailing
`_raw_transcript` (for a YouTube URL, ask the user for a short snake_case name).

All paths are relative to the repo root. Each talk gets its own folder, `output/<name>/`, and
every file for that talk goes in it:

| File | Content |
|------|---------|
| `<name>_raw_transcript.txt` | YouTube transcript or WhisperX output, untouched |
| `<name>_clean.txt` | Cleaned transcript |
| `<name>_blog.txt` / `_blog_en.txt` | Blog text (prompt `tools/prompts/transcript_to_blog.txt`), Hindi; English via `tools/prompts/hindi_to_english.txt` |
| `blog/index.html` | Antar Yog Foundation blog page with both languages and a language switch (images in `blog/assets/`; the `blog/` folder is everything needed to publish) |

This skill writes no book chapter; `/chapter` does that, from the same transcripts.

## Step 1: Get the raw transcript

Read `tools/prompts/get_transcript.md` and follow it.

## Step 2: Clean the transcript

Unless `output/<name>/<name>_clean.txt` already exists (step 1 says when to keep it), read
`tools/prompts/clean_transcript.txt` and follow it with the raw transcript, and write the result
to `output/<name>/<name>_clean.txt`.

## Step 3: Write the Hindi blog

Read `tools/prompts/transcript_to_blog.txt` and follow it, with the cleaned transcript as the
transcript it refers to. Write the result to `output/<name>/<name>_blog.txt`. The prompt decides
content, tone and style; the format below decides the layout.

## Step 4: Write the English blog

Read `tools/prompts/hindi_to_english.txt` and follow it to translate the Hindi blog into
`output/<name>/<name>_blog_en.txt`. Same title, sections, order, questions and takeaways; add
nothing that is not in the Hindi. Where the prompt and this skill differ, this skill's format wins.

## Format for both texts

- `# <Title>` once at the top, with no label and no colon in the title
- `## <Section heading>` only: no subheadings (`###`)
- No direct quotes from Acharya Ji: his words are ordinary text in indirect speech
- Scripture verses: a `>` block whose first line is `**bold**` (Devanagari in Hindi, IAST in
  English; the English block also has the quoted meaning), ending with the reference in
  parentheses as its own line, e.g. `> (श्रीमद्भगवद्गीता १८.६६)` / `> (Bhagavad Gita 18.66)`
- A reflective question for the reader is a paragraph of its own in `*italics*`
- The closing takeaways are a `- ` bullet list; `१. ` / `1. ` for numbered lists
- `**bold**` for key ideas, `*text*` for emphasis
- No em dashes (—)

## Step 5: Blog page

Find the video ID of the original discourse from the input (URL or `..._<ID>.mp3` file name):

```bash
python3 -c "import sys; sys.path.insert(0, 'tools'); from fetch_yt_transcript import video_id; print(video_id(sys.argv[1]) or '')" "<input>"
```

Then build the page from the two blog texts, Hindi first as the default (it is written to
`output/<name>/blog/index.html`; leave out `--video` if there is no ID, and the page then has no
video card):

```bash
python3 tools/template/blog_page.py output/<name>/<name>_blog.txt output/<name>/<name>_blog_en.txt \
  --video=<ID>
```

Each language gets the full page: hero, table of contents, author card, video card and call to action. A switch in the header and a
button in the hero change the language in place; `#en` / `#hi` in the URL opens one directly.

Check it: screenshot the page with headless Chrome at desktop (1366px wide) and phone (400px)
widths into the scratchpad, once plain and once with `#en` appended to the file URL, and look
at them. Confirm both languages show the title, photo, video card and footer, and
the Devanagari text is intact.

Finally rebuild the gallery of all blogs: `python3 tools/template/gallery_page.py`.

## Step 6: Report

List the output files (blog text in both languages and the blog page), the transcript source, and
anything in the transcript that was unclear or that you had to interpret.
