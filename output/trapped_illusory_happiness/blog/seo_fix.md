trapped_illusory_happiness: SEO fix

Copies written: `trapped_illusory_happiness_blog_seo.txt` (Hindi) and `trapped_illusory_happiness_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro ("...सबसे अधिक क्षणिक भी है।") | (none) | इंद्रिय सुख क्षणिक क्यों है? क्योंकि यह बाहरी विषयों से बंधा है। शब्द, स्पर्श, रूप, रस और गंध के माध्यम से मिलने वाला शारीरिक आनंद विषय के जाते ही चला जाता है। आचार्य जी बताते हैं कि यह लालसा, आदत और निर्भरता का चक्र बनाता है, और इसे सीखना नहीं, बस पहचानना है। | The focus keyword "इंद्रिय सुख क्षणिक क्यों है" was not in the body (check_seo error) and the opening gave no direct answer. The paragraph (report section 5) uses only what the blog says (sections 3, 4 and 5); it puts the keyword within the first 100 words |
| H2 2 | इंद्रियों का सुख: देखना गलत नहीं, पर... | शारीरिक आनंद क्या है? देखना गलत नहीं, पर... | A question readers search (secondary keyword "शारीरिक आनंद क्या है"); the section opens with the definition ("शारीरिक आनंद वह सुख है जो इंद्रियों से मिलता है") |
| H2 3 | विषय गया, तो आनंद गया | इंद्रिय सुख क्यों नहीं टिकता? विषय गया, तो आनंद गया | Report section 4: a question heading for snippet capture; the section answers it ("बाहरी विषय चला गया, तो आनंद भी चला गया"). The original wording is kept after the question |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the intro ("...the most fleeting of all.") | (none) | Why do sense pleasures fade so fast? Because they are tied to outer objects. Physical bliss comes through sound, touch, form, taste and smell, so when the object goes, the joy goes with it. As Acharya Ji explains, it breeds a cycle of craving, habit and dependency, and there is nothing to learn here, only something to recognise. | The focus keyword was not in the body (check_seo error) and the opening gave no direct answer. The paragraph (report section 5) uses only what the blog says; it carries the new focus keyword "why sense pleasures fade" (matched as "Why do sense pleasures fade") within the first 100 words |
| H2 2 | Pleasures of the Senses: Seeing Is Not Wrong, But... | What Is Physical Bliss? Seeing Is Not Wrong, But... | A question readers search (secondary keyword "physical bliss meaning"); the section opens with the definition |
| H2 3 | When the Object Goes, So Does the Joy | Why Don't Sense Pleasures Last? When the Object Goes, So Does the Joy | Report section 4: a question heading; it uses the searched wording of the secondary keyword "why sense pleasures don't last", and the section answers it. The original wording is kept after the question |

The headings keep their number and order; the inline image and the Also read box are placed by section position. No teaching, example or H1 was touched (the blog quotes no verses). All five `links` phrases and the `also_read` headings ("रोज़मर्रा के जीवन में शारीरिक आनंद" / "Physical Bliss in Everyday Life") are still in the texts word for word.

## Checklist

Now met:
- Focus keyword in the body text: both languages (both failed `check_seo.py` before).
- Focus keyword in the meta description and URL slug (English): the old keyword "why sense pleasures don't last" could not match the slug (its apostrophe gives "dont") and was not in the meta description; the new keyword "why sense pleasures fade" is in the title, the meta description ("Why do sense pleasures fade so fast?"), the body and the slug.
- Focus keyword within the first 100 words: both languages, in the direct-answer paragraph.
- Direct answer early (report section 5): added in both languages.
- Question headings: two H2s per language are now natural questions.

Still unmet (1):
- No unsupported scriptural claims: the body presents the tamasic/rajasic/sattvic ladder, with sense pleasure as tamasic, as what "the scriptures" say, while Gita 18.38 classes sense-contact pleasure as rajasic (Sanskrit review issue 1, report flag 1). This is a content correction for the editor, not an SEO fix, so it was not made here; no SEO field repeats it. The minor review issues 2–5 (tanmatras wording, सात्त्विक spelling, "your own nature", takeaway wording) are also left to the editor.

`python3 tools/check_seo.py trapped_illusory_happiness` passes.

## Report updates

- Section 2: "why sense pleasures fade" added as the English primary keyword, with a keyword note on the `_seo` texts and the focus keyword change.
- Section 3: the titles, meta descriptions and slugs in seo.json are marked recommended in both languages; the new English title and slug added.
- Section 8: English alternativeHeadline and keywords match seo.json; URL slugs noted.
- Section 11: the JSON block equals seo.json.
- Section 12: the SEO checklist was missing from the report; added and marked for the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Why Sense Pleasures Don't Last: The Trap of Physical Bliss | Why Sense Pleasures Fade: The Trap of Physical Bliss (52 characters) |
| wordpress.en.focus_keyword | why sense pleasures don't last | why sense pleasures fade |
| wordpress.en.slug | why-sense-pleasures-dont-last | why-sense-pleasures-fade |
| wordpress.en.secondary_keywords | physical bliss meaning, illusory happiness, cycle of craving and dependency, five tanmatras | why sense pleasures don't last, physical bliss meaning, illusory happiness, cycle of craving and dependency |
| wordpress.en.meta_description | (as below) | unchanged (already contains the new focus keyword) |
| wordpress.hi (slug, focus_keyword, title, meta_description) | (as below) | unchanged (the `_seo` text now uses the focus keyword) |
| links, also_read | (unchanged) | unchanged (no edit touched a phrase or heading) |

No other talk uses the new slug or focus keyword.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | indriya-sukh-kshanik-kyon | why-sense-pleasures-fade |
| focus_keyword | इंद्रिय सुख क्षणिक क्यों है | why sense pleasures fade |
| title | इंद्रिय सुख क्षणिक क्यों है? शारीरिक आनंद का जाल | Why Sense Pleasures Fade: The Trap of Physical Bliss |
| meta_description | इंद्रिय सुख क्षणिक क्यों है? आचार्य जी बताते हैं: शारीरिक आनंद बाहरी विषयों से बंधा है, विषय गया तो आनंद गया। यह लालसा और निर्भरता का चक्र बनाता है। | Why do sense pleasures fade so fast? Acharya Ji explains physical bliss: tied to outer objects, it breeds craving and dependency. Spot it in daily life. |
