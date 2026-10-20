spiritual_science_om_aum: SEO fix

The report had one unmet checklist item: the body credited the mouth-position reading of Om to "our scriptures" (flag 1, Sanskrit review issue 1). Section 2 also noted a mismatch: people search "ॐ में अ उ म का अर्थ" / "meaning of AUM", but neither body used those words. Each language gets two changes: a short direct answer, built only from what the blog already says, that brings in the searched wording, and the review's correction to the scripture sentence. The focus keywords move to the searched wording.

## Hindi (`spiritual_science_om_aum_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…हमारे अपने मुख से देते हैं।") | (none) | संक्षेप में, ॐ में अ उ म का अर्थ हमारे मुख से ही समझ आता है। मुख की तीन ही अवस्थाएँ हैं: खुला मुख "अ" देता है, आधा खुला "उ" और बंद मुख "म"। संसार के सारे शब्द इन्हीं तीन अवस्थाओं के भीतर आ जाते हैं, इसलिए अ, उ, म मिलकर उस ब्रह्म का प्रतीक हैं। | The opening asked "ॐ ही क्यों?" but did not answer it early. This adds a direct answer of about 50 words, restating the blog's own sections 2 and 3, and puts the searched wording (the new focus keyword) in the first 100 words. It keeps "अ उ म" without commas, as the H1 writes it, so it matches the query. |
| "मुख की केवल तीन अवस्थाएँ", paragraph 3 | ध्वनि-चिकित्सा (sound therapy) के जानकार और हमारा शास्त्र, जो स्वयं एक विज्ञान है, दोनों यही कहते हैं। | ध्वनि-चिकित्सा (sound therapy) के जानकार भी यही कहते हैं, और हमारा शास्त्र, जो स्वयं एक विज्ञान है, ॐ को अ, उ, म इन तीन मात्राओं से बना मानता है। | Content trust: no scripture teaches the open/half-open/closed reading. The new wording is the Sanskrit review's own correction (issue 1). The link phrase "हमारा शास्त्र, जो स्वयं एक विज्ञान है" stays word for word. |

## English (`spiritual_science_om_aum_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…our own mouth.") | (none) | In short, the meaning of AUM begins in the mouth. The mouth has only three positions: open, it gives "A"; half open, "U"; closed, "M". Every word in the world falls within these three positions, so A, U and M together stand for Brahman, the Absolute. | Adds a direct answer of about 48 words, restating the blog's own sections 2 and 3. The searched wording "meaning of AUM" (the new focus keyword), which the body never used, now sits in the first 100 words. |
| "The Mouth Has Just Three Positions", paragraph 3 | Experts in sound therapy agree, and so do our scriptures, which are a science in their own right. | Experts in sound therapy agree, and our scriptures, which are a science in their own right, also describe Om as made of the three matras A, U and M. | Content trust: this is the Sanskrit review's correction (issue 1). The link phrase "our scriptures, which are a science in their own right" is kept word for word. |

No teaching, example, H1, heading or order of ideas changed. The blog quotes no verses. All five `links` phrases and the `also_read` heading are still in both texts, each found by grep.

## Checklist

- Now met: "No unsupported scriptural claims". The scripture sentence now follows the review's wording in both languages.
- Improved: the focus keyword is now the searched query in both languages. It appears in the first 100 words, inside an early direct answer of 40 to 60 words. This settles the mismatch flagged in section 2.
- Already met and still met: every other item in section 12. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - No heading was rephrased as a question. The best candidate, "अ + उ + म = ॐ" / "A + U + M = Om", is the heading that `images.txt` uses to place inline.jpg, and this fix may not change `images.txt`. The page already has one question H2 ("क्या गाली भी ब्रह्म है?" / "Is Even an Insult Brahman?"), which is the `also_read` anchor and has to stay.
  - The searched wording was not added again later. In Hindi, the natural spot ("अ, उ, म का वास्तविक अर्थ है") would need "वास्तविक" dropped to match exactly, so it was left as is.
  - Sanskrit review issue 2 (म called a स्वर) and issue 3 (the dharma gloss) are not SEO items. They are left for the editor to fix in the original blog.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | ॐ ही क्यों? अ, उ, म में छिपा पूरा ब्रह्मांड | ॐ में अ उ म का अर्थ: ॐ ही क्यों चुना गया (40) |
| title.en | Why Om? What the Three Sounds A, U and M Mean | Meaning of AUM: Why Om, and What A, U and M Stand For (53) |
| wordpress.hi.slug | om-hi-kyon-a-u-m | om-mein-a-u-m-ka-arth |
| wordpress.hi.focus_keyword | ॐ ही क्यों | ॐ में अ उ म का अर्थ |
| wordpress.hi.secondary_keywords | ॐ में अ उ म का अर्थ, ॐ का अर्थ क्या है, ओंकार का रहस्य, ॐ और ब्रह्म | ॐ ही क्यों, ॐ का अर्थ क्या है, ओंकार का रहस्य, ॐ और ब्रह्म |
| wordpress.hi.meta_description | ॐ ही क्यों, कोई और ध्वनि क्यों नहीं? आचार्य उपेंद्र जी समझाते हैं कि मुख की तीन अवस्थाएँ अ, उ, म देती हैं, और क्यों संसार का हर शब्द ॐ में समाया है। | ॐ में अ उ म का अर्थ क्या है, और ॐ ही क्यों? आचार्य उपेंद्र जी समझाते हैं कि मुख की तीन अवस्थाएँ अ, उ, म देती हैं, और संसार का हर शब्द ॐ में समाया है। (149) |
| wordpress.en.slug | why-om-meaning-of-a-u-m | meaning-of-aum-why-om |
| wordpress.en.focus_keyword | why Om | meaning of AUM |
| wordpress.en.secondary_keywords | meaning of AUM, what does Om mean, why do we chant Om, Om and Brahman | why Om, what does Om mean, why do we chant Om, Om and Brahman |
| wordpress.en.meta_description | Why Om and not another sound? Acharya Upendra Ji shows how the open, half-open and closed mouth give A, U and M, and why every word lies within Om. | What is the meaning of AUM, and why Om and not another sound? Acharya Upendra Ji shows how the open, half-open and closed mouth give A, U and M. (144) |

`links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON. Section 2's keyword table and note, and the section 12 checklist mark, were updated to match.

Note: the report's sections 3 and 8 (titles, slugs and schema) still show the old titles and slugs. This fix may only edit sections 2, 11 and 12. Use seo.json for the WordPress values.
