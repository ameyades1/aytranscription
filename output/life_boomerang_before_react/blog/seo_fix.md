life_boomerang_before_react: SEO fix

`check_seo.py` failed on the original texts. The Hindi focus keyword "ये यथा मां प्रपद्यन्ते का अर्थ" was in neither the body (only the verse itself was) nor the meta description (which wrapped the verse words in quotes). The English focus keyword "Bhagavad Gita 4.11 meaning" was in neither the body nor the meta description, and could never be in the slug: SureRank reads the slug's hyphens as spaces, so "4.11" never matches `4-11`. Neither opening answered its own question ("does this simply mean tit for tat?") early. The report also listed unapplied Sanskrit review corrections (flags 1–6). Each language gets a direct answer after the opening question (with the focus keyword in the first 100 words), one H2 with "before you react" from the video title, and the review's text-only corrections. The English focus keyword moves to "does God take revenge", which the talk answers directly and which was already in the title, meta description and an H2.

## Hindi (`life_boomerang_before_react_blog_seo.txt`): 7 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…इसी प्रश्न की गहराई खुलती है।") | (none) | संक्षेप में, आचार्य जी के अनुसार ये यथा मां प्रपद्यन्ते का अर्थ केवल जैसे को तैसा नहीं है। जो भाषा हमें समझ आती है, भगवान वही भाषा बोलते हैं; उनका बाहरी स्वरूप हमारे व्यवहार जैसा हो सकता है, पर भाव सदा हमारे उद्धार का होता है। कहाँ प्रतिक्रिया देनी है और कहाँ चुप रहना है, यह बोध गणपति देते हैं। | Direct answer (about 60 words) built only from the blog's own sections ("क्या भगवान बदला लेते हैं?", "कहाँ चिल्लाना था…"). Puts the focus keyword word for word in the body, within the first 100 words. It says "केवल … नहीं" because the blog keeps reciprocity as the first meaning. |
| H2, second section | ## कहाँ चिल्लाना था, कहाँ चुप रहना था? | ## प्रतिक्रिया देने से पहले: कहाँ बोलें, कहाँ चुप रहें? | Report section 4's suggestion: matches the video title and the secondary keyword "प्रतिक्रिया देने से पहले क्या करें". The section answers it. Number and order of headings unchanged. |
| "पहले क्षण में गुरु अच्छे नहीं लगते", paragraph 2 | अर्जुन को भी पहले कृष्ण अच्छे नहीं लगते; | अर्जुन को भी पहले कृष्ण का उपदेश कठोर लगता है; | Content trust: the Gita does not say Arjuna disliked Krishna (Sanskrit review issue 3, flag 3). The review's own wording. |
| "दुर्गा देवी…", paragraph 1 | दुर्गा देवी युद्ध करती हैं, फिर शस्त्र | आचार्य जी इस प्रसंग को इस भाव से सुनाते हैं: दुर्गा देवी शुम्भ से युद्ध करती हैं, फिर शस्त्र | Content trust: the dialogue was told as the Saptashati's own account (review issue 1, Major, flag 1). The review's attribution, and the demon named. This frames issue 2 too, as the review allows. |
| "आरती में छिपा हुआ रहस्य", paragraph 1 | पर क्या यह भाव कभी पढ़ा? | पर क्या उसकी करुणा का भाव कभी समझा? | Content trust: the aarti has no line about weapons used for the enemy's uplift (review issue 8, flag 6). The review's wording. |
| "माँ का भाव…", paragraph 1 | आचार्य जी कहते हैं कि कर्म करो और फल का हठ छोड़ दो। | आचार्य जी कहते हैं कि कर्म करो और फल का हठ छोड़ दो। उपनिषद् माँ को देवता के समान मानने को कहता है: | Content trust: without a bridge, the Taittiriya mantra read as if it taught फल-त्याग (review issue 6, flag 5). The review's sentence; the verse is untouched and the link phrase is kept. |
| Key takeaway 3 | जैसे अर्जुन को कृष्ण और | जैसे अर्जुन को कृष्ण का उपदेश और | Same correction as the body (review issue 3). |

## English (`life_boomerang_before_react_blog_seo_en.txt`): 8 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…explores that question in depth.") | (none) | So does God take revenge? No. Acharya Ji teaches that Bhagavad Gita 4.11 means more than tit for tat. God speaks whatever language we understand, and His outward form may mirror our behaviour, but His intent is always our uplift and liberation. When to respond and when to stay silent is decided by discernment, which Lord Ganesha grants. | Direct answer (57 words) built only from the blog's own sections and report section 5. Puts the new focus keyword "does God take revenge" in the first 100 words. |
| H2, second section | ## When to Raise Your Voice, When to Stay Silent | ## Before You React: When to Raise Your Voice, When to Stay Silent? | The video title's wording and the secondary keyword "pause before you react", asked as the reader's question; the section answers it. Number and order of headings unchanged. |
| "Why the Guru Feels Harsh at First", paragraph 2 | Even Arjuna does not like Shri Krishna at first, with all his conditions: | Even Arjuna at first finds Shri Krishna's teaching hard to accept, with all its conditions: | Review issue 3, flag 3. The review's wording. |
| "Maa Durga…", paragraph 1 | Maa Durga fights the demon, then throws | Acharya Ji tells the episode in this way: Maa Durga fights the demon Shumbha, then throws | Review issue 1 (Major), flag 1. The review's attribution and the demon's name. |
| "The Secret Hidden in the Aarti", paragraph 1 | But have we ever read the feeling behind it? | But have we ever understood the compassion behind it? | Review issue 8, flag 6. The review's wording. |
| "A Mother's Way…", paragraph 1 | Acharya Ji says: act, and let go of your insistence on the fruit. | Acharya Ji says: act, and let go of your insistence on the fruit. The Upanishad asks us to regard the mother as God: | Review issue 6, flag 5. The review's bridge; link phrase kept. |
| "A Mother's Way…", last paragraph | The scriptures call this the highest state. | This is said to be the highest state. | Review issue 7, flag 5: the English named "the scriptures" as the source while the Hindi names none. Now matches the Hindi; no new citation added. |
| Key takeaway 3 | as Shri Krishna did to Arjuna | as Shri Krishna's teaching did to Arjuna | The review's wording for the takeaway (issue 3). |

No teaching, example, verse, translation, reference, H1 or order of ideas was changed, and the Markdown is kept. All four `links` phrases and the `also_read` heading ("दुर्गा देवी: शस्त्र हाथ में, करुणा हृदय में" / "Maa Durga: A Weapon in Her Hand, Compassion in Her Heart") are still in both texts, confirmed by grep, and the rebuild printed no "Note:" lines. The H2 "क्या भगवान बदला लेते हैं?" / "Does God Take Revenge?" was already a question and is unchanged.

## Checklist

- Now met: the focus keyword is in the body, in the meta description and (English) in the slug, and within the first 100 words in both languages; there is a direct answer early. "No unsupported scriptural claims": review issues 1 (Major), 3, 6, 7 and 8 are applied with the review's wording, and issue 2 is framed by issue 1's attribution. `check_seo.py` passes.
- The report had no section 12; it has now been added, with every item marked met.
- Still unmet: none.
- Left alone on purpose:
  - Review issues 4 and 5 (mark Gita 4.11 as "पूर्वार्ध / first half" and Taittiriya 1.11.2 as "अंश / excerpt") and issue 9 (IAST ṃ for ṁ) change verse references or verse text, which this fix may not touch. They are left for the editor to fix in the original blog.
  - The FAQ (report section 6) was not added to the text: it is optional, and the direct answer already covers the main question.
  - The report's sections 1, 4, 5, 9 and 10 still describe the original texts (for example "not yet applied", and section 9's note on images.txt); this fix may only edit sections 2, 3, 8, 11 and 12.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या भगवान बदला लेते हैं? आचार्य उपेंद्र जी 'ये यथा मां प्रपद्यन्ते' का अर्थ बताते हैं: भगवान हमारी भाषा में उत्तर देते हैं, पर भाव सदा उद्धार का होता है। | क्या भगवान बदला लेते हैं? आचार्य उपेंद्र जी ये यथा मां प्रपद्यन्ते का अर्थ बताते हैं: भगवान हमारी भाषा में उत्तर देते हैं, पर भाव सदा उद्धार का होता है। (152) |
| wordpress.hi.focus_keyword | ये यथा मां प्रपद्यन्ते का अर्थ | ये यथा मां प्रपद्यन्ते का अर्थ (unchanged; now in the body) |
| wordpress.hi.slug | ye-yatha-mam-prapadyante-arth | ye-yatha-mam-prapadyante-arth (unchanged) |
| wordpress.en.focus_keyword | Bhagavad Gita 4.11 meaning | does God take revenge |
| wordpress.en.secondary_keywords | does God take revenge, life is a boomerang, pause before you react, ye yatha mam prapadyante meaning | Bhagavad Gita 4.11 meaning, life is a boomerang, pause before you react, ye yatha mam prapadyante meaning |
| wordpress.en.slug | bhagavad-gita-4-11-meaning | does-god-take-revenge-gita-4-11 (31 characters, unique) |
| wordpress.en.meta_description | Does God take revenge? Acharya Upendra Ji explains Bhagavad Gita 4.11: … | unchanged (143 characters; already contains the new keyword) |

`title` (both already contain their focus keywords), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2, 3 and 8 were updated to match, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ye-yatha-mam-prapadyante-arth | does-god-take-revenge-gita-4-11 |
| focus_keyword | ये यथा मां प्रपद्यन्ते का अर्थ | does God take revenge |
| title | ये यथा मां प्रपद्यन्ते का अर्थ: क्या भगवान बदला लेते हैं? | Bhagavad Gita 4.11 Meaning: Does God Take Revenge? |
| meta_description | क्या भगवान बदला लेते हैं? आचार्य उपेंद्र जी ये यथा मां प्रपद्यन्ते का अर्थ बताते हैं: भगवान हमारी भाषा में उत्तर देते हैं, पर भाव सदा उद्धार का होता है। | Does God take revenge? Acharya Upendra Ji explains Bhagavad Gita 4.11: God answers us in the language we understand, yet always for our uplift. |
