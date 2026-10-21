know_your_god_transformative_path: SEO fix

`check_seo.py` failed on the original texts. Neither focus keyword was in the blog body. The Hindi only says "भगवान को **जानना** होता है, केवल **मानना** नहीं" and the English only "you must **know** God, not merely **believe** in Him". The searched "भगवान को जानना या मानना" / "knowing God vs believing in God" never appeared. The English keyword was also missing from the title, the meta description and the slug, and the Hindi keyword from the meta description. Each language gets two text changes. First, a short direct answer after the intro, built only from what the blog already says (report section 5), which puts the focus keyword in the first 100 words. Second, the Ganesha Gita heading is reworded as the question readers search for (report section 4). seo.json gets new slugs (both languages), a new English title and new meta descriptions (both languages). The report had no section 12 checklist, so this fix added it.

## Hindi (`know_your_god_transformative_path_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…यही प्रश्न उठाते हैं।") | (none) | भगवान को जानना या मानना? शास्त्र कहते हैं: भगवान को जानना होता है, केवल मानना नहीं। बिना जाने किसी रूप से "प्रेम" करना अनजान चित्र से विवाह करने जैसा है। भक्ति की पहली सीढ़ी प्रेम है, और सच्चा प्रेम जानने की इच्छा जगाता है। गणेश गीता के अनुसार शिव, विष्णु, शक्ति, सूर्य और गणेश में अभेद देखना ही यथार्थ योग है। | The focus keyword "भगवान को जानना या मानना" was nowhere in the body (SureRank error), and the opening gave no direct answer. This direct answer (61 words) puts the keyword at word 63 of the body. It only restates the "जानना, मानना नहीं" section ("भगवान को जानना होता है, केवल मानना नहीं"), the second Key Takeaway (the stranger's photograph), the bhakti section ("भक्ति की पहली सीढ़ी प्रेम है", the wish to know) and Ganesha Gita 1.21 as the blog explains it. It repeats no `links` phrase and adds no scripture or claim (no Vyasa line, no verse numbers). |
| `##` heading of the Ganesha Gita section | ## गणेश गीता का यथार्थ योग | ## क्या शिव और विष्णु में भेद है? गणेश गीता का यथार्थ योग | Report section 4: the top question query, which the section's verses answer (1.19, 1.21). It carries the secondary keyword "शिव और विष्णु में भेद" and keeps the old heading's words. Rewording the heading instead of adding the suggested H3 keeps the number of sections. Not a `links`, `also_read` or image heading. |

## English (`know_your_god_transformative_path_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…a simple example that stings.") | (none) | Knowing God vs believing in God? The scriptures say God is to be known, not merely believed in. Loving a form without knowing it is like marrying a stranger's photograph. Bhakti begins with love, and real love awakens the wish to know Him. The Ganesha Gita calls seeing no difference between Shiva, Vishnu, Shakti, the Sun and Ganesha true yoga. | The focus keyword "knowing God vs believing in God" was nowhere in the body (SureRank error), and the opening gave no direct answer. This direct answer (60 words) puts the keyword at word 59 of the body. It only restates the "Know Him, Don't Just Accept Him" section, the second Key Takeaway, the bhakti section ("The first step of bhakti is love", "the wish to know Him") and Ganesha Gita 1.21 as the blog translates it. It repeats no `links` phrase and adds no scripture or claim. |
| `##` heading of the Ganesha Gita section | ## The True Yoga of the Ganesha Gita | ## Are Shiva and Vishnu the Same? The True Yoga of the Ganesha Gita | Report section 4's suggested question, which the verses answer. It carries the secondary keyword "are Shiva and Vishnu the same" and keeps the old heading. Per flag 7, the section answers it only from the Ganesha Gita verses, as before. Not a `links`, `also_read` or image heading. |

No teaching, example, verse, translation, reference, H1, gloss or order of ideas changed, and the Markdown is kept. The number and order of `##` headings are the same. grep confirms that all five `links` phrases and the `also_read` heading ("जानना, मानना नहीं" / "Know Him, Don't Just Accept Him") are still in both texts, once each. The inline image's Hindi heading ("एक अनजान चित्र से प्रेम?", from images.txt) is unchanged.

## Checklist

- Now met (both languages): the focus keyword is in the body text and within the first 100 words. It is also in the English title, both meta descriptions and the English slug. The opening has a direct answer, and no searched-wording mismatch is left. `check_seo.py` passes.
- Added: section 12, the SEO checklist, which was missing from the report.
- Still unmet (1): "No unsupported scriptural claims". The blog still introduces "साधकानां हितार्थाय ब्रह्मणो रूपकल्पना" as Maharshi Vedavyasa's, and quotes the line in its popular form rather than the Upanishad's "उपासकानां कार्यार्थं" (review issues 1 and 2, Major; flags 1 and 2). Changing a scripture attribution or a verse goes beyond an SEO edit, so this is left for the editor to correct in the original blog with the review's wording. The new direct answers and seo.json do not mention the line.
- Left alone on purpose:
  - Review issues 3 (the Ganesha Gita gloss only in English), 4 (IAST "ṁ") and 5 (the "God takes form" takeaway) are editorial or touch a verse, so they are left for the editor.
  - Report section 4's suggested heading "Knowing God or Believing in God: What Do the Scriptures Say?" was not used. That heading anchors the Also read box, and the keyword is already in the direct answer.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Know God, Don't Just Believe: The Ganesha Gita's Yoga | Knowing God vs Believing in God: The Ganesha Gita's Yoga |
| wordpress.hi.slug | bhagwan-ko-jano-sirf-mano-nahi | bhagwan-ko-janna-ya-manna |
| wordpress.hi.meta_description | क्या आप उस भगवान को जानते हैं जिसकी रोज़ पूजा करते हैं? आचार्य उपेंद्र जी बताते हैं कि भक्ति जानने से शुरू होती है, और गणेश गीता का अभेद योग क्या है। | भगवान को जानना या मानना? आचार्य उपेंद्र जी बताते हैं कि शास्त्र भगवान को जानने की बात कहते हैं, भक्ति प्रेम से शुरू होती है, और गणेश गीता का अभेद योग क्या है। (158 characters) |
| wordpress.en.slug | know-god-dont-just-believe | knowing-god-vs-believing-in-god |
| wordpress.en.meta_description | Do you really know the God you worship? Acharya Upendra Ji explains why bhakti begins with knowing, and the Ganesha Gita's yoga of seeing no difference. | Knowing God vs believing in God: Acharya Upendra Ji explains why the scriptures ask us to know God, and the Ganesha Gita's yoga of seeing no difference. (152 characters) |

Both slugs are unique across all talks. No other field changed: the focus keywords (now in the fixed bodies), secondary keywords, title.hi (it already contains its keyword), `links`, `also_read`, `alt`, `caption`, `related`, category and tags. The report's section 11 holds the same JSON. Section 2 has a keyword note. Section 3 marks the seo.json title, meta descriptions and slugs as recommended. Section 4 notes the applied edits. Section 8 has the new alternativeHeadline (English), descriptions and slugs. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bhagwan-ko-janna-ya-manna | knowing-god-vs-believing-in-god |
| focus_keyword | भगवान को जानना या मानना | knowing God vs believing in God |
| title | भगवान को जानना या मानना? गणेश गीता का यथार्थ योग | Knowing God vs Believing in God: The Ganesha Gita's Yoga |
| meta_description | भगवान को जानना या मानना? आचार्य उपेंद्र जी बताते हैं कि शास्त्र भगवान को जानने की बात कहते हैं, भक्ति प्रेम से शुरू होती है, और गणेश गीता का अभेद योग क्या है। | Knowing God vs believing in God: Acharya Upendra Ji explains why the scriptures ask us to know God, and the Ganesha Gita's yoga of seeing no difference. |
