# aytranscription

Turn Acharya Upendra Ji's spiritual discourses (YouTube videos or local audio) into book chapters
and SEO-optimized Antar Yog Foundation blog posts, in Hindi and English, ready to import into
WordPress.

**Read the blogs online: [ameyades1.github.io/aytranscription](https://ameyades1.github.io/aytranscription/)**

## How it works

```
Audio (local MP3 or YouTube URL)
    ↓  YouTube's own transcript, or WhisperX locally     /chapter
Raw transcript → clean transcript
    ↓  Claude writes the chapter and the blog text, then English versions
Chapter + blog texts (Hindi and English)
    ↓  /dequote, /review_blog                            optional quality passes
    ↓  /seo_blog       SEO report + seo.json
    ↓  /seo_blog_fix   SEO-fixed copies of the blog texts
    ↓  /imageplan + image scripts                         hero and inline images
Blog pages (output/<name>/blog/index.html) + gallery (output/index.html)
    ↓  publish_wordpress.sh                               local WordPress import + static export
GitHub Pages (on push to main)
```

Each step runs in Claude Code as a slash command, and each has a batch script that runs it on every
talk. `./publish_blog.sh` chains blog → SEO → fix → check → rebuild in one go.

```
./publish_blog.sh https://www.youtube.com/watch?v=<ID>
./publish_wordpress.sh <name>
```

## Documentation

- [WORKFLOW.md](WORKFLOW.md): every step, script and option in detail
- [CLAUDE.md](CLAUDE.md): conventions for Claude Code working in this repository

## Repository layout

| Path | Purpose |
|------|---------|
| `.claude/skills/` | Slash commands: `chapter`, `dequote`, `review_blog`, `seo_blog`, `seo_blog_fix`, `imageplan` |
| `tools/prompts/` | Writing prompts the skills follow (chapter, blog, translation, Sanskrit review, SEO) |
| `tools/fetch_yt_transcript.py`, `tools/transcribe.sh` | YouTube transcript, or local WhisperX transcription |
| `tools/template/blog_page.py` | One talk's bilingual blog page (`blog.css`, `assets/`) |
| `tools/template/gallery_page.py` | Gallery of all blogs (`output/index.html`), topics from `gallery_topics.txt` |
| `tools/template/seo_gallery_page.py` | English SEO gallery of the exported WordPress posts (`output/seo/`) |
| `tools/template/seo_diff_page.py` | Original vs SEO-fixed blog comparison page (`output/seo-diff/`) |
| `tools/rebuild_blogs.sh` | Rebuild talks' pages, the pages linking to them, and the gallery |
| `tools/check_seo.py`, `tools/verify_seo_fix.py` | Check SEO files and SEO-fixed talks |
| `tools/build_image_plan.py`, `tools/*_image.py` | Image plan and image generation (Gemini, AI Horde, OpenRouter) |
| `tools/make_post_zip.py` | One talk's upload zip for the WordPress Markdown importer |
| `tools/render_chapter.sh` | Optional: chapter `.txt` → styled `.html` + A5 `.pdf` |
| `batch_*.sh` | Run one step on every talk, resumable |
| `publish_blog.sh`, `publish_wordpress.sh` | End-to-end blog pipeline, and WordPress publishing |
| `wordpress-plugin/` | `smd-importer` (Markdown post importer) and `fpj-seo-sync` plugins |
| `ay_existing_blogs_seo/` | Existing FPJ and AY blog archives, duplicate matching and SEO plans |
| `.github/workflows/pages.yml` | Publishes `output/` to GitHub Pages on every push to `main` |
| `output/<name>/` | Everything generated for one talk |
| `project/` | Finished book projects |
| `master.sh` | Legacy Gemini pipeline (see WORKFLOW.md) |
