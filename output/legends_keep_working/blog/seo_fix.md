legends_keep_working: SEO fix

Copies written: `legends_keep_working_blog_seo.txt` (Hindi) and `legends_keep_working_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new paragraph after "…संसार के लिए कर्म करते हैं।**" | (none) | संक्षेप में, यहाँ लोकसंग्रह का अर्थ है लोगों को जोड़ना और उन्हें दिशा देना। गीता (३.२१–३.२६) में श्रीकृष्ण बताते हैं कि श्रेष्ठ पुरुष जैसा आचरण करता है, लोग वैसा ही करते हैं। इसलिए जिसे कुछ पाना शेष नहीं, वह भी कर्म करता है, ताकि समाज को आदर्श मिले और लोगों में कर्मों के प्रति अश्रद्धा न हो। | The focus keyword "लोकसंग्रह का अर्थ" was not in the body (SureRank error), "लोकसंग्रह" first appeared only in the 3.25 section, and there was no early direct answer. 57 words, built only from the blog: its own gloss of लोकसंग्रह (3.25, marked "यहाँ" as this talk's sense), 3.21, 3.22 and the "कर्मों में अश्रद्धा" of 3.26. The keyword now starts at about word 64 |
| H2 9 | बुद्धि में भ्रम मत डालो | क्या आध्यात्मिक होने के लिए काम छोड़ना ज़रूरी है? | The natural life question readers search (report sections 2 and 4); the section answers it ("व्यापार छोड़ दे… ऐसा कहने वाले गुरु के पास मत जाना", त्याग is not merely leaving). The 3.26 verse under it is unchanged |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new paragraph after "…but for the world.**" | (none) | In short, the lokasangraha meaning in this talk is simple: bringing people together and giving them direction. In the Gita (3.21 to 3.26), Shri Krishna says that whatever the great do, others follow. So even one with nothing left to gain keeps acting, to set an example and to keep people from losing faith in action. | The focus keyword "lokasangraha meaning" was not in the body (SureRank error) and there was no early direct answer. 56 words, built only from the blog (its 3.25 gloss, stated as this talk's sense; 3.21; 3.22; the "distrust of action" of 3.26). The keyword now starts at about word 82 |
| H2 9 | Do Not Unsettle Their Minds | Must You Give Up Work to Be Spiritual? | The emotional query in section 2 ("does spirituality mean giving up work"); the section answers it ("Stay away from a Guru who tells you, 'Child, give up your business'"; "Walking away is not the right path"). The 3.26 verse under it is unchanged |

All `links` phrases and both `also_read` headings ("विकल्प के बिना बदलाव नहीं" / "No Change Without an Alternative") are unchanged and still in the `_seo` texts. The number and order of `##` sections is the same. Scripture verses, translations, references and the H1 are untouched. The Sanskrit review's corrections (tools/review/legends_keep_working.md: Gita 3.24 first person and second half, the वर्णसंकर and लोकसंग्रह glosses, the dropped vocatives in 3.22, 3.23 and 3.25, "attached to action" in 3.26, सात्त्विक, वसिष्ठ) are outside this fix's scope and remain open for the editor. If the editor adopts the review's लोकसंग्रह gloss ("लोक-कल्याण और लोकमर्यादा" / "the welfare and right order of the world"), the new direct-answer paragraphs should be updated to match.

## Checklist

Now met:
- Focus keyword in the body text (both languages; it was missing in both)
- Focus keyword in the meta description (English; the old meta said "What is lokasangraha?" without "meaning")
- Focus keyword within the first 100 words (both languages)
- Focus keyword taken from wording the article uses (the `_seo` texts now use it)
- Direct answer paragraph (40–60 words) placed early (both languages)
- One H2 per language phrased as the question readers search (the gurukul H2 was already a question)

Still unmet: none. Section 12 (the SEO checklist, missing from the report until now) is added with every item marked `[x]`; `tools/check_seo.py` passes.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | What is lokasangraha? Through Gita 3.21 to 3.26, Acharya Upendra Ji explains why those who need nothing still act: to set the example the world follows. | Lokasangraha meaning: through Gita 3.21 to 3.26, Acharya Upendra Ji explains why those who need nothing still act, to set the example the world follows. (152 characters) |

Unchanged: both focus keywords (already the searched wording, now in the body), both slugs (`lokasangraha-ka-arth`, `lokasangraha-meaning-gita`: old and new are the same), both titles, the Hindi meta description, secondary keywords, `links`, `also_read`, `related`, alt text, captions, category and tags. Report updated: section 2 (keyword note), section 3 (meta descriptions and slugs marked recommended; English meta replaced), section 8 (English BlogPosting description), section 11 (seo.json block), and section 12 (checklist added and marked).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | lokasangraha-ka-arth | lokasangraha-meaning-gita |
| focus_keyword | लोकसंग्रह का अर्थ | lokasangraha meaning |
| title | लोकसंग्रह का अर्थ: श्रेष्ठ पुरुष कर्म क्यों करते हैं | Lokasangraha Meaning: Why Legends Keep Working (Gita 3) |
| meta_description | लोकसंग्रह का अर्थ क्या है? गीता ३.२१ से ३.२६ पर आचार्य उपेंद्र जी बताते हैं कि जिसे कुछ नहीं चाहिए, वह भी कर्म क्यों करता है, ताकि समाज को आदर्श मिले। | Lokasangraha meaning: through Gita 3.21 to 3.26, Acharya Upendra Ji explains why those who need nothing still act, to set the example the world follows. |
