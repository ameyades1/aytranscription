lakshmi_come_some_people_not_others: SEO fix

Copies written: `lakshmi_come_some_people_not_others_blog_seo.txt` (Hindi) and `lakshmi_come_some_people_not_others_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| End of section "आपका लक्ष्य कितना बड़ा है?", new paragraph after "…तब लक्ष्मी हमारे पास आती है।" | (none) | तो लक्ष्मी किसके पास आती है? उसके पास, जिसमें लक्ष्य साधने की शक्ति है। लक्ष्मी चंचल हैं, अकेली आएं तो टिकती नहीं। उनकी लाल साड़ी बताती है कि वे किसके साथ आती हैं: जिनकी आप सेवा करते हैं उनके लिए निःस्वार्थ प्रेम, पूरी शक्ति से कर्म और समाज के लिए त्याग। | The focus keyword "लक्ष्मी किसके पास आती है" was not in the body (SureRank error) and there was no early direct answer; built only from the blog's own points (lakshya, चंचल, red sari: love, rajoguna, त्याग); the keyword now starts at word 85 |
| H2 3 | लक्ष्मी चंचल क्यों हैं? | लक्ष्मी क्यों नहीं ठहरतीं? | Echoes the searched thumbnail query "घर में लक्ष्मी क्यों नहीं ठहरतीं?"; the section answers it ("जब अकेली आती हैं, तो अधिक दिन टिकती नहीं") and still says she is चंचल; "घर में" left out to avoid the remedy framing (report section 10, flag 5) |

## English (2 changes)

| Where | Before | After | Why |
|---|---|---|---|
| End of section "How Big Is Your Goal?", new paragraph after "…the strength to pursue that goal." | (none) | So why does Lakshmi come to some people and not others? She comes to those who gain the strength to pursue a goal. She is restless and does not stay when she comes alone. Her red sari shows what she comes with: unconditional love for those you serve, full-strength action, and sacrifice for society. | The focus phrase was not in the body (SureRank error) and there was no early direct answer; uses the searched wording (the video title) within the first 100 words (words 93–99); built only from the blog's own points (53 words) |
| H2 3 | Why Is Lakshmi Restless? | Why Doesn't Lakshmi Stay? | The natural question readers search ("why Lakshmi does not stay", a secondary keyword); the section answers it ("she does not stay for long") |

All `links` phrases and both `also_read` headings are unchanged and still in the `_seo` texts. Scripture verses, translations, references and the H1 are untouched. The Sanskrit review's corrections (tools/review/lakshmi_come_some_people_not_others.md: the Hindi meaning of Durga Saptashati 4.5, "first half" marking, the lakshya "root" wording, attributing the "unmarried" line) are outside this fix's scope and remain open for the editor.

## Checklist

Now met:
- Focus keyword in the body text (both languages; it was missing in both)
- Focus keyword in the meta description (English; the new keyword matches the existing meta's "Why does Lakshmi come to some people")
- Focus keyword within the first 100 words (both languages)
- Focus keyword taken from wording the article uses (the `_seo` texts now use it)
- Direct answer paragraph (40–60 words) placed early (both languages)
- One H2 per language phrased as the question readers search

Still unmet: none. All section 12 items are marked `[x]`; `tools/check_seo.py` passes.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.en | Why Lakshmi Comes to Some People: Goal, Love, Sacrifice | Why Does Lakshmi Come to Some People? Goal, Love, Sacrifice |
| wordpress.en.focus_keyword | why Lakshmi comes to some people | why does Lakshmi come to some people |
| wordpress.en.slug | why-lakshmi-comes-to-some-people | why-does-lakshmi-come-to-some-people |

The old English focus keyword is not added to `secondary_keywords`: it is a near-duplicate of the new one, and the list already has 4 entries. The Hindi fields, both meta descriptions, `links`, `also_read`, `related`, alt text, captions, category and tags are unchanged. Report updated: section 2 (keyword table and note), section 3 (English recommended title and slug), section 8 (English alternativeHeadline and keywords; the `{{HI_URL}}`/`{{EN_URL}}` placeholders now carry the Hindi and English slugs), section 11 (seo.json block), and section 12 (checklist added and marked).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | lakshmi-kiske-paas-aati-hai | why-does-lakshmi-come-to-some-people |
| focus_keyword | लक्ष्मी किसके पास आती है | why does Lakshmi come to some people |
| title | लक्ष्मी किसके पास आती है: लक्ष्य, प्रेम और त्याग | Why Does Lakshmi Come to Some People? Goal, Love, Sacrifice |
| meta_description | लक्ष्मी किसके पास आती है और किसके पास टिकती है? आचार्य उपेंद्र जी बताते हैं कि लक्ष्मी लक्ष्य हैं, और उनकी लाल साड़ी प्रेम, कर्मशीलता और त्याग की प्रतीक है। | Why does Lakshmi come to some people and not others? Acharya Upendra Ji explains Lakshmi as lakshya, a goal, and her red sari as love, drive and sacrifice. |
