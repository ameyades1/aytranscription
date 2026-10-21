pind_daan: SEO fix

`check_seo.py` failed before this fix: neither blog body nor either meta description contained the focus keyword word for word ("पिंडदान का अर्थ" / "pind daan meaning"). The report had no section 12 checklist, so one was added. Its "No unsupported scriptural claims" item would have been unmet: the report's flags 1–4 (Sanskrit review issues 1–4, Minor) were not yet applied. Each language gets a short direct answer after the first intro paragraph, which puts the focus keyword in the first 100 words. It also gets one H2 rephrased as the question readers search, plus the review's own corrections. The focus keywords and slugs stay the same. Only the meta descriptions changed in seo.json.

## Hindi (`pind_daan_blog_seo.txt`): 5 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…यह सब क्यों?") | (none) | संक्षेप में, पिंडदान का अर्थ यह है: श्राद्ध में चावल का पिंड पितरों को अर्पित किया जाता है, पर आचार्य उपेंद्र जी के अनुसार पिंड का गहरा अर्थ है श्राद्ध करने वाले का अपना शरीर, मन और बुद्धि। विकारों और वासनाओं को एक ओर रखकर इसी पिंड को परमात्मा को अर्पण करना है। कौवा किसी का पूर्वज नहीं, वह पितरों की उपस्थिति का संकेतक है। | The focus keyword was missing from the body. This direct answer (about 60 words) is built only from the blog's own sections and the report's section 5, and it puts "पिंडदान का अर्थ" in the first 100 words. It answers the intro's question early. It gives the literal meaning first (flag 2) and attributes the deeper reading to Acharya Ji. It does not repeat the link phrase "इस पिंड को परमात्मा के लिए अर्पण करना". |
| First H2 | ## पिंड क्या है? यह शरीर भी एक गांव है | ## पिंडदान का अर्थ क्या है? यह शरीर भी एक गांव है | Rephrased as the question readers search. The section answers it: the pind and offering it to God. The number and order of headings are unchanged. |
| "पिंडदान का अर्थ क्या है?", paragraph 1 | **पिंड** का अर्थ है स्वयं श्राद्ध करने वाले का शरीर, मन और बुद्धि। प्रत्येक जीव को पिंड ही कहा जाता है। | श्राद्ध में चावल के गोले को **पिंड** कहते हैं, पर आचार्य जी के अनुसार पिंड का गहरा अर्थ है स्वयं श्राद्ध करने वाले का शरीर, मन और बुद्धि। संस्कृत में पिंड शब्द शरीर के लिए भी आता है, इसीलिए प्रत्येक जीव को पिंड कहा जाता है। | Content trust: the symbolic reading was given as the definition, and a snippet for the focus keyword would misdefine the term (review issue 2, flag 2). Uses the review's own correction. |
| "सफेद चावल का पिंड क्या कहता है?", paragraph 1 | पिंड चावल का ही बनता है, | पिंड प्रायः चावल का बनता है, | Content trust: "ही" was too absolute, since barley flour is also used (review issue 3, flag 3). Uses the review's own correction. |
| "मुख्य बातें", last item | - कौवा पिंड खा ले तो पितर मुक्त हैं; न खाए तो वे अभी आसपास हैं। | - आचार्य जी के अनुसार, कौवा पिंड खा ले तो पितर मुक्त हो चुके हैं; न खाए तो वे अभी मुक्त नहीं हुए और आसपास हैं। | Content trust: Acharya Ji's own reading was stated as plain fact (review issue 1, flag 1). Uses the review's own correction. |

## English (`pind_daan_blog_seo_en.txt`): 5 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…why we do all this?") | (none) | In short, the pind daan meaning has two layers. A ball of rice, the pind, is offered to the ancestors. According to Acharya Upendra Ji, its deeper meaning is the performer's own body, mind and intellect, set free of inner impurities and desires and offered to God. The crow is nobody's ancestor; like dogs and cows, it senses whether the ancestors are present. | The focus keyword was missing from the body, and the whole intro already runs to 94 words. This direct answer (about 60 words, from the report's section 5) goes after the first paragraph, so "pind daan meaning" falls within the first 100 words. It avoids the link phrase "offer this pind to God". |
| First H2 | ## What Is a Pind? Your Body Is a Village Too | ## What Does Pind Daan Mean? Your Body Is a Village Too | Rephrased as the question readers search. The section answers it. The number and order of headings are unchanged. |
| "What Does the White Rice Pind Tell Us?", paragraph 1 | The pind is always made of rice, so it is white. | The pind is usually made of rice, so it is white. | Content trust: review issue 3, flag 3. Uses the review's own correction. |
| "Is the Crow Really Our Ancestor?", paragraph 1 | …some other departed relative. This is a mistaken belief. | …some other departed relative. | Content trust: a judgement that is not in the Hindi (review issue 4, flag 4). Deleted, as the review says. Acharya Ji's own statement follows in the next paragraph, unchanged. |
| "Key Takeaways", last item | - If the crow eats the pind, the ancestors are free; if it refuses, they are still lingering nearby. | - According to Acharya Ji, if the crow eats the pind, the ancestors are already free; if it refuses, they are not yet liberated and are still lingering nearby. | Content trust: review issue 1, flag 1. Uses the review's own correction. |

No teaching, example, H1 or order of ideas changed, and the Markdown is kept. The blog quotes no verses. grep confirms that all four `links` phrases in each language are still in the texts, once each. So is the `also_read` heading ("कौवा: एक संकेतक" / "The Crow as a Signal"). The inline image's Hindi heading ("सफेद चावल का पिंड क्या कहता है?") is unchanged.

## Checklist

- Now met:
  - Focus keyword in the body text and within the first 100 words, in both languages.
  - Focus keyword in the meta description, in both languages.
  - No unsupported scriptural claims: review issues 1–4 are applied in the `_seo` texts.
- `check_seo.py` now passes; it failed before.
- The report had no section 12. The checklist was added from `tools/prompts/seo_checklist.md` and marked.
- Still unmet: none.
- Left alone on purpose:
  - The crow H2 "कौवा: एक संकेतक" / "The Crow as a Signal" was not rephrased as a question, although report section 4 suggests it. It is the `also_read` heading and must stay word for word.
  - Report sections 1 and 10 still call review issues 1–4 "not yet applied". This fix may edit only sections 2, 3, 8, 11 and 12. In the published `_seo` texts, the issues are applied.
  - The original blog texts still carry the review issues, for the editor to fix.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | पिंडदान का वास्तविक अर्थ क्या है और कौवा कभी पिंड क्यों नहीं खाता? आचार्य उपेंद्र जी बताते हैं: पिंड आपका अपना शरीर, मन और बुद्धि है, और कौवा पितरों का संकेतक। | पिंडदान का अर्थ क्या है और कौवा कभी पिंड क्यों नहीं खाता? आचार्य उपेंद्र जी बताते हैं: पिंड आपका अपना शरीर, मन और बुद्धि है, और कौवा पितरों का संकेतक। (150) |
| wordpress.en.meta_description | What does pind daan really mean, and why does a crow sometimes refuse the pind? Acharya Upendra Ji explains the white rice pind and the crow as a signal. | What is the real pind daan meaning, and why does a crow at times refuse the pind? Acharya Upendra Ji explains the white rice pind and the crow as a signal. (155) |
| wordpress.hi.slug | pind-daan-ka-arth | pind-daan-ka-arth (unchanged; already fits the keyword) |
| wordpress.en.slug | pind-daan-meaning | pind-daan-meaning (unchanged; 17 characters, contains the keyword) |

These fields are unchanged: `focus_keyword` and `secondary_keywords` (the focus keywords were already the searched wording), `title` (both already contain the keyword), `links`, `also_read`, `alt`, `caption`, `related`, category and tags. The report's section 11 holds the same JSON. Sections 2 (keyword note), 3 (metas and slugs marked recommended) and 8 (schema descriptions) were updated to match, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | pind-daan-ka-arth | pind-daan-meaning |
| focus_keyword | पिंडदान का अर्थ | pind daan meaning |
| title | पिंडदान का अर्थ: कौवा पिंड क्यों खाता है, क्यों नहीं? | Pind Daan Meaning: Why the Crow Eats the Pind, or Refuses |
| meta_description | पिंडदान का अर्थ क्या है और कौवा कभी पिंड क्यों नहीं खाता? आचार्य उपेंद्र जी बताते हैं: पिंड आपका अपना शरीर, मन और बुद्धि है, और कौवा पितरों का संकेतक। | What is the real pind daan meaning, and why does a crow at times refuse the pind? Acharya Upendra Ji explains the white rice pind and the crow as a signal. |
