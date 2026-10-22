why_society_remains_divided_interview: SEO fix

Copies written: `why_society_remains_divided_interview_blog_seo.txt` (Hindi) and `why_society_remains_divided_interview_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new paragraph after the first | (none) | अगर आप जानना चाहते हैं कि जातिवाद कैसे खत्म हो, तो उत्तर हनुमान जी के जवाब में है। समाज इसलिए बंटा है क्योंकि यह समझ अभी सब में एक साथ नहीं आई। श्री राम के प्रश्न पर हनुमान जी ने तीन स्तरों पर उत्तर दिया: शरीर बोध में मैं आपका दास हूं, मन और बुद्धि में आपका अंश, और आत्मा में आप और मैं एक हैं। | The searched wording "जातिवाद कैसे खत्म हो" was missing from the body (section 2's mismatch note), and the opening did not answer the main question. The answer is built only from the blog's own sections ("क्योंकि यह भावना अभी सब में एक साथ नहीं आई है" and the three levels) |
| H2 1 | एक सीधा सा प्रश्न: हमारा संबंध क्या है? | हनुमान जी और श्री राम का संबंध क्या है? | A question readers search (secondary keyword); the section and the three levels that follow answer it |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new paragraph after the first | (none) | If you are asking how to end casteism, the answer is in Hanuman's reply. Society remains divided because this understanding has not yet awakened in everyone together. Asked by Shri Rama about their relationship, Hanuman answered on three levels: in the body I am your servant, in mind and intellect I am a part of you, and in the Atman you and I are one. | The searched wording "how to end casteism" was missing from the body (section 2's mismatch note), and the opening did not answer the main question. The answer is built only from the blog's own sections ("this understanding has not yet awakened in everyone together" and the three levels) |
| H2 1 | A Simple Question: What Binds Us Together? | What Is the Relationship Between Hanuman and Shri Rama? | A question readers search (secondary keyword "Hanuman and Rama relationship"); the section and the three levels that follow answer it |

The headings keep their number and order. No teaching, example, verse, verse translation or H1 was touched. All five `links` phrases and the `also_read` headings ("तो समाज बंटा क्यों है?" / "Why, Then, Does Society Remain Divided?") are still in the texts word for word; the new paragraphs avoid the link phrases ("आप और मैं एक हैं" / "you and I are one" are not the linked "बिल्कुल एक" / "entirely one"). The searched wording is used once per language; the closing heading that would have carried it a second time is the `also_read` anchor, so it was left unchanged.

## Checklist

Now met:
- Searched wording mismatch (section 2) resolved: both `_seo` texts use "जातिवाद कैसे खत्म हो" / "how to end casteism", which are now the focus keywords, within the first 100 words.
- Direct answer early: a 50–60 word answer now follows the opening question in each language.
- Question headings: H2 1 is now a natural search question in each language.

Still unmet: none. All section 12 items were already met and still are; `python3 tools/check_seo.py why_society_remains_divided_interview` passes.

Not changed:
- **Authenticity flags 1–4** (Hindi verse meaning, sandhi, the Dvaitadvaita gloss, the English Manusmriti gloss) are content corrections from the Sanskrit review that touch verses or translations, so they stay with the editor.
- **Flag 6**: the new focus keywords are questions ("how to end"), keeping the claim conditional as the talk does; no Manusmriti, reservation or caste-name keywords were added.
- Section 4's optional H3 above the verse was not added: it would sit inside the verse section and the verse is not body text SureRank counts.

## Report updates

- Section 2: the keyword table marks "जातिवाद कैसे खत्म हो" and "how to end casteism" as focus; the keyword notes describe the `_seo` texts.
- Section 3: the recommended titles, meta descriptions and slugs are the ones now in seo.json.
- Section 8: alternativeHeadline, description, keywords (both languages) and the suggested URL slugs match seo.json.
- Section 11: the same JSON as seo.json.
- Section 12: notes that the focus keyword comes from the `_seo` texts' wording.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | जातिवाद कैसे मिटे? हनुमान जी का तीन स्तरों वाला उत्तर | जातिवाद कैसे खत्म हो? हनुमान जी का तीन स्तरों वाला उत्तर (56 characters) |
| title.en | How Casteism Can End: Hanuman's Answer to Shri Rama | How to End Casteism: Hanuman's Answer to Shri Rama (50 characters) |
| wordpress.hi.slug | jativad-kaise-mite-hanuman-ji-ka-uttar | jativad-kaise-khatam-ho-hanuman-ji-ka-uttar |
| wordpress.hi.focus_keyword | जातिवाद | जातिवाद कैसे खत्म हो |
| wordpress.hi.secondary_keywords | जातिवाद कैसे खत्म हो, समाज बंटा क्यों है, देहबुद्ध्या तु दासोऽहं, हनुमान जी और श्री राम का संबंध | जातिवाद, समाज बंटा क्यों है, देहबुद्ध्या तु दासोऽहं, हनुमान जी और श्री राम का संबंध |
| wordpress.hi.meta_description | जातिवाद क्यों नहीं मिटता? श्री राम के प्रश्न पर … | जातिवाद कैसे खत्म हो? श्री राम के प्रश्न पर … (153 characters; the rest is unchanged) |
| wordpress.en.slug | hanuman-answer-to-end-casteism | how-to-end-casteism-hanuman-answer |
| wordpress.en.focus_keyword | casteism | how to end casteism |
| wordpress.en.secondary_keywords | how to end casteism, why society remains divided, dehabuddhya tu daso'ham meaning, Hanuman and Rama relationship | casteism, why society remains divided, dehabuddhya tu daso'ham meaning, Hanuman and Rama relationship |
| wordpress.en.meta_description | Why does casteism last? Hanuman's answer … | How to end casteism? Hanuman's answer … (150 characters; the rest is unchanged) |
| links, also_read | (unchanged) | (unchanged; no edit touched a phrase or heading) |

No other talk uses either focus keyword or either new slug.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | jativad-kaise-khatam-ho-hanuman-ji-ka-uttar | how-to-end-casteism-hanuman-answer |
| focus keyword | जातिवाद कैसे खत्म हो | how to end casteism |
| title | जातिवाद कैसे खत्म हो? हनुमान जी का तीन स्तरों वाला उत्तर | How to End Casteism: Hanuman's Answer to Shri Rama |
| meta description | जातिवाद कैसे खत्म हो? श्री राम के प्रश्न पर हनुमान जी का उत्तर: शरीर से दास, मन से अंश, आत्मा से एक। आचार्य जी बताते हैं कि यही समझ समाज को जोड़ सकती है। | How to end casteism? Hanuman's answer to Shri Rama, a servant in the body, a part in the mind, one in the Atman, shows how a divided society can heal. |
