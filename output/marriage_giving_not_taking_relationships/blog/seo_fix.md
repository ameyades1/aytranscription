marriage_giving_not_taking_relationships: SEO fix

The report's focus keywords ("विवाह का उद्देश्य" / "spiritual purpose of marriage") were the searched wording but did not appear in either blog body or meta description, so `check_seo.py` failed (body and meta in both languages, and the English slug). The report also recommended putting the keyword in the first 100 words, a 40–60 word direct answer early, and one question heading. The fixes below add the searched wording once, inside a direct-answer paragraph built only from what the blog already says (its intro, "जो आपके पास है, वही दीजिए" / "Give What You Have", the duty section, the difficult-partner section and the Key Takeaways).

## Hindi (`marriage_giving_not_taking_relationships_blog_seo.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| "क्या विवाह सुखी होने का सौदा है?", after the first paragraph | (no paragraph) | संक्षेप में, विवाह का उद्देश्य लेना नहीं, देना है। पति और पत्नी दोनों अपनी क्षमता और प्रतिभा से वही देते हैं जो उन्हें आता है, बदले में कुछ पाने के लिए नहीं, बल्कि चित्त-शुद्धि के लिए। कठिन जीवनसाथी पूर्व प्रारब्ध है, और उसके साथ हमारा व्यवहार हमारा नया कर्म है। | Focus keyword "विवाह का उद्देश्य" in the body and in the first 100 words; direct answer for featured snippets. Every point is from the blog (the Key Takeaways say the same). |
| 3rd `##` heading | कर्तव्य कर्म: बदले में कुछ नहीं | विवाह में कर्तव्य कर्म का उद्देश्य क्या है? | A natural search question (report section 4) that the section answers: "उसका उद्देश्य है चित्त-शुद्धि, व्यापार नहीं". |

## English (`marriage_giving_not_taking_relationships_blog_seo_en.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| "Is Marriage a Deal for Happiness?", after the first paragraph | (no paragraph) | In short, the spiritual purpose of marriage is giving, not taking. Husband and wife each give what they know how to give, through their own abilities and talents, not to get something back but to purify the mind. A difficult partner is our prarabdha, and how we treat them is our new action. | Focus keyword "spiritual purpose of marriage" in the body and in the first 100 words; direct answer (53 words) for featured snippets. Every point is from the blog; "prarabdha" is used, not "destiny" (Sanskrit review, issue 2). |
| 3rd `##` heading | Dutiful Action Expects Nothing Back | What Is the Purpose of Duty in Marriage? | A natural search question (report section 4) that the section answers: "Its purpose is chitta-shuddhi (purification of the mind), not trade." |

No teaching, example, scripture, link phrase, "Also read" heading or the H1 was changed. The number and order of headings are the same. The Sanskrit review's corrections (the Chanakya attribution, "Destiny" in the English heading and takeaway) are content corrections, not SEO fixes, and are left to the editor; the "Also read" heading "A Difficult Partner: Destiny and New Action" is kept word for word so the box is still placed.

## Checklist

Now met (both languages):
- Focus keyword in the meta description (SureRank; failed before the fix).
- Focus keyword in the body text (SureRank; failed before the fix).
- Focus keyword in the URL slug, English (SureRank; failed before the fix: `marriage-giving-not-taking` → `spiritual-purpose-of-marriage`).
- Focus keyword within the first 100 words.
- Focus keyword taken from wording the article uses (the `_seo` texts now use it).
- Also (report section 4/5, not checklist items): a direct answer paragraph placed early, and one question heading per language.

Still unmet: none. (The report had no section 12 before; it has been added, marked against the `_seo` texts, with every item met.)

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या विवाह सुखी होने का सौदा है? आचार्य उपेंद्र जी बताते हैं कि विवाह लेने का नहीं, देने का संबंध है, और कठिन जीवनसाथी के साथ हमारा व्यवहार हमारा नया कर्म है। | विवाह का उद्देश्य क्या है? आचार्य उपेंद्र जी बताते हैं कि विवाह सुखी होने का सौदा नहीं, देने का संबंध है, और कठिन जीवनसाथी से हमारा व्यवहार हमारा नया कर्म है। |
| wordpress.en.meta_description | Is marriage a deal for happiness? Acharya Upendra Ji explains why marriage is about giving, not taking, and why a difficult partner is your prarabdha. | What is the spiritual purpose of marriage? Acharya Upendra Ji explains why it is about giving, not taking, and why a difficult partner is your prarabdha. |
| wordpress.en.slug | marriage-giving-not-taking | spiritual-purpose-of-marriage |
| wordpress.hi.slug | vivah-ka-uddeshya | vivah-ka-uddeshya (unchanged) |

Focus keywords, secondary keywords, titles, `links` and `also_read` are unchanged.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | vivah-ka-uddeshya | spiritual-purpose-of-marriage |
| focus_keyword | विवाह का उद्देश्य | spiritual purpose of marriage |
| title | विवाह का उद्देश्य: लेना नहीं, देना \| आचार्य उपेंद्र जी | Spiritual Purpose of Marriage: Giving, Not Taking |
| meta_description | विवाह का उद्देश्य क्या है? आचार्य उपेंद्र जी बताते हैं कि विवाह सुखी होने का सौदा नहीं, देने का संबंध है, और कठिन जीवनसाथी से हमारा व्यवहार हमारा नया कर्म है। | What is the spiritual purpose of marriage? Acharya Upendra Ji explains why it is about giving, not taking, and why a difficult partner is your prarabdha. |

The Hindi title contains a `|`, escaped in the table above; exactly as in seo.json: विवाह का उद्देश्य: लेना नहीं, देना | आचार्य उपेंद्र जी
