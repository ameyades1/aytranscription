hidden_meaning_spiritual_symbols: SEO fix

The check failed in both languages: the focus keyword ("धर्म में प्रतीकों का महत्व" / "importance of symbols in religion") was nowhere in the body text. The post also had no early direct answer. Each language gets two changes. First, a short direct answer after the intro that opens with the focus keyword, built from the report's section 5 and only from what the blog already says. Second, one H2 rephrased as the question its section answers. The focus keywords, slugs, titles and meta descriptions already used the searched wording, so seo.json is unchanged. The report had no section 12; it has been added with every item marked.

## Hindi (`hidden_meaning_spiritual_symbols_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new paragraph after "…प्रतीक उसी गहरे सत्य तक पहुंचने का पुल है।" | (none) | धर्म में प्रतीकों का महत्व, आचार्य जी के अनुसार, संक्षेप में यही है: गूढ़ आध्यात्मिक सत्य सीधे न समझ में आता है, न याद रहता है, इसलिए उसे सामान्य उदाहरणों और प्रतीकों से समझाया जाता है, जैसे हर विद्या में याद रखने के लिए प्रतीक होते हैं। पर जब हम प्रतीक को पकड़ लेते हैं और उसका अर्थ भूल जाते हैं, तब अंधश्रद्धा शुरू होती है। प्रतीक का सही अर्थ गुरु की अनुभूति से खुलता है। | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 55 words follows the report's section 5 and repeats only the blog's own points (subtle truth taught through examples and symbols, symbols as memory aids in every discipline, blind faith from clinging to the symbol, the key in the Guru's experience). The keyword is now within the first 100 words. It is worded so that it does not repeat the link phrase "प्रतीक की कुंजी", which stays in its later paragraph. |
| H2 before "प्रतीक का काम है हमें याद दिलाना…" | ## जब प्रतीक ही सत्य बन जाए | ## अंधश्रद्धा कैसे शुरू होती है? | Rephrased as the searched question (a secondary keyword, report section 4). The section answers it. The number and order of headings are unchanged. |

## English (`hidden_meaning_spiritual_symbols_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new paragraph after "…A symbol is the bridge that carries you to that deeper truth." | (none) | The importance of symbols in religion, as Acharya Ji explains it, comes down to this: spiritual truth is too subtle to grasp or remember directly, so it is taught through everyday examples and symbols, just as every field of study uses symbols as memory aids. Blind faith begins when we cling to a symbol and lose its meaning. The Guru's direct experience unlocks what the symbol means. | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 60 words follows the report's section 5 and repeats only the blog's own points. The keyword is now within the first 100 words. It avoids repeating the link phrases "forget the meaning behind it" and "The key to their symbols". |
| H2 before "A symbol exists to remind us…" | ## When the Symbol Takes the Place of the Truth | ## How Does Blind Faith Begin? | Rephrased as the searched question (a secondary keyword, report section 4). The section answers it. The number and order of headings are unchanged. |

No teaching, example or order of ideas changed, and no H1 was touched. The blog has no verses. The Markdown format is kept. All five `links` phrases and the `also_read` heading ("हर विद्या का अपना संकेत-शास्त्र" / "Every Discipline Has Its Own Shorthand") are still in both texts once each, confirmed by grep. The inline image's heading is the same Also read heading and is unchanged. `rebuild_blogs.sh` printed no "Note:" lines.

## Checklist

- Now met: the focus keyword is in the body text in both languages (the two check_seo errors) and within the first 100 words. There is an early direct answer of about 40–60 words. Each language has two H2s phrased as natural questions.
- Already met and still met: every other item in the new section 12. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - Sanskrit review issues 1–4 ("superstition" vs "blind faith" in the English body, गूढ़ glossed as "subtle", "even harder to remember", "sacred signs") are wording and consistency fixes, not SEO items, so they are left for the editor to apply in the original blog. The new direct answers use "blind faith" and avoid the other three.
  - The report's section 4 also suggested renaming "प्रतीक भी, ज्ञान भी" / "Symbols and Knowledge Together" to "क्या प्रतीक छोड़ दें?" / "Should We Give Up Symbols?". Not done: the section's first line already asks that exact question, so the heading would repeat it.
  - The report's sections 1, 4, 5, 6 and 10 still describe the original texts. This fix may only edit sections 2, 3, 8, 11 and 12.

## seo.json changes

None. The focus keywords were already the searched wording and now appear in the body, so the focus keywords, secondary keywords, slugs, titles, meta descriptions, `links` and `also_read` all stay as they were.

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | dharm-mein-prateekon-ka-mahatva | dharm-mein-prateekon-ka-mahatva (unchanged) |
| wordpress.en.slug | importance-of-symbols-in-religion | importance-of-symbols-in-religion (unchanged) |

The report's section 11 still matches seo.json, and section 8 needed no change. Section 3 now marks the meta descriptions and slugs in seo.json as recommended (the titles were already marked). Section 2 has a keyword note, and section 12 is the new checklist.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | dharm-mein-prateekon-ka-mahatva | importance-of-symbols-in-religion |
| focus_keyword | धर्म में प्रतीकों का महत्व | importance of symbols in religion |
| title | धर्म में प्रतीकों का महत्व: प्रतीक, अंधश्रद्धा और गुरु | Importance of Symbols in Religion: Meaning vs Blind Faith |
| meta_description | शास्त्र प्रतीकों में क्यों बोलते हैं? आचार्य उपेंद्र जी बताते हैं धर्म में प्रतीकों का महत्व, अंधश्रद्धा कैसे जन्मती है और प्रतीक की कुंजी गुरु के पास क्यों है। | Why do scriptures speak in symbols? Acharya Upendra Ji explains the importance of symbols in religion, how blind faith begins, and why you need a Guru. |
