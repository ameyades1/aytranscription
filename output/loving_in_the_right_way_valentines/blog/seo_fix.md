loving_in_the_right_way_valentines: SEO fix

The report's focus keywords "प्रेम कैसे जताएं" and "show love through actions" were in the titles and slugs but missing from the blog bodies and the meta descriptions (check_seo failed on both). Neither opening gave a direct answer. Each `_seo` text now gets a short direct answer after the opening paragraph, built only from what the blog already says, that uses the focus keyword word for word in the first 100 words; one heading per language becomes the natural question suggested in report section 4.

## Hindi changes (`loving_in_the_right_way_valentines_blog_seo.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening paragraph | (none) | तो प्रेम कैसे जताएं? आचार्य जी के अनुसार प्रेम केवल हृदय में रखने या शब्दों में कहने से पूरा नहीं होता; कहना वाणी का, सरस्वती का काम है। प्रेम हो जाने के बाद उसे कृति में दिखाना होता है: अपनी सामर्थ्य भर कुछ देना, कभी-कभी साथ जाना, और बीच-बीच में देते रहना, केवल अंतिम समय में नहीं। | Direct answer (≈57 words) early, only from the blog's own sections and takeaways; puts the focus keyword "प्रेम कैसे जताएं" in the body and in the first 100 words |
| First H2 | ## प्रेम से पहले सरस्वती, प्रेम के बाद? | ## प्रेम के बाद केवल ज्ञान क्यों काफ़ी नहीं? | Natural question readers search (report section 4), answered by the section |

## English changes (`loving_in_the_right_way_valentines_blog_seo_en.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening paragraph | (none) | How do you show love? Acharya Ji's answer: show love through actions, not only in the heart or in words. Saying it is the work of speech, of Saraswati. Once love has come, it has to show in what you do: giving within your means, sometimes going along with the person, and giving along the way, not only at the end. | Direct answer (≈61 words) early, only from the blog's own sections and takeaways; puts the focus keyword "show love through actions" in the body and in the first 100 words |
| First H2 | ## Saraswati Before Love, and After? | ## Why Is Knowledge Not Enough Once Love Has Come? | Natural question readers search (report section 4), answered by the section |

No teaching, example or link phrase was changed; the blog has no scripture verses; heading number and order are the same, and the H1s are untouched. All four `links` phrases and the `also_read` heading appear unchanged in both `_seo` texts. The Sanskrit review's two minor wording suggestions (Saraswati "leads you downhill"; "As Acharya Ji tells it" for Krishna's gifts) are editorial, not SEO, and were not applied here.

## Checklist

Now met:
- Focus keyword in the body text (Hindi and English)
- Focus keyword in the meta description (Hindi and English)
- Focus keyword within the first 100 words (Hindi and English)
- Direct answer placed early (both languages)
- Question headings (both languages)

Still unmet: none. The report had no section 12; it was added with every item marked met after the fix.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या "मैं तुमसे प्रेम करता हूँ" कहना काफ़ी है? आचार्य उपेंद्र जी बताते हैं कि प्रेम केवल शब्दों से नहीं, कृति से जताया जाता है, जीवनसाथी के साथ भी। | प्रेम कैसे जताएं? आचार्य उपेंद्र जी बताते हैं कि "मैं तुमसे प्रेम करता हूँ" कहना काफ़ी नहीं; प्रेम कृति से जताया जाता है, जीवनसाथी के साथ भी। |
| wordpress.en.meta_description | Is saying "I love you" enough? Acharya Upendra Ji explains why love must show in action, from Krishna's gifts to Radha to going along with your wife. | Is saying "I love you" enough? Acharya Upendra Ji explains why you must show love through actions, from Krishna's gifts to Radha to going with your wife. |

Slugs are unchanged (hi: `prem-kaise-jatayen` → `prem-kaise-jatayen`; en: `show-love-through-actions` → `show-love-through-actions`), as are the focus keywords, titles, secondary keywords, `links` and `also_read`.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | prem-kaise-jatayen | show-love-through-actions |
| focus_keyword | प्रेम कैसे जताएं | show love through actions |
| title | प्रेम कैसे जताएं: प्रेम जो कृति में दिखे \| आचार्य जी | Show Love Through Actions, Not Just Words \| Acharya Ji |
| meta_description | प्रेम कैसे जताएं? आचार्य उपेंद्र जी बताते हैं कि "मैं तुमसे प्रेम करता हूँ" कहना काफ़ी नहीं; प्रेम कृति से जताया जाता है, जीवनसाथी के साथ भी। | Is saying "I love you" enough? Acharya Upendra Ji explains why you must show love through actions, from Krishna's gifts to Radha to going with your wife. |

Titles exactly as in seo.json (the table escapes their `|`): hi `प्रेम कैसे जताएं: प्रेम जो कृति में दिखे | आचार्य जी`; en `Show Love Through Actions, Not Just Words | Acharya Ji`.
