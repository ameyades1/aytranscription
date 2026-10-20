do_this_one_thing_achieve_successful_life: SEO fix

Fixed texts: `do_this_one_thing_achieve_successful_life_blog_seo.txt` (Hindi) and `do_this_one_thing_achieve_successful_life_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the second paragraph | (none) | तो काम में आनंद कैसे पाएं? संक्षेप में: बदले के लिए किया गया काम अपेक्षा और स्वार्थ लाता है, और अंत में दुख। आनंद तब आता है जब आप वह करें जो पैसे के बिना भी प्रिय हो, और जो कर रहे हैं उससे प्रेम करें, ताकि काम खेल जैसा लगे। | Focus keyword was not in the body or the first 100 words; early direct answer (about 45 words), built only from the blog's own points (report section 5) |
| Second H2 | ## खुश होकर करना: जब काम ही आनंद हो | ## काम में आनंद कैसे पाएं? खुश होकर करें | Heading as the question readers search; the section answers it (report section 4) |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the second paragraph | (none) | In short, here is how to find joy in your work. Work done only for a return brings expectation and self-interest, and in the end suffering. Joy comes when you do what you would enjoy even without money, and love what you do, so that your work feels like play. | Focus keyword was not in the body or the first 100 words; early direct answer (about 50 words), built only from the blog's own points (report section 5) |
| Second H2 | ## Acting from Happiness: When the Work Itself Is Joy | ## How to Find Joy in Your Work: Act from Happiness | Heading matches the searched query; the section answers it (report section 4) |

All `links` phrases and the `also_read` headings ("आचार्य जी स्वयं क्यों सिखाते हैं" / "Why Acharya Ji Teaches") are unchanged. The inline image's Hindi heading (images.txt) is unchanged. Scripture lines, the H1s and the teaching are untouched; the Sanskrit review's corrections (the Gita "passion" line and the निःस्वार्थ प्रेम gloss) are not SEO edits and were left for the editor.

## Checklist

Now met:
- Focus keyword in the body text (both languages; `tools/check_seo.py` failed on this before)
- Focus keyword in the English URL slug
- Focus keyword within the first 100 words (both languages)
- Focus keyword taken from wording the article uses (now in the `_seo` texts)
- A short direct answer early in the post; one H2 per language phrased as the searched question

Still unmet:
- No unsupported scriptural claims: the line attributing "those who follow their passion grow" to the Bhagavad Gita (report section 10, flag 1) remains. Fixing it would change the content, so it is left to the editor with the Sanskrit review's correction.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | find-joy-in-your-work | how-to-find-joy-in-your-work |

No other field changed: both focus keywords, titles and meta descriptions already contained the keyword; the Hindi slug stays `kaam-mein-anand-kaise-paayen`; `links` and `also_read` unchanged.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | kaam-mein-anand-kaise-paayen | how-to-find-joy-in-your-work |
| focus_keyword | काम में आनंद कैसे पाएं | how to find joy in your work |
| title | काम में आनंद कैसे पाएं: खुश होकर करें कर्म | How to Find Joy in Your Work: Act from Happiness |
| meta_description | क्या आप केवल वेतन और बदले के लिए काम करते हैं? आचार्य उपेंद्र जी बताते हैं कि काम में आनंद कैसे पाएं: खुश होकर कर्म करें, यही कर्मयोग की पात्रता है। | Working only for salary and reward? Acharya Upendra Ji explains how to find joy in your work by acting from happiness, which readies you for Karma Yoga. |
