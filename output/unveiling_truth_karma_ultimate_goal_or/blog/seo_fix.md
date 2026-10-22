unveiling_truth_karma_ultimate_goal_or: SEO fix

The SEO-improved copies are `unveiling_truth_karma_ultimate_goal_or_blog_seo.txt` (Hindi) and `unveiling_truth_karma_ultimate_goal_or_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| "एक खेल जो पूरा जीवन समझा देता है", new paragraph after "और फिर भी, उस बाँस के बिना वह वहाँ तक पहुँच ही नहीं सकता था।" | (none) | तो कर्मयोगी कौन है? आचार्य जी के अनुसार वह व्यक्ति, जो काम करते हुए अपने मन में एक निश्चित अंतिम बिंदु रखता है और समय आने पर स्वयं निवृत्त हो जाता है। कर्मयोग और ज्ञानयोग का संबंध बाँस और शिखर जैसा है: कर्म ज्ञान तक ले जाता है, और फिर खिलाड़ी की तरह उसे छोड़ना होता है। | Focus keyword "कर्मयोगी कौन है" was not in the first 100 words, and there was no early direct answer. It also uses the searched wording "कर्मयोग और ज्ञानयोग" once. Built only from the blog's own sections ("कर्मयोगी कौन है?", "चलता है वाला नहीं चलता", the pole/summit image). 57 words. |
| `##` heading 2 | बाँस है कर्मयोग, शिखर है ज्ञानयोग | क्या कर्मयोग अंतिम लक्ष्य है? | Question heading matching the secondary keyword and the video title; the section answers it, and its first sentence still says the pole is Karma Yoga and the goal is Jnana Yoga. |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| "A Sport That Explains All of Life", new paragraph after "And yet, without that pole, they could never have risen so high." | (none) | Who is a Karma Yogi? According to Acharya Ji, it is someone who works with a clear end point in mind and, when the time comes, steps back of their own accord. Karma Yoga and Jnana Yoga are related like the pole and the summit: action carries you toward knowledge, and then, like the vaulter, you must let it go. | Focus keyword "who is a karma yogi" was not in the first 100 words, and there was no early direct answer. It also names "Karma Yoga and Jnana Yoga" (natural English for the searched "karma yoga vs jnana yoga"). Built only from the blog's own sections. 60 words. |
| `##` heading 2 | The Pole Is Karma Yoga, the Summit Is Jnana Yoga | Is Karma Yoga the Ultimate Goal? | Question heading matching the secondary keyword "is karma yoga the ultimate goal" and the video title; the section answers it, and its first sentence keeps the pole/summit image. |

Not changed: the H1, the Gita 2.47 verse, its translation and reference, every other heading, the order of ideas, all `links` phrases and the `also_read` headings (checked with grep). The Sanskrit review's points (H1 "लाठी", verse reference "first half", Vivekananda account, Nadi Jyotish gloss) are content corrections, not SEO, and are left for the editor.

## Checklist

Now met:
- Focus keyword within the first 100 words (both languages), through the added direct answer.
- Direct answer paragraph early (40–60 words; English 60 words).
- Searched wording "कर्मयोग और ज्ञानयोग" / "Karma Yoga and Jnana Yoga" now used in the body.
- A question heading for the secondary query "क्या कर्मयोग अंतिम लक्ष्य है" / "is karma yoga the ultimate goal".

Still unmet: none. (Section 12 was missing from the report; it has been added and marked. The tag Jnana Yoga / ज्ञानयोग is in 2 posts so far, but it is a core concept more posts will share.)

## Report updates

- Section 2: the wording-mismatch note now says what the `_seo` texts fixed.
- Section 3: the recommended titles, meta descriptions and slugs are marked as the ones in seo.json (unchanged values).
- Section 8: no change needed (headline, alternativeHeadline, description, keywords and slugs already match seo.json).
- Section 11: no change (seo.json unchanged).
- Section 12: added from `tools/prompts/seo_checklist.md` and marked.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.focus_keyword | कर्मयोगी कौन है | unchanged (the primary keyword; the searched "कर्मयोग और ज्ञानयोग" stays secondary) |
| wordpress.en.focus_keyword | who is a karma yogi | unchanged (the primary keyword; "karma yoga vs jnana yoga" is not used word for word and stays secondary) |
| wordpress.hi.slug | karmayogi-kaun-hai | unchanged |
| wordpress.en.slug | who-is-a-karma-yogi | unchanged |
| title, meta_description | (both languages) | unchanged (they already contain the focus keyword) |
| secondary_keywords, tags, links, also_read | | unchanged (no edit touched a link phrase or the Also read heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | karmayogi-kaun-hai | who-is-a-karma-yogi |
| focus keyword | कर्मयोगी कौन है | who is a karma yogi |
| title | कर्मयोगी कौन है? कर्म का बाँस कब छोड़ें | Who Is a Karma Yogi? When to Let Go of the Pole of Action |
| meta description | कर्मयोगी कौन है? बाँस-कूद के उदाहरण से आचार्य उपेंद्र जी बताते हैं कि कर्मयोग ज्ञानयोग तक ले जाता है, और अपने कर्म की एक सीमा तय करना क्यों ज़रूरी है। | Who is a Karma Yogi? Through a pole vault image, Acharya Upendra Ji explains why action leads to Jnana Yoga and why you must set a limit to your work. |
