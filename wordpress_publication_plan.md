# WordPress publication plan: staging first, then blogs.antaryogfoundation.in

Checked 26 Nov 2026 against the Markdown Blog Importer 3.0.0 (`wordpress-plugin/smd-importer/`), the
zips from `tools/make_post_zip.py` and the live site.

## What the live site has now

- WordPress 7.1.5, Astra theme, Elementor installed.
- **No Polylang and no Hindi**: no hreflang links and no `/hi/` addresses. The site is English only.
- **Yoast SEO and SureRank both active**: every page prints two canonical tags.
- 8 categories: Daan (Donation), Diet, Festivals and Observances, Ganesh Vidya, Guru Gyan,
  Idol Worship, Uncategorized, Women Empowerment.

## Does the importer need changes?

No code changes are needed for staging. It was built for this:

- Posts are created as **Pending Review**, never published.
- Links between posts are written **site-relative** (`/slug/`, `/hi/slug/`), so they are correct
  on staging and on live.
- It writes SEO fields to every active SEO plugin (Yoast and SureRank both).

Points to settle, none of them code:

| # | Point | Why it matters | Decision needed |
|---|---|---|---|
| 1 | **Hindi** | Our zips hold English and Hindi. Without Polylang, the Hindi post is still created, but there are no `/hi/` URLs, no per-language categories, and both posts sit in one mixed list. | Install and set up Polylang on staging (and later live), or import English only (`--lang en`). |
| 2 | **Categories** | Our posts use their own categories (for example "Deities & Worship"); the importer creates any that are missing, alongside the 8 live ones. | Keep ours, or map them to the live categories first. |
| 3 | **Image addresses** | Images in the post body are saved with full staging addresses (`https://staging.../wp-content/uploads/...`), as WordPress always does. | Push staging to live with a tool that rewrites the domain (the host's "push to live" usually does). Copying posts by hand would break the images. |
| 4 | **Duplicate SEO plugins** | Two canonical tags on every page. | Deactivate one (Yoast or SureRank) on staging first, and on live at go-live. |
| 5 | **SureRank image titles** | SureRank renames every uploaded image's title (see the plugin README). | Turn off "auto set image title" on staging if SureRank stays. |
| 6 | **Links to posts not yet imported** | A link to a talk that is not on the site yet is kept as `/slug/` and reported. | Import all talks, then re-import those with reported links (`--update`, while still Pending). |
| 7 | **Updates after publishing** | `--update` only changes Pending or Draft posts. | Finish all fixes on staging before publishing. |

## Steps

1. **Back up live** (database and uploads).
2. **Refresh staging** from live, so slugs and media match.
3. **On staging**: decide points 1, 2 and 4; set up Polylang if chosen; turn off SureRank image titles if needed.
4. **Install** the importer zip (`wordpress-plugin/build_zip.sh`) on staging.
5. **Pilot**: import 2 or 3 talks; check layout, images, video, Also read boxes, language switch,
   SEO panel, categories and links, on desktop and mobile.
6. **Import the rest** (`wp smd import <zip> --user=<admin>`, or the upload page); then re-import
   those with unresolved links.
7. **Review and publish on staging** (Pending to Published), in batches.
8. **Push staging to live** with the domain rewrite; check a few posts' image and link addresses on live.
9. **After go-live**: submit the sitemap in Search Console, check that the GitHub Pages copy stays
   noindex, and spot-check pages for one canonical tag.

## Hindi URLs: /hi/<english-slug>

Wanted: the English post at `/<english-slug>/` and its Hindi translation at `/hi/<english-slug>/`.
Today the Hindi post gets its own Latin slug from seo.json (for example `/hi/pashu-bali-ka-arth/`).

- **WordPress needs a unique slug per post**, so with free Polylang the Hindi post would become
  `<english-slug>-2`. Only **Polylang Pro** ("Share slugs", paid) allows the same slug in each language.
- **The importer refuses it now**: it rejects two files with the same slug, and its "slug already
  exists" check is not per language.
- With Polylang Pro, the changes needed are:
  - `tools/make_post_zip.py`: give the Hindi post the English slug.
  - Importer: allow the same slug across languages, check existing posts per language, find
    link targets per language, and save the Hindi post through Polylang so it keeps the shared slug.
  - Then test on staging that both URLs open the right post and the language switch and hreflang work.
- Without Polylang Pro, the nearest is `/hi/<english-slug>-hi/`.

**Decision (26 Nov 2026): `/hi/<english-slug>-hi/`.** Done:
- `seo.json` of all 146 talks: the Hindi slug is now the English slug with `-hi`; the JSON copies
  in `seo_report.md` / `seo_fix.md` were updated to match.
- `tools/make_post_zip.py` always builds the Hindi slug from the English one, so Hindi in-text and
  Also read links also point to `/hi/<english-slug>-hi/`.
- `tools/check_seo.py` fails a talk whose Hindi slug is not the English slug with `-hi`.
- The `/seo_blog` and `/seo_blog_fix` skills and `tools/prompts/seo_blog_specialist.txt` state the rule.
- The local test WordPress still has the Hindi posts under the old slugs; remove them before
  re-importing there, or the importer refuses the new ones as a second Hindi post for the same talk.

## Open questions

- Is Hindi going on the live site now (Polylang), or English first?
- Keep our categories, or map to the live ones?
- Which SEO plugin stays: Yoast or SureRank?
- How is staging pushed to live (host tool, migration plugin, other)?
