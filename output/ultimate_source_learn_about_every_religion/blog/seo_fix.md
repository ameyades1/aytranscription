ultimate_source_learn_about_every_religion: SEO fix

SEO copies: `ultimate_source_learn_about_every_religion_blog_seo.txt` (Hindi) and `ultimate_source_learn_about_every_religion_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the italic standfirst | (none) | गीता जी की समझ में सभी धर्मों का मूल स्रोत एक है: वेदों पर आधारित सनातन धर्म, जिससे आगे अन्य धर्म निकले। तत्व के स्तर पर सब धर्मग्रंथों में गहरा साम्य है; यह उन्हें तब समझ आया जब गुरुजी ने भविष्य पुराण और बाइबल के अंश पढ़कर भगवद्गीता से उनका मेल दिखाया। | Searched wording "सभी धर्मों का मूल स्रोत" (video title) was missing from the body, and no focus keyword appeared in the first 100 words. This also gives a direct answer early (53 words). It is built only from the blog: sections "जब धर्मग्रंथ आमने-सामने आए", "मैं हिंदू नहीं हूँ" and Key Takeaways, and is attributed to Geeta Ji (review issue 6). "तत्व" follows the blog's current spelling. |
| `##` heading before "सब धर्मों के मूल धर्मगुरु…" | धर्म नहीं बिगड़ता, उसकी व्याख्या बिगड़ती है | क्या सब धर्म एक समान हैं? | This is the question people search ("सब धर्म एक समान हैं", High). The section answers it: the founding teachers give the same knowledge, no religion is greater or lesser, and later interpretation causes the differences (the body text is unchanged). |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the italic standfirst | (none) | In Geeta Ji's understanding, the essence of all religions is the same: their founding teachers give one knowledge, and Sanatana Dharma, founded on the Vedas, is the root from which the others arose. This unity of all religions became clear to her when Acharya Ji read passages from the Puranas and the Bible and showed how they agree with the Bhagavad Gita. | Searched wording "unity of all religions" (thumbnail) was missing from the body, and the focus keyword "essence of all religions" was not in the first 100 words. This also gives a direct answer early (58 words), built only from the blog's own statements and attributed to Geeta Ji. It does not reuse the `dharma_teaches_us` link phrase, so the link stays where it was. |
| `##` heading before "The founding teachers of every religion…" | Religion Does Not Go Wrong; Its Interpretation Does | Are All Religions the Same? | Matches the search "are all religions the same" (High). The section answers it and its body text is unchanged. |

"When the Scriptures Stood Side by Side" / "जब धर्मग्रंथ आमने-सामने आए" was not turned into a question (section 4's suggestion), because `blog/images.txt` places the inline image by that heading. The also_read heading ("मैं हिंदू नहीं हूँ" / "I Am Not a Hindu"), every `links` phrase, the H1 and all verses are unchanged.

## Checklist

Now met:
- Focus keyword placement: within the first 100 words (both languages).
- Searched wording in the body and now the focus keyword (Hindi "सभी धर्मों का मूल स्रोत", English "unity of all religions").
- Direct answer paragraph early in both languages (not a checklist item; this was section 5 of the report).

Still unmet: none. `python3 tools/check_seo.py ultimate_source_learn_about_every_religion` passes.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | सब धर्मों का मूल स्रोत एक: एक साधिका का अनुभव | सभी धर्मों का मूल स्रोत एक: एक साधिका का अनुभव |
| title.en | Essence of All Religions: A Seeker's Story of One Source | Unity of All Religions: A Seeker's Story of One Source |
| wordpress.hi.slug | sab-dharmon-ka-mool-srot | sabhi-dharmon-ka-mool-srot |
| wordpress.hi.focus_keyword | सब धर्मों का मूल स्रोत | सभी धर्मों का मूल स्रोत |
| wordpress.hi.secondary_keywords | सभी धर्मों का मूल स्रोत, सब धर्म एक समान हैं, गीता और बाइबल में समानता, सनातन धर्म सबसे प्राचीन धर्म | सब धर्मों का मूल स्रोत, सब धर्म एक समान हैं, गीता और बाइबल में समानता, सनातन धर्म सबसे प्राचीन धर्म |
| wordpress.hi.meta_description | सब धर्मों का मूल स्रोत क्या है? साधिका गीता डांगी बताती हैं… | सभी धर्मों का मूल स्रोत क्या है? साधिका गीता डांगी बताती हैं… (rest unchanged, 155 characters) |
| wordpress.en.slug | essence-of-all-religions | unity-of-all-religions |
| wordpress.en.focus_keyword | essence of all religions | unity of all religions |
| wordpress.en.secondary_keywords | unity of all religions, are all religions the same, Bhagavad Gita and Bible similarities, Sanatana Dharma oldest religion | essence of all religions, are all religions the same, Bhagavad Gita and Bible similarities, Sanatana Dharma oldest religion |
| wordpress.en.meta_description | The essence of all religions is one: how seeker Geeta Dangi's hidden bias turned to respect when Acharya Ji showed that the Gita and the Bible agree. | Unity of all religions, in one seeker's story: Geeta Dangi's hidden bias turned to respect when Acharya Ji showed that the Gita and the Bible agree. (148 characters) |

`links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report's sections 2, 11 and 12 were updated to match. Sections 3 and 8 still give the old titles and slugs.
