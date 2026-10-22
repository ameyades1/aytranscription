two_causes_create_your_life: SEO fix

Fixed texts: `two_causes_create_your_life_blog_seo.txt` (Hindi) and `two_causes_create_your_life_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro (new paragraph after "…असल में करने वाला कौन है?") | (none) | उपादान और निमित्त कारण को ऐसे समझें: उपादान वह सामग्री है जिससे कोई वस्तु बनती है, जैसे घड़े के लिए मिट्टी, और निमित्त वह है जो उसे बनाता है, जैसे कुम्हार। आचार्य जी बताते हैं कि गहराई से देखें तो कुम्हार का शरीर, मन और इच्छा भी उपादान ही हैं, और "मैंने बनाया" कहने वाले अहंकार के आगे एक उच्चतर शक्ति है। | The focus keyword "उपादान और निमित्त कारण" was not in the body (only "उपादान कारण और निमित्त कारण"); it now appears within the first 100 words. Also gives the early direct answer (about 60 words), built only from the blog's own points (clay, potter, body, mind, desire, the ego's "मैंने बनाया", the higher power). Uses only clay as the example of upadana, so it is accurate whatever the editor decides on review issue 1. |
| `##` heading of the second-to-last section | ## वास्तविक कर्ता | ## वास्तविक कर्ता कौन है? | Phrased as the question readers search for; the section answers it. Keeps the blog's own word "वास्तविक" (not "असली कर्ता कौन है", another talk's focus keyword). |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro (new paragraph after "…who is really doing the work?") | (none) | Every creation has a material and efficient cause: the material cause is what a thing is made of, like clay for a pot, and the efficient cause is the one who makes it, the potter. Acharya Ji shows that the potter's body, mind and desire are material too, and a higher power stands beyond the ego that says "I made it." | The searched wording "material and efficient cause" was not in the body; it now appears within the first 100 words and is the new focus keyword. Also gives the early direct answer (about 60 words), built only from the blog's own points. Clay is the only example of the material cause (safe with review issue 1). |
| `##` heading of the second-to-last section | ## The True Doer | ## Who Is the True Doer? | Phrased as the question readers search for; the section answers it. |

## Checklist

Now met (were failing before):
- Hindi focus keyword in the body text, within the first 100 words.
- English focus keyword in the SEO title, meta description, body text, slug, and within the first 100 words (focus keyword changed to "material and efficient cause"; meta description reworded).
- Direct answer paragraph placed early in both languages; one heading per language phrased as a question.

Still unmet:
- No unsupported scriptural claims: both bodies still place tools (wheel, hammer, nails) on the upadana side under "वेदांत कहता है" / "Vedanta teaches", and state Ganapati as the true doer without "according to Acharya Ji" (Sanskrit review issues 1–2, report flags 1–2). These are corrections of content, not SEO, and are left to the editor (`tools/review/two_causes_create_your_life.md`).

Not changed: review issues 3–4 (चैतन्य as an adjective; "the foundational text of Vedanta") are also content corrections for the editor. The report's section 4 note that the keyword was already in the first 100 words was outside the sections this fix updates; it is now true of the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.focus_keyword | material and efficient cause in Vedanta | material and efficient cause |
| wordpress.en.secondary_keywords | upadana karana and nimitta karana; who is the real doer; ego and doership; Brahma Sutras potter and pot | material and efficient cause in Vedanta; upadana karana and nimitta karana; who is the real doer; ego and doership |
| wordpress.en.meta_description | What are the material and efficient causes in Vedanta? With a potter and his pot, Acharya Upendra Ji shows why the "I made it" ego is not the true doer. | What is the material and efficient cause in Vedanta? With a potter and his pot, Acharya Upendra Ji shows why the "I made it" ego is not the true doer. (150 characters) |
| wordpress.en.slug | material-and-efficient-cause-vedanta | material-and-efficient-cause-vedanta (unchanged: already contains the new focus keyword) |
| wordpress.hi (all fields) | unchanged | unchanged (the focus keyword was already in the title, meta and slug idea; only the body needed it) |
| title, links, also_read, alt, caption, related | unchanged | unchanged |

Report updated to match: section 2 (keyword table and note), section 3 (recommended meta and slugs marked), section 8 (English description and keywords), section 11 (seo.json block), and section 12 (checklist, added).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | upadan-aur-nimitt-karan | material-and-efficient-cause-vedanta |
| focus_keyword | उपादान और निमित्त कारण | material and efficient cause |
| title | उपादान और निमित्त कारण: घड़ा कौन बनाता है? | Material and Efficient Cause: Who Really Makes the Pot? |
| meta_description | उपादान और निमित्त कारण क्या हैं? कुम्हार और घड़े के उदाहरण से आचार्य उपेंद्र जी समझाते हैं कि "मैंने बनाया" कहने वाला अहंकार असली कर्ता क्यों नहीं है। | What is the material and efficient cause in Vedanta? With a potter and his pot, Acharya Upendra Ji shows why the "I made it" ego is not the true doer. |
