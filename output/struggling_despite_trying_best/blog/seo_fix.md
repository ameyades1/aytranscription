struggling_despite_trying_best: SEO fix

`check_seo.py` passed before the fix, but neither body used its focus keyword: the Hindi "पूरी कोशिश के बाद भी संघर्ष क्यों" was only in the H1 (which SureRank does not count as body text), and the English "struggling despite trying your best" (the video's own title) did not appear at all. Neither opening gave a short answer to the question. The report also had no section 12 checklist. The changes:
- a short direct answer, built only from what the blog already says (report section 5), that brings in the focus keyword within the first 100 words (Hindi: word 85, English: word 90);
- one heading rephrased as the question readers search for (report section 4);
- the Sanskrit review's wording corrections that touch no verse or reference (review issues 1, 2, 3 and 5; report flags 1, 2, 3 and 5).

The focus keywords, slugs, titles and meta descriptions stay the same.

## Hindi (`struggling_despite_trying_best_blog_seo.txt`): 6 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new fourth paragraph (after "…तो संघर्ष निश्चित है।") | (none) | तो पूरी कोशिश के बाद भी संघर्ष क्यों होता है? क्योंकि हमारा लक्ष्य ज्ञान नहीं, सुख होता है। ज्ञान तो आना ही है: या तो ज्ञानयुक्त कर्म से, या कटु अनुभव से। इसलिए कर्म से पहले चिंतन करें, गुरु से जानें, और हर घटना से पूछें कि उसने आपको क्या सिखाया। | The focus keyword was missing from the body text and the first 100 words, and the opening gave no direct answer. This answer (about 50 words) uses only the blog's own points (aim at knowledge, not pleasure; ज्ञानयुक्त कर्म or कटु अनुभव; think first, ask the Guru, ask what each event taught). |
| Seventh H2 | ## समय केवल समय है | ## अच्छा समय और बुरा समय किसलिए है? | The question form suggested in report section 4, close to the searched "बुरे समय में क्या करें". The section answers it (good times for service, bad times for reflection, study and meditation). |
| Same section, first sentence | महर्षि मंकि की गीता (मंकि गीता) सिखाती है कि अच्छा या बुरा समय… | आचार्य जी मंकि गीता के संदर्भ में बताते हैं कि अच्छा या बुरा समय… | Content trust: the review cannot confirm this in the Manki Gita, so it is given as Acharya Ji's reading, and "महर्षि" is dropped (review issues 1 and 5; the review's own wording). |
| Same section, before the list | पर मंकि गीता के अनुसार इनका उद्देश्य अलग है: | पर आचार्य जी के अनुसार इनका उद्देश्य अलग है: | Content trust: review issue 1, the review's own wording. |
| "निःस्वार्थ सेवा और योगक्षेम का वचन", paragraph after the verse | …उसकी रक्षा करना। जो अनन्य भाव से… | …उसकी रक्षा करना। आचार्य जी यहाँ भगवान के अनन्य चिंतन को लोगों की सेवा के रूप में देखते हैं: जो अनन्य भाव से… | Content trust: the bridge from review issue 2, so Acharya Ji's application is not read as the verse's own meaning (the English already had it). The verse and its translation are untouched. |
| "मुख्य बातें", seventh item | - निःस्वार्थ सेवा करने वाले का योगक्षेम… (गीता ९.२२) | - आचार्य जी के अनुसार, निःस्वार्थ सेवा करने वाले का योगक्षेम… (गीता ९.२२) | Content trust: review issue 3. The reference itself is kept as it was. |

## English (`struggling_despite_trying_best_blog_seo_en.txt`): 5 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new fourth paragraph (after "…struggle is guaranteed.") | (none) | So why are you still struggling despite trying your best? Because we aim at pleasure rather than understanding. The lesson comes either way: through action guided by knowledge, or through bitter experience. So reflect before you act, seek the Guru's guidance, and ask of every event what it is teaching you. | The focus keyword was missing from the body, and the opening gave no direct answer. This answer (about 50 words) is report section 5's, built from the blog's own points. It also echoes the searched "why am I still struggling". |
| Seventh H2 | ## Time Is Just Time | ## What Are Good and Bad Times For? | The question form suggested in report section 4, close to "what to do in bad times"; the section answers it. |
| Same section, first sentence | Maharshi Manki's Gita teaches that there is… | Drawing on the Manki Gita, Acharya Ji teaches that there is… | Content trust: review issues 1 and 5, the review's own wording. |
| Same section, before the list | According to Maharshi Manki's Gita, though, these periods serve… | In Acharya Ji's teaching, though, these periods serve… | Content trust: review issue 1. The review's "As Acharya Ji explains" would repeat the next paragraph's opening ("As Acharya Ji explains, what we call…"), so the same attribution is worded differently. |
| "Key Takeaways", seventh item | - For those who serve selflessly, God Himself… (Gita 9.22) | - In Acharya Ji's reading, for those who serve selflessly, God Himself… (Gita 9.22) | Content trust: review issue 3. The reference itself is kept as it was. |

Nothing else changed:
- no teaching, example, H1 or order of ideas, and no heading count or order;
- the Gita 9.22 verse, its translation and its references are untouched in both languages;
- the H2 "कर्म से पहले चिंतन" / "Reflect Before You Act" (used by `images.txt`) and the `also_read` heading "निःस्वार्थ सेवा और योगक्षेम का वचन" / "Selfless Service and the Promise of Yogakshema" are untouched.

A grep finds all five `links` phrases and the `also_read` heading in both texts, word for word, and each focus keyword once in its body ("संघर्ष निश्चित है" / "struggle is guaranteed" still comes before the new paragraph, so the link stays on the original sentence).

## Checklist

- Now met:
  - Focus keyword in the body text (both languages).
  - Focus keyword within the first 100 words (both languages).
- Section 12 was missing from the report and has been added, marked against the fixed texts. `check_seo.py` passes.
- Still unmet (2):
  - Each tag can be shared by at least 3 posts: "कर्म योग सीरीज़" / "Karma Yog Series" is used by this post only so far. It is the series' own name, and this fix does not change tags.
  - No unsupported scriptural claims: mostly met now. Review issues 4 (add the Gita 8.15 reference and sandhi form to "दुःखालयम् अशाश्वतम्") and 6 (IAST ṃ and "yogakṣemaṃ" in the 9.22 transliteration) change a verse reference or transliteration, which the SEO fix may not touch; they are left for the editor. "अनेक श्लोकों में यह परखा जा चुका है" / "Shloka after shloka has tested and confirmed this" still cites no verse; it is Acharya Ji's statement and is left as it is.
- Left alone on purpose:
  - No new H3 "गीता ९.२२ का अर्थ" / "Bhagavad Gita 9.22 Meaning" (report section 4): it would add a heading, and the fix keeps the heading count.
  - The focus keyword is not put into a heading: the first H2 matches the hero image, and no other heading reads naturally with it.

## seo.json changes

None. The focus keywords now appear in both bodies as they are, so `focus_keyword`, `secondary_keywords`, `slug`, `title`, `meta_description`, `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged.

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | poori-koshish-ke-baad-bhi-sangharsh-kyon | poori-koshish-ke-baad-bhi-sangharsh-kyon (unchanged) |
| wordpress.en.slug | struggling-despite-trying-your-best | struggling-despite-trying-your-best (unchanged) |

Report: section 11 holds the same JSON. Section 2 has a new keyword note. Section 3 already marked the recommended titles, meta descriptions and slugs exactly as in seo.json. Section 8 now names the URL slugs for the post-URL placeholders; its headlines, descriptions and keywords already matched. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | poori-koshish-ke-baad-bhi-sangharsh-kyon | struggling-despite-trying-your-best |
| focus keyword | पूरी कोशिश के बाद भी संघर्ष क्यों | struggling despite trying your best |
| title | पूरी कोशिश के बाद भी संघर्ष क्यों? ज्ञानयुक्त कर्म का रहस्य | Struggling Despite Trying Your Best? Act with Understanding |
| meta description | पूरी कोशिश के बाद भी संघर्ष क्यों? आचार्य जी बताते हैं: ज्ञान आना ही है, या समझ से या कटु अनुभव से। कर्म से पहले चिंतन करें और हर अनुभव से सीखें। | Struggling despite trying your best? Acharya Ji explains that life teaches either way: through understanding before you act, or through bitter experience. |
