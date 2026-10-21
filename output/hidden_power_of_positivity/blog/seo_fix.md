hidden_power_of_positivity: SEO fix

The report had no section 12 checklist yet, so this fix added it (from `tools/prompts/seo_checklist.md`) and marked it for the `_seo` texts. Before the fix, `check_seo.py` failed: the Hindi focus keyword was not in the body, and the English focus keyword was in neither the body nor the meta description.

## Hindi (`hidden_power_of_positivity_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, second paragraph | वेद का एक छोटा सा शांति मंत्र इस प्रश्न को पूरी तरह पलट देता है। | वेद का एक छोटा सा शांति मंत्र, "भद्रं कर्णेभिः", इस प्रश्न को पूरी तरह पलट देता है। | Names the mantra people search for in the intro (report section 4). The intro only said "a peace mantra". |
| Intro, new paragraph after "…उसके एक-एक शब्द में उतरें।" | (none) | संक्षेप में, भद्रं कर्णेभिः मंत्र का अर्थ है: हे देवताओं, हम कानों से शुभ ही सुनें और आँखों से शुभ ही देखें। आचार्य जी के अनुसार भद्र वह नहीं जो प्रिय लगे, बल्कि वह है जिसका परिणाम कल्याणकारी हो, और भद्र देखना यानी हर वस्तु के पीछे का यज्ञ भाव (त्याग) देखना। | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 50 words takes its meaning from the blog's own verse block and Key Takeaways. It puts the keyword in the first 100 words and presents the yajna reading as Acharya Ji's, as Sanskrit review issue 2 asks. It does not repeat the link phrase "जो केवल प्रिय है, वह भद्र नहीं". |
| First H2 | ## एक मंत्र, जिसे हम रोज़ दोहराते हैं | ## भद्रं कर्णेभिः मंत्र का अर्थ क्या है? | Rephrased as the question readers search for (report section 4). The section answers it word by word. The number and order of headings are unchanged. |

## English (`hidden_power_of_positivity_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, second paragraph | A short Vedic peace mantra turns that question completely on its head. | A short Vedic peace mantra, Bhadram Karnebhih, turns that question completely on its head. | Names the mantra people search for in the intro (report section 4). |
| Intro, new paragraph after "…one word at a time." | (none) | Put briefly, the Bhadram Karnebhih meaning is a prayer: O gods, may we hear with our ears what is auspicious, and see with our eyes what is auspicious. Acharya Ji explains that bhadra is not what pleases us but what leads to our well-being, and that seeing what is bhadra means seeing the spirit of sacrifice behind everything. | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 57 words uses only the blog's own verse meaning and Key Takeaways. The keyword is now within the first 100 words. It avoids repeating the link phrase "Whatever merely pleases is not bhadra". |
| First H2 | ## A Mantra We Recite Every Day | ## What Does Bhadram Karnebhih Mean? | Rephrased as the question readers search for (report section 4). The section answers it. The number and order of headings are unchanged. |

No teaching, example or order of ideas changed. The H1, verses, their translations and references are untouched, and the Markdown format is kept. All four `links` phrases and the `also_read` heading ("क्या "भद्र" का अर्थ "मीठा" है?" / "Does "Bhadra" Mean "Pleasant"?") are still in both texts once each, confirmed by grep. The inline image's heading ("बंगले को नहीं, तपस्या को देखो") is unchanged. `rebuild_blogs.sh` printed no "Note:" lines.

## Checklist

- Now met: the focus keyword is in the body text in both languages and in the English meta description (the three check_seo errors), and within the first 100 words. Both languages have an early direct answer of about 40–60 words. Each language now has two H2s phrased as natural questions (the new one and "क्या हर यज्ञ शुभ है?" / "Is Every Sacrifice Auspicious?").
- Already met and still met: every other item in the new section 12. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - The Sanskrit review issues (Markandeya's "sixteen kalpas", the yajatrāḥ vocative, the incomplete Gita 3.14-15 meaning, the mantra marked as complete, parjanya, हेयम्, phalashruti and others) are content corrections, not SEO items. They touch verses, translations or teaching, which this fix must not change, so they are left for the editor to apply in the original blog.
  - The report's section 4 also suggests turning some H2s into H3s. Not done: the number of `##` sections has to stay the same so that images and the Also read box keep their place.
  - The report's sections 1, 4, 5, 6 and 10 still describe the original texts. This fix may only edit sections 2, 3, 8, 11 and 12.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | What does Bhadram Karnebhih really mean? Acharya Upendra Ji explains why auspicious is not pleasant, and how to see the sacrifice behind everything. | What is the Bhadram Karnebhih meaning? Acharya Upendra Ji explains why auspicious is not pleasant, and how to see the sacrifice behind everything. |
| wordpress.hi.slug | bhadram-karnebhih-mantra-ka-arth | bhadram-karnebhih-mantra-ka-arth (unchanged) |
| wordpress.en.slug | bhadram-karnebhih-meaning | bhadram-karnebhih-meaning (unchanged) |

The English meta description changed because "really mean" did not match the focus keyword "Bhadram Karnebhih meaning" (146 characters now). The focus keywords already were the searched wording and are now in the body, so the focus keywords, secondary keywords, slugs, titles, the Hindi meta description, `links` and `also_read` stay as they were. The report's section 11 and section 8 (the English schema description) carry the new meta description. Section 3 marks the meta descriptions and slugs in seo.json as recommended (the titles were already marked), section 2 has a keyword note, and section 12 is the new checklist.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bhadram-karnebhih-mantra-ka-arth | bhadram-karnebhih-meaning |
| focus_keyword | भद्रं कर्णेभिः मंत्र का अर्थ | Bhadram Karnebhih meaning |
| title | भद्रं कर्णेभिः मंत्र का अर्थ: शुभ सुनो, शुभ देखो | Bhadram Karnebhih Meaning: The Hidden Power of Positivity |
| meta_description | भद्रं कर्णेभिः मंत्र का अर्थ क्या है? आचार्य उपेंद्र जी बताते हैं कि भद्र सुनना यानी कल्याणकारी सुनना, और भद्र देखना यानी हर वस्तु के पीछे का त्याग देखना। | What is the Bhadram Karnebhih meaning? Acharya Upendra Ji explains why auspicious is not pleasant, and how to see the sacrifice behind everything. |
