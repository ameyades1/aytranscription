ganpati_visarjan_tradition: SEO fix

Copies: `ganpati_visarjan_tradition_blog_seo.txt` (Hindi) and `ganpati_visarjan_tradition_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph at the end of "दस दिन, और फिर?" | (none) | तो गणपति विसर्जन का अर्थ क्या है? आचार्य उपेंद्र जी के अनुसार यह मूर्ति का नाम-रूप बहते जल, यानी ज्ञान-गंगा में अर्पित करना है, जैसे अलग-अलग गहने गलकर एक ही स्वर्ण बन जाते हैं। विसर्जन के बाद लौटी मुट्ठी भर मिट्टी सबको समान मिलती है: वह एक ही परमात्मा का प्रतीक है और अद्वैत सिखाती है। | The focus keyword was not in the body at all (`check_seo.py` failed). It now comes in the first 100 words (word 84), inside a 56-word direct answer (report sections 4 and 5) built only from "विसर्जन: नाम-रूप को ज्ञान-गंगा में अर्पित करना", "सबके हाथ एक जैसी मिट्टी" and the key takeaways. It repeats none of the link phrases |
| H2 | ## मिट्टी को कचरा मत समझो | ## विसर्जन के बाद मिट्टी का क्या करें? | Natural search question and secondary keyword (report section 4). The section answers it: tradition spread the clay through the house and mixed it into the walls, and it should not go down the drain |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph at the end of "Ten Days, and Then What?" | (none) | So what is the meaning of Ganpati Visarjan? According to Acharya Upendra Ji, it is offering the idol's name and form to flowing water, the Ganga of knowledge, just as different ornaments melt into the same gold. The handful of clay that comes back is the same for everyone: it stands for the one God in all and teaches Advaita. | "Ganpati Visarjan" (the searched wording) and the focus keyword were missing from the body. Both now come in the first 100 words (word 96), inside a 60-word direct answer built only from the visarjan and clay sections and the key takeaways. It uses the blog's own "the one God in all" (Key Takeaways), not section 5's "Supreme Self", so it adds no new term. It repeats none of the link phrases |
| H2 | ## Do Not Treat the Clay as Rubbish | ## What to Do with the Clay After Visarjan? | Natural search question and secondary keyword ("what to do with visarjan clay"). The section answers it |

A first draft also added "गणपति विसर्जन के दिन" / "the day of Ganpati Visarjan" to the opening sentence. I took it out again: the direct answer already puts the keyword in the first 100 words, and with both edits the English keyword fell just past word 100.

Not changed: the H1s. Also unchanged is the Also read heading "विसर्जन: नाम-रूप को ज्ञान-गंगा में अर्पित करना" / "Visarjan: Offering Name and Form to the Ganga of Knowledge". So is the inline image's heading "सबके हाथ एक जैसी मिट्टी" / "The Same Clay in Every Hand". All five link phrases in each language are unchanged, each still found by grep and by the rebuild (no "Note:" lines). The number and order of headings are unchanged. The blog has no scripture verses.

The Sanskrit review's corrections are not part of this fix and are still open (report section 10):
- "अंतर में" → "अंतर योग में"
- the unsourced "शास्त्र कहता है"
- "गुरुदेव" → "आचार्य जी"
- English glosses in the Hindi
- "Lord Ganesha arrives" → "Ganpati arrives"
- "God" → "Paramatma (the Supreme Self)"

## Checklist

Now met:
- The focus keyword is in the body text, both languages. It was missing from both bodies, and `check_seo.py` failed.
- The focus keyword is in the meta description, both languages. Both failed before: the Hindi had "गणपति विसर्जन का असली अर्थ", and the English had "Ganpati Visarjan really mean".
- The focus keyword comes within the first 100 words, both languages.
- The focus keyword is taken from wording the article uses (the `_seo` texts), and the searched-wording mismatch is flagged in section 2 and fixed.
- A 40–60 word direct answer comes early in the post, both languages.
- One H2 per language is phrased as a natural search question.

Still unmet: none. Report section 12 was added by this fix, since the report had none, and it marks every item met. `python3 tools/check_seo.py ganpati_visarjan_tradition` passes.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Ganpati Visarjan Meaning: What the Returned Clay Teaches | Meaning of Ganpati Visarjan: What the Returned Clay Teaches (59 characters) |
| wordpress.en.focus_keyword | Ganpati Visarjan meaning | meaning of Ganpati Visarjan |
| wordpress.en.slug | ganpati-visarjan-meaning | meaning-of-ganpati-visarjan |
| wordpress.en.meta_description | What does Ganpati Visarjan really mean? Acharya Upendra Ji explains why name and form dissolve, and why everyone gets back the same handful of clay. | What is the meaning of Ganpati Visarjan? Acharya Upendra Ji explains why name and form dissolve, and why everyone gets back the same handful of clay. (149 characters) |
| wordpress.en.secondary_keywords | unchanged (the old keyword is the same query in a different word order, so it is not added) | unchanged |
| wordpress.hi.meta_description | गणपति विसर्जन का असली अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि नाम-रूप का विलय क्यों होता है और लौटी मुट्ठी भर मिट्टी अद्वैत का पाठ कैसे पढ़ाती है। | गणपति विसर्जन का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि नाम-रूप का विलय क्यों होता है और लौटी मुट्ठी भर मिट्टी अद्वैत का पाठ कैसे पढ़ाती है। (146 characters) |
| wordpress.hi.slug | ganpati-visarjan-ka-arth | ganpati-visarjan-ka-arth (unchanged; built from the unchanged focus keyword) |
| wordpress.hi.focus_keyword, title.hi | unchanged | unchanged |
| links, also_read, alt, caption, related, tags, category | unchanged | unchanged |

The report was updated to match:
- section 2: the keyword table and the mismatch note;
- section 3: the English recommended title, both meta descriptions and the English slug;
- section 7: the cannibalization note's keyword;
- section 8: the English alternativeHeadline, both descriptions, the English keywords and the suggested slug;
- section 11: the seo.json block;
- section 12: the checklist, added and marked.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ganpati-visarjan-ka-arth | meaning-of-ganpati-visarjan |
| focus_keyword | गणपति विसर्जन का अर्थ | meaning of Ganpati Visarjan |
| title | गणपति विसर्जन का अर्थ: मुट्ठी भर मिट्टी क्या सिखाती है | Meaning of Ganpati Visarjan: What the Returned Clay Teaches |
| meta_description | गणपति विसर्जन का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि नाम-रूप का विलय क्यों होता है और लौटी मुट्ठी भर मिट्टी अद्वैत का पाठ कैसे पढ़ाती है। | What is the meaning of Ganpati Visarjan? Acharya Upendra Ji explains why name and form dissolve, and why everyone gets back the same handful of clay. |
