hardcore_non_vegetarian_awakening: SEO fix

The check failed on one item in each language: the focus keyword ("मांसाहार क्यों नहीं करना चाहिए" / "challenge for meat eaters") was in the title, meta description and slug, but nowhere in the body. As a result, the report's section 4 also found it missing from the first 100 words, and section 5 found the post had no early direct answer. Each language gets two changes: a short direct answer after the intro, built from the blog's own challenge and closing reflection, which carries the focus keyword; and the last content H2 rephrased as a question carrying a secondary keyword. The report had no section 12; it has been added with every item marked.

## Hindi (`hardcore_non_vegetarian_awakening_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…बस एक खुली चुनौती।") | (none) | मांसाहार क्यों नहीं करना चाहिए? आचार्य जी इसका उत्तर किसी तर्क से नहीं, एक चुनौती से देते हैं: दूसरों को खाने से पहले खुद को खाकर दिखाओ। रोज़ अपने ही शरीर का एक छोटा टुकड़ा, किसी भी मसाले के साथ, हलाल करके या मंत्र बोलकर। जो पीड़ा हम अपने लिए नहीं सह सकते, वह किसी और जीव को देना कैसे उचित हो सकता है? | The focus keyword was not in the body (check_seo error) or the first 100 words, and there was no early direct answer. This answer of about 55 words restates only the blog's challenge (sections 1–3) and its closing reflection, following the report's section 5. It does not repeat the `see_god_even_enemy` link phrase, so that link stays on the closing line. |
| H2 before "यह धरती के हर व्यक्ति के लिए खुली चुनौती है।" | ## एक दिन का दिखावा नहीं, रोज़ का नियम | ## मांसाहारी को खुली चुनौती: रोज़ कौन कर पाएगा? | Rephrased as a question using the secondary keyword "मांसाहारी को खुली चुनौती". The section answers it: the challenge is open and daily, and it closes on "तो कौन कर पाएगा?". Number and order of headings unchanged. |

## English (`hardcore_non_vegetarian_awakening_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…an open challenge.") | (none) | Why not eat meat? Acharya Ji answers with a challenge for meat eaters rather than an argument: before eating others, eat yourself first. One small piece of your own body every day, with any spices, the halal way or with a mantra. If we cannot bear that pain ourselves, how can it be right to inflict it on another being? | The focus keyword was not in the body (check_seo error) or the first 100 words, and there was no early direct answer. This answer of about 58 words restates only the blog's challenge and closing reflection (report section 5), and opens with the secondary query "why not eat meat". It does not repeat the `see_god_even_enemy` link phrase. |
| H2 before "This is an open challenge to every person on earth." | ## A Daily Rule, Not a One-Day Show | ## Hardcore Non-Vegetarian? Could You Do It Every Day? | Rephrased as a question using the secondary keyword "hardcore non-vegetarian" (the video's title wording). The section answers it: one piece every single day, and "Who among you could manage that?". Number and order of headings unchanged. |

No teaching, example or order of ideas changed, and no H1 was touched. The blog has no verses. The Markdown format is kept. All four `links` phrases and the `also_read` heading ("मंत्र बोलकर काटो, फिर?" / "What If You Recite a Mantra While You Cut?") are still in both texts once each, confirmed by grep. The inline image's heading ("स्वाद के प्रेमी से एक खुला प्रश्न" / "An Open Question for Those Who Love the Taste") is unchanged.

## Checklist

- Now met: the focus keyword is in the body text in both languages (the check_seo error) and within the first 100 words; there is an early direct answer of 40–60 words; one H2 per language is phrased as a question.
- Already met and still met: every other item in the new section 12. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - Sanskrit review issues 1–3 (Minor: whose "बच्चों" / "young ones" are meant, "stunt" in the Hindi text, and a framing sentence that the challenge is rhetorical) are not SEO items, and issue 1 needs the transcript. They are left for the editor to fix in the original blog. The new direct answer does state the challenge's point as a question early on.
  - The report's section 4 suggested adding a new H2 before "मुख्य बातें" / "Key Takeaways". It was not added, because the number of headings must stay the same. An existing H2 was rephrased instead.
  - The report's sections 1, 4, 5 and 10 still describe the original texts. This fix may only edit sections 2, 3, 8, 11 and 12.

## seo.json changes

None. Both focus keywords were already the searched wording, and the `_seo` texts now use them in the body. Titles, meta descriptions and slugs already contain them, and no link phrase or `also_read` heading was touched.

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | mansahar-kyon-nahi-karna-chahiye | mansahar-kyon-nahi-karna-chahiye (unchanged) |
| wordpress.en.slug | challenge-for-meat-eaters | challenge-for-meat-eaters (unchanged) |

The report's section 11 therefore still matches seo.json. Section 3 already marks these titles and metas as recommended, and section 8 already uses them, so neither needed a change. Sections 2 (keyword note) and 12 (new checklist) were updated.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | mansahar-kyon-nahi-karna-chahiye | challenge-for-meat-eaters |
| focus_keyword | मांसाहार क्यों नहीं करना चाहिए | challenge for meat eaters |
| title | मांसाहार क्यों नहीं करना चाहिए? खुद को खाकर दिखाओ | A Challenge for Meat Eaters: Eat Yourself First |
| meta_description | मांसाहार क्यों नहीं करना चाहिए? आचार्य उपेंद्र जी हर कट्टर मांसाहारी को एक खुली चुनौती देते हैं: जो पीड़ा आप खुद नहीं सह सकते, वह किसी जीव को क्यों दें? | A challenge for meat eaters from Acharya Upendra Ji: if you could not bear to eat a small piece of yourself, is it right to make another being bear it? |
