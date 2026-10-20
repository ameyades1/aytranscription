dharma_teaches_us: SEO fix

The check passed before the fix, but neither focus keyword ("धर्म का असली सार" / "true essence of dharma") appeared in the body below the H1, so neither was in the first 100 words. The opening also gave no direct answer to the main question. Each language now has a short direct answer after the two opening paragraphs, built only from what the blog already says (one shared essence, the Supreme Reality or Atman; God's word universal; part of a saint's word bound to time and society; stories and rituals differ). It is report section 5's paragraph, cut to the blog's own terms and spelling (तत्व, as in the body). The first heading is now the question readers search for (report section 4). Focus keywords, titles, meta descriptions and slugs stay the same.

## Hindi (`dharma_teaches_us_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the two opening paragraphs, new paragraph | (none) | तो धर्म का असली सार क्या है? आचार्य जी के अनुसार यह वह मूल तत्व है जो हर धर्म में एक है: परम तत्व, आत्मा। परमात्मा की वाणी सार्वभौमिक है और हर देश-काल में लागू होती है, जबकि संत-वाणी का कुछ हिस्सा किसी विशेष समय और समाज के लिए होता है। कहानियां और कर्मकांड अलग हैं, तत्व एक है। | Focus keyword in the body, at word 69 (first 100 words). Direct answer (59 words) from report section 5, using only what the blog says. |
| First `##` heading | कौन-सा वचन किसका है? | संत-वाणी और परमात्मा-वाणी में अंतर कैसे पहचानें? | Question heading carrying the secondary keyword "संत वाणी और परमात्मा वाणी में अंतर" (report section 4); the section answers it. |

## English (`dharma_teaches_us_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the two opening paragraphs, new paragraph | (none) | So what is the true essence of dharma? According to Acharya Ji, it is the one foundation every religion shares: the Supreme Reality, the Atman. God's word is universal and holds in every land and age, while part of a saint's word serves a particular time and society. Stories and rituals differ; the essence is one. | Focus keyword in the body, at word 80 (first 100 words). Direct answer (56 words) from report section 5, using only what the blog says. |
| First `##` heading | Who Spoke These Words? | How Do You Tell the Word of a Saint from the Word of God? | Question heading matching "word of saints vs word of God" (secondary keyword, FAQ 1; report section 4); the section answers it. |

No teaching, example, verse, translation, reference, H1 or order of ideas changed, and the number and order of headings are the same. "हर धर्म के तीन हिस्से" / "The Three Parts of Every Religion" was not made a question (report section 4 offered it as optional), because `images.txt` places `inline.jpg` under it. "एक उदाहरण जो सब साफ़ कर देता है" / "One Example Makes It Clear" was not renamed to the ghunghat/burqa heading, so burqa stays out of headings (flag 4). All four `links` phrases and the `also_read` heading ("हम कहां अटक जाते हैं?" / "Where Do We Get Stuck?") are unchanged in each language, and the page build found them all.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages): before, it was only in the H1, which does not count.
  - Focus keyword within the first 100 words (both languages).
  - A direct answer (40–60 words) early on, and a question heading for the first section.
- Section 12 was missing from the report. It has been added, with every item met.
- Still unmet: none.
- Left alone on purpose: the Sanskrit review's corrections to the original text are for the editor to make in the original blog, because they change the teaching's wording or a verse reference rather than an SEO item. They are: the Ramapurvatapaniya reading and reference, "ऐसा शास्त्र कहता है" / "So the scriptures say", the koti gloss, the Hindi "मान लीजिए" for the burqa example, "अल्लाह या ईसा", the Paravani note, and तत्व → तत्त्व. If तत्त्व is applied, the Hindi link phrase "तत्व एक है, कहानियां अलग हैं, कर्मकांड अलग हैं" in seo.json must be updated too (flag 7).

## seo.json changes

None. The focus keywords, secondary keywords, titles and meta descriptions (all already contain the focus keyword), slugs (old and new are both `dharma-ka-asli-saar` / `true-essence-of-dharma`), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON. These report sections were updated: 2 (keyword note), 3 (the title, meta and slug in seo.json marked as recommended), 4 (a note on what was applied) and 12 (the checklist, newly added). Section 8 needed no change: its headline is the unchanged H1, and its description, keywords and suggested slugs match seo.json.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | dharma-ka-asli-saar | true-essence-of-dharma |
| focus_keyword | धर्म का असली सार | true essence of dharma |
| title | धर्म का असली सार: संत-वाणी और परमात्मा-वाणी का भेद | True Essence of Dharma: Word of Saints vs Word of God |
| meta_description | धर्म का असली सार क्या है? आचार्य उपेंद्र जी बताते हैं कि परमात्मा की वाणी सार्वभौमिक है, संत-वाणी देश-काल से बंधी, और हर धर्म के तीन भाग हैं पर तत्त्व एक है। | What is the true essence of dharma? Acharya Upendra Ji explains how God's universal word differs from a saint's word, and the three parts of each religion. |
