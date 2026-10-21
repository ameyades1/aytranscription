see_lord_everyone_but_treat_merit: SEO fix

Copies: `see_lord_everyone_but_treat_merit_blog_seo.txt` (Hindi) and `see_lord_everyone_but_treat_merit_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening (before the first H2) | (none) | संक्षेप में उत्तर है: नहीं। गीता ५.१८ ज्ञानी को समदर्शी कहती है, यानी वह सबमें एक ही परमात्मा देखता है। आचार्य जी के अनुसार यह देखने की बात है, व्यवहार की नहीं। कुत्ते में भी भगवान है और मंत्री में भी, फिर भी दोनों को एक ही थाली नहीं दी जाती। बर्ताव हर किसी की योग्यता से होता है। | Direct answer (59 words) to the opening question, built only from the blog's own content (गीता ५.१८, the dog-and-minister example, behaviour by merit). Attributes the merit principle to Acharya Ji (flag 5) and keeps "merit" away from the caste terms of the verse (flag 8). Uses no link phrase |
| H2 1 | ## गीता क्या कहती है: समदर्शन | ## गीता ५.१८ में समदर्शन का अर्थ क्या है? | Natural search question with the secondary keyword "समदर्शन का अर्थ" and the verse number (section 4); the section explains the verse |
| H2 2 | ## देखना और बर्ताव करना, दो अलग बातें | ## क्या सबमें भगवान देखने का अर्थ सबसे एक जैसा व्यवहार है? | The searched question with the focus keyword (section 4); the section answers it (see alike, behave by merit) |

## English (4 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening sentence | Does seeing God in everyone mean treating everyone the same way? | What does seeing God in everyone mean? Does it mean treating everyone the same way? | Puts the focus keyword "what does seeing God in everyone mean" word for word in the body and the first 100 words (SureRank error: it was not in the body) |
| New paragraph after the opening (before the first H2) | (none) | In short, no. Bhagavad Gita 5.18 calls the wise people of equal vision, who see the same Supreme Being in all. As Acharya Ji explains, this is about how you see, not how you behave. God dwells in a dog and in a minister, yet you would not serve both the same plate. Behaviour follows merit. | Direct answer (56 words) built only from the blog's own content; merit attributed to Acharya Ji (flag 5), kept away from the caste terms (flag 8). Uses no link phrase |
| H2 1 | ## What the Gita Teaches: Equal Vision | ## What Does Gita 5.18 Mean by Equal Vision? | Natural search question with the verse number (secondary keyword "Bhagavad Gita 5.18 meaning") |
| H2 2 | ## Seeing and Behaving Are Not the Same | ## Does Seeing God in Everyone Mean Treating Everyone Alike? | Natural search question (section 4; "should we treat everyone equally"); the section answers it |

Not changed: the H1s, all verses, their translations and references, the "Also read" heading "शत्रु से प्रेम, शत्रु पर विजय" / "Love the Enemy to Overcome the Enemy", the image section heading "पहले साम, फिर दाम, तब युद्ध" / "First Persuasion, Then an Offer, and Only Then War", and all four link phrases in each language (checked: each still present). The number and order of headings are unchanged. The Sanskrit review's corrections (Durga dialogue attribution, Shumbha vs Mahishasura, the order of the upayas, the five villages, "treat on merit" in the body, partial verses) are not SEO edits and are still open (report section 10).

## Checklist

Now met (section 12 added to the report, which had none):
- English focus keyword in the SEO title, meta description, body text, first 100 words and slug.
- Two H2s per language phrased as natural search questions.
- A 40–60 word direct answer at the start of the post, both languages.

Still unmet (1): no unsupported scriptural claims — the Durga dialogue reads as scripture, "treat on merit" is given as the Gita's own message, and the partial verses 4.8/4.11 are not marked (flags 1–6); fixing them changes the blog's wording beyond SEO, so they are left to the editor.

`python3 tools/check_seo.py see_lord_everyone_but_treat_merit` passes. Report sections 2, 3, 8, 11 and 12 updated. Pages rebuilt with `tools/rebuild_blogs.sh see_lord_everyone_but_treat_merit` (no notes).

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | See God in Everyone, Treat on Merit: Gita 5.18 Explained | What Does Seeing God in Everyone Mean? Equal Vision vs Merit |
| wordpress.en.meta_description | Does seeing God in everyone mean treating all alike? Acharya Upendra Ji explains Gita 5.18, why we must treat each on merit, and why Durga fought so long. | What does seeing God in everyone mean? Acharya Upendra Ji explains Gita 5.18, why we must still treat each person on merit, and why Durga fought so long. |
| wordpress.en.slug | see-god-in-everyone-treat-on-merit | what-does-seeing-god-in-everyone-mean |
| wordpress.hi.slug | sabmein-bhagwan-vyavhar-yogyata-se | sabmein-bhagwan-vyavhar-yogyata-se (unchanged) |
| focus_keyword, secondary_keywords (both); title.hi, wordpress.hi.meta_description | unchanged | unchanged |
| links, also_read | unchanged | unchanged |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sabmein-bhagwan-vyavhar-yogyata-se | what-does-seeing-god-in-everyone-mean |
| focus_keyword | सबमें भगवान देखने का अर्थ | what does seeing God in everyone mean |
| title | सबमें भगवान देखने का अर्थ: व्यवहार योग्यता से (गीता 5.18) | What Does Seeing God in Everyone Mean? Equal Vision vs Merit |
| meta_description | क्या सबमें भगवान देखने का अर्थ सबसे एक जैसा व्यवहार है? आचार्य उपेंद्र जी समझाते हैं गीता ५.१८ का समदर्शन, योग्यता से व्यवहार और दुर्गा देवी का लंबा युद्ध। | What does seeing God in everyone mean? Acharya Upendra Ji explains Gita 5.18, why we must still treat each person on merit, and why Durga fought so long. |
