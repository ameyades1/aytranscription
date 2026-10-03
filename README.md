# aytranscription

Turn spiritual discourses (YouTube videos or local audio) into publication-ready book chapters,
delivered as a web page, an A5 book PDF, plain text, and a ready-to-publish Antar Yog
Foundation blog page.

**Read the chapters online: [ameyades1.github.io/aytranscription](https://ameyades1.github.io/aytranscription/)**

## How it works

```
Audio (local MP3 or YouTube URL)
    ↓  YouTube's own transcript          tools/fetch_yt_transcript.py
    ↓  or, if none: WhisperX locally     tools/transcribe.sh
Raw transcript
    ↓  Claude cleans the transcript      /chapter (Claude Code)
Clean transcript
    ↓  Claude writes the chapter
Chapter text
    ↓  HTML + PDF template               tools/render_chapter.sh
Web page + book PDF
    ↓  Antar Yog blog layout            tools/template/blog_page.py
Blog page (logo, photo, header, footer, video)
```

Run everything with one command inside Claude Code:

```
/chapter tools/my_talk.mp3 my_talk
```

The chapter keeps the talk's original language: a Hindi talk becomes a Hindi chapter, with the
English and Sanskrit the speaker used kept as spoken, and each section built on the speaker's own
words.

## Documentation

- [QUICK_START.md](QUICK_START.md): setup and the one command you need
- [WORKFLOW.md](WORKFLOW.md): every step, script and option in detail

## Repository layout

| Path | Purpose |
|------|---------|
| `.claude/skills/chapter/SKILL.md` | The `/chapter` command: cleaning and chapter-writing instructions |
| `tools/fetch_yt_transcript.py` | Downloads the video's existing YouTube transcript (ID from URL or MP3 file name) |
| `tools/transcribe.sh` | Local WhisperX transcription (audio file or YouTube URL) |
| `tools/render_chapter.sh` | Chapter `.txt` → styled `.html` + `.pdf` |
| `tools/template/` | Page template: `chapter.css` (look) and `md_to_html.py` (converter) |
| `tools/template/blog_page.py` | Blog page: site links, contact details and layout (`blog.css`, `assets/`) |
| `tools/template/gallery_page.py` | Gallery of all blogs (`output/index.html`), with search and topic filters |
| `gallery_topics.txt` | Gallery topics and which talk belongs to which topic |
| `.github/workflows/pages.yml` | Publishes `output/` to GitHub Pages on every push to `main` |
| `tools/whisperx-env/` | Python environment with WhisperX installed |
| `master.sh` | Older pipeline that uses the Gemini API (still works, see WORKFLOW.md) |
| `output/<name>/` | Everything generated for one talk (transcripts, chapters, PDFs, `blog/`) |
| `project/` | Finished book projects |
