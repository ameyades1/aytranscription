joy_sorrow_transformation: SEO fix

`check_seo.py` failed on the original texts. Neither focus keyword appeared in the blog body: the Hindi had only "सुख-दुःख की असली जड़" (a heading), and the English never asked why some people are always unhappy. The English meta description also asked "Why are some people always unhappy?", which is not the keyword's word order. The report had no section 12 checklist, so this fix added it. Each language gets one change: a short direct answer after the intro, built only from what the blog already says, that carries the focus keyword into the first 100 words. The English meta description now uses the keyword word for word. The focus keywords and slugs stay the same.

## Hindi (`joy_sorrow_transformation_blog_seo.txt`): 1 change

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…भीतर की **धारणा शक्ति** का है।") | (none) | संक्षेप में, आचार्य जी के अनुसार सुख-दुःख का असली कारण बाहर की परिस्थिति नहीं, मन की धारणा शक्ति है। मन जिसे बार-बार स्वीकार करता है, वही उसका स्वभाव बन जाता है। इसीलिए दुःख धारण करने वाले मन को खिलौनों में भी दुःख दिखता है, और सुख धारण करने वाला मन गोबर में भी घोड़ा ढूँढ लेता है। | The focus keyword "सुख-दुःख का असली कारण" was nowhere in the body (SureRank error). This direct answer (57 words) puts it in the first 100 words. It is built only from the blog's own intro, the धारणा शक्ति section and the takeaways ("मन जिसे बार-बार स्वीकार करता है, वही उसका स्वभाव बन जाता है"), and follows report section 5. It repeats no `links` phrase. |

## English (`joy_sorrow_transformation_blog_seo_en.txt`): 1 change

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new second paragraph (after "…until it becomes its nature).") | (none) | In short, the answer to why some people are always unhappy lies within, not in what happens outside. Whatever the mind accepts again and again becomes its nature. A mind that keeps accepting pain finds it even among gifts; a mind that holds on to joy finds the promise of a horse even in the dung. | The focus keyword "why some people are always unhappy" was nowhere in the body (SureRank error). This direct answer (56 words) puts it in the first 100 words. It is built only from the blog's own sections and takeaways ("whatever the mind accepts again and again becomes its nature", "the promise of a horse even in the dung") and follows report section 5. It repeats no `links` phrase. |

No teaching, example, H1 or order of ideas changed, and the Markdown is kept. The blog quotes no scripture. No heading was changed: "क्या दुःख बाहर से आता है?" / "Does Suffering Come from Outside?" is already a natural question. The other candidate, "धारणा शक्ति: सुख-दुःख की असली जड़" / "Dharana Shakti: The Real Root of Happiness and Suffering", is the `also_read` heading and has to stay word for word. grep confirms that all four `links` phrases and the `also_read` heading are still in both texts. The inline image's heading ("बैटरी कौन लाएगा?") is unchanged.

## Checklist

- Now met (both languages): the focus keyword is in the body text and within the first 100 words. The English focus keyword is in the meta description. `check_seo.py` passes.
- Added: section 12, the SEO checklist, which was missing from the report. Every item is marked met.
- Still unmet: none.
- Left alone on purpose:
  - Sanskrit review issue 1 (Major): the happy son's words "पूरी तरह सकारात्मक सोच वाले… उनकी माँ ने भी…" are given to Acharya Ji (flag 1). It is not a scriptural claim and no checklist item covers it, and correcting it means rewriting the story's narration, which goes beyond an SEO edit. It is left for the editor to fix in the original blog with the review's wording. Until then it must not be quoted in snippets.
  - Review issues 2–4 (Minor: the Patanjali dharana note, गोबर / लीद, उलटे / उल्टे) are not SEO items and are left for the editor.
  - Report section 4's optional outline ideas (story H2s as H3s, "धारणा शक्ति क्या है?" as an H2) were not applied. They would change the number of headings or the `also_read` heading.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.en.meta_description | Why are some people always unhappy? Through the story of a father and two sons, Acharya Upendra Ji shows that joy and sorrow come from dharana shakti. | Why some people are always unhappy: through the story of a father and two sons, Acharya Upendra Ji shows that joy and sorrow come from dharana shakti. (150) |
| wordpress.hi.slug | sukh-dukh-ka-asli-karan | sukh-dukh-ka-asli-karan (unchanged; already fits the focus keyword) |
| wordpress.en.slug | why-some-people-are-always-unhappy | why-some-people-are-always-unhappy (unchanged; 34 characters, the focus keyword) |

The focus keywords, secondary keywords, `title` (both already contain the focus keywords), Hindi meta description, `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON. Sections 2, 3 and 8 (the English description) were updated to match, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sukh-dukh-ka-asli-karan | why-some-people-are-always-unhappy |
| focus_keyword | सुख-दुःख का असली कारण | why some people are always unhappy |
| title | सुख-दुःख का असली कारण: धारणा शक्ति की एक कथा | Why Some People Are Always Unhappy: Dharana Shakti |
| meta_description | सुख-दुःख का असली कारण क्या है? एक पिता, दो पुत्र और एक अनोखे प्रयोग की कथा से आचार्य उपेंद्र जी बताते हैं कि सुख-दुःख बाहर नहीं, मन की धारणा शक्ति में है। | Why some people are always unhappy: through the story of a father and two sons, Acharya Upendra Ji shows that joy and sorrow come from dharana shakti. |
