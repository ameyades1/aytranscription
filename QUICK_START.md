# Quick Start Guide

## One Command

Inside Claude Code, in this repository:

```
/chapter <audio.mp3 | youtube_url | raw_transcript.txt> [name]
```

Examples:

```
/chapter tools/power_of_surrendering_to_guru_xXkJCnkCJh4.mp3 surrendering_to_guru
/chapter https://www.youtube.com/watch?v=xXkJCnkCJh4 surrendering_to_guru
/chapter output/surrendering_to_guru/surrendering_to_guru_raw_transcript.txt
```

Claude will:
1. ✅ Get the transcript: YouTube's own transcript if the video has one, otherwise a local
   WhisperX transcription (skipped if you give a `.txt` transcript)
2. ✅ Clean the transcript
3. ✅ Write the book chapter, in the talk's original language, plus a faithful translation in the
   other language (English for a Hindi talk, Hindi for an English talk)
4. ✅ Render each as a web page and an A5 book PDF, and check the PDF displays correctly
5. ✅ Build an Antar Yog Foundation blog page with the logo, Acharya Ji's photo, site header,
   footer with links and contact details, a card for the original YouTube video, and both
   languages on the same page with a हिन्दी / English switch

No Gemini API key is needed.

## Output Files

Each talk gets its own folder, `output/<name>/`, with everything for that talk:

| File | Description |
|------|-------------|
| `<name>_raw_transcript.txt` | YouTube transcript or WhisperX transcription, unedited |
| `<name>_clean.txt` | Cleaned transcript, same language as spoken |
| `<name>_chapter.txt` | Chapter in the talk's language |
| `<name>_chapter_en.txt` / `_hi.txt` | Same chapter in the other language |
| `<name>_chapter*.html` | Styled web page for each language (works on desktop and phone) |
| `<name>_chapter*.pdf` | A5 book PDF for each language |
| `blog/index.html` | Blog page with both languages; open `#en` or `#hi` to link a language directly (images in `blog/assets/`) |

Example: `output/surrendering_to_guru/surrendering_to_guru_chapter.pdf`, `output/surrendering_to_guru/blog/index.html`.

## Prerequisites (One-Time Setup)

- **WhisperX** is already installed in `tools/whisperx-env/`. To reinstall: `bash tools/setup_whisperx.sh`
- **ffmpeg** for audio processing: `sudo apt install ffmpeg` (Ubuntu) or `brew install ffmpeg` (Mac)
- **yt-dlp**, for YouTube transcripts, downloads and video details: `pip install yt-dlp`
- **Google Chrome**, used to make the PDF (it renders Hindi text correctly)
- **Internet connection** when rendering, to load the Noto Serif fonts

## Running Steps Individually

For local MP3s, the YouTube video ID must be at the end of the file name
(`my_talk_xXkJCnkCJh4.mp3`) so the YouTube transcript can be found.

```bash
# Get YouTube's transcript only
python3 tools/fetch_yt_transcript.py tools/my_talk_xXkJCnkCJh4.mp3 my_talk

# Transcribe locally with WhisperX only
tools/transcribe.sh tools/my_talk.mp3 my_talk

# Re-render a chapter after editing its .txt
tools/render_chapter.sh output/my_talk/my_talk_chapter.txt

# Rebuild the blog page
python3 tools/template/blog_page.py output/my_talk/my_talk_chapter.txt output/my_talk/my_talk_chapter_en.txt \
  --video xXkJCnkCJh4
```

## Tips

- **Force local transcription:** say so when running `/chapter`, e.g. "use WhisperX".
- **Edit and re-render:** change `output/<name>/<name>_chapter.txt` by hand, then run `tools/render_chapter.sh` on it.
- **Change the look:** colors are defined at the top of `tools/template/chapter.css`.
- **Change how chapters are written:** edit `.claude/skills/chapter/SKILL.md`.
- **New command not showing up?** Restart Claude Code.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `/chapter` not found | Restart Claude Code in this repository |
| "WhisperX site-packages not found" | Run `bash tools/setup_whisperx.sh` |
| YouTube download fails | Check the URL, then `pip install --upgrade yt-dlp` |
| PDF shows plain/default font | Check your internet connection and re-run `tools/render_chapter.sh` |

## Older Gemini-based pipeline

`master.sh` still works and uses the Gemini API for cleaning and chapter writing. See
[WORKFLOW.md](WORKFLOW.md#legacy-mastersh-gemini-api).
