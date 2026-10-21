sacred_guru_jupiter_chanting: SEO fix

The check failed before the fix: neither focus keyword was in the blog body ("गुरु ग्रह का महत्व" never appeared in the Hindi text, which only says "गुरु ग्रह"; "significance of Jupiter in Vedic astrology" never appeared in the English text, and Jupiter was absent from the English H1 and first 100 words). The Hindi meta description lacked its focus keyword, and the long English keyword was in neither the English title tag, the meta description nor the slug. The opening also had no direct answer (report sections 4 and 5). The fix adds a short direct-answer paragraph after the intro in each language, built only from what the blog already says (the section on what Jupiter presides over, the "weak Jupiter" section and "गुरु ही शिव है"), which uses the focus keyword in the first 100 words. It turns one H2 into the question readers search for. The English focus keyword becomes the shorter searched wording "significance of Jupiter", which the title and slug already contained, and both meta descriptions were rewritten to contain the focus keyword. The report had no section 12, so the checklist was added.

## Hindi (`sacred_guru_jupiter_chanting_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro ("…क्यों रखा गया है।"), new paragraph | (none) | संक्षेप में, गुरु ग्रह का महत्व यह है कि देवगुरु बृहस्पति शिक्षा, ज्ञान, स्थिरता, मान-सम्मान, धन, वैवाहिक सुख, संतान, धर्म और आध्यात्मिक प्रगति के अधिष्ठाता हैं। संतुलित गुरु स्पष्ट मार्गदर्शन, विवेक और भक्ति देते हैं; दोषग्रस्त गुरु भ्रम और बाधाएँ लाते हैं। और आचार्य जी के अनुसार गुरु ही शिव हैं, जो बताते हैं कि छिपे परमात्मा कहाँ हैं। | Focus keyword in the body and the first 100 words (word 64). A direct answer early (about 55 words), taken from the blog's own sections ("गुरु ग्रह…", "जब गुरु कमज़ोर हो", "परमात्मा छिप क्यों जाते हैं?") and section 5's snippet. It names Jupiter's domains only and promises no result (flag 7) |
| Second H2 | ## गुरु ग्रह: जीवन को अर्थ देने वाली शक्ति | ## जीवन में गुरु ग्रह का महत्व क्या है? | The section answers this searched question (primary query; section 4's suggestion, FAQ 1) |

## English (`sacred_guru_jupiter_chanting_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro ("…even before God."), new paragraph | (none) | In short, the significance of Jupiter is this: known in Vedic astrology as Guru, Devguru Brihaspati presides over education, knowledge, stability, honour, wealth, marriage, children, righteous work and spiritual progress. A well-balanced Jupiter brings clear guidance, discernment and devotion; an afflicted one brings confusion and obstacles. And, as Acharya Ji teaches, the Guru is Shiva, who shows where the hidden God is. | Focus keyword in the body and the first 100 words (word 62); Jupiter now named early. A direct answer early (about 60 words), from the blog's own sections and section 5's snippet, with no promised outcome (flag 7) |
| Second H2 | ## Jupiter: The Power That Gives Life Meaning | ## What Is the Significance of Jupiter in Your Life? | The section answers this searched question (section 4's suggestion, FAQ 1) |

No teaching, example, order of ideas, verse (Guru Gita line, Kabir's doha, Gita 7.25) or H1 was changed, and the number and order of headings are the same. "जब गुरु कमज़ोर हो" / "When Jupiter Is Weak" was kept because it is the `also_read` heading (section 4's question version was not used), and "छुपा-छुपी और माँ का इशारा" is untouched (`images.txt` places `inline.jpg` there). The new paragraphs avoid the `links` phrases; all four phrases and the `also_read` heading are still in both texts, word for word. The Sanskrit review's corrections (Guru Gita meaning "शिव… कोई भी रक्षा नहीं कर सकता", partial-verse marks, "शास्त्र कहता है" → "संत कहते हैं", the "four forms" heading, "brahmacharya") change the talk's content beyond SEO, so they are left to the editor (section 10) and were not applied here.

## Checklist

- Now met: the focus keyword is in the body text and within the first 100 words in both languages, in both meta descriptions, and (English) in the title tag and slug. "Focus keyword taken from wording the article already uses" is met for the `_seo` texts. `check_seo.py` passes, where it failed before. Both texts give a direct answer early, and one H2 per language is now a question.
- Already met and still met: every other item in section 12 (added to the report by this fix, all items marked).
- Still unmet: none. Notes kept on two items: the tag "गुरु कृपा / Guru Kripa" is in only 2 posts so far, and the body's "शास्त्र कहता है" and "ग्रंथराज" are flagged for the editor (section 10).

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.focus_keyword | significance of Jupiter in Vedic astrology | significance of Jupiter |
| wordpress.en.secondary_keywords | weak Jupiter effects, who is Devguru Brihaspati, Guru beej mantra sadhana, shive ruste gurus trata meaning | significance of Jupiter in Vedic astrology, weak Jupiter effects, who is Devguru Brihaspati, Guru beej mantra sadhana |
| wordpress.en.meta_description | What does Jupiter, Devguru Brihaspati, govern in your life? Acharya Upendra Ji explains Guru grace, the signs of a weak Jupiter and the Guru beej mantra. | What is the significance of Jupiter, Devguru Brihaspati, in your life? Acharya Upendra Ji explains Guru grace, signs of a weak Jupiter and Guru sadhana. (152) |
| wordpress.hi.meta_description | देवगुरु बृहस्पति, यानी गुरु ग्रह, जीवन में क्या देते हैं? आचार्य उपेंद्र जी बताते हैं गुरु कृपा का रहस्य, कमज़ोर गुरु के लक्षण और गुरु बीज मंत्र साधना। | गुरु ग्रह का महत्व क्या है? देवगुरु बृहस्पति जीवन में क्या देते हैं? आचार्य उपेंद्र जी बताते हैं गुरु कृपा, कमज़ोर गुरु के लक्षण और गुरु बीज मंत्र साधना। (153) |
| wordpress.hi.slug | guru-grah-ka-mahatva | guru-grah-ka-mahatva (unchanged) |
| wordpress.en.slug | significance-of-jupiter-guru-grace | significance-of-jupiter-guru-grace (unchanged; already built from the new focus keyword, 34 characters) |
| wordpress.hi.focus_keyword | गुरु ग्रह का महत्व | unchanged |

The old English focus keyword moved to the secondary keywords; "shive ruste gurus trata meaning" was dropped from them to stay at four, since flag 1 says not to push it until the verse meaning is corrected. No other talk uses either focus keyword. Both titles already contained their focus keywords and are unchanged. `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in section 2 (keyword note and the new keyword row), section 3 (the meta descriptions and slugs in seo.json marked recommended), section 8 (Hindi and English description, English keywords; headlines and URL placeholders unchanged) and section 11, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | guru-grah-ka-mahatva | significance-of-jupiter-guru-grace |
| focus_keyword | गुरु ग्रह का महत्व | significance of Jupiter |
| title | गुरु ग्रह का महत्व: देवगुरु बृहस्पति की कृपा का रहस्य | Significance of Jupiter: Devguru Brihaspati's Grace |
| meta_description | गुरु ग्रह का महत्व क्या है? देवगुरु बृहस्पति जीवन में क्या देते हैं? आचार्य उपेंद्र जी बताते हैं गुरु कृपा, कमज़ोर गुरु के लक्षण और गुरु बीज मंत्र साधना। | What is the significance of Jupiter, Devguru Brihaspati, in your life? Acharya Upendra Ji explains Guru grace, signs of a weak Jupiter and Guru sadhana. |
