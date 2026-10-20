every_human_inherently_spiritual: SEO fix

`check_seo.py` already passed, but the focus keywords "आध्यात्मिक और सांसारिक जीवन" and "spiritual and worldly life" were only in the H1 (and, in English, the Key Takeaways), not in the first 100 words of the body; the opening also had no direct answer, and no H2 was phrased as a searched question. Each language gets two changes: a short direct answer after the two opening paragraphs, built only from what the blog already says (and the report's section 5), which carries the focus keyword within the first 100 words; and one H2 rephrased as the video-title question. Focus keywords, slugs, titles and meta descriptions stay as they were.

## Hindi (`every_human_inherently_spiritual_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…वह आध्यात्मिक संसार है।") | (none) | आध्यात्मिक और सांसारिक जीवन दो अलग संसार नहीं हैं; संसार केवल एक है, और वह आध्यात्मिक है। दो सौ प्रतिशत जीवन का अर्थ है सौ प्रतिशत सांसारिक और सौ प्रतिशत आध्यात्मिक, एक साथ; बारह घंटे ऑफिस और बारह घंटे मंदिर नहीं। विवाह में शिव-पार्वती और ग्राहक में विष्णु को देखने से हर काम भगवान की सेवा बन जाता है। | Direct answer (59 words) restating the blog's own sections and Key Takeaways; puts the focus keyword in the body within the first 100 words. |
| H2 before the closing section | ## प्रेम और द्वेष का खेल | ## क्या हर मनुष्य आध्यात्मिक है? | The searched question (secondary keyword "हर मनुष्य आध्यात्मिक है", video title); the section concludes "कोई भी मनुष्य आध्यात्म से बाहर नहीं है". Number and order of headings unchanged. |

## English (`every_human_inherently_spiritual_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…it is a spiritual one.") | (none) | In short, spiritual and worldly life are not two separate worlds; there is only one world, and it is spiritual. Living two hundred percent means being fully worldly and fully spiritual at once, not splitting the day between office and temple. Seeing Shiva and Parvati in a marriage and Vishnu in a customer makes every task a service to God. | Direct answer (60 words), built only from the blog's own points; puts the focus keyword in the first 100 words. |
| H2 before the closing section | ## The Play of Love and Aversion | ## Is Every Human Inherently Spiritual? | The searched question (secondary keyword "every human is inherently spiritual", video title); the section concludes "No human being, then, stands outside the spiritual." Number and order of headings unchanged. |

No teaching, example, order of ideas, H1 or Markdown changed; the blog has no verses. All five `links` phrases and the `also_read` heading ("दो सौ प्रतिशत जीवन क्या है?" / "What Does It Mean to Live Two Hundred Percent?") are still in both texts, confirmed by grep. The inline image's heading ("विवाह और व्यापार में भगवान" / "Finding God in Marriage and Business") is unchanged.

## Checklist

The report had no section 12; one was added (from the standard checklist) with the fix.

- Now met: focus keyword within the first 100 words (both languages; Hindi also now in the body below the H1); one question H2; a direct answer of 40–60 words early in the post.
- Already met and still met: every other item. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose: the Sanskrit review's four Minor issues (the love/aversion attribution to Shankaracharya, the Bhaja Govindam "fear" paraphrase, "आध्यात्म" → "अध्यात्म", "आत्म तत्व" → "आत्मतत्त्व") are not SEO items and are left for the editor to fix in the original blog. Report sections 1, 4, 5 and 10 are not edited (this fix may only edit sections 2, 3, 8, 11 and 12); section 8 needed no change, as no title, description, keyword or slug changed.

## seo.json changes

None. The focus keywords already match the searched wording and now appear in the `_seo` bodies within the first 100 words; titles, meta descriptions and slugs already contain them. Slugs stay `adhyatmik-aur-sansarik-jeevan` (Hindi) and `spiritual-and-worldly-life` (English). `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged; the report's section 11 holds the same JSON. Sections 2 and 3 were updated and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | adhyatmik-aur-sansarik-jeevan | spiritual-and-worldly-life |
| focus_keyword | आध्यात्मिक और सांसारिक जीवन | spiritual and worldly life |
| title | आध्यात्मिक और सांसारिक जीवन: क्या सच में दो संसार हैं? | Spiritual and Worldly Life: Are They Really Separate? |
| meta_description | क्या आध्यात्मिक और सांसारिक जीवन अलग हैं? आचार्य उपेंद्र जी बताते हैं कि संसार एक ही है, विवाह और व्यापार भी पूजा हैं, और हर मनुष्य अनजाने में आध्यात्मिक है। | Are spiritual and worldly life really separate? Acharya Upendra Ji shows how marriage, business and duty become worship, and why every human is spiritual. |
