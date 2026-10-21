ganesh_chaturthi_pitru_paksha_navratri_diwali: SEO fix

The report stopped after section 11 and had no section 12 checklist; it was added in this fix. `check_seo.py` failed before the fix: neither body used the focus keyword ("त्योहारों का आध्यात्मिक क्रम" / "spiritual order of Hindu festivals"; the H1s say "त्योहारों का छिपा हुआ आध्यात्मिक क्रम" / "Hidden Spiritual Sequence of Festivals", and the H1 does not count), neither meta description contained it, and the English title and slug ("The Hidden Order of Festivals", `hidden-order-of-hindu-festivals`) lacked "spiritual". Each language gets three changes: a short direct answer as the opening paragraph, built only from what the blog already says (matching report section 5), and two `##` headings rephrased as the questions readers search, which those sections answer. seo.json gets a new English title and slug and new meta descriptions in both languages.

## Hindi (`ganesh_chaturthi_pitru_paksha_navratri_diwali_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| New opening paragraph (after the H1, before "## क्या छुट्टियाँ सिर्फ़ घूमने के लिए हैं?") | (none) | आचार्य जी के अनुसार गणेश चतुर्थी से दिवाली तक त्योहारों का आध्यात्मिक क्रम साधक की भीतरी यात्रा है। गणपति विवेक बुद्धि जगाते हैं, पितृपक्ष में पितरों की मुक्ति होती है, नवरात्रि तीनों गुणों पर अधिकार देती है, नरक चतुर्दशी अंतिम नकारात्मकता मिटाती है, और पाडवा पर साधक स्वर्णिम आभा बाँटने का अधिकारी बनता है। हर त्योहार नर से नारायण की ओर एक विराम है। | Direct answer to the main question ("why do the festivals come in this order"), built only from the blog's own sections and Key Takeaways (viveka, freeing the ancestors, mastery of the three gunas, the last negativity, the golden aura of Padwa, the pause from Nara to Narayana). Puts the focus keyword and the searched secondary wording "गणेश चतुर्थी से दिवाली तक" in the first 100 words. No `links` phrase is repeated, and the Rahu/Narakasura and apta claims (review flags) are left out. |
| H2 before "गणपति का अर्थ है **विवेक बुद्धि**…" | ## गणपति: विवेक बुद्धि (Discernment) का जागरण | ## गणपति पहले क्यों? विवेक बुद्धि (Discernment) का जागरण | Question readers ask (report section 6, FAQ 1); the section answers it ("जब यह जागती है, तभी आगे की यात्रा शुरू होती है"). Original wording kept after the question. |
| H2 before "**पितृ ऋण** (पूर्वजों के प्रति ऋण) से मुक्त हुआ व्यक्ति…" | ## पितृपक्ष और नवरात्रि: ऋण से मुक्ति, गुणों पर अधिकार | ## पितृपक्ष के बाद नवरात्रि क्यों आती है? | The question-style H2 suggested in report section 4; the section answers it (once free of pitru rina, one can master the three gunas). Number and order of headings unchanged; the also_read heading is untouched. |

## English (`ganesh_chaturthi_pitru_paksha_navratri_diwali_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| New opening paragraph (after the H1, before "## Are Holidays Only for Travel and Fun?") | (none) | According to Acharya Ji, the spiritual order of Hindu festivals, from Ganesh Chaturthi to Diwali, maps the seeker's inner journey. Ganapati awakens discernment, Pitru Paksha frees the ancestors, Navratri brings mastery of the three gunas, Naraka Chaturdashi removes the last negativity, and Padwa makes the seeker worthy of sharing the golden aura. Each festival is a pause from Nara towards Narayana, not a vacation. | Direct answer, built only from the blog's own sections and Key Takeaways. Puts the focus keyword and the searched secondary wording "Ganesh Chaturthi to Diwali" in the first 100 words. No `links` phrase is repeated; flagged claims are left out. |
| H2 before "Ganapati stands for **viveka**…" | ## Ganapati: Awakening Discernment | ## Why Does Ganapati Come First? Awakening Discernment | Question readers ask (FAQ 1); the section answers it ("The journey ahead begins only once this faculty awakens"). |
| H2 before "Once you are free of **pitru rina**…" | ## Pitru Paksha and Navratri: Freedom from Debt, Mastery of the Gunas | ## Why Does Navratri Follow Pitru Paksha? | The question-style H2 suggested in report section 4; the section answers it. Number and order of headings unchanged. |

No teaching, example, order of ideas, H1 or Markdown changed; the blog quotes no verses. All five `links` phrases and the `also_read` heading ("नरक चतुर्दशी: आख़िरी अंधेरा" / "Naraka Chaturdashi: The Last Darkness") appear once each in the fixed texts, confirmed by grep. The inline image's section (the firecracker heading) was not reworded. The rebuild gave no "Note:" lines.

## Checklist

- Now met: "In the SEO title" (English), "In the meta description" (both), "In the body text" (both), "In the URL slug (English keywords)", "Within the first 100 words (preferred)" (both), and "Focus keyword taken from wording the article already uses". `check_seo.py` now passes.
- Already met: every other item in section 12 (added to the report in this fix), except the one below.
- Still unmet (1): "No unsupported scriptural claims". The Sanskrit review's Major fixes (Rahu called Narakasura, apta leaves placed on Padwa, "scriptures describe crackers that burst within") change the teaching's claims, not SEO wording, so they are left for the editor to apply in the original blog (report section 10, flags 1–3). The Minor fixes (तुरीय, सण, गुरुदेव, Shri Vidya gloss, "leelas") are also left for the editor.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Ganesh Chaturthi to Diwali: The Hidden Order of Festivals | Spiritual Order of Hindu Festivals: Ganapati to Diwali |
| wordpress.en.slug | hidden-order-of-hindu-festivals | spiritual-order-of-hindu-festivals |
| wordpress.en.meta_description | Why does Ganapati come first, then Pitru Paksha, Navratri and Diwali? Acharya Upendra Ji sees each festival as a step from Nara to Narayana, not a holiday. | Why Ganapati, then Pitru Paksha, Navratri and Diwali? Acharya Upendra Ji explains the spiritual order of Hindu festivals, a journey from Nara to Narayana. |
| wordpress.hi.meta_description | पहले गणपति, फिर पितृपक्ष, नवरात्रि और दिवाली, यही क्रम क्यों? आचार्य उपेंद्र जी बताते हैं कि हर त्योहार छुट्टी नहीं, नर से नारायण की यात्रा का एक पड़ाव है। | पहले गणपति, फिर पितृपक्ष, नवरात्रि और दिवाली क्यों? आचार्य उपेंद्र जी बताते हैं त्योहारों का आध्यात्मिक क्रम: हर त्योहार नर से नारायण की यात्रा का पड़ाव है। |
| wordpress.hi.slug | tyoharon-ka-adhyatmik-kram | tyoharon-ka-adhyatmik-kram (unchanged) |
| wordpress.hi.focus_keyword | त्योहारों का आध्यात्मिक क्रम | त्योहारों का आध्यात्मिक क्रम (unchanged) |
| wordpress.en.focus_keyword | spiritual order of Hindu festivals | spiritual order of Hindu festivals (unchanged) |

The focus keywords stay: the searched wording "गणेश चतुर्थी से दिवाली तक" / "Ganesh Chaturthi to Diwali" is now in the body too, but it stays a secondary keyword because the sequence keyword is the talk's own thesis and avoids competing with the single-festival posts (report section 7). The Hindi title already contained its keyword and is unchanged. Secondary keywords, tags, `links` and `also_read` are unchanged. Meta descriptions are 156 (Hindi) and 154 (English) characters; the English title is 54. The report was updated to match: section 2 (keyword note), section 3 (new English title, both meta descriptions and slugs marked recommended), section 8 (English alternativeHeadline, both schema descriptions, the suggested English slug; headlines and keywords unchanged), section 11 (seo.json), and section 12 (added).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | tyoharon-ka-adhyatmik-kram | spiritual-order-of-hindu-festivals |
| focus_keyword | त्योहारों का आध्यात्मिक क्रम | spiritual order of Hindu festivals |
| title | गणेश चतुर्थी से दिवाली तक: त्योहारों का आध्यात्मिक क्रम | Spiritual Order of Hindu Festivals: Ganapati to Diwali |
| meta_description | पहले गणपति, फिर पितृपक्ष, नवरात्रि और दिवाली क्यों? आचार्य उपेंद्र जी बताते हैं त्योहारों का आध्यात्मिक क्रम: हर त्योहार नर से नारायण की यात्रा का पड़ाव है। | Why Ganapati, then Pitru Paksha, Navratri and Diwali? Acharya Upendra Ji explains the spiritual order of Hindu festivals, a journey from Nara to Narayana. |
