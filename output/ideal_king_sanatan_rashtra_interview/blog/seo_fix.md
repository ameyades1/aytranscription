ideal_king_sanatan_rashtra_interview: SEO fix

The report had no section 12 checklist yet, so this fix added it (from `tools/prompts/seo_checklist.md`) and marked it for the `_seo` texts. Before the fix, `check_seo.py` failed: neither focus keyword ("अच्छे नेता की पहचान" / "what makes a good leader") was in the body text.

## Hindi (`ideal_king_sanatan_rashtra_interview_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| First H2 | ## एक छोटा सा अनुभव, एक बड़ा सबक | ## अच्छे और बुरे नेता में क्या फर्क है? | Rephrased as the question readers search for (report section 4). The section opens with this question and answers it with the parking example. The number and order of headings are unchanged. |
| Intro, new paragraph after "…एक साधारण से अनुभव में छिपा है।" | (none) | संक्षेप में, आचार्य जी के अनुसार अच्छे नेता की पहचान यह है कि वह केवल मना नहीं करता, साथ में कोई अच्छा विकल्प भी देता है। जो राजा केवल "यहां नहीं" कहकर रोकता है, उससे प्रजा असंतुष्ट होती है। जो निषेध के साथ व्यवस्था भी देता है, उसकी बात लोग थोड़ी कीमत चुकाकर भी सहर्ष मानते हैं। | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 55 words is built only from the blog's own text (its sections and मुख्य बातें, report section 5). It puts the keyword in the first 100 words and repeats no `links` phrase. |

## English (`ideal_king_sanatan_rashtra_interview_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| First H2 | ## A Small Experience, a Big Lesson | ## What Separates a Good Leader from a Bad One? | Rephrased as the question readers search for (report section 4). The section opens with this question and answers it. The number and order of headings are unchanged. |
| Intro, new paragraph after "…an ordinary, everyday experience." | (none) | In short, what makes a good leader, according to Acharya Ji, is that they never only forbid: they also offer some good alternative. A king who only says "not here" leaves his people dissatisfied. One who gives a proper arrangement along with the prohibition is followed gladly, even when it costs people something. | The focus keyword was not in the body (check_seo error), and there was no early direct answer. This answer of about 53 words uses only what the blog already says (its sections and Key Takeaways). The keyword is now within the first 100 words, and no `links` phrase is repeated. |

No teaching, example or order of ideas changed. The H1 is untouched (the blog has no verses), and the Markdown format is kept. All four `links` phrases and the `also_read` heading ("सनातन राष्ट्र की दृष्टि से" / "Through the Lens of a Sanatan Rashtra") are still in both texts once each, confirmed by grep. The inline image's heading ("जब मना करने के साथ रास्ता भी मिले" / "When a "No" Comes With a Way Forward") is unchanged. `rebuild_blogs.sh` printed no "Note:" lines.

## Checklist

- Now met: the focus keyword is in the body text in both languages (the two check_seo errors) and within the first 100 words. Both languages have an early direct answer of about 50–55 words, and the first H2 is now a natural question.
- Already met and still met: every other item in the new section 12 except the one below. `check_seo.py` passes.
- Still unmet (1): "Each tag can be shared by at least 3 posts". The tag Sanatan Rashtra / सनातन राष्ट्र is used by this post only. Tags are outside what this fix may change; left for a later `/seo_blog` pass.
- Left alone on purpose: the post is still thin (about 350 words per language); expanding it from the source talk is the editor's call (report section 4, flag 2). The report's sections 1, 4, 5, 6 and 10 still describe the original texts; this fix may only edit sections 2, 3, 8, 11 and 12. Section 8 needed no change, since no title, meta description, keyword or slug changed.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | achhe-neta-ki-pehchan | achhe-neta-ki-pehchan (unchanged) |
| wordpress.en.slug | what-makes-a-good-leader | what-makes-a-good-leader (unchanged) |

No seo.json field changed. The focus keywords were already the searched wording and are now in the body, and the titles and meta descriptions already contain them, so focus keywords, secondary keywords, slugs, titles, meta descriptions, `links` and `also_read` stay as they were. Section 11 of the report still matches seo.json. Section 3 now marks the meta descriptions and slugs in seo.json as recommended (the titles were already marked), section 2 has a keyword note, and section 12 is the new checklist.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | achhe-neta-ki-pehchan | what-makes-a-good-leader |
| focus_keyword | अच्छे नेता की पहचान | what makes a good leader |
| title | अच्छे नेता की पहचान: जो मना करे, वही राह भी दिखाए | What Makes a Good Leader? Stop, Then Show the Way |
| meta_description | अच्छे नेता की पहचान क्या है? आचार्य उपेंद्र जी एक साधारण उदाहरण से समझाते हैं कि अच्छा राजा केवल मना नहीं करता, बेहतर विकल्प भी देता है। | What makes a good leader? Acharya Upendra Ji explains, with a simple parking example, that a good king never only forbids: he also offers an alternative. |
