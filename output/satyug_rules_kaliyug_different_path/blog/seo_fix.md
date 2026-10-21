satyug_rules_kaliyug_different_path: SEO fix

The check failed before the fix: neither focus keyword was in the blog body, and neither was in its title tag. The Hindi keyword "कलियुग में साधना का मार्ग" was also missing from the Hindi meta description. The English keyword "spiritual path in Kaliyug" was also missing from the English slug. The English body spells the age "Kaliyuga" throughout, which SureRank does not count as "Kaliyug". The opening raised the question but gave no direct answer (report section 5). The fix adds a short direct-answer paragraph after the first intro paragraph in each language. It is built only from what the blog already says: the personal liberation vs. expansion distinction, the Kularnava verse's four ages, the four paths and "ask the Guru", following section 5's snippet and the first Key Takeaway. This puts the focus keyword in the body and in the first 100 words. The fix also turns two H2s per language into the questions readers search for. It changes the English focus keyword to the body's spelling, "spiritual path in Kaliyuga", and rewrites both titles, both meta descriptions and both slugs so that each contains its focus keyword. The report had no section 12, so this fix added the checklist.

## Hindi (`satyug_rules_kaliyug_different_path_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the first intro paragraph ("…क्या वही आज भी उतना ही सफल होगा?"), new paragraph | (none) | संक्षेप में, कलियुग में साधना का मार्ग लक्ष्य पर निर्भर है। व्यक्तिगत मोक्ष किसी भी युग के मार्ग से संभव है, पर संसार में विस्तार के लिए कलियुग में आगम और तंत्र प्रभावी हैं: सत्ययुग में श्रुति, त्रेता में स्मृति, द्वापर में पुराण और कलियुग में आगम। चार मार्गों में से अपना मार्ग गुरु से पूछकर चुनिए। | Focus keyword in the body and the first 100 words (word 47). An early direct answer (57 words) built from "व्यक्तिगत मोक्ष बनाम संसार में विस्तार", "चार युग, चार ज्ञान", "मेरे लिए कौन सा मार्ग?" and the first two Key Takeaways. No Vama or Panchamakara wording (flags 1, 2) |
| H2 "चार मार्ग…" | ## चार मार्ग: दक्षिण, वाम, सिद्धांत, कौल | ## साधना के चार मार्ग कौन से हैं: दक्षिण, वाम, सिद्धांत, कौल? | The section answers this question (section 4, FAQ 3) |
| H2 "पंचमकार…" | ## पंचमकार: तंत्र के पाँच साधन | ## पंचमकार का अर्थ क्या है? तंत्र के पाँच साधन | The section answers it. Matches the secondary keyword "पंचमकार का अर्थ" (FAQ 4) |

## English (`satyug_rules_kaliyug_different_path_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the first intro paragraph ("…succeed just as well today?"), new paragraph | (none) | In short, the spiritual path in Kaliyuga depends on the goal. Personal liberation is possible on any age's path, but to expand in the world in Kaliyuga, the Agamas and tantra work best: Satyuga rested on the Shruti, Treta on the Smriti, Dvapara on the Puranas and Kaliyuga on the Agamas. To choose among the four paths, ask the Guru. | Focus keyword in the body and the first 100 words (word 52). An early direct answer (60 words) built from the same sections and Key Takeaways as the Hindi |
| H2 "Four Paths…" | ## Four Paths: Dakshina, Vama, Siddhanta, Kaula | ## What Are the Four Paths: Dakshina, Vama, Siddhanta and Kaula? | The section answers this question (section 4, FAQ 3) |
| H2 "Panchamakara…" | ## Panchamakara: The Five Means of Tantra | ## What Does Panchamakara Mean? The Five Means of Tantra | The section answers it. Matches the secondary keyword "Panchamakara meaning" (FAQ 4) |

The fix changed no teaching, example, order of ideas, verse or H1. The headings keep their number and order. The new paragraphs avoid the `links` phrases. All five phrases and the `also_read` heading ("महिलाओं को पहले उठना होगा" / "Women Must Rise First") are still in both texts, word for word. "भैरव: निर्भयता की शक्ति" / "Bhairava: The Power of Fearlessness", where `inline.jpg` sits, is untouched. The Sanskrit review's corrections were not applied. These are the Hindi Gita 3.26 heading (section 4), the Bhavishya Purana sentence, the Bhartrihari/Shankaracharya attributions and the सात्त्विक spelling. They change the talk's content beyond SEO, so they are left to the editor (section 10). If सात्विक → सात्त्विक is applied later, the link phrase "यह साधन सात्विक हाथों में होना चाहिए" must change with it (flag 10).

## Checklist

- Now met: in both languages, the focus keyword is in the SEO title, the body text and the first 100 words. It is in the Hindi meta description and the English slug. "Focus keyword taken from wording the article already uses" is met for the `_seo` texts. `check_seo.py` passes; it failed before. Both texts give a direct answer early, and two H2s per language are now questions.
- Already met and still met: every other item in section 12 except the one below (this fix added the section to the report).
- Still unmet (1): "No unsupported scriptural claims". The body keeps statements the Sanskrit review flags as unsourced: the Bhavishya Purana claim about other religions and the Shankaracharya statement (flags 3 and 5). Removing or rewording them would change the talk's content, so that is an editorial decision. No SEO copy uses them.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | सत्ययुग के नियम, कलियुग का मार्ग: आगम, तंत्र और भैरव शक्ति | कलियुग में साधना का मार्ग: आगम, तंत्र और भैरव शक्ति (51) |
| title.en | Satyug Rules, Kaliyug Path: Agama, Tantra and Bhairava | Spiritual Path in Kaliyuga: Agama, Tantra and Bhairava (54) |
| wordpress.hi.slug | satyug-ke-niyam-kaliyug-ka-marg | kaliyug-mein-sadhana-ka-marg |
| wordpress.en.slug | satyug-rules-kaliyug-path | spiritual-path-in-kaliyuga (26 characters) |
| wordpress.hi.focus_keyword | कलियुग में साधना का मार्ग | unchanged |
| wordpress.en.focus_keyword | spiritual path in Kaliyug | spiritual path in Kaliyuga |
| wordpress.hi.meta_description | कलियुग में कौन सा मार्ग काम करेगा? आचार्य उपेंद्र जी से जानिए आगम और तंत्र का अर्थ, दक्षिण, वाम, सिद्धांत और कौल मार्ग, पंचमकार का सात्विक अर्थ और भैरव शक्ति। | कलियुग में साधना का मार्ग कौन सा है? आचार्य उपेंद्र जी से जानिए आगम और तंत्र का अर्थ, दक्षिण, वाम, सिद्धांत और कौल मार्ग, पंचमकार का सात्विक अर्थ और भैरव शक्ति। (160) |
| wordpress.en.meta_description | Which spiritual path works in Kaliyug? Acharya Upendra Ji on Agama and tantra, the four paths of sadhana, the sattvic Panchamakara and Bhairava Shakti. | What is the spiritual path in Kaliyuga? Acharya Upendra Ji on Agama and tantra, the four paths of sadhana, the sattvic Panchamakara and Bhairava Shakti. (152) |

The English focus keyword targets the same query, now in the body's spelling. "Kaliyuga" is the spelling used throughout the English text, and putting "Kaliyug" in the opening alone would read as a typo. Search engines treat the two spellings alike. The old keyword was not added to `secondary_keywords`, because it differs only in spelling and the list already has four keywords. Both focus keywords are unique across all talks. `secondary_keywords`, `links`, `also_read`, alt text, captions, related posts, category and tags are unchanged. The report was updated in these places:
- section 2: the English focus keyword row and a keyword note;
- section 3: the new titles, meta descriptions and slugs marked as recommended, with the earlier titles kept as option 4;
- section 8: both alternativeHeadlines and descriptions, the English keywords and the suggested slugs;
- section 11;
- section 12, which was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | kaliyug-mein-sadhana-ka-marg | spiritual-path-in-kaliyuga |
| focus_keyword | कलियुग में साधना का मार्ग | spiritual path in Kaliyuga |
| title | कलियुग में साधना का मार्ग: आगम, तंत्र और भैरव शक्ति | Spiritual Path in Kaliyuga: Agama, Tantra and Bhairava |
| meta_description | कलियुग में साधना का मार्ग कौन सा है? आचार्य उपेंद्र जी से जानिए आगम और तंत्र का अर्थ, दक्षिण, वाम, सिद्धांत और कौल मार्ग, पंचमकार का सात्विक अर्थ और भैरव शक्ति। | What is the spiritual path in Kaliyuga? Acharya Upendra Ji on Agama and tantra, the four paths of sadhana, the sattvic Panchamakara and Bhairava Shakti. |
