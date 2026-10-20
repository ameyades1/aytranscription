SURE RANK MARKDOWN BLOG IMPORTER — VERSION 1.5.0

WHAT IT DOES
- Adds Tools > Markdown Blog Importer in WordPress admin.
- Accepts one .md/.markdown file (maximum 2 MB), or one .zip (maximum 50 MB) holding the .md and its images.
- Converts basic Markdown headings, paragraphs, bold/italic, links, lists, blockquotes and horizontal rules.
- Creates the WordPress post as PENDING REVIEW (never publishes automatically). An editor reviews it and publishes it.
- Supports title, slug, excerpt, categories, tags, SEO title, meta description, canonical URL and robots directive in front matter.
- Creates missing categories and tags.
- Prevents duplicate slugs by default; optional update is limited to existing pending or draft posts.
- Imports images uploaded with the Markdown file: the hero becomes the post's featured image (shown by Astra at the top of the post) and each inline image is placed where the Markdown puts it, with its alt text and caption.
- Optionally assigns a featured image using an existing WordPress media attachment ID instead.

SURERANK
The importer writes seo_title, meta_description, focus_keyword and canonical_url into the post's own SureRank settings (the surerank_settings_general post meta, the same place the SureRank panel saves them), and robots into SureRank's no-index and no-follow flags. The post's SureRank panel shows these values, and no template setup is needed. Copies are also kept in smd_seo_title, smd_seo_description, smd_canonical_url and smd_robots. Empty fields fall back to SureRank's defaults (for the title, %title% - %site_name%). Schema is not written. This was tested with SureRank 1.10.2; check the SureRank panel on a draft after a SureRank update.

INSTALLATION
1. In WordPress admin, go to Plugins > Add New Plugin > Upload Plugin.
2. Upload surerank-markdown-importer.zip and click Install Now, then Activate.
3. Go to Tools > Markdown Blog Importer.
4. Upload a .md file using the format below and select its images (if any) in the Images field, or upload one .zip holding the .md and its images.
5. Open the resulting pending post and review it in Astra and in the SureRank panel before publishing.

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
- focus_keyword (SureRank's focus keyword)
- featured_image_id (an existing WordPress media attachment ID; used only when featured_image is empty)

IMAGES
- Hero: name it in the front matter (featured_image: hero.jpg). It is set as the featured image, not repeated in the body.
- Inline: put a line containing only ![alt text](inline.jpg "Optional caption") where the image belongs, usually at the end of the section it illustrates. It becomes an image block (figure with caption).
- Images are matched by file name, so assets/inline.jpg in the Markdown finds an uploaded inline.jpg. An http(s) URL is downloaded into the Media Library instead.
- Every image the file names must be uploaded, or the import stops before creating anything and lists the missing files.
- JPEG, PNG, WebP or GIF, at most 10 MB each. Re-importing a post with the same image files reuses the existing Media Library items instead of duplicating them.

ALSO READ AND VIDEO
- A line "Also read: [Post title](https://...)" becomes a boxed link. If a post on this site has the URL's last path segment as its slug (index.html is ignored), the box shows that post's featured image as a thumbnail. The link itself is kept as written.
- A line that is only a YouTube link, [Title](https://www.youtube.com/watch?v=...) or a bare URL, becomes an embedded video, with the link text as its caption. Watch, youtu.be, embed, shorts and live links all work.

ZIP UPLOAD
- Instead of the .md file and separate images, upload one .zip in the Markdown field. It must hold exactly one .md or .markdown file; its images (JPEG, PNG, WebP or GIF) may sit beside it or in any folder, such as assets/.
- Images are matched by file name as above, so two images with the same file name in different folders are rejected.
- Other files, hidden files and macOS __MACOSX entries are ignored. At most 100 files, 2 MB for the .md and 10 MB per image.
- An image also picked in the Images field replaces the zip's copy of it.
- The server's PHP upload_max_filesize and post_max_size must allow the zip's size.

LINE BREAKS
- End a line with two spaces or a backslash to keep a line break inside a paragraph or blockquote (useful for verses).

LIMITATIONS IN VERSION 1.5.0
- Does not write SureRank schema settings.
- Markdown support is intentionally basic. Fenced code blocks, tables, images inside a paragraph (an image must be on its own line) and nested lists are not supported in this first version.
- Always back up the site and test on staging before installing on a production website.
