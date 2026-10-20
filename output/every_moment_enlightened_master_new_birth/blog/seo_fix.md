every_moment_enlightened_master_new_birth: SEO fix

`check_seo.py` failed before the fix: the focus keywords "गुरु सेवा का महत्व" and "importance of Guru seva" were in neither the blog bodies nor the meta descriptions (the bodies say only "सेवा" / "seva"). The opening also had no direct answer. Each language gets two text changes: a short direct answer after "…एक साधन देते हैं: **सेवा**" / "…one tool: **seva**", built only from what the blog already says (and the report's section 5), which puts the focus keyword in the body within the first 100 words; and the last H2 rephrased as the searched question (secondary keyword "गुरु पादुका पूजन का अर्थ" / "meaning of Guru Paduka puja"). The meta descriptions were rewritten to open with the focus keyword. Focus keywords, slugs and titles stay as they were.

## Hindi (`every_moment_enlightened_master_new_birth_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new fourth paragraph (after "इस परिवर्तन के लिए गुरु एक साधन देते हैं: **सेवा** (selfless service)।") | (none) | गुरु सेवा का महत्व यही है कि सफाई या सबके लिए भोजन बनाने जैसे छोटे कार्य "मैं-मेरा" की सीमा तोड़ते हैं और परिवार की परिभाषा बड़ी करते हैं। गुरु की वाणी संस्कार बनकर भीतर स्थायी हो जाती है, साधक क्रमशः तमस से रजस और रजस से सत्त्व की ओर बढ़ता है, और जीवन नया जन्म जैसा लगता है। | Direct answer (58 words) restating the blog's own sections and Key Takeaways; puts the focus keyword in the body, within the first 100 words. The guna sequence is given as the seeker's experience, with no Gita claim (report flag 1). |
| Last H2 before Key Takeaways | ## पादुका-पूजन का सच्चा अर्थ | ## गुरु पादुका पूजन का सच्चा अर्थ क्या है? | Question heading matching the secondary keyword "गुरु पादुका पूजन का अर्थ" (report section 4); the section answers it. Number and order of headings unchanged. |

## English (`every_moment_enlightened_master_new_birth_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new fourth paragraph (after "For this transformation, the Guru gives you one tool: **seva** (selfless service).") | (none) | The importance of Guru seva is that small tasks, such as cleaning or cooking for fellow seekers, break the habit of "me and mine" and widen your idea of family. The Guru's words settle in as lasting samskaras, the seeker moves step by step from tamas to rajas and on towards sattva, and life feels like a new birth. | Direct answer (59 words), built only from the blog's own points; puts the focus keyword in the body, within the first 100 words. No Gita claim (report flag 1). |
| Last H2 before Key Takeaways | ## What Worshipping the Paduka Really Means | ## What Does Guru Paduka Worship Really Mean? | Question heading matching the secondary keyword "meaning of Guru Paduka puja" (report section 4); the section answers it. Number and order of headings unchanged. |

No teaching, example, order of ideas, verse, translation, reference, H1 or Markdown changed. All five `links` phrases and the `also_read` heading ("वाणी जो संस्कार बन जाती है" / "Words That Become Samskaras", left unchanged for that reason, although section 4 suggested a question form) are still in both texts, confirmed by grep. The inline image is placed by section position; images.txt's Hindi heading "पादुका-पूजन का सच्चा अर्थ" is still in the original Hindi text.

## Checklist

The report had no section 12; one was added (from the standard checklist) with the fix.

- Now met: focus keyword in the body and in the meta description (both languages); focus keyword within the first 100 words; one question H2; a direct answer of 40–60 words early in the post. `check_seo.py` passes.
- Already met and still met: every other item except the one below.
- Still unmet (1): "No unsupported scriptural claims". The Sanskrit review's Major issue (Gita 14.10 introduced as "यही क्रम" / "exactly this sequence", a tamas → rajas → sattva ladder) and the uncited "गुरु गीता में भी यही कहा गया है" / "The Guru Gita says the same" remain in the body. Fixing them changes the blog's wording around a verse, which this SEO fix may not do; they are left for the editor to fix in the original blog (report section 10, flags 1–3).
- Left alone on purpose: the review's Minor issues (half-verse reference, missing "हे भारत!", सात्विक → सात्त्विक, the Hindi halahala gloss) are not SEO items. Report sections 1, 4, 5 and 10 are not edited.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | गुरु सेवा क्यों देते हैं? एक साधिका बताती हैं कि शिविर में सबके लिए भोजन बनाने, 'मैं-मेरा' छोड़ने और गुरु पादुका के मार्ग पर चलने से जीवन नया जन्म कैसे बना। | गुरु सेवा का महत्व क्या है? एक साधिका बताती हैं कि शिविर में सबके लिए भोजन बनाने, 'मैं-मेरा' छोड़ने और गुरु पादुका के मार्ग पर चलने से जीवन नया जन्म कैसे बना। |
| wordpress.en.meta_description | Why does the Guru give seva? A sadhika shares how cooking for fellow seekers and following the Guru's paduka made life in his presence a new birth. | What is the importance of Guru seva? A sadhika shares how cooking for fellow seekers and following the Guru's paduka made life in his presence a new birth. (155 characters) |

Slugs unchanged: `guru-seva-ka-mahatva` (Hindi) and `importance-of-guru-seva` (English). Focus keywords, secondary keywords, titles, `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2 (keyword note), 3 (meta descriptions and slugs marked as recommended) and 8 (schema descriptions, and the suggested URL slugs in the placeholder note) were updated, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | guru-seva-ka-mahatva | importance-of-guru-seva |
| focus_keyword | गुरु सेवा का महत्व | importance of Guru seva |
| title | गुरु सेवा का महत्व: सान्निध्य में हर क्षण नया जन्म | Importance of Guru Seva: Every Moment a New Birth |
| meta_description | गुरु सेवा का महत्व क्या है? एक साधिका बताती हैं कि शिविर में सबके लिए भोजन बनाने, 'मैं-मेरा' छोड़ने और गुरु पादुका के मार्ग पर चलने से जीवन नया जन्म कैसे बना। | What is the importance of Guru seva? A sadhika shares how cooking for fellow seekers and following the Guru's paduka made life in his presence a new birth. |
