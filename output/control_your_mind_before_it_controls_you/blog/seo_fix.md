control_your_mind_before_it_controls_you: SEO fix

The check failed before the fix: the Hindi focus keyword "मन को वश में कैसे करें" was in neither the body nor the meta description, and the English focus keyword "how to control the mind Bhagavad Gita" was in none of the title, meta description, body or slug (report sections 4 and 5 noted that neither keyword was in the first 100 words). Each language now has a short direct answer after the two opening paragraphs, built only from what the blog already says (entertainment is not forbidden; true control is withdrawing the mind as easily as it settles in, when a higher duty arrives; Gita 18.33's sattvic dhriti, the unwavering power of holding firm). It carries the focus keyword within the first 100 words. The English focus keyword is now "how to control your mind", the wording the English title and the new paragraph already use; the old one moves to the secondary keywords.

## Hindi (`control_your_mind_before_it_controls_you_blog_seo.txt`): 1 change

| Where | Before | After | Why |
|---|---|---|---|
| After the opening, new paragraph | (none) | संक्षेप में, मन को वश में कैसे करें? आचार्य जी के अनुसार इसका अर्थ मनोरंजन छोड़ना नहीं है। मन जितनी आसानी से किसी चीज़ में लगे, ऊँचा कर्तव्य आने पर उतनी ही आसानी से वहाँ से हट भी सके, यही सच्चा नियंत्रण है। इसका आधार वह है जिसे गीता (१८.३३) सात्त्विक धृति कहती है: कभी न डगमगाने वाली धारणा शक्ति। | Focus keyword (absent from the body) in the first 100 words; direct answer (report section 5, 60 words), using only what the blog says. |

## English (`control_your_mind_before_it_controls_you_blog_seo_en.txt`): 1 change

| Where | Before | After | Why |
|---|---|---|---|
| After the opening, new paragraph | (none) | In short, Acharya Ji teaches that learning how to control your mind does not mean giving up entertainment. It means being able to pull your mind out of something as easily as it settles into it, the moment a higher duty arrives. This rests on what the Bhagavad Gita (18.33) calls sattvic dhriti, the unwavering power of holding firm. | New focus keyword "how to control your mind" in the body and the first 100 words; direct answer (report section 5, 59 words), using only what the blog says. |

No teaching, example, verse, translation, H1, heading or order of ideas changed. Headings were not rephrased: each language already has two question H2s ("क्या धारावाहिक देखना गलत है?", "मन मालिक, तुम गुलाम?" / "Is It Wrong to Watch a TV Serial?", "Is Your Mind the Master and You the Slave?"). Report section 4's suggested "सात्त्विक धृति क्या है?" / "What Is Sattvic Dhriti?" heading was not applied: images.txt places inline.jpg by the "सात्त्विक बुद्धि: पहले चुनाव, फिर एकाग्रता" heading, and changing "buddhi" to "dhriti" in it would shift what the section says (review issue 3). Its optional extra H2 was not added, to keep the number of headings. All five `links` phrases and the `also_read` heading ("रंजन से ऊपर रक्षण" / "Protection Comes Before Entertainment") are unchanged and still found by the page build.

## Checklist

- Now met:
  - Focus keyword in the body text and the meta description (both languages), and in the English title and URL slug. `check_seo.py` failed on these before; it now passes.
  - Focus keyword within the first 100 words (both languages).
  - Focus keyword taken from wording the article uses: the `_seo` texts now contain it.
  - A direct answer (40-60 words) early on.
- Section 12 was missing from the report; it has been added, with every item met.
- Still unmet: none.
- Left alone on purpose: Sanskrit review issues 1-5 (missing "पार्थ" in the Hindi verse meaning, the cryptic Shukra wording, the optional 18.30 line, the "pravritti" gloss, the English gloss in the Hindi text) and the editorial notes ("जितना आसानी से", the repeated Vishnu paragraph, "क्वालिटी") are verse-translation or wording points, not SEO items; they are left for the editor to fix in the original blog.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या अध्यात्म में मनोरंजन वर्जित है? आचार्य उपेंद्र जी गीता १८.३३ की सात्त्विक धृति से बताते हैं: जितनी आसानी से मन लगे, उतनी आसानी से हटे, यही नियंत्रण है। | मन को वश में कैसे करें? आचार्य उपेंद्र जी गीता १८.३३ की सात्त्विक धृति से बताते हैं: जितनी आसानी से मन लगे, उतनी आसानी से हटे, यही सच्चा नियंत्रण है। (149) |
| wordpress.en.focus_keyword | how to control the mind Bhagavad Gita | how to control your mind |
| wordpress.en.secondary_keywords | sattvic dhriti meaning; Bhagavad Gita 18.33 meaning; is watching TV bad for spiritual life; mind is the master | how to control the mind Bhagavad Gita; sattvic dhriti meaning; Bhagavad Gita 18.33 meaning; is watching TV bad for spiritual life |
| wordpress.en.slug | control-your-mind-bhagavad-gita | how-to-control-your-mind-bhagavad-gita |
| wordpress.en.meta_description | Spiritual life need not mean giving up entertainment. Acharya Upendra Ji on sattvic dhriti, Gita 18.33: pull your mind out as easily as it settles in. | How to control your mind without giving up entertainment: Acharya Upendra Ji on sattvic dhriti, Gita 18.33. Pull it out as easily as it settles in. (147) |

The Hindi focus keyword (kept: the body now uses it), Hindi secondary keywords, both titles (both already contain the focus keyword), the Hindi slug (`man-ko-vash-mein-kaise-karein`), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2 (keyword note and the new keyword row), 3 (recommended meta descriptions and slugs), 8 (descriptions, English keywords and suggested English slug) and 12 (checklist, newly added) were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | man-ko-vash-mein-kaise-karein | how-to-control-your-mind-bhagavad-gita |
| focus_keyword | मन को वश में कैसे करें | how to control your mind |
| title | मन को वश में कैसे करें? गीता की सात्त्विक धृति | How to Control Your Mind: Sattvic Dhriti in the Gita |
| meta_description | मन को वश में कैसे करें? आचार्य उपेंद्र जी गीता १८.३३ की सात्त्विक धृति से बताते हैं: जितनी आसानी से मन लगे, उतनी आसानी से हटे, यही सच्चा नियंत्रण है। | How to control your mind without giving up entertainment: Acharya Upendra Ji on sattvic dhriti, Gita 18.33. Pull it out as easily as it settles in. |
