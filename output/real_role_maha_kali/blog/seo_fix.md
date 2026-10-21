real_role_maha_kali: SEO fix

The check failed before the fix: the focus keywords "महाकाली की भूमिका" / "role of Mahakali" were not in the blog body in either language (the intro says "महाकाली की वास्तविक भूमिका" / "Mahakali's real role", which SureRank does not match), the Hindi title tag said "महाकाली की असली भूमिका" (a Hindi keyword must appear exactly), and the English meta description said "her real role". The opening also asked why the Durga Saptashati's first section is Mahakali's without answering it until the fourth section. The fix adds a short direct-answer paragraph after the intro in each language, built only from what the blog already says (section 5's snippet and the Key Takeaways, attributed to Acharya Ji, see flag 11), which uses the focus keyword in the first 100 words. It turns one H2 into the question readers search for, and rewrites the Hindi title and the English meta description to contain the focus keyword. The report had no section 12, so the checklist was added.

## Hindi (`real_role_maha_kali_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro paragraph (new paragraph) | (none) | संक्षेप में, आचार्य जी के अनुसार महाकाली की भूमिका रक्षा की है। दुर्गा तीन गुणों से बनी हैं: सरस्वती सात्विक (ज्ञान), महालक्ष्मी राजसिक (धन) और महाकाली तामसिक। महाकाली ज्ञान और लक्ष्मी की रक्षा के लिए लड़ती हैं। जैसे भवन से पहले सीमा और चौकीदार आते हैं, वैसे ही हर कार्य का आरंभ सुरक्षा से होता है। | Focus keyword in the body and the first 100 words (word 67). A direct answer early (about 55 words), taken from the blog's own sections ("त्रिगुणात्मक दुर्गा", "पहले सीमा, फिर नींव", Key Takeaways) and attributed to Acharya Ji. It says "तीन गुणों से बनी" rather than त्रिगुणात्मक/त्रिगुणात्मिका, so it neither repeats nor pre-empts review issue 2 |
| Second H2 | ## रक्षा किसकी? ज्ञान और लक्ष्मी की | ## महाकाली किसकी रक्षा करती हैं? ज्ञान और लक्ष्मी की | The section answers this searched question (FAQ 3, "महाकाली किसकी रक्षा करती हैं?"; section 4 asks for question headings) |

## English (`real_role_maha_kali_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro paragraph (new paragraph) | (none) | In short, according to Acharya Ji, the role of Mahakali is protection. Durga is made of the three gunas: Saraswati is sattvic (knowledge), Mahalakshmi rajasic (wealth) and Mahakali tamasic. Mahakali fights to protect the other two, knowledge and wealth. Just as a boundary wall and a watchman come before a building, every undertaking begins with protection. | Focus keyword in the body and the first 100 words (word 66). A direct answer early (about 58 words), taken from the blog's own sections and Key Takeaways ("Mahakali (tamasic, protection)") and attributed to Acharya Ji |
| Second H2 | ## What Needs Guarding? Knowledge and Wealth | ## What Does Mahakali Protect? Knowledge and Wealth | The section answers this searched question (secondary keyword "what does Mahakali protect", section 2; FAQ 3) |

No teaching, example, order of ideas, verse (Gita 10.41) or H1 was changed, and the number and order of headings are the same. The heading "पहले सीमा, फिर नींव" / "First the Boundary, Then the Foundation" (section 4's other suggestion) was kept because `images.txt` places `inline.jpg` after it, and "त्रिगुणात्मक दुर्गा: तीन गुण, तीन शक्तियाँ" / "Durga of the Three Gunas: Three Qualities, Three Powers" was kept because it is the `also_read` heading. The new paragraphs avoid the `links` phrases, so each link still lands where it did; all five phrases and the `also_read` heading are still in both texts, word for word. The Sanskrit review's corrections (Indra's thousand eyes, त्रिगुणात्मिका, महासरस्वती, सत्त्व/राजसिक, the Gita 10.41 bridge, IAST ṃ, the कलिका यंत्र gloss, the Ravana clause, "शास्त्र उन्हें मूर्ख कहते हैं") change the talk's content or wording beyond SEO, so they are left to the editor (section 10) and were not applied here.

## Checklist

- Now met: the focus keyword is in the body text and within the first 100 words in both languages, in the Hindi title tag and in the English meta description. "Focus keyword taken from wording the article already uses" is met for the `_seo` texts. `check_seo.py` passes, where it failed before. Both texts give a direct answer early, and one H2 per language is now a question.
- Already met and still met: every other item in section 12 (added to the report by this fix, all items marked).
- Still unmet: none.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | महाकाली की असली भूमिका: हर आरंभ उन्हीं से क्यों | महाकाली की भूमिका: सुरक्षा से ही हर शुभ आरंभ (44; section 3's option 2) |
| wordpress.en.meta_description | Why is the first part of the Durga Saptashati Mahakali's? Acharya Upendra Ji explains her real role: guarding knowledge and wealth before anything begins. | Why is the first part of the Durga Saptashati Mahakali's? Acharya Upendra Ji explains the role of Mahakali: guarding knowledge and wealth before all else. (154) |
| wordpress.hi.slug | mahakali-ki-bhumika | mahakali-ki-bhumika (unchanged) |
| wordpress.en.slug | role-of-mahakali | role-of-mahakali (unchanged) |
| wordpress.hi.focus_keyword | महाकाली की भूमिका | unchanged |
| wordpress.en.focus_keyword | role of Mahakali | unchanged |

The focus keywords were already the searched wording (section 2 had no mismatch), so they and the slugs stay; no other talk uses them. The English title and the Hindi meta description already contained the focus keywords and are unchanged. Secondary keywords, `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in section 2 (keyword note), section 3 (Hindi title option 2 and the new English meta description marked recommended, with the slugs), section 8 (Hindi alternativeHeadline and English description; headlines, keywords and slugs unchanged) and section 11, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | mahakali-ki-bhumika | role-of-mahakali |
| focus_keyword | महाकाली की भूमिका | role of Mahakali |
| title | महाकाली की भूमिका: सुरक्षा से ही हर शुभ आरंभ | Real Role of Mahakali: Why Every Beginning Starts With Her |
| meta_description | दुर्गा सप्तशती का पहला खंड महाकाली का क्यों है? आचार्य उपेंद्र जी समझाते हैं महाकाली की भूमिका: ज्ञान और लक्ष्मी की रक्षा, और हर आरंभ से पहले सुरक्षा। | Why is the first part of the Durga Saptashati Mahakali's? Acharya Upendra Ji explains the role of Mahakali: guarding knowledge and wealth before all else. |
