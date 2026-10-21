know_your_first_duty_in_life: SEO fix

`check_seo.py` failed on the original texts. Neither focus keyword was in the blog body: the Hindi only says "उसका प्रथम कर्तव्य क्या था" and the English only "what its first duty was", never the searched "जीवन का प्रथम कर्तव्य" / "first duty in life". Each language gets three changes. First, a short direct answer after the intro, built only from what the blog already says (report section 5), which puts the focus keyword in the first 100 words. Second and third, two headings are rephrased as the questions readers search for (report section 4). The report had no section 12 checklist, so this fix added it. seo.json is unchanged: the focus keywords, slugs, titles and meta descriptions already fit the fixed texts.

## Hindi (`know_your_first_duty_in_life_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…और फिर भूल गए।") | (none) | संक्षेप में, आचार्य जी के अनुसार जीवन का प्रथम कर्तव्य है अपने भीतर ज्ञान की अग्नि जलाना और ऐसे साक्षात्कारी गुरु को पाना, जो हमें नर से नारायण तक ले जाए। यही वचन जीव गर्भ में स्वयं से करता है: गुरु की खोज, पुराने कर्मों का प्रायश्चित, पुण्य और साकार कार्य, और ध्यान द्वारा मोक्ष। | The focus keyword "जीवन का प्रथम कर्तव्य" was nowhere in the body (SureRank error) and the opening gave no direct answer. This direct answer (55 words) puts the keyword in the first 100 words. It only restates the first section ("ज्ञान की अग्नि", "नर से नारायण तक ले जाए"), the womb section, the four steps and the takeaways ("साक्षात्कारी गुरु"), and repeats no `links` phrase. It adds no scripture or claim (no twelve-day, naamkaran or Upanishad mention). |
| `##` heading of the first section | ## सबसे पहला कर्म क्या है? | ## जीवन का प्रथम कर्तव्य क्या है? | Report section 4: the question readers search for, which the section answers ("ज्ञान की अग्नि प्रज्वलित करना ही सर्वप्रथम कर्म है", the realized Guru). Not a `links`, `also_read` or image heading. |
| `##` heading of the four-steps section | ## कर्ता बनने के चार कदम | ## प्रथम कर्तव्य के चार कदम कौन से हैं? | Report section 4: a question that suits a list snippet; the section lists the four steps of the resolve. Not a `links`, `also_read` or image heading. |

## English (`know_your_first_duty_in_life_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…and then forgot.") | (none) | In short, according to Acharya Ji, your first duty in life is to kindle the fire of knowledge within and find a realized Guru who can lead you from nara to Narayana. It is the promise each soul makes to itself in the womb: find the Guru, atone for past karma, do tangible good work, and reach moksha through meditation. | The focus keyword "first duty in life" was nowhere in the body (SureRank error) and the opening gave no direct answer. This direct answer (60 words) puts the keyword in the first 100 words. It only restates the first section, the womb section, the four steps and the takeaways, and repeats no `links` phrase. It adds no scripture or claim. |
| `##` heading of the first section | ## What Comes Before Everything Else? | ## What Is Your First Duty in Life? | Report section 4's suggested heading: the searched question, which the section answers. Not a `links`, `also_read` or image heading. |
| `##` heading of the four-steps section | ## Four Steps to Becoming a True Doer | ## What Are the Four Steps of Your First Duty? | Report section 4: a question that suits a list snippet; the section lists the four steps. Not a `links`, `also_read` or image heading. |

No teaching, example, H1, gloss or order of ideas changed, and the Markdown is kept. The number and order of `##` headings are the same. grep confirms that all five `links` phrases and the `also_read` heading ("गुरु कुछ थोपते नहीं, बस याद दिलाते हैं" / "The Guru Does Not Impose, Only Reminds") are still in both texts. The inline image's heading ("गर्भ में किया गया एक वादा" / "A Promise Made in the Womb", from images.txt) is unchanged.

## Checklist

- Now met (both languages): the focus keyword is in the body text and within the first 100 words; the opening has a direct answer; no searched-wording mismatch is left. `check_seo.py` passes.
- Added: section 12, the SEO checklist, which was missing from the report.
- Still unmet (1): "No unsupported scriptural claims". The blog attributes the womb account to the Katha Upanishad (review issue 1, Major; flag 1), and presents naamkaran "only after the twelfth day" and the twelve-day memory as scripture (review issues 2 and 3, Major; flags 2 and 3). Fixing them changes scriptural references and claims, which goes beyond an SEO edit. They are left for the editor to correct in the original blog with the review's wording. The new direct answers mention none of them, and they stay out of titles, keywords and snippets.
- Left alone on purpose:
  - Review issues 4 (Vaitarani) and 5 (साक्षात्कार किया हुआ गुरु / साक्षात्कारी गुरु, English glosses in the Hindi) are editorial and left for the editor. The direct answer uses "साक्षात्कारी गुरु", the form already in the Key Takeaways and the secondary keyword.
  - Report section 4's optional FAQ heading was not added: it would change the number of headings.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | jeevan-ka-pratham-kartavya | jeevan-ka-pratham-kartavya (unchanged; already built from the focus keyword) |
| wordpress.en.slug | first-duty-in-life | first-duty-in-life (unchanged; 18 characters, the focus keyword) |

No other field changed: the focus keywords (now in the fixed bodies), secondary keywords, `title` and meta descriptions (both already contain the focus keywords), `links`, `also_read`, `alt`, `caption`, `related`, category and tags. The report's section 11 holds the same JSON. Section 2 has a new keyword note, section 3 already marks the seo.json values as recommended, section 4 notes the applied edits, section 8 already matched and now also names the seo.json slugs for its URL placeholders, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | jeevan-ka-pratham-kartavya | first-duty-in-life |
| focus_keyword | जीवन का प्रथम कर्तव्य | first duty in life |
| title | जीवन का प्रथम कर्तव्य क्या है? गर्भ में किया गया वचन | Your First Duty in Life: The Promise Made in the Womb |
| meta_description | जीवन का प्रथम कर्तव्य क्या है? आचार्य उपेंद्र जी वह वचन याद दिलाते हैं जो हर जीव गर्भ में स्वयं से करता है: गुरु की खोज, प्रायश्चित, पुण्य कार्य और मोक्ष। | What is your first duty in life? Acharya Upendra Ji recalls the promise each soul makes in the womb: find a realized Guru, atone, do good, seek moksha. |
