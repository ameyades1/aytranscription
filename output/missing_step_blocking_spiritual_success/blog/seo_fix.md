missing_step_blocking_spiritual_success: SEO fix

The fixed texts are `missing_step_blocking_spiritual_success_blog_seo.txt` (Hindi) and `missing_step_blocking_spiritual_success_blog_seo_en.txt` (English). The original blog texts are unchanged. No teaching, example, verse, translation, reference or H1 was changed, and the Sanskrit review's corrections (tools/review/missing_step_blocking_spiritual_success.md) were left for the editor, as they are not SEO fixes. The heading that places inline.jpg ("निदिध्यासन: वह सीढ़ी जो अक्सर छूट जाती है" / "Nididhyasana: The Step People Most Often Skip") was not touched.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after "और अक्सर हम इनमें से किसी एक को अधूरा छोड़कर अगली पर कूद जाते हैं।" | (none) | संक्षेप में, श्रवण मनन निदिध्यासन साधना की तीन सीढ़ियाँ हैं। श्रवण तब पूरा होता है जब आप गुरु की बात बिंदुवार दोहरा सकें; मनन तब, जब कोई संदेह शेष न रहे; और निदिध्यासन विश्वास को अनुभव में बदलता है, जिसके लिए तपस्या और योग्यता चाहिए। किसी एक सीढ़ी को अधूरा छोड़ें, तो साधना रुक जाती है। | The focus keyword "श्रवण मनन निदिध्यासन" was not in the body, because the body only writes "श्रवण, मनन और निदिध्यासन" (SureRank error); now at word 62. Also the direct answer early (about 55 words), built only from the blog's own points (Key Takeaways and the H1) |
| `##` heading of the second section | क्या आपने सच में सुना है? | श्रवण कब पूरा होता है? | Heading as the natural question readers search for (report section 4); the section asks and answers it in its own words |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after "Too often we leave one of them half done and leap ahead to the next." | (none) | In short, shravana manana nididhyasana is the three-step sequence of sadhana. Shravana (listening) is complete when you can repeat the Guru's teaching point by point; manana (reflection) is complete when no doubt remains; and nididhyasana turns belief into experience, which demands tapasya and qualification. Leave any one step half done, and your sadhana is held back. | The focus keyword "shravana manana nididhyasana" was not in the body, because SureRank does not match across the commas in "shravana, manana and nididhyasana" (SureRank error); now at word 74. Also the direct answer early (about 55 words), built only from the blog's own points (Key Takeaways and the H1) |
| `##` heading of the second section | Have You Truly Heard? | When Is Shravana Complete? | Heading as the natural question readers search for (report section 4); the section asks and answers "when is listening complete?" |

## Checklist

Now met:
- Focus keyword in the title tag, meta description and body text (both languages): all six were failing in `check_seo.py` because of the commas in "श्रवण, मनन, निदिध्यासन" / "shravana, manana and nididhyasana".
- Focus keyword taken from wording the article uses (the `_seo` texts now use it word for word), and within the first 100 words.
- The searched wording versus the body's wording is flagged in section 2's keyword note.
- Direct answer paragraph early, and one heading phrased as a reader's question, in each language.

Still unmet (2):
- Each tag can be shared by at least 3 posts: "Tapasya" / "तपस्या" is used by no other post yet; tags are outside the SEO fix.
- No unsupported scriptural claims: the body still says the scriptures prescribe seven or eleven parayanas (Sanskrit review item 3); left for the editor, as it is not an SEO fix.

The report had no section 12 yet; it was added with these marks.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | श्रवण, मनन, निदिध्यासन: साधना की छूटी हुई सीढ़ी | श्रवण मनन निदिध्यासन: साधना की छूटी हुई सीढ़ी |
| title.en | Shravana, Manana, Nididhyasana: The Missing Step in Sadhana | Shravana Manana Nididhyasana: The Missing Step in Sadhana |
| wordpress.hi.meta_description | प्रवचन सुने, ग्रंथ पढ़े, फिर भी भीतर कुछ क्यों नहीं बदलता? आचार्य उपेंद्र जी श्रवण, मनन और निदिध्यासन का क्रम और सच्ची अनुभूति की तीन कसौटियाँ बताते हैं। | प्रवचन सुने, ग्रंथ पढ़े, फिर भी भीतर कुछ क्यों नहीं बदलता? आचार्य उपेंद्र जी श्रवण मनन निदिध्यासन का क्रम और सच्ची अनुभूति की तीन कसौटियाँ बताते हैं। |
| wordpress.en.meta_description | Why does sadhana not change you? Acharya Upendra Ji explains shravana, manana and nididhyasana, and three tests to know if an experience is real. | Why does sadhana not change you? Acharya Upendra Ji explains the shravana manana nididhyasana sequence and three tests to know if an experience is real. |
| wordpress.hi.focus_keyword | श्रवण मनन निदिध्यासन | श्रवण मनन निदिध्यासन (unchanged; it is the searched wording) |
| wordpress.en.focus_keyword | shravana manana nididhyasana | shravana manana nididhyasana (unchanged; it is the searched wording) |
| wordpress.hi.slug | shravan-manan-nididhyasan | shravan-manan-nididhyasan (unchanged) |
| wordpress.en.slug | shravana-manana-nididhyasana | shravana-manana-nididhyasana (unchanged; already built from the focus keyword, 28 characters) |

Secondary keywords, `links` and `also_read` are unchanged: no edit touched a link phrase or the "Also read" heading. The report's sections 2, 3, 8, 11 and 12 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | shravan-manan-nididhyasan | shravana-manana-nididhyasana |
| focus_keyword | श्रवण मनन निदिध्यासन | shravana manana nididhyasana |
| title | श्रवण मनन निदिध्यासन: साधना की छूटी हुई सीढ़ी | Shravana Manana Nididhyasana: The Missing Step in Sadhana |
| meta_description | प्रवचन सुने, ग्रंथ पढ़े, फिर भी भीतर कुछ क्यों नहीं बदलता? आचार्य उपेंद्र जी श्रवण मनन निदिध्यासन का क्रम और सच्ची अनुभूति की तीन कसौटियाँ बताते हैं। | Why does sadhana not change you? Acharya Upendra Ji explains the shravana manana nididhyasana sequence and three tests to know if an experience is real. |
