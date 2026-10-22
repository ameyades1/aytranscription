truly_independent: SEO fix

Copies written: `truly_independent_blog_seo.txt` (Hindi) and `truly_independent_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| H2 1 | एक लंबा नाम, एक गहरा अर्थ | हमारा संविधान भारत को क्या कहता है? | A natural question readers search (report section 4); the section answers it by listing the Constitution's description of India |
| New paragraph after the two opening paragraphs | (none) | लोकतंत्र का असली अर्थ है लोगों का, लोगों के द्वारा, लोगों के लिए शासन, जिसमें देश का पूरा तंत्र लोगों के हाथ में हो। आचार्य उपेंद्र जी कहते हैं कि आज "by the people" "buy the people" बनता जा रहा है, क्योंकि नागरिक अपनी ताकत भूल गए हैं। सच्ची स्वतंत्रता अपनी ताकत को याद रखने और अपने संविधान को जानने से शुरू होती है। | The focus keyword "लोकतंत्र का असली अर्थ" was not in the body (`check_seo.py` failed) or the first 100 words, and the opening gave no direct answer. Built only from the blog (section "By the People या Buy the People?" and the takeaways; report section 5) |
| H2 3 | By the People या Buy the People? | लोकतंत्र का असली अर्थ: By the People या Buy the People? | Focus keyword in a heading; the section defines democracy and explains the "buy the people" wordplay |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| H2 1 | A Long Name with a Deep Meaning | How Does Our Constitution Describe India? | A natural question readers search (report section 4); the section answers it |
| New paragraph after the two opening paragraphs | (none) | The true meaning of democracy is government of the people, by the people, for the people, with the entire machinery of the country in the hands of its people. Acharya Upendra Ji observes that "by the people" is turning into "buy the people" because citizens have forgotten their strength. True freedom begins with remembering that strength and knowing your Constitution. | The focus keyword "true meaning of democracy" was not in the body (`check_seo.py` failed) or the first 100 words, and the opening gave no direct answer. Built only from the blog (section "By the People or Buy the People?" and the takeaways; report section 5) |
| H2 3 | By the People or Buy the People? | The True Meaning of Democracy: By the People or Buy the People? | Focus keyword in a heading; the section defines democracy and explains the wordplay |

The headings keep their number and order. No teaching, example or the H1 was touched (the blog quotes no verses). The Sanskrit review's corrections (Chanakya framing, "federal") are content changes left to the editor. All five `links` phrases are still in each text word for word, and the `also_read` headings ("आपने अपना संविधान पढ़ा है?" / "Have You Read Your Constitution?") are unchanged.

## Checklist

Now met:
- Focus keyword in the body text: both languages (both failed `check_seo.py` before).
- Focus keyword within the first 100 words: both languages, in the direct-answer paragraph.
- Direct answer early (report section 5): added in both languages.
- Question headings: the first H2 in each language is now a natural question, and the third carries the focus keyword.

Still unmet (2):
- Each tag can be shared by at least 3 posts: "Democracy" / "लोकतंत्र" is used by 1 post and "Independence Day" / "स्वतंत्रता दिवस" by 2. A tag choice, not something the blog text can fix.
- No unsupported scriptural claims: the Chanakya sayings on democracy are unsourced and presented as known sayings (Sanskrit review item 1, report flag 1). A content correction for the editor, not an SEO fix.

`python3 tools/check_seo.py truly_independent` passes.

## Report updates

- Section 2: keyword note added describing the `_seo` texts.
- Section 3: the titles, meta descriptions and slugs marked recommended already equal seo.json; unchanged.
- Section 4: note that the direct answer and heading changes are done in the `_seo` texts.
- Section 8: headline (the unchanged H1), alternativeHeadline, description, keywords and slugs already match seo.json; unchanged.
- Section 11: the JSON block equals seo.json (unchanged).
- Section 12: the SEO checklist was missing from the report; added and marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.focus_keyword, wordpress.en.focus_keyword | लोकतंत्र का असली अर्थ / true meaning of democracy | unchanged (the `_seo` texts now use them) |
| wordpress.hi.slug, wordpress.en.slug | loktantra-ka-asli-arth / true-meaning-of-democracy | unchanged |
| title, meta_description (both languages) | (as below) | unchanged (already contain the focus keyword) |
| links, also_read | (unchanged) | unchanged (no edit touched a link phrase or the Also read heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | loktantra-ka-asli-arth | true-meaning-of-democracy |
| focus_keyword | लोकतंत्र का असली अर्थ | true meaning of democracy |
| title | लोकतंत्र का असली अर्थ: क्या हम सच में आज़ाद हैं? | True Meaning of Democracy: Are We Really Free? |
| meta_description | लोकतंत्र का असली अर्थ क्या है? आचार्य उपेंद्र जी: भारत ने स्वयं को संप्रभु क्यों कहा, by the people कैसे buy the people बना, और नागरिक की असली ताकत। | What is the true meaning of democracy? Acharya Upendra Ji on why India calls itself sovereign, how by the people became buy the people, and your power. |
