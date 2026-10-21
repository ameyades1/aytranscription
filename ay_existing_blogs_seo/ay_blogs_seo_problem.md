# AY blog SEO problem: two SEO plugins, conflicting canonicals

Site: https://blogs.antaryogfoundation.in (Founder's Reflections, 39 posts)
Checked: 2026-10-21, from each post's page source. Data: `ay_blogs/ay_articles.json` (`seo.canonical`, `seo.meta`, `seo.json_ld`).

## Summary

Every post's `<head>` contains two complete sets of SEO tags, from two plugins running at once:

1. **Yoast SEO v28.7** (between `<!-- This site is optimized with the Yoast SEO plugin v28.7 ... -->` and `<!-- / Yoast SEO plugin. -->`)
2. **SureRank** (after `<!-- SureRank Meta Data -->`)

On **37 of 39** posts, Yoast's canonical points to the **Free Press Journal** copy of the article, while SureRank's canonical points to the AY page itself. Two canonicals that disagree are a conflicting signal; Google then chooses on its own and, for content first published on FPJ, is likely to credit FPJ. The AY pages may be treated as duplicates and not ranked.

## Example (Ganesh Chaturthi post)

```html
<!-- Yoast -->
<link rel="canonical" href="https://www.freepressjournal.in/weekend/ganesh-chaturthi-2023-celebrate-the-festival-in-the-right-way" />
<meta property="og:url" content="https://www.freepressjournal.in/weekend/ganesh-chaturthi-2023-celebrate-the-festival-in-the-right-way" />

<!-- SureRank -->
<link rel="canonical" href="https://blogs.antaryogfoundation.in/ganesh-chaturthi-celebrate-the-festival-in-the-right-way/">
<meta property="og:url" content="https://blogs.antaryogfoundation.in/ganesh-chaturthi-celebrate-the-festival-in-the-right-way/">
```

## Everything that is duplicated

On all 39 posts, both plugins output: `canonical`, `og:locale`, `og:type`, `og:title`, `og:description`, `og:url`, `og:site_name`, `article:published_time`, `twitter:card`. Also `og:image` / `og:image:width` / `og:image:height` (37 posts with a featured image) and `article:modified_time` (18 posts).
Both also output a separate JSON-LD schema graph. In Yoast's graph, the Article and WebPage `@id`/`url` values also point to the FPJ URL.

The descriptions differ too: Yoast's `og:description` is an auto-excerpt ending in `[…]`; SureRank's is a cut-off first sentence.

## Posts with the FPJ canonical (37)

| AY post | Yoast canonical points to |
|---|---|
| [Navratri: How To Celebrate This Festival In Its True Sense](https://blogs.antaryogfoundation.in/navratri-how-to-celebrate-this-festival-in-its-true-sense/) | https://www.freepressjournal.in/weekend/navratri-2023-how-to-celebrate-this-festival-in-its-true-sense |
| [Pitru Paksha: Real Secret To Liberate Ancestors & Solve Problems](https://blogs.antaryogfoundation.in/pitru-paksha-real-secret-to-liberate-ancestors-solve-problems/) | https://www.freepressjournal.in/weekend/pitru-paksha-real-secret-to-liberate-ancestors-solve-problems |
| [Thousands Of Seekers Attend Antar Yog Pitru Rin Mukti Shibir Every Year During Pitru Paksha And Get Instant Results Thereafter](https://blogs.antaryogfoundation.in/thousands-of-seekers-attend-antar-yog-pitru-rin-mukti-shibir-every-year-during-pitru-paksha-and-get-instant-results-thereafter/) | https://www.freepressjournal.in/spirituality/thousands-of-seekers-attend-antar-yog-pitru-rin-mukti-shibir-every-year-during-pitru-paksha-and-get-instant-results-thereafter |
| [Ganesh Chaturthi: Celebrate The Festival In The Right Way](https://blogs.antaryogfoundation.in/ganesh-chaturthi-celebrate-the-festival-in-the-right-way/) | https://www.freepressjournal.in/weekend/ganesh-chaturthi-2023-celebrate-the-festival-in-the-right-way |
| [Do you know that the real purpose of Jagran is to awaken you to your true self?](https://blogs.antaryogfoundation.in/do-you-know-that-the-real-purpose-of-jagran-is-to-awaken-you-to-your-true-self/) | https://www.freepressjournal.in/spirituality/do-you-know-that-the-real-purpose-of-jagran-is-to-awaken-you-to-your-true-self |
| [Do you meet people by coincidence or for a reason? The science behind runanubandh](https://blogs.antaryogfoundation.in/do-you-meet-people-by-coincidence-or-for-a-reason-the-science-behind-runanubandh/) | https://www.freepressjournal.in/spirituality/do-you-meet-people-by-coincidence-or-for-a-reason-the-science-behind-runanubandh |
| [Do you know the true purpose of prayer? Understanding the art and science of prayer](https://blogs.antaryogfoundation.in/do-you-know-the-true-purpose-of-prayer-understanding-the-art-and-science-of-prayer/) | https://www.freepressjournal.in/spirituality/do-you-know-the-true-purpose-of-prayer-understanding-the-art-and-science-of-prayer |
| [Why do good people suffer? Here’s why](https://blogs.antaryogfoundation.in/why-do-good-people-suffer-heres-why/) | https://www.freepressjournal.in/spirituality/why-do-good-people-suffer-heres-why |
| [Bharat’s future and your big role in it](https://blogs.antaryogfoundation.in/bharats-future-and-your-big-role-in-it/) | https://www.freepressjournal.in/spirituality/fpj-anniversary-2022-bharats-future-and-your-big-role-in-it |
| [Guru Purnima special: Why do you need a Guru?](https://blogs.antaryogfoundation.in/guru-purnima-special-why-do-you-need-a-guru/) | https://www.freepressjournal.in/spirituality/guru-purnima-special-why-do-you-need-a-guru |
| [International Day of Yoga: Your ‘yoga’ is incomplete without THIS](https://blogs.antaryogfoundation.in/international-day-of-yoga-your-yoga-is-incomplete-without-this/) | https://www.freepressjournal.in/spirituality/international-day-of-yoga-your-yoga-is-incomplete-without-this |
| [Her right education is our bright future](https://blogs.antaryogfoundation.in/her-right-education-is-our-bright-future/) | https://www.freepressjournal.in/spirituality/her-right-education-is-our-bright-future |
| [The role of in-laws in the successful married life of a woman](https://blogs.antaryogfoundation.in/the-role-of-in-laws-in-the-successful-married-life-of-a-woman/) | https://www.freepressjournal.in/spirituality/the-role-of-in-laws-in-the-successful-married-life-of-a-woman |
| [Key role of parents in the successful marriage of a woman](https://blogs.antaryogfoundation.in/key-role-of-parents-in-the-successful-marriage-of-a-woman/) | https://www.freepressjournal.in/spirituality/key-role-of-parents-in-the-successful-marriage-of-a-woman |
| [The importance of setting the right boundaries in every woman’s life](https://blogs.antaryogfoundation.in/the-importance-of-setting-the-right-boundaries-in-every-womans-life/) | https://www.freepressjournal.in/spirituality/the-importance-of-setting-the-right-boundaries-in-every-womans-life |
| [Do saints commit sin if they consume meat?](https://blogs.antaryogfoundation.in/do-saints-commit-sin-if-they-consume-meat/) | https://www.freepressjournal.in/weekend/do-saints-commit-sin-if-they-consume-meat |
| [Guru Gyan: Who is a real Guru?](https://blogs.antaryogfoundation.in/guru-gyan-who-is-a-real-guru/) | https://www.freepressjournal.in/spirituality/guru-gyan-who-is-a-real-guru |
| [Guru Gyan: Do you really love others? Or only your own self?](https://blogs.antaryogfoundation.in/guru-gyan-do-you-really-love-others-or-only-your-own-self/) | https://www.freepressjournal.in/spirituality/guru-gyan-do-you-really-love-others-or-only-your-own-self |
| [Guru Gyan: You must read this if you love anyone](https://blogs.antaryogfoundation.in/guru-gyan-you-must-read-this-if-you-love-anyone/) | https://www.freepressjournal.in/spirituality/guru-gyan-you-must-read-this-if-you-love-anyone |
| [Guru Gyan: Are you Wise or Otherwise? Understanding the difference between knowledge and wisdom](https://blogs.antaryogfoundation.in/guru-gyan-are-you-wise-or-otherwise-understanding-the-difference-between-knowledge-and-wisdom/) | https://www.freepressjournal.in/spirituality/guru-gyan-are-you-wise-or-otherwise-understanding-the-difference-between-knowledge-and-wisdom |
| [Guru Gyan: Awaken the giant within you… life lessons from Bhagavad Gita](https://blogs.antaryogfoundation.in/guru-gyan-awaken-the-giant-within-you-life-lessons-from-bhagavad-gita/) | https://www.freepressjournal.in/spirituality/guru-gyan-awaken-the-giant-within-you-life-lessons-from-bhagavad-gita |
| [The right way of idol worship, its significance and the science behind it](https://blogs.antaryogfoundation.in/the-right-way-of-idol-worship-its-significance-and-the-science-behind-it/) | https://www.freepressjournal.in/spirituality/the-right-way-of-idol-worship-its-significance-and-the-science-behind-it |
| [The untold science behind idol worship](https://blogs.antaryogfoundation.in/the-untold-science-behind-idol-worship/) | https://www.freepressjournal.in/spirituality/the-untold-science-behind-idol-worship |
| [What’s the ‘ideal’ way of idol worshipping?](https://blogs.antaryogfoundation.in/whats-the-ideal-way-of-idol-worshipping/) | https://www.freepressjournal.in/spirituality/whats-the-ideal-way-of-idol-worshipping |
| [Do multiple forms of gods and goddesses exist in other religions apart from Hindu? Read on to find out more](https://blogs.antaryogfoundation.in/do-multiple-forms-of-gods-and-goddesses-exist-in-other-religions-apart-from-hindu-read-on-to-find-out-more/) | https://www.freepressjournal.in/spirituality/do-multiple-forms-of-god-and-goddess-exist-in-other-religions-read-on-to-find-out-more |
| [Do Hindus really have 33 koti devatas? Here’s the truth behind the belief](https://blogs.antaryogfoundation.in/do-hindus-really-have-33-koti-devatas-heres-the-truth-behind-the-belief/) | https://www.freepressjournal.in/spirituality/do-hindus-really-have-33-koti-devatas-heres-the-truth-behind-the-belief |
| [Why multiple forms of God were designed and their deep significance as per our scriptures](https://blogs.antaryogfoundation.in/why-multiple-forms-of-god-were-designed-and-their-deep-significance-as-per-our-scriptures/) | https://www.freepressjournal.in/spirituality/why-multiple-forms-of-god-were-designed-and-their-deep-significance-as-per-our-scriptures |
| [Settling the debate: Veg v/s Non-Veg](https://blogs.antaryogfoundation.in/settling-the-debate-veg-v-s-non-veg/) | https://www.freepressjournal.in/weekend/settling-the-debate-veg-vs-non-veg |
| [Significance of a perfect life partner in every woman’s life](https://blogs.antaryogfoundation.in/significance-of-a-perfect-life-partner-in-every-womans-life/) | https://www.freepressjournal.in/spirituality/significance-of-a-perfect-life-partner-in-every-womans-life |
| [The art of leading a virtuous life that every woman must know](https://blogs.antaryogfoundation.in/the-art-of-leading-a-virtuous-life-that-every-woman-must-know/) | https://www.freepressjournal.in/spirituality/the-art-of-leading-a-virtuous-life-that-every-woman-must-know |
| [Here’s why you shouldn’t take your diet lightly](https://blogs.antaryogfoundation.in/heres-why-you-shouldnt-take-your-diet-lightly/) | https://www.freepressjournal.in/spirituality/heres-why-you-shouldnt-take-your-diet-lightly |
| [These 7 divine qualities are naturally present in women, but they are not aware of it](https://blogs.antaryogfoundation.in/these-7-divine-qualities-are-naturally-present-in-women-but-they-are-not-aware-of-it/) | https://www.freepressjournal.in/spirituality/these-7-divine-qualities-are-naturally-present-in-women-but-they-are-not-aware-of-it |
| [The untold purpose of your diet that you should know](https://blogs.antaryogfoundation.in/the-untold-purpose-of-your-diet-that-you-should-know/) | https://www.freepressjournal.in/weekend/the-untold-purpose-of-your-diet-that-you-should-know |
| [Did you know that there is a connection between food and your karma?](https://blogs.antaryogfoundation.in/did-you-know-that-there-is-a-connection-between-food-and-your-karma/) | https://www.freepressjournal.in/weekend/did-you-know-that-there-is-a-connection-between-food-and-your-karma |
| [Why do people worship symbols or photos? Tracing the origin of idol worship](https://blogs.antaryogfoundation.in/why-do-people-worship-symbols-or-photos-tracing-the-origin-of-idol-worship/) | https://www.freepressjournal.in/spirituality/why-do-people-worship-symbols-or-photos-tracing-the-origin-of-idol-worship |
| [Common misconceptions about spiritual donations and gifts](https://blogs.antaryogfoundation.in/common-misconceptions-about-spiritual-donations-and-gifts/) | https://www.freepressjournal.in/spirituality/common-misconceptions-about-spiritual-donations-and-gifts |
| [Guru Gyan: What is the Antar Yog way of life? Here’s all you need to know](https://blogs.antaryogfoundation.in/guru-gyan-what-is-the-antar-yog-way-of-life-heres-all-you-need-to-know/) | https://www.freepressjournal.in/spirituality/guru-gyan-what-is-the-antar-yog-way-of-life-heres-all-you-need-to-know |

## Posts without the FPJ canonical (2)

These still have both plugins' tags, but both canonicals point to the AY page:

- [I Thought I Had Control Over Myself. Then I Realised My Senses Were Controlling Me](https://blogs.antaryogfoundation.in/i-thought-i-had-control-over-myself-then-i-realised-my-senses-were-controlling-me/)
- [What Mahakali Taught Me About Bhakti, Fear and Where We Surrender](https://blogs.antaryogfoundation.in/what-mahakali-taught-me-about-bhakti-fear-and-where-we-surrender/)

## What to fix

1. **Use one SEO plugin.** Deactivate either Yoast or SureRank so each page has one canonical, one set of Open Graph tags and one schema graph.
2. **Decide the canonical deliberately.** If the AY blog should rank for these articles, set each post's canonical to its own AY URL (in Yoast: post → Yoast SEO → Advanced → Canonical URL; clear the FPJ link). If the FPJ canonical was set on purpose (syndication, agreement with FPJ), keep it, but then these AY pages will not rank and SEO effort on them is wasted.
3. **Check after the fix.** View the page source of a few posts: there should be exactly one `<link rel="canonical">`. Then use Google Search Console → URL Inspection to see "Google-selected canonical" and request re-indexing.
