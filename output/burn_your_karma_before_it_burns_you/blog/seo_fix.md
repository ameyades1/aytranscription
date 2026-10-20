burn_your_karma_before_it_burns_you: SEO fix

Fixed texts: `burn_your_karma_before_it_burns_you_blog_seo.txt` (Hindi) and `burn_your_karma_before_it_burns_you_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes (1)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro (before the first H2) | (none) | संचित कर्म कैसे जलाएं, इसका छोटा उत्तर यह है: उन्हें प्रारब्ध बनकर भोगे जाने का इंतज़ार करना ज़रूरी नहीं। आचार्य जी के अनुसार अपनी पत्रिका देखो, गुरु से पूछो, शिविर और साधना करो, और पुराने कर्मों को पकने से पहले ही जला दो। यह उपाय आज ही शुरू करना है। | Section 2's mismatch: the searched wording "संचित कर्म कैसे जलाएं" was missing from the body; it now appears once, in the first 100 words. Also the short direct answer (section 5, 50 words), built only from the first section's teaching (पत्रिका देखो, गुरु से पूछो, शिविर करो, पहले ही जला दो; उपाय आज ही करना है). Link phrases are not repeated, so the links stay in place. |

## English changes (1)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro (before the first H2) | (none) | The short answer on how to burn past karma: you need not wait for your accumulated karma to ripen and then suffer it. According to Acharya Ji, look at your birth chart, ask the Guru, take up sadhana, and burn that old karma before it ripens. The remedy has to begin today. | Section 2's mismatch: the searched wording "how to burn past karma" was missing from the body; it now appears once, in the first 100 words. Also the short direct answer (section 5, 52 words), built only from the first section ("Look at your birth chart, ask the Guru… burn it before it ever ripens"; "the remedy has to begin today"). |

Headings were not rephrased: the post already has question H2s ("क्या संचित कर्म भोगने ही पड़ेंगे?" / "Must You Suffer Through Your Accumulated Karma?", "क्या आप सच में सुनते हैं?" / "Do You Really Listen?"). The planets heading carries the inline image (`images.txt`), and the report advises against making "वाणी के चार स्तर" a heading until the Sanskrit review's flag 1 is fixed. The Sanskrit review's corrections (`tools/review/burn_your_karma_before_it_burns_you.md`) concern teaching and scripture wording and are not part of this SEO fix.

## Checklist

All section 12 items were already met in the report, and remain met with the fixed texts:
- Focus keyword (Hindi "संचित कर्म कैसे जलाएं", English "how to burn past karma") in the title, meta description, body, first 100 words and (English) slug.
- The searched wording is now in the body and is the focus keyword; the mismatch flagged in section 2 is resolved.
- A direct answer now sits early in both languages.
- Internal link phrases, the "Also read" heading and image placement unchanged and still found.

Still unmet: none.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | How to Burn Sanchit Karma: Obstacles on the Path | How to Burn Past Karma: Obstacles on the Spiritual Path |
| wordpress.hi.focus_keyword | संचित कर्म | संचित कर्म कैसे जलाएं |
| wordpress.hi.secondary_keywords | संचित कर्म कैसे जलाएं, संचित और प्रारब्ध कर्म, साधना में विघ्न और उपाय, वाणी के चार स्तर | संचित कर्म, संचित और प्रारब्ध कर्म, साधना में विघ्न और उपाय, वाणी के चार स्तर |
| wordpress.hi.meta_description | संचित कर्म को प्रारब्ध बनने से पहले कैसे जलाएं? आचार्य उपेंद्र जी साधना के विघ्न बताते हैं, दशा से अहंकार, संशय और आलस्य तक, और हर एक का उपाय। | संचित कर्म कैसे जलाएं, प्रारब्ध बनने से पहले? आचार्य उपेंद्र जी साधना के विघ्न बताते हैं, दशा से अहंकार, संशय और आलस्य तक, और हर एक का उपाय। |
| wordpress.en.slug | how-to-burn-sanchit-karma | how-to-burn-past-karma |
| wordpress.en.focus_keyword | sanchit karma | how to burn past karma |
| wordpress.en.secondary_keywords | how to burn past karma, sanchit karma vs prarabdha, obstacles on the spiritual path, four levels of speech para pashyanti | sanchit karma, sanchit karma vs prarabdha, obstacles on the spiritual path, four levels of speech para pashyanti |
| wordpress.en.meta_description | How do you burn sanchit karma before it ripens? Acharya Upendra Ji names the obstacles on the spiritual path, from dasha to doubt, and the remedy for each. | How to burn past karma before it ripens? Acharya Upendra Ji names the obstacles on the spiritual path, from dasha to doubt, and the remedy for each one. |

The Hindi title and slug (`sanchit-karma-kaise-jalayen`) are unchanged; the title already contains the new focus keyword. `links` and `also_read` are unchanged. The report's sections 2, 3, 8 and 11 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sanchit-karma-kaise-jalayen | how-to-burn-past-karma |
| focus_keyword | संचित कर्म कैसे जलाएं | how to burn past karma |
| title | संचित कर्म कैसे जलाएं? साधना के विघ्न और उनके उपाय | How to Burn Past Karma: Obstacles on the Spiritual Path |
| meta_description | संचित कर्म कैसे जलाएं, प्रारब्ध बनने से पहले? आचार्य उपेंद्र जी साधना के विघ्न बताते हैं, दशा से अहंकार, संशय और आलस्य तक, और हर एक का उपाय। | How to burn past karma before it ripens? Acharya Upendra Ji names the obstacles on the spiritual path, from dasha to doubt, and the remedy for each one. |
