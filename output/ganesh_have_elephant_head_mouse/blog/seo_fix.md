ganesh_have_elephant_head_mouse: SEO fix

Copies: `ganesh_have_elephant_head_mouse_blog_seo.txt` (Hindi) and `ganesh_have_elephant_head_mouse_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening, second paragraph | गणपति का रूप वास्तविक है या **प्रतीकात्मक** (symbolic)? यह रूप किसी कारण से दिया गया था | गणपति का रूप वास्तविक है या **प्रतीकात्मक** (symbolic)? गणेश जी का सिर हाथी का क्यों है? यह रूप किसी कारण से दिया गया था | The focus keyword (the searched wording) was not in the body at all; it is now in the first 100 words, as one more of the opening's own questions |
| New paragraph at the end of "क्या आपने कभी यह सवाल पूछा?" | (none) | आचार्य उपेंद्र जी के अनुसार गणेश जी का हाथी वाला सिर और चूहे की सवारी प्रतीक हैं। परम तत्त्व निराकार और अनंत है, और हमारा सीमित शरीर उसे माप नहीं सकता। इसलिए ऋषियों ने उसे हाथ, पैर, हाथी का सिर और वाहन वाला एक रूप दिया, जो हमारे भीतर के गुणों की ओर इशारा करता है। | Direct answer (56 words) placed early (report sections 4 and 5), built only from "सीमित पट्टी से अनंत नहीं मापा जा सकता", the next section and the key takeaways; does not repeat the link phrase "ये प्रतीक हैं" |
| H2 | ## इसलिए ऋषियों ने हमें एक रूप दिया | ## गणेश जी को हाथी का सिर क्यों दिया गया? | Natural search question (section 4); the section answers it ("उसे हाथ, पैर, हाथी का सिर दिया गया, ताकि परम तत्त्व का वर्णन हो सके") |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening, second paragraph | real, or is it symbolic? The sages gave this form for a reason | real, or is it symbolic? Why does Ganesha have an elephant head? The sages gave this form for a reason | The searched question was not in the body; it is now in the first 100 words and is the new focus keyword |
| New paragraph at the end of "Have You Ever Asked This Question?" | (none) | According to Acharya Upendra Ji, Ganesha's elephant head and his mouse mount are symbols. The Supreme Reality has no form and no end, and our finite body cannot measure it. So the sages gave it a form with hands, feet, an elephant's head and an animal mount, and every part of that form points to qualities within us. | Direct answer (58 words) placed early (report sections 4 and 5), built only from "A Finite Ruler Cannot Measure the Infinite", the next section and the key takeaways; does not repeat the link phrase "These forms are symbols" |
| H2 | ## That Is Why the Sages Gave Us a Form | ## Why Did the Sages Give Ganesha an Elephant's Head? | Natural search question (section 4); the section answers it ("they gave the deity hands, feet and an elephant's head, so that the form could describe the Supreme Reality") |

Not changed: the H1s, both verses with their translations and references, the Also read heading "अथर्वशीर्ष में हाथी कहाँ है?" / "Where Is the Elephant in the Atharvashirsha?", the inline image's heading "सीमित पट्टी से अनंत नहीं मापा जा सकता" / "A Finite Ruler Cannot Measure the Infinite", and all four link phrases in each language (checked with grep and by the rebuild: each still found once). The number and order of headings are unchanged. The Sanskrit review's corrections (the Hindi gloss missing रद, "in one sitting", "the Upanishads call") are not part of this fix and are still open (report section 10).

## Checklist

Now met:
- Focus keyword in the body text and in the first 100 words, both languages (it was missing from both bodies; `check_seo.py` failed before this fix).
- English focus keyword in the meta description and the slug (both failed before).
- Focus keyword taken from wording the article uses, and the searched-wording mismatch flagged (section 2) and fixed.
- A 40–60 word direct answer early in the post, both languages.
- One H2 per language phrased as the natural search question.

Still unmet: none. Report section 12 (added by this fix, since the report had none) marks every item met. `python3 tools/check_seo.py ganesh_have_elephant_head_mouse` passes.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Why Ganesha Has an Elephant Head and Rides a Mouse | Why Does Ganesha Have an Elephant Head and Ride a Mouse? (56 characters) |
| wordpress.en.focus_keyword | why Ganesha has an elephant head | why does Ganesha have an elephant head |
| wordpress.en.slug | why-ganesha-has-elephant-head | why-does-ganesha-have-an-elephant-head |
| wordpress.en.secondary_keywords | unchanged (the old keyword is a near-duplicate of the new one, so it is not added) | unchanged |
| wordpress.en.meta_description | unchanged (already contains "Why does Ganesha have an elephant head") | unchanged |
| wordpress.hi.slug | ganesh-ji-ka-sir-hathi-ka-kyon | ganesh-ji-ka-sir-hathi-ka-kyon (unchanged; built from the unchanged focus keyword) |
| wordpress.hi (all fields), title.hi | unchanged | unchanged |
| links, also_read, alt, caption, related | unchanged | unchanged |

Report updated to match: section 2 (keyword table and mismatch note), section 3 (English recommended title and slug), section 7 (cannibalization note's keyword), section 8 (English alternativeHeadline, keywords, suggested slug), section 11 (seo.json block) and section 12 (checklist added and marked).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ganesh-ji-ka-sir-hathi-ka-kyon | why-does-ganesha-have-an-elephant-head |
| focus_keyword | गणेश जी का सिर हाथी का क्यों है | why does Ganesha have an elephant head |
| title | गणेश जी का सिर हाथी का क्यों है, वाहन चूहा क्यों? | Why Does Ganesha Have an Elephant Head and Ride a Mouse? |
| meta_description | गणेश जी का सिर हाथी का क्यों है, वे चूहे पर कैसे बैठते हैं? आचार्य उपेंद्र जी बताते हैं कि यह रूप प्रतीक है, जो ऋषियों ने अनंत परम तत्त्व तक ले जाने को दिया। | Why does Ganesha have an elephant head and ride a mouse? Acharya Upendra Ji explains why the sages gave the formless Infinite a form full of symbols. |
