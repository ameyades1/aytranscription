true_disciple_change_your_life: SEO fix

Copies written: `true_disciple_change_your_life_blog_seo.txt` (Hindi) and `true_disciple_change_your_life_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro ("...तुमने सीखा, यह कब माना जाएगा?") | (none) | सच्चा शिष्य कौन है? आचार्य जी के अनुसार, वह जिसमें गुरु के शब्द केवल कान तक नहीं रुकते, बल्कि सिर, हृदय, रक्त और कृति (आचरण) से होते हुए संस्कार बन जाते हैं। श्रुति का अंत सदा कर्म में होता है। जो ज्ञान कभी कर्म में न बदले, वह व्यर्थ है; एक ओवी, एक वाक्य भी जीवन में उतर जाए, तो पर्याप्त है। | The focus keyword "सच्चा शिष्य कौन है" was not in the body (check_seo error) and the opening gave no direct answer. The paragraph (report sections 4 and 5) uses only what the blog says (the six stages, "श्रुति का अंत सदा कर्म में होता है", "वह ज्ञान व्यर्थ है", the single ovi); it puts the keyword within the first 100 words |
| H2 5 | श्रुति का अंत कर्म में होता है | कैसे जानें कि सच में सीखा? श्रुति का अंत कर्म में होता है | A question readers ask (report FAQ 2, "कैसे पता चले कि मैंने सच में कुछ सीखा?"); the section answers it ("\"तुमने जाना\" यह तभी कहा जाता है जब वह जानना कर्म में उतर आए"). The original wording is kept after the question |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro ("...that you have learned something?") | (none) | What makes a true disciple? According to Acharya Ji, it is one in whom the Guru's words do not stop at the ear, but travel through the head, heart, blood and conduct until they become samskaras. Shruti always ends in action. Knowledge that never turns into action is wasted, and living out even one ovi, one sentence, is enough. | The focus keyword "what makes a true disciple" was not in the body (only split across an H2; check_seo error) and the opening gave no direct answer. The paragraph (report section 5) uses only what the blog says; it puts the keyword within the first 100 words |
| H2 5 | Shruti Always Ends in Action | How Do You Know You Have Really Learned? Shruti Always Ends in Action | A question readers ask (report FAQ 2); the section answers it ("you can say you have known something only when that knowing shows up in what you do"). The original wording is kept after the question |

The headings keep their number and order; the inline image and the Also read box are placed by section position. No teaching, example, verse, verse reference or H1 was touched. All five `links` phrases and the `also_read` headings ("कान से संस्कार तक: गुरु के शब्दों की यात्रा" / "From the Ear to the Samskaras: How the Guru's Words Travel") are still in the texts word for word, and each link phrase still comes first where it was.

## Checklist

Now met:
- Focus keyword in the body text: both languages (both failed `check_seo.py` before).
- Focus keyword in the URL slug (English): the old slug `true-disciple-knowledge-into-action` did not contain "what makes a true disciple"; the new slug does.
- Focus keyword within the first 100 words: both languages, in the direct-answer paragraph.
- Direct answer early (report section 5): added in both languages.
- Question headings: one more H2 per language is now a natural question (two H2s were already questions).

Still unmet (1):
- No unsupported scriptural claims: both texts credit "एक तरी ओवी अनुभवावी" to Sant Dnyaneshwar, while it closes Sant Namdev's abhang on the Jnaneshwari (Sanskrit review issue 1, report flag 1). Changing a verse's source line is outside the SEO fix's rules, so it is left to the editor; no SEO field names the author. The minor review issues 2–5 (Vedic hymn gloss, anuchana gloss, "data and dhata", सात्त्विक spelling) are also left to the editor.

`python3 tools/check_seo.py true_disciple_change_your_life` passes.

## Report updates

- Section 2: keyword note on the `_seo` texts and the English slug change.
- Section 3: the meta descriptions and slugs in seo.json are marked recommended in both languages (titles were already marked); the new English slug added.
- Section 8: the suggested English URL slug updated; headline, alternativeHeadline, description and keywords already match seo.json.
- Section 11: the JSON block equals seo.json.
- Section 12: the SEO checklist was missing from the report; added and marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | true-disciple-knowledge-into-action | what-makes-a-true-disciple |
| wordpress.en (focus_keyword, title, meta_description, secondary_keywords) | (as below) | unchanged (the `_seo` text now uses the focus keyword; title and meta already contain it) |
| wordpress.hi (slug, focus_keyword, title, meta_description) | (as below) | unchanged (the `_seo` text now uses the focus keyword) |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

No other talk uses the new slug or the focus keywords.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sachcha-shishya-kaun-hai | what-makes-a-true-disciple |
| focus_keyword | सच्चा शिष्य कौन है | what makes a true disciple |
| title | सच्चा शिष्य कौन है? जब ज्ञान कर्म बन जाए | What Makes a True Disciple? Turning Knowledge into Action |
| meta_description | सच्चा शिष्य कौन है? आचार्य उपेंद्र जी बताते हैं कि गुरु के शब्द कान से कृति और संस्कार तक कैसे पहुंचें, और क्यों वही ज्ञान सच्चा है जो कर्म बन जाए। | What makes a true disciple? Acharya Upendra Ji explains how the Guru's words travel from ear to conduct, and why real knowledge always ends in action. |
