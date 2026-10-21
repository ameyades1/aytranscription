spiritual_power_women_kali_yug: SEO fix

The SEO check failed before this fix: neither focus keyword ("महिला नेतृत्व और वाणी की शक्ति" / "power of speech for women leaders") appeared in the body or the meta description, and the English slug lacked "for". The original texts only said "वाणी की शक्ति" / "the power of speech". The fix adds a short direct-answer paragraph after the opening in each language that uses the focus keyword once, built only from what the blog already says (section 5 of the report), turns two `##` headings into the questions the sections answer (section 4's suggestions), and updates the meta descriptions and English slug.

## Hindi (`spiritual_power_women_kali_yug_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the opening (new paragraph, before the first H2) | (none) | महिला नेतृत्व और वाणी की शक्ति का क्या संबंध है? आचार्य जी के अनुसार नेतृत्व करने वाली स्त्री के लिए पहला गुण वाक् है, अर्थात् सशक्त वाणी। गीता १०.३४ में श्रीकृष्ण कहते हैं कि स्त्रियों में वे कीर्ति, श्री, वाक्, स्मृति, मेधा, धृति और क्षमा हैं। जिसके भीतर वाक् है, उसके भीतर अग्नि है, और उसी वाक् से महाकाली आती हैं। पर वाणी केवल द्वार खोलती है; टिकाता काम ही है। | Focus keyword in the body and in the first 100 words; a direct answer (about 60 words) built only from the blog's own sentences (opening, Gita 10.34 section, "वाक् वास्तव में क्या है?", fire-of-speech section, first section's closing) |
| Fourth H2 | ## स्त्री में सबसे अधिक कौन है: सरस्वती | ## स्त्री में सबसे अधिक कौन सी शक्ति है? | Question readers ask, answered by the section (Saraswati); section 4's suggestion |
| Seventh H2 | ## वाणी की अग्नि और महाकाली | ## वाणी से महाकाली कैसे जागती हैं? | Question form for snippets; the section answers it, with "नेता के पास जो वाक् होती है, उसी से महाकाली आती है" earlier; section 4's suggestion |

## English (`spiritual_power_women_kali_yug_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the opening (new paragraph, before the first H2) | (none) | Why is the power of speech for women leaders so important? According to Acharya Ji, the first quality a woman who leads needs is vak, a strong voice. In Bhagavad Gita 10.34, Shri Krishna says that among women he is fame, prosperity, speech, memory, intelligence, steadfastness and forgiveness. Whoever has vak has fire within, and that vak brings Mahakali forth. Yet speech only opens the door; work is what keeps you there. | Focus keyword in the body and in the first 100 words; a direct answer (about 65 words) built only from the blog's own sentences |
| Fourth H2 | ## Saraswati: The Strongest Presence in a Woman | ## Which Power Is Strongest in a Woman? | Question readers ask, answered by the section (Saraswati); section 4's suggestion |
| Seventh H2 | ## The Fire of Speech and Mahakali | ## How Does Speech Bring Forth Mahakali? | Question form for snippets; worded to avoid the link phrase "awaken Mahakali", which must stay linked in the punishment section |

No teaching, example, verse, translation, reference or H1 was changed, and the number and order of `##` sections is the same, so the inline image and the "Also read" box keep their places. All five `links` phrases and the `also_read` heading ("अति रौद्र, अति सौम्य: स्त्री का स्वरूप" / "Fierce and Gentle: The Nature of a Woman") are still in both texts, once each. The direct answers leave out the punishment teaching (authenticity flag 6) and the Brahma–Saraswati story (flag 1). The Sanskrit review's issues (`tools/review/spiritual_power_women_kali_yug.md`) are content corrections for the editor, not SEO, and were not applied here.

## Checklist

- Now met: the focus keyword is in the body, the meta description and within the first 100 words in both languages, and in the English slug. There is a direct answer early on, and two sections have question headings. `tools/check_seo.py` now passes (it failed with five errors before).
- The report had no section 12; it was added from `tools/prompts/seo_checklist.md` and marked for the `_seo` texts.
- Still unmet: none.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | power-of-speech-women-leaders | power-of-speech-for-women-leaders |
| wordpress.hi.meta_description | नेतृत्व के लिए स्त्री को वाक् अर्थात् वाणी की शक्ति क्यों चाहिए? आचार्य जी गीता १०.३४, सरस्वती का सत्त्वगुण और भीतर सोई महाकाली को जगाने का अर्थ समझाते हैं। | महिला नेतृत्व और वाणी की शक्ति का क्या संबंध है? आचार्य जी गीता १०.३४, सरस्वती का सत्त्वगुण और वाक् से भीतर सोई महाकाली के जागने का अर्थ समझाते हैं। (148) |
| wordpress.en.meta_description | Why must a woman who leads master vak, the power of speech? Acharya Ji explains Gita 10.34, Saraswati's sattva and how speech awakens the Mahakali within. | Why is the power of speech for women leaders so vital? Acharya Ji explains Gita 10.34, Saraswati's sattva and how speech awakens the Mahakali within. (149) |

The focus keywords were already the searched wording, so they are unchanged; the Hindi slug (`mahila-netritva-vani-ki-shakti`) is unchanged. Titles, secondary keywords, `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report's sections 2, 3, 8, 11 and 12 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | mahila-netritva-vani-ki-shakti | power-of-speech-for-women-leaders |
| focus_keyword | महिला नेतृत्व और वाणी की शक्ति | power of speech for women leaders |
| title | महिला नेतृत्व और वाणी की शक्ति: स्त्री में सोई महाकाली | Power of Speech for Women Leaders: The Mahakali Within |
| meta_description | महिला नेतृत्व और वाणी की शक्ति का क्या संबंध है? आचार्य जी गीता १०.३४, सरस्वती का सत्त्वगुण और वाक् से भीतर सोई महाकाली के जागने का अर्थ समझाते हैं। | Why is the power of speech for women leaders so vital? Acharya Ji explains Gita 10.34, Saraswati's sattva and how speech awakens the Mahakali within. |
