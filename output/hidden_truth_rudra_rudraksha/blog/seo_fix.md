hidden_truth_rudra_rudraksha: SEO fix

The report had no section 12 checklist yet, so this fix added it (from `tools/prompts/seo_checklist.md`) and marked it for the `_seo` texts. Before the fix, `check_seo.py` failed: the Hindi focus keyword was not in the body, and the English focus keyword was in neither the body nor the meta description.

## Hindi (`hidden_truth_rudra_rudraksha_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new paragraph after "…और यह अर्थ आपके रोज़ के जीवन को छूता है।" | (none) | संक्षेप में, आचार्य जी के अनुसार रुद्राक्ष का अर्थ प्रतीकात्मक है। रुद्र क्रोध नहीं, बल्कि वह है जिसके न रहने पर रोना आता है, और रुद्राक्ष अर्थात् गुरु के आँसू, क्योंकि गुरु ही शिव हैं। रुद्राक्ष धारण करने का अर्थ है हर कर्म से पहले गुरु का स्मरण: "क्या उनकी आँखों में आँसू आएँगे?" | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 50 words is built only from the blog's own sections and सार (report section 5). It puts the keyword in the first 100 words, presents the reading as Acharya Ji's, and leaves out the "अक्ष = आँसू" gloss the Sanskrit review marks wrong. It does not repeat the link phrase "गुरु ही शिव है और शिव ही गुरु है". |
| Third H2 | ## रुद्र: जिसकी कमी रुलाती है | ## रुद्र का अर्थ क्या है? | Rephrased as the question readers search for (secondary keyword "रुद्र का अर्थ", report section 4). The section answers it directly. The number and order of headings are unchanged. |

## English (`hidden_truth_rudra_rudraksha_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new paragraph after "…and it touches your everyday life." | (none) | In short, the rudraksha meaning Acharya Ji gives is symbolic. Rudra is not anger but whatever brings you to tears when it is gone, and rudraksha means the tears of the Guru, because the Guru is Shiva. To wear rudraksha is to remember the Guru before every action: "Will this bring tears to the Guru's eyes?" | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 57 words uses only what the blog already says (its sections and Key Takeaways). The keyword is now within the first 100 words. It avoids the "aksha = tears" gloss (review item 1) and does not repeat the link phrase "the Guru is Shiva and Shiva is the Guru". |
| Third H2 | ## Rudra: The One Whose Absence Makes You Weep | ## What Does Rudra Mean? | Rephrased as the question readers search for (secondary keyword "meaning of Rudra", report section 4). The section answers it directly. The number and order of headings are unchanged. |

No teaching, example or order of ideas changed. The H1, verses, their translations and references are untouched, and the Markdown format is kept. All five `links` phrases and the `also_read` heading ("वेद नहीं, वेदांत" / "Not the Vedas, but Vedanta") are still in both texts once each, confirmed by grep. The inline image's heading ("गुरु क्यों रोते हैं?" / "Why Does the Guru Weep?") is unchanged. `rebuild_blogs.sh` printed no "Note:" lines.

## Checklist

- Now met: the focus keyword is in the body text in both languages and in the English meta description (the three check_seo errors), and within the first 100 words. Both languages have an early direct answer of about 40–60 words. Each language now has three H2s phrased as natural questions (the new one, "रुद्राक्ष: शिव के आँसू या गुरु के?" / "Rudraksha: Shiva's Tears or the Guru's?" and "गुरु क्यों रोते हैं?" / "Why Does the Guru Weep?").
- Already met and still met: every other item in the new section 12 except the one below. `check_seo.py` passes.
- Still unmet (1): "Each tag can be shared by at least 3 posts". The tag Rudraksha / रुद्राक्ष is used by this post only, and Shiva / शिव by two. Tags are outside what this fix may change; left for a later `/seo_blog` pass.
- Left alone on purpose:
  - The Sanskrit review issues (the aksha gloss, the Purva Mimamsa gloss, the Shiva Purana "खंड", half-verse labels, सुदुर्लभ, plural ते in 9.21, the 18.66 lead-in, "काल्पनिक कथा", the ज्ञानेंद्रियाँ gloss, the optional Brihadaranyaka 3.9.4 reference) are content corrections, not SEO items. They touch verses, translations or teaching, which this fix must not change, so they are left for the editor to apply in the original blog.
  - The report's sections 1, 4, 5, 6 and 10 still describe the original texts. This fix may only edit sections 2, 3, 8, 11 and 12.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | What does rudraksha really mean? Acharya Upendra Ji explains Rudra as what we weep for when it is gone, and wearing rudraksha as remembering the Guru. | What is the true rudraksha meaning? Acharya Upendra Ji explains Rudra as what we weep for when it is gone, and wearing rudraksha as remembering the Guru. |
| wordpress.hi.slug | rudraksha-ka-arth | rudraksha-ka-arth (unchanged) |
| wordpress.en.slug | rudraksha-meaning | rudraksha-meaning (unchanged) |

The English meta description changed because "rudraksha really mean" did not match the focus keyword "rudraksha meaning" (153 characters now). The focus keywords already were the searched wording and are now in the body, so the focus keywords, secondary keywords, slugs, titles, the Hindi meta description, `links` and `also_read` stay as they were. The report's section 11 and section 8 (the English schema description) carry the new meta description. Section 3 marks the meta descriptions and slugs in seo.json as recommended (the titles were already marked), section 2 has a keyword note, and section 12 is the new checklist.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | rudraksha-ka-arth | rudraksha-meaning |
| focus_keyword | रुद्राक्ष का अर्थ | rudraksha meaning |
| title | रुद्राक्ष का अर्थ: रुद्र कौन है और गुरु क्यों रोते हैं | Rudraksha Meaning: Who Is Rudra and Why the Guru Weeps |
| meta_description | रुद्राक्ष का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि रुद्र क्रोध नहीं, वह है जिसकी कमी रुलाती है, और रुद्राक्ष धारण करना गुरु का निरंतर स्मरण क्यों है। | What is the true rudraksha meaning? Acharya Upendra Ji explains Rudra as what we weep for when it is gone, and wearing rudraksha as remembering the Guru. |
