knowledge_work_for_you: SEO fix

The originals (`knowledge_work_for_you_blog.txt`, `_blog_en.txt`) are unchanged; the fixes are in `knowledge_work_for_you_blog_seo.txt` and `_blog_seo_en.txt`.

## Hindi changes

| where | before | after | why |
|---|---|---|---|
| Opening, new paragraph after the second paragraph (before "## हर प्राणी अपने स्वभाव से बँधा है") | (none) | हम जानते हुए भी सही क्यों नहीं कर पाते? भगवद्गीता ३.३३ कहती है कि ज्ञानी भी अपनी प्रकृति के अनुसार ही चेष्टा करता है, इसलिए केवल किताबी ज्ञान हमें पाप से नहीं रोकता। गीता ३.३४ समाधान देती है: राग और द्वेष, यानी पसंद-नापसंद, के वश में न हों। और आचार्य जी कहते हैं: प्रेय नहीं, श्रेय चुनें। | The focus keyword "जानते हुए भी सही क्यों नहीं कर पाते" was not in the body at all (SureRank error), and the opening gave no direct answer. 57 words, built only from the blog: the 3.33 meaning, "केवल किताबी ज्ञान पाप से नहीं रोकता" (Key points), the 3.34 teaching "इन दोनों के वश में नहीं होना चाहिए", and "प्रेय नहीं, श्रेय चुनें". The Duryodhana quote (report flag 1) is left out of it. |
| Second H2 | ## किताबी ज्ञान की सीमा | ## क्या केवल ज्ञान पाप से रोकता है? | A question readers search for (report section 4). The section answers it: "ज्ञान पाप करने से नहीं रोकता है।" |

## English changes

| where | before | after | why |
|---|---|---|---|
| Opening, new paragraph after the second paragraph (before "## Every Being Is Bound by Its Nature") | (none) | Why do we end up knowing what is right but not doing it? Bhagavad Gita 3.33 says that even the learned act according to their own nature, so book learning alone does not stop wrongdoing. Gita 3.34 gives the way out: do not fall under the control of attraction and aversion. Acharya Ji's advice: choose shreyas over preyas. | The focus keyword "knowing what is right but not doing it" was not in the body (SureRank error), and the opening gave no direct answer. 58 words, built only from the blog: the 3.33 meaning, "book learning alone does not stop wrongdoing" (Key Takeaways), the 3.34 meaning "Do not fall under their control", and "Choose shreyas over preyas". The Duryodhana quote (report flag 1) is left out of it. |
| Second H2 | ## Where Book Learning Falls Short | ## Does Knowledge Alone Stop Wrongdoing? | A question readers search for (report section 4). The section answers it: "knowledge alone does not stop a person from doing wrong." |

The number and order of the H2s, the verses, their translations and references, the H1, every `links` phrase and the `also_read` heading are unchanged. The new paragraphs repeat no link phrase, so each link still goes to the same place.

## Checklist

Now met:
- Focus keyword in the body text (both languages); it was missing, which `check_seo.py` reported as an error.
- Focus keyword in the meta description (both languages) and in the English slug.
- Focus keyword within the first 100 words (both languages).
- Focus keyword taken from wording the article uses (now true of the `_seo` texts).
- A direct answer near the top. This is not a checklist item, but section 4 of the report asked for it.

Still unmet: none. Section 12 was missing from the report; it has been added with every item met.

Not changed (outside this fix): the Sanskrit review's accuracy issues are left to the editor, as the fix must not change the teaching, verses or meanings: the heading "गीता पहले दुर्योधन को सुनाई गई थी" / "The Gita Was First Offered to Duryodhana" (review issue 3, report flag 2), the Duryodhana "cure" passage (issue 2), the incomplete Hindi 3.34 meaning (issue 1), the name readings, the daivi sampatti list, the "moha (attachment)" gloss and IAST ṁ/ṃ (issues 4 to 8). The heading "समाधान: पसंद-नापसंद से ऊपर उठना" / "The Way Out: Rising Above Likes and Dislikes" was left as it is: only one heading per language needed to change.

## seo.json changes

| field | before | after |
|---|---|---|
| wordpress.hi.meta_description | सही जानते हुए भी कर नहीं पाते? आचार्य उपेंद्र जी गीता ३.३३-३४ से बताते हैं कि केवल ज्ञान क्यों काफ़ी नहीं, और राग-द्वेष से ऊपर उठकर श्रेय कैसे चुनें। | जानते हुए भी सही क्यों नहीं कर पाते? आचार्य उपेंद्र जी गीता ३.३३-३४ से बताते हैं कि केवल ज्ञान क्यों काफ़ी नहीं, और राग-द्वेष से ऊपर उठकर श्रेय कैसे चुनें। |
| wordpress.en.meta_description | Know what is right but cannot do it? Acharya Upendra Ji explains Gita 3.33-3.34: why knowledge alone fails and how to rise above likes and dislikes. | Knowing what is right but not doing it? Acharya Upendra Ji explains Gita 3.33-3.34: why knowledge alone fails and how to rise above likes and dislikes. |
| wordpress.en.slug | knowing-right-but-not-doing-it | knowing-what-is-right-but-not-doing-it |

The Hindi slug `jaante-hue-bhi-sahi-kyon-nahi-kar-paate` already follows the focus keyword, so it is unchanged. The focus keywords, secondary keywords, titles, `links` and `also_read` are unchanged. The meta descriptions are 155 (Hindi) and 151 (English) characters. The report's section 11 holds the same JSON, and its sections 2 (keyword note), 3 (recommended titles, meta descriptions and slugs marked as in seo.json), 8 (schema descriptions; URL placeholders mapped to the slugs) and 12 (added) are updated. `python3 tools/check_seo.py knowledge_work_for_you`: passed.

## Final seo.json values

| field | Hindi | English |
|---|---|---|
| slug | jaante-hue-bhi-sahi-kyon-nahi-kar-paate | knowing-what-is-right-but-not-doing-it |
| focus keyword | जानते हुए भी सही क्यों नहीं कर पाते | knowing what is right but not doing it |
| title | जानते हुए भी सही क्यों नहीं कर पाते? गीता 3.33 का उत्तर | Knowing What Is Right but Not Doing It: Gita 3.33-34 |
| meta description | जानते हुए भी सही क्यों नहीं कर पाते? आचार्य उपेंद्र जी गीता ३.३३-३४ से बताते हैं कि केवल ज्ञान क्यों काफ़ी नहीं, और राग-द्वेष से ऊपर उठकर श्रेय कैसे चुनें। | Knowing what is right but not doing it? Acharya Upendra Ji explains Gita 3.33-3.34: why knowledge alone fails and how to rise above likes and dislikes. |
