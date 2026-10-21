ghee_more_than_food: SEO fix

The fixed texts are `ghee_more_than_food_blog_seo.txt` (Hindi) and `ghee_more_than_food_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes

| where | before | after | why |
|---|---|---|---|
| Opening section, paragraph 1 | पर गुरुदेव इसे एक बिल्कुल अलग दृष्टि से देखते हैं। | पर आचार्य जी इसे एक बिल्कुल अलग दृष्टि से देखते हैं। | Consistent entity naming for AI search attribution (report flag 6, review item 4); the post already says आचार्य जी later |
| Opening section, new paragraph after "...उसे घी के समान समझो।" | (none) | आचार्य जी के अनुसार घी का आध्यात्मिक महत्व यह है: पेट में चल रहे सहज यज्ञ में घी उस अग्नि का तेज है। जो वसा हम खाते हैं, उसका एक भाग हमारी वाणी बनता है, इसलिए जैसा घी हम ग्रहण करते हैं, वैसी ही हमारी वाणी बनती है। | Focus keyword was not in the body or the first 100 words; adds a short direct answer (≈47 words) built only from the blog's own sections 1–3 |

## English changes

| where | before | after | why |
|---|---|---|---|
| Opening section, paragraph 1 | The Guru sees it in an entirely different light. | Acharya Ji sees it in an entirely different light. | Consistent entity naming for AI search attribution (report flag 6, review item 4); the post already says Acharya Ji later |
| Opening section, new paragraph after "...think of it as ghee." | (none) | The spiritual significance of ghee, as Acharya Ji explains it, is this: digestion is a natural yajna in the stomach, and ghee is the tejas of that inner fire. Part of the fat we eat becomes our speech, so the ghee we choose shows in the way we speak. | Focus keyword was not in the body or the first 100 words; adds a short direct answer (48 words) built only from the blog's own sections 1–3 |

Not changed: the H1, the `##` headings (the first two are already natural questions, the third is the `also_read` heading, the fourth is the summary), the Khadgamala verse, its translation and reference, every `links` phrase and the `also_read` heading, the order of ideas and all teachings.

## Checklist

Now met:
- Focus keyword in the body text (both languages)
- Focus keyword within the first 100 words (both languages; word 82 in Hindi, 83 in English)
- Focus keyword taken from wording the article uses (the `_seo` texts)
- Direct answer (40–60 words) early in the post

Still unmet:
- No unsupported scriptural claims: the Khadgamala line (सर्वरोगहरचक्रस्वामिनी, रहस्ययोगिनी) is presented as the goddess of the Vishuddhi chakra, while it belongs to the Sri Chakra's seventh avarana (report flag 1, review item 1). Fixing it changes the scripture passage's introduction and attribution, which the SEO fix may not do; left to the editor.

## seo.json changes

| field | before | after |
|---|---|---|
| (none) | | |

No seo.json change was needed: the focus keywords already were the searched wording and now appear in the `_seo` texts; the title, meta description, slugs (`ghee-ka-adhyatmik-mahatva`, `spiritual-significance-of-ghee`), links and also_read stay as they were.

## Final seo.json values

| field | Hindi | English |
|---|---|---|
| slug | ghee-ka-adhyatmik-mahatva | spiritual-significance-of-ghee |
| focus keyword | घी का आध्यात्मिक महत्व | spiritual significance of ghee |
| title | घी का आध्यात्मिक महत्व: भीतर का यज्ञ और वाणी | Spiritual Significance of Ghee: Inner Fire and Speech |
| meta description | घी का आध्यात्मिक महत्व क्या है? आचार्य उपेंद्र जी बताते हैं कि पेट में एक सहज यज्ञ चलता है, घी उसका तेज है, और जो हम खाते हैं वही हमारी वाणी बनता है। | What is the spiritual significance of ghee? Acharya Upendra Ji explains the inner yajna of digestion and how what we eat becomes the way we speak. |
