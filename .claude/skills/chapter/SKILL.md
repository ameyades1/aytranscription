---
name: chapter
description: Turn a spiritual discourse (local audio file, YouTube URL, or existing raw transcript .txt) into a book chapter (.txt) and a separate Antar Yog Foundation blog page, in Hindi and English, in a folder per talk under output/<name>/. The chapter follows tools/prompts/transcript_to_chapter.txt and the blog follows tools/prompts/transcript_to_blog.txt. Uses the video's YouTube transcript when one exists, otherwise transcribes locally with WhisperX; Claude does the cleaning and writing (no Gemini).
argument-hint: <audio.mp3 | youtube_url | raw_transcript.txt> [name]
model: claude-opus-5-5
effort: low
---

# Discourse → book chapter and blog

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
| `<name>_chapter.txt` / `_chapter_en.txt` | Book chapter (prompt `tools/prompts/transcript_to_chapter.txt`), Hindi and English |
| `<name>_blog.txt` / `_blog_en.txt` | Blog text (prompt `tools/prompts/transcript_to_blog.txt`), Hindi and English |
| `blog/index.html` | Antar Yog Foundation blog page with both languages and a language switch (images in `blog/assets/`; the `blog/` folder is everything needed to publish) |

## Step 1: Get the raw transcript

**Input is a `.txt` transcript:** create `output/<name>/` and copy it to `output/<name>/<name>_raw_transcript.txt` unless it is
already there, and go to step 2.

**Transcripts already there:** if `output/<name>/<name>_raw_transcript.txt` exists, keep it and skip
the rest of step 1; if `<name>_clean.txt` also exists, keep it too and skip step 2. Only fetch or
transcribe again when the user asks for it.

**Input is an audio file or YouTube URL:** prefer YouTube's own transcript over WhisperX.

1. Run `python3 tools/fetch_yt_transcript.py "<input>" "<name>"`. It reads the video ID from the
   URL, or from the end of the file name (`..._<11-char ID>.mp3`), and downloads the channel's
   uploaded captions, or else YouTube's auto-generated captions in the original spoken language
   (never an auto-translated track).
   - Exit 0: the transcript is written. Note the `Source:` line and skip WhisperX.
   - Exit 2 (no video ID, or no transcript on YouTube) or exit 1 (error, e.g. no network or a
     private video): say why in one line and fall back to WhisperX.
2. WhisperX fallback: run `tools/transcribe.sh "<input>" "<name>"` in the background (5-20
   minutes) and wait for it to finish.

If the user asks to use WhisperX (or a local transcription), skip the YouTube fetch.

## Step 2: Clean the transcript

Read the raw transcript and write `output/<name>/<name>_clean.txt`:
- Fix grammar, spelling, punctuation; remove filler words, false starts, stutters.
- YouTube captions have no punctuation and one short phrase per line: join them into sentences.
- Fix speech-recognition errors (YouTube or WhisperX): repeated-word loops, garbled Sanskrit (restore verses to their correct
  Devanagari form, e.g. शर्णम्भ्रज → शरणं व्रज), English words transliterated into Devanagari
  (फॉचर → future) where the speaker clearly spoke English.
- Keep the speaker's language exactly as spoken: Hindi stays Hindi, English phrases stay English,
  Sanskrit stays Sanskrit. Do not translate or summarize.
- Keep proper nouns, deity names and spiritual terms intact.
- Organize into paragraphs by topic. Put channel promotions / subscribe requests after a `***`
  separator so they are kept but clearly marked.

## Step 3: Write the book chapter

Read `tools/prompts/transcript_to_chapter.txt` and follow it, with the cleaned transcript as the
transcript it refers to. Write the result to `output/<name>/<name>_chapter.txt`.

The prompt file decides the content, language, tone and style. This skill adds only:
- **Authenticity:** never attribute to the speaker a teaching, story, example or quote that is
  not in the transcript.
- Leave out channel promotions and subscribe requests.
- **Format** (below). The title line is `# अध्याय: <Title>`.

## Step 3b: Write the blog text

Read `tools/prompts/transcript_to_blog.txt` and follow it, again with the cleaned transcript as
the transcript. Write the result to `output/<name>/<name>_blog.txt`. It is written from the
transcript, not from the book chapter, and the same three additions apply:
- Authenticity and no channel promotions, as in step 3.
- **Format** (below). The title line is `# <Title>`, with no label and no colon in the title.
  Pull quotes are `> "..."` lines. A reflective question for the reader is a paragraph of its
  own in `*italics*`. The closing takeaways are a `- ` bullet list.

## Step 3c: Write the English versions

Translate both into English: `<name>_chapter_en.txt` from the chapter and `<name>_blog_en.txt`
from the blog text. Each is a faithful translation, not a new text:
- Same title, sections, order, quotes, questions and takeaways. Translate quotes faithfully and
  keep them as `> "..."` quotes. Add nothing that is not in the Hindi version.
- Scripture verses keep their Sanskrit as the IAST transliteration in `**bold**`, followed by a
  quoted English meaning and the source line (e.g. `> (Bhagavad Gita 18.66)`).
- Title line `# Chapter: <Title>` for the chapter, `# <Title>` for the blog. Same format rules.

## Format for all four texts

- `# <title line>` once at the top (see each step)
- `## <Section heading>` only: no subheadings (`###`), even where a prompt asks for them
- Speaker quotes: `> "..."` lines
- Scripture verses: a `>` block whose first line is `**bold**`, ending with the reference in
  parentheses as its own line, e.g. `> (श्रीमद्भगवद्गीता १८.६६)`; the explanation follows as normal text
- `- ` for bullet lists; `१. ` / `1. ` for numbered lists
- `**bold**` for key ideas, `*text*` for emphasis
- No em dashes (—), as the prompts require

## Step 4: Blog page

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

Delete any `<name>_chapter*.html` / `.pdf` left from earlier runs (PDFs are no longer made).

Finally rebuild the gallery of all blogs: `python3 tools/template/gallery_page.py`.

## Step 5: Report

List the output files (chapter and blog text in both languages and the blog page), the transcript source (YouTube uploaded captions, YouTube
auto-generated captions, WhisperX, or the user's `.txt`), and anything in the transcript that was unclear
or that you had to interpret.
