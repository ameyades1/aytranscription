only_way_know_god: SEO fix

The fixed texts are `only_way_know_god_blog_seo.txt` (Hindi) and `only_way_know_god_blog_seo_en.txt` (English). The originals are unchanged. The verse, its translation and reference, the H1, every `links` phrase and the `also_read` heading are untouched. The Sanskrit review's verse corrections (tools/review/only_way_know_god.md) are left for a separate verse edit, because this fix does not touch scripture.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph, last sentence | तो उत्तर क्या होगा? | तो उत्तर क्या होगा? और अपने भगवान को कैसे जानें? | The focus keyword "भगवान को कैसे जानें" was not in the body; it now appears in the first 100 words (word 54) |
| New paragraph after the introduction (before the first H2) | (none) | संक्षेप में उत्तर यह है: भगवान के केवल रूप से प्रेम काफ़ी नहीं; मर्म जाने बिना वह आकर्षण भर है। गुरुदेव के अनुसार मूर्ति और शास्त्र मानचित्र हैं, और जीवित गुरु वह चालक है जो आज का रास्ता जानता है। गुरु से दीक्षा लेकर, आंखें खोलकर, मानचित्र के सहारे मूल तक पहुंचना ही मार्ग है। | No direct answer early; this 55-word answer uses only what the blog says later (report section 5) |
| H2 | जिसने देखा है, वही बता सकता है | जीवित गुरु क्यों आवश्यक है? जिसने देखा है, वही बता सकता है | Turns the heading into the question readers search for (secondary keyword); the section answers it |
| H2 | शास्त्र का संकेत: रूप साधकों के लिए है | शास्त्र क्या कहते हैं: ईश्वर का रूप किसके लिए है? | Question heading, as suggested in report section 4; the section answers it |

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the introduction (before the first H2) | (none) | Here is how to know God: loving His form is not enough, because without understanding its essence that love is only infatuation. The murti and the scriptures are the map, and a living Guru is the driver who knows today's road. Take diksha from such a Guru and travel with open eyes, map in hand, to reach the original. | The focus keyword "how to know God" was not in the body; it now appears in the first 100 words (word 81), and the 59-word paragraph is the early direct answer, built only from the blog |
| H2 | Only Someone Who Has Seen Can Describe | Why Do You Need a Living Guru? Only Someone Who Has Seen Can Describe | Question heading matching the searched "why you need a living Guru"; the section answers it |
| H2 | The Scriptures Agree: Form Is Meant for Seekers | What Do the Scriptures Say: Who Is God's Form For? | Question heading, as suggested in report section 4; the section answers it |

## Checklist

Now met:
- Focus keyword in the body text (Hindi and English); `tools/check_seo.py` failed on this before the fix.
- Focus keyword within the first 100 words (Hindi and English).
- Focus keyword in the meta description (English); `check_seo.py` failed on this before the fix.
- Focus keyword taken from wording the article uses (true of the `_seo` texts).
- Early direct answer (40–60 words) in both languages, and question headings.

Still unmet: none. The report had no section 12 before this fix; it was added with every item met.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | How do you truly know God? Acharya Ji explains why loving only the form is infatuation, why the murti is a map and why a living Guru must drive the way. | How to know God? Acharya Ji explains why loving only the form is infatuation, why the murti is a map and why a living Guru must drive the way. (142 chars) |
| wordpress.hi.slug | bhagwan-ko-kaise-jane | unchanged |
| wordpress.en.slug | how-to-know-god-murti-map-guru | unchanged (already contains the focus keyword) |
| focus keywords, titles, Hindi meta, links, also_read | | unchanged |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bhagwan-ko-kaise-jane | how-to-know-god-murti-map-guru |
| focus_keyword | भगवान को कैसे जानें | how to know God |
| title | भगवान को कैसे जानें? मूर्ति मानचित्र है, गुरु चालक | How to Know God: The Murti Is the Map, the Guru the Driver |
| meta_description | भगवान को कैसे जानें? आचार्य जी समझाते हैं कि केवल रूप से प्रेम आकर्षण है, मूर्ति एक मानचित्र है, और मूल तक पहुंचने के लिए जीवित गुरु रूपी चालक क्यों चाहिए। | How to know God? Acharya Ji explains why loving only the form is infatuation, why the murti is a map and why a living Guru must drive the way. |
