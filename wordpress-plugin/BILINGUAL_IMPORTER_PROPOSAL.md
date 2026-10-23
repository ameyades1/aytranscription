# Proposal: bilingual Markdown Blog Importer (3.0.0)

Status: built as smd-importer 3.0.0 on 2026-10-23 and tested on the local WordPress (see
`smd-importer/README.txt`). Differences from this proposal: `make_post_zip.py` writes each language's
own slugs in links (the plugin adds the `/hi/` prefix); the plugin also has a `wp smd import` command,
which `publish_wordpress.sh` now uses instead of `~/wordpress/import_post.py`; tests 7 (no Polylang)
and 8 (Yoast, Rank Math, AIOSEO) are not run yet.

## Goal

One upload imports a talk's English **and** Hindi posts, and links them as translations of
each other, so the हिन्दी / English switch in each post moves between them and search engines
get `hreflang` tags. Today (2.1.0) each language is a separate upload, and nothing links the two
posts.

The design matches what we built and tested on the local WordPress (Polylang 3.9.1, English
default at `/<slug>/`, Hindi at `/hi/<slug>/`, switch under the byline).

## What stays the same

- Markdown format, blocks, images, YouTube, Also read, boxes, SEO-plugin support (SureRank, Yoast,
  Rank Math, AIOSEO).
- Posts are created as **Pending Review**, never published.
- Only pending or draft posts are updated, and only with "update" ticked.
- A single `.md` without a language still imports exactly as today (backward compatible).
- **Out of scope: the plugin never touches menus, themes or Polylang's settings.** Menus are
  site setup. Note for whoever installs Polylang: a language with no menu assigned shows no menu,
  so once, in Appearance > Menus > Manage Locations, give the Hindi locations the existing menu.

## Design

### 1. Upload: one zip per talk, both languages

```
<talk>.zip
├── en.md            # English post
├── hi.md            # Hindi post
└── assets/
    ├── hero.jpg
    └── inline.jpg   # shared; each post gets its own Media Library copy with its own alt text
```

A zip may hold one or two `.md` files (2.1.0 requires exactly one). Each `.md` names its language.

**One language at a time** works too: upload a zip (or a plain `.md`) with only `en.md` or only
`hi.md`. That post is created with its language and `translation_key`, and has no switch until
its partner arrives. When the other language is uploaded later, in either order, the importer
finds the first post by `translation_key` and links them, even if the first is already published.

### 2. New front matter

| Field | Example | Purpose |
|-------|---------|---------|
| `lang` | `en` / `hi` | The post's language. Missing → the site's default language |
| `translation_key` | `two_causes_create_your_life` | Stable ID shared by both posts of a talk. Pairs them across separate uploads too (e.g. Hindi uploaded a week after English) |
| `category_key` | `karma` | Links "Karma & Destiny" and "कर्म और भाग्य" as translations of one category |

Everything else (title, slug, tags, SEO fields, images) stays per file, as now.

### 3. Import steps

1. **Check everything first:** both documents, slugs, image references, update permissions. If
   anything fails, nothing is created. Today a failure can stop halfway; with two posts that
   would leave one language behind.
2. **Create or update each post** with the current code path, once per language.
3. **Set the language and pair the posts** through a small *language adapter*:
   - **Polylang active:** `pll_set_post_language`, `pll_save_post_translations`; categories and
     tags get the post's language (`pll_set_term_language`), and categories with the same
     `category_key` are linked (`pll_save_term_translations`).
   - **No multilingual plugin:** store `smd_lang` and `smd_translation_key` as post meta only, and
     the import page says pairing needs Polylang. (A WPML adapter could be added later the same way.)
4. **Find an existing partner:** a post with the same `translation_key` in the other language is
   linked even if it is already **published**. Linking doesn't change its content, so this is
   allowed without "update".
5. **Language-correct links:** site-relative links (`/slug/`) and Also read links are resolved to
   the target post's real permalink in **this post's language**, so Hindi posts link to
   `/hi/<slug>/`. If the target isn't on the site yet, the link is kept as written and listed in
   the result message.

### 3a. Linking by hand

- **In the post editor (Polylang, no plugin code):** the post's Languages panel has a
  Translations field per language; search for the other post by title and save to link them.
  Works for any post, including older ones without a `translation_key`.
- **On the import page:** an optional **Translation of** field (search existing posts by title)
  links the uploaded post to the chosen one. It wins over a `translation_key` match. Available only
  when one language is uploaded; the chosen post must be in the other language and not already
  linked to a different post.

### 4. Language switch (built in, optional)

The in-post हिन्दी / English toggle (now in `~/wordpress/ay-lang-switch.php`) moves into the plugin:

- Settings: position *below the byline* (default) / *top of content* / *off*; labels per language.
- Shown only on posts that have a translation; also available as `[smd_lang_switch]`.
- Works with Polylang. Without it, the plugin can still draw the switch and print `hreflang`
  links from `smd_translation_key` (basic mode, posts only).

### 5. Import page

- Same single upload field; accepts the bilingual zip.
- After upload, the result lists each language: title, slug, **created / updated / skipped**,
  and **linked to** (the partner post's title and edit link).
- The notice at the top also names the multilingual plugin found (Polylang / none), like
  it already does for SEO plugins.

### 6. `tools/make_post_zip.py`

- Default `--lang both`: writes `<en-slug>.zip` with `en.md`, `hi.md` and `assets/`.
- Adds `lang`, `translation_key` (the talk's folder name) and `category_key` (seo.json's category)
  to the front matter.
- Writes internal links as `/slug/` of the **English** slug in both files, and the plugin
  translates them (step 3.5). `--lang en|hi` still builds one language.

## Edge cases

| Case | Behaviour |
|------|-----------|
| English published, Hindi new | Hindi created as pending, linked to the published English post |
| Both already exist, update not ticked | Rejected, as today; pairing is still repaired if missing |
| Same slug in both languages | Rejected before import (Polylang free doesn't allow shared slugs) |
| Partner exists with another language already linked | Rejected with a message; never silently re-paired |
| Polylang switched off later | Posts keep their meta; re-activating Polylang and re-uploading re-pairs them |

## SEO plugins

The live site uses **SureRank**, but all four supported plugins (SureRank, Yoast SEO, Rank Math,
All in One SEO) keep working. Each post's SEO fields are written per post exactly as in 2.1.0, so
each language gets its own title, description and focus keyword. Language handling stays with
Polylang (`hreflang`, `<html lang>`), not the SEO plugin. Checked locally: SureRank with Polylang
gives correct canonicals and `hreflang`. Yoast and AIOSEO support Polylang directly; Rank Math
needs the compatibility snippet from its own docs (rankmath.com/kb/polylang-compatibility), which
is site setup, not plugin code.

## Testing

On the local WordPress (`~/wordpress`, Polylang installed):

1. Bilingual zip, new talk → two pending posts, linked, both switches work, `hreflang` correct.
2. English only, then Hindi only (two uploads) → paired by `translation_key`.
3. Re-upload with update → same two posts updated, images reused, pairing kept.
4. English already published → Hindi created and linked; English untouched.
5. Old single-file `.md` without `lang` → behaves exactly like 2.1.0.
6. A broken `hi.md` → nothing created for either language.
7. Without Polylang → posts import, meta saved, warning shown.
8. Repeat test 1 with each SEO plugin active (SureRank, Yoast SEO, Rank Math, AIOSEO) → each
   language's SEO panel shows its own title, description and focus keyword.

Then run `./publish_wordpress.sh` and the Simply Static export to confirm `/hi/` pages export.

## Work estimate

About a day: plugin roughly +250 lines (adapter, pairing, validation pass, link resolution,
switch and settings), `make_post_zip.py` about +40 lines, README update, the tests above.

## Questions before building

1. **Live Hindi URLs:** are there Hindi posts on the live site already? If so, Polylang's `/hi/`
   prefix changes their URLs. We'd either keep them (Polylang setting: language from content,
   no prefix) or add redirects.
2. **Local importer:** should `~/wordpress/import_post.py` be retired, with local imports going
   through the plugin too, so local and live use the same code?
