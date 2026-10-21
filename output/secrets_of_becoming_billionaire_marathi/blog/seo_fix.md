secrets_of_becoming_billionaire_marathi: SEO fix

Copies: `secrets_of_becoming_billionaire_marathi_blog_seo.txt` (Hindi) and `secrets_of_becoming_billionaire_marathi_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening (before the first H2) | (none) | वक्ता के अनुसार, अरबपति बनने का रहस्य श्रीविद्या है: देवी ललिता त्रिपुरसुंदरी की उपासना की प्राचीन भारतीय परंपरा, जो धन को सँभालना और भोग व मोक्ष दोनों साथ पाना सिखाती है। जो वर्ग इसे जानता है, वह उसी परिश्रम से अत्यंत समृद्ध हो जाता है। चाणक्य भी कहते हैं कि धर्म का मूल अर्थ है। | Direct answer (55 words) built only from the sections "मेहनत बराबर, फल इतना अलग क्यों?", "धर्म की जड़ में अर्थ है" and "धन बुरा नहीं"; puts the focus keyword "अरबपति बनने का रहस्य" in the body and in the first 100 words (it was missing from the body; SureRank error). Keeps the blog's "वक्ता" attribution |
| H2 | ## श्रीयंत्र की गुप्त साधना | ## श्रीयंत्र पर कुंकुम अभिषेक क्या है? | Natural search question (section 4; secondary keyword "श्रीयंत्र कुंकुम अभिषेक"); the section answers it |
| H2 | ## धर्म की जड़ में अर्थ है | ## सुखस्य मूलं धर्मः का अर्थ क्या है? | Verse-meaning query from section 4 (secondary keyword "सुखस्य मूलं धर्मः का अर्थ"); the section gives the sutra and its meaning. The verse itself is untouched |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening (before the first H2) | (none) | According to Acharya Ji, the secret of becoming a billionaire is Shri Vidya, the ancient Indian spiritual tradition centred on the worship of Devi Lalita Tripurasundari. It teaches how to handle wealth and attain worldly enjoyment and liberation together. Those who know it prosper from the same labour, and as Chanakya teaches, wealth is the root of dharma. | Direct answer (58 words) built only from the blog's own sections; puts the focus keyword "secret of becoming a billionaire" in the body text and the first 100 words (it was only in the H1) |
| H2 | ## The Secret Practice of the Shri Yantra | ## What Is Kumkum Abhishek on the Shri Yantra? | Natural search question (section 4; secondary keyword "Shri Yantra kumkum abhishek"); the section answers it |
| H2 | ## Wealth Lies at the Root of Dharma | ## What Does Sukhasya Mulam Dharmah Mean? | Verse-meaning query (secondary keyword "sukhasya mulam dharmah meaning"); the section gives the sutra and its meaning. The verse itself is untouched |

Not changed: the H1s, the Chanakya sutra, its translation and reference, the "Also read" heading "धन बुरा नहीं: भोग और मोक्ष साथ-साथ" / "Wealth Is Not Evil: Enjoyment and Liberation Together", and all four link phrases in each language (checked with grep: each still present exactly once). The number and order of headings are unchanged. The Sanskrit review's corrections (lineage wording, sutra line form, "for the first time", आह्वान) are not SEO edits and are still open (report section 10).

## Checklist

Now met (section 12 added to the report, which had none):
- Focus keyword in the body text and within the first 100 words, both languages.
- Focus keyword in the meta description, both languages.
- One or two H2s phrased as natural search questions (two per language).
- A 40–60 word direct answer early in the post.
- Searched wording used in the body: "अरबपति बनने का रहस्य" / "secret of becoming a billionaire"; "सुखस्य मूलं धर्मः का अर्थ" / "sukhasya mulam dharmah" in an H2.

Still unmet (1): the Sanskrit review corrections (flags 1, 4, 5, 6) — they change wording of the teaching and verse formatting, which this SEO fix may not do; left to the editor.

`python3 tools/check_seo.py secrets_of_becoming_billionaire_marathi` passes. Report sections 2, 3, 8, 11 and 12 updated.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | मेहनत बराबर, फिर भी फल इतना अलग क्यों? आचार्य उपेंद्र जी बताते हैं कि श्रीविद्या, श्रीयंत्र साधना और चाणक्य का सूत्र धन के बारे में क्या सिखाते हैं। | अरबपति बनने का रहस्य क्या है? मेहनत बराबर, फल अलग क्यों? आचार्य उपेंद्र जी बताते हैं कि श्रीविद्या, श्रीयंत्र साधना और चाणक्य का सूत्र क्या सिखाते हैं। |
| wordpress.en.meta_description | Why do some grow rich from the same hard work others barely live on? Acharya Upendra Ji points to Shri Vidya, the Shri Yantra and Chanakya on wealth. | What is the secret of becoming a billionaire? Acharya Upendra Ji explains why equal hard work brings unequal wealth and points to Shri Vidya and Chanakya. |
| wordpress.hi.slug | arabpati-banne-ka-rahasya | arabpati-banne-ka-rahasya (unchanged) |
| wordpress.en.slug | secret-of-becoming-a-billionaire | secret-of-becoming-a-billionaire (unchanged) |
| focus_keyword, secondary_keywords, title (both) | unchanged | unchanged |
| links, also_read | unchanged | unchanged |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | arabpati-banne-ka-rahasya | secret-of-becoming-a-billionaire |
| focus_keyword | अरबपति बनने का रहस्य | secret of becoming a billionaire |
| title | अरबपति बनने का रहस्य: श्रीविद्या और श्रीयंत्र साधना | Secret of Becoming a Billionaire: India's Shri Vidya |
| meta_description | अरबपति बनने का रहस्य क्या है? मेहनत बराबर, फल अलग क्यों? आचार्य उपेंद्र जी बताते हैं कि श्रीविद्या, श्रीयंत्र साधना और चाणक्य का सूत्र क्या सिखाते हैं। | What is the secret of becoming a billionaire? Acharya Upendra Ji explains why equal hard work brings unequal wealth and points to Shri Vidya and Chanakya. |
