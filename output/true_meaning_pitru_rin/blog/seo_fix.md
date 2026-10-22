true_meaning_pitru_rin: SEO fix

Copies written: `true_meaning_pitru_rin_blog_seo.txt` (Hindi) and `true_meaning_pitru_rin_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro | (none) | पितृ ऋण का अर्थ क्या है? आचार्य जी के अनुसार माता-पिता ने हमारे लिए जो त्याग किया, उसका ऋण उनके जीते जी चुकाया जाता है: उनके साथ समय बिताकर, उनकी लाठी ही नहीं, उनका आनंद भी बनकर। उनके जाने के बाद किया गया श्राद्ध भी गलत नहीं, बशर्ते वह दिखावे या डर से न हो। | The focus keyword "पितृ ऋण का अर्थ" was not in the body (`check_seo.py` failed), "पितृ ऋण" first appeared only in the sixth section, and the opening gave no direct answer. The 55-word answer uses only what the blog says (sections "देर से जागे तो भी सवेरा है" and "लाठी ही नहीं, आनंद भी बनो"), attributed to Acharya Ji |
| H2 6 | लाठी ही नहीं, आनंद भी बनो | पितृ ऋण कैसे चुकाएं? लाठी ही नहीं, आनंद भी बनो | A question readers search (secondary keyword "पितृ ऋण कैसे चुकाएं"); the section answers it ("यही पितृ ऋण है, और इसे चुकाने के लिए...") |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro | (none) | What is pitru rin? In Acharya Ji's teaching, it is the debt we owe our parents for all they gave up for us. We repay it while they are alive, by spending time with them and being their joy, not just their walking stick. Shraddha performed later is not wrong, if it is not for show or out of fear. | The focus keyword "pitru rin meaning" was not in the body (`check_seo.py` failed), "pitru rin" first appeared only in the sixth section, and the opening gave no direct answer. The 60-word answer uses only what the blog says, attributed to Acharya Ji; it carries the new focus keyword "what is pitru rin" within the first 100 words |
| H2 6 | Be Their Joy, Not Just Their Support | How Do We Repay Pitru Rin? Be Their Joy, Not Just Their Support | A question readers search (secondary keyword "how to repay pitru rin"); the section answers it ("This is pitru rin ..., and to repay it ...") |

The headings keep their number and order. No teaching, example, verse, translation, reference or H1 was touched. The traditional "three debts" meaning (Sanskrit review issue 6) was not added, because the blog does not contain it; the direct answers say "according to Acharya Ji" instead. All four `links` phrases and the `also_read` headings ("जिस घर में श्राद्ध की ज़रूरत ही न पड़े" / "A Home That Never Needs Shraddha") are still in the texts word for word, once each. The inline image's Hindi heading in images.txt is in the original text, so the image is placed by section position.

## Checklist

Now met:
- Focus keyword in the title tag (Hindi), the meta description and the body text (both languages): all failed `check_seo.py` before.
- Focus keyword taken from wording the article uses: now true of the `_seo` texts.
- Focus keyword within the first 100 words: both languages, in the direct-answer paragraph.
- Direct answer early (report section 5): added in both languages.
- Question headings: one more H2 per language is now a natural question.

Still unmet (2):
- No unsupported scriptural claims: "शास्त्र कहता है" / "the scriptures say" for the shraddha exemption, "pitar yoni" and ancestors "forever free" (Sanskrit review issues 1, 2 and 8, report flags 1, 2 and 5), and the Hindi "यह तभी होता है" sentence (issue 3). These are content corrections for the editor, not SEO fixes; they were left untouched.
- No broad labels that only restate a category: the tags "Ancestors" / "पितर" and "Shraddha" / "श्राद्ध" restate the category "Ancestors & Shraddha" / "पितृ और श्राद्ध". A tag choice, not something the blog text can fix.

`python3 tools/check_seo.py true_meaning_pitru_rin` passes. `tools/rebuild_blogs.sh true_meaning_pitru_rin` rebuilt 11 pages with no "Note:" lines.

## Report updates

- Section 2: English focus marked as "what is pitru rin", "pitru rin meaning" now a secondary row; keyword note added describing the `_seo` texts.
- Section 3: the titles, meta descriptions and slugs in seo.json are marked recommended (new Hindi title and meta, new English title, meta and slug).
- Section 8: alternativeHeadline and description of both BlogPostings match seo.json; English keywords and the suggested English URL slug updated.
- Section 11: the JSON block equals seo.json.
- Section 12: the SEO checklist was missing from the report; added and marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | पितृ ऋण का सच्चा अर्थ: श्राद्ध से पहले माता-पिता की सेवा | पितृ ऋण का अर्थ: श्राद्ध से पहले माता-पिता की सेवा (50 characters) |
| title.en | Pitru Rin Meaning: Serve Your Parents While They Are Alive | What Is Pitru Rin? Serve Your Parents While They Are Alive (58 characters) |
| wordpress.hi.meta_description | पितृ ऋण का सच्चा अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि जीते जी माता-पिता को समय और आनंद देना ही पितृ ऋण चुकाना है, और श्राद्ध दिखावे या डर से क्यों न हो। | पितृ ऋण का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि जीते जी माता-पिता को समय और आनंद देना ही पितृ ऋण चुकाना है, और श्राद्ध दिखावे या डर से क्यों न हो। (154 characters) |
| wordpress.en.meta_description | What does pitru rin truly mean? Acharya Upendra Ji explains why we repay the debt to our parents by serving them and giving them joy while they live. | What is pitru rin? Acharya Upendra Ji explains why we repay the debt to our parents by serving them and giving them joy while they are alive. (141 characters) |
| wordpress.en.focus_keyword | pitru rin meaning | what is pitru rin |
| wordpress.en.secondary_keywords | how to repay pitru rin, serving parents while they are alive, matru devo bhava meaning, shraddha after neglecting parents | pitru rin meaning, how to repay pitru rin, serving parents while they are alive, shraddha after neglecting parents |
| wordpress.en.slug | pitru-rin-meaning | what-is-pitru-rin |
| wordpress.hi.slug | pitru-rin-ka-sachcha-arth | unchanged |
| wordpress.hi.focus_keyword | पितृ ऋण का अर्थ | unchanged (the `_seo` text now uses it) |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | pitru-rin-ka-sachcha-arth | what-is-pitru-rin |
| focus_keyword | पितृ ऋण का अर्थ | what is pitru rin |
| title | पितृ ऋण का अर्थ: श्राद्ध से पहले माता-पिता की सेवा | What Is Pitru Rin? Serve Your Parents While They Are Alive |
| meta_description | पितृ ऋण का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि जीते जी माता-पिता को समय और आनंद देना ही पितृ ऋण चुकाना है, और श्राद्ध दिखावे या डर से क्यों न हो। | What is pitru rin? Acharya Upendra Ji explains why we repay the debt to our parents by serving them and giving them joy while they are alive. |
