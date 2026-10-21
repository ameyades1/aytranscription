saturn_mars_succeed_shani_mangal: SEO fix

The check failed before the fix: neither focus keyword was in the blog body or the meta description. The body only says "मंगल और शनि का संबंध" / "the link between Mars and Saturn", which SureRank does not count as "शनि और मंगल का संबंध" / "Saturn and Mars relationship", and both meta descriptions said "शनि और मंगल दोनों" / "both Saturn and Mars" instead. The opening also had no direct answer (report section 5). The fix adds a short direct-answer paragraph after the intro in each language, built only from what the blog already says (Mars as speed, Saturn as control and obstacles, the brakes image, Mars exalted in Capricorn, Saturn's sign) and taken from section 5's snippet. This puts the focus keyword in the body and the first 100 words. It also turns one H2 into the question readers search for (section 4's suggestion), and rewrites both meta descriptions to contain the focus keyword. Focus keywords, slugs and titles are unchanged. The report had no section 12, so this fix added the checklist.

## Hindi (`saturn_mars_succeed_shani_mangal_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro ("…दोनों रूपों का अर्थ।"), new paragraph | (none) | संक्षेप में, शनि और मंगल का संबंध संतुलन का है। ज्योतिष में मंगल गति का और शनि नियंत्रण व विघ्न का प्रतीक है। सफलता के लिए दोनों चाहिए, जैसे गाड़ी में ब्रेक इसलिए होता है कि हम भरोसे के साथ तेज गति से चला सकें। शनि की राशि मकर में मंगल उच्च का होता है; दोनों एक-दूसरे के पूरक हैं। | Focus keyword in the body and the first 100 words (word 67). An early direct answer (60 words) built from the blog's own sections ("मंगल यानी गति…", "ब्रेक किसलिए होता है?", "शनि और मंगल…") and section 5's snippet. No dosh, yuti or remedy (flag 5) |
| Last H2 before the takeaways | ## शनि और मंगल: एक-दूसरे के पूरक | ## शनि और मंगल एक-दूसरे के पूरक कैसे हैं? | The section answers this question (section 4's suggestion, FAQ 1) |

## English (`saturn_mars_succeed_shani_mangal_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the intro ("…the one who removes them."), new paragraph | (none) | In short, the Saturn and Mars relationship is one of balance. In astrology, Mars stands for speed and Saturn for control and obstacles. Success needs both, just as a car has brakes so that we can drive fast with confidence. Mars is exalted in Capricorn, the sign ruled by Saturn, which shows how the two complete each other. | Focus keyword in the body and the first 100 words (word 73). An early direct answer (58 words) built from the blog's own sections and section 5's snippet ("balance" follows the blog's "the force that always balances it is Saturn") |
| Last H2 before the takeaways | ## Saturn and Mars Complete Each Other | ## How Do Saturn and Mars Complete Each Other? | The section answers this question (section 4's suggestion, FAQ 1) |

No teaching, example, order of ideas or H1 was changed, and the number and order of headings are the same (the blog quotes no verse). The intro's own wording ("मंगल और शनि का संबंध" / "the link between Mars and Saturn") was left as it is. "बिना स्टेशन की रेलगाड़ी" / "A Train With No Stations" (where `inline.jpg` sits) and the `also_read` heading are untouched. The new paragraphs avoid the `links` phrases; all five phrases and the `also_read` heading are still in both texts, word for word. The Sanskrit review's corrections (the Mangalmurti/Mars gloss, the Saturn → Ganesha bridge sentence, यश → सफलता) change the talk's content beyond SEO, so they are left to the editor (section 10) and were not applied here.

## Checklist

- Now met: the focus keyword is in the body text and within the first 100 words in both languages, and in both meta descriptions. "Focus keyword taken from wording the article already uses" is met for the `_seo` texts. `check_seo.py` passes, where it failed before. Both texts give a direct answer early, and one H2 per language is now a question.
- Already met and still met: every other item in section 12 (added to the report by this fix, all items marked).
- Still unmet: none.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | सफलता के लिए शनि और मंगल दोनों क्यों ज़रूरी हैं? आचार्य उपेंद्र जी बताते हैं गति और नियंत्रण का संतुलन, ब्रेक का असली उद्देश्य और विघ्नकर्ता गणपति का अर्थ। | शनि और मंगल का संबंध क्या है? आचार्य उपेंद्र जी बताते हैं सफलता के लिए गति और नियंत्रण का संतुलन, ब्रेक का असली उद्देश्य और विघ्नकर्ता गणपति का अर्थ। (149) |
| wordpress.en.meta_description | Why do you need both Saturn and Mars to succeed? Acharya Upendra Ji explains speed and control, the real purpose of brakes, and Ganesha as Vighnakarta. | What is the Saturn and Mars relationship, and why does success need both? Acharya Upendra Ji explains speed, control and the real purpose of brakes. (148) |
| wordpress.hi.slug | shani-aur-mangal-ka-sambandh | shani-aur-mangal-ka-sambandh (unchanged) |
| wordpress.en.slug | saturn-and-mars-relationship | saturn-and-mars-relationship (unchanged; already built from the focus keyword, 28 characters) |
| wordpress.hi.focus_keyword | शनि और मंगल का संबंध | unchanged |
| wordpress.en.focus_keyword | Saturn and Mars relationship | unchanged |

Both focus keywords were already the searched wording and are now in the `_seo` texts, so they stay; no other talk uses them. Both titles already contained their focus keywords and are unchanged. `secondary_keywords`, `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in section 2 (keyword note), section 3 (the meta descriptions and slugs in seo.json marked recommended), section 8 (Hindi and English description, and the suggested slugs added to the URL placeholder note; headlines and keywords unchanged) and section 11, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | shani-aur-mangal-ka-sambandh | saturn-and-mars-relationship |
| focus_keyword | शनि और मंगल का संबंध | Saturn and Mars relationship |
| title | शनि और मंगल का संबंध: ब्रेक से सीखें सफलता का रहस्य | Saturn and Mars Relationship: Why Brakes Help You Succeed |
| meta_description | शनि और मंगल का संबंध क्या है? आचार्य उपेंद्र जी बताते हैं सफलता के लिए गति और नियंत्रण का संतुलन, ब्रेक का असली उद्देश्य और विघ्नकर्ता गणपति का अर्थ। | What is the Saturn and Mars relationship, and why does success need both? Acharya Upendra Ji explains speed, control and the real purpose of brakes. |
