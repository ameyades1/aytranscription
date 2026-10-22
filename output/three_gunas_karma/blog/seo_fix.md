three_gunas_karma: SEO fix

Fixed copies: `output/three_gunas_karma/three_gunas_karma_blog_seo.txt` (Hindi) and `output/three_gunas_karma/three_gunas_karma_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| "क्या सचमुच मैं ही कर्ता हूँ?", new 2nd paragraph | (none) | त्रिगुण और कर्म का संबंध यह है: हर मनुष्य में किसी क्षण सत्व, रज या तम में से एक गुण प्रबल होता है, हर स्थान और वस्तु का भी अपना गुण होता है, और दोनों के मेल से कर्म होता है। भगवद्गीता (३.२७) कहती है कि सारे कर्म प्रकृति के गुणों द्वारा होते हैं, पर अहंकार से मोहित मनुष्य स्वयं को कर्ता मानता है। | The focus keyword "त्रिगुण और कर्म" was not in the body (SureRank error) or the first 100 words, and there was no early direct answer. Built only from the blog's own sentences (gunas dominating, every place's guna, the meeting, Gita 3.27 as the blog renders it). |
| 2nd H2 | ## गुणों का मेल ही कर्म बनाता है | ## कर्म कौन करवाता है? | Question heading matching the secondary keyword "कर्म कौन करवाता है"; the section answers it (the meeting of gunas, Gita 3.27). |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| "Am I Really the Doer?", new 2nd paragraph | (none) | The three gunas and human behaviour are linked like this: at any moment one guna dominates each of us, each place and object has its own quality too, and action arises when the two meet. The Bhagavad Gita (3.27) says every action is carried out by the gunas of nature, yet the ego-deluded person believes, "I am the doer." | The focus keyword "three gunas and human behaviour" was not in the body (SureRank error) or the first 100 words, and there was no early direct answer (59 words). Built only from what the blog already says. |
| 2nd H2 | ## When Qualities Meet, Action Follows | ## How Do the Gunas Influence Our Actions? | Question heading matching the secondary keyword "how gunas influence our actions"; the section answers it. |

Headings keep their number and order; the H1, the verse, its translation and reference, every link phrase and the Also read headings are unchanged.

## Checklist

Now met (they were failing before the fix):
- Focus keyword in the body text (both languages)
- Focus keyword in the meta description (both languages)
- Focus keyword in the URL slug (English)
- Focus keyword within the first 100 words (both languages)
- Focus keyword taken from wording the article uses (the published `_seo` text)
- Direct answer paragraph early in the post; question-style H2s

Still unmet:
- Each tag can be shared by at least 3 posts: "कर्तापन" / "Doership" is used by only 2 posts so far. Tags are outside this fix's scope.
- No unsupported scriptural claims: the Sanskrit review's minor flags (Gita 3.27 placed after Acharya Ji's "inner guna meets outer guna" wording in the Key Takeaways; the pitar takeaway not attributed to Acharya Ji) are not applied. They are content corrections, not SEO edits.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | three-gunas-human-behaviour | three-gunas-and-human-behaviour |
| wordpress.en.meta_description | Do you act, or does nature act through you? Acharya Upendra Ji shows how the gunas within you meet the gunas of a place to shape what you do (Gita 3.27). | Three gunas and human behaviour: Acharya Upendra Ji explains Gita 3.27 and shows how the gunas within you meet the gunas of a place to shape what you do. |
| wordpress.hi.meta_description | क्या कर्म सच में आप करते हैं? आचार्य उपेंद्र जी गीता ३.२७ और गोवा तट व मदिरालय के उदाहरणों से समझाते हैं कि भीतर और बाहर के गुणों का मेल ही कर्म बनाता है। | त्रिगुण और कर्म: क्या कर्म आप करते हैं? आचार्य उपेंद्र जी गीता ३.२७ और गोवा तट व मदिरालय के उदाहरणों से बताते हैं कि भीतर-बाहर के गुणों का मेल कर्म बनाता है। |

Unchanged: the Hindi slug (`trigun-aur-karma`), both focus keywords, secondary keywords, titles, links, also_read, related, category and tags.

The report's sections 2, 3, 8 and 11 were updated to match, and section 12 (the SEO checklist, missing before) was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | trigun-aur-karma | three-gunas-and-human-behaviour |
| focus_keyword | त्रिगुण और कर्म | three gunas and human behaviour |
| title | त्रिगुण और कर्म: कर्म आप करते हैं या प्रकृति करवाती है? | Three Gunas and Human Behaviour: Who Really Acts? |
| meta_description | त्रिगुण और कर्म: क्या कर्म आप करते हैं? आचार्य उपेंद्र जी गीता ३.२७ और गोवा तट व मदिरालय के उदाहरणों से बताते हैं कि भीतर-बाहर के गुणों का मेल कर्म बनाता है। | Three gunas and human behaviour: Acharya Upendra Ji explains Gita 3.27 and shows how the gunas within you meet the gunas of a place to shape what you do. |
