future_country_bharat_know: SEO fix

The report had no section 12 checklist; it was added in this fix. The one unmet item was "Within the first 100 words": neither body used the focus keyword ("भारत का भविष्य" / "future of Bharat") near the start, the English body never used "future of Bharat" at all (only "Bharat has a bright future"), and neither opening answered the H1's question early. Each language gets two changes: a short direct answer as the opening paragraph, built only from what the blog already says (its sections and Key Takeaways, matching the report's section 5), and the "आने वाला समय" / "The Times Ahead" H2 rephrased as the searched question, which that section answers. Focus keywords, titles, meta descriptions and slugs already fit and are unchanged.

## Hindi (`future_country_bharat_know_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| New opening paragraph (after the H1, before "## गुरु की दुविधा…") | (none) | गुरुदेव के अनुसार भारत का भविष्य उज्ज्वल तो है, पर वह बहुत सारी कठिनाइयों से होकर आएगा। नया प्रशासन और नया भारत एक ही आधार पर खड़ा होगा: आध्यात्मिक शक्ति का बढ़ना। देश बदलना केवल गुरु का काम नहीं है; इसमें हर भारतवासी की भूमिका है, और जो साधना करेंगे, वही ऊपर आएँगे। | Direct answer (about 55 words) to the H1's question, restating only the blog's own points (bright future through hardship, spiritual strength as the one foundation, everyone's role, those who do sadhana will rise). Puts the focus keyword "भारत का भविष्य" in the first 100 words. Worded so that no `links` phrase is repeated before its original place. |
| H2 before "गुरुदेव कुछ भविष्यवाणियाँ बताते हैं…" | ## आने वाला समय: उज्ज्वल, पर कठिनाइयों से होकर | ## भारत का भविष्य कैसा है? | Rephrased as the question readers search (report section 4); the section answers it ("भारत का भविष्य उज्ज्वल है, लेकिन…"). Number and order of headings unchanged. |

## English (`future_country_bharat_know_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| New opening paragraph (after the H1, before "## The Guru's Dilemma…") | (none) | According to Acharya Ji, the future of Bharat is bright, but it will come through many hardships. A new administration and a new Bharat can rest on one foundation alone: the growth of spiritual strength. Changing the country is not the Guru's job alone; every Indian has a part in it, and those who practise sadhana will rise. | Direct answer (58 words) from the blog's own points only. Puts the focus keyword "future of Bharat", which the body never used, in the first 100 words. No `links` phrase repeated. |
| H2 before "Acharya Ji shares a few predictions…" | ## The Times Ahead: Bright, but Through Hardship | ## What Is the Future of Bharat? | Rephrased as the searched question (also the meta description's opening question); the section answers it. Number and order of headings unchanged. |

No teaching, example, prediction, date, H1 or order of ideas changed, and Markdown is kept. All five `links` phrases and the `also_read` heading ("क्या भारत को बदलना केवल गुरु का काम है?" / "Is Changing Bharat the Guru's Job Alone?") appear once each in both texts, confirmed by grep. The inline image's section is found by its original Hindi heading in the original text, so WordPress still places it.

## Checklist

- Now met: "Within the first 100 words (preferred)", in both languages (direct-answer opening). The English body now also contains the exact focus keyword.
- Already met and still met: every other item in section 12 (added to the report in this fix). `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - The dating note "(This talk was given in January 2024.)" (report section 4, flag 1): the date comes from the video's details, not the blog text, so it would add a fact; left for the editor.
  - Renaming "नाड़ी शास्त्र" to "नाड़ी ज्योतिष" and the other Sanskrit review items (गुरुदेव vs Acharya Ji, "अंतर" vs "अंतर योग", "this is a mistake", "five days"): not SEO items; left for the editor to fix in the original blog.

## seo.json changes

None. Both focus keywords already appear in the titles, meta descriptions and (English) slug, and now in the first 100 words of the `_seo` bodies.

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | bharat-ka-bhavishya | bharat-ka-bhavishya (unchanged) |
| wordpress.en.slug | future-of-bharat | future-of-bharat (unchanged) |
| wordpress.hi.focus_keyword | भारत का भविष्य | भारत का भविष्य (unchanged) |
| wordpress.en.focus_keyword | future of Bharat | future of Bharat (unchanged) |

The report's section 11 is unchanged and matches seo.json; section 2 got a keyword note, section 3 marks the meta descriptions and slugs in seo.json as recommended, section 8 needed no change, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bharat-ka-bhavishya | future-of-bharat |
| focus_keyword | भारत का भविष्य | future of Bharat |
| title | भारत का भविष्य: आध्यात्मिक शक्ति से बदलेगा देश | The Future of Bharat: Why Spiritual Strength Must Grow |
| meta_description | भारत का भविष्य किसके हाथ में है? आचार्य उपेंद्र जी बताते हैं: भविष्य उज्ज्वल है, पर कठिनाइयों से होकर; देश बदलने में सबकी भूमिका है, आधार है आध्यात्मिक शक्ति। | What is the future of Bharat? Acharya Upendra Ji says it is bright but comes through hardship, and a new Bharat rests on growing spiritual strength. |
