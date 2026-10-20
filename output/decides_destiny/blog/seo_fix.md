decides_destiny: SEO fix

The check failed before the fix: the Hindi focus keyword "भाग्य कैसे बनता है" was not in the Hindi body, and neither focus keyword was in the first 100 words (the English "what decides your destiny" appeared only in the surgeon paragraph). Each language now has a short direct answer after the opening paragraph, built only from what the blog already says (Gita 18.13-14's five causes; Acharya Ji's explanation of daiva as the samskaras of past good and bad actions; the ego-in-charity example). It is attributed to Acharya Ji, not to the verse, in line with the review's major issue. Two headings were rephrased as the questions readers search for. Both focus keywords and slugs stay the same.

## Hindi (`decides_destiny_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the first paragraph, new paragraph | (none) | तो भाग्य कैसे बनता है? भगवद्गीता (१८.१३-१४) कर्म की सिद्धि के पाँच हेतु बताती है: अधिष्ठान, कर्ता, करण, विविध चेष्टाएँ और दैव। आचार्य जी समझाते हैं कि दैव, यानी भाग्य, पहले किए हुए शुभ-अशुभ कर्मों के संस्कारों का नाम है। इसलिए भाग्य कर्म से नहीं, उसके पीछे के संस्कार से बनता है, जैसे दान के साथ आए अहंकार से। | Focus keyword (absent from the body) in the first 100 words; direct answer (59 words) from report section 5, using only what the blog says. |
| Five causes `##` heading | गीता के पाँच हेतु: भाग्य के पाँच स्तंभ | गीता के अनुसार कर्म की सिद्धि के पाँच हेतु कौन-से हैं? | Question heading matching "कर्म की सिद्धि के पाँच हेतु" / "गीता के अनुसार भाग्य"; also fixes the "pillars of destiny" wording (review issue, report flag 2). |
| Daiva `##` heading | दैव: जो बाकी चारों को भी तय करता है | दैव का अर्थ क्या है? | Question heading matching the secondary keyword "दैव का अर्थ"; the section answers it. |

## English (`decides_destiny_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the first paragraph, new paragraph | (none) | So what decides your destiny? The Bhagavad Gita (18.13-14) names five causes behind every accomplished action: the foundation, the doer, the instruments, the efforts and daiva, or destiny. Acharya Ji explains daiva as the samskaras left by past good and bad actions. Your destiny comes not from the deed but from the samskara behind it, such as ego in charity. | Focus keyword in the first 100 words; direct answer (60 words) from report section 5, using only what the blog says. |
| Five causes `##` heading | The Gita's Five Causes: The Pillars of Destiny | What Are the Gita's Five Causes of Action? | Question heading matching "five causes of action Bhagavad Gita 18.14"; also fixes "pillars of destiny" (report flag 2). |
| Daiva `##` heading | Daiva: The Hidden Hand Behind the Other Four | What Does Daiva Mean? | Question heading matching "daiva meaning in the Gita"; the section answers it. |

No teaching, example, verse, translation, H1 or order of ideas changed; the number and order of headings are the same. All five `links` phrases in each language are unchanged and found by the page build; the `also_read` heading changed with the five-causes heading and seo.json was updated to match. The inline image's heading ("एक ही कर्म, दो अलग भाग्य" / "One Deed, Two Different Destinies") is untouched.

## Checklist

- Now met:
  - Focus keyword in the body text (Hindi): `check_seo.py` failed on this before; it now passes.
  - Focus keyword within the first 100 words (both languages).
  - Focus keyword taken from wording the article uses: the Hindi `_seo` text now contains it.
  - A direct answer (40-60 words) early on, and question headings for the five causes and daiva.
- Section 12 was missing from the report; it has been added, with every item met.
- Still unmet: none.
- Left alone on purpose: the Sanskrit review's other corrections ("भगवद्गीता के अनुसार यह धारणा पूरी तरह गलत है" / "the Gita define daiva", the samskara etymology wording in Hindi, the bridge line for the Gita Press glosses, the missing "हे महाबाहो!") change wording of the teaching or verse meanings, not SEO items; they are left for the editor to fix in the original blog.

## seo.json changes

| Field | Before | After |
|---|---|---|
| also_read.after.hi | गीता के पाँच हेतु: भाग्य के पाँच स्तंभ | गीता के अनुसार कर्म की सिद्धि के पाँच हेतु कौन-से हैं? |
| also_read.after.en | The Gita's Five Causes: The Pillars of Destiny | What Are the Gita's Five Causes of Action? |

Focus keywords, secondary keywords, titles, meta descriptions (all already contain the focus keyword), slugs (old and new `bhagya-kaise-banta-hai` / `what-decides-your-destiny`, unchanged), `links`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2 (keyword note), 3 (recommended title, meta and slug marked as in seo.json), 4 (note on what was applied) and 12 (checklist, newly added) were updated. Section 8 needed no change: its headline is the unchanged H1 and its description, keywords and suggested slugs match seo.json.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bhagya-kaise-banta-hai | what-decides-your-destiny |
| focus_keyword | भाग्य कैसे बनता है | what decides your destiny |
| title | भाग्य कैसे बनता है? गीता के पाँच हेतु और संस्कार | What Decides Your Destiny? Karma vs Samskaras |
| meta_description | भाग्य कैसे बनता है, कर्म से या संस्कार से? आचार्य उपेंद्र जी गीता (१८.१३-१४) के पाँच हेतु और दैव का अर्थ समझाते हैं, क्रिकेट, डॉक्टर और दान के उदाहरणों से। | What decides your destiny: past karma or the samskaras it leaves? Acharya Upendra Ji explains the Gita's five causes of action and the meaning of daiva. |
