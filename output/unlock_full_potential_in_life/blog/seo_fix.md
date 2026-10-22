unlock_full_potential_in_life: SEO fix

The report had no section 12 checklist yet, and `check_seo.py` failed: the focus keywords "वर्ण और आश्रम व्यवस्था" / "varna and ashrama system" were in the title and meta description but not in either blog body, word for word (the intros say "वर्ण और आश्रम की प्राचीन व्यवस्था" / "the ancient system of **varna** ... and **ashrama**"). The opening also asked "who can guarantee it?" without a short answer. Each language gets three changes: a short direct answer after the intro, built only from what the blog already says (report section 5), which puts the focus keyword in the first 100 words, and two H2s rephrased as the searched questions (report section 4). Focus keywords, slugs, titles and meta descriptions stay.

## Hindi (`unlock_full_potential_in_life_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro, new paragraph before "## गुणों से वर्ण, आयु से आश्रम" | (none) | आचार्य जी के अनुसार वर्ण और आश्रम व्यवस्था में वर्ण तीन गुणों से बनते हैं और आश्रम आयु से: ब्रह्मचर्य, गृहस्थ, वानप्रस्थ और संन्यास। जब वर्ण का आधार गुण और कर्म है, तो वर्ण बदल सकता है। जीवन की गारंटी नहीं, इसलिए अध्यात्म को साठ के बाद तक टालना उचित नहीं; संन्यास वृत्ति पच्चीस से ही अपनाई जा सकती है। | Direct answer (60 words), restating the blog's own points (गुणों से वर्ण, आयु से आश्रम, the four ashramas, "जब आधार गुण और कर्म है, तो वर्ण भी बदल सकता है", the key takeaways on not waiting past sixty and संन्यास वृत्ति from twenty-five). Puts the focus keyword at about word 51 of the body. Attributed to Acharya Ji; avoids the Prahlada and "मया" wording (flags 1 and 2) and uses no link phrase. |
| H2 of the third section | ## सबकी निवृत्ति आती है | ## चार आश्रम कौन से हैं? | The searched question "चार आश्रम कौन से हैं" as a heading; the section names all four ashramas and their ages. |
| H2 of the seventh section | ## यह विद्या क्या बदलती है | ## यह विद्या क्या बदलती है, और क्या वर्ण बदल सकता है? | Adds the searched question "क्या वर्ण बदल सकता है"; the section ends with Gita 4.13 and "वर्ण भी बदल सकता है". Original wording kept. |

## English (`unlock_full_potential_in_life_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro, new paragraph before "## Varna by Nature, Ashrama by Age" | (none) | In the varna and ashrama system as Acharya Ji explains it, varna arises from the three gunas and ashrama from age: Brahmacharya, Grihastha, Vanaprastha and Sannyasa. If varna rests on qualities and action, it can change. Since life itself comes with no guarantee, spirituality need not wait until after sixty; the spirit of renunciation can be embraced from twenty-five. | Direct answer (59 words), built only from the blog. Puts the focus keyword at about word 55 of the body. Attributed to Acharya Ji; no link phrase used. |
| H2 of the third section | ## Everyone Steps Back Eventually | ## What Are the Four Ashramas of Life? | The searched question "four ashramas of life" as a heading; the section lists all four with their ages. |
| H2 of the seventh section | ## How This Knowledge Transforms a Life | ## Can Varna Change? How This Knowledge Transforms a Life | Adds the searched question "can varna change"; the section answers it from Gita 4.13. Original wording kept. |

No teaching, example, verse, translation, H1 or order of ideas changed, and Markdown is kept. The number and order of headings are unchanged; the image heading in images.txt ("वानप्रस्थ का असली अर्थ") is untouched. All five `links` phrases and the `also_read` heading ("कौन दे सकता है गारंटी?" / "Who Can Promise You Your Later Years?") are still in both texts once each, confirmed by grep.

## Checklist

- Now met: focus keyword in the body text (both) and within the first 100 words (both); focus keyword taken from wording the article uses. `check_seo.py` passes.
- Added: the report's section 12, which was missing; section 2 got a keyword note, and section 4's stale "keyword already present" line was corrected.
- Still unmet (1): "No unsupported scriptural claims". The Sanskrit review's Major issue 1 (Prahlada became a devotee "on his own"; the Bhagavata credits Narada's teaching in the womb) and Major issue 2 (the Hindi Gita 4.13 meaning drops "मया") are still in the body. They are editorial corrections for the original blog, and the verse translation may not be touched by an SEO fix; no title, meta or new paragraph uses them.
- Left alone on purpose: the English gloss "(renunciate attitude)" in the Hindi text (flag 10, an editorial change, not needed for the keyword) and review issues 3–10 (for the editor).

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | varna-aur-ashram-vyavastha | varna-aur-ashram-vyavastha (unchanged) |
| wordpress.en.slug | varna-and-ashrama-system | varna-and-ashrama-system (unchanged; 24 characters, contains the keyword) |

No seo.json field changed: the focus keywords are the searched wording and the `_seo` texts now use them, and the titles and meta descriptions already contain them. `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 3 and 8 already match it.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | varna-aur-ashram-vyavastha | varna-and-ashrama-system |
| focus_keyword | वर्ण और आश्रम व्यवस्था | varna and ashrama system |
| title | वर्ण और आश्रम व्यवस्था: अध्यात्म साठ तक क्यों टालें? | Varna and Ashrama System: Why Wait Until 60 to Turn Inward? |
| meta_description | वर्ण और आश्रम व्यवस्था का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि वर्ण गुण और कर्म से बदलता है, और अध्यात्म को साठ के बाद तक टालना क्यों ठीक नहीं। | What does the varna and ashrama system teach? Acharya Upendra Ji shows how varna shifts with guna and action, and why spirituality should not wait for 60. |
