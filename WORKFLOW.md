# Discourse to Blog Workflow

This workflow turns a spiritual discourse (YouTube video or local audio) into a book chapter and
an SEO-optimized bilingual blog post, published as a static page on GitHub Pages and imported
into WordPress.

## Overview

| Step | Command | Writes (under `output/<name>/`) |
|------|---------|--------------------------------|
| 1. Transcript, chapter, blog | `/chapter` | `_raw_transcript.txt`, `_clean.txt`, `_chapter.txt`, `_chapter_en.txt`, `_blog.txt`, `_blog_en.txt`, `blog/index.html` |
| 2. Remove direct quotes (optional) | `/dequote` | edits `_blog.txt`, `_blog_en.txt` |
| 3. Sanskrit / scripture review (optional) | `/review_blog` | `tools/review/<name>.md` |
| 4. SEO report | `/seo_blog` | `blog/seo_report.md`, `blog/seo.json` |
| 5. SEO fix | `/seo_blog_fix` | `_blog_seo.txt`, `_blog_seo_en.txt`, `blog/seo_fix.md`, updates `seo.json` |
| 6. Check | `tools/check_seo.py`, `tools/verify_seo_fix.py` | — |
| 7. Image prompts | `/imageplan` | `blog/image_plan.txt` |
| 8. Images | `batch_images.sh` / `tools/*_image.py` | `blog/assets/hero.jpg`, `inline.jpg` |
| 9. Rebuild pages | `tools/rebuild_blogs.sh` | `blog/index.html`, `output/index.html` |
| 10. WordPress | `publish_wordpress.sh` | local WordPress posts, `output/wp/`, `output/seo/` |
| 11. Publish | commit and push `output/` | GitHub Pages |

Steps 1, 4, 5, 6 and 9 run together with `./publish_blog.sh`.

## Output structure

```
output/
├── index.html                          # gallery of all blogs (gallery_page.py)
├── seo/index.html                      # English SEO gallery of exported WordPress posts
├── seo-diff/index.html                 # original vs SEO-fixed comparison
├── wp/<slug>/                          # Simply Static export of the local WordPress
└── <name>/                             # one folder per talk
    ├── <name>_raw_transcript.txt       # YouTube transcript or WhisperX output, unedited
    ├── <name>_clean.txt                # cleaned transcript
    ├── <name>_chapter.txt / _en.txt    # book chapter, Hindi and English
    ├── <name>_blog.txt / _en.txt       # blog text, Hindi and English
    ├── <name>_blog_seo.txt / _seo_en.txt  # SEO-fixed copies (pages are built from these)
    └── blog/
        ├── index.html                  # bilingual blog page
        ├── seo_report.md, seo.json     # /seo_blog
        ├── seo_fix.md                  # /seo_blog_fix change log
        ├── image_plan.txt, images.txt  # image prompts and inline image placement
        └── assets/                     # logo, photo, video thumbnail, hero.jpg, inline.jpg
```

## Step details

### 1. `/chapter`

```
/chapter <audio.mp3 | youtube_url | raw_transcript.txt> [name]
```

Instructions are in `.claude/skills/chapter/SKILL.md`.

- **Transcript:** tries YouTube's own captions first (`tools/fetch_yt_transcript.py`), otherwise
  transcribes locally with WhisperX (`tools/transcribe.sh`). Say "use WhisperX" to force it.
- **Clean:** fixes transcription errors, keeps the speaker's language exactly, marks channel
  promotions off after `***`.
- **Chapter:** follows `tools/prompts/transcript_to_chapter.txt`; title line `# अध्याय: <Title>`.
- **Blog:** follows `tools/prompts/transcript_to_blog.txt`, written from the transcript, not the
  chapter. No direct quotes from Acharya Ji; scripture verses stay as verse blocks.
- **English:** both translated with `tools/prompts/hindi_to_english.txt`.
- **Page:** `tools/template/blog_page.py` builds `blog/index.html` from the two blog texts, with the
  YouTube video card when the input has a video ID.

Nothing is attributed to the speaker that is not in the transcript.

#### YouTube transcript: `tools/fetch_yt_transcript.py`

```bash
python3 tools/fetch_yt_transcript.py <youtube_url | audio_file | video_id> <name>
```

- **Video ID:** from the URL, or the end of a local file name, `<anything>_<11-character ID>.mp3`.
- **Track:** channel-uploaded captions first, then YouTube's auto captions in the spoken language
  (`hi-orig`). Never auto-translated tracks.
- Exit code `2` when there is no ID or no transcript, `1` on errors.

#### Local transcription: `tools/transcribe.sh`

```bash
tools/transcribe.sh <audio_file|youtube_url> <name>
```

Downloads audio with yt-dlp (or uses the local file) and runs WhisperX (`medium`, CPU, `int8`) from
`tools/whisperx-env/`. Change the model with `--model` in the script.

### 2. `/dequote <name>`

Rewrites Acharya Ji's direct quotes in the blog texts as ordinary text, keeping scripture verses.
Chapters are not touched. Batch: `./batch_dequote.sh`.

### 3. `/review_blog <name>`

Reviews the blog's Sanskrit and scripture references (Gita Press as the authority) following
`tools/prompts/sanskrit_review.txt`, and writes `tools/review/<name>.md`. Does not edit the blog.
Batch: `./batch_review.sh`.

### 4. `/seo_blog <name>`

Writes `blog/seo_report.md` and `blog/seo.json` following `tools/prompts/seo_blog_specialist.txt`.
`seo.json` feeds the page generator and WordPress: title tag, slug, focus keyword, meta
description, category (one of the 14 approved), tags, image alt text and captions, internal
links, "Also read" and "Further reading". See `tools/seo/SEO_REPORT_GUIDE.md`. The blog text is
not edited. Batch: `./batch_seo.sh` (talks run in order so each can reuse earlier tags).

### 5. `/seo_blog_fix <name>`

Writes SEO-fixed copies `<name>_blog_seo.txt` and `_blog_seo_en.txt` with the smallest faithful
edits for the report's unmet checklist items, logs them in `blog/seo_fix.md`, updates `seo.json`
to match, and rebuilds the page. The original blog texts are kept. Batch: `./batch_seo_fix.sh`
(commits and pushes each talk once `verify_seo_fix.py --strict` passes).

### 6. Checks

```bash
python3 tools/check_seo.py [<talk> ...]                # SEO files are complete and consistent
python3 tools/verify_seo_fix.py [--strict] [<talk> ...] # no stale files before WordPress
```

### 7–8. Images

```bash
/imageplan <name> [<name> ...]           # writes blog/image_plan.txt (hero 16:9 + one inline)
./batch_imageplan.sh                     # for every blog without one, then build_image_plan.py
python3 tools/build_image_plan.py        # rebuilds tools/image_plan.md and each blog/images.txt
./batch_images.sh                        # AI Horde images for every blog without hero.jpg
```

Image generators, all reading `tools/image_plan.md`:

- `tools/horde_image.py`: AI Horde (free); key from `HORDE_API_KEY` or `tools/.horde_key`.
- `tools/generate_image.py`: Gemini (`gemini-3.1-flash-image`); needs `GEMINI_API_KEY`. Run with
  `tools/image-env/bin/python`.
- `tools/openrouter_image.py`: OpenRouter.

### 9. Rebuild pages: `tools/rebuild_blogs.sh`

```bash
tools/rebuild_blogs.sh <talk> [<talk> ...]   # these talks, pages linking to them, the gallery
tools/rebuild_blogs.sh --all
```

Pages are built from the SEO-fixed texts when they exist. The gallery's topics are in
`gallery_topics.txt`. Other generated pages:

- `python3 tools/template/gallery_page.py` → `output/index.html`
- `python3 tools/template/seo_gallery_page.py` → `output/seo/index.html`
- `python3 tools/template/seo_diff_page.py` → `output/seo-diff/index.html`

Site links, contact details and the founder description are in `SITE` and `TEXT` at the top of
`blog_page.py`; the design is `tools/template/blog.css`.

### 10. WordPress: `./publish_wordpress.sh [talk ...]`

Uses the local WordPress in `~/wordpress` (outside this repo):

1. Imports each talk that passes the checks with `~/wordpress/import_post.py` (from the SEO-fixed
   texts).
2. Re-imports posts that link to a talk whose slug changed.
3. Exports the site with Simply Static to `output/wp/` and rebuilds the SEO gallery and main gallery.
   `STATIC=0` skips this.

Nothing is committed and nothing goes to the live site.

For the live site, `tools/make_post_zip.py <talk> [dir] [--lang en|hi]` builds an upload zip
(`<slug>.md` + images) for the **smd-importer** plugin in `wordpress-plugin/smd-importer/`
(SEO-plugin neutral: SureRank, Yoast, Rank Math, AIOSEO). Build the plugin zip with
`wordpress-plugin/build_zip.sh`. `wordpress-plugin/fpj-seo-sync/` syncs SEO data onto existing
posts, using `ay_existing_blogs_seo/fpj_to_ay.json`.

### 11. Publish

Commit and push `output/`; `.github/workflows/pages.yml` deploys it to GitHub Pages.

## End-to-end: `./publish_blog.sh`

```bash
./publish_blog.sh [talk_name | youtube_url ...]   # default: every talk with a blog page
```

Runs `/chapter` (URL input only), `/seo_blog`, `/seo_blog_fix` and `check_seo.py` per talk, then
`rebuild_blogs.sh` once. Steps already done are skipped. Settings: `MODEL`, `EFFORT`,
`PERMISSION_MODE`, `LIMIT_WAIT`, `MAX_FAILURES`, `PAUSE`.

## Batch scripts

Each runs one fresh `claude -p` session per talk, skips finished talks (safe to stop and re-run),
waits and retries on usage limits, and logs to `tools/batch_logs/`.

| Script | Runs |
|--------|------|
| `batch_chapters.sh` | `/chapter` on every mp3 in `batch_chapters.txt` |
| `batch_translate_en.sh` | Retranslates every `_blog_en.txt` from the Hindi blog |
| `batch_dequote.sh` | `/dequote` on talks with quotes left |
| `batch_review.sh` | `/review_blog` on talks without a review |
| `batch_seo.sh` | `/seo_blog` on talks failing `check_seo.py` |
| `batch_seo_fix.sh` | `/seo_blog_fix` on talks not yet verified |
| `batch_imageplan.sh` | `/imageplan` in groups |
| `batch_images.sh` | Image generation (no Claude) |

## Optional: chapter HTML / PDF

```bash
tools/render_chapter.sh output/<name>/<name>_chapter.txt
```

Writes a styled `.html` and an A5 `.pdf` (headless Chrome, Noto Serif fonts from Google Fonts)
next to the chapter. `/chapter` no longer does this. Look: `tools/template/chapter.css`;
converter: `tools/template/md_to_html.py`.

### Text format (chapters and blogs)

| Write | Renders as |
|-------|-----------|
| `# Title` (`# अध्याय: Title` for chapters) | Title |
| `## Heading` | Section heading (no `###`) |
| `> "quote"` | Quote box |
| `> **verse line**` ... `> (source)` | Scripture verse panel |
| `- item` / `1. item` | Bullet / numbered list |
| `**bold**` / `*text*` | Bold / emphasis |

## Requirements

- Claude Code (all slash commands and batch scripts)
- WhisperX in `tools/whisperx-env/` (`bash tools/setup_whisperx.sh`), `ffmpeg`
- `yt-dlp` (keep it updated: `pip install --upgrade yt-dlp`)
- `tools/image-env/` for image generation
- Local WordPress in `~/wordpress` for `publish_wordpress.sh`
- Google Chrome for screenshots and the optional PDFs

## Troubleshooting

- **Slash command not found:** restart Claude Code from the repository folder.
- **WhisperX not found:** run `bash tools/setup_whisperx.sh`; do not call
  `tools/whisperx-env/bin/whisperx` directly (the scripts use `python3 -m whisperx`).
- **YouTube download fails:** check the URL is public, then upgrade yt-dlp.
- **Batch script stuck on a talk:** see its log in `tools/batch_logs/`; after `MAX_FAILURES` the
  talk is skipped.

## Legacy: `master.sh` (Gemini API)

The original pipeline: WhisperX plus `tools/process_with_gemini.py` with
`tools/prompts/clean_transcript.txt` and `generate_chapter.txt`. Writes flat files into
`output/`, needs `GEMINI_API_KEY`, and can add material the speaker never said. Kept for
reference; use `/chapter` instead.
