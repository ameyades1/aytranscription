# CLAUDE.md

Turns Acharya Upendra Ji's discourses into book chapters and bilingual (Hindi + English)
Antar Yog Foundation blog posts, then SEO-optimizes them and publishes to GitHub Pages and
WordPress. Full pipeline: [WORKFLOW.md](WORKFLOW.md).

## Pipeline

`/chapter` → (`/dequote`, `/review_blog`) → `/seo_blog` → `/seo_blog_fix` → `tools/check_seo.py`
+ `tools/verify_seo_fix.py` → `/imageplan` + images → `tools/rebuild_blogs.sh` →
`./publish_wordpress.sh` → commit and push `output/`.

Skills live in `.claude/skills/<name>/SKILL.md`; the writing rules they follow are in
`tools/prompts/`. Each step has a resumable `batch_*.sh`; `./publish_blog.sh` chains the main ones.

## Files per talk (`output/<name>/`)

- `<name>_blog.txt` / `_blog_en.txt`: original blog texts. `/seo_blog_fix` never edits them.
- `<name>_blog_seo.txt` / `_blog_seo_en.txt`: SEO-fixed copies. Pages and WordPress posts are built
  from these when they exist.
- `blog/seo.json`: source of truth for slug, title, meta description, keywords, category, tags,
  alt text, captions and internal links. Keep it consistent with the SEO-fixed texts.
- `blog/index.html`: generated; never hand-edit. Rebuild with `tools/rebuild_blogs.sh <name>`
  (also rebuilds pages linking to it and the gallery).

## Content rules

- Never attribute to Acharya Ji a teaching, story or quote not in the transcript.
- Blogs have no direct quotes from Acharya Ji (indirect speech instead); scripture verses stay as
  `>` verse blocks with a source line. Gita Press is the authority for scripture.
- Text format: one `#` title, `##` sections only (no `###`), no em dashes (—).
- In English, शिविर is always "Shibir".
- Leave out channel promotions and subscribe requests.

## Environment

- The local WordPress test site is in `~/wordpress`, outside this repo; no WordPress or Docker
  files go in the repo.
- Python environments: `tools/whisperx-env/` (transcription), `tools/image-env/` (images).
- Pushing to `main` with changes under `output/` deploys GitHub Pages.
- Batch logs go to `tools/batch_logs/`.
- Write documents and analyses as local `.md` files.
