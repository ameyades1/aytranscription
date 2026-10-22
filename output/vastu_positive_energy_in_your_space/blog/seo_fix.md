vastu_positive_energy_in_your_space: SEO fix

Copies written: `vastu_positive_energy_in_your_space_blog_seo.txt` (Hindi) and `vastu_positive_energy_in_your_space_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| After the intro (new paragraph, 52 words) | (none; the intro ends "यह लेख उसी संवाद से निकला है।") | क्या वास्तु दोष के उपाय बिना तोड़-फोड़ हो सकते हैं? अंतरयोग के मार्ग में हाँ। आचार्य जी बताते हैं कि घर स्थान, संरचना और ऊर्जा से बनता है, और वास्तु सुधार दीवारें तोड़कर नहीं, महायज्ञ, पूजा और ऊर्जित यंत्रों से पूरे स्थान के स्पंदन ऊँचे करके होता है, बने-बनाए फ्लैट में भी। | The opening gave no direct answer; the searched wording "वास्तु दोष के उपाय" was missing from the body; no focus keyword in the first 100 words (now about word 77). Built only from the blog's own sections (three foundations, no demolition, mahayajna/puja/yantras, ready-built flat) |
| H2 1 | आपका घर तीन चीज़ों से बना है | आपका घर किन तीन चीज़ों से बनता है? | A natural question heading; the section answers it (स्थान, संरचना, ऊर्जा) |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| After the intro (new paragraph, 55 words) | (none; the intro ends "This article grew out of that conversation.") | Are there Vastu remedies without demolition? In Antar Yog's approach, yes. Acharya Ji explains that a home rests on location, structure and energy, and that instead of breaking walls, raising the vibration of the whole space through mahayajna, puja and energised yantras set into the floor or walls brings balance, even in a ready-built flat. | The opening gave no direct answer; the searched wording "Vastu remedies without demolition" was missing from the body; no focus keyword in the first 100 words (now about word 89). Built only from the blog's own sections |
| H2 1 | Three Things Make Up Your Home | What Three Things Make Up a Home? | A natural question heading; the section answers it (location, structure, energy) |

The headings keep their number and order; the other question headings ("क्या वास्तु सुधार के लिए दीवारें तोड़नी पड़ेंगी?" / "Do You Have to Break Down Walls to Fix Your Vastu?", the destiny and flat headings) were already questions and are unchanged. No teaching, example or H1 was touched (the blog has no verses). All five `links` phrases and the `also_read` headings ("व्यापार की सफलता: श्रीविद्या का सूत्र" / "Business Success: The Shri Vidya Formula") are still in the texts word for word, once each.

## Checklist

Now met:
- Focus keyword within the first 100 words: was unmet in both languages (about 140 / 160 words); now in the direct-answer paragraph.
- The searched wording mismatch (section 2) is resolved for "वास्तु दोष के उपाय" and "Vastu remedies without demolition", now the focus keywords.
- Direct answer early (section 4/5 suggestion): added, 52 / 55 words.

Still unmet (1):
- Each tag can be shared by at least 3 posts: "वास्तु / Vastu" is used only by this post; it is meant for future Vastu Rupantaran posts. The blog text cannot fix this.

`python3 tools/check_seo.py vastu_positive_energy_in_your_space` passes; `tools/rebuild_blogs.sh` gave no "Note:" lines.

Not changed:
- "Positive energy" (the video's wording) is still not in the body; adding it would put new wording into Acharya Ji's explanation, so it is not targeted.
- The optional H2 bridge before the Shri Vidya sections (section 4) would add a heading, so it was not made.
- The Sanskrit review's corrections (Shri Vidya definition, "Shri Vidya says honesty…", Agastya's date, the 33 percent takeaway, श्राप → शाप, kumkum gloss, "wife's name") are content corrections, not SEO fixes; they stay with the editor.

## Report updates

- Section 2: keyword table marks "वास्तु दोष के उपाय" and "Vastu remedies without demolition" as primary; the keyword note describes the `_seo` texts.
- Section 3: the new titles, meta descriptions and slugs are marked recommended; the old choices are kept and labelled.
- Section 8: alternativeHeadline, description and keywords in both languages, and the slugs for the post URLs.
- Section 11: the new seo.json. Section 12: first-100-words item now met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | वास्तु सुधार: बिना तोड़-फोड़ घर की ऊर्जा ऊँची करें | वास्तु दोष के उपाय: बिना तोड़-फोड़ घर की ऊर्जा ऊँची करें (56 characters) |
| title.en | How to Fix Your Vastu Without Breaking Down Walls | Vastu Remedies Without Demolition: Raise Your Home's Energy (59 characters) |
| wordpress.hi.slug | vastu-sudhar-bina-tod-phod | vastu-dosh-ke-upay-bina-tod-phod |
| wordpress.hi.focus_keyword | वास्तु सुधार | वास्तु दोष के उपाय |
| wordpress.hi.secondary_keywords | बिना तोड़-फोड़ वास्तु उपाय, फ्लैट के लिए वास्तु, वास्तु यंत्र, वास्तु दोष के उपाय | वास्तु सुधार, बिना तोड़-फोड़ वास्तु उपाय, फ्लैट के लिए वास्तु, वास्तु यंत्र |
| wordpress.hi.meta_description | क्या वास्तु सुधार के लिए दीवारें तोड़नी पड़ेंगी? आचार्य जी बताते हैं… | क्या वास्तु दोष के उपाय बिना तोड़-फोड़ हो सकते हैं? आचार्य जी बताते हैं… (146 characters; the rest is unchanged) |
| wordpress.en.slug | fix-your-vastu-without-demolition | vastu-remedies-without-demolition |
| wordpress.en.focus_keyword | fix your Vastu | Vastu remedies without demolition |
| wordpress.en.secondary_keywords | Vastu without demolition, Vastu for flats, Vastu yantras, Vastu Transformation | fix your Vastu, Vastu for flats, Vastu yantras, Vastu Transformation |
| wordpress.en.meta_description | Can you fix your Vastu without breaking walls? Acharya Ji explains… | Are there Vastu remedies without demolition? Acharya Ji explains… (151 characters; the rest is unchanged) |
| links, also_read | (unchanged) | (unchanged; no edit touched a phrase or heading) |

No other talk uses either focus keyword or either new slug.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | vastu-dosh-ke-upay-bina-tod-phod | vastu-remedies-without-demolition |
| focus keyword | वास्तु दोष के उपाय | Vastu remedies without demolition |
| title | वास्तु दोष के उपाय: बिना तोड़-फोड़ घर की ऊर्जा ऊँची करें | Vastu Remedies Without Demolition: Raise Your Home's Energy |
| meta description | क्या वास्तु दोष के उपाय बिना तोड़-फोड़ हो सकते हैं? आचार्य जी बताते हैं कि यंत्र, महायज्ञ और ऊँचे स्पंदन से बने-बनाए घर की ऊर्जा भी कैसे बदलती है। | Are there Vastu remedies without demolition? Acharya Ji explains how yantras, yajna and higher vibrations change a home's energy, even in a built flat. |
