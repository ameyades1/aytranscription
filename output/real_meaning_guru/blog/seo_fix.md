real_meaning_guru: SEO fix

The check failed before the fix: the focus keywords "गुरु पूर्णिमा का आध्यात्मिक अर्थ" / "spiritual meaning of Guru Purnima" appeared in neither the blog body nor the meta descriptions (section 4 noted that the phrase never appears in the text). The opening also asked why Guru Purnima falls on the full moon without answering it until later. The fix adds a short direct-answer paragraph after the opening in each language. It is built only from what the blog already says (section 5's snippet, framed as Acharya Ji's explanation, see flag 8) and uses the focus keyword in the first 100 words. It also turns two H2s into the questions people search for (section 4's suggestions), and rewrites both meta descriptions to contain the focus keyword. The report had no section 12, so the checklist was added.

## Hindi (`real_meaning_guru_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the opening paragraph (new paragraph) | (none) | आचार्य जी बताते हैं कि गुरु पूर्णिमा का आध्यात्मिक अर्थ पूर्णिमा में ही छिपा है। सूर्य आत्मा का और चंद्रमा मन का प्रतीक है; जब आत्मा का पूरा प्रकाश मन पर प्रतिबिंबित होता है, वह गुरु की अवस्था है। इसी दिन को व्यास पूर्णिमा भी कहते हैं, और "व्यास" एक उपाधि है: वेदव्यास जी का नाम कृष्ण द्वैपायन था। | Focus keyword in the body and the first 100 words (word 43). A direct answer early (about 55 words), taken from the blog's own sections and attributed to Acharya Ji |
| First H2 | ## यह पर्व अमावस्या को क्यों नहीं? | ## गुरु पूर्णिमा पूर्णिमा को ही क्यों होती है? | The section answers this searched question (secondary keyword "गुरु पूर्णिमा पूर्णिमा को क्यों होती है"; section 4) |
| Third H2 | ## व्यास कोई नाम नहीं था | ## वेदव्यास का असली नाम क्या था? | The section answers this searched question (secondary keyword "वेदव्यास का असली नाम"; section 4) |

## English (`real_meaning_guru_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the opening paragraph (new paragraph) | (none) | As Acharya Ji explains, the spiritual meaning of Guru Purnima lies in the full moon. The sun symbolises the Atman and the moon the mind; when the Self's full light is reflected in the mind, that is the state of a Guru. The day is also called Vyasa Purnima, and "Vyasa" is a title: Vedavyasa's name was Krishna Dvaipayana. | Focus keyword in the body and the first 100 words (word 47). A direct answer early (about 58 words), taken from the blog's own sections and attributed to Acharya Ji |
| First H2 | ## Why Not the New Moon? | ## Why Is Guru Purnima on the Full Moon? | The section answers this searched question (secondary keyword "why Guru Purnima is on the full moon"; section 4) |
| Third H2 | ## Vyasa Was Never a Name | ## What Was Vedavyasa's Real Name? | The section answers this searched question (secondary keyword "real name of Vedavyasa"; section 4) |

No teaching, example, order of ideas or H1 was changed (the blog quotes no verses), and the number and order of headings are the same. The new paragraphs avoid the `links` phrases, so each link still lands where it did. All five `links` phrases and the `also_read` heading ("सत्रह पुराण, फिर भी बेचैनी" / "Seventeen Puranas, Yet No Peace") are still in both texts, word for word. The Sanskrit review's corrections (the "seventeen Puranas" account, sleeplessness, what was divided, the duplicate Hindi sentence, the Hindi question's grammar, the meaning of "Vyasa", the English heading "Why Did Someone Divide the Vedas?") change the talk's content or wording beyond SEO, so they are left to the editor and were not applied here. The direct answer speaks only of "dividing the Vedas" and avoids those points.

## Checklist

- Now met: the focus keyword is in the body text, within the first 100 words, and in the meta description, in both languages. `check_seo.py` passes, where it failed before. Both texts give a direct answer early, and two H2s per language are now questions.
- Already met and still met: every other item in section 12 (added to the report by this fix, all items marked).
- Still unmet: none.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | गुरु पूर्णिमा पूर्णिमा को ही क्यों होती है? आचार्य उपेंद्र जी बताते हैं सूर्य-चंद्र का प्रतीक, व्यास एक पद क्यों है, और ज्ञान के साथ भक्ति क्यों आवश्यक है। | गुरु पूर्णिमा का आध्यात्मिक अर्थ: यह पूर्णिमा को ही क्यों होती है, व्यास एक पद क्यों है, और ज्ञान के साथ भक्ति क्यों आवश्यक है, बताते हैं आचार्य उपेंद्र जी। (156) |
| wordpress.en.meta_description | Why does Guru Purnima fall on the full moon? Acharya Upendra Ji explains the sun-moon symbolism, why Vyasa is a title, and why knowledge needs devotion. | Spiritual meaning of Guru Purnima: why it falls on the full moon, why Vyasa is a title, and why knowledge needs devotion, as Acharya Upendra Ji explains. (153) |
| wordpress.hi.slug | guru-purnima-ka-adhyatmik-arth | guru-purnima-ka-adhyatmik-arth (unchanged) |
| wordpress.en.slug | spiritual-meaning-of-guru-purnima | spiritual-meaning-of-guru-purnima (unchanged) |
| wordpress.hi.focus_keyword | गुरु पूर्णिमा का आध्यात्मिक अर्थ | unchanged |
| wordpress.en.focus_keyword | spiritual meaning of Guru Purnima | unchanged |

The focus keywords were already the searched wording (section 2 had no mismatch), so they and the slugs stay; no other talk uses them. The titles already contained the focus keywords and are unchanged. Secondary keywords, `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in section 2 (keyword note), section 3 (new meta descriptions, marked recommended with the slugs), section 8 (description in both schema blocks; headline, alternativeHeadline, keywords and slugs unchanged) and section 11, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | guru-purnima-ka-adhyatmik-arth | spiritual-meaning-of-guru-purnima |
| focus_keyword | गुरु पूर्णिमा का आध्यात्मिक अर्थ | spiritual meaning of Guru Purnima |
| title | गुरु पूर्णिमा का आध्यात्मिक अर्थ और व्यास का असली अर्थ | Spiritual Meaning of Guru Purnima and Who Vyasa Really Was |
| meta_description | गुरु पूर्णिमा का आध्यात्मिक अर्थ: यह पूर्णिमा को ही क्यों होती है, व्यास एक पद क्यों है, और ज्ञान के साथ भक्ति क्यों आवश्यक है, बताते हैं आचार्य उपेंद्र जी। | Spiritual meaning of Guru Purnima: why it falls on the full moon, why Vyasa is a title, and why knowledge needs devotion, as Acharya Upendra Ji explains. |
