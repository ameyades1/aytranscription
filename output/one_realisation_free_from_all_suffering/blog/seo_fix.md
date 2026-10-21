one_realisation_free_from_all_suffering: SEO fix

Fixed texts: `one_realisation_free_from_all_suffering_blog_seo.txt` (Hindi) and `one_realisation_free_from_all_suffering_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the introduction, before the first H2 | (none) | तो अस्थिर संसार में स्थिर क्या है? इस संसार में कुछ भी हमेशा नहीं रहता: शरीर, धन, दशा, संबंध और मन, सब बदलते हैं। इस अस्थिरता में स्थिर केवल परमात्मा है, जो प्रेम, क्षमा और शांति के रूप में मिलता है। चीज़ें भोगना गलत नहीं, पर उनका अस्थिर स्वभाव समझो, कर्तव्य करो और छोड़ दो। | The focus keyword "अस्थिर संसार में स्थिर क्या है" was not in the body (the H1 says "अस्थिर संसार में स्थिर की खोज"); now in the first 100 words. Also the missing direct answer (report section 5, about 50 words), built only from the blog: "स्थिर है परमात्मा", "प्रेम, क्षमा, शांति परमेश्वर", "कर्तव्य समझकर करो, और छोड़ दो", and the Key Takeaways. Repeats no link phrase; no pitar wording (flag 1) |
| H2 (vanaprastha section) | ## वानप्रस्थ: जंगल नहीं, जीने का ढंग | ## वानप्रस्थ आश्रम का अर्थ: जंगल नहीं, जीने का ढंग | Matches the High-priority query "वानप्रस्थ आश्रम का अर्थ" (report section 4); the section explains the four ashramas and what vanaprastha means |

## English changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the introduction, before the first H2 | (none) | So what stays steady when nothing lasts forever? Body, wealth, relationships and even the mind all change. Within this change, the one steady thing is God, found as love, forgiveness and peace. Enjoying things is not wrong, but understand that they do not last: do your duty, then let go. | The focus keyword "nothing lasts forever" was only in Key Takeaways; now in the first 100 words. Also the missing direct answer (about 52 words), built only from the blog's "What Stays Steady" section, the duty principle and the Key Takeaways. Leaves out "dasha" (flag 4) and pitar wording (flag 1) |
| H2 (vanaprastha section) | ## Vanaprastha: A Way of Living, Not a Trip to the Forest | ## Vanaprastha Meaning: A Way of Living, Not a Trip to the Forest | Matches the High-priority query "vanaprastha meaning" (report section 4) |

Number and order of headings are unchanged in both languages; the H1 was not touched (the blog quotes no verses). "A Truth That Matters Deeply" / "एक महत्त्वपूर्ण सत्य" was left as it is: the suggested question ("Why Turn Toward Vanaprastha After Fifty?") would nearly repeat the "Also read" heading two sections earlier. All `links` phrases and the `also_read` heading ("पचास के बाद धीरे-धीरे अलिप्त होना क्यों?" / "Why Begin Letting Go After Fifty?") are still in the texts, word for word, once each.

## Checklist

The report had no section 12; it was added (from `tools/prompts/seo_checklist.md`) and marked against the fixed texts.

Now met:
- Focus keyword in the body text, Hindi (missing before word for word).
- Focus keyword within the first 100 words, both languages.
- Focus keyword taken from wording the article uses (true of the `_seo` texts).
- A direct answer paragraph (40–60 words) placed early, both languages.
- One H2 per language phrased as the searched query ("vanaprastha meaning").

Still unmet: none.

Left for the editor (not SEO fixes): the Sanskrit review's content corrections (the pitar gloss and "pitars trouble the family", the unnamed "first verse" and "second verse", "उच्च की दशा" / "exalted planetary period", the dasha sense, the maya, virakti and vanaprastha glosses) are not applied in the body; they are flagged in report section 10.

## seo.json changes

None. Both texts now use the existing focus keywords, which were already in the titles, meta descriptions and the English slug, so the slugs stay the same: Hindi `asthir-sansar-mein-sthir-kya-hai` (old and new), English `nothing-lasts-forever` (old and new). Titles, meta descriptions, secondary keywords, `links`, `also_read`, `related`, alt text, captions, category and tags are unchanged.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | asthir-sansar-mein-sthir-kya-hai | nothing-lasts-forever |
| focus keyword | अस्थिर संसार में स्थिर क्या है | nothing lasts forever |
| title | अस्थिर संसार में स्थिर क्या है? दुःख से मुक्ति का एक बोध | Nothing Lasts Forever: One Realisation That Frees You |
| meta description | संसार को तुम छोड़ोगे या संसार तुम्हें छोड़ देगा। आचार्य उपेंद्र जी बताते हैं कि अस्थिर संसार में स्थिर क्या है, और पचास के बाद वानप्रस्थ का अर्थ क्या है। | Body, wealth and relationships all change. Acharya Upendra Ji explains what stays steady when nothing lasts forever, and why vanaprastha begins at home. |
