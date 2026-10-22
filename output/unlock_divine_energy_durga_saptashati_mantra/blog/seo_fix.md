unlock_divine_energy_durga_saptashati_mantra: SEO fix

The report had no section 12 checklist yet, and `check_seo.py` failed: the focus keywords "दुर्गा सप्तशती बीज मंत्र" / "Durga Saptashati beej mantra" are the searched wording (and the video title's), but neither blog body used them (the bodies say "दुर्गा सप्तशती" and "बीज मंत्र" only apart, English spells "bija", and the Durga Saptashati first appears in the fourth section), and neither meta description contained them. The opening asked "can sadhana come in a capsule?" without a short answer. Each language gets two changes: a short direct answer at the start of the first section, built only from what the blog already says (report section 5), and one H2 rephrased as the searched question. The focus keywords stay; both meta descriptions are rewritten to contain them.

## Hindi (`unlock_divine_energy_durga_saptashati_mantra_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Start of "क्या साधना भी एक कैप्सूल में आ सकती है?", new paragraph before "बीज मंत्र को समझने के लिए…" | (none) | हाँ। आचार्य जी के अनुसार बीज मंत्र ऐसा ही कैप्सूल है: लं, कं, चं जैसे छोटे अक्षर, जो ध्वनि की शक्ति से पूरा परिणाम देते हैं। गुरुदेव ने इसी आधार पर दुर्गा सप्तशती बीज मंत्र साधना रची, जिसके दस-बीस मिनट में छह घंटे के पाठ का फल मिलना चाहिए। | Direct answer (about 50 words) to the section's question, restating the blog's own points (capsule, लं कं चं, ध्वनि की शक्ति, गुरुदेव की रचना, दस-बीस मिनट). Puts the focus keyword at about word 31. The promise keeps "मिलना चाहिए" and is attributed to Acharya Ji (flag 9). |
| H2 of the bija mantra section | ## बीज मंत्र: बिंदु में छिपी शक्ति | ## बीज मंत्र क्या है? बिंदु में छिपी शक्ति | The searched question "बीज मंत्र क्या है" as a heading (report section 4); the section answers it. Number and order of headings unchanged; images.txt still matches the original heading, so inline.jpg is placed by position. |

## English (`unlock_divine_energy_durga_saptashati_mantra_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Start of "Can Spiritual Practice Come in a Capsule?", new paragraph before "To understand a **bija mantra**…" | (none) | Yes. According to Acharya Ji, a bija mantra is just such a capsule: short syllables like lam, kam and cham that give the full result through the power of sound. On this basis Gurudev composed the Durga Saptashati beej mantra sadhana, in which ten or twenty minutes of practice should yield the fruit of a six-hour recitation. | Direct answer (about 57 words), built only from the blog. Puts the focus keyword, in its searched "beej" spelling, at about word 36. Keeps "should" and the attribution (flag 9). |
| H2 of the bija mantra section | ## Bija Mantras: The Power Hidden in a Dot | ## What Is a Bija Mantra? The Power Hidden in a Dot | The searched question "what is a bija mantra" as a heading; the section answers it. Number and order unchanged. |

No teaching, example, verse, translation, H1 or order of ideas changed, and Markdown is kept. All four `links` phrases and the `also_read` heading ("कलियुग का समाधान: तंत्रोक्त बीज मंत्रात्मक साधना" / "The Answer for Kali Yuga: A Tantric Practice of Seed Mantras") are still in both texts once each, confirmed by grep. The new paragraphs say "ध्वनि की शक्ति से पूरा परिणाम" / "through the power of sound", not the link phrases, so the links still land in the bija mantra section.

## Checklist

- Now met: focus keyword in the meta description (both), in the body text (both), within the first 100 words (both); focus keyword taken from wording the article uses. `check_seo.py` passes.
- Added: the report's section 12, which was missing.
- Still unmet (1): "No unsupported scriptural claims". The Sanskrit review's Critical issue 1 (Arjuna recited the Durga Stotra, not the Saptashati) and Major issue 2 (Shri Rama and the Saptashati) are still in the body. They are corrections to the teaching's wording for the editor to make in the original blog, not SEO edits; no title, meta, snippet or new paragraph uses them (flags 1 and 2).
- Left alone on purpose: the "अर्जुन और श्रीराम…" heading change (section 4, an editorial decision tied to the review), the courses-page sentence (an addition, not an SEO fix), and review issues 3–8 (Minor, for the editor).

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | बीज मंत्र क्या है और उसे कैप्सूल क्यों कहा गया? आचार्य उपेंद्र जी बताते हैं कि रोज़ दोहराया विचार मंत्र कैसे बनता है, और दुर्गा सप्तशती की बीज साधना क्या है। | दुर्गा सप्तशती बीज मंत्र साधना क्या है, और बीज मंत्र को कैप्सूल क्यों कहा गया? आचार्य उपेंद्र जी बताते हैं कि रोज़ दोहराया विचार मंत्र कैसे बन जाता है। (151) |
| wordpress.en.meta_description | What is a bija mantra, and why does Acharya Upendra Ji call it a capsule? On the Durga Saptashati, the mantra you repeat daily and a short tantric sadhana. | What is the Durga Saptashati beej mantra sadhana? Acharya Upendra Ji explains why a bija mantra is a capsule, and the mantra you repeat every day. (146) |
| wordpress.hi.slug | durga-saptashati-beej-mantra | durga-saptashati-beej-mantra (unchanged) |
| wordpress.en.slug | durga-saptashati-beej-mantra-sadhana | durga-saptashati-beej-mantra-sadhana (unchanged; 36 characters, contains the keyword) |

Focus keywords, secondary keywords, titles (both already contain the keyword), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2, 3 and 8 were updated to match, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | durga-saptashati-beej-mantra | durga-saptashati-beej-mantra-sadhana |
| focus_keyword | दुर्गा सप्तशती बीज मंत्र | Durga Saptashati beej mantra |
| title | दुर्गा सप्तशती बीज मंत्र: कैप्सूल जैसी साधना | Durga Saptashati Beej Mantra: Sadhana in a Capsule |
| meta_description | दुर्गा सप्तशती बीज मंत्र साधना क्या है, और बीज मंत्र को कैप्सूल क्यों कहा गया? आचार्य उपेंद्र जी बताते हैं कि रोज़ दोहराया विचार मंत्र कैसे बन जाता है। | What is the Durga Saptashati beej mantra sadhana? Acharya Upendra Ji explains why a bija mantra is a capsule, and the mantra you repeat every day. |
