what_is_a_guru: SEO fix

Copies written: `what_is_a_guru_blog_seo.txt` (Hindi) and `what_is_a_guru_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (1 change)

| Where | Before | After | Why |
|---|---|---|---|
| H2 1 | एक प्रश्न जो सबसे पहले आता है | गुरु क्या है: व्यक्ति या सत्य का द्वार? | The question readers search, as recommended in report section 4; the section asks exactly this question ("क्या गुरु केवल एक व्यक्ति हैं, या स्वयं परम सत्य का द्वार?") |

## English (1 change)

| Where | Before | After | Why |
|---|---|---|---|
| H2 1 | The First Question That Arises | What Is a Guru: a Person or the Doorway to Truth? | The question readers search, as recommended in report section 4; the section asks exactly this question ("Is the Guru just a person, or the doorway to the ultimate truth itself?") |

The headings keep their number and order. No teaching, example, verse or H1 was touched. All five `links` phrases and the `also_read` headings ("आज हम किसकी शरण में जाएं?" / "In Whom Should We Take Refuge Today?") are still in the texts word for word.

## Checklist

All section 12 items were already met in the original texts, and stay met. The focus keyword ("गुरु क्या है" / "What is a Guru") was already the first line of each body; it is now also in a question H2.

Still unmet: none. `python3 tools/check_seo.py what_is_a_guru` passes.

Not changed:
- **Direct answer.** The opening already gives the blog's answer ("without the Guru there is no knowledge, and without knowledge no liberation") right after the question. Section 5's snippet states that the Guru *is* the doorway to truth, which the talk leaves as a question, so adding it would settle something the talk does not; it stays with the editor.
- **Second H2** ("गुरु गीता: गुरु तत्व का रहस्य" / "The Guru Gita: The Secret of the Guru Principle"): adding "स्कंद पुराण की" / "from the Skanda Purana" is optional in section 4 and touches authenticity flag 4, so it was left as is.
- **Authenticity flags 1–5** (मा शुचः meaning, "duties", IAST break, Guru Gita source, glosses) are content corrections, not SEO fixes, and concern verses or claims, so they stay with the editor.

## Report updates

- Section 2: the keyword note now says the focus keyword is also in the first H2 of the `_seo` texts.
- Section 3: the recommended titles, meta descriptions and slugs already match seo.json.
- Section 8: the `{{HI_URL}}` / `{{EN_URL}}` placeholders are now post URLs built from the slugs (`{{SITE_URL}}/hi/guru-kya-hai/`, `{{SITE_URL}}/en/what-is-a-guru/`); headline, description and keywords already matched.
- Sections 11 and 12: already match seo.json and the `_seo` texts; nothing changed.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.focus_keyword | गुरु क्या है | unchanged (no searched-wording mismatch) |
| wordpress.en.focus_keyword | what is a Guru | unchanged |
| wordpress.hi.slug | guru-kya-hai | unchanged |
| wordpress.en.slug | what-is-a-guru | unchanged |
| title, meta_description | (both languages) | unchanged (they still contain the focus keyword) |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | guru-kya-hai | what-is-a-guru |
| focus_keyword | गुरु क्या है | what is a Guru |
| title | गुरु क्या है? स्कंद पुराण की गुरु गीता का रहस्य | What Is a Guru? The Guru Gita and India as Vishwaguru |
| meta_description | गुरु क्या है: एक व्यक्ति या परम सत्य का द्वार? स्कंद पुराण की गुरु गीता पर आचार्य उपेंद्र जी की टीका गुरु, कृपा और शरण का रहस्य सरल भाषा में खोलती है। | What is a Guru: a person, or the doorway to truth? Acharya Ji's Guru Gita commentary explains the Guru, grace and refuge before India is Vishwaguru. |
