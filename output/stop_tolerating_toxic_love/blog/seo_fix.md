stop_tolerating_toxic_love: SEO fix

`check_seo.py` failed before the fix. Neither body contained its focus keyword ("तामसिक रिश्ता क्या है" / "why do people stay in toxic relationships"): the Hindi has only the heading "तामसिक रिश्ता क्या होता है?", and the English never uses "toxic". The English slug (`why-people-stay-in-toxic-relationships`) also lacked the keyword's "do". Neither opening gave a short answer. The changes:
- a short direct answer, built only from what the blog already says, that brings in the focus keyword within the first 100 words;
- one heading rephrased as the question readers search for (report section 4);
- the Sanskrit review's corrections (dhriti as a quality of the person; "No, Guruji" in English).

The focus keywords stay the same. The English slug changes.

## Hindi (`stop_tolerating_toxic_love_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new second paragraph (after "…पहली सीढ़ी क्या है।") | (none) | तो तामसिक रिश्ता क्या है? यह वह संबंध है जिसे व्यक्ति अज्ञान और भय के कारण बहुत लंबे समय तक पकड़े रहता है, भले ही उसमें रोज़ रोना, चिल्लाना और अत्याचार हो। लोग "लोग क्या कहेंगे" के डर, आत्म-मूल्य की कमी, अकेले रह जाने के डर या आदत के कारण उसमें रुके रहते हैं। | The focus keyword was missing from the body (a SureRank error). This direct answer (about 50 words) restates the blog's own sections (tamas, fear of society, low self-worth, fear of being alone, habit) and puts the keyword in the first 100 words. |
| "तामसिक रिश्ता क्या होता है?", first sentence | तामसिक रिश्ते की **धृति** (steadfastness, टिके रहने की शक्ति) का अर्थ है किसी संबंध को बहुत लंबे समय तक पकड़े रहना। | तामसी **धृति** (steadfastness, टिके रहने की शक्ति) में व्यक्ति किसी संबंध को बहुत लंबे समय तक पकड़े रहता है। | Content trust: in the Gita (18.35) dhriti is a quality of the person. The new wording is the Sanskrit review's own correction (issue 1, report flag 1). |
| Fourth H2 | ## आदत बन चुकी पीड़ा | ## हम पीड़ा क्यों सहते रहते हैं? | The question form suggested in report section 4. The section answers it (habit, no boundaries). |

## English (`stop_tolerating_toxic_love_blog_seo_en.txt`): 4 changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, new second paragraph (after "…the first step out of it.") | (none) | Why do people stay in toxic relationships? In Acharya Ji's teaching, such a bond is tamasic: the person clings to it out of ignorance and fear. Fear of what people will say, low self-worth, the fear of being left alone and sheer habit keep them holding on, even when every day brings tears, shouting and abuse. | The focus keyword was missing from the body (a SureRank error). This direct answer (about 55 words) is built from the blog's own sections and puts the keyword in the first 100 words. "Toxic" is used only as the reader's question and answered with the talk's own term, tamasic (report flag 3). |
| "What Is a Tamasic Relationship?", first sentence | The **dhriti** (steadfastness, the strength to stay put) of a tamasic relationship means clinging to a bond for a very long time. | Under tamasic **dhriti** (steadfastness, the strength to stay put), a person clings to a bond for a very long time. | Content trust: the Sanskrit review's correction (issue 1, report flag 1). |
| Fourth H2 | ## Pain That Has Become a Habit | ## Why Do We Keep Enduring the Pain? | The question form suggested in report section 4; the section answers the focus query most directly. |
| "But Where Does This Refusal Belong?", first paragraph | will you answer, "No, I won't do it"? | will you answer, "No, Guruji, I won't do it"? | Matches the Hindi ("नहीं गुरुजी, नहीं करेंगे"); the Sanskrit review's correction (issue 2, report flag 2). |

Nothing else changed:
- no teaching, example, H1 or order of ideas, and no heading count or order;
- the blog quotes no scripture verses;
- the H2 "स्वस्थ सीमा कैसी दिखती है?" / "What Does a Healthy Boundary Look Like?" (used by `images.txt`) and the `also_read` heading "सहना: गुण या अज्ञान?" / "Endurance: Virtue or Ignorance?" are untouched.

A grep finds all five `links` phrases and the `also_read` heading in both texts, word for word, and each focus keyword once in its body.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages).
  - Focus keyword in the URL slug (English).
  - Focus keyword within the first 100 words (both languages).
  - No unsupported scriptural claims: the dhriti sentence now follows the Sanskrit review.
- Already met and still met: every other item except the one below. `check_seo.py` passes.
- Section 12 was missing from the report and has been added, marked against the fixed texts.
- Still unmet (1):
  - Each tag can be shared by at least 3 posts. "टॉक्सिक रिश्ते" / "Toxic Relationships" is used by this post only so far. This fix does not change tags.
- Left alone on purpose:
  - The Hindi opening question is not reworded to "टॉक्सिक रिश्ता"; "टॉक्सिक रिश्ते में लोग क्यों रहते हैं" stays a secondary keyword, and the Hindi focus keyword is the talk's own term.
  - Report flag 4 (a safety note pointing to local help) is the editor's decision and is not added.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | why-people-stay-in-toxic-relationships | why-do-people-stay-in-toxic-relationships (41 characters) |
| wordpress.hi.slug | tamasik-rishta-kya-hai | tamasik-rishta-kya-hai (unchanged) |

Unchanged:
- in seo.json: the titles, focus keywords, secondary keywords, meta descriptions, `links`, `also_read`, `alt`, `caption`, `related`, category and tags;
- in the report: section 11 holds the same JSON. Section 2 has a new keyword note. Section 3 marks the recommended title, meta description and slug for each language and has the new English slug. Section 8's URL slug placeholder has the new slug. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | tamasik-rishta-kya-hai | why-do-people-stay-in-toxic-relationships |
| focus keyword | तामसिक रिश्ता क्या है | why do people stay in toxic relationships |
| title | तामसिक रिश्ता क्या है? अत्याचार सहना गुण नहीं | Why Do People Stay in Toxic Relationships? The Tamasic Trap |
| meta description | तामसिक रिश्ता क्या है? आचार्य उपेंद्र जी बताते हैं कि अत्याचार सहना सहिष्णुता नहीं, भय और आत्म-मूल्य की कमी है, और आत्मविश्वास से ना कहना क्यों ज़रूरी है। | Why do people stay in toxic relationships? Acharya Upendra Ji explains tamasic clinging, why enduring abuse is not a virtue, and how to say a confident no. |
