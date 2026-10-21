rigid_mind_vs_flexible_mind_destiny: SEO fix

`check_seo.py` failed this talk: neither focus keyword was in the body text (SureRank), and the Hindi meta description did not contain "अड़ियल स्वभाव कैसे बदलें". The bodies only said "अड़े हुए" / "अड़ जाएँ" and "rigid", and neither language had an intro before the first `##` heading, so there was no early direct answer. Each language gets three changes: a short direct answer before the first heading, built only from the blog's own lines, with the focus keyword in its first words; and two `##` headings rephrased as the questions their sections answer. The focus keywords and slugs stay the same; only the Hindi meta description changed.

## Hindi (`rigid_mind_vs_flexible_mind_destiny_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| New intro paragraph, after the H1 and before "## क्या भाग्य बदला जा सकता है?" | (none) | अड़ियल स्वभाव कैसे बदलें? आचार्य उपेंद्र जी के अनुसार "हम तो ऐसे ही हैं" कहना दुर्मेधा, यानी बंद बुद्धि का लक्षण है, और जीवन के कई विघ्न इसी कठोरता से आते हैं। उपाय है कुछ समय के लिए अपना स्वभाव बदलकर दूसरे की जगह खड़े हो जाना। लक्ष्य एक रहे, पर स्वभाव परिस्थिति के अनुसार ढलता रहे। | The focus keyword was missing from the body (check_seo error) and there was no direct answer. 57 words, built from the blog's "हम तो ऐसे ही हैं", the दुर्मेधा gloss (जड़ और बंद बुद्धि), "विघ्न इसलिए आते हैं क्योंकि हम कठोर हैं", "अपना स्वभाव बदलकर दूसरे की जगह खड़े हो जाना" and "लक्ष्य एक रहे … स्वभाव परिस्थिति के अनुसार ढलता रहे". The keyword is in the first words. |
| 4th `##` heading | जब दोनों अड़ जाएँ | अड़ियल स्वभाव कैसे बदलें? दूसरे की जगह खड़े होइए | A natural search question; the section gives exactly this remedy ("दूसरे की जगह खड़े हो जाना"). Report section 4's suggestion. |
| 6th `##` heading | ऊँचा उठना है तो लचीला बनना होगा | ऊँचा उठने के लिए लचीलापन क्यों ज़रूरी है? | Question form readers search; the section answers it (FAQ 5). |

## English (`rigid_mind_vs_flexible_mind_destiny_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| New intro paragraph, after the H1 and before "## Can You Change Your Destiny?" | (none) | Rigid mind vs flexible mind: according to Acharya Upendra Ji, saying "this is just how we are" marks durmedha, a closed intellect, and many of life's obstacles come from that rigidity. The way out is to set your own nature aside for a while and stand where the other person stands, keeping one goal while your nature adapts. | The focus keyword was missing from the body (check_seo error) and there was no direct answer. 58 words, built from the blog's "This is just how we are", the durmedha gloss ("a dull, closed intellect"), "Obstacles arise because we are rigid", "Set your own nature aside for a while and stand where the other person stands" and "Keep your goal single … let your nature adapt". The keyword opens the paragraph and matches the video title. |
| 4th `##` heading | When Both Refuse to Budge | How Do You Soften a Rigid Mind? Stand Where the Other Stands | A natural search question; the section gives this remedy. Report section 4's suggestion. |
| 6th `##` heading | To Rise Higher, Learn to Bend | Why Must You Be Flexible to Rise Higher? | Question form readers search; the section answers it (FAQ 5). |

No teaching, example, H1 or order of ideas changed; the blog quotes no verses. The number and order of `##` sections are unchanged, and the Markdown is kept. "एक कमरा, दो सच" / "One Room, Two Truths" (where `images.txt` places inline.jpg) and the `also_read` heading "दूसरे का जीवन कब देखोगे?" / "When Will You Look at Their Life?" are untouched. All five `links` phrases are still in both texts, each once (script check).

## Checklist

- Now met: "In the body text" and "In the meta description" (Hindi), the items `check_seo.py` failed on; "Within the first 100 words" (both languages); and an early direct answer.
- Section 12 was missing from the report. It has now been added from `tools/prompts/seo_checklist.md`, with every item marked against the `_seo` texts and seo.json. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose: the Sanskrit review issues (chatukar etymology, "Mars controls Saturn", योग्यता as "capacity", परमेश्वर का उद्देश्य, निम्न चेतना) are for the editor to fix in the original blog; none is an SEO item. Changing "capacity" would also change an English `links` phrase.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या आप भी कहते हैं, "मैं तो ऐसा ही हूँ"? आचार्य उपेंद्र जी बताते हैं कि अड़ियल स्वभाव से विघ्न क्यों आते हैं और ऊँचा उठने के लिए लचीली बुद्धि क्यों ज़रूरी है। | अड़ियल स्वभाव कैसे बदलें? आचार्य उपेंद्र जी बताते हैं कि "मैं तो ऐसा ही हूँ" की कठोरता से विघ्न क्यों आते हैं और ऊँचा उठने के लिए लचीली बुद्धि क्यों ज़रूरी है। |

Nothing else changed. Both focus keywords ("अड़ियल स्वभाव कैसे बदलें" / "rigid mind vs flexible mind") were already the searched wording and now appear in the `_seo` bodies. The slugs are unchanged (old and new: `adiyal-swabhav-kaise-badlen` / `rigid-mind-vs-flexible-mind`). Titles, the English meta description, `links`, `also_read`, `alt`, `caption`, `related`, category, secondary keywords and tags are unchanged. In the report: section 2 has a keyword note, section 3 and section 8 (Hindi description) show the new Hindi meta description, section 11 matches seo.json, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | adiyal-swabhav-kaise-badlen | rigid-mind-vs-flexible-mind |
| focus_keyword | अड़ियल स्वभाव कैसे बदलें | rigid mind vs flexible mind |
| title | अड़ियल स्वभाव कैसे बदलें? लचीली बुद्धि का रहस्य | Rigid Mind vs Flexible Mind: Who Holds Your Destiny? |
| meta_description | अड़ियल स्वभाव कैसे बदलें? आचार्य उपेंद्र जी बताते हैं कि "मैं तो ऐसा ही हूँ" की कठोरता से विघ्न क्यों आते हैं और ऊँचा उठने के लिए लचीली बुद्धि क्यों ज़रूरी है। | Rigid mind vs flexible mind: Acharya Upendra Ji explains why "I'm just like this" invites obstacles, and why rising higher needs a flexible intellect. |
