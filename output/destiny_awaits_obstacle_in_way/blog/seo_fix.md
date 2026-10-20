destiny_awaits_obstacle_in_way: SEO fix

The check failed before the fix: neither focus keyword ("भाग्य में रुकावट" / "what is blocking your destiny") was in the body text, so it was not in the first 100 words either, and the opening had no direct answer to the main question. Each language now has a short direct answer after the introduction. It is built only from what the blog already says: the water as tattvajnana, the channel as destiny, the debris of maya as desire, "me, me"/ego and selfishness, and the sutra's point that efforts only remove the obstruction. Following the review's first issue, the water and channel are attributed to Acharya Ji, and only the sutra's principle to Patanjali. The "three kinds of mind" heading was rephrased as the question readers search for. Focus keywords, titles, meta descriptions and slugs stay the same.

## Hindi (`destiny_awaits_obstacle_in_way_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the introduction (second paragraph), new paragraph | (none) | तो भाग्य में रुकावट क्यों आती है? आचार्य जी समझाते हैं कि तत्त्वज्ञान का पानी और भाग्य की नहर पहले से हैं। रुकावट माया का कचरा है: कामना, "मैं, मैं" का भाव और स्वार्थ। पतंजलि योगसूत्र (४.३) के अनुसार साधन प्रकृति को चलाते नहीं, केवल रुकावट हटाते हैं। यह कचरा हटाइए, प्रवाह अपने आप होगा। | Focus keyword (missing from the body) placed within the first 100 words, along with the searched question "भाग्य में रुकावट क्यों आती है". Direct answer (55 words) from report section 5, using only what the blog says. |
| Third `##` heading | तीन बुद्धियां, कचरे के साथ तीन व्यवहार | सात्त्विक, राजसिक और तामसिक बुद्धि रुकावट के साथ क्या करती है? | Question heading carrying the secondary keyword "सात्त्विक राजसिक तामसिक बुद्धि" (report section 4); the section answers it. |

## English (`destiny_awaits_obstacle_in_way_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the introduction (second paragraph), new paragraph | (none) | So what is blocking your destiny? Acharya Ji explains that the water of knowledge and the channel of your destiny already exist. The block is the debris of maya: desire, ego and selfishness. As Patanjali's Yoga Sutras (4.3) teach, our efforts do not drive nature; they only remove the obstruction. Clear it, and the flow takes care of itself. | Focus keyword (missing from the body) within the first 100 words. Direct answer (59 words) from report section 5, using only what the blog says. |
| Third `##` heading | Three Kinds of Mind, Three Ways of Handling the Debris | How Do Sattvic, Rajasic and Tamasic Minds Handle Obstacles? | Question heading matching "sattvic rajasic tamasic mind" (secondary keyword, FAQ 4); the section answers it. |

No teaching, example, verse, translation, reference, H1 or order of ideas changed. The number and order of headings are also the same. The "खेत, नहर और एक पत्थर" / "A Field, a Channel and a Stone" heading was not renamed (report section 4 suggested renaming it), because `images.txt` places `inline.jpg` under it. All five `links` phrases in each language are unchanged and the page build found them. The `also_read` heading changed along with the third heading, and seo.json was updated to match.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages): `check_seo.py` failed on this before and now passes.
  - Focus keyword within the first 100 words (both languages).
  - Focus keyword taken from wording the article uses: the published `_seo` texts now contain it.
  - A direct answer (40–60 words) early on, and a question heading for the three gunas section.
- Section 12 was missing from the report. It has been added, with every item met.
- Still unmet: none.
- Left alone on purpose: the Sanskrit review's corrections to the original text are for the editor to make in the original blog, because they change the teaching's wording or the verse meaning rather than an SEO item. They are: the Patanjali attribution of the tap and channel, the plural प्रकृतीनां and the bhashya clause in the verse meaning, "पातंजल योगसूत्र", "trigunas", and the Duryodhana gloss.

## seo.json changes

| Field | Before | After |
|---|---|---|
| also_read.after.hi | तीन बुद्धियां, कचरे के साथ तीन व्यवहार | सात्त्विक, राजसिक और तामसिक बुद्धि रुकावट के साथ क्या करती है? |
| also_read.after.en | Three Kinds of Mind, Three Ways of Handling the Debris | How Do Sattvic, Rajasic and Tamasic Minds Handle Obstacles? |

The following are unchanged: focus keywords, secondary keywords, titles and meta descriptions (all already contain the focus keyword), slugs (old and new are both `bhagya-mein-rukawat` / `what-is-blocking-your-destiny`), `links`, `alt`, `caption`, `related`, category and tags. The report's section 11 holds the same JSON. These report sections were updated: 2 (keyword note), 3 (the recommended title, meta and slug marked as the ones in seo.json), 4 (a note on what was applied) and 12 (the checklist, newly added). Section 8 needed no change: its headline is the unchanged H1, and its description, keywords and suggested slugs match seo.json.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bhagya-mein-rukawat | what-is-blocking-your-destiny |
| focus_keyword | भाग्य में रुकावट | what is blocking your destiny |
| title | भाग्य में रुकावट क्यों? पतंजलि का किसान और नहर | What Is Blocking Your Destiny? Patanjali's Farmer Analogy |
| meta_description | भाग्य में रुकावट क्यों आती है? आचार्य उपेंद्र जी योगसूत्र ४.३ के किसान दृष्टांत से समझाते हैं: माया का कचरा हटाइए, भाग्य का प्रवाह अपने आप बहने लगता है। | What is blocking your destiny? Acharya Upendra Ji explains Yoga Sutra 4.3: like a farmer opening a channel, remove the debris of maya and the flow returns. |
