see_god_even_enemy: SEO fix

Copies: `see_god_even_enemy_blog_seo.txt` (Hindi) and `see_god_even_enemy_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before the first H2) | (none) | शत्रु में भगवान कैसे देखें? आचार्य जी के अनुसार इसके लिए साक्षी भाव चाहिए: जीवन की घटनाओं को एक दर्शक की तरह देखना। तब खलनायक में केवल पात्र नहीं, उसके पीछे का अभिनेता दिखता है। लड़ना पड़े तो कर्तव्य मानकर लड़ें, पर वैर भाव के बिना, क्योंकि हर व्यक्ति में वही ब्रह्म है और हर कोई बदल सकता है। | Direct answer (57 words) built only from the blog's own sections (साक्षी भाव, अभिनेता बनाम पात्र, लड़ना पर वैर भाव के बिना, वाल्या का वाल्मीकि). Puts the focus keyword "शत्रु में भगवान कैसे देखें" in the body and the first 100 words (it was only near-matched in the H1; SureRank error). Uses no link phrase, so the links stay where they were |
| H2 | ## अभिनेता बनाम पात्र | ## साक्षी भाव क्या है? अभिनेता बनाम पात्र | Natural search question (section 4; secondary keyword "साक्षी भाव क्या है"); the section explains the witness view through the actor and the role |
| H2 | ## संभावना उसकी नहीं, आपकी दृष्टि की खत्म होती है | ## क्या कोई व्यक्ति कभी नहीं बदल सकता? | Natural question for readers who feel someone can never change; the section answers it (the potential has not ended, our vision has) |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before the first H2) | (none) | Learning how to see God in your enemy begins, according to Acharya Ji, with sakshi bhava: watching the events of life the way a spectator watches a play. Then you see the actor behind the villain's role, not just the role. If you must fight, fight as a duty but without hostility, because Brahman dwells in every person and anyone can change. | Direct answer (60 words) built only from the blog's own sections. Puts the focus keyword "how to see God in your enemy" in the body text and the first 100 words (it was only in the H1, as "How to See God Even in Your Enemy"). Uses no link phrase |
| H2 | ## The Actor and the Role | ## What Is Sakshi Bhava? The Actor and the Role | Natural search question (secondary keyword "what is sakshi bhava"); the section explains the witness view |
| H2 | ## Your Vision Runs Out, Not Their Potential | ## Can a Person Really Never Change? | Natural question; the section answers it |

Not changed: the H1s, the Shanti Mantra line, its translation and label, the "Also read" heading "लड़ना, पर वैर भाव के बिना" / "Fight, but Without Hatred", the image section heading "वाल्या का वाल्मीकि हो सकता है" / "Valya Can Become Valmiki" (used by `images.txt`), and all four link phrases in each language (checked: each still present). The number and order of headings are unchanged. The Sanskrit review's corrections (half Shanti Mantra label, "according to tradition" for Valya, the English "Brahman within me", the cancer stage, gloss parity) are not SEO edits and are still open (report section 10).

## Checklist

Now met (section 12 added to the report, which had none):
- Focus keyword in the body text and within the first 100 words, both languages.
- Focus keyword in the meta description, both languages.
- Focus keyword in the English slug.
- Two H2s per language phrased as natural search questions.
- A 40–60 word direct answer at the start of the post.

Still unmet (1): no unsupported scriptural claims — the Valya-to-Valmiki story is stated as plain fact and the half Shanti Mantra is not marked as a part (flags 1, 2); fixing them changes the blog's wording beyond SEO, so they are left to the editor.

`python3 tools/check_seo.py see_god_even_enemy` passes. Report sections 2, 3, 8, 11 and 12 updated. Pages rebuilt with `tools/rebuild_blogs.sh see_god_even_enemy` (no notes).

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | क्या शत्रु में भी भगवान दिख सकता है? आचार्य उपेंद्र जी बताते हैं साक्षी भाव, बिना वैर भाव के लड़ना, और क्यों डाकू वाल्या भी महर्षि वाल्मीकि बन सकता है। | शत्रु में भगवान कैसे देखें? आचार्य उपेंद्र जी बताते हैं साक्षी भाव, बिना वैर भाव के लड़ना, और क्यों डाकू वाल्या भी महर्षि वाल्मीकि बन सकता है। |
| wordpress.en.meta_description | Can you see God even in your enemy? Acharya Upendra Ji explains sakshi bhava, how to fight without hatred, and why the bandit Valya could become Valmiki. | Learn how to see God in your enemy: Acharya Upendra Ji explains sakshi bhava, fighting without hatred, and why the bandit Valya could become Valmiki. |
| wordpress.en.slug | see-god-in-your-enemy | how-to-see-god-in-your-enemy |
| wordpress.hi.slug | shatru-mein-bhagwan-kaise-dekhen | shatru-mein-bhagwan-kaise-dekhen (unchanged) |
| focus_keyword, secondary_keywords, title (both) | unchanged | unchanged |
| links, also_read | unchanged | unchanged |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | shatru-mein-bhagwan-kaise-dekhen | how-to-see-god-in-your-enemy |
| focus_keyword | शत्रु में भगवान कैसे देखें | how to see God in your enemy |
| title | शत्रु में भगवान कैसे देखें: पाप से घृणा, पापी से नहीं | How to See God in Your Enemy: Hate the Sin, Not the Sinner |
| meta_description | शत्रु में भगवान कैसे देखें? आचार्य उपेंद्र जी बताते हैं साक्षी भाव, बिना वैर भाव के लड़ना, और क्यों डाकू वाल्या भी महर्षि वाल्मीकि बन सकता है। | Learn how to see God in your enemy: Acharya Upendra Ji explains sakshi bhava, fighting without hatred, and why the bandit Valya could become Valmiki. |
