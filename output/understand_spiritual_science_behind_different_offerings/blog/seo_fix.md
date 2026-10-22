understand_spiritual_science_behind_different_offerings: SEO fix

The report had no section 12 checklist yet, and `check_seo.py` failed: the focus keywords "देवताओं को अलग-अलग अर्पण क्यों" / "why different offerings to different gods" are the searched wording, but neither blog body used them (the bodies only list the pairings and say "प्रतीकात्मक विज्ञान" / "symbolic science"), the Hindi title had "अलग" instead of "अलग-अलग", and neither meta description contained the keyword. The opening also asked its question without answering it until the next section. Each language gets two changes: a short direct answer at the end of the first section, built only from what the blog already says (report section 5), and one H2 rephrased as the searched question. The focus keywords stay; the Hindi title and both meta descriptions are rewritten to contain them.

## Hindi (`understand_spiritual_science_behind_different_offerings_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| End of "क्या भगवान भी अपनी पसंद चुनते हैं?", new paragraph after "…क्या आपके पास उत्तर है?*" | (none) | तो देवताओं को अलग-अलग अर्पण क्यों किया जाता है? संक्षेप में, आचार्य जी के अनुसार यह देवताओं के बीच कोई बँटवारा नहीं, बल्कि प्रतीकों और ऊर्जा का विज्ञान है। रंग, ध्वनि, मंत्र और वनस्पति, सबमें ऊर्जा है, और हर अर्पण की ऊर्जा उस परिणाम से मेल खाती है जिसकी हम उस देवता से कामना करते हैं, जैसे गणेश जी से बुद्धि। | Direct answer (about 55 words) restating the blog's own sections (बँटवारा नहीं, हर वस्तु में ऊर्जा, गणेश जी यानी बुद्धि). Puts the focus keyword in the first 100 words. Worded "प्रतीकों और ऊर्जा का विज्ञान" so the link phrase "प्रतीकात्मक विज्ञान" keeps its place. |
| H2 of the energy section | ## हर वस्तु में ऊर्जा है | ## देवताओं को अलग-अलग अर्पण क्यों? हर वस्तु में ऊर्जा है | The searched question as a heading (report section 4); the section answers it. Number and order of headings unchanged. |

## English (`understand_spiritual_science_behind_different_offerings_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| End of "Do the Gods Have Their Own Preferences?", new paragraph after "…would you have an answer?*" | (none) | So why different offerings to different gods? In short, Acharya Ji explains that the gods have not divided up their favourites; behind each offering lies a science of symbols and energy. Colour, sound, mantra and plants all carry energy, and each offering's energy matches the result we seek from that deity, such as intelligence from Ganesha. | Direct answer (about 52 words), built only from the blog's sections and report section 5. Puts the focus keyword in the first 100 words. Worded "a science of symbols" so the link phrase "symbolic science" keeps its place. |
| H2 of the energy section | ## Every Object Carries Energy | ## Why Different Offerings to Different Gods? Every Object Carries Energy | The searched question as a heading (report section 4); the section answers it. Number and order of headings unchanged. |

No teaching, example, puja formula, H1 or order of ideas changed, and Markdown is kept. All four `links` phrases and the `also_read` heading ("पहले भगवान को जानो, फिर पूजा को" / "First Know Your God, Then Your Worship") are still in both texts, confirmed by grep. The inline image's heading ("अभिषेक: कोई साधारण स्नान नहीं" / "Abhisheka Is No Ordinary Bath") is unchanged.

## Checklist

- Now met: focus keyword in the SEO title (Hindi), in the meta description (both), in the body text (both), within the first 100 words (both); focus keyword taken from wording the article uses. `check_seo.py` passes.
- Added: the report's section 12, which was missing; every item is marked met.
- Still unmet: none.
- Left alone on purpose:
  - Report section 4's other heading ideas: "अभिषेक का अर्थ" / "Meaning of Abhisheka" and "पूजा में सुपारी और पान क्यों?" would promise answers those sections do not give (flag 4).
  - Sanskrit review issues 1–5 (all Minor: panchamrita's missing sugar, compound spellings and IAST, the bilva gloss) are not SEO items; they are left for the editor to fix in the original blog.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | देवताओं को अलग अर्पण क्यों? तुलसी, बिल्व, दूर्वा का विज्ञान | देवताओं को अलग-अलग अर्पण क्यों? तुलसी, बिल्व पत्र, दूर्वा (57) |
| wordpress.hi.meta_description | विष्णु को तुलसी, शिव को बिल्व पत्र, गणेश को दूर्वा क्यों? आचार्य उपेंद्र जी बताते हैं अर्पण के पीछे का प्रतीकात्मक विज्ञान, ऊर्जा और अभिषेक का अर्थ। | देवताओं को अलग-अलग अर्पण क्यों? विष्णु को तुलसी, शिव को बिल्व पत्र, गणेश को दूर्वा। आचार्य उपेंद्र जी बताते हैं अर्पण के पीछे का प्रतीकात्मक विज्ञान और ऊर्जा। (158) |
| wordpress.en.meta_description | Why tulsi for Vishnu, bilva for Shiva, durva for Ganesha? Acharya Upendra Ji explains the symbolic science of energy behind each offering and abhisheka. | Why different offerings to different gods? Tulsi to Vishnu, bilva to Shiva, durva to Ganesha: Acharya Upendra Ji explains the symbolic science of energy. (153) |
| wordpress.hi.slug | devtaon-ko-alag-arpan-kyon | devtaon-ko-alag-arpan-kyon (unchanged) |
| wordpress.en.slug | why-different-offerings-to-different-gods | why-different-offerings-to-different-gods (unchanged; 41 characters, contains the keyword) |

Focus keywords, secondary keywords, `title.en` (already contains the keyword), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2, 3 and 8 were updated to match, and section 12 was added.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | devtaon-ko-alag-arpan-kyon | why-different-offerings-to-different-gods |
| focus_keyword | देवताओं को अलग-अलग अर्पण क्यों | why different offerings to different gods |
| title | देवताओं को अलग-अलग अर्पण क्यों? तुलसी, बिल्व पत्र, दूर्वा | Why Different Offerings to Different Gods? The Science |
| meta_description | देवताओं को अलग-अलग अर्पण क्यों? विष्णु को तुलसी, शिव को बिल्व पत्र, गणेश को दूर्वा। आचार्य उपेंद्र जी बताते हैं अर्पण के पीछे का प्रतीकात्मक विज्ञान और ऊर्जा। | Why different offerings to different gods? Tulsi to Vishnu, bilva to Shiva, durva to Ganesha: Acharya Upendra Ji explains the symbolic science of energy. |
