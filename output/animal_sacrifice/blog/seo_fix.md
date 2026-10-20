animal_sacrifice: SEO fix

The report had one unmet checklist item: "No unsupported scriptural claims", because the body carried Sanskrit review issues 1 and 2 (Major): the Gita 4.33 line given the speaker's meaning, and the opening claim stated as the Vedas' own words (flags 1–2). Section 2 also noted a mismatch: people search "पशुबलि का अर्थ" / "spiritual meaning of animal sacrifice", but the bodies only had "पशुबलि" / "animal sacrifice", and the direct answer ("no real animal is to be killed") came only near the end. Each language gets four changes: the review's corrections for issues 1 and 2, a short direct answer after the intro built only from what the blog already says, and one H2 rephrased as the searched question. The focus keywords move to the searched wording.

## Hindi (`animal_sacrifice_blog_seo.txt`): 4 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, paragraph 1, first sentence | वेदों में लिखा है कि जब तक पशुबलि नहीं होगी, तब तक युग परिवर्तन नहीं होगा, आत्म-जागरण नहीं होगा। | आचार्य जी बताते हैं कि वेदों में अग्निचयन की विधि में पशुबलि का विधान आता है, और उसके बिना वह यज्ञ, जिसे वे युग परिवर्तन और आत्म-जागरण से जोड़ते हैं, पूरा नहीं होता। | Content trust: the speaker's paraphrase was presented as the Vedas' words (review issue 2, flag 2). The review's own correction. "पशुबलि" stays in the first sentence. |
| Intro, new third paragraph (after "…हमारे भीतर मिलता है।") | (none) | संक्षेप में, आचार्य जी के अनुसार पशुबलि का अर्थ किसी निर्दोष प्राणी को मारना नहीं, अपने भीतर के पशु की बलि देना है। पशु शब्द पाश यानी बंधन से जुड़ा है: काम, क्रोध, लोभ, भय और क्रूरता जैसे गुण, जो हमें बाँधे रखते हैं। गीता ४.३३ जिस ज्ञानयज्ञ को श्रेष्ठ कहती है, उसी की अग्नि में यह पशु अर्पित होता है। | The opening asked its question without answering it early. A direct answer of 60 words, restating the blog's own sections (पशु यानी पाश, कौन सा यज्ञ, विधि का असली अर्थ) and the report's section 5, puts the searched wording "पशुबलि का अर्थ" (new focus keyword) in the first 100 words. "जुड़ा है" follows review issue 5 rather than claiming a derivation. |
| "हर कर्म अंत में ज्ञान बनता है", paragraph 1 | गीता निश्चित रूप से कहती है: हर कर्म अंततः ज्ञान में बदल जाता है। | गीता (४.३३) कहती है कि सम्पूर्ण कर्म ज्ञान में ही समाप्त होते हैं। आचार्य जी इसे जीवन के अनुभव पर भी लागू करते हैं: हर कर्म अंततः एक सीख बन जाता है। | Content trust: the speaker's application was given as the Gita's literal meaning (review issue 1, flag 1; marked "Please fix" in the review). The review's own correction; the examples that follow are unchanged. |
| H2 before "अब विधि साफ़ है।" | ## विधि का असली अर्थ | ## पशुबलि का अर्थ क्या है? | Rephrased as the question readers search (the video thumbnail's question). The section answers it: no real animal is to be killed, only the animal within. Number and order of headings unchanged. |

## English (`animal_sacrifice_blog_seo_en.txt`): 4 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, paragraph 1, first sentence | The Vedas declare that without animal sacrifice there can be no turning of the age and no awakening of the Self. | Acharya Ji points out that the Vedic procedure for the Agnichayana prescribes an animal sacrifice, and that without it the rite, which he links to the turning of the age and the awakening of the Self, is not complete. | Content trust: review issue 2, flag 2. The review's own correction. "animal sacrifice" stays in the first sentence. |
| Intro, new third paragraph (after "…but within us.") | (none) | In short, the spiritual meaning of animal sacrifice, as Acharya Ji explains it, is not killing an innocent creature but offering up the animal within. Pashu (animal) is linked to pasha (bondage): the lust, anger, greed, fear and cruelty that bind us. It is offered in the fire of jnana yajna, which Gita 4.33 places far above material offerings. | Direct answer of 59 words, built only from the blog's own sections and the report's section 5. The searched wording "spiritual meaning of animal sacrifice" (new focus keyword), which the body never used, now sits in the first 100 words. |
| "Every Action Turns into Knowledge", paragraph 1 | The Gita states it plainly: every action ultimately turns into knowledge. | The Gita (4.33) says that all action finds its completion in knowledge. Acharya Ji applies this to everyday experience too: every action ultimately becomes a lesson. | Content trust: review issue 1, flag 1. The review's own correction. |
| H2 before "Now the procedure becomes clear." | ## What the Procedure Really Means | ## What Is the Spiritual Meaning of Animal Sacrifice? | Rephrased as the searched question; the section answers it. Number and order of headings unchanged. |

No teaching, example, verse, translation, reference, H1 or order of ideas changed, and Markdown is kept. All five `links` phrases and the `also_read` heading ("क्या शास्त्र कोई स्वयं-सहायता की पुस्तक हैं?" / "Are the Scriptures Self-Help Books?") are still in both texts, each confirmed by grep. The inline image's heading ("सोने की तरह तपना" / "Refined Like Gold") is unchanged.

## Checklist

- Now met: "No unsupported scriptural claims". Review issues 1 and 2 (Major) are corrected with the review's wording in both languages.
- Improved: the focus keyword is now the searched wording in both languages, in the first 100 words (inside a direct answer of about 60 words) and in one question H2. This settles the mismatch noted in section 2.
- Already met and still met: every other item in section 12. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - Review issues 3–8 (Minor: other religions' scriptures, the asuri sampatti list, pashu "comes from" pasha, "yajna means fire", the विनाशकाले spelling, the Atman/inner sun wording) are not SEO items; they are left for the editor to fix in the original blog.
  - "कौन सा यज्ञ? कौन सा कुंड?" was not renamed "ज्ञानयज्ञ क्या है?" (report section 4, optional): the next H2 already asks about jnana yajna, and one question H2 per language is enough.
  - The report's sections 1 and 10 still describe the old focus keywords and call review issues 1–2 "not yet applied"; this fix may only edit sections 2, 3, 8, 11 and 12. For the published `_seo` texts, issues 1–2 are applied.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.focus_keyword | पशुबलि | पशुबलि का अर्थ |
| wordpress.hi.secondary_keywords | पशु बलि का अर्थ, पशुबलि का अर्थ, ज्ञानयज्ञ गीता ४.३३, भीतर का पशु | पशुबलि, पशु बलि का अर्थ, ज्ञानयज्ञ गीता ४.३३, भीतर का पशु |
| wordpress.hi.meta_description | वेदों में पशुबलि का क्या अर्थ है? आचार्य उपेंद्र जी बताते हैं: पशु यानी पाश, भीतर के काम-क्रोध का बंधन, और गीता ४.३३ में ज्ञानयज्ञ क्यों श्रेष्ठ है। | वेदों में पशुबलि का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं: पशु यानी पाश, भीतर के काम-क्रोध का बंधन, और गीता ४.३३ में ज्ञानयज्ञ क्यों श्रेष्ठ है। (148) |
| wordpress.hi.slug | pashu-bali-ka-arth | pashu-bali-ka-arth (unchanged; already fits the new keyword) |
| wordpress.en.focus_keyword | animal sacrifice | spiritual meaning of animal sacrifice |
| wordpress.en.secondary_keywords | spiritual meaning of animal sacrifice, pashu bali meaning, jnana yajna Bhagavad Gita 4.33, sacrifice the animal within | animal sacrifice, pashu bali meaning, jnana yajna Bhagavad Gita 4.33, sacrifice the animal within |
| wordpress.en.meta_description | What does animal sacrifice in the Vedas mean? Acharya Upendra Ji reads pashu as pasha, the bonds within, and shows why Gita 4.33 puts jnana yajna first. | What is the spiritual meaning of animal sacrifice? Acharya Upendra Ji reads pashu as pasha, the bonds within, offered in the jnana yajna of Gita 4.33. (150) |
| wordpress.en.slug | spiritual-meaning-of-animal-sacrifice | spiritual-meaning-of-animal-sacrifice (unchanged; 37 characters, contains the new keyword) |

`title` (both already contain the new keywords), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2, 3, 8 and 12 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | pashu-bali-ka-arth | spiritual-meaning-of-animal-sacrifice |
| focus_keyword | पशुबलि का अर्थ | spiritual meaning of animal sacrifice |
| title | पशुबलि का अर्थ क्या है? भीतर के पशु की आहुति | Spiritual Meaning of Animal Sacrifice: The Beast Within |
| meta_description | वेदों में पशुबलि का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं: पशु यानी पाश, भीतर के काम-क्रोध का बंधन, और गीता ४.३३ में ज्ञानयज्ञ क्यों श्रेष्ठ है। | What is the spiritual meaning of animal sacrifice? Acharya Upendra Ji reads pashu as pasha, the bonds within, offered in the jnana yajna of Gita 4.33. |
