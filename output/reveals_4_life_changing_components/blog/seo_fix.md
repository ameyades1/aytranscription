reveals_4_life_changing_components: SEO fix

`check_seo.py` failed this talk: neither focus keyword was in the body text (SureRank). People search "भाग्य कैसे बदलें" / "how to change your destiny", but the bodies only said "भाग्य अगर बदलना है" / "changing your destiny". The opening also named "four things" without saying what they are until the fourth section. Each language gets one change: a short direct answer at the end of the introduction, built only from the blog's own four principles and its line "भाग्य बदला जा सकता है" / "Destiny can be changed". It uses the searched wording once, within the first 100 words. The focus keywords stay the same.

## Hindi (`reveals_4_life_changing_components_blog_seo.txt`): 1 change

| Where | Before | After | Why |
|---|---|---|---|
| Intro ("सब कहते हैं, पर योजना किसके पास है?"), paragraph 3 split, new paragraph after "…ये चार सूत्र वही रहते हैं।" | …ये चार सूत्र वही रहते हैं। आइए, एक-एक कर के इन्हें समझें। | …ये चार सूत्र वही रहते हैं।<br><br>तो भाग्य कैसे बदलें? संक्षेप में, आचार्य जी के अनुसार चार चीज़ें चाहिए: स्पष्ट योजना और संकल्प; प्रारब्ध का साथ, जो पिछले कर्मों से बनता है; अपनी योजना और अपने भाग्य पर आत्मविश्वास; और सबसे ऊपर, गुरु कृपा। भाग्य बदला जा सकता है, पर योजना को प्रारब्ध का साथ मिल जाए, तो राह आसान हो जाती है। आइए, एक-एक कर के इन्हें समझें। | The focus keyword "भाग्य कैसे बदलें" was missing from the body (check_seo error), and there was no early direct answer. This answer is 57 words and restates the blog's own four principles, the prarabdha gloss and the line "भाग्य बदला जा सकता है… राह कितनी आसान हो जाती है". The keyword falls at about word 95. The closing sentence "आइए…" moved down unchanged. |

## English (`reveals_4_life_changing_components_blog_seo_en.txt`): 1 change

| Where | Before | After | Why |
|---|---|---|---|
| Intro ("Everyone Talks, but Who Has a Plan?"), paragraph 3 split, new paragraph after "…these four principles stay the same." | …these four principles stay the same. Let us look at them one by one. | …these four principles stay the same.<br><br>In short, this is how to change your destiny, according to Acharya Ji: a clear plan and resolve (sankalpa); the support of prarabdha, the destiny shaped by past actions; self-belief in both your plan and your destiny; and, above all, the Guru's grace. Destiny can be changed, but the road is far easier when prarabdha supports your plan. Let us look at them one by one. | The focus keyword "how to change your destiny" was missing from the body (check_seo error), and there was no early direct answer. This answer is 57 words and is built only from the blog's four principles, its prarabdha gloss and "Destiny can be changed". The keyword falls at about word 88. The closing sentence "Let us…" moved down unchanged. |

No teaching, example, verse, translation, reference, H1, heading or order of ideas changed, and the Markdown is kept. All five `links` phrases and the `also_read` heading ("जो दुःख अभी आया नहीं, उसे आज ही रोको" / "Stop Today the Suffering That Has Not Yet Come") are still in both texts, each confirmed by a script check. The number and order of `##` sections are unchanged.

## Checklist

- Now met: "In the body text" (focus keyword placement, both languages), the item `check_seo.py` failed on; and "Within the first 100 words".
- Section 12 was missing from the report. It has now been added from `tools/prompts/seo_checklist.md`, with every item marked against the `_seo` texts and seo.json. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - Headings were not rephrased. Three H2s are already natural questions ("सब कहते हैं, पर योजना किसके पास है?", "दूसरा सूत्र: क्या भाग्य साथ दे रहा है?", "आखिर प्रारब्ध देखें ही क्यों?" and their English versions). The heading the report suggested renaming ("जो दुःख अभी आया नहीं…") is the `also_read` anchor. The H3 summary the report suggested would add a heading.
  - Sanskrit review issues (section 10) are left for the editor to fix in the original blog. These are: the English Yoga Sutra 2.16 translation, which this fix may not touch; the danda, IAST and reference forms; the Nadi gloss; गुरुदेव / आचार्य जी; and "अंतर का संकल्प". The cleaned transcript reads "अंतर की पत्रिका", so issue 1 still needs the audio. None of these is an SEO item.
  - `images.txt` still names "The First Key: A Plan (Sankalpa)" for the English heading (report section 4). This fix may not write `images.txt`, and the image is placed through the Hindi heading.

## seo.json changes

None. Both focus keywords ("भाग्य कैसे बदलें" / "how to change your destiny") were already the searched wording and now appear in the `_seo` bodies. The titles and meta descriptions already contain them. The slugs (`bhagya-kaise-badle` / `how-to-change-your-destiny`, old and new) are unchanged and unique. `links`, `also_read`, `alt`, `caption`, `related`, category and tags are also unchanged. The report's section 11 block already matches seo.json. In the report, section 2 has a new keyword note and section 12 was added. Sections 3 and 8 already show these values.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bhagya-kaise-badle | how-to-change-your-destiny |
| focus_keyword | भाग्य कैसे बदलें | how to change your destiny |
| title | भाग्य कैसे बदलें? योजना, प्रारब्ध, आत्मविश्वास और गुरु कृपा | How to Change Your Destiny: 4 Principles from Acharya Ji |
| meta_description | भाग्य कैसे बदलें? आचार्य उपेंद्र जी चार सूत्र बताते हैं: योजना, प्रारब्ध, आत्मविश्वास और गुरु कृपा, और योगसूत्र २.१६ से आने वाले दुःख को आज ही रोकना। | How to change your destiny? Acharya Upendra Ji gives four principles: a clear plan, prarabdha, self-belief and the Guru's grace, with Yoga Sutra 2.16. |
