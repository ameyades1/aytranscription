need_murtis_symbols_understand_god: SEO fix

The report's checklist (section 12) had no unmet items. The fixes below put the searched wording into the body and turn one heading per language into a searched question. The original blog texts are unchanged; the edits are in `need_murtis_symbols_understand_god_blog_seo.txt` and `need_murtis_symbols_understand_god_blog_seo_en.txt`.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Section "क्या कोई सचमुच बिना आकार के पूजा कर सकता है?", 2nd paragraph, start | उनका उत्तर स्पष्ट है। | तो हम मूर्ति पूजा क्यों करते हैं? उनका उत्तर स्पष्ट है। | The searched question "मूर्ति पूजा क्यों करते हैं" was missing from the body. It now appears once in the first 100 words, followed directly by the existing answer, so it can be the focus keyword. |
| 6th `##` heading | दो ही रास्ते हैं | ईश्वर से जुड़ने के दो रास्ते कौन से हैं? | Rephrased as the question readers search for (report section 4). The section answers it ("योग के लिए दो ही स्थितियां हैं"; योग = जुड़ना). |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| Section "Can Anyone Truly Worship Without a Form?", 1st sentence | (a sacred image of the Divine) | (a sacred image of the Divine, often called an idol) | The most-searched wording uses "idol", which the body never used (section 2's mismatch note). A neutral gloss adds the word once in the first 100 words. The full query "why do Hindus worship idols" would not read naturally, so it stays a secondary keyword. |
| 6th `##` heading | Only Two Ways Forward | What Are the Two Ways to Union With God? | Rephrased as the question readers search for (report section 4). The section answers it ("Union, then, can happen in only two ways"). |

No teaching, example, verse or idea order was changed. The number and order of headings are the same, and the H1 is untouched. Every `links` phrase and both `also_read` headings are still in the texts word for word (checked with grep).

Direct answer: the opening already answers the main question within the first 100 words (paragraph 2: as long as we have form, worship needs a form in front of us). No paragraph was added.

Not done here (outside SEO scope, see tools/review/need_murtis_symbols_understand_god.md and report section 10): the Mecca/Medina correction, the ऋतम्भरा attribution, the जीवन्मुक्त spelling, the indriyas gloss and the गुरुदेव/आचार्य जी naming. These belong to an editorial pass on the original texts.

## Checklist

Now met (they were already met in the report, and still are): every item in section 12. The Hindi focus keyword is now the searched question and is in the first 100 words, the title, the meta description and the body. The English focus keyword "worship a murti" is in the first sentence, title, meta and slug.

Still unmet: none. `python3 tools/check_seo.py need_murtis_symbols_understand_god` passes.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | मूर्ति पूजा क्यों? निराकार ईश्वर और साकार उपासना | मूर्ति पूजा क्यों करते हैं, जब ईश्वर निराकार है? (48 characters) |
| wordpress.hi.focus_keyword | मूर्ति पूजा | मूर्ति पूजा क्यों करते हैं |
| wordpress.hi.secondary_keywords | मूर्ति पूजा क्यों करते हैं, साकार और निराकार, निराकार की पूजा | मूर्ति पूजा, साकार और निराकार, निराकार की पूजा |
| wordpress.hi.slug | murti-puja-kyon | murti-puja-kyon-karte-hain |
| wordpress.hi.meta_description | ईश्वर निराकार है तो मूर्ति पूजा क्यों? आचार्य जी समझाते हैं कि सीमित मनुष्य को साकार क्यों चाहिए, योग के दो रास्ते और मूर्ति ऋषियों के दर्शन से कैसे आई। | ईश्वर निराकार है तो मूर्ति पूजा क्यों करते हैं? आचार्य जी बताते हैं कि सीमित मनुष्य को साकार क्यों चाहिए, योग के दो रास्ते और मूर्ति ऋषियों के दर्शन से कैसे आई। (160 characters) |

English: no changes. The focus keyword stays "worship a murti", the slug stays `why-worship-a-murti-formless-god`, and the title and meta already contain the keyword. `links`, `also_read` and `related` are unchanged in both languages. The report's section 11 block matches the new seo.json, and section 2's keyword table and notes were updated. Section 12 needed no mark changes. Sections 3 and 8 now show the seo.json title, meta description and slug for both languages (section 3 marks them "recommended; in seo.json" and keeps the old Hindi title as a listed alternative; section 8's Hindi alternativeHeadline, description and keywords were updated, and both URL slugs are noted).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| Slug | murti-puja-kyon-karte-hain | why-worship-a-murti-formless-god |
| Focus keyword | मूर्ति पूजा क्यों करते हैं | worship a murti |
| Title | मूर्ति पूजा क्यों करते हैं, जब ईश्वर निराकार है? | Why Worship a Murti If God Is Formless? |
| Meta description | ईश्वर निराकार है तो मूर्ति पूजा क्यों करते हैं? आचार्य जी बताते हैं कि सीमित मनुष्य को साकार क्यों चाहिए, योग के दो रास्ते और मूर्ति ऋषियों के दर्शन से कैसे आई। | If God is formless, why worship a murti? Acharya Ji explains why finite beings need form, the two paths of yoga, and why murtis follow the rishis' vision. |
