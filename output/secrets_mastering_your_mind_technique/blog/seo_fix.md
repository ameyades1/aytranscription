secrets_mastering_your_mind_technique: SEO fix

Fixed texts: `secrets_mastering_your_mind_technique_blog_seo.txt` (Hindi) and `secrets_mastering_your_mind_technique_blog_seo_en.txt` (English). The original blog texts are unchanged. No teaching, example, verse, translation, reference, H1 or order of ideas was changed, and no new claim was added.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new third paragraph (after "…यही असली प्रश्न है।") | (none) | तो स्थिर मन कैसे पाएं? संक्षेप में, आचार्य जी के अनुसार स्थिर मन, यानी अथर्व मन, तब आता है जब आप स्वयं, अर्थात आत्मा, अपने भीतर के गण (शरीर, मन, बुद्धि, चित्त, श्वास और प्राण) के अधिपति बनते हैं। इसका मार्ग है उत्तेजना से दूरी, प्राणायाम और आसन, और अंत में केवल सिद्धांत नहीं, गुरु के प्रति शरणागति। | The body never used the focus keyword "स्थिर मन कैसे पाएं" (`check_seo.py` failed), and the opening did not answer the main question early. A 58-word direct answer, built only from the blog's own sections (the inner gana, pranayama and asana, surrender to the Guru) and the report's section 5, puts the keyword in the first 100 words. |
| `##` heading 3 | आपके भीतर का गण | आपके भीतर का गण: शरीर, मन और प्राण का अधिपति कौन? | Turns the heading into the question readers search (report section 4); the section answers it (आप, आत्मा). The original wording is kept at the start. |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new third paragraph (after "…what kind of mind does the fighting.") | (none) | In short, Acharya Ji teaches how to develop a steady mind: an atharva mind comes when you, the Atman, take charge of your inner gana of body, mind, intellect, chitta, breath and prana. Distance from overstimulation, pranayama and asanas bring breath and mind under your command, and the final step is not theory but surrender to the Guru. | The body never used the focus keyword "how to develop a steady mind" (`check_seo.py` failed), and the opening did not answer the main question early. A 58-word direct answer, built only from the blog's own sections and the report's section 5, puts the keyword in the first 100 words. |
| `##` heading 3 | The Gana Within You | The Gana Within You: Who Rules Body, Mind and Breath? | Question heading from report section 4; the section answers it (you, the Atman). The original wording is kept at the start. |

Every `links` phrase and both `also_read` headings ("हारा हुआ मन, हारा हुआ राष्ट्र" / "A Defeated Mind, a Defeated Nation") are still in the `_seo` texts word for word; none was touched. The inline image heading ("क्या आपकी श्वास आपकी सुनती है?" / "Does Your Breath Obey You?") was not changed.

## Checklist

Now met:
- Focus keyword in the body text (Hindi and English; `check_seo.py` failed on both before).
- Focus keyword in the meta description (English; `check_seo.py` failed before).
- Focus keyword within the first 100 words (Hindi and English).
- Focus keyword taken from wording the article uses (Hindi and English, in the `_seo` texts).
- Section 12 (the checklist) was missing from the report and has been added.

Still unmet (1):
- No unsupported scriptural claims: the blog adds a promise of liberation to the meaning of Narada Bhakti Sutra 42, names a non-existent "ज्ञानमय कोश" / "jnanamaya kosha", and attributes the "true devotee" line to sutra 42 (report flags 1–3, Sanskrit review). Fixing these would change verse translations and the teaching's wording, which the SEO fix must not do; it is left to the editor.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | How do you develop a steady mind? Acharya Upendra Ji explains the atharva mind, ruling your inner gana of body, breath and mind, and surrender to the Guru. | How to develop a steady mind? Acharya Upendra Ji explains the atharva mind, ruling your inner gana of body, breath and mind, and surrender to the Guru. |
| wordpress.hi.slug | sthir-man-kaise-paayen | sthir-man-kaise-paayen (unchanged) |
| wordpress.en.slug | how-to-develop-a-steady-mind | how-to-develop-a-steady-mind (unchanged) |

Both focus keywords stay as they were ("स्थिर मन कैसे पाएं" / "how to develop a steady mind"): they are already the searched wording, the `_seo` texts now use them, and they are unique across all talks. Titles, the Hindi meta description, `secondary_keywords`, `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in these places:
- section 2: a keyword note;
- section 3: the meta descriptions and slugs marked as recommended (English meta updated, 151 characters);
- section 4: the direct answer and heading suggestions marked as done;
- section 8: the English schema description;
- section 11;
- section 12, which was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sthir-man-kaise-paayen | how-to-develop-a-steady-mind |
| focus_keyword | स्थिर मन कैसे पाएं | how to develop a steady mind |
| title | स्थिर मन कैसे पाएं? अथर्व मन और जीवन का नेतृत्व | How to Develop a Steady Mind: The Atharva Way to Lead |
| meta_description | स्थिर मन कैसे पाएं? आचार्य उपेंद्र जी बताते हैं अथर्व मन का अर्थ, शरीर, श्वास और मन के भीतरी गण का नेतृत्व, और गुरु के प्रति शरणागति का रहस्य। | How to develop a steady mind? Acharya Upendra Ji explains the atharva mind, ruling your inner gana of body, breath and mind, and surrender to the Guru. |
