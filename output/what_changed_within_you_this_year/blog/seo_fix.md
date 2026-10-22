what_changed_within_you_this_year: SEO fix

The original blog texts are unchanged. The fixes are in `what_changed_within_you_this_year_blog_seo.txt` (Hindi) and `what_changed_within_you_this_year_blog_seo_en.txt` (English).

## Hindi changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| Introduction, new paragraph after "जो हर साधक को हर साल खुद से पूछना चाहिए।" | (none) | संक्षेप में चातुर्मास का महत्व: ये वर्षा ऋतु के चार महीने हैं। आचार्य जी के अनुसार अधिकतर त्योहार इसी समय आते हैं, क्योंकि पैदल चलने वाले ऋषि बरसात में किसी एक गांव में ठहर जाते थे और गांव उनके मार्गदर्शन में धार्मिक उपक्रम इसी काल में करता था। ब्रह्मचर्य की तैयारी पूरी होने पर फिर विवाह का मौसम आता है। | Puts the focus keyword and searched wording "चातुर्मास का महत्व" in the body and the first 100 words (the body only said "चातुर्मास", first in the H2), and adds an early direct answer (60 words). Built only from the blog's own sections (चातुर्मास, the rishis' monsoon stay, the wedding season) and attributed to Acharya Ji as in the blog. |
| H2 of the third section | ## चार महीने, एक गांव, पूरा मार्गदर्शन | ## अधिकतर त्योहार चातुर्मास में ही क्यों आते हैं? | Question heading readers search for ("चातुर्मास में त्योहार क्यों"); the section ends with exactly that answer. Number and order of headings unchanged. |

## English changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| Introduction, new paragraph after "one that every seeker should ask themselves each year." | (none) | In short, the significance of Chaturmas, the four monsoon months, is this: according to Acharya Ji, most festivals fall in this season because the sages, who travelled on foot, stayed in a single village through the rains, and the village carried out its religious observances under their guidance. Once the preparation of brahmacharya is complete, the wedding season follows. | Puts the focus keyword "significance of Chaturmas" in the body and the first 100 words, and adds an early direct answer (59 words), built only from what the blog says. |
| H2 of the third section | ## Four Months, One Village, Complete Guidance | ## Why Do Most Festivals Fall in Chaturmas? | Question heading matching "why festivals fall in Chaturmas"; the section answers it. Number and order of headings unchanged. |

## Checklist

Now met:
- Focus keyword in the body text (both languages; `tools/check_seo.py` failed on this before).
- Focus keyword in the meta description (both languages; also failed before).
- Focus keyword within the first 100 words (both languages).
- Direct answer placed early, and a question heading for the main question (report sections 4 and 5).

Still unmet (1):
- "Each tag can be shared by at least 3 posts": the tag "Chaturmas" / "चातुर्मास" is used by only 2 posts so far. Not fixable from the blog text; it fits future Chaturmas-season posts.

Deliberately not done:
- The "Also read" heading "चातुर्मास: चार महीने का ठहराव" / "Chaturmas: Four Months of Pause" and "हर साल का एक प्रश्न" / "A Question for Every Year" were kept (the first is an `also_read` heading; the report advises keeping the second so it does not repeat the H1).
- The Sanskrit review's points (verse reference, "every religion places the Guru above God", Chaturmas dates, उपक्रम gloss, "bhavati" gloss, mixed glosses) touch verses, references or teaching wording, which an SEO fix must not change. They are left for the editor.
- "chaturmas me shadi kyu nahi hoti" is not targeted: the talk does not answer it (report flag 7).

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | अधिकतर त्योहार चातुर्मास में क्यों आते हैं और फिर विवाह क्यों? आचार्य उपेंद्र जी बताते हैं ऋषियों का वर्षा में ठहराव और त्योहारों का प्रश्न: भीतर क्या बदला? | चातुर्मास का महत्व: अधिकतर त्योहार इन्हीं चार महीनों में क्यों आते हैं और फिर विवाह क्यों? आचार्य उपेंद्र जी बताते हैं ऋषियों का ठहराव और त्योहारों का प्रश्न। |
| wordpress.en.meta_description | Why do most Hindu festivals fall in Chaturmas, and why do weddings follow? Acharya Upendra Ji explains the sages' monsoon stay and what each festival asks. | Significance of Chaturmas: why most festivals fall in the monsoon and weddings follow. Acharya Upendra Ji explains the sages' stay and what festivals ask. |
| wordpress.hi.slug | chaturmas-ka-mahatva | unchanged |
| wordpress.en.slug | significance-of-chaturmas | unchanged |
| focus_keyword, secondary_keywords, title (hi, en) | (as below) | unchanged: the searched wording was already the focus keyword and is now in the text |
| links, also_read | (unchanged) | unchanged (no edit touched a link phrase or the Also read heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | chaturmas-ka-mahatva | significance-of-chaturmas |
| focus keyword | चातुर्मास का महत्व | significance of Chaturmas |
| title | चातुर्मास का महत्व: त्योहार इन्हीं महीनों में क्यों आते हैं | Significance of Chaturmas: Why Festivals Come in Monsoon |
| meta description | चातुर्मास का महत्व: अधिकतर त्योहार इन्हीं चार महीनों में क्यों आते हैं और फिर विवाह क्यों? आचार्य उपेंद्र जी बताते हैं ऋषियों का ठहराव और त्योहारों का प्रश्न। | Significance of Chaturmas: why most festivals fall in the monsoon and weddings follow. Acharya Upendra Ji explains the sages' stay and what festivals ask. |
