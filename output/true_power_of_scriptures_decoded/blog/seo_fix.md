true_power_of_scriptures_decoded: SEO fix

Copies written: `true_power_of_scriptures_decoded_blog_seo.txt` (Hindi) and `true_power_of_scriptures_decoded_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph | हम "शास्त्र" शब्द बहुत सुनते हैं, पर इसका अर्थ क्या है? | हम "शास्त्र" शब्द बहुत सुनते हैं, पर शास्त्र का अर्थ क्या है? | The focus keyword "शास्त्र का अर्थ" appeared only in the key takeaways; now it is in the first 100 words |
| New paragraph after the opening | (none) | आचार्य जी के अनुसार शास्त्र वह ग्रंथ है जिसमें कर्तव्य और अकर्तव्य, यानी क्या करें और क्या न करें, का विधान होता है। उसे कोई भी नहीं लिख सकता, बल्कि उस विषय का अनुभवी अधिकारी लिखता है। इसलिए धर्म, अर्थ, काम और मोक्ष, हर पुरुषार्थ और हर विद्या का अपना शास्त्र है। | Direct answer early (report sections 4 and 5), about 55 words, built only from the blog's own sections (definition, author, the four purusharthas and every science), attributed to Acharya Ji |
| H2 2 | लिखता कौन है? | शास्त्र कौन लिखता है? | A full question readers search (secondary keyword "शास्त्र कौन लिखता है", report section 4); the section answers it |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph | but what does it actually mean? | but what is the actual meaning of shastra? | The focus keyword "meaning of shastra" was only in the H1, which SureRank does not count; now it is in the first 100 words |
| New paragraph after the opening | (none) | According to Acharya Ji, a shastra is a text that sets out what to do and what not to do in a field. It is written not by anyone with an opinion but by an authority with real mastery and experience. That is why dharma, artha, kama, moksha and every science have their own shastra. | Direct answer early (report sections 4 and 5), 52 words, built only from what the blog says, attributed to Acharya Ji |
| H2 2 | Who Writes It? | Who Writes a Shastra? | A question that stands on its own in search (report section 4); the section answers it |

The headings keep their number and order. No teaching, example, verse, translation, reference or H1 was touched. The Sanskrit review's corrections (Gita 17.20 half verse, Vatsyayana's statement, the seven-fold artha list, sandhi and IAST) change verses or content and are left for the editor. All five `links` phrases and the `also_read` headings ("अर्थशास्त्र: समृद्धि, धर्म के लिए" / "Artha Shastra: Prosperity in the Service of Dharma") are still in the texts word for word, once each. The inline image's Hindi heading in images.txt is unchanged.

## Checklist

Now met:
- Focus keyword in the meta description (both languages): failed `check_seo.py` before.
- Focus keyword within the first 100 words (both languages): in the opening paragraph.
- Direct answer early: added in both languages.
- Question headings: the second H2 in each language is now a full, searchable question.
- SEO checklist (section 12) was missing from the report; added and marked for the `_seo` texts.

Still unmet (2):
- Each tag can be shared by at least 3 posts: "Shastra" / "शास्त्र" and "Dana" / "दान" are used by no other post yet. A tag choice, not something the blog text can fix.
- No unsupported scriptural claims: Gita 17.20 quoted as a half verse, Vatsyayana's "lifelong" celibacy and moksha as his stated aim, and the seven-fold artha list (Sanskrit review issues 1, 2 and 5; report flags 1–3). These are content corrections for the editor, not SEO fixes; they were left untouched.

`python3 tools/check_seo.py true_power_of_scriptures_decoded` passes. `tools/rebuild_blogs.sh true_power_of_scriptures_decoded` rebuilt 12 pages with no "Note:" lines.

## Report updates

- Section 2: keyword note added describing the `_seo` texts.
- Section 3: the new meta descriptions (with character counts) and the slugs are marked recommended; the titles were already marked.
- Section 8: description of both BlogPostings matches the new meta descriptions; headline, alternativeHeadline, keywords and slugs were already current.
- Section 11: the JSON block equals seo.json.
- Section 12: the SEO checklist added and marked.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | शास्त्र का असली अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि शास्त्र अनुभवी अधिकारी का बताया कर्तव्य-अकर्तव्य है, और धर्म, अर्थ, काम, मोक्ष, सबका शास्त्र है। | शास्त्र का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि शास्त्र अनुभवी अधिकारी का बताया कर्तव्य-अकर्तव्य है, और धर्म, अर्थ, काम, मोक्ष, सबका शास्त्र है। (152 characters) |
| wordpress.en.meta_description | What does shastra mean? Acharya Upendra Ji explains it as the do's and don'ts set by a true authority, from Dharma Shastra and dana to Artha and Kama. | What is the meaning of shastra? Acharya Upendra Ji explains it as the do's and don'ts set by a true authority, from Dharma Shastra to Artha and Kama. (149 characters) |
| wordpress.hi.slug | shastra-ka-arth | unchanged |
| wordpress.en.slug | meaning-of-shastra | unchanged |
| focus_keyword (hi, en) | शास्त्र का अर्थ / meaning of shastra | unchanged (the `_seo` texts now use them in the opening) |
| title (hi, en) | (unchanged) | unchanged (already contain the focus keyword) |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | shastra-ka-arth | meaning-of-shastra |
| focus_keyword | शास्त्र का अर्थ | meaning of shastra |
| title | शास्त्र का अर्थ: धर्म, अर्थ, काम, मोक्ष के नियम | Meaning of Shastra: Dharma, Artha, Kama and Moksha |
| meta_description | शास्त्र का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि शास्त्र अनुभवी अधिकारी का बताया कर्तव्य-अकर्तव्य है, और धर्म, अर्थ, काम, मोक्ष, सबका शास्त्र है। | What is the meaning of shastra? Acharya Upendra Ji explains it as the do's and don'ts set by a true authority, from Dharma Shastra to Artha and Kama. |
