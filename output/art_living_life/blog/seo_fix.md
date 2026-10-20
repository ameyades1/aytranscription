art_living_life: SEO fix

The report had one gap, noted in section 4: the focus keyword (संसार छोड़ने की कला / art of leaving) appeared in the H1 but not in the first 100 words of the body, and the opening began with "what is guaranteed in life?" without saying early what the Art of Leaving is. The searched wording already matches the body (section 2), so the focus keywords stay. Each language gets two changes: a direct answer of 60 words under the H1, built from the report's section 5 and the blog's own sections, and one H2 rephrased as the question readers search, as section 4 suggests. The Sanskrit review's six Minor issues are not SEO items and are left for the editor to fix in the original blog.

## Hindi (`art_living_life_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before "## जीवन में गारंटी किस बात की है?") | (none) | संक्षेप में, संसार छोड़ने की कला का अर्थ है उस एक निश्चित घटना, मृत्यु, के लिए तैयार रहना, जिसकी तारीख कोई नहीं जानता। आचार्य जी कहते हैं कि जीने की कला तो बहुत लोग सिखा सकते हैं, पर मंच छोड़ने की यह विद्या केवल जीवनमुक्त सद्गुरु से ही मिलती है, क्योंकि मुक्ति वही दिला सकता है जो स्वयं मुक्त है। | Focus keyword in the first 100 words, and a direct answer early (60 words). It only restates the blog: only death is certain, its date is unknown, many teach the art of living, the art of leaving the stage comes only from a जीवनमुक्त सद्गुरु, and only the free can free. It keeps the body's spelling जीवनमुक्त and avoids the link phrases, so the links still fall on their original sentences. |
| H2 of the fourth section | ## Art of Living और Art of Leaving | ## संसार छोड़ने की कला क्या है? | Rephrased as the question readers search (report section 4); the section answers it (life is a play, learn how to leave the stage, from a जीवनमुक्त सद्गुरु). Number and order of headings unchanged. |

## English (`art_living_life_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before "## What Does Life Actually Guarantee?") | (none) | In short, the Art of Leaving means being ready for the one certain event in life, death, whose date no one knows. Many people can teach the Art of Living, Acharya Ji says, but the art of stepping off life's stage can only be learned from a jivanmukta Sadguru, because only one who is free can lead others to liberation. | Focus keyword in the first 100 words, and a direct answer early (60 words), built only from the blog's own points and the report's section 5. Worded so it does not repeat the link phrases "how to step off the stage" and "can lead you to liberation". |
| H2 of the fourth section | ## The Art of Living and the Art of Leaving | ## What Is the Art of Leaving? | Rephrased as the searched question (report section 4); the section answers it. Number and order of headings unchanged. |

No teaching, example, order of ideas, H1 or Markdown changed, and the blog quotes no scripture. All five `links` phrases and the `also_read` heading ("क्या आप जानते हैं वह दिन कब है?" / "Do You Know When Your Day Will Come?") are still in both texts, each confirmed by grep. The links still fall on their original sentences. The inline image's heading ("जीवन में गारंटी किस बात की है?") is unchanged.

## Checklist

- Now met: "Within the first 100 words (preferred)" in both languages, through the direct answer under the H1.
- Improved: a direct answer is placed early, and one question H2 per language carries the focus keyword.
- Already met and still met: every other item in section 12 (added to the report by this fix, since the report had no checklist yet). `check_seo.py` passes.
- Still unmet: none.
- Left alone on purpose:
  - Section 4's optional second H2 ("यह कला कौन सिखा सकता है?" / "Who Can Teach the Art of Leaving?") was not used: the rephrased H2's section already answers who can teach it, and one question H2 per language is enough.
  - Sanskrit review issues 1–6 (Minor: the videhamukta and chiranjeevi glosses, the जीवनमुक्त/जीवन्मुक्त spelling, "विदेह सद्गुरु" in the takeaways, the 180-year and 1,400-year claims) are content edits, not SEO items. They are left for the editor in the original blog. The new paragraph keeps the body's spelling जीवनमुक्त.
  - The report's section 4 still suggests these edits as "consider"; this fix may only edit sections 2, 3, 8, 11 and 12.

## seo.json changes

None. Both focus keywords were already the searched wording and are now in the first 100 words. The titles and meta descriptions contain them, and the English slug `art-of-leaving` contains the English keyword. No edit touched a `links` phrase or the `also_read` heading.

| Field | Before | After |
|---|---|---|
| wordpress.hi.slug | sansar-chhodne-ki-kala | sansar-chhodne-ki-kala (unchanged) |
| wordpress.en.slug | art-of-leaving | art-of-leaving (unchanged) |
| wordpress.hi.focus_keyword | संसार छोड़ने की कला | संसार छोड़ने की कला (unchanged) |
| wordpress.en.focus_keyword | art of leaving | art of leaving (unchanged) |

The report's section 11 therefore stays the same as seo.json; sections 3 and 8 already match it. Sections 2 (keyword note) and 12 (checklist) were updated.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | sansar-chhodne-ki-kala | art-of-leaving |
| focus_keyword | संसार छोड़ने की कला | art of leaving |
| title | संसार छोड़ने की कला: मृत्यु की तैयारी किससे सीखें | The Art of Leaving: Who Can Teach You to Prepare for Death? |
| meta_description | केवल मृत्यु निश्चित है, पर उसकी तारीख कोई नहीं जानता। आचार्य उपेंद्र जी बताते हैं संसार छोड़ने की कला क्या है और इसे कौन सिखा सकता है। | Death is life's only certainty, and no one knows the day. Acharya Upendra Ji explains the Art of Leaving, and why only a liberated Sadguru can teach it. |
