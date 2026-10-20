big_pitru_dosh_understanding_pitru_rin: SEO fix

The report's checklist had one unmet item: the focus keyword "पितृ दोष" / "pitru dosh" was not in the first 100 words (it first appeared in the second section). Section 2 also noted that the searched question form "पितृ दोष क्या है" / "what is pitru dosh" never appeared in the body, and the opening asked whether one shraddha is enough without giving a short answer. The fix adds the report's section 5 direct answer after the H1, led by the searched question, and turns one H2 into the question its section answers (section 4's suggestion). The direct answer uses only what the blog already says (sections "पितृ दोष और पितृ लाभ", "सात पीढ़ियों का वृक्ष", "पिछले जन्म के पितर भी आपके ही हैं", "उनचास गुना भार" and their English versions), attributed to Acharya Ji. The focus keywords now use the searched wording.

## Hindi (`big_pitru_dosh_understanding_pitru_rin_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the H1 (new paragraph) | (none) | पितृ दोष क्या है? आचार्य जी के अनुसार पितृ दोष पूर्वजों के कर्मों से आया बोझ है, और पितृ ऋण वह कर्ज़ है जो पूर्वजों के प्रति हम पर है। हर मनुष्य पर माता और पिता दोनों ओर की सात पीढ़ियों और पिछले सात जन्मों के पितरों का कर्म आता है। इसीलिए एक बार का श्राद्ध पर्याप्त नहीं होता। | Puts the searched wording and the focus keyword in the first 100 words; a direct answer (about 59 words) built only from the blog's own sections. Worded so it does not repeat the `links` phrase "पूर्वजों के प्रति हमारा कर्ज़", which stays in its section |
| Second H2 | ## पितृ दोष और पितृ लाभ: दोनों सच हैं | ## पितृ दोष, पितृ ऋण और पितृ लाभ में क्या अंतर है? | The section explains all three; this is the question readers search (secondary keyword "पितृ दोष और पितृ ऋण में अंतर"; section 4's suggestion) |

## English (`big_pitru_dosh_understanding_pitru_rin_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the H1 (new paragraph) | (none) | What is pitru dosh? According to Acharya Ji, pitru dosh is the burden carried over from the deeds of one's ancestors, while pitru rin is the debt we owe them. Every person carries the karma of seven generations, on both the mother's and the father's side, across seven lifetimes. That is why a single shraddha is not enough. | Puts the searched wording and the focus keyword in the first 100 words; a direct answer (about 58 words) built only from the blog's own sections. Worded so it does not repeat the `links` phrase "the debt we owe our ancestors", which stays in its section |
| Second H2 | ## Ancestral Burden and Ancestral Blessing: Both Are Real | ## Pitru Dosh, Pitru Rin and Pitru Labh: What Is the Difference? | The section explains all three; this is the question readers search (secondary keyword "pitru dosh vs pitru rin"; section 4's suggestion) |

No teaching, example, H1 or order of ideas was changed (the blog quotes no verses), and the number and order of headings are the same. All five `links` phrases and the `also_read` heading ("मुक्त भी आपको ही करना है" / "Freeing Them Is Your Task") are still in both texts, word for word. The inline image's section ("सात पीढ़ियों का वृक्ष" / "A Tree Seven Generations Tall") is unchanged. The Sanskrit review's corrections (tools/review: the names attributed to "शास्त्र", the shraddha gloss, spellings, "गुरुदेव") change the teaching's wording, so they are left to the editor and were not applied here.

## Checklist

- Now met: "Within the first 100 words": the focus keyword opens the new direct answer in both languages. The searched question form (section 2's mismatch) is now in the body and is the focus keyword, in the title, meta description and English slug. The text gives a direct answer early, and one H2 is now a question.
- Already met and still met: every other item in section 12.
- Still unmet: none. (Outside the checklist, the review's open issues listed above remain for the editor.)

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | पितृ दोष कितना गहरा है? सात पीढ़ी, सात जन्म और पितृ ऋण | पितृ दोष क्या है? सात पीढ़ी, सात जन्म और पितृ ऋण (48) |
| title.en | Pitru Dosh: Ancestral Karma Across Seven Lifetimes | What Is Pitru Dosh? Ancestral Karma Across Seven Lifetimes (58) |
| wordpress.hi.slug | pitru-dosh-saat-peedhi-saat-janm | pitru-dosh-kya-hai |
| wordpress.hi.focus_keyword | पितृ दोष | पितृ दोष क्या है |
| wordpress.hi.secondary_keywords | पितृ दोष क्या है, पितृ दोष और पितृ ऋण में अंतर, हर साल श्राद्ध क्यों करें, सात पीढ़ी के पितर | पितृ दोष, पितृ दोष और पितृ ऋण में अंतर, हर साल श्राद्ध क्यों करें, सात पीढ़ी के पितर |
| wordpress.hi.meta_description | (unchanged; already contains "पितृ दोष क्या है") | (unchanged) |
| wordpress.en.slug | pitru-dosh-seven-lifetimes | what-is-pitru-dosh |
| wordpress.en.focus_keyword | pitru dosh | what is pitru dosh |
| wordpress.en.secondary_keywords | what is pitru dosh, pitru dosh vs pitru rin, ancestral karma, seven generations of ancestors | pitru dosh, pitru dosh vs pitru rin, ancestral karma, seven generations of ancestors |
| wordpress.en.meta_description | (unchanged; already contains "What is pitru dosh") | (unchanged) |

The old focus keywords "पितृ दोष" / "pitru dosh" are broad, high-priority terms used throughout the body, so they took the new focus keywords' place in `secondary_keywords` (still 4 per language). The new focus keywords and slugs are not used by any other talk. The titles changed to the report's option 2, which contains the new focus keyword. `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in sections 2, 3, 8 (alternativeHeadline, keywords and the URL slugs line; headline and description are unchanged), 11 and 12.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | pitru-dosh-kya-hai | what-is-pitru-dosh |
| focus_keyword | पितृ दोष क्या है | what is pitru dosh |
| title | पितृ दोष क्या है? सात पीढ़ी, सात जन्म और पितृ ऋण | What Is Pitru Dosh? Ancestral Karma Across Seven Lifetimes |
| meta_description | पितृ दोष क्या है और एक बार का श्राद्ध काफ़ी क्यों नहीं? आचार्य उपेंद्र जी समझाते हैं पितृ ऋण, पितृ लाभ और सात पीढ़ियों व सात जन्मों के पितरों का कर्म। | What is pitru dosh, and why is one shraddha not enough? Acharya Upendra Ji explains pitru rin and the karma of seven generations across seven lifetimes. |
