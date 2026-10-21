love_burden_for_child_parenting: SEO fix

`check_seo.py` failed on the original texts: neither focus keyword ("बच्चों पर अपेक्षाओं का बोझ" / "parental pressure on children") was in the body text or the meta description. The originals talk about "दबाव", "अपेक्षाएं", "pressure" and "expectations", but never in the searched wording, and neither opening gave a direct answer. Each language now has a short direct answer in the opening section, built only from the blog's own sections and Key Takeaways, with the focus keyword inside the first 100 words. The comparison H2 now carries the secondary keyword. Both meta descriptions were rewritten to include the focus keyword. The focus keywords, titles and slugs stay as they were.

## Hindi (`love_burden_for_child_parenting_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| "क्या आप भी ऐसे ही पाल रहे हैं?", new third paragraph (after "…पिता भी इसमें शामिल हैं।") | (none) | संक्षेप में, राजसिक परवरिश बच्चों पर अपेक्षाओं का बोझ है, जो माता-पिता के "मैं" से चलता है: ऊंची अपेक्षाएं, लगातार तुलना, अनेक कक्षाएं, पैसे और नाम के लिए व्यवसाय का चुनाव, और माता-पिता के अधूरे सपने। आचार्य जी के अनुसार रजोगुण का अंत दुख है: बोझ में दबा बच्चा घर छोड़ता है, और जो चाहा था, वह अधिकतर नहीं मिलता। | Direct answer (about 55 words) built only from the blog's own sections and Key Takeaways (report section 5). Puts the focus keyword in the body, within the first 100 words, and uses the secondary keyword "माता-पिता के अधूरे सपने" naturally. "रजोगुण का अंत दुख" is attributed to Acharya Ji, not to the Gita (flag 2). |
| H2, fifth section | ## तुलना की अंतहीन दौड़ | ## बच्चों की दूसरों से तुलना: अंतहीन दौड़ | Adds the searched secondary keyword "बच्चों की दूसरों से तुलना" and keeps the talk's image of an endless race. The section describes exactly this. The number and order of headings are unchanged. |

## English (`love_burden_for_child_parenting_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| "Are You Raising Your Children This Way Too?", new third paragraph (after "…fathers are included too.") | (none) | In short, rajasic parenting is parental pressure on children that runs on the parent's own "I": very high expectations, constant comparison, endless classes, careers chosen for money and fame, and the burden of the parents' unfinished dreams. As Acharya Ji says, rajas ends in suffering: a child crushed by that burden leaves home, and the parents rarely get what they wanted. | Direct answer (about 58 words) built only from the blog's own sections and Key Takeaways (report section 5). Puts the focus keyword in the body, within the first 100 words. Attributed to Acharya Ji (flag 2). |
| H2, fifth section | ## The Endless Race of Comparison | ## Comparing Your Child to Others: An Endless Race | Adds the searched secondary keyword "comparing your child to others" and keeps the talk's image. The number and order of headings are unchanged. |

No teaching, example, H1, order of ideas or Markdown formatting was changed (the blog quotes no verse). Every `links` phrase in both languages and the `also_read` heading ("सिर पर सवार अपेक्षाएं" / "Expectations That Never Let Up") are still in the texts word for word, confirmed by grep. That is also why the "Expectations" H2, which the report's section 4 suggested rewording, was left alone. The new paragraphs avoid the link phrases, so the links still attach to their original places. The rebuild printed no "Note:" lines.

## Checklist

- Now met: the focus keyword is in the meta description and in the body text, and within the first 100 words, in both languages. The opening now gives a direct answer. `check_seo.py` passes.
- The report had no section 12; it has now been added, with every item marked met.
- Still unmet: none.
- Left alone on purpose:
  - Sanskrit review (minor): "सात्विक" → "सात्त्विक" and "महत्वाकांक्षा" → "महत्त्वाकांक्षा" is a spelling standardisation across all blogs, not an SEO issue, so it is left for the editor.
  - Report section 4's other optional ideas (a question H2 on expectations, an H3 "What Does a Sattvic Parent Do?") were not applied. The first would break the `also_read` heading, and the second would add a heading, which this fix must not do.
  - Report sections 1, 4, 5, 9 and 10 still describe the original texts. This fix may only edit sections 2, 3, 8, 11 and 12.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या आपका प्रेम बच्चे पर बोझ बन रहा है? आचार्य उपेंद्र जी बताते हैं राजसिक परवरिश के संकेत: ऊंची अपेक्षाएं, तुलना, अधूरे सपनों का बोझ और दिखावा। | क्या आपका प्रेम बच्चे पर बोझ बन रहा है? आचार्य उपेंद्र जी राजसिक परवरिश के संकेत बताते हैं: बच्चों पर अपेक्षाओं का बोझ, तुलना, अधूरे सपने और दिखावा। (148) |
| wordpress.en.meta_description | Is your love becoming a burden for your child? Acharya Upendra Ji explains rajasic parenting: high expectations, comparison and unfulfilled dreams. | Is your love a burden for your child? Acharya Upendra Ji explains rajasic parenting: parental pressure on children, comparison and unfulfilled dreams. (150) |
| wordpress.hi.focus_keyword | बच्चों पर अपेक्षाओं का बोझ | unchanged (now in the body) |
| wordpress.en.focus_keyword | parental pressure on children | unchanged (now in the body) |
| wordpress.hi.slug | bachchon-par-apekshaon-ka-bojh | unchanged |
| wordpress.en.slug | parental-pressure-on-children | unchanged (29 characters, unique) |

`title` (both already contain their focus keywords), `secondary_keywords`, `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON. Section 2 has a new keyword note, section 3 has the new metas marked as recommended, section 8 has the new descriptions, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bachchon-par-apekshaon-ka-bojh | parental-pressure-on-children |
| focus_keyword | बच्चों पर अपेक्षाओं का बोझ | parental pressure on children |
| title | बच्चों पर अपेक्षाओं का बोझ: राजसिक परवरिश के संकेत | Parental Pressure on Children: Signs of Rajasic Parenting |
| meta_description | क्या आपका प्रेम बच्चे पर बोझ बन रहा है? आचार्य उपेंद्र जी राजसिक परवरिश के संकेत बताते हैं: बच्चों पर अपेक्षाओं का बोझ, तुलना, अधूरे सपने और दिखावा। | Is your love a burden for your child? Acharya Upendra Ji explains rajasic parenting: parental pressure on children, comparison and unfulfilled dreams. |
