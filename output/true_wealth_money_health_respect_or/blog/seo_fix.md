true_wealth_money_health_respect_or: SEO fix

Copies written: `true_wealth_money_health_respect_or_blog_seo.txt` (Hindi) and `true_wealth_money_health_respect_or_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph under the H1 | (none) | सच्चा धन क्या है? सच्चा धन केवल पैसा नहीं है। आचार्य जी के अनुसार इसमें संपत्ति, सम्मान, समाज, समय, परिवार और संबंध, और स्वास्थ्य, ये सब आते हैं। धन केवल मेहनत से नहीं, बुद्धि से आता है, और आत्मा बुद्धि से भी ऊपर है। जिसके पास केवल पैसा है और बाकी सब टूट गया है, वहां लक्ष्मी नहीं होती। | The focus keyword "सच्चा धन क्या है" appeared only in the H1, which SureRank does not count, and the opening gave no direct answer (report sections 4 and 5). The 59-word answer uses only what the blog says (the six forms, "केवल मेहनत से नहीं, बुद्धि से", the Atman above the intellect, no Lakshmi where only money remains), attributed to Acharya Ji, with "परिवार और संबंध" as in the report (flag 3) |
| H2 2 | बुद्धि से भी आगे: आत्मा | बुद्धि से ऊपर क्या है? आत्मा | A natural question readers search (report section 4); the section answers it with Gita 3.42 |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph under the H1 | (none) | What is true wealth? It is far more than money. According to Acharya Ji, true wealth includes property, respect, community, time, family and relationships, and health. Money comes through intelligence, not hard work alone, and the Atman stands even higher than the intellect. Where there is only money and everything else has broken down, Lakshmi is not present. | The focus keyword "what is true wealth" appeared only in the H1, which SureRank does not count, and the opening gave no direct answer (report sections 4 and 5). The 58-word answer uses only what the blog says (the six forms, Key Takeaways 1 and 5), attributed to Acharya Ji |
| H2 2 | Beyond the Intellect: The Atman | What Lies Beyond the Intellect? The Atman | A natural question readers search (report section 4); the section answers it with Gita 3.42 |

The headings keep their number and order. No teaching, example, verse, translation, reference or H1 was touched. The direct answers avoid the link phrases, so each `links` phrase and the `also_read` headings ("धन के छह रूप" / "The Six Forms of Wealth") still appear in the texts word for word, once each. The inline image is still placed under "धन के छह रूप" / "The Six Forms of Wealth".

## Checklist

Now met:
- Focus keyword in the body text (both languages): before, only the H1 had it.
- Focus keyword within the first 100 words: both languages, in the direct-answer paragraph.
- Direct answer early (report section 5): added in both languages.
- Question headings: one more H2 per language is now a natural question.

Still unmet (1):
- No unsupported scriptural claims: the body still says Adi Shankaracharya brought a shower of gold "whenever he wished" (Sanskrit review issue 2, report flag 2), and the Hindi meaning of Gita 3.42 drops its first clause (issue 1, flag 1). These are content corrections for the editor, not SEO fixes, and verse translations may not be touched here; they were left as they are.

`python3 tools/check_seo.py true_wealth_money_health_respect_or` passes. `tools/rebuild_blogs.sh true_wealth_money_health_respect_or` rebuilt 9 pages with no "Note:" lines.

## Report updates

- Section 2: keyword note added describing the `_seo` texts.
- Section 3: the titles, meta descriptions and slugs already marked recommended are the ones in seo.json; unchanged.
- Section 8: the schema fields already match seo.json; a note giving the suggested URL slugs for `{{HI_URL}}` and `{{EN_URL}}` was added.
- Section 11: unchanged; the JSON block equals seo.json.
- Section 12: the SEO checklist was missing from the report; added and marked for the `_seo` texts.

## seo.json changes

None. The `_seo` texts now use both focus keywords in the body, and the titles and meta descriptions already contain them.

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | sachcha-dhan-kya-hai | unchanged |
| wordpress.en.slug | what-is-true-wealth | unchanged |
| focus_keyword (hi, en) | सच्चा धन क्या है, what is true wealth | unchanged |
| title, meta_description, links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sachcha-dhan-kya-hai | what-is-true-wealth |
| focus_keyword | सच्चा धन क्या है | what is true wealth |
| title | सच्चा धन क्या है: पैसा, सम्मान, समय और स्वास्थ्य | What Is True Wealth? Money, Health, Respect and More |
| meta_description | सच्चा धन क्या है? आचार्य उपेंद्र जी बताते हैं कि धन केवल मेहनत से नहीं, बुद्धि से आता है, संत धन से अनासक्त क्यों रहते हैं, और धन के छह रूप कौन से हैं। | What is true wealth? Acharya Upendra Ji explains why money follows intellect, why saints stay unattached, and the six forms of wealth beyond money. |
