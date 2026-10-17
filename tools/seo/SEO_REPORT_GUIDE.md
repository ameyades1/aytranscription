# The SEO report, explained from scratch

This guide explains every section of a `/seo_blog` report (for example
`tools/seo/33_crore_gods_truth_about_hinduism.md`) for someone who has never studied SEO.

## First, what SEO is

When someone types a question into Google, Google has to pick about 10 pages to show from millions. **SEO (Search Engine Optimization)** means making your page easy for Google to understand and trust, so it picks yours, and making the result look worth clicking when it appears.

It comes down to three things:
1. **Being found:** Google can read and understand your page.
2. **Being chosen:** Google thinks your page is the best answer to the question.
3. **Being clicked:** your title and description in the results make people want to open it.

Everything in the report serves one of these. Here is each section in order.

---

## 1. Summary

This sets out the opportunity:
- **Who searches:** people asking "why does Hinduism have 33 crore gods?" Some are young Hindus who were asked this by friends, some are from other faiths, some live abroad.
- **What the competing pages are like:** mostly short lists arguing whether *koti* means "crore" or "kinds".
- **What your blog offers that they don't:** Acharya Ji's explanation (one God, many roles; form versus essence) with everyday examples.

**Concept: search intent.** This means *why* someone searches. "33 crore gods" is usually someone wanting an **explanation**, sometimes someone wanting to **defend their faith**. Google ranks the pages that best fit the intent, not just the ones that contain the words.

---

## 2. Keywords

**Concept: keyword.** The exact words people type into Google. People phrase the same question in many ways:
- English: "33 crore gods"
- Hindi: "33 कोटि देवता" or "33 करोड़ देवी देवता"
- Hinglish (Hindi in English letters): "33 crore devi devta ka sach"

Google treats each spelling and language separately, so the report lists them all.

The table columns:
- **Language:** each one is planned on its own, since Hindi searchers don't type translated English.
- **Intent:** what the person wants. *Informational* means they want to understand something. *Apologetic* means they want to defend their faith.
- **Priority:** which keywords this page should aim at. The **primary keyword** ("33 crore gods", "33 कोटि देवता") is the main target. The others are **secondary keywords**, related phrasings the page can also show up for.

The report says no volume numbers were used. SEO tools such as Ahrefs and Semrush show how many people search each phrase monthly and how hard it is to rank. We didn't use any, so the priorities are judgement.

---

## 3. Titles and meta

On a Google results page, each result shows:

```
33 Crore Gods or One God? The Truth About Hinduism   ← title tag
blogs.antaryogfoundation.in › en › 33-crore-gods       ← URL (with slug)
Why does Hinduism have 33 crore gods? Acharya ...      ← meta description
```

- **Title tag:** the blue clickable headline. This is the single most important thing on the page for Google. Keep it under about 60 characters or Google cuts it off with "…", and put the keyword near the start. Your page's current title, "तैंतीस कोटि देवता या एक भगवान", writes the number out in words. People type "33", so the report suggests using "33" in the title tag. The heading readers see on the page (the **H1**) can stay as it is. The two can differ.
- **Meta description:** the two grey lines under the title. It doesn't affect ranking directly, but it decides whether people click. It works like a shop window. Yours currently just repeats the title, which wastes the space.
- **Slug:** the end part of the URL. `/en/33-crore-gods-or-one-god` is readable and contains the keyword. `/post?id=4821` isn't.
- **CTR (click-through rate):** of 100 people who see your result, how many click. A good title and description raise it.

Our generator doesn't use these yet. They're recommendations for whoever sets the final title and meta tags on the published site.

---

## 4. Outline changes

**Concept: headings (H1, H2, H3).** The H1 is the page's main title, H2s are section headings, and H3s are sub-sections. Google reads headings to understand what each part of the page covers. A heading phrased as a real question, like "रूप और स्वरूप में क्या अंतर है?", can match that exact search.

The report's main suggestion is to add a line explaining what *koti* means, since that's the most-searched sub-question. Without it, the post looks like it is avoiding the question next to competitors. The report also suggests linking the thin idol section to the fuller post on murtis rather than expanding it. These are suggestions only; the text has not been changed.

---

## 5. Direct answer paragraph

**Concept: featured snippet.** Sometimes Google shows a boxed answer at the very top, above all results, quoted from one page. **AI Overviews** (Google's AI summary) and tools like ChatGPT do something similar. They prefer a clear, self-contained answer of 40–60 words.

The blogs' opening paragraph already does this, which is why the "In short" box was removed from the pages. The only gap in this blog is that the opening doesn't contain "33 कोटि". This section of the report is still useful as a check that the opening answers the question.

---

## 6. FAQ

Questions people commonly ask about the topic, answered from the talk. These are kept only in the report, not on the page. That fits, because Google now rarely shows FAQs from sites like yours as special results. The questions are still useful for YouTube descriptions, Instagram captions, or spotting what the blog doesn't cover.

---

## 7. Internal links

**Concept: internal links** are links from one of your pages to another of your pages. They matter for three reasons:
1. **Readers stay longer** and read more of Acharya Ji's teaching instead of leaving after one post.
2. **Google finds and understands your pages** by following links, and a page with many links pointing to it looks important.
3. **Topic authority:** when many posts on one theme link to each other, Google sees the site as an expert on that theme.

Related terms:
- **Anchor text:** the clickable words. "Why worship a murti if God is formless" tells Google what the linked page is about. "Click here" tells it nothing.
- **Topic cluster / pillar page:** a set of related posts around one main overview post (the pillar) on a big theme like "Gods and Devtas". Every post links to the pillar and the pillar links to all of them. There is no Gods and Devtas pillar yet, so the report uses *Know Before You Worship* as a temporary hub.
- **Keyword cannibalization:** two of your own posts competing for the same search, so Google doesn't know which to show and both rank lower. The report warns that *Know Before You Worship* and this post could overlap on "do you know your God", so this post should stay focused on "33 crore".

This is the part `/seo_blog` applies to the page: the in-text links, the "Also read" box and Further Reading.

---

## 8. Schema

**Concept: structured data (schema).** Hidden code on the page, invisible to readers, that labels its content for Google: "this is an article, the author is Brahmarshi Acharya Upendra Ji, the publisher is Antar Yog Foundation, it includes this YouTube video lasting 6:30". It's written in a format called **JSON-LD**.

Google can then show richer results, such as the author, a video thumbnail with its length, and the **breadcrumb** path (Home › Blog › Post) instead of a raw URL. It also helps Google connect all of Acharya Ji's content to one person, which builds trust.

The `{{...}}` parts are placeholders for facts we don't have, such as publish dates and final URLs. The report doesn't guess them.

The technical notes below the schema matter:
- **Open Graph tags:** control the preview (image, title, description) when someone shares the link on WhatsApp or Facebook. The page has none, so WhatsApp shares look plain. Your audience shares heavily on WhatsApp, so this is valuable.
- **hreflang:** tells Google that the Hindi and English pages are translations of each other, so Hindi searchers get the Hindi one. The page holds both languages on one URL behind a toggle. Google treats it as a Hindi page, so the English version will rarely appear in English searches. The recommended fix is separate `/hi/` and `/en/` pages.
- **Canonical tag:** tells Google which URL is the "official" copy of a page, when the same content is reachable at more than one address.
- **Embedding the video:** playing it on the page instead of linking out keeps readers on your site.

---

## 9. Images

- **Alt text:** a written description of an image. Blind readers' screen readers read it aloud, Google uses it to understand the image, and it appears if the image fails to load. The hero's alt text just repeated the title. A good one describes what's shown: one brass lamp with thousands of diyas around it. The report also found the Hindi page using English alt text for one image.
- **File names:** `33-koti-devta-ek-jyoti-anek-deep.jpg` tells Google something; `hero.jpg` doesn't. This also helps in Google Images.
- **Compression:** large images slow the page. Google ranks slow pages lower, especially on phones.

---

## 10. Authenticity flags

This section isn't standard SEO. It's the rule built into the prompt: **SEO must never bend the teaching.** In the 33 crore gods report it lists six places where chasing searches could cause harm:

1. **"330 million":** people search "33 crore", but the page shouldn't claim scripture literally counts 330 million gods. *Koti* can also mean "kinds", as the Sanskrit review already flagged.
2. **"Other religions don't accept idol worship":** this is an overstatement that readers from other faiths will see, and it's still in the blog.
3. **तत्व vs तत्त्व:** a spelling the review flagged and that hasn't been fixed.
4. **The Chandogya verse:** the verse's meaning hasn't been checked against Gita Press yet.
5. **"All religions worship the same God":** don't use this as a title. It's Acharya Ji's view, not the post's main point, and it invites arguments.
6. **Lakshmi = earning power, and so on:** these are Acharya Ji's teaching explanations, not full scriptural definitions, so they should always be credited to him.

Points 1–3 are fixes to the blog text that only the editor can approve.

---

## 11. seo.json

A copy of the exact values the skill wrote to `output/<name>/blog/seo.json`: the title tag, alt text, captions, links, Also read and Further reading that the page uses, and the `wordpress` part (slug, focus and secondary keywords, meta description, category and tags) to enter in WordPress. The check script makes sure this copy always matches the file.

---

## Two more ideas behind the report

- **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness): what Google looks for, especially on topics that shape people's beliefs and lives. Verse references, a named author with a bio, and accurate content all count. The Sanskrit reviews help with this too.
- **SEO is slow:** changes take weeks to months to show up in rankings. That's why the prompt includes monthly and quarterly checks using **Google Search Console**, a free Google tool that shows which searches your pages appear for, how often, and how many people click.

**In short:** the keywords say *what to aim for*, the titles and meta are *what people see in the results*, headings and the opening paragraph are *what Google reads*, links and schema are *how Google connects and trusts your pages*, and the authenticity flags make sure none of it changes what Acharya Ji actually said.
