MARKDOWN BLOG IMPORTER — VERSION 3.0.0

WHAT IT DOES
- Adds Tools > Markdown Blog Importer in WordPress admin.
- Accepts one .md/.markdown file (maximum 2 MB), or one .zip (maximum 50 MB) holding the .md and its images. A zip may hold two .md files, one per language, to import an English and a Hindi post together and link them as translations (see LANGUAGES).
- Converts Markdown into standard WordPress blocks (see BLOCKS below), so the post looks right in any theme and opens in the block editor as ordinary, editable blocks. The plugin adds no CSS of its own.
- Creates the WordPress post as PENDING REVIEW (never publishes automatically). An editor reviews it and publishes it.
- Supports title, slug, excerpt, categories, tags, SEO title, meta description, canonical URL and robots directive in front matter.
- Creates missing categories and tags.
- Prevents duplicate slugs by default; optional update is limited to existing pending or draft posts, and keeps the post's author.
- Imports images uploaded with the Markdown file: the hero becomes the post's featured image (shown by the theme, usually at the top of the post) and each inline image is placed where the Markdown puts it, with its alt text and caption.
- Optionally assigns a featured image using an existing WordPress media attachment ID instead.

SEO PLUGINS
The front matter's seo_title, meta_description, focus_keyword, canonical_url and robots are written into the post's own settings of every active supported SEO plugin, so its panel shows them and no template setup is needed:
- SureRank: surerank_settings_general (page_title, page_description, focus_keyword, canonical_url) and the surerank_settings_post_no_index / _no_follow flags
- Yoast SEO: _yoast_wpseo_title, _metadesc, _focuskw, _canonical, _meta-robots-noindex and _meta-robots-nofollow
- Rank Math: rank_math_title, _description, _focus_keyword, _canonical_url and rank_math_robots
- All in One SEO: its own aioseo_posts table, through its Post::savePost() method (title, description, focus keyword, canonical URL, noindex, nofollow)
The import page says which of them it found. With none active, the values are kept only in the importer's own fields (smd_seo_title, smd_seo_description, smd_canonical_url, smd_robots), which it always writes; re-import once an SEO plugin is active to pass them on. An empty field clears that plugin's per-post value, so it falls back to its default. Schema is not written. Tested with SureRank 1.10.2, Yoast SEO 28.7, Rank Math 1.0.280 and All in One SEO; check the SEO panel on a draft after updating any of them.

SureRank checks a post's SEO when it is first saved, before the importer has written these values, so its panel may show warnings (such as a long default title or no focus keyword) until the post is saved again, for example when it is reviewed and published.

SURERANK IMAGE TITLES (one-time setup, only if you use SureRank)
SureRank's "auto set image title" setting is on by default. It replaces the title of every image added to the Media Library with one it makes itself (in lowercase), overwriting the alt-text titles this importer gives its images. The file names and the alt text in the post are not affected. SureRank 1.10.2 has no switch for it in its settings screens, so turn it off with WP-CLI:

  wp eval '$s = get_option("surerank_settings", []); $s["auto_set_image_title"] = false; update_option("surerank_settings", $s);'

Check it with:

  wp eval 'var_dump(SureRank\Inc\Functions\Settings::get("auto_set_image_title"));'

which should print bool(false). Without WP-CLI, run the same PHP once from a code-snippets plugin. A SureRank update may add a switch for this or reset it, so check again after updating.

A related setting, SureRank > Advanced > Image SEO > "Optimize Image SEO without AI" (auto_set_image_alt), fills in missing alt text from the image's file name, such as "Hero 2 300x169". Turn it off too if you want only the alt text you wrote.

LANGUAGES (new in 3.0.0)
- Each .md can name its language and its talk in the front matter:
    lang: hi                        # a language set up in Polylang (en, hi, ...)
    translation_key: two_causes     # the same in every language version of one post
    category_key: karma             # links the post's category with its translations
- Two .md files in one zip (for example en.md and hi.md, sharing the images in assets/) are imported
  together and linked as translations. Each language must appear once, with its own slug.
- One language at a time also works, in either order: the post is linked to the posts already here
  with the same translation_key, even if those are published (linking does not change them).
- "Translation of" on the import page links an upload of one language to a post you pick instead,
  for older posts without a translation_key. Posts can also be linked later in the post editor's
  Languages panel (Polylang).
- Before anything is saved, every file is checked (front matter, slugs, images, languages). If one
  fails, nothing is created. An upload that would give a language a second, different post is
  refused instead of silently re-linking.
- With Polylang, each post gets its language, and its categories and tags are found or created in that
  language ("Karma & Destiny" for English, "कर्म और भाग्य" for Hindi). Categories with the same
  category_key are linked as translations. Without a lang: field, a post gets Polylang's default language.
- Site-relative links to other posts ([text](/slug/)) and Also read links are pointed at the post in the
  importing post's language: its translation when it has one (so a Hindi post links to /hi/<slug>/),
  else the post itself. A slug not on the site yet keeps its slug under the language's URL, and the
  result message lists it; import that post and re-import this one to update the link.
- Without Polylang, posts are still imported and their language (smd_lang) and translation_key
  (smd_translation_key) are saved, so the language switch and hreflang links work for posts; menus,
  language URLs and per-language categories need Polylang.
- The plugin never changes menus, the theme or Polylang's settings. A language with no menu assigned
  shows no menu: in Appearance > Menus > Manage Locations, give its locations a menu once.

LANGUAGE SWITCH
- A post with a published translation shows a switch with its languages (for example English | हिन्दी),
  the current one highlighted. The setting is at the bottom of Tools > Markdown Blog Importer:
  below the byline (in Astra; other themes put it at the top of the post), top of the post, or off.
- Also available as the [smd_lang_switch] shortcode.

WP-CLI
  wp smd import <file.zip|file.md> [--update] [--translation-of=<post ID>] --user=<admin>
- Imports exactly as the upload page does (Pending Review; --update for an existing pending or draft
  post). Prints the result, then one line per saved post: "<ID> <lang> <slug>". Run it as a user who
  can upload files.

INSTALLATION
1. In WordPress admin, go to Plugins > Add New Plugin > Upload Plugin.
2. Upload markdown-blog-importer-<version>.zip and click Install Now, then Activate.
3. Go to Tools > Markdown Blog Importer.
4. Upload a .md file using the format below and select its images (if any) in the Images field, or upload one .zip holding the .md and its images.
5. Open the resulting pending post and review it in the theme and in your SEO plugin's panel before publishing.

MARKDOWN TEMPLATE EXAMPLE
----------------------------------
---
title: "33 Crore Gods: The Truth About Hinduism"
slug: "33-crore-gods-truth-about-hinduism"
excerpt: "Explore the meaning behind the popular belief of 33 crore Hindu gods."
categories:
  - Hinduism
  - Philosophy
tags:
  - Hindu scriptures
  - Hindu philosophy
seo_title: "33 Crore Gods in Hinduism: Meaning Explained"
meta_description: "Discover what the concept of 33 crore gods means and how Hindu scriptures explain the diversity of divine forms."
canonical_url: ""
robots: "index,follow"
featured_image: "hero.jpg"
featured_image_alt: "Thousands of lit diyas in a temple courtyard at dusk"
featured_image_caption: "One flame, many lamps"
---

# 33 Crore Gods: The Truth About Hinduism

Intro paragraph with **bold text**, *italics*, and a [useful link](https://example.com/related-article).

## What Does 33 Crore Mean?

Your article text goes here.

![A banyan tree with lamps hanging from every branch](inline.jpg "One root, many branches")

### Important distinctions

- First point
- Second point
- Third point

## Conclusion

Your conclusion goes here.
----------------------------------

SUPPORTED FRONT MATTER
- title (required)
- slug
- excerpt
- categories (YAML list or comma-separated)
- tags (YAML list or comma-separated)
- seo_title
- meta_description
- canonical_url
- robots: index,follow | noindex,follow | index,nofollow | noindex,nofollow
- featured_image: file name of the hero image (uploaded in the Images field) or an http(s) URL; it becomes the featured image
- featured_image_alt, featured_image_caption: alt text and caption for the hero
- focus_keyword (the SEO plugin's focus keyword)
- lang, translation_key, category_key (see LANGUAGES)
- featured_image_id (an existing WordPress media attachment ID; used only when featured_image is empty)

IMAGES
- Hero: name it in the front matter (featured_image: hero.jpg). It is set as the featured image, not repeated in the body.
- Inline: put a line containing only ![alt text](inline.jpg "Optional caption") where the image belongs, usually at the end of the section it illustrates. It becomes a centred image block, with its caption centred under it.
- Images are matched by file name, so assets/inline.jpg in the Markdown finds an uploaded inline.jpg. An http(s) URL is downloaded into the Media Library instead.
- Every image the file names must be uploaded, or the import stops before creating anything and lists the missing files.
- Each new image is saved under the post's slug: hero.jpg in a post with slug art-of-leaving becomes art-of-leaving-hero.jpg, so every blog can use the same hero.jpg and inline.jpg names and the Media Library still gets descriptive, distinct file names. Its Media Library title is its alt text.
- JPEG, PNG, WebP or GIF, at most 10 MB each. Re-importing a post with the same image files reuses that post's existing Media Library items instead of duplicating them. Another post's identical image is not reused, so two posts sharing an image (such as the English and Hindi posts of one blog) each get their own copy with their own alt text.

LINKS
- [text](https://...) and site-relative [text](/post-slug/) links are converted. A site-relative link points into the site the post is imported to, so links between imported posts work on any site.

ALSO READ AND VIDEO
- A line "Also read: [Post title](https://...)" becomes a bordered box with the label and the linked title. For a Hindi post, write "यह भी पढ़ें: [शीर्षक](/slug/)"; the box shows the label as written. The link is kept as written.
- For a thumbnail, put an image before the link: "Also read: ![alt](also-read.jpg) [Post title](/slug/)", and include also-read.jpg with the upload. Without one, the box uses the featured image of the post on this site whose slug is the URL's last path segment (index.html is ignored), if there is one; otherwise it has no thumbnail.
- A line that is only a YouTube link, [Title](https://www.youtube.com/watch?v=...) or a bare URL, becomes an embedded video, with the link text as its caption. Watch, youtu.be, embed, shorts and live links all work.
- Some videos cannot be embedded, because their owner has turned embedding off. The importer checks this with YouTube at import time; such a video becomes the video's thumbnail, linking to it on YouTube, with the same caption. Re-importing a post checks every video again.

BOXES
- Lines ":::" or "::: name" and a later ":::" put everything between them in a bordered box (a group block with a 1px border, rounded corners and padding saved on the block), with "name" as its CSS class. For example:
    ::: takeaways
    ## Key Takeaways
    - First point
    :::
- Boxes can hold any of the other elements, including headings, lists, images and other boxes. A box left open at the end of the file is closed there.

BLOCKS
Every element becomes a standard WordPress core block, in the markup the block editor itself saves:
- paragraph (with bold, italic, strikethrough, links and line breaks inside it) -> Paragraph
- # to ###### heading -> Heading. A # heading becomes level 2, since the post title is the page's only level-1 heading.
- "- item" / "1. item" lists -> List of List items (bulleted or numbered)
- > quote lines -> Quote holding a Paragraph
- --- / *** / ___ -> Separator
- ![alt](file "caption") -> Image (centred, with caption)
- YouTube line -> Embed, or Image linking to the video when it cannot be embedded
- ::: box -> Group
- Also read line -> Group holding Columns: a Column with a linked Image thumbnail and a Column with a Paragraph
Before saving, the importer checks that the content parses back into exactly the same blocks; if not, nothing is saved.

ZIP UPLOAD
- Instead of the .md file and separate images, upload one .zip in the Markdown field. It must hold exactly one .md or .markdown file; its images (JPEG, PNG, WebP or GIF) may sit beside it or in any folder, such as assets/.
- Images are matched by file name as above, so two images with the same file name in different folders are rejected.
- Other files, hidden files and macOS __MACOSX entries are ignored. At most 100 files, 2 MB for the .md and 10 MB per image.
- An image also picked in the Images field replaces the zip's copy of it.
- The server's PHP upload_max_filesize and post_max_size must allow the zip's size.

HINDI AND OTHER LANGUAGES
- The .md file must be UTF-8. Titles, headings, body, tags, categories, alt text and captions can be in Hindi (Devanagari) or any other script.
- Give a Hindi post a Latin-letter slug (slug: "sansar-chhodne-ki-kala"), since WordPress would otherwise turn the Devanagari title into a long encoded URL.

LINE BREAKS
- End a line with two spaces or a backslash to keep a line break inside a paragraph or blockquote (useful for verses).

LIMITATIONS IN VERSION 3.0.0
- Does not write any SEO plugin's schema settings.
- Languages and translations are linked through Polylang only (WPML is not supported).
- If saving the second language's post fails after the first was saved (a rare server error, not a
  problem the checks find), the first is kept; the message says so, and a re-import with update fixes it.
- Fenced code blocks, tables, images inside a paragraph (an image must be on its own line), nested lists and raw HTML are not supported; such lines come through as plain text.
- Always back up the site and test on staging before installing on a production website.
