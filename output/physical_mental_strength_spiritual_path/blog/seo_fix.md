physical_mental_strength_spiritual_path: SEO fix

The fixed texts are `physical_mental_strength_spiritual_path_blog_seo.txt` (Hindi) and `physical_mental_strength_spiritual_path_blog_seo_en.txt` (English). The originals are unchanged. The Hanuman Chalisa verse, its translation and reference, the H1, every `links` phrase, the `also_read` heading and the inline image's heading ("प्रतिकार शक्ति: महाकाली और भैरवी" / "The Power to Resist: Mahakali and Bhairavi") are untouched. The Sanskrit review's content corrections (tools/review/physical_mental_strength_spiritual_path.md, items 1–6: garima gloss, Hindi chaupai meaning, नौ/नव निधि, the excrement comparison, श्राप → शाप, Hindi glosses) are left for a separate edit, because this fix does not change teachings or claims.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before the first H2) | (none) | साधना में स्वास्थ्य का महत्व आचार्य जी चार सीढ़ियों से समझाते हैं: रोगी से निरोगी, निरोगी से भोगी, भोगी से सिद्धि और सिद्धि से मुक्ति। रोगी अवस्था में न सच्चा भोग संभव है, न मोक्ष, क्योंकि पीड़ा में "मैं शरीर नहीं हूं" टिकता नहीं। पहले शरीर और मन स्वस्थ हों; सिद्धियों का सही उपयोग मुक्ति के बाद ही होता है। | The focus keyword was not in the body at all (`check_seo.py` failed); it now opens the post (word 1). This 60-word paragraph is the early direct answer from report section 5, built only from the blog's four-step sequence, the pain example and the jivanmukta passage |
| H2 | साधना का क्रम: चार सीढ़ियां | साधना में स्वास्थ्य क्यों आवश्यक है? | Question heading readers search (report section 4); the section answers it ("पहली सीढ़ी सबसे आवश्यक है। रोगी अवस्था में किसी को मोक्ष नहीं मिलता।") |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before the first H2) | (none) | Health on the spiritual path comes first. Acharya Ji lays out four steps: illness to health, health to enjoyment, enjoyment to siddhi, and siddhi to liberation. The sick can neither truly enjoy life nor attain moksha, because "I am not the body" does not hold in pain. So heal body and mind first; siddhis are used rightly only after liberation. | The focus keyword was not in the body at all (`check_seo.py` failed); it now opens the post (word 1). The opening section already runs 100 words, so the answer goes before it. This 60-word paragraph is the early direct answer from report section 5, built only from the blog |
| H2 | Four Steps on the Path of Practice | Why Does Health Matter on the Spiritual Path? | Question heading readers search (report section 4); the section answers it ("The first step matters most. Nobody attains moksha while lying sick.") |

## Checklist

Now met:
- Focus keyword in the body text (Hindi and English); `tools/check_seo.py` failed on this before the fix.
- Focus keyword within the first 100 words (Hindi and English).
- Focus keyword taken from wording the article uses (true of the `_seo` texts).
- Early direct answer (40–60 words) in both languages, and a question heading carrying the topic.

Still unmet: none. The report had no section 12 before this fix; it was added with every item met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | sadhana-mein-swasthya-ka-mahatva | unchanged |
| wordpress.en.slug | health-on-the-spiritual-path | unchanged |
| focus keywords, secondary keywords, titles, meta descriptions, links, also_read | | unchanged (titles and metas already contain the focus keywords) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sadhana-mein-swasthya-ka-mahatva | health-on-the-spiritual-path |
| focus_keyword | साधना में स्वास्थ्य का महत्व | health on the spiritual path |
| title | साधना में स्वास्थ्य का महत्व: रोगी से मुक्ति तक | Health on the Spiritual Path: From Illness to Liberation |
| meta_description | साधना में स्वास्थ्य का महत्व: आचार्य जी चार सीढ़ियां बताते हैं, रोगी से निरोगी, भोगी, सिद्धि और मुक्ति, और क्यों मुक्ति से पहले सिद्धियों का उपयोग पतन लाता है। | Why health matters on the spiritual path: Acharya Ji maps four steps, from illness to health, enjoyment, siddhi and liberation, and why siddhis must wait. |
