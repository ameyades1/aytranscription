know_kind_student_shishya: SEO fix

`check_seo.py` failed on the original texts. Neither focus keyword was in the blog body: the Hindi only says "शिष्य तीन प्रकार के होते हैं" and the English only "three kinds of disciples", never the searched "शिष्य के तीन प्रकार" / "three types of disciples". Each language gets two changes. First, a short direct answer after the intro, built only from what the blog already says (report section 5), which puts the focus keyword in the first 100 words. Second, one heading is rephrased as the question readers search for. The report had no section 12 checklist, so this fix added it. seo.json is unchanged: the focus keywords, slugs, titles and meta descriptions already fit the fixed texts.

## Hindi (`know_kind_student_shishya_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…पहचान लेता है कि आप कैसे शिष्य हैं।") | (none) | संक्षेप में, शिष्य के तीन प्रकार उनकी मांग से पहचाने जाते हैं। तामसिक शिष्य कहता है "मेरे लिए कुछ तो कीजिए" और तुरंत उपाय चाहता है। राजसिक शिष्य समाधान नहीं, केवल मन की शांति चाहता है। सात्विक शिष्य पूछता है "मैं कहां गलत था?", और यही प्रश्न ज्ञान लाता है, जिससे कर्म स्थायी रूप से सुलझता है। | The focus keyword "शिष्य के तीन प्रकार" was nowhere in the body (SureRank error). This direct answer (57 words) puts it in the first 100 words. It only restates the three disciple sections, the "दवा से नहीं…" section ("कर्म **स्थायी रूप से** सुलझता है") and the takeaways, and repeats no `links` phrase. It keeps the blog's own spelling "सात्विक". |
| `##` heading of the fourth section | ## दवा से नहीं, ज्ञान से मिटता है कर्म | ## बाहरी उपाय से समस्या क्यों लौट आती है? | Report section 4: a natural question that the section answers ("अस्थायी दवा या अस्थायी उपचार से समस्या लौट आती है… क्यों? क्योंकि…"). It also softens the medical reading (flag 7). Not a `links`, `also_read` or image heading. |

## English (`know_kind_student_shishya_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…from a single sentence you speak.") | (none) | In short, the three types of disciples differ in what they ask the Guru for. The tamasic disciple says "please do something for me" and wants an instant remedy. The rajasic disciple wants only peace of mind, not a solution. The sattvic disciple asks "where did I go wrong?", and that question brings the knowledge that resolves karma for good. | The focus keyword "three types of disciples" was nowhere in the body (SureRank error). This direct answer (60 words) puts it in the first 100 words. It only restates the three disciple sections, the karma section ("the karma resolves **for good**") and the takeaways, and repeats no `links` phrase. |
| `##` heading of the fourth section | ## Knowledge, Not Medicine, Dissolves Karma | ## Why Do Problems Keep Coming Back? | A natural search question (section 2's "why do problems keep coming back karma") that the section answers ("A temporary medicine or a passing treatment only lets the problem come back… Why?"). It also softens the medical reading (flag 7). Not a `links`, `also_read` or image heading. |

No teaching, example, H1, verse, verse translation or order of ideas changed, and the Markdown is kept. The number and order of `##` headings are the same. grep confirms that all five `links` phrases and the `also_read` heading ("तीसरा शिष्य: \"मैं कहां गलत था?\"" / "The Third Disciple: \"Where Did I Go Wrong?\"") are still in both texts, and the `links` phrases still come first in the intro (the direct answer follows "शिष्य तीन प्रकार के होते हैं" / "there are three kinds of disciples"). The inline image's heading ("नचिकेता: बारह वर्ष का उत्तम शिष्य") is unchanged.

## Checklist

- Now met (both languages): the focus keyword is in the body text and within the first 100 words; no searched-wording mismatch is left. `check_seo.py` passes.
- Added: section 12, the SEO checklist, which was missing from the report.
- Still unmet (1): "No unsupported scriptural claims". The Nachiketa boons passage and its takeaway present pitru dosha and Shri Vidya as the Katha Upanishad's boons (Sanskrit review issue 1, Critical; flag 1), and the Hindi meaning of Gita 2.47 is off (review issue 2, Major; flag 2). Fixing them means adding scriptural facts and changing a verse translation, which goes beyond an SEO edit. They are left for the editor to correct in the original blog with the review's wording. Until then the boons, pitru dosha and Shri Vidya stay out of titles, keywords and snippets (they are).
- Left alone on purpose:
  - Review issues 3–9 (verse context, half-verse marking, Nachiketa's age, सात्त्विक spelling, the chemotherapy line, गुरुदेव / आचार्य जी naming) are editorial and left for the editor. The new paragraphs name no speaker and add no medical claim.
  - Report section 4's new H2 "शिष्य के तीन प्रकार कौन-से हैं?" / "What Are the Three Types of Disciples?" was not added: it would change the number of headings. The direct answer sits in the intro instead.
  - `images.txt` gives the English inline heading as "Nachiketa: The Twelve-Year-Old Best Disciple", not the blog's "Nachiketa: The Ideal Disciple at Twelve". The Hindi heading matches, so the image is still placed; images.txt is not this fix's file.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | shishya-ke-teen-prakar | shishya-ke-teen-prakar (unchanged; already built from the focus keyword) |
| wordpress.en.slug | three-types-of-disciples | three-types-of-disciples (unchanged; 24 characters, the focus keyword) |

No other field changed: the focus keywords (now in the fixed bodies), secondary keywords, `title` and meta descriptions (both already contain the focus keywords), `links`, `also_read`, `alt`, `caption`, `related`, category and tags. The report's section 11 holds the same JSON. Section 2 has a new keyword note, section 3 marks the seo.json values as recommended, section 8 already matched, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | shishya-ke-teen-prakar | three-types-of-disciples |
| focus_keyword | शिष्य के तीन प्रकार | three types of disciples |
| title | शिष्य के तीन प्रकार: आप गुरु से क्या मांगते हैं? | Three Types of Disciples: What Do You Ask the Guru For? |
| meta_description | तामसिक, राजसिक या सात्त्विक? आचार्य जी बताते हैं शिष्य के तीन प्रकार, बाहरी उपाय क्यों अस्थायी है, और "मैं कहां गलत था?" पूछने से कर्म कैसे सुलझता है। | Tamasic, rajasic or sattvic? Acharya Ji explains three types of disciples, why outer remedies fade, and how asking where you went wrong resolves karma. |
