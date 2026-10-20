evolution_of_dharma_sanatan_dharma: SEO fix

Fixed texts: `evolution_of_dharma_sanatan_dharma_blog_seo.txt` (Hindi) and `evolution_of_dharma_sanatan_dharma_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes (3)

| Where | Before | After | Why |
|---|---|---|---|
| After the second intro paragraph, before the first `##` | (no paragraph) | संक्षेप में, सनातन धर्म का विकास वेद के चार भागों में दिखता है: मंत्र संहिता में ऋषियों ने परमेश्वर और प्रकृति की स्तुति की; ब्राह्मण भाग में यह स्तुति कृति बनी, यानी यज्ञ, दान और पूजा; आरण्यक में वन का चिंतन आया; और उपनिषदों में आत्मा का ज्ञान मिला, जो अंतिम विद्या है। | Focus keyword was missing from the body (check_seo failed); now within the first 100 words. Adds a 52-word direct answer built only from the blog's four-stage list and its "अंतिम विद्या… आत्मा को जानने की विद्या" |
| First `##` heading | पहला कदम: जब ऋषियों ने प्रकृति को धन्यवाद कहा | मंत्र संहिता क्या है? जब ऋषियों ने प्रकृति को धन्यवाद कहा | Question readers search; the section defines the Mantra Samhita |
| `##` heading before "तीन-चार पीढ़ियों बाद…" | जब पूजा यांत्रिक हो गई | पूजा यांत्रिक क्यों हो गई? | Question readers search; the section answers why (the generations forgot whom and why) |

## English changes (4)

| Where | Before | After | Why |
|---|---|---|---|
| Second intro paragraph, first sentence | In this discourse, Acharya Upendra Ji takes us on a journey through the Vedas | In this discourse on the evolution of Sanatan Dharma, Acharya Upendra Ji takes us on a journey through the Vedas | Focus keyword was missing from the body (check_seo failed); now within the first 100 words |
| After the second intro paragraph, before the first `##` | (no paragraph) | In short, Sanatan Dharma grew through the four parts of the Vedas. In the Mantra Samhita the rishis praised God and nature; in the Brahmanas that praise became action, through yajna, charity and worship; the Aranyakas brought reflection in the forest; and the Upanishads gave the final knowledge, the knowledge of the Self. | 54-word direct answer built only from the blog's four-stage list and its "that final knowledge, the knowledge of the Self"; uses the secondary keyword "four parts of the Vedas" |
| First `##` heading | The First Step: When the Rishis Thanked Nature | What Is the Mantra Samhita? When the Rishis Thanked Nature | Question readers search; the section defines the Mantra Samhita |
| `##` heading before "Three or four generations later…" | When Worship Became Mechanical | Why Did Worship Become Mechanical? | Question readers search; the section answers why |

Not changed: the H1, scripture verses and their meanings, the order and number of `##` sections (14 in each language), every `links` phrase and the Also read heading, the "आरण्यक से उपनिषद तक" / "From Aranyaka to Upanishad" heading (images.txt places the inline image there). The Sanskrit review's corrections (section 10 of the report) change the teaching text and are left to the editor.

## Checklist

Now met:
- Focus keyword in the body text (both languages; check_seo failed on this before)
- Focus keyword in the meta description (English; rewritten)
- Focus keyword within the first 100 words (both languages)
- Focus keyword taken from wording the article already uses (in the fixed texts)
- Direct answer paragraph early, and question-style H2s (report sections 4 and 5)

Still unmet (1):
- No unsupported scriptural claims: the Sanskrit review found claims attributed to scripture without support (Yajurveda split, origin of dakshina, Patanjali, "Do not read me", and others). Correcting them changes the teaching text, which this fix may not do; the editor should apply the review's corrections.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | How did Sanatan Dharma evolve? Acharya Upendra Ji traces the Vedas from praise to ritual, forest reflection and the Upanishads' knowledge of the Self. | The evolution of Sanatan Dharma, as Acharya Upendra Ji tells it: the Vedas grew from praise to ritual, forest reflection and Upanishadic Self-knowledge. |
| wordpress.en.slug | evolution-of-sanatan-dharma | evolution-of-sanatan-dharma (unchanged) |
| wordpress.hi.slug | sanatan-dharma-ka-vikas | sanatan-dharma-ka-vikas (unchanged) |

Focus keywords, secondary keywords, titles, the Hindi meta description, links and also_read are unchanged. The report's sections 2, 3, 8 and 11 were updated to match, and section 12 (the checklist) was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sanatan-dharma-ka-vikas | evolution-of-sanatan-dharma |
| focus_keyword | सनातन धर्म का विकास | evolution of Sanatan Dharma |
| title | सनातन धर्म का विकास: स्तुति से आत्मज्ञान तक की यात्रा | Evolution of Sanatan Dharma: From Praise to Self-Knowledge |
| meta_description | सनातन धर्म का विकास कैसे हुआ? आचार्य उपेंद्र जी बताते हैं वेदों की यात्रा: मंत्र संहिता की स्तुति से ब्राह्मण के कर्मकांड, आरण्यक और उपनिषद के आत्मज्ञान तक। | The evolution of Sanatan Dharma, as Acharya Upendra Ji tells it: the Vedas grew from praise to ritual, forest reflection and Upanishadic Self-knowledge. |
