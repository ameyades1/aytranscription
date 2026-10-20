divine_power_every_woman_holds: SEO fix

Copies: `divine_power_every_woman_holds_blog_seo.txt` (Hindi) and `divine_power_every_woman_holds_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (1 change)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph under the H1, before the first H2 | (none) | स्त्री को शक्ति क्यों कहा जाता है? हमारी परंपरा में स्त्री शक्ति है, जैसे पार्वती, लक्ष्मी और सरस्वती शक्ति हैं। आचार्य उपेंद्र जी के अनुसार यह शक्ति शरीर के बल की नहीं, किसी गहरे स्तर की है। वह पुरुष के बराबर भर नहीं, कम से कम हज़ार गुना शक्तिशाली है, और माँ के रूप में उस पर बड़ा उत्तरदायित्व है। | The focus keyword "स्त्री को शक्ति क्यों कहा जाता है" was not in the body (check_seo error); this puts it in the body and the first 100 words, as a 60-word direct answer (report sections 4 and 5) built only from the sections "स्त्री को 'शक्ति' क्यों कहा गया?", "माँ की हज़ार गुना शक्ति" and the closing. It does not repeat any link phrase, and it names the goddesses as Shakti without a causal "इसीलिए" (review issue 4) |

## English (1 change)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph under the H1, before the first H2 | (none) | Why is woman called Shakti? In our tradition, woman is Shakti, as Parvati, Lakshmi and Saraswati are Shakti. According to Acharya Upendra Ji, this power is not physical strength; it lives at a deeper level. A woman is not merely equal to a man but at least a thousand times more powerful, and as a mother she carries great responsibility. | The focus keyword "why is woman called Shakti" was not in the body (check_seo error); this puts it in the body and the first 100 words, as a 60-word direct answer built only from the blog's own sections. It does not repeat the link phrase "they have always been at least a thousand times more powerful" |

Not changed: the H1s, every H2 (they are already natural questions, report section 4, and "विवाह न किया हो, तब भी?" / "What If She Has Never Married?" is the Also read anchor), and all five link phrases in each language (checked with grep: all still present). The number and order of headings are unchanged. The blog quotes no verses. The Sanskrit review's corrections (Gandhari wording, the Hindi "पापी" sentence, "इसीलिए / This is why" in the takeaways) are not SEO items and are still open (report section 10).

## Checklist

Now met:
- Focus keyword in the body text (both languages).
- Focus keyword in the meta description (English).
- Focus keyword in the URL slug (English): `why-is-woman-called-shakti`.
- Focus keyword within the first 100 words (both languages).
- A 40–60 word direct answer early in the post.

All other checklist items were already met. Unmet: none. `python3 tools/check_seo.py divine_power_every_woman_holds` passes.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | why-woman-is-called-shakti | why-is-woman-called-shakti |
| wordpress.en.meta_description | Why does our tradition call woman Shakti? Acharya Upendra Ji explains a strength beyond the body, and why a mother's power brings great responsibility. | Why is woman called Shakti in our tradition? Acharya Upendra Ji explains a strength beyond the body, and why a mother's power brings great responsibility. |

Unchanged: both focus keywords (the body now uses them), secondary keywords, titles, the Hindi slug and meta description, links, also_read, related, category and tags. The report's sections 2, 3, 4 (note), 8, 11 and 12 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | stri-ko-shakti-kyon-kaha-jata-hai | why-is-woman-called-shakti |
| focus_keyword | स्त्री को शक्ति क्यों कहा जाता है | why is woman called Shakti |
| title | स्त्री को शक्ति क्यों कहा जाता है? माँ की हज़ार गुना शक्ति | Why Is Woman Called Shakti? A Mother's Thousandfold Power |
| meta_description | स्त्री को शक्ति क्यों कहा जाता है? आचार्य उपेंद्र जी बताते हैं कि यह शक्ति शरीर के बल से परे है, और माँ की हज़ार गुना शक्ति के साथ बड़ा उत्तरदायित्व भी आता है। | Why is woman called Shakti in our tradition? Acharya Upendra Ji explains a strength beyond the body, and why a mother's power brings great responsibility. |
