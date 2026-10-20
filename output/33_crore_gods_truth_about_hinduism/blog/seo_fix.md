33_crore_gods_truth_about_hinduism: SEO fix

Copies written: `33_crore_gods_truth_about_hinduism_blog_seo.txt` (Hindi) and `33_crore_gods_truth_about_hinduism_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph | इतने सारे भगवान क्यों? इस प्रवचन में… | इतने सारे भगवान क्यों? 33 कोटि देवता क्यों? इस प्रवचन में… | The searched wording "33 कोटि देवता" was missing from the body, and the focus keyword was not in the first 100 words |
| H2 2 | विदेशी विद्यार्थियों का प्रश्न | हिंदू धर्म में इतने भगवान क्यों? | A question readers search; the section answers it ("हमारा भी एक ही भगवान है") |
| H2 3 | देवता यानी विभाग | क्या 33 कोटि देवता एक ही भगवान के विभाग हैं? | A question heading with the searched wording; the section answers it ("ये विभाग हैं। परमात्मा एक ही है।") |

## English (3 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Opening paragraph | …this: why so many gods? This discourse… | …this: why so many gods? Why 33 crore gods? This discourse… | The searched wording "33 crore gods" was missing from the body (it only said "thirty-three crore") |
| H2 2 | A Question from Students Abroad | Why Does Hinduism Have So Many Gods? | A question readers search; the section answers it ("We, too, have only one God") |
| H2 3 | The Gods as Departments | Are the 33 Crore Gods Departments of One God? | A question heading with the searched wording; the section answers it ("They are departments. God is one.") |

The headings keep their number and order. No teaching, example, verse or H1 was touched. All five `links` phrases and the `also_read` headings ("फिर मूर्ति क्यों?" / "Why an Idol, Then?") are still in the texts word for word.

## Checklist

Now met:
- Focus keyword within the first 100 words: Hindi was unmet; "33 कोटि देवता" is now in the opening paragraph. English "33 crore gods" is in the opening paragraph too.
- The searched wording mismatch (section 2) is resolved: both `_seo` texts now use it, so it is the focus keyword in each language.

Still unmet: none. `python3 tools/check_seo.py 33_crore_gods_truth_about_hinduism` passes.

Not changed:
- **Direct answer.** The opening already answers the question ("Hinduism, too, has one God. Everything else is an expression of that One."), so no answer paragraph was added. Section 5's longer snippet is still there if the editor wants it.
- **Authenticity flags 1–3** (the meaning of *koti*, "Other religions do not accept idol worship", परम तत्व → तत्त्व) are content corrections, not SEO fixes. Making them would add a claim or change wording that the talk's meaning depends on, so they stay with the editor.
- Report sections 5 (direct answer) and 6 (FAQ) still say "तैंतीस कोटि देवता" / "thirty-three crore gods". That is the body's own wording and is still a secondary keyword, so they were left as they are.

## Report updates

- Section 2: keyword table now marks "33 कोटि देवता" and "33 crore gods" as primary; the keyword note describes the `_seo` texts.
- Section 3: the recommended Hindi title and meta description and the English slug are now the ones in seo.json.
- Section 8: Hindi alternativeHeadline and description, the keywords and `about` names (both languages) and the post URLs (built from the slugs) match seo.json.
- Sections 11 and 12: already matched seo.json and the `_seo` texts.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | तैंतीस कोटि देवता या एक भगवान? हिंदू धर्म का सच | 33 कोटि देवता या एक भगवान? हिंदू धर्म का सच (43 characters) |
| wordpress.hi.focus_keyword | तैंतीस कोटि देवता | 33 कोटि देवता |
| wordpress.hi.secondary_keywords | 33 कोटि देवता, 33 करोड़ देवी देवता, हिंदू धर्म में कितने भगवान हैं, भगवान एक है या अनेक | तैंतीस कोटि देवता, 33 करोड़ देवी देवता, हिंदू धर्म में कितने भगवान हैं, भगवान एक है या अनेक |
| wordpress.hi.meta_description | हिंदू धर्म में तैंतीस कोटि देवता क्यों हैं? … | हिंदू धर्म में 33 कोटि देवता क्यों हैं? … (153 characters; the rest is unchanged) |
| wordpress.hi.slug | 33-koti-devta-ya-ek-bhagwan | unchanged (already built from "33 कोटि देवता") |
| wordpress.en.focus_keyword | why so many gods | 33 crore gods |
| wordpress.en.secondary_keywords | thirty-three crore gods, 33 crore gods, why does Hinduism have so many gods, one God in Hinduism | why so many gods, thirty-three crore gods, why does Hinduism have so many gods, one God in Hinduism |
| wordpress.en.slug | why-so-many-gods-hinduism-one-god | 33-crore-gods-one-god |
| title.en | Why So Many Gods? 33 Crore Gods or One God in Hinduism | unchanged (already contains "33 Crore Gods") |
| wordpress.en.meta_description | Why so many gods in Hinduism? … the 33 crore gods are … | unchanged (already contains "33 crore gods"; 155 characters) |
| links, also_read | (unchanged) | (unchanged; no edit touched a phrase or heading) |

No other talk uses either focus keyword or the new slug.
