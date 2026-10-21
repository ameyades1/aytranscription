gyan_sarovar_mount_abu_women_address: SEO fix

The fixed texts are `gyan_sarovar_mount_abu_women_address_blog_seo.txt` (Hindi) and `gyan_sarovar_mount_abu_women_address_blog_seo_en.txt` (English). The original blog texts are unchanged.

## Hindi changes

| where | before | after | why |
|---|---|---|---|
| New paragraph after the opening paragraphs | (none) | क्या स्त्री पुरुष के बराबर है? आचार्य जी के अनुसार स्त्री पुरुष के बराबर नहीं, कम से कम हजार गुना शक्तिशाली है। दुर्गा सप्तशती देवी को अतिसौम्य और अतिरौद्र दोनों रूपों में नमन करती है। अंतर्ज्ञान, धृति, स्मृति और मेधा स्त्री की स्वाभाविक शक्तियां हैं, और भारत को अर्धनारीश्वर संतुलन महिला सशक्तिकरण से ही मिलेगा। | The focus keyword "क्या स्त्री पुरुष के बराबर है" was only in the body after about 100 words; it is now in the first 100. This is also the early direct answer (52 words, report section 5), built only from what the blog says. It doesn't define धृति (flag 4) and repeats no `links` phrase |
| `##` heading 4 | बीस मिनट की यात्रा और अंतर्ज्ञान | क्या स्त्री का अंतर्ज्ञान स्वाभाविक है? | A natural question the section answers ("यह अंतर्ज्ञान कोई सीखी हुई चीज नहीं, स्त्री में स्वाभाविक है"); it carries the secondary keyword "स्त्री का अंतर्ज्ञान" (report section 4) |

## English changes

| where | before | after | why |
|---|---|---|---|
| New paragraph after the opening paragraphs | (none) | Is a woman equal to a man? According to Acharya Ji, she is not merely equal; she is at least a thousand times more powerful. The Durga Saptashati bows to the Goddess as both supremely gentle and supremely fierce. Intuition, dhriti, smriti and medha are a woman's natural powers, and only women's empowerment can bring India the balance of Ardhanarishvara. | The focus keyword "is a woman equal to a man" was only in the body after about 100 words; it is now in the first 100. This is also the early direct answer (60 words, report section 5), built only from what the blog says, with the claim credited to Acharya Ji (flag 6). It repeats no `links` phrase |
| `##` heading 4 | A Twenty-Minute Journey and the Gift of Intuition | Is a Woman's Intuition Natural? | A natural question the section answers ("It is part of a woman's very nature"), report section 4 |

These things are not changed: the H1, the number and order of the `##` headings, both verses with their translations and references, the Key Takeaways, every `links` phrase, the `also_read` heading "मां, गुरु और भारत माता" / "The Mother, the Guru and Mother India" (also the inline image's section), the order of ideas and all the teachings. The Sanskrit review's corrections (the source of "न दैन्यं न पलायनम्", the gloss in its translation, marking 5.13 as a half verse, धृति, the Hindi takeaway "गुरु मां", निःस्वार्थ, IAST) touch scripture or meaning, so the editor decides on them.

## Checklist

Now met:
- Focus keyword within the first 100 words (both languages; `_seo` texts)
- Focus keyword in the URL slug (English): the old slug `is-woman-equal-to-man` left out "a"
- Direct answer (40–60 words) early in the post (both languages)
- Section 12 (SEO checklist) added to the report; it was missing

Still unmet: none.

## seo.json changes

| field | before | after |
|---|---|---|
| wordpress.en.slug | is-woman-equal-to-man | is-a-woman-equal-to-a-man |

Nothing else changed. Both focus keywords stay, because the `_seo` texts use them, and the Hindi slug `kya-stri-purush-ke-barabar-hai` stays. The titles and meta descriptions already contain the keywords. Secondary keywords, tags, `links` and `also_read` are unchanged. In the report, I added the keyword note to section 2, put the new English slug in sections 3, 8 and 11, and added section 12.

## Final seo.json values

| field | Hindi | English |
|---|---|---|
| slug | kya-stri-purush-ke-barabar-hai | is-a-woman-equal-to-a-man |
| focus keyword | क्या स्त्री पुरुष के बराबर है | is a woman equal to a man |
| title | क्या स्त्री पुरुष के बराबर है? माउंट आबू में आचार्य जी | Is a Woman Equal to a Man? Acharya Ji's Answer at Mount Abu |
| meta description | क्या स्त्री पुरुष के बराबर है? माउंट आबू में आचार्य उपेंद्र जी ने 500 महिलाओं से कहा: नारी हजार गुना शक्तिशाली है। जानें अर्धनारीश्वर और अंतर्ज्ञान का संदेश। | Is a woman equal to a man? At Mount Abu, Acharya Upendra Ji told 500 women she is a thousand times stronger, and why India needs Ardhanarishvara balance. |
