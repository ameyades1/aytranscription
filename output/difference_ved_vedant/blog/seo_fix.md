difference_ved_vedant: SEO fix

The check failed before the fix: the Hindi meta description said "वेद और वेदांत में क्या अंतर है?", which is not the focus keyword word for word. Neither focus keyword ("वेद और वेदांत में अंतर" / "difference between Veda and Vedanta") appeared in the body, so neither was in the first 100 words, and the opening gave no direct answer; "वेदांत" / "Vedanta" only came halfway down. Each language now has a short direct answer after the two opening paragraphs, built only from what the blog already says (the Veda is the process of knowing, of this world and the world beyond; Vedanta is the end of the Vedas, where the final words of the rishis were recorded and knowing is complete; it is the jnana kanda, learned near the Guru in the Upanishad). It is report section 5's paragraph, cut to the blog's own wording. Two headings are now the questions readers search for (report section 4). Focus keywords, titles and slugs stay the same.

## Hindi (`difference_ved_vedant_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the two opening paragraphs, new paragraph | (none) | तो वेद और वेदांत में अंतर क्या है? आचार्य जी के अनुसार वेद कोई किताब नहीं, जानने की प्रक्रिया है: इस लोक और परलोक, दोनों का ज्ञान। वेदांत वेदों का अंत है, जहां ऋषियों के अंतिम वचन लिखे गए और जानने की प्रक्रिया पूरी हो जाती है। इसे ज्ञान कांड कहते हैं, जो उपनिषद में गुरु के समीप बैठकर सीखा जाता है। | Focus keyword in the body, within the first 100 words (word 50). Direct answer (53 words after the question) from report section 5, using only what the blog says. |
| `##` heading before "अब प्रश्न उठता है" | वेदांत: जहां जानना पूरा होता है | वेदांत क्या है? जहां जानना पूरा होता है | Question heading for the secondary keyword "वेदांत क्या है" (report section 4); the section answers it. |
| `##` heading before the three levels list | कर्मकांड से ज्ञान कांड तक | वेद के तीन कांड कौन-से हैं? | Question heading matching "कर्मकांड उपासना कांड ज्ञान कांड" and FAQ 3 (report section 4); the section lists the three kandas. |

## English (`difference_ved_vedant_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the two opening paragraphs, new paragraph | (none) | So what is the difference between Veda and Vedanta? According to Acharya Ji, the Veda is not a book but the process of knowing this world and the world beyond. Vedanta is the end of the Vedas, where the final words of the rishis were recorded and knowing is complete. It is the jnana kanda, learned near the Guru in the Upanishad. | Focus keyword in the body, within the first 100 words (word 61). Direct answer (53 words after the question) from report section 5, using only what the blog says. |
| `##` heading before "A question arises here" | Vedanta: Where Knowing Reaches Its End | What Is Vedanta? Where Knowing Reaches Its End | Question heading for the secondary keyword "what is Vedanta" (report section 4); the section answers it. |
| `##` heading before the three levels list | From Ritual to Knowledge | What Are the Three Kandas of the Veda? | Question heading matching "karma kanda and jnana kanda" and FAQ 3 (report section 4); the section lists the three kandas. |

No teaching, example, verse, translation, reference, H1 or order of ideas changed, and the number and order of headings are the same. The direct answer avoids the points the Sanskrit review questions (the "अहं वेद" gloss, apaurusheya, the tamasic chapters). "वेद यानी जानना, पर क्या जानना?" / "Veda Means Knowing, but Knowing What?" was kept, as section 4 advises and because `images.txt` places `inline.jpg` under it. All five `links` phrases and the `also_read` heading ("फिर राजसिक और सात्विक स्वर आते हैं" / "Then the Rajasic and Sattvic Voices Arrive") are unchanged in each language, and the page build found them all.

## Checklist

- Now met:
  - Focus keyword in the meta description (Hindi): it now uses "वेद और वेदांत में अंतर" word for word.
  - Focus keyword in the body text (both languages).
  - Focus keyword within the first 100 words (both languages).
  - A direct answer (40–60 words) early on, and two question headings.
- Section 12 was missing from the report. It has been added.
- Still unmet: 1. "No unsupported scriptural claims": the blog body still says the Vedas contain tamasic chapters on drinking and on many women, with no passage cited (report flag 1, Sanskrit review issue 1). Fixing it changes the teaching's wording, so it is for the editor to correct in the original blog. The titles, metas, snippet and FAQ do not use it.
- Left alone on purpose: the other Sanskrit review corrections (apaurusheya, "अहं वेद" = "मैं जानता हूँ", the Hindi Gita 2.45 attribution, सत्त्व/तत्त्व spelling, devavani, "original name of the Hindu tradition", ṃ in IAST) are for the editor in the original blog. If सात्त्विक is applied, the Hindi `also_read` heading in seo.json must be updated too (flag 6).

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | वेद और वेदांत में क्या अंतर है? आचार्य उपेंद्र जी बताते हैं कि वेद कोई किताब नहीं, जानने की प्रक्रिया है, और वेदांत वह भाग है जहां जानना पूर्ण होता है। | वेद और वेदांत में अंतर क्या है? आचार्य उपेंद्र जी बताते हैं कि वेद कोई किताब नहीं, जानने की प्रक्रिया है, और वेदांत वह भाग है जहां जानना पूर्ण होता है। |

Nothing else changed: focus keywords, secondary keywords, titles, slugs (old and new are both `ved-aur-vedant-mein-antar` / `difference-between-veda-and-vedanta`), `links`, `also_read`, `alt`, `caption`, `related`, category and tags. The report's section 11 holds the same JSON. These report sections were updated: 2 (keyword note), 3 (the Hindi meta, and the metas and slugs in seo.json marked as recommended), 4 (a note on what was applied), 8 (the Hindi description) and 12 (the checklist, newly added). Section 8's headline is the unchanged H1; its alternativeHeadline, keywords and suggested slugs already match seo.json.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ved-aur-vedant-mein-antar | difference-between-veda-and-vedanta |
| focus_keyword | वेद और वेदांत में अंतर | difference between Veda and Vedanta |
| title | वेद और वेदांत में अंतर: वेद किताब नहीं, जानने की यात्रा | Difference Between Veda and Vedanta: Knowing, Not a Book |
| meta_description | वेद और वेदांत में अंतर क्या है? आचार्य उपेंद्र जी बताते हैं कि वेद कोई किताब नहीं, जानने की प्रक्रिया है, और वेदांत वह भाग है जहां जानना पूर्ण होता है। | What is the difference between Veda and Vedanta? Acharya Upendra Ji explains why the Veda is a process of knowing, and why Vedanta is where knowing ends. |
