manifesting_goals_correctly: SEO fix

The report found one failing SureRank check in each language: the focus keyword was not in the body text, because the body worded the idea differently ("**इच्छा** और **प्रबल इच्छाशक्ति** में क्या अंतर है" / "how a **wish** differs from **strong willpower**"). It also recommended a 40–60 word direct answer after the intro and one question heading. The fixes below add the searched wording once, inside a direct-answer paragraph built only from what the blog already says.

## Hindi (`manifesting_goals_correctly_blog_seo.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| After the intro, before the first `##` | (no paragraph) | संक्षेप में, इच्छा और इच्छाशक्ति में अंतर यह है: इच्छा मन में आई क्षणिक चाह है, जबकि प्रबल इच्छाशक्ति वह संकल्प है जिसके लिए व्यक्ति पूरे मन से प्रयास करता है। कर्मयोग की दृष्टि से हल्की इच्छा भी कर्म है और उसका फल आता है, अक्सर ऐसे अनुभव के रूप में जो सिखाता है कि "यह नहीं चाहिए।" प्रबल इच्छाशक्ति हो तो मार्ग स्वयं मिलता चला जाता है। | Focus keyword "इच्छा और इच्छाशक्ति में अंतर" in the body and in the first 100 words; direct answer for featured snippets. Every point comes from the blog (intro, "क्या हल्की इच्छा भी कर्म है?", the reflection question, "मुख्य बातें"). |
| 6th `##` heading | जब इच्छा प्रबल होती है | प्रबल इच्छाशक्ति से मार्ग कैसे खुलता है? | A natural search question that the section answers ("तब मार्ग स्वयं मिलता चला जाता है"); matches the secondary keyword "प्रबल इच्छाशक्ति". |

## English (`manifesting_goals_correctly_blog_seo_en.txt`)

| Where | Before | After | Why |
|---|---|---|---|
| After the intro, before the first `##` | (no paragraph) | Wish vs willpower: a wish is a passing want, while strong willpower is a resolve you work for wholeheartedly. In Karma Yoga, even a faint wish is an action and bears fruit, often as an experience that teaches you, "I don't want this." Wishing alone manifests nothing; a good, strong will finds its own path. | Focus keyword "wish vs willpower" in the body and in the first 100 words; direct answer for featured snippets; "manifests" ties the text to the video title and the secondary keyword "manifesting goals correctly" while keeping the talk's point that wishing alone achieves nothing (authenticity flag 5). |
| 2nd `##` heading | Is a Faint Wish Also an Action? | Is a Faint Wish Also Karma? | Matches the searched question "is a wish also karma"; the Hindi heading already says कर्म, so the meaning is unchanged. |
| 6th `##` heading | When the Wish Runs Deep | How Does Strong Willpower Open the Path? | A natural search question that the section answers ("The path keeps opening up on its own"). |

No teaching, example, scripture, link phrase, "Also read" heading or the H1 was changed. The number and order of headings are the same.

## Checklist

Now met (both languages):
- Focus keyword in the body text (SureRank; `check_seo.py` failed on this before the fix).
- Focus keyword within the first 100 words.
- Direct answer paragraph (40–60 words) placed early.
- Question headings: "क्या हल्की इच्छा भी कर्म है?" was already one; now also "प्रबल इच्छाशक्ति से मार्ग कैसे खुलता है?" / "Is a Faint Wish Also Karma?" and "How Does Strong Willpower Open the Path?".

Still unmet: none. (The report had no section 12 before; it has been added, with every item met.)

## seo.json changes

None. The focus keywords were already the searched wording and are now in the body, so the focus keyword, secondary keywords, slugs, titles, meta descriptions, `links` and `also_read` all stay as they were.

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | ichha-aur-ichhashakti-mein-antar | ichha-aur-ichhashakti-mein-antar (unchanged) |
| wordpress.en.slug | wish-vs-willpower | wish-vs-willpower (unchanged) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ichha-aur-ichhashakti-mein-antar | wish-vs-willpower |
| focus_keyword | इच्छा और इच्छाशक्ति में अंतर | wish vs willpower |
| title | इच्छा और इच्छाशक्ति में अंतर: हर चाह का फल आता है | Wish vs Willpower: Are You Manifesting Goals Correctly? |
| meta_description | क्या हल्की इच्छा भी कर्म है? आचार्य उपेंद्र जी बताते हैं इच्छा और इच्छाशक्ति में अंतर: क्षणिक चाह का फल कैसे आता है, प्रबल इच्छाशक्ति से मार्ग कैसे खुलता है। | Is a passing wish also karma? Acharya Upendra Ji explains wish vs willpower: why idle wishes bear unwanted fruit, and how strong will opens the path ahead. |
