stop_asking_god_fix_your_life: SEO fix

`check_seo.py` failed before the fix. Neither body contained its focus keyword ("भगवान से क्या माँगें" / "what to ask God in prayer"), and the English meta description did not contain the English keyword. The bodies only had "प्रार्थना में क्या माँगें?" / "What Should You Ask for in Prayer?". The opening said asking God is not wrong, but it never gave a short, clear answer. Each language gets three changes:
- a short direct answer, built only from what the blog already says, that brings in the focus keyword within the first 100 words;
- one heading rephrased as the question readers search for;
- the Sanskrit review's correction to the unsourced "the scriptures say" sentence.

The focus keywords and slugs stay the same.

## Hindi (`stop_asking_god_fix_your_life_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| "क्या सच में बिना समस्या का जीवन संभव है?", new fourth paragraph (after "…की ओर कैसे जाऊँ।") | (none) | तो भगवान से क्या माँगें? यह मत माँगो कि जीवन में कोई समस्या न आए। भगवान से भक्ति, शक्ति, वैराग्य, आरोग्य, और समस्या हल करने की बुद्धि, शक्ति और प्रतिभा माँगो। परिश्रम तुम्हारा है, इसलिए उपलब्धि भी तुम्हारी होगी। | The focus keyword was missing from the body (a SureRank error). This is a direct answer of about 45 words that restates the blog's own first three sections, and it puts the keyword in the first 100 words. |
| "कसौटी एक ही है: आत्मबल", paragraph 1 | शास्त्र कहता है कि जिससे तुम्हारा **आत्मबल** … बढ़े, वह सब करो। | आचार्य जी कहते हैं कि जिससे तुम्हारा **आत्मबल** … बढ़े, वह सब करो। | Content trust: no source is named, and no known verse says this (Sanskrit review issue 1, report flag 1). The new wording is the review's own correction. |
| H2 before the rings section | ## पीला कपड़ा, अंगूठी और उत्प्रेरक का नियम | ## क्या अंगूठी और उपाय काम करते हैं? उत्प्रेरक का नियम | Turns the heading into the question readers search for (secondary keyword cluster "अंगूठी और उपाय"). The section answers it: remedies are catalysts and do not do the main work. |

## English (`stop_asking_god_fix_your_life_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| "Is a Life Without Problems Really Possible?", new fourth paragraph (after "…to **Narayan** (the Divine).") | (none) | So here is what to ask God in prayer: not a life without problems, but devotion, strength, detachment, good health, and the intelligence, strength and talent to solve the problems you face. The effort is yours, and that is what makes the achievement yours. | The focus keyword was missing from the body (a SureRank error). This is a direct answer of about 45 words that restates the blog's own first three sections, and it puts the keyword in the first 100 words. |
| "The One Test: Inner Strength", paragraph 1 | The scriptures say: do whatever increases your **atmabal** … | Acharya Ji says: do whatever increases your **atmabal** … | Content trust: this is the Sanskrit review's correction (issue 1, report flag 1). |
| H2 before the rings section | ## Yellow Clothes, Rings and the Law of the Catalyst | ## Do Rings and Remedies Work? The Law of the Catalyst | The question form suggested in report section 4. It matches the secondary keyword "do astrological remedies work", and the section answers it. |

Nothing else changed:
- no teaching, example, H1 or order of ideas, and no heading count or order;
- no verses (the blog quotes none);
- the H2 "जितनी ऊँचाई, उतने विघ्न", which `images.txt` uses to place inline.jpg, is untouched.

A grep finds all five `links` phrases and the `also_read` heading in both texts, word for word.

## Checklist

- Now met:
  - Focus keyword in the body text (both languages).
  - Focus keyword in the meta description (English).
  - Focus keyword within the first 100 words (both languages).
  - No unsupported scriptural claims: the atmabal sentence is now credited to Acharya Ji.
- Already met and still met: every other item except the one below. `check_seo.py` passes.
- Section 12 was missing from the report and has been added, marked against the fixed texts.
- Still unmet (1):
  - Each tag can be shared by at least 3 posts. "प्रार्थना" / "Prayer" is used by this post only so far. This fix does not change tags.
- Left alone on purpose:
  - "विघ्न कभी अचानक नहीं आते" / "Obstacles Never Arrive Suddenly" is not rephrased as a question, because the heading states the teaching itself.
  - Sanskrit review issues 2 to 4 (naming the Durga Saptashati, the Ganadhipati gloss, the sense of दशा) are not SEO items and are left for the editor. Issue 2 rewords the `links` phrase "दुर्गा की उपासना में पहला पाठ" / "the worship of Maa Durga always begins", so if the editor adopts it, the link phrase in seo.json must change too.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | Should you ask God to remove your problems? Acharya Upendra Ji explains what to ask for in prayer, why the effort is yours, and why remedies are catalysts. | What to ask God in prayer? Acharya Upendra Ji explains why to ask for the strength to solve problems, not remove them, and why remedies are only catalysts. (155) |
| wordpress.hi.slug | bhagwan-se-kya-mange | bhagwan-se-kya-mange (unchanged) |
| wordpress.en.slug | what-to-ask-god-in-prayer | what-to-ask-god-in-prayer (unchanged) |

Unchanged:
- in seo.json: the titles, focus keywords, secondary keywords, the Hindi meta description, `links`, `also_read`, `alt`, `caption`, `related`, category and tags;
- in the report: section 11 holds the same JSON. Section 2 has a new keyword note. Section 3 marks the recommended title, meta description and slug for each language. Section 8 has the new English description and names the suggested slugs. Section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | bhagwan-se-kya-mange | what-to-ask-god-in-prayer |
| focus keyword | भगवान से क्या माँगें | what to ask God in prayer |
| title | भगवान से क्या माँगें? समस्या हटाना नहीं, हल करने की शक्ति | What to Ask God in Prayer: Strength, Not a Problem-Free Life |
| meta description | भगवान से क्या माँगें? आचार्य उपेंद्र जी बताते हैं कि समस्या हटाने की नहीं, हल करने की शक्ति माँगो, और अंगूठी, रंग जैसे उपाय केवल उत्प्रेरक क्यों हैं। | What to ask God in prayer? Acharya Upendra Ji explains why to ask for the strength to solve problems, not remove them, and why remedies are only catalysts. |
