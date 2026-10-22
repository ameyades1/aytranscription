without_guru_scriptures_can_mislead: SEO fix

Copies written: `without_guru_scriptures_can_mislead_blog_seo.txt` (Hindi) and `without_guru_scriptures_can_mislead_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| H2 1 "क्या किताब गुरु की जगह ले सकती है?", new first paragraph | (none) | क्या गुरु के बिना शास्त्र समझे जा सकते हैं? आचार्य जी की यह कथा बताती है: नहीं। शास्त्र संकेतों में बोलते हैं, और अक्षरशः पढ़ने पर वे अंधश्रद्धा तक ले जा सकते हैं। इसीलिए शास्त्र समझने के लिए गुरु चाहिए, और गुरु लेना प्रथम कर्तव्य है: पहले माँ, फिर पिता, फिर आचार्य। | The searched wording "गुरु के बिना शास्त्र" was missing from the body (section 2's mismatch note); neither focus keyword was in the first 100 words; the opening gave no direct answer. The answer (about 50 words) is built only from the blog's own sentences: "शास्त्र संकेतों में बोलते हैं", "अंधश्रद्धा", "शास्त्र समझने के लिए गुरु चाहिए ही चाहिए", "गुरु लेना प्रथम कर्तव्य है: पहले माँ, फिर पिता, फिर आचार्य" |
| H2 6 | शास्त्र संकेतों में बोलते हैं | गुरु के बिना शास्त्र क्यों समझ में नहीं आते? | The question readers search (section 4's suggestion); the section answers it: scriptures speak in signs that the Guru decodes |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| H2 1 "Can a Book Replace the Guru?", new first paragraph | (none) | Can you understand the scriptures without a Guru? This parable from Acharya Ji says no. Scriptures speak in signs, and read literally they can lead to blind faith. You need a Guru to understand them, and taking a Guru is your first duty: first your mother, then your father, then an acharya. | The focus keyword "scriptures without a Guru" was not in the first 100 words, and the opening gave no direct answer. The answer (about 50 words) is built only from the blog's own sentences ("Scriptures speak in signs", "blind faith", "you cannot understand the scriptures without a Guru", "Taking a Guru is your first duty: first your mother, then your father, then an acharya") |
| H2 6 | Scriptures Speak in Signs | Why Can't You Understand Scriptures Without a Guru? | The question readers search (section 4's suggestion); the section answers it |

The headings keep their number and order. No teaching, example, verse, verse translation or H1 was touched. All five `links` phrases and the `also_read` headings ("या दत्तात्रेय बनो, या जीवित गुरु लो" / "Be a Dattatreya, or Find a Living Guru") are still in the texts word for word, once each; the new paragraphs avoid the link phrases. The H2 that holds inline.jpg ("जब शब्दों को अक्षरशः पकड़ लिया जाए" / "When You Take the Words Literally") is unchanged.

## Checklist

Now met:
- Focus keyword within the first 100 words: both `_seo` texts have it in the direct answer under the first H2.
- Searched wording mismatch (section 2) resolved: the Hindi `_seo` text uses "गुरु के बिना शास्त्र", now the Hindi focus keyword.
- Direct answer early: a 40–60 word answer opens each blog.
- Question headings: H2 6 is now a natural search question in each language.

Still unmet: none. `python3 tools/check_seo.py without_guru_scriptures_can_mislead` passes.

Not changed:
- Authenticity flags 1–4 (sattvic doer definition, partial mantra, IAST notation, "गुरुदेव") are Sanskrit-review corrections for the editor; they touch teaching wording or verses, not SEO.
- "गुरु क्यों ज़रूरी है" is not added word for word: it stays a secondary keyword, to keep edits minimal and avoid stuffing.
- Section 7's cannibalization note still names the old Hindi focus; section 7 is outside what this fix may edit. The new focus "गुरु के बिना शास्त्र" is not used by any other talk.

## Report updates

- Section 2: keyword table marks "गुरु के बिना शास्त्र" as the Hindi focus; notes describe the `_seo` texts.
- Section 3: the recommended Hindi title, meta description and slug are the ones now in seo.json; the English ones are marked recommended (unchanged).
- Section 8: Hindi alternativeHeadline, description and keywords match seo.json; URL slugs added.
- Section 11: the same JSON as seo.json.
- Section 12: "Within the first 100 words" now met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | शास्त्र समझने के लिए गुरु क्यों ज़रूरी है | गुरु के बिना शास्त्र क्यों भटका सकते हैं (40 characters) |
| wordpress.hi.slug | shastra-samajhne-ke-liye-guru | guru-ke-bina-shastra |
| wordpress.hi.focus_keyword | शास्त्र समझने के लिए गुरु | गुरु के बिना शास्त्र |
| wordpress.hi.secondary_keywords | गुरु के बिना शास्त्र, जीवित गुरु, गुरु क्यों ज़रूरी है, सात्त्विक कर्ता | शास्त्र समझने के लिए गुरु, जीवित गुरु, गुरु क्यों ज़रूरी है, सात्त्विक कर्ता |
| wordpress.hi.meta_description | शास्त्र समझने के लिए गुरु क्यों ज़रूरी है? अक्षरशः … | गुरु के बिना शास्त्र क्यों भटका सकते हैं? अक्षरशः … (156 characters; the rest is unchanged) |
| English fields | (unchanged) | (unchanged; focus keyword already the searched wording, slug scriptures-without-a-guru kept) |
| links, also_read | (unchanged) | (unchanged; no edit touched a phrase or heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | guru-ke-bina-shastra | scriptures-without-a-guru |
| focus keyword | गुरु के बिना शास्त्र | scriptures without a Guru |
| title | गुरु के बिना शास्त्र क्यों भटका सकते हैं | Scriptures Without a Guru: Why Literal Reading Misleads |
| meta description | गुरु के बिना शास्त्र क्यों भटका सकते हैं? अक्षरशः पढ़े ग्रंथ से एक लड़के ने गाँव उल्टा कर दिया। आचार्य जी बताते हैं शास्त्र के संकेत और जीवित गुरु का महत्व। | Can you read scriptures without a Guru? Acharya Upendra Ji's parable of a boy who took them literally shows why a living Guru is your first duty. |
