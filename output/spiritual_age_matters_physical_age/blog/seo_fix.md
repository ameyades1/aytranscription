spiritual_age_matters_physical_age: SEO fix

Fixed texts: `spiritual_age_matters_physical_age_blog_seo.txt` (Hindi) and `spiritual_age_matters_physical_age_blog_seo_en.txt` (English). The originals, H1s, `links` phrases, the Also read heading, the inline image's heading ("सच्चा जिज्ञासु: वेदांत का विद्यार्थी" / "The True Seeker: A Student of Vedanta") and the images are unchanged; the number and order of `##` sections are unchanged. The blog quotes no verses.

The focus keywords ("आध्यात्मिक आयु", "spiritual age") were already the body's own wording and in the first 100 words of both originals, so the report found no searched-wording mismatch. The fix adds the early direct answer and one question heading per language (report sections 4 and 5).

## Hindi changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| After the second paragraph, before "## गणपति आए, और आपका मन कहां गया?" | (none) | आध्यात्मिक आयु शरीर से नहीं, समझ से नापी जाती है। जो केवल सजावट देखने मंदिर जाता है, वह पचानवे का होकर भी शून्य से छह वर्ष का है। कथा तक सीमित समझ, हाजिरी वाली भक्ति और भगवान से रूठना इसके आगे की अवस्थाएं हैं; सच्चा जिज्ञासु मूर्ति के पीछे का अर्थ खोजता है। | No direct answer early; this 53-word snippet answer (report section 5) is built only from the blog's own stages and Key Takeaways, and uses the focus keyword near the top. |
| H2 of the 15–18 stage | ## भगवान से रूठना: पंद्रह से अठारह वर्ष | ## भगवान से रूठना: क्या आप पंद्रह से अठारह वर्ष के हैं? | Report section 4: one stage heading phrased as the self-assessment question readers ask; same stage, same ages. |

## English changes (2)

| Where | Before | After | Why |
|---|---|---|---|
| After the second paragraph, before "## When Ganapati Arrives, Where Does Your Mind Go?" | (none) | Spiritual age is measured by understanding, not by the body. Someone who visits temples only to see the decorations is zero to six years old spiritually, even at ninety-five. Understanding that stops at stories, prayer as mere attendance and sulking at God are the next stages; the true seeker looks for the meaning behind the idol. | No direct answer early; this 56-word snippet answer (report section 5) is built only from the blog's own stages and Key Takeaways, and uses the focus keyword near the top. |
| H2 of the 15–18 stage | ## Sulking at God: Fifteen to Eighteen Years | ## Sulking at God: Are You Fifteen to Eighteen? | Report section 4: one stage heading phrased as the self-assessment question readers ask; same stage, same ages. |

## Checklist

Now met: an early direct answer in both languages (report section 5), a stage heading phrased as a question. The report had no section 12; it was added, with every item met (`tools/check_seo.py` passes against the `_seo` texts).

Still unmet: none.

Left for the editor (content, not SEO, so outside this fix): the Sanskrit review's issues 1 ("15 से 17 साल" / "fifteen to seventeen" in the body vs 15 to 18 in the heading and Key Takeaways), 2 ("गुरुजी" and "आचार्य जी" mixed in the Hindi) and 3 ("Bhagavat Saptah" spelling), and the "परफेक्ट वेदांत" guarantee (authenticity flag 3).

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | spiritual-age-vs-physical-age | unchanged |
| wordpress.hi.slug | aadhyatmik-aayu | unchanged |
| focus_keyword (hi / en) | आध्यात्मिक आयु / spiritual age | unchanged |
| title, meta descriptions, secondary_keywords, links, also_read | | unchanged |

No seo.json field needed changing: the focus keywords, titles and meta descriptions still match the fixed texts, and no edit touched a link phrase or the Also read heading.

Report updated: section 2 (wording check note), section 12 (checklist added). Sections 3, 8 and 11 already match seo.json and are unchanged.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | aadhyatmik-aayu | spiritual-age-vs-physical-age |
| focus keyword | आध्यात्मिक आयु | spiritual age |
| title | आध्यात्मिक आयु: आपकी असली उम्र कितनी है? | Spiritual Age vs Physical Age: How Old Are You Really? |
| meta description | आपकी आध्यात्मिक आयु कितनी है? आचार्य उपेंद्र जी बताते हैं कि मंदिर जाने, कथा सुनने और प्रार्थना के ढंग से यह कैसे दिखती है, और क्यों वे कहते हैं: गति बढ़ाओ। | What is your spiritual age? Acharya Upendra Ji shows how the way you visit temples, hear katha and pray reveals it, and why he says: move faster. |
