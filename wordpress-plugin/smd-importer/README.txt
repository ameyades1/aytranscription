SURE RANK MARKDOWN BLOG IMPORTER — VERSION 1.0.0

WHAT IT DOES
- Adds Tools > Markdown Blog Importer in WordPress admin.
- Accepts one .md/.markdown file (maximum 2 MB).
- Converts basic Markdown headings, paragraphs, bold/italic, links, lists, blockquotes and horizontal rules.
- Creates a WordPress post as a DRAFT (never publishes automatically).
- Supports title, slug, excerpt, categories, tags, SEO title, meta description, canonical URL and robots directive in front matter.
- Creates missing categories and tags.
- Prevents duplicate slugs by default; optional update is limited to existing drafts.
- Optionally assigns a featured image using an existing WordPress media attachment ID.

IMPORTANT SURE RANK NOTE
SureRank's SEO UI supports per-post Search Engine Title, Search Engine Description, canonical URL and robots settings. SureRank does not document a stable public PHP metadata-key contract for all of those fields. This importer therefore stores SEO title/description in its own custom fields instead of guessing SureRank's private metadata format. The canonical and robots values are retained as importer metadata but are NOT automatically applied to SureRank's output in this version.

To use SEO title/description from the importer fields in SureRank, go to SureRank > General Settings > Meta Templates and set the post Search Engine Title template to:
%custom_field.smd_seo_title%

Set the post Search Engine Description template to:
%custom_field.smd_seo_description%

Test this on a draft first. Template behavior can depend on the SureRank version/configuration; confirm the rendered <title> and meta description on a preview or staging site before publishing. If you prefer SureRank's built-in per-post overrides, keep the existing template and manually transfer those two fields in the SureRank panel. This plugin does not claim to write the native SureRank canonical/robots/schema fields.

INSTALLATION
1. In WordPress admin, go to Plugins > Add New Plugin > Upload Plugin.
2. Upload surerank-markdown-importer.zip and click Install Now, then Activate.
3. Go to Tools > Markdown Blog Importer.
4. Upload a .md file using the format below.
5. Open the resulting draft and review it in Astra and in the SureRank panel before publishing.

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
featured_image_id: ""
---

# 33 Crore Gods: The Truth About Hinduism

Intro paragraph with **bold text**, *italics*, and a [useful link](https://example.com/related-article).

## What Does 33 Crore Mean?

Your article text goes here.

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
- featured_image_id (an existing WordPress media attachment ID)

LIMITATIONS IN VERSION 1.0.0
- Does not upload image files; featured_image_id must refer to an image already in the WordPress Media Library.
- Does not implement native SureRank canonical/robots/schema writes.
- Markdown support is intentionally basic. Fenced code blocks, tables, embedded images and nested lists are not supported in this first version.
- SEO title and description fields are stored by this plugin. SureRank's custom-field template integration must be tested before production use.
- Always back up the site and test on staging before installing on a production website.
