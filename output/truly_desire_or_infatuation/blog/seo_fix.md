truly_desire_or_infatuation: SEO fix

Copies written: `truly_desire_or_infatuation_blog_seo.txt` (Hindi) and `truly_desire_or_infatuation_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro | (none) | आचार्य उपेंद्र जी के अनुसार काम का असली अर्थ केवल कामवासना नहीं, बल्कि कोई भी इच्छा है। उच्च स्तर की कामना दूसरे का भला चाहती है, जैसे आशीर्वाद देते समय सिर पर रखा हाथ या मित्र से हाथ मिलाना। स्पर्श के पीछे का हेतु ही तय करता है कि वह काम है या वासना। | The focus keyword "काम का असली अर्थ" was not in the body (`check_seo.py` failed) or the first 100 words, and the opening gave no direct answer. Built only from the blog (sections "काम की सच्ची परिभाषा", "चिकित्सक का उदाहरण" and the takeaways) |
| H2 3 | काम की सच्ची परिभाषा | काम का असली अर्थ क्या है? | The question readers search, with the focus keyword; the section answers it ("काम का अर्थ है कोई इच्छा...") |
| H2 5 (also_read heading) | कलयुग की सबसे बड़ी उलझन | प्रेम या वासना? कलयुग की सबसे बड़ी उलझन | A natural question (secondary keyword cluster "प्रेम और वासना में अंतर"); the section answers it ("वह प्रेम था ही नहीं, वह वासना थी"). seo.json `also_read.after.hi` updated to match |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro | (none) | Love vs lust: how do we tell them apart? According to Acharya Upendra Ji, kama does not mean only sensual craving; it means desire of any kind. Its higher form wishes for another's good, like a hand placed on the head in blessing or a handshake with a friend. The intention behind a touch decides whether it is kama or lust. | The focus keyword "love vs lust" was not in the body (`check_seo.py` failed) or the first 100 words, and the opening gave no direct answer. Built only from the blog (report section 5, worded to the takeaways' "kama or lust") |
| H2 3 | What Kama Really Means | What Is the True Meaning of Kama? | The question readers search (secondary keyword "true meaning of kama"); the section answers it |
| H2 5 (also_read heading) | The Great Confusion of Kali Yuga | Love or Lust? The Great Confusion of Kali Yuga | A natural question for "love vs lust" searchers; the section answers it ("It was lust"). seo.json `also_read.after.en` updated to match |

The headings keep their number and order. No teaching, example, verse, translation, reference or H1 was touched; the Hindi spelling fixes from the Sanskrit review (कलियुग, तत्त्व, निःस्वार्थ) are left to the editor, since "लक्ष्मी तत्व" is a link phrase. All five `links` phrases are still in the texts word for word, and the `also_read` headings match seo.json.

## Checklist

Now met:
- Focus keyword in the body text: both languages (both failed `check_seo.py` before).
- Focus keyword in the meta description: English (failed before).
- Focus keyword within the first 100 words: both languages, in the direct-answer paragraph.
- Direct answer early (report section 5): added in both languages.
- Question headings: two H2s per language are now natural questions.

Still unmet (2):
- Each tag can be shared by at least 3 posts: "Vasana" / "वासना" is used by 2 posts, "Kalki Avatar" / "कल्कि अवतार" by 1–2. A tag choice, not something the blog text can fix.
- No unsupported scriptural claims: the Kalki "kama avatar / prema avatar" passage and "प्रेम आया तो काम आएगा ही" are presented as scripture without a source (Sanskrit review issues 1–2, report flags 1–2). Content corrections for the editor, not SEO fixes.

`python3 tools/check_seo.py truly_desire_or_infatuation` passes.

## Report updates

- Section 2: keyword note added describing the `_seo` texts.
- Section 3: titles, meta descriptions and slugs in seo.json marked recommended; the English meta description replaced with the new one.
- Section 4: note that the direct answer and heading changes are done in the `_seo` texts.
- Section 7: the Also read note uses the new headings.
- Section 8: English BlogPosting description matches the new meta description; both alternativeHeadlines are now the full title in seo.json; keywords and slugs unchanged.
- Section 11: the JSON block equals seo.json.
- Section 12: the SEO checklist was missing from the report; added and marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | Is it love or attraction? Acharya Upendra Ji explains the true meaning of kama, the two levels of desire, and why the intention behind a touch matters. | Love vs lust: what is the difference? Acharya Upendra Ji explains the true meaning of kama, its two levels, and why the intention behind a touch matters. (153 characters) |
| also_read.after.hi | कलयुग की सबसे बड़ी उलझन | प्रेम या वासना? कलयुग की सबसे बड़ी उलझन |
| also_read.after.en | The Great Confusion of Kali Yuga | Love or Lust? The Great Confusion of Kali Yuga |
| wordpress.hi.focus_keyword, wordpress.en.focus_keyword | काम का असली अर्थ / love vs lust | unchanged (the `_seo` texts now use them) |
| wordpress.hi.slug, wordpress.en.slug | kaam-ka-asli-arth / love-vs-lust | unchanged |
| title.hi, title.en, wordpress.hi.meta_description | (as below) | unchanged (already contain the focus keyword) |
| links | (unchanged) | unchanged (no edit touched a link phrase) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | kaam-ka-asli-arth | love-vs-lust |
| focus_keyword | काम का असली अर्थ | love vs lust |
| title | काम का असली अर्थ: प्रेम या केवल आकर्षण? | आचार्य जी | Love vs Lust: The True Meaning of Kama | Acharya Ji |
| meta_description | जिसे हम प्रेम कहते हैं, क्या वह प्रेम है या केवल आकर्षण? आचार्य उपेंद्र जी बताते हैं काम का असली अर्थ, कामना के दो स्तर और स्पर्श के पीछे का हेतु। | Love vs lust: what is the difference? Acharya Upendra Ji explains the true meaning of kama, its two levels, and why the intention behind a touch matters. |
