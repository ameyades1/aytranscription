who_real_doer_karma_ego_bhagavad: SEO fix

Copies written: `who_real_doer_karma_ego_bhagavad_blog_seo.txt` (Hindi) and `who_real_doer_karma_ego_bhagavad_blog_seo_en.txt` (English). The original blog texts are unchanged.

The report's section 12 checklist had every item met. What the texts still lacked: the opening only asks the question ("असली कर्ता कौन है?" / "who is the real doer?") and the verse that answers it comes only in the third section, so there was no direct answer early (report sections 4 and 5). Section 2 also noted that the searched "गीता 3.27" (Latin digits) and "कर्तापन का अहंकार" were not in the Hindi body. Each language gets three changes: a direct answer paragraph after the opening, built only from what the blog already says (the verse's meaning, "they happen through us", and the takeaway on liberation), and two question or verse-number headings that section 4 recommended. The focus keywords were already in the first 100 words and stay as they are.

## Hindi (`who_real_doer_karma_ego_bhagavad_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening | (none) | भगवद्गीता 3.27 में श्रीकृष्ण कहते हैं कि संपूर्ण कर्म प्रकृति के गुणों द्वारा किए जाते हैं, पर अहंकार से मोहित व्यक्ति मानता है "मैं कर्ता हूं"। यानी असली कर्ता प्रकृति है; कर्म हम नहीं करते, वह हमारे माध्यम से होता है। "मैं ही करता हूं" मानना अहंकार और अज्ञान है। यही कर्तापन का अहंकार है, और इसे पहचानने से ही मोक्ष की राह शुरू होती है। | Direct answer (about 55 words) early, as report section 5 recommends; built from the verse translation, "वह हमारे माध्यम से होता है" and the takeaways. Puts the searched "गीता 3.27" (Latin digits) and "कर्तापन का अहंकार" (section 2) in the first 100 words. The verse reference itself still reads ३.२७ |
| H2 1 | आज का वर्तमान, कल की कमाई | क्या आज का सुख पिछले पुण्य का फल है? | Question heading suggested in report section 4; the section answers it ("यदि आपका वर्तमान बहुत अच्छा है, तो … भूतकाल में आपने बहुत अच्छा किया होगा") |
| H2 5 | पितर क्यों बनते हैं? | पितर बंधे क्यों रहते हैं? | The heading did not match what the section answers (report section 4, authenticity flag 3, Sanskrit review item 3); the review's wording, matching the English |

## English (`who_real_doer_karma_ego_bhagavad_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening | (none) | In Bhagavad Gita 3.27, Shri Krishna says that all actions are carried out by the qualities of nature, yet a person deluded by ego believes, "I am the doer." The real doer is prakriti; our actions happen through us. Believing "I alone do it" is the ego of doership, and seeing through it is where the path to liberation begins. | Direct answer (60 words) early, as report section 5 recommends; built from the verse translation, "They happen through us" and the takeaways. Puts the secondary keywords "Bhagavad Gita 3.27", "I am the doer" and "ego of doership" in the first 100 words |
| H2 1 | Today's Comfort, Yesterday's Earnings | Is Today's Comfort the Fruit of Past Merit? | Question heading suggested in report section 4; the section answers it |
| H2 8 | Reading the Verse Step by Step | Reading Gita 3.27 Step by Step | Verse number in the heading for verse searches (report section 4); the section explains Gita 3.27 phrase by phrase |

The headings keep their number and order. No teaching, example, verse, translation, reference or H1 was touched. All five `links` phrases and the `also_read` headings ("मैं नहीं, मेरे माध्यम से" / "Not by Me, but Through Me") are still in the texts word for word, once each; the new paragraphs use none of the link phrases, so every link stays where it was.

## Checklist

- Already met and still met: every item in section 12. `python3 tools/check_seo.py who_real_doer_karma_ego_bhagavad` passes.
- Improved (not a checklist item): a direct answer now comes right after the opening in both languages, and the Hindi body contains the searched "गीता 3.27" and "कर्तापन का अहंकार".

Still unmet: none.

Not changed:
- **"वक्ता" → "आचार्य जी"** (flag 4), **the prapancha etymology** (flag 1) and **the Gita 7.4 addition** (flag 2) are wording and content corrections from the Sanskrit review, not SEO fixes, and stay with the editor.
- **Optional FAQ block** (section 4): it would add a new section, so it is left for the editor.

## Report updates

- Section 2: the keyword notes now say that the `_seo` texts use "गीता 3.27", "कर्तापन का अहंकार", "Bhagavad Gita 3.27" and "ego of doership" in the direct answer paragraph.
- Section 3: notes that the recommended titles, meta descriptions and slugs are the ones in seo.json (they already matched, unchanged).
- Section 8: the `{{HI_POST_URL}}` / `{{EN_POST_URL}}` placeholders are now post URLs built from the slugs (`{{SITE_URL}}/hi/asli-karta-kaun-hai-gita-3-27/`, `{{SITE_URL}}/en/who-is-the-real-doer-gita-3-27/`); headline, alternativeHeadline, description and keywords already matched seo.json.
- Sections 11 and 12: no change needed; seo.json is unchanged and every checklist item was and is met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | asli-karta-kaun-hai-gita-3-27 | asli-karta-kaun-hai-gita-3-27 (unchanged) |
| wordpress.en.slug | who-is-the-real-doer-gita-3-27 | who-is-the-real-doer-gita-3-27 (unchanged) |
| focus_keyword, secondary_keywords, title, meta_description | (as before) | unchanged: the focus keywords were already the searched wording and in the first 100 words, and title and meta still contain them |
| links, also_read | (as before) | unchanged (no edit touched a phrase or heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | asli-karta-kaun-hai-gita-3-27 | who-is-the-real-doer-gita-3-27 |
| focus_keyword | असली कर्ता कौन है | who is the real doer |
| title | असली कर्ता कौन है? गीता के अनुसार कर्म और अहंकार | Who Is the Real Doer? Bhagavad Gita 3.27 on Karma and Ego |
| meta_description | असली कर्ता कौन है? आचार्य उपेंद्र जी भगवद्गीता ३.२७ से समझाते हैं कि सारे कर्म प्रकृति के गुणों से होते हैं, और 'मैं ही करता हूं' मानना अहंकार है। | Who is the real doer of your actions? Acharya Upendra Ji explains Bhagavad Gita 3.27: nature's qualities do every action, and 'I alone do it' is ego. |
