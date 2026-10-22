struggling_laziness_lack_drive_spiritual: SEO fix

`check_seo.py` passed before the fix only on the seo.json side; neither body used its focus keyword. The Hindi "आलस्य कैसे दूर करें" appeared only in the title and meta description (the body says "आलस्य कम नहीं हो रहा"), and the English "spiritual solution for laziness" (the video's own title wording) was not in the body. Once the check ran against the fixed texts, it also found that the English meta description did not contain the keyword word for word ("the spiritual solution"). The report had no section 12 checklist and no section 2 keyword note. The changes:
- a short direct answer under the first H2, built only from what the blog already says (report section 5), that brings in the focus keyword within the first 100 words (Hindi: about word 65, English: about word 80);
- the first H2 rephrased as the question readers search for (report section 4);
- in English only, the Sanskrit review's two wording corrections, which touch no verse or reference (review issues 1 and 2; report flags 1 and 2);
- the English meta description reworded so it holds the focus keyword.

The focus keywords, slugs and titles stay the same.

## Hindi (`struggling_laziness_lack_drive_spiritual_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| First H2 | ## जब आलस्य हटता ही नहीं | ## आलस्य क्यों नहीं जाता? | The question form suggested in report section 4, close to the searched "आलस्य क्यों आता है". The section answers it (laziness is a mark of tamoguna, and you cannot leap straight out of it). |
| First section, new paragraph after "…में आना ही पड़ता है।" | (none) | तो आलस्य कैसे दूर करें? पहले कर्तव्य-बोध से रजोगुण में आएं, चाहे यह बोध बाहर के नियम और अनुशासन से आए या भीतर की प्रेरणा से। फिर श्रेष्ठ को ही प्रिय बनाकर सत्त्व में जाएं। और प्रत्यक्ष गुरु का हस्तक्षेप सीधी छलांग भी करा सकता है। | The focus keyword was missing from the body text and the first 100 words. This direct answer (about 45 words) uses only the blog's own points (कर्तव्य-बोध lifts you into rajas, from outside discipline or inner drive; making the श्रेष्ठ your प्रिय leads to sattva; a present Guru's intervention makes the direct leap; see "मुख्य बातें"). Placed under the first H2, as report section 4 suggests. |

## English (`struggling_laziness_lack_drive_spiritual_blog_seo_en.txt`): 4 changes

| Where | Before | After | Why |
|---|---|---|---|
| First H2 | ## When Laziness Refuses to Budge | ## Why Won't Laziness Go Away? | The question form suggested in report section 4; the section answers it. |
| First section, new paragraph after "…(the quality of action and movement)." | (none) | So what is the spiritual solution for laziness? First, a sense of duty lifts you into rajas, whether it comes from outside rules and discipline or from an inner drive. Then, by learning to love what is best for you, you rise into sattva. And a Guru who steps into your life can make a direct leap possible. | The focus keyword was missing from the body. This direct answer (about 55 words) is report section 5's, built from the blog's own points; "a living Guru" became "a Guru who steps into your life", the blog's own wording. |
| "When Is a Direct Leap Possible?", Narada's gloss | (the wandering sage of Indian lore) | (the divine sage, or devarshi, of the Puranas) | Content trust: review issue 2, the review's own wording. |
| Same paragraph, last sentence | Valya was a highway robber; after meeting Narada, he became Maharshi Valmiki, the author of the Ramayana. | According to popular tradition, Valya was a highway robber who, after meeting Narada, became Maharshi Valmiki, the author of the Ramayana. | Content trust: review issue 1, the review's softened wording, so the popular story is not stated as scriptural fact. |

Nothing else changed:
- no teaching, example, H1 or order of ideas, and no heading count or order;
- the blog quotes no verses; no scripture reference was added;
- the H2 "तमस से निकलने के दो ही रास्ते" / "Only Two Ways Out of Tamas" (used by `images.txt` for inline.jpg) and the `also_read` heading "प्रेय या श्रेय: क्या चुनें?" / "Preya or Shreya: Which Will You Choose?" are untouched.

A grep finds all five `links` phrases and the `also_read` heading in both texts, word for word, once each, and each focus keyword once in its body. The new paragraphs do not repeat any link phrase ("तमस से सीधी छलांग" is not used; the English says "a direct leap"), so every link stays on its original sentence.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages).
  - Focus keyword within the first 100 words (both languages).
  - Focus keyword in the meta description (English; it was missing word for word).
  - No unsupported scriptural claims (English: review issues 1 and 2 applied).
- Section 12 was missing from the report and has been added, marked against the fixed texts. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - The H2 "तमस से निकलने के दो ही रास्ते" / "Only Two Ways Out of Tamas" is not rephrased as "तमोगुण से कैसे निकलें?" / "How Do You Get Out of Tamas?" (report section 4): `images.txt` places inline.jpg under this heading by its exact text, and the fix may not change the images.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | Struggling with laziness? Acharya Ji explains the spiritual solution: a sense of duty lifts you from tamas to rajas, and a Guru can make the direct leap. | Seeking a spiritual solution for laziness? Acharya Ji explains how a sense of duty lifts you from tamas to rajas, and how a Guru can make the direct leap. (154 chars) |
| wordpress.hi.slug | aalasya-kaise-door-karen | aalasya-kaise-door-karen (unchanged) |
| wordpress.en.slug | spiritual-solution-for-laziness | spiritual-solution-for-laziness (unchanged) |

Everything else (`focus_keyword`, `secondary_keywords`, `title`, the Hindi meta description, `links`, `also_read`, `alt`, `caption`, `related`, category and tags) is unchanged.

Report: section 11 holds the same JSON. Section 2 has a new keyword note. Section 3 marks the English meta description now in seo.json (154 chars); the titles, Hindi meta and slugs already matched. Section 8 has the new English description and names the URL slugs for the post-URL placeholders. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | aalasya-kaise-door-karen | spiritual-solution-for-laziness |
| focus keyword | आलस्य कैसे दूर करें | spiritual solution for laziness |
| title | आलस्य कैसे दूर करें? तमोगुण से निकलने का आध्यात्मिक उपाय | Spiritual Solution for Laziness: How to Break Out of Tamas |
| meta description | आलस्य कैसे दूर करें? आचार्य जी बताते हैं: आलस्य तमोगुण है। कर्तव्य-बोध तमस से रजस में लाता है, श्रेष्ठ को प्रिय बनाना सत्त्व में, और गुरु संस्कार बदलते हैं। | Seeking a spiritual solution for laziness? Acharya Ji explains how a sense of duty lifts you from tamas to rajas, and how a Guru can make the direct leap. |
