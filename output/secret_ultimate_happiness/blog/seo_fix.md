secret_ultimate_happiness: SEO fix

Fixed texts: `secret_ultimate_happiness_blog_seo.txt` (Hindi) and `secret_ultimate_happiness_blog_seo_en.txt` (English). The original blog texts are unchanged. No teaching, example, verse, translation, reference, H1 or order of ideas was changed, and no new claim was added.

## Hindi changes

| Where | Before | After | Why |
|---|---|---|---|
| `##` heading 5 | वासना: असली बॉस | वासना क्या है, और वह असली बॉस क्यों है? | Phrases the heading as the question readers search ("वासना क्या है", a secondary keyword); the section answers it. |
| `##` heading 8 | सद्गुरु: जिसकी वासना कट चुकी है | सद्गुरु कौन है? जिसकी वासना कट चुकी है | Question heading for "सद्गुरु कौन है"; the section answers it and keeps the original wording. |

The focus keyword "कौन सा ज्ञान मुक्ति देता है" was already in the body, word for word, in the first 100 words (paragraph 2), so the opening was not changed.

## English changes

| Where | Before | After | Why |
|---|---|---|---|
| Opening, paragraph 2 | We only need to understand which kind of knowledge frees you and which kind keeps you stuck. | We only need to understand which knowledge leads to liberation and which kind keeps you stuck. | Puts the searched wording and focus keyword "which knowledge leads to liberation" in the first 100 words; same meaning (the blog already speaks of "the knowledge that liberates"). |
| `##` heading 5 | Vasana: The Real Boss | What Is Vasana, and Why Is It the Real Boss? | Question heading for "what is vasana", a secondary keyword; the section answers it. |
| `##` heading 8 | The Sadguru: One Whose Vasanas Have Been Severed | Who Is a Sadguru? One Whose Vasanas Have Been Severed | Question heading for "who is a Sadguru"; the section answers it and keeps the original wording. |

No direct answer paragraph was added in either language: paragraph 3 of the opening already answers the main question within the first 100 words ("The knowledge that liberates comes from a Guru who has realised the Self..." / "मुक्त करने वाला ज्ञान ... गुरु से आता है"), so a new paragraph would only repeat it.

Every `links` phrase and both `also_read` headings are still in the `_seo` texts word for word; the `also_read` heading ("आप शरीर, मन, बुद्धि नहीं हो" / "You Are Not the Body, Mind or Intellect") was not touched.

## Checklist

Now met:
- Focus keyword in the meta description (Hindi and English; `check_seo.py` failed on both before).
- Focus keyword in the body text (English).
- Focus keyword within the first 100 words (English).
- Focus keyword taken from wording the article uses (English, in the `_seo` text).

Still unmet (1):
- No unsupported scriptural claims: the blog attributes "knowledge does not stop sin, it adds birth upon birth" to Krishna and adds "you are only the witness" to the meaning of Gita 3.27 (report flags 1–2, Sanskrit review). This is a change to a teaching and a verse translation, which the SEO fix must not make; it is left to the editor.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | ज्ञान पाप से नहीं रोकता, फिर भी ज्ञानी को मोक्ष क्यों? आचार्य उपेंद्र जी समझाते हैं वासना, अहंकार और सद्गुरु का रहस्य, और कौन सा ज्ञान सच में मुक्त करता है। | ज्ञान पाप से नहीं रोकता, फिर भी ज्ञानी को मोक्ष क्यों? आचार्य उपेंद्र जी समझाते हैं वासना, अहंकार और सद्गुरु का रहस्य, और कौन सा ज्ञान मुक्ति देता है। |
| wordpress.en.meta_description | Why doesn't knowledge stop sin, yet the wise attain moksha? Acharya Upendra Ji explains vasana, ego and the Sadguru, and which knowledge truly frees you. | Knowledge doesn't stop sin, yet the wise attain moksha. Acharya Upendra Ji explains vasana, ego and the Sadguru, and which knowledge leads to liberation. |
| wordpress.hi.slug | kaun-sa-gyan-mukti-deta-hai | kaun-sa-gyan-mukti-deta-hai (unchanged) |
| wordpress.en.slug | which-knowledge-leads-to-liberation | which-knowledge-leads-to-liberation (unchanged) |

Both focus keywords stay as they were ("कौन सा ज्ञान मुक्ति देता है" / "which knowledge leads to liberation"): the searched wording is the focus keyword and the `_seo` texts now use it. They are unique across all talks. Titles, `secondary_keywords`, `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in these places:
- section 2: a keyword note;
- section 3: the meta descriptions, marked as recommended;
- section 8: both schema descriptions;
- section 11;
- section 12, which was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | kaun-sa-gyan-mukti-deta-hai | which-knowledge-leads-to-liberation |
| focus_keyword | कौन सा ज्ञान मुक्ति देता है | which knowledge leads to liberation |
| title | कौन सा ज्ञान मुक्ति देता है? परम आनंद का रहस्य | Which Knowledge Leads to Liberation? The Secret of Bliss |
| meta_description | ज्ञान पाप से नहीं रोकता, फिर भी ज्ञानी को मोक्ष क्यों? आचार्य उपेंद्र जी समझाते हैं वासना, अहंकार और सद्गुरु का रहस्य, और कौन सा ज्ञान मुक्ति देता है। | Knowledge doesn't stop sin, yet the wise attain moksha. Acharya Upendra Ji explains vasana, ego and the Sadguru, and which knowledge leads to liberation. |
