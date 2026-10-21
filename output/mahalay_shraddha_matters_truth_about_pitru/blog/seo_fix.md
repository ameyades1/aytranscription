mahalay_shraddha_matters_truth_about_pitru: SEO fix

The report's focus keywords "महालय श्राद्ध क्या है" and "Mahalaya Shraddha meaning" were in the titles and slugs but missing from the blog bodies, and the English one was also missing from the English meta description (check_seo failed on all three). Neither opening gave a direct answer to the main question. Each `_seo` text now gets the report's section 5 direct answer after the intro, opening with the focus keyword word for word, so the keyword is in the body and in the first 100 words (Hindi: from word 75; English: from word 88). One heading per language becomes the "difference" question suggested in report section 4.

## Hindi changes (`mahalay_shraddha_matters_truth_about_pitru_blog_seo.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro, before the first H2 | (none) | महालय श्राद्ध क्या है? यह पितृ पक्ष के पंद्रह दिनों में सभी पूर्वजों का एक साथ किया जाने वाला श्राद्ध है। आचार्य उपेंद्र जी के अनुसार अलग-अलग तिथियों पर साल भर पितरों का स्मरण करते रहने से व्यक्ति स्वयं पितर बनने की ओर जाता है, इसलिए सबका श्राद्ध एक साथ होता है और किसी का कोई पूर्वज नहीं छूटता। | Direct answer (≈58 words) early, built only from the section "तो फिर महालय श्राद्ध क्यों?" and the last Key Takeaway, with the reasoning attributed to Acharya Ji (flag 1); puts the focus keyword in the body and in the first 100 words |
| Second H2 | ## तीन क्रियाएँ, तीन अर्थ | ## श्राद्ध, पिंडदान और तर्पण में क्या अंतर है? | Natural question readers search (secondary keyword "श्राद्ध, पिंडदान और तर्पण में अंतर", report section 4); the section and the three that follow answer it |

## English changes (`mahalay_shraddha_matters_truth_about_pitru_blog_seo_en.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro, before the first H2 | (none) | The Mahalaya Shraddha meaning, in short: a single rite honouring all of one's ancestors together during the fifteen days of Pitru Paksha. According to Acharya Upendra Ji, dwelling on the ancestors on separate dates all year pulls a person toward becoming an ancestral spirit, so all are honoured at once and no one's ancestor is left out. | Direct answer (≈58 words) early, built only from the section "Why Mahalaya Shraddha, Then?" and the last Key Takeaway, with the reasoning attributed to Acharya Ji (flag 1); puts the focus keyword in the body and in the first 100 words |
| Second H2 | ## Three Rites, Three Meanings | ## What Is the Difference Between Shraddha, Pinda Daan and Tarpan? | Natural question readers search (secondary keyword "difference between shraddha, pind daan and tarpan", report section 4); the section and the three that follow answer it |

No teaching, example, verse, translation, reference or link phrase was changed; heading number and order are the same, and the H1s are untouched. The heading "तो फिर महालय श्राद्ध क्यों?" / "Why Mahalaya Shraddha, Then?" was left as it is: the report allows its question rewrite only together with the Sanskrit review's flag 1 correction, which is editorial, not SEO. All five `links` phrases and the `also_read` heading appear unchanged in both `_seo` texts. The inline image's section (images.txt, "तर्पण: एक सीधा सा धन्यवाद" / "Tarpan: A Simple Thank You") is unchanged. The Sanskrit review's corrections (issues 1–7) were not applied here.

## Checklist

Now met:
- Focus keyword in the body text (Hindi and English)
- Focus keyword in the meta description (English)
- Focus keyword within the first 100 words (Hindi and English)
- Direct answer placed early (both languages)
- A question heading (both languages)

Still unmet (2), in the new section 12:
- No broad labels that only restate a category: the tags "Ancestors" / "पितर" largely restate the category "Ancestors & Shraddha" / "पितृ और श्राद्ध". Tags are outside this fix's scope, so they were left as /seo_blog chose them.
- No unsupported scriptural claims: the body still presents the three-year annual-shraddha rule as the sages' system (Sanskrit review issue 1, report flag 1). That is an editorial correction of the blog text, not an SEO fix. The new direct answers attribute the reasoning to Acharya Ji and do not say the tithi shraddha may be stopped.

The report had no section 12; it was added, marked against the `_seo` texts. Report section 2 got a keyword-placement note; sections 3, 8 and 11 now show the new English meta description.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | What is Mahalaya Shraddha, and why honour all ancestors together in Pitru Paksha? Acharya Upendra Ji explains shraddha, pinda daan and tarpan simply. | Mahalaya Shraddha meaning: why honour all ancestors together in Pitru Paksha? Acharya Upendra Ji explains shraddha, pinda daan and tarpan simply. (145 characters) |

Slugs are unchanged (hi: `mahalaya-shraddha-kya-hai` → `mahalaya-shraddha-kya-hai`; en: `mahalaya-shraddha-meaning` → `mahalaya-shraddha-meaning`). So are the focus keywords, the titles, the Hindi meta description, the secondary keywords, the tags, `links` and `also_read`.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | mahalaya-shraddha-kya-hai | mahalaya-shraddha-meaning |
| focus_keyword | महालय श्राद्ध क्या है | Mahalaya Shraddha meaning |
| title | महालय श्राद्ध क्या है? श्राद्ध, पिंडदान, तर्पण का सच्चा अर्थ | Mahalaya Shraddha Meaning: Shraddha, Pind Daan and Tarpan |
| meta_description | महालय श्राद्ध क्या है और पितृ पक्ष में सभी पूर्वजों का श्राद्ध एक साथ क्यों? आचार्य उपेंद्र जी सरल भाषा में बताते हैं श्राद्ध, पिंडदान और तर्पण का अर्थ। | Mahalaya Shraddha meaning: why honour all ancestors together in Pitru Paksha? Acharya Upendra Ji explains shraddha, pinda daan and tarpan simply. |
