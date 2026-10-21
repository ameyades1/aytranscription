non_veg_food_remains_body_truths: SEO fix

Fixed texts: `non_veg_food_remains_body_truths_blog_seo.txt` (Hindi) and `non_veg_food_remains_body_truths_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| H2 (first section) | ## शरीर स्वयं उत्तर देता है | ## क्या मनुष्य का शरीर मांसाहार के लिए बना है? | The focus keyword was not in the body at all; now in a heading phrased as the question readers search (report section 4). The section answers it. Number and order of headings unchanged |
| New paragraph after the first paragraph of that section | (none) | आचार्य उपेंद्र जी के अनुसार मनुष्य का शरीर मांसाहार के लिए नहीं बना। हमारा पाचन तंत्र लंबा है और आँतें लहरदार नली जैसी हैं, जो भोजन से सत्व और रस सोखने के लिए बनी हैं। मांसाहारी प्राणियों का पाचन तंत्र छोटा और चिकना है, ताकि मांस तुरंत बाहर निकल जाए। वे बताते हैं कि हमारे भीतर मांस देर तक रहकर सड़ता है और रोग लाता है। | Direct answer early (report section 5, about 58 words), built only from the blog's sections on the digestive tract, the two pipes and rotting; every claim attributed to Acharya Ji (flags 1–3). Leaves out the "ten years" claim (flag 1) and repeats no link phrase |

## English changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| H2 (first section) | ## Your Own Anatomy Holds the Answer | ## Are Humans Meant to Eat Meat? | The focus keyword was not in the body; now in a heading phrased as the searched question (report section 4). The section answers it. Number and order of headings unchanged |
| New paragraph after the first paragraph of that section | (none) | According to Acharya Upendra Ji, the human body is not built for meat. Our digestive tract is long and our intestine works like a ridged pipe, made to absorb nourishment and essence from food. A carnivore's tract is short and smooth, so meat passes straight out. In us, he explains, meat lingers, ferments and brings disease. | Direct answer early (report section 5, about 57 words), built only from the blog; attributed to Acharya Ji; no "ten years" claim; repeats no link phrase |

All `links` phrases and the `also_read` heading ("सिंह बीमार नहीं होता, तो हम क्यों?" / "If the Lion Stays Healthy, Why Don't We?") are still in the texts, word for word, once each. The H1 was not touched; the blog has no verses.

## Checklist

The report had no section 12; it was added (from `tools/prompts/seo_checklist.md`) and marked against the fixed texts.

Now met:
- Focus keyword in the body text, both languages (it was missing before).
- Focus keyword within the first 100 words, both languages.
- A direct answer paragraph (40–60 words) placed early, both languages.
- One H2 per language phrased as the searched question.

Still unmet: none.

Left for the editor (not SEO fixes): Sanskrit review issues 1 and 2 (attribute the "food eaten ten years ago stays in the intestines" claim and the rotting/disease claims to Acharya Ji) and the optional सत्व → सत्त्व spelling (issue 3) are not applied in the body; they are content corrections, flagged in report section 10.

## seo.json changes

None. Both focus keywords now appear in the fixed texts as they are, so the focus keywords, secondary keywords, titles, meta descriptions and slugs (Hindi `kya-sharir-mansahar-ke-liye-bana-hai`, English `are-humans-meant-to-eat-meat`, old and new) stay the same, as do `links`, `also_read`, `related`, alt text, captions, category and tags.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | kya-sharir-mansahar-ke-liye-bana-hai | are-humans-meant-to-eat-meat |
| focus keyword | क्या मनुष्य का शरीर मांसाहार के लिए बना है | are humans meant to eat meat |
| title | क्या मनुष्य का शरीर मांसाहार के लिए बना है? | Are Humans Meant to Eat Meat? What Your Gut Reveals |
| meta description | क्या मनुष्य का शरीर मांसाहार के लिए बना है? आचार्य उपेंद्र जी लंबी, लहरदार मानव आँत की तुलना मांसाहारी प्राणियों की छोटी, चिकनी आँत से करते हैं। | Are humans meant to eat meat? Acharya Upendra Ji compares the long, ridged human gut with the short, smooth gut of a carnivore and what each is built for. |
