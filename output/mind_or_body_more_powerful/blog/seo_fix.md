mind_or_body_more_powerful: SEO fix

The fixed texts are `mind_or_body_more_powerful_blog_seo.txt` (Hindi) and `mind_or_body_more_powerful_blog_seo_en.txt` (English). The original blog texts are unchanged. No teaching, example, verse, translation, reference or H1 was changed, and the Sanskrit review's corrections (tools/review/mind_or_body_more_powerful.md) were left for the editor, as they are not SEO fixes.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph, after the first question | क्या आपने कभी सोचा है कि हमारी परंपरा में **काली उपासना** को सबसे पहले क्यों रखा गया है? अंतर्योग फाउंडेशन ... | क्या आपने कभी सोचा है कि हमारी परंपरा में **काली उपासना** को सबसे पहले क्यों रखा गया है? मन या शरीर, कौन अधिक शक्तिशाली? अंतर्योग फाउंडेशन ... | Searched wording (the video's question) was missing from the body, and the focus keyword "मन या शरीर" was not in the body (SureRank error); now in the first 100 words |
| New paragraph after "पहले शरीर, फिर बुद्धि।" | (none) | संक्षेप में उत्तर है: पहले शरीर। "मैं कौन हूँ?" का पहला उत्तर शरीर ही होता है, इसलिए महाकाली, जो शरीरबोध और आत्मरक्षा की देवी हैं, की उपासना पहली है। उपनिषद कहते हैं कि पहले शरीर पुष्ट और बलवान हो, बुद्धि उसके बाद; और बल केवल शरीर का नहीं, हर प्रकार का होना चाहिए। | Direct answer early; built only from the blog's own points (मैं कौन हूँ, शरीरबोध, आत्मरक्षा, उपनिषद, हर प्रकार का बल), keeping "पहले" rather than "शरीर अधिक शक्तिशाली" (report section 10, flag 5) |
| `##` heading of the Vivekananda / Chandogya section | फुटबॉल, उपवास और वेदांत | क्या मन अन्न से बनता है? | Heading as the natural question readers search for (verse-meaning query, report section 4); the section's verse answers it |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph, after the first question | Have you ever wondered why our tradition places **Kali worship** first of all? In this discourse, ... | Have you ever wondered why our tradition places **Kali worship** first of all? Mind or body, which is more powerful? In this discourse, ... | Searched wording (the video's question) was missing from the body, and the focus keyword "mind or body" was not in the body (SureRank error); now in the first 100 words |
| New paragraph after "first the body, then the intellect." | (none) | In short: the body comes first. When we ask "Who am I?", the first answer is the body, which is why Mahakali, the goddess of body-awareness and self-defence, is worshipped first. The Upanishads say the body must grow strong before the intellect, and that strength should be of every kind, not merely physical. | Direct answer early (53 words); built only from the blog's own points, keeping "comes first" rather than "is more powerful" (report section 10, flag 5) |
| `##` heading of the Vivekananda / Chandogya section | Football, Fasting and Vedanta | Is the Mind Really Made of Food? | Heading as the natural question readers search for (report section 4); the section's verse answers it |

## Checklist

Now met:
- Focus keyword in the title tag, meta description and body text (both languages): all six were failing in `check_seo.py`, because SureRank does not match "mind or body which is more powerful" across the comma in "Mind or body, which is more powerful?". The focus keyword is now the core phrase, which all of them contain.
- Focus keyword within the first 100 words (both languages).
- Focus keyword taken from wording the article uses (the `_seo` texts now use it word for word).
- Searched wording flagged and kept as a secondary keyword (section 2's keyword note).
- Direct answer paragraph early, and one heading phrased as a reader's question, in each language.

Still unmet: none. The report had no section 12 yet; it was added with every item marked met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.focus_keyword | मन या शरीर कौन अधिक शक्तिशाली | मन या शरीर |
| wordpress.hi.secondary_keywords | कलम या तलवार कौन बड़ा; अन्नमयं हि सोम्य मनः का अर्थ; स्वस्थ शरीर में स्वस्थ मन | मन या शरीर कौन अधिक शक्तिशाली; कलम या तलवार कौन बड़ा; अन्नमयं हि सोम्य मनः का अर्थ; स्वस्थ शरीर में स्वस्थ मन |
| wordpress.en.focus_keyword | mind or body which is more powerful | mind or body |
| wordpress.en.secondary_keywords | is the pen mightier than the sword; annamayam hi somya manah meaning; Mahakali goddess of self-defence | mind or body which is more powerful; is the pen mightier than the sword; annamayam hi somya manah meaning; Mahakali goddess of self-defence |
| wordpress.hi.slug | man-ya-sharir-kaun-shaktishali | man-ya-sharir-kaun-shaktishali (unchanged) |
| wordpress.en.slug | mind-or-body-which-is-more-powerful | mind-or-body-which-is-more-powerful (unchanged; already contains the focus keyword, 35 characters) |

Titles, meta descriptions, `links` and `also_read` are unchanged: they already contain the new focus keywords, and no edit touched a link phrase or the "Also read" heading. The report's sections 2, 3, 8, 11 and 12 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | man-ya-sharir-kaun-shaktishali | mind-or-body-which-is-more-powerful |
| focus_keyword | मन या शरीर | mind or body |
| title | मन या शरीर, कौन अधिक शक्तिशाली? पहले शरीर क्यों | Mind or Body, Which Is More Powerful? Why Kali Comes First |
| meta_description | मन या शरीर, कौन अधिक शक्तिशाली? आचार्य उपेंद्र जी उपनिषद और महाकाली उपासना से बताते हैं कि पहले शरीर बलवान हो, फिर बुद्धि, और रचना की रक्षा क्यों ज़रूरी है। | Mind or body, which is more powerful? Acharya Upendra Ji explains why the Upanishads put a strong body before intellect, and why Kali worship comes first. |
