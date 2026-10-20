chant_thousand_names_god: SEO fix

The `_seo` texts (`chant_thousand_names_god_blog_seo.txt`, `chant_thousand_names_god_blog_seo_en.txt`) are what gets published. The original blog texts are unchanged.

## Hindi changes (3)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after "एक ही ईश्वर के हज़ार नाम लेना क्यों?" (first section) | (none) | सहस्रनाम का अर्थ यही है कि ये हज़ार नाम एक ही परमात्मा के हैं। इसका उद्देश्य हज़ार बार रटना नहीं, बल्कि हर रूप में उसी एक को पहचानना है। जैसे आपके अनेक नाम होकर भी आप एक हैं, वैसे ही ईश्वर के सब नाम एक ही सत्य के हैं। गीता का "वासुदेवः सर्वम्" यही कहता है: सब कुछ परमात्मा है। | The focus keyword "सहस्रनाम का अर्थ" was nowhere in the body (only "सहस्रनाम का असली अर्थ"). This adds it in the first 100 words (about word 87), plus a direct answer (60 words) built only from the blog's own key points and Gita 7.19 |
| H2 4 | सहस्रनाम में संसार का ही वर्णन है | सहस्रनाम के नाम किसका वर्णन करते हैं? | A question readers search for, which the section answers (report section 4) |
| H2 6 | दूसरा यहाँ कोई है ही नहीं | दूसरों की मदद क्यों करें? | A question readers search for; the section opens with that question and answers it |

## English changes (3)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after "Why call the one God by a thousand names?" (first section) | (none) | The meaning of sahasranama is simple: all thousand names belong to one God. A sahasranama is not about rote repetition; it is about recognising that one God in every form. Just as you remain one person despite your many names, God's names belong to one truth, the Gita's "Vasudevah sarvam": all is God. | Adds the exact focus keyword "meaning of sahasranama" early (before, the body only had "the real meaning of a sahasranama", in section 3) and a direct answer (53 words) from the blog's own key points |
| H2 4 | Every Sahasranama Describes the World | What Do the Names in a Sahasranama Describe? | Question heading (report section 4) |
| H2 6 | There Is No "Other" Here | Why Should We Help Others? | Question heading; the section answers it |

Not touched: the H1s, all verses, translations and references, the headings used by images.txt ("आपके भी तो कितने नाम हैं") and by Also read ("कहानी के रचयिता आप ही हैं" / "You Wrote the Story Yourself"), and every `links` phrase. All were checked as still present.

## Checklist

Now met:
- Hindi focus keyword in the SEO title, the meta description and the body text (all three were failing)
- English focus keyword in the meta description (was failing)
- Hindi focus keyword in the first 100 words
- Direct answer placed early (40–60 words) in both languages
- One or two question H2 headings per language
- `python3 tools/check_seo.py chant_thousand_names_god` passes

Still unmet (1):
- English focus keyword within the first 100 words (preferred): it comes at about word 112. The direct answer has to follow the question it answers ("Why call the one God by a thousand names?"), which comes at about word 108. Putting it earlier would mean answering before the question is asked, or changing the opening.

Notes, not fixed here (outside this command's scope):
- The Sanskrit review's issues (tools/review/chant_thousand_names_god.md: Gita 17.23 "first half" marking, the 17.23-27 pointer, "कृष्ण कहते हैं, गलत किया", the 7.19 gloss, "Vedic hymn") are not SEO fixes and touch verse references and the teaching, so they were not applied. Report section 10 still flags them.
- images.txt's English heading "You Have So Many Names Too" does not match the blog's "You Have Many Names Too" (this was already the case and is unchanged).

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | सहस्रनाम का असली अर्थ: भगवान के हज़ार नाम क्यों? | सहस्रनाम का अर्थ: भगवान के हज़ार नाम क्यों? |
| wordpress.hi.meta_description | एक ही भगवान के हज़ार नाम क्यों? आचार्य उपेंद्र जी बताते हैं कि सहस्रनाम का उद्देश्य रटना नहीं, गीता के 'वासुदेवः सर्वम्' की तरह हर रूप में परमात्मा को देखना है। | सहस्रनाम का अर्थ क्या है? एक भगवान के हज़ार नाम क्यों? आचार्य उपेंद्र जी बताते हैं: उद्देश्य रटना नहीं, 'वासुदेवः सर्वम्' यानी हर रूप में परमात्मा को देखना है। (159 characters) |
| wordpress.en.meta_description | Why chant a thousand names of one God? Acharya Upendra Ji explains that a sahasranama is not rote repetition but a way to see God in every form. | What is the meaning of sahasranama? Acharya Upendra Ji explains why we chant a thousand names of one God: not rote repetition, but to see God in all forms. (155 characters) |
| wordpress.hi.slug | sahasranam-ka-arth | sahasranam-ka-arth (unchanged) |
| wordpress.en.slug | meaning-of-sahasranama | meaning-of-sahasranama (unchanged) |
| focus_keyword (hi / en) | सहस्रनाम का अर्थ / meaning of sahasranama | unchanged (both now appear word for word in the `_seo` bodies) |

Unchanged: title.en, secondary keywords, alt text, captions, links, also_read, related, category and tags. Report section 11 was updated to match, along with the keyword note in section 2. Section 3 now shows the new Hindi title and both new meta descriptions as the recommended ones, and section 8's schema uses the new Hindi alternativeHeadline and both new descriptions (keywords and slugs were already current). Section 12 (the checklist) was added because the report did not have one.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sahasranam-ka-arth | meaning-of-sahasranama |
| focus_keyword | सहस्रनाम का अर्थ | meaning of sahasranama |
| title | सहस्रनाम का अर्थ: भगवान के हज़ार नाम क्यों? | Meaning of Sahasranama: Why Chant 1000 Names of God? |
| meta_description | सहस्रनाम का अर्थ क्या है? एक भगवान के हज़ार नाम क्यों? आचार्य उपेंद्र जी बताते हैं: उद्देश्य रटना नहीं, 'वासुदेवः सर्वम्' यानी हर रूप में परमात्मा को देखना है। | What is the meaning of sahasranama? Acharya Upendra Ji explains why we chant a thousand names of one God: not rote repetition, but to see God in all forms. |
