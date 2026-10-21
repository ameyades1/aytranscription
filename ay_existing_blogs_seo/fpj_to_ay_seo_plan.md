# Plan: copy FPJ SEO data and "Also Read" boxes into the AY blog

Status: decisions made (see "Decisions made"); next is the Python script. Written 2026-10-21.

## Goal

37 articles are published on both Free Press Journal (FPJ) and the AY blog (blogs.antaryogfoundation.in); the pairs are in `identical_blogs.json`. For each of these 37 AY posts:

- replace the AY post's SEO information with FPJ's
- add FPJ's "Also Read" boxes to the AY post, in the same places as on FPJ

## Approach

Build a small WordPress plugin that updates the 37 existing AY posts in place, driven by one JSON file that a Python script builds from the data already in this folder.

Do not re-import the posts. They are already published, the Markdown importer never overwrites published posts, and re-creating them risks changing their URLs.

### Step 1: a Python script builds `fpj_to_ay.json`

It reads `identical_blogs.json`, `fpj_blogs/` and `ay_blogs/`, and writes one record per AY post:

- **Which post:** the AY post's slug, so the plugin can find it.
- **SEO fields from FPJ:** title, meta description, keywords, Facebook (Open Graph) and Twitter tags, image alt text, and the H2 subheading.
- **"Also Read" boxes:**
  - Each box's link is changed from the FPJ article to its AY copy, using `identical_blogs.json`.
  - Each box's place is found by matching the text of the paragraph before it on FPJ (`position.preceding_paragraph_end` in the FPJ JSON) against the AY text. The AY text is 89–100% identical to FPJ's, so this matching is reliable.

### Step 2: the plugin, "FPJ SEO Sync" (under Tools in WordPress)

You upload `fpj_to_ay.json`, and the plugin:

1. **Shows a preview** for each post: the current values next to the FPJ ones, and where each "Also Read" box will go.
2. **On Apply,** writes the SEO fields into the active SEO plugin's per-post settings and inserts the "Also Read" boxes into the post's text.
3. **Saves the old values first** and creates a WordPress revision, so a **Restore** button can undo everything.
4. **Can be run again safely:** posts already done are skipped, and no box is added twice.

### Step 3: test locally, then go live

1. Import the 37 AY posts into the local WordPress (http://localhost:8080).
2. Run the plugin there and check the results.
3. Only then run it on the live site.

## Decisions made (2026-10-21)

Informed by `ay_vs_fpj_seo_comparison.md`.

| Question | Decision |
|---|---|
| SEO plugin to write to | Decide later. The plugin writes to whichever supported SEO plugin is active (as the Markdown importer does), and warns when both Yoast and SureRank are active. |
| Canonical URL | The user chooses in the plugin, per run: the AY page itself (default), the FPJ article, or leave unchanged. |
| SEO title and meta description | Copy FPJ's word for word now; improve them later in a separate `/seo_blog_fix`-style pass. |
| "Also Read" links to articles not on the AY blog (7) | Leave them out; add them once those 3 articles are on the AY blog. |
| What else is copied from FPJ | H2 subheading, image alt text, keywords (as tags or focus keyword), and the "Also Read" boxes (117), relinked to the AY copies. |
| What stays from AY | Post title, slug, categories, featured image. |
| "Also Read" box look | A simple styled block with the linked post's title and featured image, labelled "Read Also" as on FPJ. |

## Original decision list

1. **Canonical URL.** Strong recommendation: point it at the AY page itself, not FPJ's. Copying FPJ's canonical locks in the problem in `ay_blogs_seo_problem.md`, and the AY pages will not rank.
2. **Which SEO plugin stays on the live site, Yoast or SureRank.** The plugin should write to one of them. Fix the two-plugin conflict first; otherwise the second plugin's tags still override part of what we write.
3. **What to copy word for word.** FPJ's own SEO data is weak: titles with no keywords, meta descriptions longer than Google shows (about 200 characters), loose keyword lists. Copying it exactly may score worse than the current AY versions. Option: copy FPJ word for word as the starting point, then apply `/seo_blog_fix`-style improvements on top.
4. **Post titles.** Change them to FPJ's (for example "Navratri 2023: …" instead of "Navratri: …"), or change only the SEO title?
5. **How the "Also Read" box looks.** Suggestion: a simple styled block with the linked article's title and featured image, similar to FPJ's.

## Gap found: "Also Read" links to articles we don't have

FPJ has 124 "Also Read" links across the 37 articles. 117 point to articles among the 37 shared ones, so they can be pointed at the AY copies. The other 7 point to 3 FPJ articles by Acharya Ji that are on neither our FPJ list nor the AY blog:

- [Guru Gyan: Holi, the festival of colours and new beginnings](https://www.freepressjournal.in/spirituality/guru-gyan-holi-the-festival-of-colours-and-new-beginnings), linked from 3 articles: Guru Gyan: Who is a real Guru?; Guru Gyan: Awaken the giant within you... life lessons from Bhagavad Gita; Guru Gyan: What is the Antar Yog way of life? Here's all you need to know
- [Guru Gyan: Living life and handling people's expectations](https://www.freepressjournal.in/spirituality/guru-gyan-living-life-and-handling-people), linked from 2 articles: FPJ Anniversary 2022: Bharat’s future and your big role in it; Guru Gyan: What is the Antar Yog way of life? Here's all you need to know
- [Guru Gyan: Living soil is the solution](https://www.freepressjournal.in/spirituality/guru-gyan-living-soil-is-the-solution), linked from 2 articles: Guru Gyan: Awaken the giant within you... life lessons from Bhagavad Gita; Guru Gyan: What is the Antar Yog way of life? Here's all you need to know

This also shows FPJ's author page is missing more of his articles than the 6 found earlier.

**Decision needed:** for these 7 links, either link the box to the FPJ article, or leave the box out until the article is on the AY blog.

## Next step

Once the decisions above are made, build the Python script first and review `fpj_to_ay.json` before writing any plugin code.
