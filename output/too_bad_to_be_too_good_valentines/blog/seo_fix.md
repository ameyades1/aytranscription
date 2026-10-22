too_bad_to_be_too_good_valentines: SEO fix

Copies written: `too_bad_to_be_too_good_valentines_blog_seo.txt` (Hindi) and `too_bad_to_be_too_good_valentines_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro | (none) | क्या ज़रूरत से ज़्यादा अच्छा होना गलत है? आचार्य उपेंद्र जी कहते हैं कि बहुत अच्छा होना भी बुरा है। जो बिना सोचे कहीं भी अपना दिल, धन और प्राण लगा देता है, उसे एक बार चोट खानी ही पड़ती है। केवल हृदय से चलना अंधभक्ति है; प्रेम के साथ विवेक भी चाहिए। | The focus keyword "ज़रूरत से ज़्यादा अच्छा होना" was only in the H1, not in the body or the first 100 words, and the opening gave no direct answer. The paragraph (report section 5) uses only what the blog says (sections 2–4) |
| H2 4 | केवल हृदय, बिना विवेक: अंधभक्ति का मार्ग | क्या बिना विवेक का प्रेम अंधभक्ति है? | A question readers search, with the secondary keyword "बिना विवेक का प्रेम"; the section answers it ("यही अंधभक्ति की दशा है: भावना तो है, पर विवेक नहीं") |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro | (none) | Is being too good a bad thing? Acharya Upendra Ji says it is too bad to be too good. If you give your heart, money and life to anyone without thought, you are bound to get hurt at least once. Led by the heart alone, love becomes blind devotion; it needs viveka, discernment, walking alongside it. | The focus keyword "is being too good a bad thing" was nowhere in the body (the H1 says "Can being too good also be a mistake?"), and the opening gave no direct answer. The paragraph (report section 5) uses only what the blog says |
| H2 4 | A Heart Without Discernment: The Road to Blind Devotion | Is Love Without Discernment Blind Devotion? | A question readers search, with the secondary keyword "love without discernment"; the section answers it ("This is the state of andhabhakti (blind devotion): the feeling is there, but viveka (discernment) is missing") |

The headings keep their number and order; the inline image and the Also read box are placed by section position. No teaching, example, story or H1 was touched (the blog quotes no verses). All five `links` phrases and the `also_read` headings ("यह कथा लक्ष्मी की नहीं, आपके हृदय की है" / "This Is Not Lakshmi's Story but Your Heart's") are still in the texts word for word.

## Checklist

Now met:
- Focus keyword in the body text: both languages (English failed `check_seo.py` before; Hindi was only in the H1).
- Focus keyword within the first 100 words: both languages, in the direct-answer paragraph.
- Focus keyword in the meta description and the URL slug (English): the English meta description and slug now carry "is being too good a bad thing".
- Direct answer early (report section 5): added in both languages.
- Question headings: one more H2 per language is now a natural question.

Still unmet (1):
- No unsupported scriptural claims: the body states Lakshmi's curse as Puranic fact and calls Radha's husband an asura (Sanskrit review issues 1–2, report flags 1–2). These are content corrections for the editor, not SEO fixes, so they were not made here; no SEO field repeats them. The minor review issues 3–5 (the "myth and legend" gloss, आयन/अयन, Latin script in the Hindi takeaway) are also left to the editor.

`python3 tools/check_seo.py too_bad_to_be_too_good_valentines` passes.

## Report updates

- Section 2: keyword note added describing the `_seo` texts.
- Section 3: the English meta description and slug are now the ones in seo.json, marked recommended; the Hindi meta description and slug are marked recommended (unchanged).
- Section 8: English description, Hindi alternativeHeadline (now the full Hindi title) and the suggested post URLs match seo.json.
- Section 11: the JSON block equals seo.json.
- Section 12: the SEO checklist was missing from the report; added and marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.slug | too-bad-to-be-too-good | is-being-too-good-a-bad-thing |
| wordpress.en.meta_description | Can being too good be a mistake? Through the story of Lakshmi, Acharya Upendra Ji shows why love without discernment hurts and what the heart must learn. | Is being too good a bad thing? Through the story of Lakshmi, Acharya Upendra Ji shows why love without discernment hurts and what the heart must learn. (151 characters) |
| wordpress.en.focus_keyword | is being too good a bad thing | unchanged (the `_seo` text now uses it) |
| wordpress.hi.focus_keyword, slug, title, meta_description | (as below) | unchanged (already contain the focus keyword) |
| title.en | Is Being Too Good a Bad Thing? Love Without Discernment | unchanged |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

No other talk uses the new slug.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | zarurat-se-zyada-achha-hona | is-being-too-good-a-bad-thing |
| focus_keyword | ज़रूरत से ज़्यादा अच्छा होना | is being too good a bad thing |
| title | ज़रूरत से ज़्यादा अच्छा होना भी गलत क्यों है | आचार्य जी | Is Being Too Good a Bad Thing? Love Without Discernment |
| meta_description | क्या ज़रूरत से ज़्यादा अच्छा होना भी गलत है? लक्ष्मी की कथा से आचार्य उपेंद्र जी बताते हैं कि बिना विवेक का प्रेम क्यों चोट देता है। | Is being too good a bad thing? Through the story of Lakshmi, Acharya Upendra Ji shows why love without discernment hurts and what the heart must learn. |
