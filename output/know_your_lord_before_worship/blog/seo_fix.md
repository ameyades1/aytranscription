know_your_lord_before_worship: SEO fix

The originals (`know_your_lord_before_worship_blog.txt`, `_blog_en.txt`) are unchanged; the fixes are in `know_your_lord_before_worship_blog_seo.txt` and `_blog_seo_en.txt`.

## Hindi changes

| where | before | after | why |
|---|---|---|---|
| Opening, new paragraph after the second paragraph (before "गणेश कौन हैं? देवी कौन हैं?") | (none) | ज्ञानी भक्त कौन है? वह भक्त जो भगवान को केवल मानता नहीं, उन्हें भली-भांति जानता है। आचार्य जी समझाते हैं कि बिना समझे किसी देवता को मान लेना एक तस्वीर देखकर हुए प्रेम जैसा है, और श्रीमद्भगवद्गीता (७.१७) के अनुसार ऐसा ज्ञानी भगवान को अत्यंत प्रिय है। | The searched wording and the focus keyword were missing from the first 100 words, and the opening gave no direct answer. 47 words, built only from the blog: the gloss "भली-भांति जानता है", the photograph analogy and the 7.17 verse meaning. |
| H2 of the last teaching section | ## ज्ञानी भक्त: भगवान का सबसे प्रिय | ## ज्ञानी भक्त कौन है? भगवान का सबसे प्रिय | Puts the question readers search into a heading. The section answers it. |

## English changes

| where | before | after | why |
|---|---|---|---|
| Opening, new paragraph after the second paragraph (before "Who Is Ganesha? Who Is the Devi?") | (none) | Who is a jnani bhakta? A devotee who does not merely believe in God but knows Him thoroughly. Acharya Ji explains that accepting a deity without understanding is like falling for a photograph, and in the Bhagavad Gita (7.17) Shri Krishna says such a devotee is exceedingly dear to Him. | The searched wording and the focus keyword were missing from the first 100 words, and the opening gave no direct answer. 50 words, built only from the blog: "knows God thoroughly", the photograph analogy and the 7.17 verse meaning. |
| H2 of the last teaching section | ## The Devotee Who Knows: Dearest to God | ## Who Is a Jnani Bhakta? Dearest to God | Puts the question readers search into a heading. The section answers it. |

The number and order of the H2s, the verse, its translation and reference, the H1, every `links` phrase and the `also_read` heading are unchanged. The new paragraphs don't repeat any link phrase, so each link still goes to the same place.

## Checklist

Now met:
- Focus keyword within the first 100 words (both languages).
- The searched wording ("ज्ञानी भक्त कौन है" / "who is a jnani bhakta") is now used in the body, so it is the focus keyword. The section 2 mismatch is resolved.
- A direct answer near the top. This is not a checklist item, but section 4 of the report asked for it.

Still unmet:
- Each tag can be shared by at least 3 posts: "ज्ञानयोग" / "Jnana Yoga" is used by only one other post so far. Editing the text can't fix this; it depends on future posts or a tag decision.

Not changed (optional suggestions in the report): the authenticity flags from the Sanskrit review (half-verse, "तत्त्व से", IAST ṁ/ṃ) are about the verse, which this fix must not touch. The heading "बाल विवाह क्यों बंद हुआ?" / "Why Did We End Child Marriage?" was left as it is: it is not a checklist item, and only one or two headings should change.

## seo.json changes

| field | before | after |
|---|---|---|
| wordpress.hi.focus_keyword | ज्ञानी भक्त | ज्ञानी भक्त कौन है |
| wordpress.hi.secondary_keywords | ज्ञानी भक्त कौन है, पूजा से पहले भगवान को जानें, गीता 7.17 का अर्थ, भगवान को सबसे प्रिय भक्त | ज्ञानी भक्त, पूजा से पहले भगवान को जानें, गीता 7.17 का अर्थ, भगवान को सबसे प्रिय भक्त |
| wordpress.hi.slug | gyani-bhakt-puja-se-pehle-bhagwan-ko-jano | gyani-bhakt-kaun-hai |
| wordpress.en.focus_keyword | jnani bhakta | who is a jnani bhakta |
| wordpress.en.secondary_keywords | who is a jnani bhakta, know your God before you worship, Bhagavad Gita 7.17 meaning, devotee dearest to God | jnani bhakta, know your God before you worship, Bhagavad Gita 7.17 meaning, devotee dearest to God |
| wordpress.en.slug | jnani-bhakta-know-your-lord-before-worship | who-is-a-jnani-bhakta |

The titles and meta descriptions already contain the new focus keywords, so they are unchanged. `links` and `also_read` are unchanged too. The report's section 11 holds the same JSON, and its sections 2, 3 (recommended title, meta description and new slugs marked as in seo.json), 8 (schema keywords now lead with the new focus keyword; URL placeholders mapped to the new slugs) and 12 are updated. `python3 tools/check_seo.py know_your_lord_before_worship`: passed.

## Final seo.json values

| field | Hindi | English |
|---|---|---|
| slug | gyani-bhakt-kaun-hai | who-is-a-jnani-bhakta |
| focus keyword | ज्ञानी भक्त कौन है | who is a jnani bhakta |
| title | ज्ञानी भक्त कौन है? पूजा से पहले अपने भगवान को जानें | Who Is a Jnani Bhakta? Know Your Lord Before You Worship |
| meta description | ज्ञानी भक्त कौन है? आचार्य उपेंद्र जी बताते हैं कि पूजा से पहले भगवान को जानना क्यों ज़रूरी है, और गीता ७.१७ ज्ञानी भक्त को अत्यंत प्रिय क्यों कहती है। | Who is a jnani bhakta? Acharya Upendra Ji explains why we must know the God we worship, not just believe, for Gita 7.17 holds the knower supremely dear. |
