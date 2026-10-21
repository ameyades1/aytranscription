sattva_rajas_tamas_balance_success_liberation: SEO fix

The check failed before the fix: neither focus keyword was in the blog body. The Hindi body only wrote "सत्व, रज और तम" (with commas, which the exact Hindi match does not accept) and never used "संतुलन", and the Hindi meta description had the same comma form. In English, SureRank's matching cannot find "balance of sattva rajas and tamas" across the commas of "Sattva, Rajas and Tamas", so it was missing from the title tag, the meta description and the body, and it was not in the slug; the English body never spoke of balance. The opening also gave no direct answer (report sections 4 and 5). The fix adds a short direct-answer paragraph after the intro in each language, built only from what the blog already says (the three gunas as cords of maya, "सत्वगुण भी बाँधता है" / "even sattva binds", the rajas / sattva / tamas list, "the right guna must lead at the right time" and liberation as the goal). It uses the focus keyword in the first 100 words, and it rephrases the first H2 as the question readers search for. The English focus keyword becomes the searched wording "balance the three gunas", with a new title tag, meta description and slug; the Hindi meta description now uses "सत्व रज तम का संतुलन" without commas. The report had no section 12, so the checklist was added.

## Hindi (`sattva_rajas_tamas_balance_success_liberation_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro ("…पूरी दृष्टि बदल देता है।"), new paragraph | (none) | संक्षेप में, तीनों गुण माया की डोरियाँ हैं, और सत्वगुण भी बाँधता है। फिर भी जीवन के लिए तीनों आवश्यक हैं: कर्म के लिए रजोगुण, ज्ञान के लिए सत्वगुण और विश्राम के लिए तमोगुण। सत्व रज तम का संतुलन यही है कि सही समय पर सही गुण प्रधान हो; पर लक्ष्य मुक्ति ही है। | Focus keyword in the body and the first 100 words (word 80). A direct answer early (about 48 words), taken from the blog's own sections and Key Takeaways and section 5's snippet; it avoids the `links` phrases |
| First H2 | ## गुण यानी विशेषता? या कुछ और? | ## गुण का अर्थ क्या है: विशेषता या डोरी? | The section answers this searched question ("गुण का अर्थ डोरी", FAQ 1) |

## English (`sattva_rajas_tamas_balance_success_liberation_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro ("…the whole teaching."), new paragraph | (none) | In short, the three gunas are cords of maya, and even sattva binds. Yet life needs all three: rajas to act, sattva to gain knowledge and tamas to rest. To balance the three gunas is to let the right guna lead at the right time, while the goal remains liberation. | New focus keyword in the body and the first 100 words (word 81). A direct answer early (about 50 words), from the blog's own sections and section 5's snippet; it avoids the `links` phrases |
| First H2 | ## Does Guna Mean a Quality, or Something Else? | ## What Does Guna Mean: a Quality or a Cord? | The section answers this searched question ("meaning of guna", FAQ 1) |

No teaching, example, order of ideas or H1 was changed (the talk quotes no verses), and the number and order of headings are the same. Section 4's other suggestion (turning "तो क्या तीनों गुण छोड़ दें?" / "Should You Give Up All Three Gunas, Then?" into a "how to balance" question) was not used: the section opens with "नहीं।" / "No.", which answers the current question, so the change would break the text. "तीन देवियाँ, तीन रंग" / "Three Goddesses, Three Colours" is untouched (the `also_read` heading and the place `images.txt` gives `inline.jpg`). All five `links` phrases and the `also_read` heading are still in both texts, word for word. The Sanskrit review's minor corrections (Kali's complexion, the Maha- forms, सत्त्व) change the talk's wording beyond SEO, so they are left to the editor (section 10).

## Checklist

- Now met: the focus keyword is in the body text and within the first 100 words in both languages, in both meta descriptions, and (English) in the title tag and slug. "Focus keyword taken from wording the article already uses" is met for the `_seo` texts. `check_seo.py` passes, where it failed before. Both texts give a direct answer early, and one H2 per language is now a searched question.
- Already met and still met: every other item in section 12 (added to the report by this fix, all items marked).
- Still unmet: none.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Balance of Sattva, Rajas and Tamas: Three Cords That Bind | How to Balance the Three Gunas: Three Cords That Bind (53) |
| wordpress.en.focus_keyword | balance of sattva rajas and tamas | balance the three gunas |
| wordpress.en.secondary_keywords | what are sattva rajas and tamas, meaning of guna, does sattva also bind | balance of sattva rajas and tamas, what are sattva rajas and tamas, meaning of guna, does sattva also bind |
| wordpress.en.slug | sattva-rajas-tamas-balance | balance-the-three-gunas (23 characters, unique) |
| wordpress.en.meta_description | Guna means cord: sattva, rajas and tamas are the cords of maya. Acharya Upendra Ji explains why even sattva binds and how to balance all three each day. | Guna means cord: sattva, rajas and tamas are the cords of maya. Acharya Upendra Ji explains why even sattva binds and how to balance the three gunas daily. (155) |
| wordpress.hi.meta_description | संस्कृत में गुण का अर्थ है डोरी। आचार्य उपेंद्र जी समझाते हैं कि सत्वगुण भी क्यों बाँधता है, और जीवन में सत्व, रज और तम का संतुलन कैसे साधें। | संस्कृत में गुण का अर्थ है डोरी। आचार्य उपेंद्र जी समझाते हैं कि सत्वगुण भी क्यों बाँधता है, और जीवन में सत्व रज तम का संतुलन कैसे साधें। (137) |
| wordpress.hi.slug | sattva-rajas-tamas-santulan | sattva-rajas-tamas-santulan (unchanged) |
| wordpress.hi.focus_keyword | सत्व रज तम का संतुलन | unchanged (now in the `_seo` body) |
| title.hi | सत्व रज तम का संतुलन: तीन डोरियाँ जो बाँधती भी हैं | unchanged (already contains the focus keyword) |

No other talk uses either focus keyword or the new slug. `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in section 2 (the new keyword row and the mismatch note), section 3 (the English title, both meta descriptions and both slugs in seo.json marked recommended), section 8 (Hindi and English description, English alternativeHeadline, keywords and suggested slugs; the headlines are the unchanged H1s) and section 11, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sattva-rajas-tamas-santulan | balance-the-three-gunas |
| focus_keyword | सत्व रज तम का संतुलन | balance the three gunas |
| title | सत्व रज तम का संतुलन: तीन डोरियाँ जो बाँधती भी हैं | How to Balance the Three Gunas: Three Cords That Bind |
| meta_description | संस्कृत में गुण का अर्थ है डोरी। आचार्य उपेंद्र जी समझाते हैं कि सत्वगुण भी क्यों बाँधता है, और जीवन में सत्व रज तम का संतुलन कैसे साधें। | Guna means cord: sattva, rajas and tamas are the cords of maya. Acharya Upendra Ji explains why even sattva binds and how to balance the three gunas daily. |
