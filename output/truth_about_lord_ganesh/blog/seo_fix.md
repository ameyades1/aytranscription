truth_about_lord_ganesh: SEO fix

Copies: `truth_about_lord_ganesh_blog_seo.txt` (Hindi) and `truth_about_lord_ganesh_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph | आचार्य उपेंद्र जी इस प्रवचन में गणेश जन्म की प्रसिद्ध कथा की परतें खोलते हैं | आचार्य उपेंद्र जी इस प्रवचन में प्रसिद्ध गणेश जन्म कथा की परतें खोलते हैं | Uses the searched wording "गणेश जन्म कथा" in the first 100 words (section 2 mismatch); same meaning, word order only |
| New paragraph after the opening | (none) | आचार्य जी की शिक्षा में असली गणेश ओंकार है, सर्वत्र व्याप्त परम सत्य, ब्रह्म वाला गणेश। मूलाधार से जुड़े गणेश हमारे भीतर की विवेक बुद्धि हैं, इंद्रियों का स्वामी बनने की बुद्धि। पार्वती का मैल, शिवजी का लौटना और हाथी का सिर, ये सब इसी विवेक के जन्म की कथा कहते हैं। | Direct answer (52 words) to the H1's question, built only from the section "दो गणेश: ओंकार और विवेक" and the opening; puts the new focus keyword "असली गणेश" in the first 100 words. It does not repeat the link phrase "वही असली, ब्रह्म वाला गणेश है", which still appears only once |
| H2 | ## पार्वती का मैल: क्या सच में? | ## पार्वती के मैल से गणेश का जन्म: इसका अर्थ क्या है? | Natural search question (section 4); the section answers it ("यह सब प्रतीक है" and the gunas reading) |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph | peels back the layers of the famous story of Ganesha's birth | peels back the layers of the famous Ganesha birth story | Uses the searched wording "Ganesha birth story" in the first 100 words (section 2 mismatch) |
| New paragraph after the opening | (none) | In Acharya Ji's teaching, the real Ganesha is Omkara, the ultimate reality that pervades everything, the Ganesha who is Brahman. The Ganesha linked to the Muladhara is the discernment within us, the intelligence that masters the senses. Parvati's bath, Lord Shiva's return and the elephant's head all tell how that discernment is born. | Direct answer (53 words) to "who is the real Ganesha", built only from "Two Ganeshas: Omkara and Discernment" and the opening; does not repeat the link phrase "the true Ganesha, the one who is Brahman" |
| H2 | ## Born from Parvati's Bathing Paste: Really? | ## Born from Parvati's Bathing Paste: What Does It Mean? | Natural search question (section 4); the section answers it |

Not changed: the H1s, all verses, translations and references, the heading "हाथी का सिर: विवेक के गुण" / "The Elephant's Head: The Marks of Discernment" (the Also read anchor), and all four link phrases in each language (each checked with grep: still present exactly once). The number and order of headings are unchanged. The Sanskrit review's corrections (for example "एक आँख" / "The single eye") are not part of this fix and are still open (report section 10).

## Checklist

Now met (added to section 12):
- One or two H2s phrased as natural search questions (one per language; the other candidate, "हाथी का सिर: विवेक के गुण", is the Also read anchor and stays as it is).
- A 40–60 word direct answer early in the post.
- The searched wording is in the body: "असली गणेश", "गणेश जन्म कथा" / "Ganesha birth story".

All earlier checklist items remain met. Unmet: none. `python3 tools/check_seo.py truth_about_lord_ganesh` passes.

The report is in step with seo.json: section 2's keyword notes, section 3 (the Hindi title, meta description and slug now in seo.json marked as recommended; English unchanged and marked), section 7's cannibalization note ("असली गणेश"), section 8's Hindi schema (alternativeHeadline, description, keywords, suggested slug), section 11 and section 12.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | कौन है वास्तविक गणेश? गणेश जन्म कथा का अर्थ | असली गणेश कौन है? गणेश जन्म कथा का अर्थ |
| wordpress.hi.focus_keyword | वास्तविक गणेश | असली गणेश |
| wordpress.hi.secondary_keywords | असली गणेश कौन है, गणेश जन्म कथा का रहस्य, पार्वती के मैल से गणेश का जन्म, गणेश और विवेक बुद्धि | वास्तविक गणेश, गणेश जन्म कथा का रहस्य, पार्वती के मैल से गणेश का जन्म, गणेश और विवेक बुद्धि |
| wordpress.hi.meta_description | कौन है वास्तविक गणेश? आचार्य उपेंद्र जी बताते हैं कि … (145 characters) | असली गणेश कौन है? आचार्य उपेंद्र जी बताते हैं कि … (141 characters; rest unchanged) |
| wordpress.hi.slug | kaun-hai-vastavik-ganesh | asli-ganesh-kaun-hai |
| wordpress.en.slug | who-is-the-real-ganesha | who-is-the-real-ganesha (unchanged; already built from the unchanged focus keyword) |
| wordpress.en (all fields) | unchanged | unchanged |
| links, also_read | unchanged | unchanged |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | asli-ganesh-kaun-hai | who-is-the-real-ganesha |
| focus_keyword | असली गणेश | who is the real Ganesha |
| title | असली गणेश कौन है? गणेश जन्म कथा का अर्थ | Who Is the Real Ganesha? The Meaning of His Birth Story |
| meta_description | असली गणेश कौन है? आचार्य उपेंद्र जी बताते हैं कि पार्वती का मैल, शिवजी का लौटना और हाथी का सिर हमारे भीतर विवेक बुद्धि के जन्म के प्रतीक हैं। | Who is the real Ganesha? Acharya Upendra Ji decodes the birth story: Parvati's bath, Shiva's return and the elephant head as discernment born within us. |
