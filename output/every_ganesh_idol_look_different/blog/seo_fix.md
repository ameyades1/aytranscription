every_ganesh_idol_look_different: SEO fix

`check_seo.py` failed on the SureRank checks: the focus keywords "गणपति की मूर्ति कैसी होनी चाहिए" and "how to choose a Ganesh idol" were not in either body, the Hindi keyword was not in the Hindi title tag, and the English slug (`how-to-choose-ganesh-idol`) lacked the keyword's "a". The opening also asked its question without an early answer. Each language gets two changes: a short direct answer after the intro, built only from what the blog already says (and the report's section 5), which carries the focus keyword in the first 100 words; and the first H2 rephrased as the searched question from the video title. Focus keywords stay as they were.

## Hindi (`every_ganesh_idol_look_different_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…उसका रूप कौन तय करता है?") | (none) | तो गणपति की मूर्ति कैसी होनी चाहिए? आचार्य जी के अनुसार उसका रूप दुकानदार या हमारी अपनी पसंद से नहीं, ऋषियों के वर्णन से आना चाहिए। शुरुआत अपनी रुचि से हो सकती है, पर गणेशोत्सव सजावट की प्रतियोगिता नहीं, नर से नारायण तक की यात्रा है, और मूर्ति उस यात्रा की पहली सीढ़ी है। | Direct answer (54 words) restating the blog's own sections and Key Takeaways; puts the focus keyword in the body and the first 100 words. |
| First H2 | ## इतने सारे गणपति, इतने सारे रूप | ## हर गणपति की मूर्ति अलग क्यों दिखती है? | The searched question (secondary keyword, video title); the section describes the many forms and asks whose choice they reflect. Number and order of headings unchanged. |

## English (`every_ganesh_idol_look_different_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…the idol you bring home?") | (none) | Here is how to choose a Ganesh idol: Acharya Ji says its form should come from the sages' description, not from the shopkeeper or our own taste. You may begin with your own preference, but the festival is not a decorating contest. It is the journey from the human to the Divine, and the idol is its first step. | Direct answer (59 words), built only from the blog's own points; puts the focus keyword in the body and the first 100 words. |
| First H2 | ## So Many Ganpatis, So Many Faces | ## Why Does Every Ganesh Idol Look Different? | The searched question (secondary keyword, video title); the section answers it. Number and order of headings unchanged. |

No teaching, example, order of ideas, H1 or Markdown changed; the blog has no verses. All four `links` phrases and the `also_read` heading ("बालवाड़ी से पहली कक्षा तक" / "From Balwadi to First Grade") are still in both texts, confirmed by grep. The inline image's heading ("निराकार तक पहुंचने की सीढ़ी") is unchanged.

## Checklist

The report had no section 12; one was added (from the standard checklist) with the fix.

- Now met: focus keyword in the body text and within the first 100 words (both languages); Hindi focus keyword in the SEO title; English focus keyword in the slug; one question H2; a direct answer of 40–60 words early in the post.
- Already met and still met: every other item. `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose: the Sanskrit review's two Minor issues ("सोला" vs "sovale"; the zero-to-six analogy) are not SEO items and are left for the editor to fix in the original blog. Report sections 1, 4, 5 and 10 are not edited (this fix may only edit sections 2, 3, 8, 11 and 12).

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | गणपति की मूर्ति कैसी हो? हर मूर्ति अलग क्यों दिखती है | गणपति की मूर्ति कैसी होनी चाहिए? ऋषियों का स्वरूप (49 characters; report section 3, option 2) |
| wordpress.hi.slug | ganpati-ki-murti-kaisi-ho | ganpati-ki-murti-kaisi-honi-chahiye |
| wordpress.en.slug | how-to-choose-ganesh-idol | how-to-choose-a-ganesh-idol (27 characters, contains the focus keyword) |

Focus keywords, secondary keywords, `title.en`, both meta descriptions (they already contain the keywords), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2, 3 and 8 were updated to match and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ganpati-ki-murti-kaisi-honi-chahiye | how-to-choose-a-ganesh-idol |
| focus_keyword | गणपति की मूर्ति कैसी होनी चाहिए | how to choose a Ganesh idol |
| title | गणपति की मूर्ति कैसी होनी चाहिए? ऋषियों का स्वरूप | How to Choose a Ganesh Idol: Whose Form Should It Follow? |
| meta_description | गणपति की मूर्ति कैसी होनी चाहिए? आचार्य उपेंद्र जी बताते हैं कि उसका रूप फैशन से नहीं, ऋषियों के वर्णन से आए, क्योंकि गणेशोत्सव नर से नारायण की यात्रा है। | How to choose a Ganesh idol? Acharya Upendra Ji explains why its form should follow the sages' description, not trends, and why the idol is a first step. |
