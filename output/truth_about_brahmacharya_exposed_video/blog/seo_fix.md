truth_about_brahmacharya_exposed_video: SEO fix

The original blog texts are unchanged; the fixes are in `truth_about_brahmacharya_exposed_video_blog_seo.txt` (Hindi) and `truth_about_brahmacharya_exposed_video_blog_seo_en.txt` (English), which the page and WordPress now use.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| After the introduction, before the first `##` | (no paragraph) | आचार्य जी के अनुसार ब्रह्मचर्य का असली अर्थ है ब्रह्म में विचरण, केवल अविवाहित रहना या भगवा पहनना नहीं। इसे फलश्रुति से पहचाना जाता है: तीव्र मेधा, चेहरे का तेज, क्रोध पर नियंत्रण, क्षमा, और यह कि स्त्रियां उस व्यक्ति के सामने सुरक्षित अनुभव करें। शास्त्रोक्त काम से जीने वाला गृहस्थ भी ब्रह्मचारी ही है। | Focus keyword "ब्रह्मचर्य का असली अर्थ" was not in the body; adds it in the first 100 words as a short direct answer (report section 5), built only from the blog's own points |
| Third `##` heading | ब्रह्मचर्य की असली परीक्षा | ब्रह्मचर्य की पहचान कैसे करें? | Question heading matching the searched "ब्रह्मचर्य की पहचान" (report section 4); the section answers it |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| After the introduction, before the first `##` | (no paragraph) | What is brahmacharya? According to Acharya Ji, it means moving in Brahman, not merely staying unmarried or wearing saffron. It is known by its fruits: a sharp intellect, radiance in the face, mastery over anger, forgiveness, and women feeling safe in a person's presence. A householder who lives by scripture-sanctioned desire is also a brahmachari. | Focus keyword "what is brahmacharya" was not in the body; adds it in the first 100 words as a short direct answer (report section 5), built only from the blog's own points |
| Third `##` heading | The Real Test of Brahmacharya | How Do You Recognise True Brahmacharya? | Question heading matching "signs of brahmacharya" searches (report section 4); the section answers it |

All `links` phrases and both `also_read` headings are unchanged and still present in the `_seo` texts. No verse, translation, reference or H1 was touched; the number and order of `##` sections are the same.

## Checklist

Now met (they failed `check_seo.py` before the fix):
- Focus keyword in the body text (Hindi and English)
- Focus keyword in the meta description (English)
- Focus keyword within the first 100 words (Hindi and English)
- Focus keyword taken from wording the article uses
- A direct answer early in the post, and a question-form `##` heading

Still unmet (1):
- No unsupported scriptural claims: the blog still carries the Sanskrit review's open issues (the gopis passage, "every avatar was married", "Krishna names four purusharthas"; report section 10). These change the content, not SEO, so they are left to the editor's review fix.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | Is marriage a spiritual step down? Acharya Upendra Ji explains what brahmacharya truly means, why kama is a purushartha, and how true restraint shows. | What is brahmacharya? Acharya Upendra Ji explains why marriage is no spiritual step down, why kama is a purushartha, and how true restraint shows. |

Slugs unchanged (Hindi `brahmacharya-ka-asli-arth`, English `what-is-brahmacharya`); focus keywords, titles, the Hindi meta description, `links` and `also_read` unchanged.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | brahmacharya-ka-asli-arth | what-is-brahmacharya |
| focus keyword | ब्रह्मचर्य का असली अर्थ | what is brahmacharya |
| title | ब्रह्मचर्य का असली अर्थ: विवाह, काम और संयम \| आचार्य जी | What Is Brahmacharya? The Truth No One Tells \| Acharya Ji |
| meta description | क्या विवाह आध्यात्मिक रूप से नीचे होना है? आचार्य उपेंद्र जी शास्त्रों से बताते हैं ब्रह्मचर्य का असली अर्थ, काम पुरुषार्थ और सच्चे संयम की पहचान। | What is brahmacharya? Acharya Upendra Ji explains why marriage is no spiritual step down, why kama is a purushartha, and how true restraint shows. |

Titles exactly as in seo.json (unescaped): Hindi `ब्रह्मचर्य का असली अर्थ: विवाह, काम और संयम | आचार्य जी`; English `What Is Brahmacharya? The Truth No One Tells | Acharya Ji`.
