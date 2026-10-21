FPJ SEO Sync
============

Copies Free Press Journal (FPJ) SEO data and "Read Also" boxes onto the matching AY blog posts.

Input: fpj_to_ay.json, built in the repo by
    cd ay_existing_blogs_seo && python3 build_fpj_to_ay.py

Install: Plugins > Add New > Upload Plugin, choose fpj-seo-sync-<version>.zip, activate.
Use:     Tools > FPJ SEO Sync.

1. Upload fpj_to_ay.json. Posts are matched by slug (any status except trash).
2. Choose the canonical URL (the AY post, the FPJ article, or unchanged) and which parts to copy:
   - SEO title and meta description (FPJ's, word for word)
   - Facebook and Twitter title and description (Yoast SEO only)
   - the FPJ H2 subheading, added at the top of the post
   - the featured image alt text (changes the image's alt everywhere it is used)
   - keywords as post tags (off by default)
   - the "Read Also" boxes, each placed after the paragraph it follows on FPJ and linked to the
     target post on this site (or to its AY address if that post is not here)
3. Tick posts in the preview and apply.

Safety:
- Before changing a post, its content, SEO fields, image alt text and tags are saved in
  _fpjss_backup. "Restore" in the preview puts them all back.
- Content changes go through wp_update_post, so WordPress also keeps a revision.
- A post already applied is skipped until restored, so boxes are never added twice.
- SEO fields are written to Yoast SEO, SureRank and Rank Math, whichever are active. With both
  Yoast and SureRank active the page shows a warning: deactivate one.
