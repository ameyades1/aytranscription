when_kalki_avatar_come: SEO fix

Copies written: `when_kalki_avatar_come_blog_seo.txt` (Hindi) and `when_kalki_avatar_come_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after paragraph 1 | (none) | कल्कि अवतार कब आएगा? गुरुजी के अनुसार गीता ४.७ से ४.९ में अवतार की परिभाषा है, पर किसी की प्रतीक्षा करने की बात नहीं लिखी। जो देश कार्य, गुरु कार्य से जुड़कर अपने गुरु को पहचान लेता है, वह भी कल्कि बन जाता है। और जब तक भीतर का कल्कि नहीं जागेगा, बाहर का कोई कल्कि नहीं आएगा। | The searched question "कल्कि अवतार कब आएगा" was only in the H1 (section 2's mismatch note); it is now in the first 100 words, and the opening gets a direct answer (58 words). Built only from the blog: the first takeaway (गीता ४.७ से ४.९, no waiting), "कल्कि बाहर नहीं, भीतर जागेगा" (देश कार्य, गुरु कार्य, recognising the Guru, becoming Kalki) and its last sentence (inner Kalki). |
| H2 2 | प्रतीक्षा की आदत | क्या हमें कल्कि की प्रतीक्षा करनी चाहिए? | The question readers ask, as suggested in report section 4; the section answers it ("ऐसा भगवद्गीता में कभी नहीं लिखा"). |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after paragraph 1 | (none) | When will the Kalki avatar come? According to Acharya Ji, the Gita defines an avatar in verses 4.7 to 4.9, but nowhere does it tell us to wait for anyone. Whoever joins the work for the nation and the Guru's mission and recognises their Guru becomes Kalki too. Until the Kalki within us awakens, no Kalki will come from outside. | The searched question "when will Kalki avatar come" was only in the H1 (section 2's mismatch note); it is now in the first 100 words, and the opening gets a direct answer (60 words). Built only from the blog: the first takeaway, "Kalki Will Awaken Within, Not Outside" (work for the nation and the Guru's mission, recognising the Guru) and its last sentence. |
| H2 2 | The Habit of Waiting | Should We Wait for Kalki? | The question readers ask, as suggested in report section 4; the section answers it ("the Bhagavad Gita never says any such thing"). |

The headings keep their number and order. No teaching, example, verse, translation, reference or H1 was touched, and no date or prophecy was added (authenticity flag 1). All five `links` phrases and the `also_read` headings ("कल्कि बाहर नहीं, भीतर जागेगा" / "Kalki Will Awaken Within, Not Outside") are still in the texts word for word. The image heading "हनुमान बनो, मावळे बनो" / "Be a Hanuman, Be a Mavala" is unchanged.

## Checklist

Now met:
- The searched wording is the focus keyword and is in the body, within the first 100 words (section 2's mismatch is resolved).
- A direct-answer paragraph (40–60 words) appears early in both languages (report section 5).
- One H2 per language is phrased as a reader's question (report section 4).

All other section 12 items were already met and stay met. Still unmet: none. `python3 tools/check_seo.py when_kalki_avatar_come` passes.

Not changed:
- **"मुक्ति की चार सीढ़ियां" / "The Four Steps to Liberation"**: adding "सालोक्य से सायुज्य तक" is optional in section 4; one question heading per language is enough, so it stays.
- **Authenticity flags 2–5** (Hanuman's answer in quotation marks, "sama, dama, danda", "आचार्य जी" vs "गुरुजी", Mughal rule and Baji Prabhu) are content corrections from the Sanskrit review, not SEO fixes, so they stay with the editor.

## Report updates

- Section 2: the keyword table and note now give "कल्कि अवतार कब आएगा" / "when will Kalki avatar come" as the focus keywords, with the earlier focus keywords as secondary.
- Section 3: the titles, meta descriptions and slugs in seo.json (unchanged) are marked as the recommended ones.
- Section 8: keywords reordered (focus keyword first); the post URL placeholders now use the slugs (`{{SITE_URL}}/hi/kalki-avatar-kab-aayega/`, `{{SITE_URL}}/en/when-will-kalki-avatar-come/`). Headline, alternativeHeadline and description already matched.
- Section 11: same JSON as seo.json.
- Section 12: the first-100-words mark notes that the `_seo` texts meet it through the direct-answer paragraph.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.focus_keyword | कल्कि अवतार | कल्कि अवतार कब आएगा |
| wordpress.hi.secondary_keywords | कल्कि अवतार कब आएगा, अवतार की परिभाषा, चार प्रकार की मुक्ति, kalki avatar kab aayega | कल्कि अवतार, अवतार की परिभाषा, चार प्रकार की मुक्ति, kalki avatar kab aayega |
| wordpress.en.focus_keyword | Kalki avatar | when will Kalki avatar come |
| wordpress.en.secondary_keywords | when will Kalki avatar come, what is an avatar in the Bhagavad Gita, four types of mukti, yada yada hi dharmasya meaning | Kalki avatar, what is an avatar in the Bhagavad Gita, four types of mukti, yada yada hi dharmasya meaning |
| wordpress.hi.slug | kalki-avatar-kab-aayega | unchanged (already built from the new focus keyword) |
| wordpress.en.slug | when-will-kalki-avatar-come | unchanged (already built from the new focus keyword) |
| title, meta_description | (both languages) | unchanged (they already contain the new focus keyword) |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | kalki-avatar-kab-aayega | when-will-kalki-avatar-come |
| focus_keyword | कल्कि अवतार कब आएगा | when will Kalki avatar come |
| title | कल्कि अवतार कब आएगा? गीता ४.७ से ४.९ का उत्तर | When Will Kalki Avatar Come? What Gita 4.7 to 4.9 Says |
| meta_description | कल्कि अवतार कब आएगा? ब्रह्मर्षि आचार्य उपेंद्र जी गीता ४.७ से ४.९ से समझाते हैं कि प्रतीक्षा क्यों व्यर्थ है और भीतर का कल्कि कैसे जागता है। | When will the Kalki avatar come? Acharya Upendra Ji explains Gita 4.7 to 4.9: why waiting is not the answer, and how the Kalki within you awakens. |
