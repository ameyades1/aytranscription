take_so_long_fulfil_desires: SEO fix

`check_seo.py` failed before the fix: the Hindi meta description split the focus keyword ("पाप का अनावश्यक डर"), and SureRank needs a Hindi keyword exactly as written. The Hindi body had "पाप का डर" only in the H1, neither language had its focus keyword in the first 100 words, and the opening asked the main question without answering it. Each language gets two changes:
- a short direct answer after the intro, built only from what the blog already says, that brings in the focus keyword within the first 100 words;
- one heading rephrased as the question readers search for.

The focus keywords and slugs stay the same. There is no searched-wording mismatch: readers search the body's own wording ("पाप का डर" / "fear of sin").

## Hindi (`take_so_long_fulfil_desires_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Introduction, new third paragraph (after "…पर गहराई से सोचने पर मुक्त करती है।") | (none) | गुरुजी के अनुसार बचपन से "बाप्पा देख रहा है" कहकर बैठाया गया पाप का डर मनुष्य को शुद्ध नहीं करता। वह मन में "तूने गलत किया" की कैसेट चलाता रहता है और हृदय ग्रंथि बनाता है, जो मुक्ति में बाधा है। उपाय है: भूल मानो, परिणाम आने से पहले सुधारो और उसे दोहराओ मत। | The focus keyword was in the H1 only and not in the first 100 words, and the opening gave no direct answer. This 54-word answer follows report section 5 and restates the blog's own sections ("बाप्पा देख रहा है", the cassette, हृदय ग्रंथि, the duty to correct). It says "गुरुजी", as the rest of the Hindi text does. |
| H2 of the last section | ## पूजा-पाठ: पहला कदम, अंतिम नहीं | ## क्या पूजा-पाठ ही अंत है? पहला कदम, अंतिम नहीं | Question form of report FAQ 5. The section answers it ("पूजा-पाठ अंत नहीं है, वह तो आरंभ है"). |

## English (`take_so_long_fulfil_desires_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Introduction, new third paragraph (after "…sets you free once you think it through.") | (none) | According to Acharya Ji, the fear of sin planted in childhood with words like "Bappa is watching you" keeps a tape of guilt playing in the mind and ties the hridaya granthi, the knot of the heart, which blocks liberation. The way out: admit the mistake, correct it before its consequences arrive, and do not repeat it. | The focus keyword was not in the first 100 words, and the opening gave no direct answer. This 57-word answer is report section 5's, slightly shortened, built only from the blog's own sections. |
| H2 of the last section | ## Ritual Worship: The First Step, Not the Last | ## Is Ritual Worship the Goal? The First Step, Not the Last | Question form of report FAQ 5. The section answers it ("ritual worship is not the end of the journey. It is only the beginning"). |

Nothing else changed:
- no teaching, example, H1 or order of ideas, and no heading count or order;
- the blog quotes no verses;
- the H2 "हृदय ग्रंथि: भीतर की गांठ" / "Hridaya Granthi: The Knot Within" was not rephrased (report section 4 suggested "हृदय ग्रंथि क्या है?"), because `images.txt` uses it to place inline.jpg.

A grep finds all five `links` phrases and the `also_read` heading in both texts, word for word, once each. The new paragraphs contain none of the link phrases, so each link still lands on its original sentence.

## Checklist

- Now met:
  - Focus keyword in the meta description (Hindi).
  - Focus keyword in the body text (Hindi; it was only in the H1 before).
  - Focus keyword within the first 100 words (both languages).
- Already met and still met: every other item. `check_seo.py` passes.
- Section 12 was missing from the report and has been added, marked against the fixed texts.
- Still unmet: none.
- Left alone on purpose:
  - Sanskrit review issues 1 to 6 ("शास्त्र की ओर से" / "Speaking on behalf of the scriptures", the optional hridaya granthi bridge, "गुरुजी" vs "आचार्य जी", "अंतर में", the unnamed Upanishad, the "पाप का अधिकार" / "Right to Err" heading pair) are editorial, not SEO, items. They change meaning or attribution, so they are left for the editor (report flags 1, 2, 3 and 6).
  - The other H2s are not rephrased: they state the teaching itself, and "या तो पूरा अर्थ सिखाओ, या डर मत सिखाओ" / "Teach the Full Meaning, or Do Not Teach Fear" is the `also_read` anchor.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या भीतर कोई आवाज़ कहती है 'तूने गलत किया'? आचार्य उपेंद्र जी बताते हैं कि पाप का अनावश्यक डर हृदय ग्रंथि कैसे बनाता है और पूजा-पाठ आरंभ क्यों है, अंत नहीं। | क्या भीतर कोई आवाज़ कहती है 'तूने गलत किया'? आचार्य जी बताते हैं कि बचपन से बैठाया पाप का डर हृदय ग्रंथि कैसे बनाता है और पूजा-पाठ आरंभ क्यों है, अंत नहीं। (155) |
| wordpress.hi.slug | paap-ka-dar-hriday-granthi | paap-ka-dar-hriday-granthi (unchanged) |
| wordpress.en.slug | fear-of-sin-knot-in-the-heart | fear-of-sin-knot-in-the-heart (unchanged) |

Unchanged:
- in seo.json: the titles, focus keywords, secondary keywords, English meta description, `links`, `also_read`, `alt`, `caption`, `related`, category and tags;
- in the report: section 11 holds the same JSON. Section 2 has a new keyword note. Section 3 marks the recommended meta descriptions and slugs and gives the new Hindi meta description. Section 8 has the new Hindi description and names the slugs. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | paap-ka-dar-hriday-granthi | fear-of-sin-knot-in-the-heart |
| focus keyword | पाप का डर | fear of sin |
| title | पाप का डर और हृदय ग्रंथि: पूजा-पाठ से आगे का रास्ता | Fear of Sin and the Knot in the Heart: Beyond Ritual |
| meta description | क्या भीतर कोई आवाज़ कहती है 'तूने गलत किया'? आचार्य जी बताते हैं कि बचपन से बैठाया पाप का डर हृदय ग्रंथि कैसे बनाता है और पूजा-पाठ आरंभ क्यों है, अंत नहीं। | Does a voice keep saying "you did wrong"? Acharya Upendra Ji explains how needless fear of sin ties the heart knot, and why ritual worship is only a start. |
