mrityu_versus_moksha: SEO fix

Fixed texts: `mrityu_versus_moksha_blog_seo.txt` (Hindi) and `mrityu_versus_moksha_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro, before "## क्या मृत्यु हो जाना ही मुक्ति है?" | (none) | क्या श्राद्ध से पितरों को मुक्ति मिलती है? आचार्य जी के अनुसार मृत्यु और मोक्ष अलग हैं। मृत्यु में केवल शरीर जाता है; अधूरी इच्छाएँ जीव को फिर जन्म दिलाती हैं। आचार्य जी मोक्ष को मोह का क्षय बताते हैं, जो जीते जी होता है। इसलिए पितरों को मुक्ति वही दे सकता है जो स्वयं जीते जी मुक्त हो; केवल विधि पूरी कर देना पर्याप्त नहीं। | The focus keyword was not in the body at all (check_seo failed); now in the first 100 words. Direct answer (about 50 words, report section 5) built only from the blog's sections on death, moksha and who can grant liberation. Moha-kshaya is attributed to Acharya Ji (flag 4). Worded so it does not repeat the link phrase "जो स्वयं जीते जी मुक्त हो चुका है" |
| H2 (fourth section) | ## मुक्ति कौन दे सकता है? | ## पितरों को मुक्ति कौन दे सकता है? | Heading as the question readers search (report section 4); the section answers it. Number and order of headings unchanged |

## English changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro, before "## Does Dying Set You Free?" | (none) | Can shraddha liberate ancestors? According to Acharya Ji, death and moksha are not the same. Death takes only the body; unfulfilled desires bring the soul back to another birth. Moksha, as he explains it, is the dissolving of attachment, and it happens while living. So only one who is already free while living can liberate the ancestors; completing the ritual alone is not enough. | The focus keyword was not in the body (check_seo failed); now in the first 100 words. Direct answer (about 60 words, report section 5) built only from the blog; moha-kshaya attributed (flag 4). Avoids the link phrases "Only someone who is already free while living" and "the soul returns in a new body" |
| H2 (fourth section) | ## Who Can Grant Liberation? | ## Who Can Liberate Our Ancestors? | Heading as the searched question ("who can liberate ancestors", a secondary keyword); the section answers it. Number and order of headings unchanged |

All `links` phrases and the `also_read` heading ("बेटे के श्राद्ध की प्रतीक्षा क्यों?" / "Why Wait for Your Son to Perform Shraddha?") are still in the texts, word for word, once each. No verse, translation, reference or H1 was touched.

## Checklist

The report had no section 12; it was added (from `tools/prompts/seo_checklist.md`) and marked against the fixed texts.

Now met:
- Focus keyword in the body text, both languages (it was missing before).
- Focus keyword in the English title and meta description (seo.json updated).
- Focus keyword within the first 100 words, both languages.
- A direct answer paragraph (40–60 words) placed early, both languages.
- One H2 per language phrased as a searched question.

Still unmet (1):
- No unsupported scriptural claims: Sanskrit review issues 1 and 2 (Major: the Vishnu Purana 3.15 reading of who the yogi is, and the empty blockquote with an unconfirmed verse number) and issue 3 (the Garuda Purana attribution of atma-shraddha) are still in the blog body. They are content corrections for the editor, not SEO fixes. The added direct answer does not cite any of these sources.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Does Shraddha Free Your Ancestors? Death vs Moksha | Can Shraddha Liberate Ancestors? Death vs Moksha |
| wordpress.en.meta_description | Is death the same as moksha, and can shraddha free your ancestors? Acharya Upendra Ji explains why only one liberated while living can grant liberation. | Can shraddha liberate ancestors, and is death the same as moksha? Acharya Upendra Ji explains why only one free while living can grant liberation. |

Slugs are unchanged (Hindi `shraddha-se-pitron-ki-mukti`, English `can-shraddha-liberate-ancestors`), as are both focus keywords, the secondary keywords, the Hindi title and meta description, `links`, `also_read`, `related`, alt text, captions, category and tags.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | shraddha-se-pitron-ki-mukti | can-shraddha-liberate-ancestors |
| focus keyword | क्या श्राद्ध से पितरों को मुक्ति मिलती है | can shraddha liberate ancestors |
| title | क्या श्राद्ध से पितरों को मुक्ति मिलती है? मृत्यु बनाम मोक्ष | Can Shraddha Liberate Ancestors? Death vs Moksha |
| meta description | क्या मृत्यु ही मुक्ति है, और क्या श्राद्ध से पितरों को मुक्ति मिलती है? आचार्य उपेंद्र जी बताते हैं कि जीते जी मुक्त व्यक्ति ही पितरों को मुक्ति दे सकता है। | Can shraddha liberate ancestors, and is death the same as moksha? Acharya Upendra Ji explains why only one free while living can grant liberation. |
