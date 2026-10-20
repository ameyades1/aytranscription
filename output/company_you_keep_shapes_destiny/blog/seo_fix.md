company_you_keep_shapes_destiny: SEO fix

The check failed before the fix: the Hindi focus keyword "संगति का प्रभाव" was not in the body, and the English focus keyword "company you keep and spiritual growth" was in none of the title, meta description, body or slug. The opening asked why the peace from sadhana fades but left the answer for later paragraphs. Each language now answers that question at once, in the opening paragraph, built only from the blog's own sections (company shapes thoughts, thoughts shape conduct, sattvic people and the Guru keep sattva, rajasic company pulls it down), and uses the focus keyword there, within the first 100 words. One heading per language is now a reader's question. The Sanskrit review's Major issue 1 (authenticity flag 1) and Minor issue 6 (flag 6) were corrected with the review's own wording, for the "No unsupported scriptural claims" item.

## Hindi (`company_you_keep_shapes_destiny_blog_seo.txt`): 6 changes

| Where | Before | After | Why |
|---|---|---|---|
| "सात्विकता का सरल रहस्य", paragraph 1 | आचार्य जी इसका उत्तर बहुत सरलता से देते हैं। | आचार्य जी इसका उत्तर बहुत सरलता से देते हैं: यह संगति का प्रभाव है। जिन लोगों के बीच हम रहते हैं, उन्हीं से विचार बनते हैं, और जैसे विचार होते हैं, वैसा आचरण होता है। सतोगुणी लोगों और गुरु का संग सत्त्व को बनाए रखता है, जबकि राजसिक संगति धीरे-धीरे उसे नीचे ले आती है। | Focus keyword (absent from the body) in the first 100 words (report section 4); direct answer from report section 5, using only what the blog says. |
| H2 2 | ## जब आप अपने परिवार से आगे निकल जाते हैं | ## परिवार से आगे निकल जाएँ, तो क्या करें? | Heading as the question readers ask; the section answers it (meet them on their level, don't show off, lift them). Number and order of headings unchanged. |
| H2 7 | ## गणेश पुराण क्या कहता है? | ## गणेश पुराण का संदर्भ | Content trust: the question promised a quotation the section cannot give (report section 4, flag 1). |
| "गणेश पुराण…", paragraph | आचार्य जी गणेश पुराण का उल्लेख करते हैं। उसमें स्वयं भगवान गणेश कहते हैं कि अधिकतर रिश्तेदार अपने लाभ के लिए ही होते हैं। यह एक **तत्त्व** (मूल सत्य) के रूप में कहा गया है, जो हर परिवार पर लागू होता है। | आचार्य जी गणेश पुराण का उल्लेख करते हुए बताते हैं कि अधिकतर रिश्तेदार अपने लाभ के लिए ही होते हैं। वे इसे एक **तत्त्व** (मूल सत्य) के रूप में देखते हैं, जो हर परिवार पर लागू होता है। | Content trust: unverified words put in Lord Ganesha's mouth (review issue 1, Major). The review's correction. |
| H2 8 | ## अवतारों के घर में भी यही हुआ | ## अवतारों और महापुरुषों के घर में भी यही हुआ | Shivaji Maharaj is not an avatar (review issue 6, flag 6, report section 4); matches the section's own closing line. |
| मुख्य बातें, item 5 | - गणेश पुराण के अनुसार अधिकतर रिश्तेदार अपने लाभ के लिए होते हैं; | - आचार्य जी गणेश पुराण के संदर्भ से बताते हैं कि अधिकतर रिश्तेदार अपने लाभ के लिए होते हैं; | Same as review issue 1; the review's wording for Key Takeaways. |

## English (`company_you_keep_shapes_destiny_blog_seo_en.txt`): 6 changes

| Where | Before | After | Why |
|---|---|---|---|
| "The Simple Secret of Staying Sattvic", paragraph 1 | Acharya Ji answers this very simply. | Acharya Ji answers this very simply: the company you keep and spiritual growth go hand in hand. Your thoughts are shaped by the people you live among, and your conduct follows your thoughts. Time with sattvic people and with the Guru keeps your sattva strong, while rajasic company slowly pulls it down. | Focus keyword (absent from the body) in the first 100 words; direct answer from report section 5, using only what the blog says. |
| H2 2 | ## When You Outgrow Your Family | ## What Should You Do When You Outgrow Your Family? | Question heading (secondary keyword "outgrowing family spiritually"); the section answers it. |
| H2 7 | ## What Does the Ganesha Purana Say? | ## A Reference from the Ganesha Purana | Content trust (report section 4, flag 1). |
| "Ganesha Purana", paragraph | Acharya Ji refers to the Ganesha Purana, a scripture devoted to Lord Ganesha. In it, Lord Ganesha himself says that most relatives are there for their own gain. He states this as a **tattva** (fundamental truth), one that applies to every family. | Referring to the Ganesha Purana, a scripture devoted to Lord Ganesha, Acharya Ji explains that most relatives are there for their own gain. He sees this as a **tattva** (fundamental truth), one that applies to every family. | Content trust: review issue 1 (Major). The review's correction. |
| H2 8 | ## Even the Avatars Faced It at Home | ## Even Avatars and Great Souls Faced It at Home | Review issue 6, flag 6, report section 4. |
| Key Takeaways, item 5 | - The Ganesha Purana says most relatives are there for their own gain, | - Citing the Ganesha Purana, Acharya Ji explains that most relatives are there for their own gain, | Same as review issue 1; the review's wording. |

No teaching, example, H1 or order of ideas changed; the blog quotes no verses. The number and order of headings are the same, and the "It is the company you keep" headings that `images.txt` uses for inline.jpg are unchanged. All four `links` phrases and the `also_read` heading ("महापुरुष घर क्यों छोड़ देते हैं?" / "Why Do Great Souls Leave Home?") are still in the texts, each found by grep.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages), and in the English title, meta description and URL slug. `check_seo.py` failed on these before; it now passes.
  - Focus keyword within the first 100 words (both languages).
  - Focus keyword taken from wording the article uses: the `_seo` texts now contain it.
  - No unsupported scriptural claims: review issue 1 fixed with the review's wording.
  - A direct answer (40-60 words) early on; one question H2 per language.
- Section 12 was missing from the report; it has been added, with every item met.
- Still unmet: none.
- Left alone on purpose: review issues 2-5 (Kamsa as राक्षस/asura, the four spellings of sattva in Hindi, "rajas" missing in the English, the viveka gloss) and flag 5 (Soyarabai's words) are wording and consistency points, not SEO items; they are left for the editor to fix in the original blog. The "It is the company you keep" heading was not made a question, because `images.txt` places inline.jpg by it.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | The Company You Keep: How It Shapes Your Spiritual Growth | The Company You Keep and Spiritual Growth: Staying Sattvic (58) |
| wordpress.en.meta_description | Why does the peace from sadhana fade? Acharya Upendra Ji explains how the company you keep shapes your thoughts and sattva, and how to meet old ties. | Why does the peace from sadhana fade? Acharya Upendra Ji explains how the company you keep and spiritual growth are linked, and how to meet old ties. (149) |
| wordpress.en.slug | company-you-keep-spiritual-growth | company-you-keep-and-spiritual-growth |

The focus keywords (both kept: the body now uses them), secondary keywords, the Hindi title, meta description and slug (`sangati-ka-prabhav`), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2 (keyword note), 3 (recommended English title, meta and slug), 8 (English alternativeHeadline, description and suggested slug) and 12 (checklist, newly added) were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sangati-ka-prabhav | company-you-keep-and-spiritual-growth |
| focus_keyword | संगति का प्रभाव | company you keep and spiritual growth |
| title | संगति का प्रभाव: आपकी संगति ही आपका भविष्य गढ़ती है | The Company You Keep and Spiritual Growth: Staying Sattvic |
| meta_description | साधना से मिली शांति क्यों फीकी पड़ती है? आचार्य उपेंद्र जी बताते हैं कि संगति का प्रभाव विचार, आचरण और सतोगुण पर कैसे पड़ता है और पुराने रिश्ते कैसे निभाएँ। | Why does the peace from sadhana fade? Acharya Upendra Ji explains how the company you keep and spiritual growth are linked, and how to meet old ties. |
