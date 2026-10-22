when_love_turns_into_control: SEO fix

Copies written: `when_love_turns_into_control_blog_seo.txt` (Hindi) and `when_love_turns_into_control_blog_seo_en.txt` (English). The original blog texts are unchanged.

The report had one unmet checklist item: "No unsupported scriptural claims", because the body said "the scriptures say" that a mother who expects is no longer a good mother, with no source (Sanskrit review issue 1, Major; authenticity flag 1). Section 2 also noted a mismatch: people search "प्रेम में अपेक्षा" / "when love turns into control", but the body only said "प्रेम धीरे-धीरे नियंत्रण ... में बदलने लगता है" / "love slowly begins to turn into control". Each language gets three changes: the searched wording once in the second paragraph (within the first 100 words), the section on expectation headed with the question section 4 recommended, and the review's correction for issue 1. The focus keywords move to the searched wording.

## Hindi (`when_love_turns_into_control_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, paragraph 2 | …समझाते हैं कि बिना हिसाब का प्रेम क्या है, और क्यों वही सबसे ऊँची आध्यात्मिक स्थिति है। | …समझाते हैं कि बिना हिसाब का प्रेम क्या है, क्यों वही सबसे ऊँची आध्यात्मिक स्थिति है, और प्रेम में अपेक्षा आते ही क्या होता है। | Searched wording "प्रेम में अपेक्षा" (section 2) in the first 100 words; the talk covers exactly this in "जब अपेक्षा आती है" |
| H2 5 | जब अपेक्षा आती है | प्रेम नियंत्रण कब बन जाता है? | The question readers search, as recommended in report section 4; the section answers it ("यहीं वह बारीक रेखा है जहाँ प्रेम नियंत्रण में बदलने लगता है") |
| Same section, paragraph 1 | पर शास्त्र कहता है कि जिस दिन माँ अपेक्षा करने लगे… | पर आचार्य जी कहते हैं कि जिस दिन माँ अपेक्षा करने लगे… | Checklist "No unsupported scriptural claims": the Sanskrit review's correction for issue 1 (no scripture says this; it is Acharya Ji's teaching) |

## English (`when_love_turns_into_control_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, paragraph 2 | …what love without accounting looks like, and why it is the highest spiritual state of all. | …what love without accounting looks like, why it is the highest spiritual state of all, and when love turns into control. | Searched wording "when love turns into control" (the video title, section 2) in the first 100 words; the talk answers it in the section on expectation |
| H2 5 | When Expectation Creeps In | When Does Love Turn Into Control? | The question readers search, as recommended in report section 4; the section answers it ("This is the fine line where love begins to turn into control") |
| Same section, paragraph 1 | Yet the scriptures say that the day a mother starts expecting… | Yet Acharya Ji says that the day a mother starts expecting… | Checklist "No unsupported scriptural claims": the Sanskrit review's correction for issue 1 |

The headings keep their number and order. No teaching, example, verse or H1 was touched. All five `links` phrases and the `also_read` headings ("कॉलेज की वह लड़की जो बदल गई" / "The College Friend Who Changed Overnight") are still in the texts word for word.

## Checklist

- Now met: "No unsupported scriptural claims". Review issue 1 (Major) is corrected with the review's wording in both languages.
- Improved: the focus keyword is now the searched wording in both languages, in the first 100 words and echoed by a question H2. This settles the mismatch noted in section 2.
- Already met and still met: every other item in section 12. `python3 tools/check_seo.py when_love_turns_into_control` passes.

Still unmet: none.

Not changed:
- **Direct answer.** The first paragraph already answers the main question ("जिस क्षण यह हिसाब शुरू होता है, प्रेम धीरे-धीरे नियंत्रण और अपेक्षा में बदलने लगता है" / "The moment that ledger opens, love slowly begins to turn into control and expectation"), so no extra paragraph was added.
- **"love without expectation", "selfless love" / "निःस्वार्थ प्रेम"** stay secondary keywords; adding them would mean new wording in several places.
- **Authenticity flags 2–5** (the partial मातृदेवो भव quote, the reason a mother is called divine, the repeated sentence, formatting parity) concern verses or content, not SEO, and stay with the editor.

## Report updates

- Section 2: the keyword table and mismatch note now give the searched wordings as the focus keywords, used in the `_seo` texts.
- Section 3: the recommended titles, meta descriptions and slugs are now the ones in seo.json.
- Section 8: alternativeHeadline, description and keywords updated in both blocks; the `{{HI_URL}}` / `{{EN_URL}}` placeholders are now post URLs built from the new slugs (`{{SITE_URL}}/hi/prem-mein-apeksha/`, `{{SITE_URL}}/en/when-love-turns-into-control/`).
- Section 11: replaced with the new seo.json.
- Section 12: "No unsupported scriptural claims" is now marked met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | बिना हिसाब का प्रेम: माँ का बिल हमेशा शून्य क्यों होता है | प्रेम में अपेक्षा: माँ का बिल हमेशा शून्य क्यों होता है |
| title.en | Love Without Accounting: Why a Mother's Bill Comes to Zero | When Love Turns Into Control: A Mother's Bill of Zeros |
| wordpress.hi.focus_keyword | बिना हिसाब का प्रेम | प्रेम में अपेक्षा |
| wordpress.hi.secondary_keywords | प्रेम में अपेक्षा, निःस्वार्थ प्रेम, माँ का प्रेम, मातृभाव | बिना हिसाब का प्रेम, निःस्वार्थ प्रेम, माँ का प्रेम, मातृभाव |
| wordpress.hi.slug | bina-hisab-ka-prem | prem-mein-apeksha |
| wordpress.hi.meta_description | प्रेम कब नियंत्रण बन जाता है? आचार्य उपेंद्र जी माँ के शून्य बिल की कथा से समझाते हैं बिना हिसाब का प्रेम, मातृभाव और अपेक्षा-रहित देने की सर्वोच्च स्थिति। | प्रेम में अपेक्षा आते ही वह नियंत्रण बनने लगता है। आचार्य उपेंद्र जी माँ के शून्य बिल की कथा से समझाते हैं बिना हिसाब का प्रेम और मातृभाव की सर्वोच्च स्थिति। |
| wordpress.en.focus_keyword | love without accounting | when love turns into control |
| wordpress.en.secondary_keywords | when love turns into control, love without expectation, mother's love, selfless love | love without accounting, love without expectation, mother's love, selfless love |
| wordpress.en.slug | love-without-accounting | when-love-turns-into-control |
| wordpress.en.meta_description | When does love turn into control? Acharya Upendra Ji uses a mother's bill of zeros to explain love without accounting, the highest spiritual state. | When love turns into control, expectation has crept in. Acharya Upendra Ji uses a mother's bill of zeros to show what love without accounting is. |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

Both new focus keywords and slugs are unique across all talks. `love_burden_for_child_parenting` (the neighbour named in section 7) keeps "बच्चों पर अपेक्षाओं का बोझ" / "parental pressure on children".

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | prem-mein-apeksha | when-love-turns-into-control |
| focus_keyword | प्रेम में अपेक्षा | when love turns into control |
| title | प्रेम में अपेक्षा: माँ का बिल हमेशा शून्य क्यों होता है | When Love Turns Into Control: A Mother's Bill of Zeros |
| meta_description | प्रेम में अपेक्षा आते ही वह नियंत्रण बनने लगता है। आचार्य उपेंद्र जी माँ के शून्य बिल की कथा से समझाते हैं बिना हिसाब का प्रेम और मातृभाव की सर्वोच्च स्थिति। | When love turns into control, expectation has crept in. Acharya Upendra Ji uses a mother's bill of zeros to show what love without accounting is. |
