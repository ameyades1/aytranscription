diet_hindering_success_link_prosperity: SEO fix

The check failed before the fix: neither focus keyword ("ईमानदार कमाई और सात्विक भोजन" / "honest earnings and sattvic food") appeared in the body, and the English slug (`honest-earnings-sattvic-food`) lacked "and", so it did not match the keyword. The opening also gave no direct answer to the main question ("is sattvic food enough?"). Each language now has a short direct answer after the two opening paragraphs, built only from what the blog already says (the Key Takeaways, the "unjust money" section and the protection by devotion, sattva guna and purity of money), carrying the focus keyword within the first 100 words. Two headings are now the questions readers search for (report section 4 and FAQ 5). The English slug now contains the whole keyword. Focus keywords, titles and meta descriptions stay the same.

## Hindi (`diet_hindering_success_link_prosperity_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the two opening paragraphs, new paragraph | (none) | तो क्या केवल सात्विक भोजन काफ़ी है? आचार्य जी के अनुसार नहीं। ईमानदार कमाई और सात्विक भोजन मिलकर फल देते हैं। अन्याय और लूट के धन से बना सात्विक भोजन भी वही फल नहीं देता, जबकि मेहनत और सत्संग से आए धन की पवित्रता, भक्ति और सत्त्वगुण व्यक्ति की कुछ तो रक्षा करते हैं। | Focus keyword in the body, at word 73 (first 100 words). Direct answer (about 50 words) from report section 5, using only what the blog says, keeping "कुछ तो" (to some degree) as in the talk. |
| Fourth `##` heading | जब सात्विक व्यक्ति के साथ गलत होता है | जब सात्विक व्यक्ति के साथ गलत हो, तो क्या भक्ति रक्षा करती है? | Question heading (report section 4: "क्या भक्ति रक्षा करती है?"); the section answers it. |
| Fifth `##` heading | मीराबाई का उदाहरण | मीराबाई ने विष कैसे पचा लिया? | Question heading matching "मीराबाई और विष का प्याला" (secondary keyword) and FAQ 5; the section answers it. |

## English (`diet_hindering_success_link_prosperity_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the two opening paragraphs, new paragraph | (none) | So is sattvic food enough? According to Acharya Ji, it is not. Honest earnings and sattvic food work together. Sattvic food bought with unjust or stolen money does not bear the same fruit, while the purity of money earned through hard work and satsang, along with devotion and sattva guna, protects a person to some degree. | Focus keyword in the body, at word 75 (first 100 words). Direct answer (57 words) from report section 5, using only what the blog says, keeping "to some degree" as in the talk. |
| Fourth `##` heading | When Wrong Is Done to a Pure Person | When Wrong Is Done to a Pure Person, Does Devotion Protect Them? | Question heading (report section 4: "Does Devotion Protect?"); the section answers it. |
| Fifth `##` heading | The Example of Meerabai | How Did Meerabai Digest the Poison? | Question heading matching "Meerabai poison story" (secondary keyword) and FAQ 5; the section answers it. |

No teaching, example, order of ideas, H1 or formatting changed (the blog quotes no verse), and the number and order of headings are the same. "धन और भोजन के अलग-अलग मेल" / "When Money and Food Combine in Different Ways" was not made a question (report section 4 offered it), because `images.txt` places `inline.jpg` under it. All five `links` phrases and the `also_read` heading ("अन्याय का धन, सात्विक भोजन" / "Unjust Money, Pure Food") are unchanged in each language, and the page build found them all.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages).
  - Focus keyword in the URL slug (English).
  - Focus keyword within the first 100 words (both languages).
  - A direct answer (40–60 words) early on, and question headings.
- Section 12 was missing from the report. It has been added.
- Still unmet (1): "Each tag can be shared by at least 3 posts": the tag "धन की शुद्धि" / "Purity of Wealth" is used by this post only so far. Tags are outside this fix's scope; it can stay if later posts on money share it, or be dropped by `/seo_blog`.
- Left alone on purpose: the Sanskrit review's corrections (फलश्रुति gloss, सात्विक → सात्त्विक, the द्रव्य-शुद्धि takeaway wording, the Meerabai description in Hindi) are for the editor to make in the original blog, as they are wording and accuracy points rather than SEO items. If the Key Takeaways line "भक्ति और सत्त्वगुण बाहर से आई तामसिकता को भी काट सकते हैं" or "अन्याय का धन, सात्विक भोजन" changes (for example to सात्त्विक), seo.json's link phrase and also_read heading must be updated too.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | honest-earnings-sattvic-food | honest-earnings-and-sattvic-food |
| wordpress.hi.slug | imandar-kamai-aur-satvik-bhojan | imandar-kamai-aur-satvik-bhojan (unchanged) |

Nothing else changed: focus keywords, secondary keywords, titles and meta descriptions (all already contain the focus keyword), `links`, `also_read`, `alt`, `caption`, `related`, category and tags. The report was updated to match: section 2 (keyword note), 3 (the meta descriptions and slugs in seo.json marked as recommended; the English slug updated), 4 (a note on what was applied), 8 (the suggested English URL slug), 11 (the new seo.json) and 12 (the checklist, newly added).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | imandar-kamai-aur-satvik-bhojan | honest-earnings-and-sattvic-food |
| focus_keyword | ईमानदार कमाई और सात्विक भोजन | honest earnings and sattvic food |
| title | ईमानदार कमाई और सात्विक भोजन: थाली में धन का असर | Honest Earnings and Sattvic Food: What Your Plate Carries |
| meta_description | क्या सात्विक भोजन ही काफ़ी है? आचार्य उपेंद्र जी बताते हैं कि ईमानदार कमाई और सात्विक भोजन मिलकर फल देते हैं, और भक्ति ने मीराबाई को विष से कैसे बचाया। | Is sattvic food enough? Acharya Upendra Ji explains why honest earnings and sattvic food work together, and how devotion protected Meerabai from poison. |
