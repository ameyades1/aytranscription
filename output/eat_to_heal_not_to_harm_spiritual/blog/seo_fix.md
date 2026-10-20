eat_to_heal_not_to_harm_spiritual: SEO fix

Copies written: `eat_to_heal_not_to_harm_spiritual_blog_seo.txt` (Hindi) and `eat_to_heal_not_to_harm_spiritual_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening | (none) | आचार्य जी के अनुसार शाकाहार का आध्यात्मिक कारण एकत्व का अनुभव है। जो साधक मोक्ष चाहता है, वह सबमें स्वयं को और ईश्वर को देखता है, इसलिए किसी को मार या खा नहीं सकता। जो लौट आए और पीड़ा न दे, उसे छोड़ना हिंसा नहीं; पौधे का फल-फूल वाला भाग फिर उग आता है। | The focus keyword was not in the body or the first 100 words, and there was no early direct answer. Report section 5's answer, built only from the blog's own points (oneness, nails and hair, plants); 54 words. No Shakambhari claim added. |
| H2 4 | हिंसा की सच्ची परिभाषा | हिंसा किसे कहते हैं? | The question readers ask (report section 4); the section answers it. |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening | (none) | According to Acharya Ji, the spiritual reason for vegetarianism is the experience of oneness. A seeker of moksha sees God and their own self in every being, so they cannot kill or eat another. Giving up what grows back without pain is not violence, and plant food takes only the part of the plant that grows again. | The focus keyword was not in the body or the first 100 words, and there was no early direct answer. Report section 5's answer, built only from the blog's own points; 57 words. |
| H2 4 | What Violence Really Means | What Counts as Violence? | The question readers ask (report section 4); the section answers it. |

The headings keep their number and order. No teaching, example, verse, translation, reference or H1 was touched. The new paragraphs avoid the exact `links` phrases, so each link still lands on its original sentence; all five `links` phrases per language are still in the texts word for word. The `also_read` heading changed with H2 4 and was copied exactly into seo.json. The inline image heading ("शाकाहार क्यों?") is unchanged.

## Checklist

Now met:
- Focus keyword in the body text (both languages).
- Focus keyword within the first 100 words (both languages).
- Early direct answer (40–60 words) in both languages.
- A question-style H2 that matches "People also ask".

Still unmet (1):
- No unsupported scriptural claims: the body still presents the Shakambhari verse as a rule for human diet and gives it a meaning wider than the half-verse quoted (Sanskrit review issues 1–2). That fix changes a verse's meaning and a claim, which is outside an SEO fix; it is left to the editor.

`python3 tools/check_seo.py eat_to_heal_not_to_harm_spiritual` passes.

## Report updates

- Section 2: Hindi keyword row "हिंसा की सच्ची परिभाषा" → "हिंसा किसे कहते हैं"; added a keyword note (no searched-wording mismatch; the `_seo` texts now use both focus keywords).
- Section 3: recommended meta descriptions and slugs marked as the ones in seo.json (titles were already marked; nothing changed).
- Section 7: the Also read line names the new headings.
- Section 8: Hindi keywords list updated to match; headline, alternativeHeadline, description and slugs unchanged.
- Section 11: replaced with the new seo.json.
- Section 12: added the SEO checklist (it was missing), marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| also_read.after.hi | हिंसा की सच्ची परिभाषा | हिंसा किसे कहते हैं? |
| also_read.after.en | What Violence Really Means | What Counts as Violence? |
| wordpress.hi.secondary_keywords | शाकाहार क्यों करें, हिंसा की सच्ची परिभाषा, मोक्ष और शाकाहार, शाकंभरी देवी | शाकाहार क्यों करें, हिंसा किसे कहते हैं, मोक्ष और शाकाहार, शाकंभरी देवी |
| wordpress.hi.slug | shakahar-ka-adhyatmik-karan | unchanged |
| wordpress.en.slug | spiritual-reason-for-vegetarianism | unchanged |
| focus_keyword, title, meta_description | (both languages) | unchanged (they already contain the focus keyword, which the `_seo` texts now use) |
| links | (unchanged) | (unchanged; no edit touched a link phrase) |

No other talk uses either focus keyword or slug.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | shakahar-ka-adhyatmik-karan | spiritual-reason-for-vegetarianism |
| focus keyword | शाकाहार का आध्यात्मिक कारण | spiritual reason for vegetarianism |
| title | शाकाहार का आध्यात्मिक कारण: उपचार के लिए खाएँ | Spiritual Reason for Vegetarianism: Eat to Heal, Not Harm |
| meta description | शाकाहार का आध्यात्मिक कारण क्या है? आचार्य उपेंद्र जी बताते हैं कि मोक्ष का साधक किसी को क्यों नहीं मारता, हिंसा क्या है और शाकंभरी का संकेत। | Why go vegetarian? Acharya Upendra Ji gives the spiritual reason for vegetarianism: seeing God in all beings, what counts as violence, and what grows back. |
