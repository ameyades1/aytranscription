overcome_struggles_of_life: SEO fix

The fixed texts are `overcome_struggles_of_life_blog_seo.txt` (Hindi) and `overcome_struggles_of_life_blog_seo_en.txt` (English). The originals are unchanged. The verse, its translation and reference, the H1, every `links` phrase, the `also_read` heading and the inline image's heading ("द्वंद्व: जीवन के विपरीत जोड़े" / "Dvandva: The Pairs of Opposites in Life") are untouched. The Sanskrit review's content corrections (tools/review/overcome_struggles_of_life.md, items 1–8) are left for a separate edit, because this fix does not change teachings or claims; only the heading grammar of item 9 is fixed, as part of a heading rephrased for SEO.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening question (before the first H2) | (none) | जीवन के संघर्षों को कैसे पार करें? गीता २.१४ के अनुसार सुख-दुःख इंद्रियों और विषयों के संयोग से आते-जाते हैं, ये अनित्य हैं। आचार्य जी के अनुसार इसीलिए कोई भी कठिन स्थिति स्थायी नहीं है, पर वह अपने आप भी नहीं जाएगी। पहला कदम है उसे सहन करना; उसके बाद कर्म, यज्ञ, भक्ति, ध्यान और ब्रह्मज्ञान की पूरी यात्रा है। | The focus keyword was not in the body (only in the H1); it now appears in the first 100 words (word 68). This 60-word paragraph is the early direct answer, built only from the blog's verse meaning and takeaways |
| H2 | गीता का पहला उपदेश क्या है? | गीता २.१४ का अर्थ क्या है? | Question heading matching the searched "गीता 2.14 का अर्थ"; the section gives the verse and its meaning. It also drops "पहला उपदेश" from the heading (review item 2) |
| H2 | गीता की अठारह अध्यायों की यात्रा | जीवन के संघर्षों को कैसे पार करें: गीता के अठारह अध्यायों की यात्रा | Focus keyword once in a heading over the section that gives the path after endurance; "की" → "के" (review item 9) |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening question (before the first H2) | (none) | Here is how to overcome struggles in life. According to Bhagavad Gita 2.14, pleasure and pain arise from the contact of the senses with their objects and are impermanent. So no hardship is permanent, Acharya Ji explains, yet it will not leave by itself. Endurance is the first step; then comes the journey of action, sacrifice, devotion, meditation and knowledge. | The focus keyword was not in the body (only "Life's Struggles" in the H1); it now appears in the first 100 words (word 81). This 60-word paragraph is the early direct answer, built only from the blog's verse meaning and takeaways |
| H2 | What Is the Gita's First Teaching? | What Does Bhagavad Gita 2.14 Mean? | Question heading matching the searched "Bhagavad Gita 2.14 meaning"; the section gives the verse and its meaning. It also drops "first teaching" from the heading (review item 2) |
| H2 | The Journey Through the Gita's Eighteen Chapters | How to Overcome Struggles in Life: The Journey Through the Gita's Eighteen Chapters | Focus keyword once in a heading over the section that gives the path after endurance |

## Checklist

Now met:
- Focus keyword in the body text (Hindi and English); `tools/check_seo.py` failed on this before the fix.
- Focus keyword in the meta description (English); `check_seo.py` failed on this before the fix.
- Focus keyword in the URL slug (English); `check_seo.py` failed on this before the fix.
- Focus keyword within the first 100 words (Hindi and English).
- Focus keyword taken from wording the article uses (true of the `_seo` texts).
- Early direct answer (40–60 words) in both languages, and a verse-meaning question heading.

Still unmet: none. The report had no section 12 before this fix; it was added with every item met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | How do you overcome struggles in life? Through Gita 2.14, Acharya Ji shows that no hardship is permanent and endurance is the first step, not the last. | How to overcome struggles in life? Through Gita 2.14, Acharya Ji shows that no hardship is permanent and endurance is the first step, not the last. (147 chars) |
| wordpress.en.slug | overcome-struggles-in-life-gita | how-to-overcome-struggles-in-life-gita |
| wordpress.hi.slug | jeevan-ke-sangharsh-kaise-paar-karen | unchanged |
| focus keywords, secondary keywords, titles, Hindi meta, links, also_read | | unchanged |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | jeevan-ke-sangharsh-kaise-paar-karen | how-to-overcome-struggles-in-life-gita |
| focus_keyword | जीवन के संघर्षों को कैसे पार करें | how to overcome struggles in life |
| title | जीवन के संघर्षों को कैसे पार करें? गीता 2.14 का उत्तर | How to Overcome Struggles in Life: What the Gita Teaches |
| meta_description | जीवन के संघर्षों को कैसे पार करें? गीता 2.14 से आचार्य जी बताते हैं: कोई कठिन स्थिति स्थायी नहीं, सहनशीलता पहला कदम है, स्थिति बदलने के लिए कर्म करना होगा। | How to overcome struggles in life? Through Gita 2.14, Acharya Ji shows that no hardship is permanent and endurance is the first step, not the last. |
