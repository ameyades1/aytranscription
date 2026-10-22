surrendering_to_guru: SEO fix

`check_seo.py` failed before the fix. Neither body contained its focus keyword ("सर्वधर्मान्परित्यज्य का अर्थ" / "sarva dharman parityajya meaning"): the bodies quote only the verse itself. The meta descriptions split the keyword with quotes ("'सर्वधर्मान्परित्यज्य' का अर्थ") or commas ("Gita 18.66, sarva dharman parityajya, really mean"), and the opening never gave a short answer to what the verse means. Each language gets two changes:
- a short direct answer, built only from what the blog already says, that brings in the focus keyword within the first 100 words;
- one heading rephrased as the question readers search for.

The focus keywords and slugs stay the same.

## Hindi (`surrendering_to_guru_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Introduction, new third paragraph (after "…शरणागति का पूरा रहस्य छिपा है।") | (none) | तो सर्वधर्मान्परित्यज्य का अर्थ क्या है? गीता १८.६६ में श्रीकृष्ण सब अधर्म नहीं, सब धर्म छोड़कर अपनी शरण में आने को कहते हैं। आचार्य जी समझाते हैं कि यहाँ धर्म का अर्थ मज़हब नहीं, हर भूमिका का कर्तव्य कर्म है, और शरण जीवित गुरु की है: अपनी धारणाएँ छोड़कर गुरु से पूछो कि तुम्हारे लिए क्या सही है। | The focus keyword was missing from the body (a SureRank error). This direct answer of 58 words is report section 5's, and it restates the blog's own sections. It credits the Guru reading to Acharya Ji (report flag 1), and it puts the keyword in the first 100 words. |
| H2 before the dharma-as-duty section | ## धर्म का अर्थ मज़हब नहीं, कर्तव्य है | ## सब धर्म छोड़ने का अर्थ क्या है? धर्म यानी कर्तव्य | This is the question form from report section 4 and the most common follow-up query. The section opens with this question and answers it. |

## English (`surrendering_to_guru_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Introduction, new third paragraph (after "…lies hidden inside it.") | (none) | The sarva dharman parityajya meaning is this: in Gita 18.66, Krishna asks Arjuna to set aside every dharma, not every wrong, and take refuge in Him alone. Acharya Ji explains that dharma here means the duty of each role, not religion, and the refuge is a living Guru: drop your assumptions and ask the Guru what is right for you. | The focus keyword was missing from the body (a SureRank error). This direct answer of 60 words is report section 5's, lightly shortened. It credits the Guru reading to Acharya Ji, and it puts the keyword in the first 100 words. |
| H2 before the dharma-as-duty section | ## Dharma Means Duty, Not Religion | ## What Does Abandoning Every Dharma Mean? Dharma as Duty | This is the question form from report section 4. The section opens with "What, then, does it mean to set aside every dharma?" and answers it. |

Nothing else changed:
- no teaching, example, H1 or order of ideas, and no heading count or order;
- no verses, verse translations or references;
- the H2 "अपनी धारणा छोड़ो, सही गाड़ी पकड़ो", which `images.txt` uses to place inline.jpg, is untouched.

A grep finds all five `links` phrases and the `also_read` heading in both texts, word for word. The new paragraphs contain none of the link phrases, so each link still lands on its original sentence.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages).
  - Focus keyword in the meta description (both languages).
  - Focus keyword within the first 100 words (both languages).
- Already met and still met: every other item. `check_seo.py` passes.
- Section 12 was missing from the report and has been added, marked against the fixed texts.
- Still unmet: none.
- Left alone on purpose:
  - Sanskrit review issues 1 to 6 (समाधिस्थ, "पूर्वार्ध" for Gita 2.47, ṃ for ṁ, "केवल" / "alone" in the मामेकं gloss, the parityajya analogy, "न मम") are not SEO items. Most of them touch verses, their translations or references, which this fix never changes. They are left for the editor.
  - The other H2s are not rephrased. "शरण किसकी: जीवित गुरु की" / "Whose Refuge? A Living Guru" is already a question and is the `also_read` anchor. The rest state the teaching itself.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | गीता 18.66 'सर्वधर्मान्परित्यज्य' का अर्थ क्या है? आचार्य जी समझाते हैं कि धर्म यानी कर्तव्य कर्म, शरण जीवित गुरु की, और चमत्कार को नहीं, ठीक से नमस्कार करो। | सर्वधर्मान्परित्यज्य का अर्थ क्या है? गीता 18.66 पर आचार्य जी समझाते हैं कि धर्म यानी कर्तव्य कर्म, शरण जीवित गुरु की, और चमत्कार को नहीं, ठीक से नमस्कार करो। (158) |
| wordpress.en.meta_description | What does Gita 18.66, sarva dharman parityajya, really mean? Acharya Ji explains dharma as duty, refuge in a living Guru, and why bowing beats miracles. | Sarva dharman parityajya meaning (Gita 18.66): Acharya Ji explains dharma as duty, refuge in a living Guru, and why bowing properly beats chasing miracles. (155) |
| wordpress.hi.slug | sarva-dharman-parityajya-ka-arth | sarva-dharman-parityajya-ka-arth (unchanged) |
| wordpress.en.slug | sarva-dharman-parityajya-meaning | sarva-dharman-parityajya-meaning (unchanged) |

Unchanged:
- in seo.json: the titles, focus keywords, secondary keywords, `links`, `also_read`, `alt`, `caption`, `related`, category and tags;
- in the report: section 11 holds the same JSON. Section 2 has a new keyword note. Section 3 marks the recommended meta descriptions and slugs and gives the new meta descriptions. Section 8 has the new descriptions and names the slugs. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sarva-dharman-parityajya-ka-arth | sarva-dharman-parityajya-meaning |
| focus keyword | सर्वधर्मान्परित्यज्य का अर्थ | sarva dharman parityajya meaning |
| title | सर्वधर्मान्परित्यज्य का अर्थ: गीता 18.66 और गुरु की शरण | Sarva Dharman Parityajya Meaning: Gita 18.66 and the Guru |
| meta description | सर्वधर्मान्परित्यज्य का अर्थ क्या है? गीता 18.66 पर आचार्य जी समझाते हैं कि धर्म यानी कर्तव्य कर्म, शरण जीवित गुरु की, और चमत्कार को नहीं, ठीक से नमस्कार करो। | Sarva dharman parityajya meaning (Gita 18.66): Acharya Ji explains dharma as duty, refuge in a living Guru, and why bowing properly beats chasing miracles. |
