durva_red_flowers_lord_ganesh_worship: SEO fix

The report had no section 12 checklist yet, and `check_seo.py` failed: the focus keywords "गणेश जी को दूर्वा क्यों चढ़ाते हैं" / "why durva is offered to Ganesha" (the searched wording) appeared in neither body, title tag nor meta description, nor in the English slug. The opening also asked "why" without answering it before the first H2. Each language gets two changes: a short direct answer after the intro that uses the searched wording, built only from what the blog already says (and the report's section 5), and the durva H2 phrased as the question it answers. The focus keywords stay; the titles, meta descriptions and English slug now contain them.

## Hindi (`durva_red_flowers_lord_ganesh_worship_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…प्रतीकात्मक रहस्य खोलते हैं।") | (none) | गणेश जी को दूर्वा क्यों चढ़ाते हैं, और लाल फूल क्यों? संक्षेप में, उनके ध्यान मंत्र में बार-बार आने वाला "रक्त" रजस शक्ति का प्रतीक है: खून-पसीना एक करके कर्म करने की तैयारी। दूर्वा तीन गुण, तीन शरीर, तीन काल और तीन अवस्थाओं के अर्पण का प्रतीक है, और हवा में झुकने वाली यह घास विनम्रता सिखाती है। | Direct answer (about 58 words) taken from the report's section 5 and the blog's own sections; puts the focus keyword, which the body never used, in the first 100 words. It quotes no verse meaning (flag 1). The "रजस शक्ति" link now lands on this first plain-text mention. |
| H2 before "दूर्वा शास्त्रों में वर्णित…" | ## दूर्वा: तीन-तीन का अर्पण | ## दूर्वा क्यों चढ़ाते हैं: तीन-तीन का अर्पण | Report section 4: the section answers this question. Number and order of headings unchanged. |

## English (`durva_red_flowers_lord_ganesh_worship_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…hidden in this tradition.") | (none) | In short, here is why durva is offered to Ganesha, along with red flowers. The "red" repeated in his meditation verse points to rajas shakti: the readiness to pour your blood and sweat into your work. Durva stands for offering him the three gunas, three bodies, three times and three states, and this grass, which bends in the wind, teaches humility. | Direct answer of 60 words from the report's section 5 and the blog's sections; puts the focus keyword word for word in the first 100 words. The "rajas shakti" link now lands here; "the three states" is avoided so that link stays on the list item. |
| H2 before "Durva represents the sets of three…" | ## Durva: Offering Everything That Comes in Threes | ## Why Offer Durva? Offering Everything That Comes in Threes | Report section 4: phrased as the reader's question, which the section answers. Number and order of headings unchanged. |

No teaching, example, verse, translation, reference, H1 or order of ideas changed, and the Markdown is kept. All four `links` phrases and the `also_read` heading ("क्या मैं संघर्ष से डरता हूँ?" / "Do You Shy Away from Struggle?") are still in both texts (checked with grep), and the rebuild printed no Note lines.

## Checklist

- Now met: focus keyword in the SEO title, meta description, body text and English slug (both languages); within the first 100 words; focus keyword taken from wording the article uses; the searched-wording mismatch is settled. `check_seo.py` passes (it failed before).
- Still unmet (1): "No unsupported scriptural claims". The Puranic story of Ganesha covered in the demons' blood is unsourced (flag 4), and the Hindi verse meaning is incomplete (review issue 1, Major). These are not SEO fixes, and verses, translations and the story may not be changed here; left for the editor in the original blog.
- Left alone on purpose: "पुराण की कथा, जीवन का अर्थ" / "An Old Story, a Lesson for Today" was not renamed (report section 4, optional): one question H2 per language is enough, and the new name would describe the unsourced story more prominently. No FAQ added (optional, and the FAQ stays in the report). Review issues 2–4 (verse reference, IAST ṃ, Vinayaka gloss) concern verses and glosses, which this fix may not touch. The report's sections 1 and 10 were not edited (only sections 2, 3, 8, 11 and 12 may be).

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | गणेश जी को दूर्वा और लाल फूल क्यों चढ़ाते हैं? | गणेश जी को दूर्वा क्यों चढ़ाते हैं, और लाल फूल क्यों? (53) |
| title.en | Why Durva and Red Flowers Are Offered to Lord Ganesha | Why Durva Is Offered to Ganesha, and Why Red Flowers (52) |
| wordpress.hi.meta_description | गणेश पूजा में लाल फूल और दूर्वा क्यों चढ़ाते हैं? आचार्य उपेंद्र जी बताते हैं प्रतीकात्मक अर्थ: रजस शक्ति, तीन-तीन का अर्पण और झुकने वाली दूर्वा की विनम्रता। | गणेश जी को दूर्वा क्यों चढ़ाते हैं और लाल फूल क्यों? आचार्य उपेंद्र जी बताते हैं प्रतीकात्मक अर्थ: रजस शक्ति, तीन-तीन का अर्पण और झुकने वाली दूर्वा की विनम्रता। (160) |
| wordpress.en.meta_description | Why are red flowers and durva offered to Ganesha? Acharya Upendra Ji explains the meaning: rajas shakti, offering the triads, and the grass that bows. | Why durva is offered to Ganesha, and why red flowers: Acharya Upendra Ji explains rajas shakti, offering the sets of three, and the grass that bows. (148) |
| wordpress.hi.slug | ganesh-ji-ko-durva-kyon-chadhate-hain | ganesh-ji-ko-durva-kyon-chadhate-hain (unchanged; already fits the keyword) |
| wordpress.en.slug | why-durva-red-flowers-for-ganesha | why-durva-is-offered-to-ganesha (31 characters, contains the keyword, unique) |

Focus keywords, secondary keywords, `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2, 3 and 8 were updated to match, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ganesh-ji-ko-durva-kyon-chadhate-hain | why-durva-is-offered-to-ganesha |
| focus_keyword | गणेश जी को दूर्वा क्यों चढ़ाते हैं | why durva is offered to Ganesha |
| title | गणेश जी को दूर्वा क्यों चढ़ाते हैं, और लाल फूल क्यों? | Why Durva Is Offered to Ganesha, and Why Red Flowers |
| meta_description | गणेश जी को दूर्वा क्यों चढ़ाते हैं और लाल फूल क्यों? आचार्य उपेंद्र जी बताते हैं प्रतीकात्मक अर्थ: रजस शक्ति, तीन-तीन का अर्पण और झुकने वाली दूर्वा की विनम्रता। | Why durva is offered to Ganesha, and why red flowers: Acharya Upendra Ji explains rajas shakti, offering the sets of three, and the grass that bows. |
