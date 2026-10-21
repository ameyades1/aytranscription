spiritual_meaning_secularism_independence_day_special: SEO fix

Fixed texts: `spiritual_meaning_secularism_independence_day_special_blog_seo.txt` (Hindi) and `spiritual_meaning_secularism_independence_day_special_blog_seo_en.txt` (English). The originals, H1s, verses and their translations and references, `links` phrases, the Also read heading, the inline image's heading ("अतिथि देवो भव, पर विवेक के साथ") and the images are unchanged. The number and order of `##` sections are unchanged.

Before this fix, the focus keywords ("धर्मनिरपेक्षता का आध्यात्मिक अर्थ", "spiritual meaning of secularism") appeared only in the H1 and not in the body, and neither opening gave a direct answer. Report section 2 found no mismatch between the searched wording and the body.

## Hindi changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| After the second paragraph, before "## सेक्युलर होने का अर्थ क्या है?" | (none) | धर्मनिरपेक्षता का आध्यात्मिक अर्थ वेद की एक पंक्ति, "एकं सद्विप्रा बहुधा वदन्ति", में छिपा है: सत्य एक है, विद्वान उसे अनेक प्रकार से कहते हैं। आचार्य जी कहते हैं कि असली प्रश्न देश के सेक्युलर होने का नहीं, बल्कि यह है कि मैं अपना धर्म कितनी अच्छी तरह जीता हूं। दूसरों से द्वेष नहीं, अपनी साधना की फलश्रुति दिखाओ। | Focus keyword was missing from the body, and there was no direct answer early. This snippet answer (report section 5) uses only the blog's own words: the section on the Veda line and the Key Takeaways. It also answers the opening's question ("या इसके पीछे कोई गहरा आध्यात्मिक अर्थ छिपा है?"). |
| H2 of the yama section | ## पहले यम की फलश्रुति दिखाओ | ## योग के पांच यम क्या हैं? पहले उनकी फलश्रुति दिखाओ | Report section 4: the heading now asks the question readers search ("योग के पांच यम", a secondary keyword). The section answers it with Yoga Sutra 2.30 and its list. The original instruction stays in the heading. |

## English changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| After the second paragraph, before "## What Does It Mean to Be Secular?" | (none) | The spiritual meaning of secularism lies in a single line of the Vedas, "ekaṃ sad viprā bahudhā vadanti": Truth is one; the wise describe it in many ways. Acharya Ji says the real question is not whether the country is secular, but how well I live my own faith. Show its fruit in your life, without hating anyone. | Focus keyword was missing from the body, and there was no direct answer early. This snippet answer (report section 5) uses only the blog's own words: the section on the Veda line and the Key Takeaways. It also answers the opening's question ("does a deeper spiritual meaning lie behind it?"). |
| H2 of the yama section | ## First, Show the Fruit of the Yamas | ## What Are the Five Yamas? First, Show Their Fruit | Report section 4: the heading now asks the question readers search ("five yamas of Patanjali", a secondary keyword). The section answers it with Yoga Sutras 2.30 and its list. The original instruction stays in the heading. |

## Checklist

Now met: the focus keyword appears in the body and within the first 100 words in both languages, there is an early direct answer in both languages (report section 5), and the yama section's heading is phrased as a question. The report had no section 12, so it was added with every item met. `tools/check_seo.py` passes against the `_seo` texts.

Still unmet: none.

Left for the editor (content, not SEO, so outside this fix): the Sanskrit review's items, which are authenticity flags 1, 2 and 4. These are the meaning of Rig Veda 1.164.46 ("the truth of God"), the phalashruti definition, the yama order, "अतिथिदेवो भव" vs "अतिथि देवो भव", and "यम के पांच नियमों". The fix does not repeat "the truth of God" / "परमेश्वर का सत्य" in the direct answer. If the Hindi heading "अतिथि देवो भव, पर विवेक के साथ" is later corrected, update `also_read.after.hi` and `images.txt`.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | spiritual-meaning-of-secularism | unchanged |
| wordpress.hi.slug | dharmanirpekshata-ka-adhyatmik-arth | unchanged |
| focus_keyword (hi / en) | धर्मनिरपेक्षता का आध्यात्मिक अर्थ / spiritual meaning of secularism | unchanged |
| title, meta descriptions, secondary_keywords, links, also_read | | unchanged |

No seo.json field needed changing. The focus keywords were already the searched wording and are now in the body. The titles and meta descriptions still contain them, and no edit touched a link phrase or the Also read heading.

Report updated:
- Section 2: wording check note added.
- Section 11: a stray duplicate copy of the JSON after the code block was removed. The block itself is unchanged and matches seo.json.
- Section 12: checklist added.
- Sections 3 and 8 already match seo.json and are unchanged.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | dharmanirpekshata-ka-adhyatmik-arth | spiritual-meaning-of-secularism |
| focus keyword | धर्मनिरपेक्षता का आध्यात्मिक अर्थ | spiritual meaning of secularism |
| title | धर्मनिरपेक्षता का आध्यात्मिक अर्थ: धर्म की फलश्रुति दिखाओ | Spiritual Meaning of Secularism: Show the Fruits of Faith |
| meta description | धर्मनिरपेक्षता का आध्यात्मिक अर्थ क्या है? आचार्य उपेंद्र जी: सत्य एक है, द्वेष नहीं दृढ़ता, विवेक के साथ अतिथि सत्कार, और पांच यमों की फलश्रुति। | What is the spiritual meaning of secularism? Acharya Upendra Ji on why Truth is one, welcoming guests with discernment, and living the five yamas. |
