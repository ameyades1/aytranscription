punya_vs_paap: SEO fix

Fixed texts: `punya_vs_paap_blog_seo.txt` (Hindi) and `punya_vs_paap_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening (third paragraph) | (none) | पाप और पुण्य में अंतर कर्म में नहीं, उसके पीछे के भाव में है। हर कर्म की क्रिया रजस है, और रजोगुण अपने आप में तटस्थ है। रजस को तमोगुण का सहारा मिले तो वह पाप बन जाता है, और सत्व का सहारा मिले तो पुण्य। | Focus keyword "पाप और पुण्य में अंतर" was not in the body at all (SureRank error); adds it in the first 100 words as a short direct answer (about 45 words), built only from the blog's own sections "पाप और पुण्य की सीधी परिभाषा" and Key Takeaways |
| H2 of the shakti section | ## गुण छोड़ो, शक्ति नहीं | ## गुण और शक्ति में अंतर क्या है? | Question heading for the secondary query "गुण और शक्ति में अंतर"; the section answers it (each guna has its shakti; use all three shaktis, keep only sattva guna) |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the opening (third paragraph) | (none) | The difference between sin and virtue lies not in the act but in the intention behind it. The act in every deed is rajas, and rajas in itself is neutral. When rajas draws its support from tamas, it becomes sin; when the same rajas is backed by sattva, it becomes virtue. | Focus keyword "difference between sin and virtue" was not in the body (SureRank error); adds it in the first 100 words as a short direct answer (about 50 words), built only from "A Simple Definition of Sin and Virtue" and Key Takeaways |
| H2 of the shakti section | ## Let Go of the Guna, Keep the Shakti | ## What Is the Difference Between a Guna and a Shakti? | Question heading for "guna and shakti difference"; the section answers it, and the teaching itself ("let every other guna fall away, but never give up its power") stays in the body |

Number and order of headings unchanged; no verse, H1, link phrase or "Also read" heading touched.

## Checklist

Now met:
- Focus keyword in the body text (both languages)
- Focus keyword in the meta description (both languages)
- Focus keyword within the first 100 words (both languages)
- Direct-answer paragraph placed early (both languages)
- Question headings: one more H2 per language now phrased as a searched question

Still unmet (1):
- No unsupported scriptural claims: the body still attributes "sattva and tamas look alike from outside" to the scriptures ("शास्त्र कहते हैं" / "The scriptures say"), and the English says "the scriptures call it sin" and "The scriptures do not call Kali evil" (report section 10, flags 2 and 4). Re-attributing these is an editorial decision from the Sanskrit review, not an SEO fix, so it is left to the editor. The new paragraphs make no scriptural claim.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | एक ही कर्म कभी पाप तो कभी पुण्य क्यों? आचार्य उपेंद्र जी समझाते हैं: रजस तमोगुण से जुड़े तो पाप, सत्त्व से जुड़े तो पुण्य। ध्यान, दान और शिवाजी के उदाहरण। | पाप और पुण्य में अंतर क्या है? आचार्य उपेंद्र जी समझाते हैं: रजस तमोगुण से जुड़े तो पाप, सत्त्व से जुड़े तो पुण्य। ध्यान, दान और शिवाजी के उदाहरण। |
| wordpress.en.meta_description | What makes the same action a sin or a virtue? Acharya Upendra Ji explains how rajas joined with tamas becomes sin, and rajas guided by sattva, virtue. | What is the difference between sin and virtue? Acharya Upendra Ji explains how rajas joined with tamas becomes sin, and rajas guided by sattva, virtue. |
| wordpress.hi.slug | paap-aur-punya-mein-antar | paap-aur-punya-mein-antar (unchanged) |
| wordpress.en.slug | difference-between-sin-and-virtue | difference-between-sin-and-virtue (unchanged) |

Focus keywords, secondary keywords, titles, links and also_read are unchanged (the focus keywords already were the searched wording; the body now uses them). Report updated: section 2 (keyword note), 3 (recommended meta and slugs), 8 (schema descriptions), 11 (seo.json) and a new section 12 (checklist).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | paap-aur-punya-mein-antar | difference-between-sin-and-virtue |
| focus keyword | पाप और पुण्य में अंतर | difference between sin and virtue |
| title | पाप और पुण्य में अंतर क्या है? सत्त्व, रज और तम | Difference Between Sin and Virtue: The Three Gunas |
| meta description | पाप और पुण्य में अंतर क्या है? आचार्य उपेंद्र जी समझाते हैं: रजस तमोगुण से जुड़े तो पाप, सत्त्व से जुड़े तो पुण्य। ध्यान, दान और शिवाजी के उदाहरण। | What is the difference between sin and virtue? Acharya Upendra Ji explains how rajas joined with tamas becomes sin, and rajas guided by sattva, virtue. |
