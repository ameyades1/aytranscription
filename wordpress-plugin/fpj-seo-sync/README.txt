FPJ SEO Sync
============

Copies Free Press Journal (FPJ) SEO data and "Read Also" boxes onto the matching AY blog posts.

Input: fpj_to_ay.json, built in the repo by
    cd ay_existing_blogs_seo && python3 build_fpj_to_ay.py

Install: Plugins > Add New > Upload Plugin, choose fpj-seo-sync-<version>.zip, activate.
Use:     Tools > FPJ SEO Sync.

1. Upload fpj_to_ay.json. Posts are matched by slug (any status except trash).
2. Choose the canonical URL (the AY post, the FPJ article, or unchanged) and which parts to copy:
   - SEO title and meta description (FPJ's, word for word, except descriptions over 160
     characters, which use the shortened versions)
   - Facebook and Twitter title and description (Yoast SEO only)
   - the FPJ H2 subheading, added at the top of the post
   - the featured image alt text (changes the image's alt everywhere it is used)
   - keywords as post tags (off by default)
   - the "Read Also" boxes, each placed after the paragraph it follows on FPJ. Each box links to
     the target's live AY address and image from fpj_to_ay.json, never to this site's address, so
     boxes made on a staging site work once pushed to live. Styles are inline, so the boxes look
     right even where this plugin is not active.
     Each box image's alt text is the linked post's title, as on FPJ.
   A "Shortened meta descriptions" table above the preview lists the descriptions that
   were shortened (FPJ's over 160 characters, replaced in fpj_to_ay.json from
   description_overrides.json), next to FPJ's original. The preview shows every description's
   length, in red over 160. On apply, any description still over 160 is cut at a word and the
   report says so.
3. Tick posts in the preview and apply.

Safety:
- Before changing a post, its content, SEO fields, image alt text and tags are saved in
  _fpjss_backup. "Restore" in the preview puts them all back.
- Content changes go through wp_update_post, so WordPress also keeps a revision.
- A post already applied is skipped until restored, so boxes are never added twice.
- SEO fields are written to Yoast SEO, SureRank and Rank Math, whichever are active. With both
  Yoast and SureRank active the page shows a warning: deactivate one.
