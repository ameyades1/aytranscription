eat_shapes_how_you_think: SEO fix

Copies written: `eat_shapes_how_you_think_blog_seo.txt` (Hindi) and `eat_shapes_how_you_think_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening principle | (none) | स्थानीय भोजन का महत्व क्या है? आचार्य जी के अनुसार जिस भूमि पर आपका जन्म हुआ, वहाँ उगा अन्न ही आपके लिए बना है। वह मिट्टी और उसका पृथ्वी तत्व आपके कर्म और प्रारब्ध से जुड़े हैं, और जो गुण हम खाते हैं, वे हमारे भीतर आते हैं। विदेशी भोजन कभी-कभार ठीक है, पर आधार अपना स्थानीय भोजन रहे। | The focus keyword was not in the body at all (check_seo failed) nor in the first 100 words, and there was no early direct answer. Built only from the blog's own points (sections 2–4 and the takeaways); 59 words. |
| H2 2 | मिट्टी, पृथ्वी तत्व और प्रारब्ध | जन्मभूमि का अन्न ही क्यों खाएँ? | A question readers ask (report section 4); the section answers it (the land of birth, its soil and earth element are tied to karma and prarabdha). |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening principle | (none) | Why eat locally grown food? According to Acharya Ji, food grown on the land of your birth is meant for you. That soil and its earth element are tied to your karma and prarabdha, and the qualities of what you eat become yours. Foreign cuisine is fine as an occasional treat, but local food should remain the foundation. | The focus keyword "why eat locally grown food" was not in the body (only "locally grown food" in the takeaways; check_seo failed) nor in the first 100 words, and there was no early direct answer. Built only from the blog's own points; 58 words. |
| H2 2 | The Soil, the Earth Element and Destiny | Why Eat the Food of Your Birthplace? | A question readers ask (report section 4); the section answers it. |

The headings keep their number and order. No teaching, example, quote or H1 was touched (the blog has no verses). The new paragraphs avoid the exact `links` phrases, so each link still lands on its original sentence. All four `links` phrases per language are still in the texts word for word; the `also_read` headings were changed with H2 2 and copied exactly into seo.json. The inline image is still placed: images.txt's Hindi heading is in the original Hindi text, and the section count is unchanged.

## Checklist

Now met:
- Focus keyword in the body text (both languages; was failing check_seo).
- Focus keyword within the first 100 words (both languages).
- Early direct answer (40–60 words) in both languages.

Still unmet (1):
- Each tag can be shared by at least 3 posts: "स्थानीय भोजन" / "Local Food" is used only by this post and "पंचतत्व" / "Five Elements" by 2. Tags are not part of the blog text, so this fix leaves them to the editor.

`python3 tools/check_seo.py eat_shapes_how_you_think` passes.

Not changed:
- Authenticity flags 1–5 (section 10) need no text change; the new paragraphs add no mind, brain, medical or scriptural claim.

## Report updates

- Section 2: added a keyword note (no searched-wording mismatch; the `_seo` texts now use both focus keywords).
- Section 3: the recommended titles, meta descriptions and slugs already match seo.json (unchanged).
- Section 7: the Also read line names the new headings.
- Section 8: headline, alternativeHeadline, description, keywords and suggested slugs already match seo.json (unchanged).
- Section 11: replaced with the new seo.json.
- Section 12: added the SEO checklist (it was missing), marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| also_read.after.hi | मिट्टी, पृथ्वी तत्व और प्रारब्ध | जन्मभूमि का अन्न ही क्यों खाएँ? |
| also_read.after.en | The Soil, the Earth Element and Destiny | Why Eat the Food of Your Birthplace? |
| wordpress.hi.slug | sthaniya-bhojan-ka-mahatva | unchanged |
| wordpress.en.slug | why-eat-locally-grown-food | unchanged |
| focus_keyword, secondary_keywords, title, meta_description | (both languages) | unchanged (they already contain the focus keyword, which the `_seo` texts now use) |
| links | (unchanged) | (unchanged; no edit touched a link phrase) |

No other talk uses either focus keyword or slug.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sthaniya-bhojan-ka-mahatva | why-eat-locally-grown-food |
| focus keyword | स्थानीय भोजन का महत्व | why eat locally grown food |
| title | स्थानीय भोजन का महत्व: जहाँ जन्म, वहीं का अन्न | Why Eat Locally Grown Food? Karma, Soil and Your Plate |
| meta description | जहाँ जन्म, वहीं का अन्न। आचार्य उपेंद्र जी बताते हैं स्थानीय भोजन का महत्व, जन्मभूमि की मिट्टी का कर्म और प्रारब्ध से संबंध, और विदेशी भोजन कब ठीक है। | Why eat locally grown food? Acharya Upendra Ji links the soil of your birthplace to karma and prarabdha, and explains why foreign food should stay a treat. |
