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

One change was made (version 3.1.0, 26 Nov 2026): links to posts not published yet are hidden
when a page is shown (see "Publishing in waves of 5"). Otherwise it was already built for this:

- Posts are created as **Pending Review**, never published.
- Links between posts are written **site-relative** (`/slug/`, `/hi/slug/`), so they are correct
  on staging and on live.
- It writes SEO fields to every active SEO plugin (Yoast and SureRank both).

Points to settle, none of them code:

| # | Point | Why it matters | Decision needed |
|---|---|---|---|
| 1 | **Hindi** | Our zips hold English and Hindi. Without Polylang, the Hindi post is still created, but there are no `/hi/` URLs, no per-language categories, and both posts sit in one mixed list. | Install and set up Polylang on staging (and later live), or import English only (`--lang en`). |
| 2 | **Categories** | Our posts use their own categories (for example "Deities & Worship"); the importer creates any that are missing, alongside the 8 live ones. | **Decided:** keep the 8 site categories and add 7 (`category_mapping.xlsx`). `make_post_zip.py` must then write the site category, not ours. |
| 3 | **Image addresses** | Images in the post body are saved with full staging addresses (`https://staging.../wp-content/uploads/...`), as WordPress always does. | Push staging to live with a tool that rewrites the domain (the host's "push to live" usually does). Copying posts by hand would break the images. |
| 4 | **Duplicate SEO plugins** | Two canonical tags on every page. | Deactivate one (Yoast or SureRank) on staging first, and on live at go-live. |
| 5 | **SureRank image titles** | SureRank renames every uploaded image's title (see the plugin README). | Turn off "auto set image title" on staging if SureRank stays. |
| 6 | **Links to posts not yet imported** | A link to a talk that is not on the site yet is kept as `/slug/`, and its Also read box gets no thumbnail. | **Import all 146 talks before publishing any**, so every link and thumbnail resolves; publishing then happens in waves. |
| 7 | **Updates after publishing** | `--update` only changes Pending or Draft posts. | Finish all fixes on staging before publishing. |

## Using the importer

**What it does with one talk's zip** (built by `tools/make_post_zip.py`: `en.md`, `hi.md` and the
images in `assets/`):

1. Checks everything first (front matter, slugs, images, languages); if anything is wrong, nothing
   is created and the message says why.
2. Creates each language's post as **Pending Review**: title, slug, excerpt, category and tags
   (created if missing), the text as ordinary blocks, the hero as featured image, the inline image,
   Also read boxes, the YouTube video under "Watch the Discourse", and the SEO title, meta
   description, focus keyword and robots in every active SEO plugin.
3. Links the two languages through Polylang (if installed); Hindi links point to `/hi/<slug>-hi/`.
4. Hides, on the public pages, links to posts not published yet (3.1.0).

**One-time setup on each site (staging, later live):**

1. Plugins > Add New > Upload Plugin: `markdown-blog-importer-3.1.0.zip`
   (`wordpress-plugin/build_zip.sh`), and activate it.
2. Polylang with English and Hindi, for Hindi posts (as `~/wordpress/setup_polylang.sh` did locally).
3. One SEO plugin active (Yoast or SureRank).
4. If SureRank stays: turn off its automatic image titles (one `wp eval` line in the plugin README).
5. Language switch position: bottom of Tools > Markdown Blog Importer.

**One talk per import (decided).** Each import takes one zip, that is one talk in both languages.

| Way | Per run | Several talks |
|---|---|---|
| Upload page (Tools > Markdown Blog Importer) | 1 zip | Upload the zips one after another |
| WP-CLI: `wp smd import <file.zip> --user=<admin>` | 1 zip | A shell loop runs them all unattended |

Build all the zips, then import them with WP-CLI:

```
for t in $(ls output/*/blog/seo.json | cut -d/ -f2); do python3 tools/make_post_zip.py "$t" zips/; done
for z in zips/*.zip; do wp smd import "$z" --user=<admin>; done
```

Each run prints `<ID> <lang> <slug>` for the posts it created; a zip that fails its checks is
skipped and the loop goes on. WP-CLI needs command-line (SSH) access to the server and WP-CLI
installed by the host; without it, use the upload page.

**Good to know:**

- `--update` (or the upload page's update box) replaces a post with the same slug only while it is
  Pending or Draft; published posts are never overwritten.
- Re-importing reuses the post's images instead of duplicating them.
- `./publish_wordpress.sh` is for the local test site only: it publishes posts straight away.

## Steps

1. **Back up live** (database and uploads).
2. **Refresh staging** from live, so slugs and media match.
3. **On staging**: decide points 1, 2 and 4; set up Polylang if chosen; turn off SureRank image titles if needed.
4. **Install** the importer zip (`wordpress-plugin/build_zip.sh`) on staging.
5. **Pilot**: import 2 or 3 talks; check layout, images, video, Also read boxes, language switch,
   SEO panel, categories and links, on desktop and mobile.
6. **Import all the rest** as Pending (`wp smd import <zip> --user=<admin>`, or the upload page),
   before anything is published. Reviewers then review and edit them on staging; posts are never
   re-imported after that.
7. **Push staging to live** with the domain rewrite, with all posts still Pending; check a few posts'
   image and link addresses on live.
8. **Publish on live in waves of 5**, in the order of the "Publishing waves" sheet of
   `category_mapping.xlsx` (English and Hindi of a talk together). Links to talks of later waves
   stay hidden until those are published.
9. **After each wave and after the last**: submit the sitemap in Search Console, check that the
   GitHub Pages copy stays noindex, and spot-check pages for one canonical tag.

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

## Publishing order: links between posts

Measured from the 146 talks' seo.json (26 Nov 2026):

- The WordPress posts carry **830 links to other talks** (in-text links and Also read boxes), about 6
  per post. "Related" cards exist only on the GitHub pages.
- **136 of the 146 talks form one linked cluster**: each can be reached from every other by
  following links, with links going both ways. So **there is no order** in which posts can be
  published one by one or in batches without some links pointing to posts that are not live yet
  (a 404 for readers and Google).
- 9 talks get no links from any other talk.

Options:

| Option | How | Broken links | Effort |
|---|---|---|---|
| **A. Launch all at once (recommended)** | Import all 146 talks (both languages) on staging as Pending, review them all, push to live, publish them together | None | Most review before anything goes live |
| B. Waves, links held back | Change the importer to write plain text instead of a link when the target post is not published, and add a "relink" command that restores links in published posts after each wave | None, but early posts have fewer links until relinked | Importer changes; a re-link after every wave |
| C. Waves as they are | Publish in batches and accept 404s until the targets are published | Many, for weeks | None |

A scheduled post (WordPress "Scheduled") is not public until its date, so scheduling does not
avoid the problem; it is the same as C.

## Publishing in waves of 5 (decided 26 Nov 2026)

Decision: publish **5 talks at a time**, starting with one talk and the talks it links to, then the
next. This is option B, done without any re-import:

**1. Import everything first.** All 146 talks are imported as Pending before any is published, so
every link already has its final address and every Also read box its thumbnail. Reviewers review
and edit on staging; nothing is re-imported later.

**2. The importer hides links to unpublished posts (version 3.1.0).**

- When a post is shown, a link to another post of the site that is not published yet (pending,
  draft, scheduled or missing) is shown as plain text, and an Also read box pointing to one is
  left out. Readers and Google never meet a 404.
- The saved post is never changed. When a wave is published, every link and box pointing to it
  appears on all posts at once.
- Not applied in the admin, the block editor or post previews, so reviewers always see every link.
  Links to pages, categories, other sites and files are never touched.
- Tested on the local WordPress: switching a linked post to Draft hid the link and its Also read
  box on the posts linking to it; publishing it again brought both back. Hindi text and pages are
  unaffected, and the saved post content stayed identical.

**How the link hiding works** (`hide_unpublished_links()` and `link_is_live()` in
`wordpress-plugin/smd-importer/surerank-markdown-importer.php`):

1. **When it runs.** WordPress passes every post's text through the `the_content` filter just before
   showing it; the importer hooks in at priority 20 (after the blocks are built). It works on the
   text on its way to the screen; the post saved in the database is never changed. It returns the
   text untouched in the admin and block editor (`is_admin()`, REST requests), in post previews
   (`is_preview()`, how reviewers see Pending posts), and when the text has no `href=`.
2. **Finding the links.** It loads the post's HTML into PHP's HTML parser (`DOMDocument`), wrapped in
   a temporary `<div id="smd-root">` and marked UTF-8 so Hindi text survives, and goes through every
   `<a>`. A link already removed with its box (a box can hold two links) is skipped.
3. **Is the link live?** For each link:
   - another site, email or other scheme: live, left alone;
   - a path not starting with `/` (such as `#section`): left alone;
   - the language prefix (`/hi/slug/`, from Polylang's language list) and the site's own sub-folder,
     if any, are removed;
   - only a single-segment address (`/slug/`) counts as a post link; longer paths (`/category/x/`)
     and files (`.jpg`, `.pdf`) are left alone;
   - the slug is looked up (`get_posts`, any status, any language). If a post has it, the link is
     live only when that post is **published**; pending, draft, scheduled and private hide it. If
     no post has it, the link stays when a page, attachment or category has that slug, or it is a
     WordPress address such as `/blog/` or `/feed/`; otherwise the target does not exist and the
     link is hidden;
   - each slug's answer is remembered for the rest of the page view (one lookup per slug), and
     forgotten whenever any post changes status, so publishing a wave takes effect at once.
4. **What happens to a hidden link.** Inside an Also read box (class `also-read`): the whole box,
   thumbnail included, is removed. Anywhere else: only the `<a>` tag is removed and its words stay as
   plain text. If nothing was hidden, the original text is returned exactly as it was.
5. **Cost.** One database lookup per distinct linked slug (about 6 per post), on post pages only.
   With a page-cache plugin, clear the cache after publishing each wave.

**Test results on the local WordPress (26 Nov 2026):**

| Test | Result |
|---|---|
| Post with an Also read box to a published post | Box and links shown |
| Target set to Draft | Box and links hidden |
| Target published again | Box and links shown again |
| Text link whose target is set to Pending | Link removed, words kept |
| Saved content of the linking post | Unchanged throughout |
| Real English and Hindi pages | Load normally, Hindi intact, no PHP errors |

All test posts were restored to Published.

**3. The wave order.** The "Publishing waves" sheet in `category_mapping.xlsx` lists 30 waves of 5.
Each wave starts with the unpublished talk most linked from the talks already live (so it reveals
the most hidden links), followed by the talks it links to. Share of links on live posts that are
still hidden (shown as plain text) after each wave:

| After wave | Talks live | Links hidden |
|---|---|---|
| 1 | 5 | 79% |
| 5 | 25 | 31% |
| 10 | 50 | 25% |
| 15 | 75 | 13% |
| 20 | 100 | 8% |
| 25 | 125 | 1% |
| 26 to 30 | 130 to 146 | 0% |

Early posts read fine without those links; they gain them as later waves go live.

**After all waves**, new talks only link to talks already live (`/seo_blog` chooses links from
existing talks), so they can be published one at a time.

## Other SEO points found

| # | Issue | What to do |
|---|---|---|
| 1 | **Two SEO plugins** (Yoast and SureRank): two canonical tags, two sets of schema and sitemaps | Keep one; deactivate the other before the launch |
| 2 | **Topic overlap with the 39 posts already live**, which can make our new posts compete with them in Google: 33 crore gods / "Do Hindus really have 33 koti devatas?"; our murti talks / the 7 Idol Worship posts; our meat talks / "Do saints commit sin if they consume meat?" and "Veg v/s Non-Veg"; pind daan, Mahalaya and Pitru Rin / "Pitru Paksha: Real Secret..."; What is a Guru / "Who is a real Guru?"; What to ask God in prayer / "True purpose of prayer"; Ganesh Chaturthi 10 days / "Ganesh Chaturthi: Celebrate The Festival In The Right Way"; The Future of Bharat / "Bharat's future and your big role in it" | Keep their focus keywords different (they mostly are), and link each pair to each other so Google sees them as related, not duplicates |
| 3 | **No links between our talks and the 39 live posts**, either way | Add the live posts as link targets in seo.json (links / also_read), and add links from the live posts to ours (FPJ SEO Sync or by hand) |
| 4 | **9 talks with no incoming links** | Give each at least one link from a related talk; category pages also help |
| 5 | **GitHub Pages copy** of the same text | Already noindex. Once live, also add a canonical link on each GitHub page to its WordPress post |
| 6 | **Staging search setting** ("Discourage search engines", noindex) can be copied to live by the push | After the push, check live robots.txt, a post's robots meta, and Settings > Reading |
| 7 | **Newsletter plugin is active on live**: publishing 146 posts may send 146 emails if it mails new posts | Check its automatic new-post emails; turn them off for the launch, send one announcement instead. Same for any auto-share to social media |
| 8 | **Hindi and English versions** | Polylang adds hreflang links between them; check one pair, and that the sitemap lists both languages |
| 9 | **Image sizes**: hero and inline images are about 250 KB each | Let WordPress make smaller sizes (it does); consider WebP or compression for page speed |
| 10 | **Sitemap and Search Console** | Submit the sitemap after launch; watch Coverage for 404s and duplicate warnings for a few weeks |
| 11 | **New category pages** with only a few posts | Fine to start; add a short description to each category |

## Open questions

- Is Hindi going on the live site now (Polylang), or English first?
- Which SEO plugin stays: Yoast or SureRank?
- How is staging pushed to live (host tool, migration plugin, other)?
