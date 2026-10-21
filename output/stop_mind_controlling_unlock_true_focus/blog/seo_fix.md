stop_mind_controlling_unlock_true_focus: SEO fix

`check_seo.py` failed before the fix. Neither body nor meta description contained its focus keyword ("चित्त वृत्ति निरोध का अर्थ" / "chitta vritti nirodha meaning"). The bodies only had "चित्तवृत्तिनिरोध" / "chitta-vritti-nirodha" (joined, at the end) and "चित्त की वृत्तियों का निरोध". The opening asked the question but gave no short answer. Each language gets three changes:
- a short direct answer, built only from what the blog already says, that brings in the focus keyword within the first 100 words;
- one heading rephrased as the question readers search for;
- the Sanskrit review's correction to the mahattattva sentence ("beneath" chitta → "at the root of" chitta, credited to Acharya Ji).

The focus keywords and slugs stay the same.

## Hindi (`stop_mind_controlling_unlock_true_focus_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new second paragraph (after "…उसे स्थिर करना ही योग क्यों है।") | (none) | संक्षेप में, चित्त वृत्ति निरोध का अर्थ है चित्त की वृत्तियों, यानी मन और बुद्धि में बार-बार होने वाले परिवर्तनों का रुक जाना। महर्षि पतंजलि इसी को योग कहते हैं। जब कोई वृत्ति प्रबल हो जाती है, तो वह प्रवृत्ति, यानी आदत बन जाती है। साधक का अभ्यास है मन को एक जगह स्थिर रखना। | The focus keyword was missing from the body (a SureRank error). This is a direct answer of about 50 words that restates the blog's own sections (the sutra's meaning, vritti, pravritti, steadiness), and it puts the keyword in the first 100 words. |
| "योग वास्तव में क्या है?", paragraph after the sutra | चित्त के नीचे महत्तत्त्व, अर्थात् बुद्धि है। | आचार्य जी बताते हैं कि चित्त के मूल में महत्तत्त्व, अर्थात् बुद्धि है। | Content trust: "नीचे" contradicted the sentence before it (Sanskrit review issue 1, report flag 1). The new wording is the review's own correction. |
| Second H2 | ## वृत्ति: मन का बार-बार बदल जाना | ## वृत्ति क्या है? मन का बार-बार बदल जाना | The question form suggested in report section 4 ("वृत्ति क्या है?"). The section answers it. |

## English (`stop_mind_controlling_unlock_true_focus_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new second paragraph (after "…why steadying it is what yoga is.") | (none) | In short, the chitta vritti nirodha meaning is this: yoga is the stilling of the vrittis, the changes that keep arising in the mind and intellect. When a vritti grows strong, it becomes a pravritti, a habit. The practice is to hold the mind steady in one place. | The focus keyword was missing from the body (a SureRank error). This is a direct answer of about 50 words built from the blog's own sections, and it puts the keyword in the first 100 words. |
| "What Is Yoga, Really?", paragraph after the sutra | Beneath chitta lies **mahattattva** (the cosmic intellect), that is, buddhi. | Acharya Ji explains that at the root of chitta lies **mahattattva** (the cosmic intellect), that is, buddhi. | Content trust: the Sanskrit review's correction (issue 1, report flag 1). |
| Second H2 | ## Vritti: A Mind That Keeps Shifting | ## What Is a Vritti? A Mind That Keeps Shifting | The question form suggested in report section 4. The section answers it. |

Nothing else changed:
- no teaching, example, H1 or order of ideas, and no heading count or order;
- the sutra, its translation and its reference are untouched (the review's issues 2 and 3, renaming the reference to "पातंजल योगसूत्र" / "Patanjala Yoga Sutra", touch a scripture reference and are left for the editor);
- the H2 "स्थिरता: योग का असली अभ्यास" / "Steadiness: The Real Practice of Yoga", which `images.txt` and `also_read` use, is untouched.

A grep finds all five `links` phrases and the `also_read` heading in both texts, word for word, and each focus keyword once in its body.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages).
  - Focus keyword in the meta description (both languages).
  - Focus keyword within the first 100 words (both languages).
  - No unsupported scriptural claims: the mahattattva sentence now follows the review and is credited to Acharya Ji.
- Already met and still met: every other item except the one below. `check_seo.py` passes.
- Section 12 was missing from the report and has been added, marked against the fixed texts.
- Still unmet (1):
  - Each tag can be shared by at least 3 posts. "एकाग्रता" / "Focus" and "आदतें" / "Habits" are used by this post only so far. This fix does not change tags.
- Left alone on purpose:
  - "प्रवृत्ति: जब वृत्ति आदत बन जाए" / "Pravritti: When a Fluctuation Becomes a Habit" is not rephrased; one question heading per language is enough, and report section 4 marks this one as optional.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | चित्त वृत्ति निरोध क्या है? आचार्य उपेंद्र जी योगसूत्र १.२ से समझाते हैं कि वृत्ति कैसे प्रवृत्ति यानी आदत बनती है, और मन को स्थिर रखना ही योग क्यों है। | चित्त वृत्ति निरोध का अर्थ क्या है? आचार्य उपेंद्र जी योगसूत्र १.२ से समझाते हैं कि वृत्ति कैसे प्रवृत्ति यानी आदत बनती है, और मन को स्थिर रखना ही योग क्यों है। (160) |
| wordpress.en.meta_description | What is chitta vritti nirodha? Acharya Upendra Ji explains Yoga Sutra 1.2, how a wandering vritti hardens into a pravritti, and why steadiness is yoga. | Chitta vritti nirodha meaning: Acharya Upendra Ji explains Yoga Sutra 1.2, how a wandering vritti hardens into a pravritti, and why steadiness is yoga. (151) |
| wordpress.hi.slug | chitta-vritti-nirodh-ka-arth | chitta-vritti-nirodh-ka-arth (unchanged) |
| wordpress.en.slug | chitta-vritti-nirodha-meaning | chitta-vritti-nirodha-meaning (unchanged) |

Unchanged:
- in seo.json: the titles, focus keywords, secondary keywords, `links`, `also_read`, `alt`, `caption`, `related`, category and tags;
- in the report: section 11 holds the same JSON. Section 2 has a new keyword note. Section 3 marks the recommended title, meta description and slug for each language and has the new meta descriptions. Section 8 has the new descriptions. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | chitta-vritti-nirodh-ka-arth | chitta-vritti-nirodha-meaning |
| focus keyword | चित्त वृत्ति निरोध का अर्थ | chitta vritti nirodha meaning |
| title | चित्त वृत्ति निरोध का अर्थ: मन बार-बार क्यों बदलता है | Chitta Vritti Nirodha Meaning: Why the Mind Keeps Wandering |
| meta description | चित्त वृत्ति निरोध का अर्थ क्या है? आचार्य उपेंद्र जी योगसूत्र १.२ से समझाते हैं कि वृत्ति कैसे प्रवृत्ति यानी आदत बनती है, और मन को स्थिर रखना ही योग क्यों है। | Chitta vritti nirodha meaning: Acharya Upendra Ji explains Yoga Sutra 1.2, how a wandering vritti hardens into a pravritti, and why steadiness is yoga. |
