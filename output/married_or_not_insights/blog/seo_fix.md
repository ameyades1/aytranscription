married_or_not_insights: SEO fix

The fixed texts are `married_or_not_insights_blog_seo.txt` (Hindi) and `married_or_not_insights_blog_seo_en.txt` (English). The original blog texts are unchanged. No teaching, example, verse, translation, reference or H1 was changed, and the Sanskrit review's corrections (tools/review/married_or_not_insights.md) were left for the editor, as they are not SEO fixes.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph, first sentence | क्या पतिव्रता होने का अर्थ है चुपचाप सब कुछ सहते जाना? | क्या पतिव्रता का अर्थ है चुपचाप सब कुछ सहते जाना? | Focus keyword "पतिव्रता का अर्थ" was not in the body word for word (SureRank error); now in the first sentence, same question |
| New paragraph after "उत्तर कोमल भी है और स्पष्ट भी।" | (none) | संक्षेप में उत्तर है: नहीं। शास्त्रों में पतिव्रता को देवी का स्वरूप कहा गया है, जिसके भीतर तेज होता है। इसलिए उसे अपनी बात मधुर स्वर में रखनी, आत्मविश्वास से "ना" कहना और अपनी रुचि व कर्तव्य, दोनों निभाने आने चाहिए। अत्याचार वह कभी सहन नहीं करती। | No direct answer early; this 40–60 word answer uses only what the blog already says (देवी का स्वरूप, तेज, मधुर स्वर, आत्मविश्वास से ना, रुचि और कर्तव्य, अत्याचार सहन नहीं) |
| `##` heading of the Kanyadaan section | कन्यादान के बाद का घर | शादी के बाद मायके से कितनी बात करें? | Heading as the natural question readers search for (secondary keyword); the section answers exactly this |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after "His answer is gentle, and it is also clear." | (none) | The short answer is no. Here is the pativrata meaning the scriptures give: she is a form of the Devi who carries tej. So she speaks up for herself, says "no" with confidence and courtesy, fulfils both her interests and her duties, and never tolerates abuse. | Focus keyword "pativrata meaning" was not in the body (SureRank error) and there was no direct answer early; built only from the blog's own points, and within the first 100 words |
| `##` heading of the Kanyadaan section | Home After Kanyadaan | How Often Should a Married Daughter Call Home? | Heading as the natural question readers search for ("married daughter calling parents too often"); the section answers exactly this |

## Checklist

Now met:
- Focus keyword in the body text (Hindi and English): was failing in `check_seo.py`.
- Focus keyword in the meta description (English): was failing in `check_seo.py`.
- Focus keyword within the first 100 words (both languages).
- Focus keyword taken from wording the article uses (the `_seo` texts now use it word for word).
- Direct answer paragraph early (both languages), and one heading phrased as a reader's question in each language.

Still unmet: none. The report had no section 12 yet; it was added with every item marked met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | Does being a pativrata mean silently enduring everything? Acharya Upendra Ji explains why a devoted wife lives with tej, speaks up and refuses abuse. | What is the true pativrata meaning? Acharya Upendra Ji explains why a devoted wife lives with tej, not silent endurance: she speaks up and refuses abuse. |
| wordpress.hi.slug | pativrata-ka-arth | pativrata-ka-arth (unchanged) |
| wordpress.en.slug | pativrata-meaning | pativrata-meaning (unchanged) |

Focus keywords, titles, secondary keywords, the Hindi meta description, `links` and `also_read` are unchanged: the searched wording is already the focus keyword in both languages, and no edit touched a link phrase or the "Also read" heading. The report's sections 2, 3, 8, 11 and 12 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | pativrata-ka-arth | pativrata-meaning |
| focus_keyword | पतिव्रता का अर्थ | pativrata meaning |
| title | पतिव्रता का अर्थ: दबना नहीं, तेज से जीना \| आचार्य उपेंद्र जी | Pativrata Meaning: Living with Radiance, Not Submission |
| meta_description | क्या पतिव्रता का अर्थ चुपचाप सब सहना है? आचार्य उपेंद्र जी बताते हैं कि पतिव्रता दबकर नहीं, तेज से जीती है, विनम्रता से ना कहती है और अन्याय कभी नहीं सहती। | What is the true pativrata meaning? Acharya Upendra Ji explains why a devoted wife lives with tej, not silent endurance: she speaks up and refuses abuse. |

Hindi title exactly as in seo.json (the table above escapes its pipe): `पतिव्रता का अर्थ: दबना नहीं, तेज से जीना | आचार्य उपेंद्र जी`
