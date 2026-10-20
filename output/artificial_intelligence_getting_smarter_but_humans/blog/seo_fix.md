artificial_intelligence_getting_smarter_but_humans: SEO fix

The report's main gap was the mismatch in section 2: people search "is AI making us dumber" / "क्या AI हमें मूर्ख बना रहा है", but neither body used that wording, so it could not be the focus keyword. The opening also did not answer that question directly. Each language gets two changes: a direct answer under the H1 that opens with the searched question, built only from the blog's own points (and the report's section 5), and the second section's H2 rephrased as that question, as section 4 suggests. The searched wording becomes the focus keyword; the old focus keyword moves to the secondary keywords. The Sanskrit review's issues are content edits, not SEO items, and are left for the editor in the original blog.

## Hindi (`artificial_intelligence_getting_smarter_but_humans_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before "## कलियुग का एक पुराना संकेत") | (none) | क्या AI हमें मूर्ख बना रहा है? आचार्य जी के अनुसार, हाँ, यदि हम अपनी सोच का काम भी उसे सौंप दें। कैलकुलेटर से लेकर ChatGPT तक हमने अपनी मूल बुद्धि का काम मशीनों को सौंप दिया है: फ़ोन स्मार्ट होता गया और हम सोचना भूलते गए। इसका उपाय प्रतिबंध नहीं, बल्कि विवेक, अर्थात भीतर के गणपति, से AI का पात्रता और उद्देश्य के साथ उपयोग है। | Searched wording (new focus keyword) in the first 100 words, and a direct answer early. It only restates the blog: calculator to ChatGPT, मूल बुद्धि handed to machines, "फ़ोन स्मार्ट होता जा रहा है और हम dumb होते जा रहे हैं", no ban but पात्रता and उद्देश्य, गणपति as विवेक. It avoids the link phrase "अपनी विवेक बुद्धि का", so that link still falls on its original sentence. |
| H2 of the second section | ## यह सब एक छोटे से कैलकुलेटर से शुरू हुआ | ## क्या AI हमें मूर्ख बना रहा है? | Rephrased as the searched question (report section 4); the section answers it ("फ़ोन स्मार्ट होता जा रहा है और हम dumb होते जा रहे हैं"), and still opens with the calculator. Number and order of headings unchanged. |

## English (`artificial_intelligence_getting_smarter_but_humans_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| New paragraph after the H1 (before "## An Old Sign of the Kali Yuga") | (none) | Is AI making us dumber? In Acharya Ji's view, it does when we hand it our own thinking. From the calculator to ChatGPT, we have given our original intelligence over to machines: the phone keeps getting smarter while we stop thinking. The answer is not a ban but viveka, the inner Ganapati: using AI with worthiness and a clear purpose. | Searched wording (new focus keyword) in the first 100 words, and a direct answer early (60 words), built only from the blog's own points. Worded so it does not repeat the link phrase "your own discerning intelligence". |
| H2 of the second section | ## It All Began with a Small Calculator | ## Is AI Making Us Dumber? | Rephrased as the searched question (report section 4); the section answers it ("the phone keeps getting smarter while we keep getting dumber") and still opens with the calculator. Number and order of headings unchanged. |

No teaching, example, order of ideas, H1, verse, verse translation or reference, or Markdown changed. All five `links` phrases and the `also_read` heading ("कलियुग का एक पुराना संकेत" / "An Old Sign of the Kali Yuga") are still in both texts, each confirmed by grep. The inline image's section (images.txt: the calculator heading) keeps its position as the second section, so the page and the importer still place `inline.jpg` there.

## Checklist

- Now met: the searched wording is the focus keyword in both languages, in the SEO title, meta description, body (first 100 words and one H2) and the English slug; a direct answer is placed early; one question H2 per language.
- Already met and still met: every other ticked item in section 12. `check_seo.py` passes.
- Still unmet (2):
  - Each tag can be shared by at least 3 posts: "कृत्रिम बुद्धि" / "Artificial Intelligence" is used only by this post so far. Not fixable in this blog's text; it needs `satyug_rules_kaliyug_different_path` and `guru_bridging_science_spirituality` to use the tag.
  - No unsupported scriptural claims: Sanskrit review issue 1 (Kali Yuga as an age of machines presented as scripture) and issue 8 (Shukracharya mapping) are content corrections, not SEO edits; they are left for the editor in the original blog, and the `_seo` copy keeps the original wording.
- Left alone on purpose: section 4's other optional H2 changes ("What Is Viveka, and How Do We Awaken It?", and dropping the half-litre figure from the water H2). The first would need added sentences the blog does not have; the second is a factual correction for the editor (flag 4), not an SEO edit.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | कृत्रिम बुद्धि बढ़ रही है, हमारी विवेक बुद्धि कहाँ है? | क्या AI हमें मूर्ख बना रहा है? कृत्रिम बुद्धि और विवेक |
| title.en | Artificial Intelligence Is Getting Smarter. Are We? | Is AI Making Us Dumber? Artificial Intelligence and Viveka |
| wordpress.hi.slug | kritrim-buddhi-aur-vivek-buddhi | kya-ai-hamein-moorkh-bana-raha-hai |
| wordpress.en.slug | artificial-intelligence-and-viveka | is-ai-making-us-dumber |
| wordpress.hi.focus_keyword | कृत्रिम बुद्धि | क्या AI हमें मूर्ख बना रहा है |
| wordpress.en.focus_keyword | artificial intelligence | is AI making us dumber |
| wordpress.hi.secondary_keywords | क्या AI हमें मूर्ख बना रहा है, विवेक बुद्धि, मूल बुद्धि, AI और अध्यात्म | कृत्रिम बुद्धि, विवेक बुद्धि, मूल बुद्धि, AI और अध्यात्म |
| wordpress.en.secondary_keywords | is AI making us dumber, AI and spirituality, what is viveka, borrowed intelligence | artificial intelligence, AI and spirituality, what is viveka, borrowed intelligence |
| wordpress.hi.meta_description | कृत्रिम बुद्धि बढ़ रही है, हम मूल बुद्धि खो रहे हैं। आचार्य उपेंद्र जी बताते हैं कि AI के युग में विवेक बुद्धि, अर्थात भीतर के गणपति, को जगाना क्यों ज़रूरी है। | क्या AI हमें मूर्ख बना रहा है? आचार्य उपेंद्र जी बताते हैं कि कृत्रिम बुद्धि के युग में विवेक बुद्धि, अर्थात भीतर के गणपति, को जगाना क्यों ज़रूरी है। |
| wordpress.en.meta_description | Artificial intelligence keeps getting smarter while we stop thinking. Acharya Upendra Ji explains why viveka, your inner Ganapati, must guide its use. | Is AI making us dumber? Acharya Upendra Ji explains how we handed our thinking to machines, and why viveka, the inner Ganapati, must guide AI's use. |

The titles and meta descriptions were rewritten because they no longer contained the new focus keyword; they keep the old keyword as well (titles 54 and 58 characters; metas 149 and 148 characters). `links` and `also_read` are unchanged: no edit touched a phrase or that heading. The report's sections 2, 3, 8, 11 and 12 were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | kya-ai-hamein-moorkh-bana-raha-hai | is-ai-making-us-dumber |
| focus_keyword | क्या AI हमें मूर्ख बना रहा है | is AI making us dumber |
| title | क्या AI हमें मूर्ख बना रहा है? कृत्रिम बुद्धि और विवेक | Is AI Making Us Dumber? Artificial Intelligence and Viveka |
| meta_description | क्या AI हमें मूर्ख बना रहा है? आचार्य उपेंद्र जी बताते हैं कि कृत्रिम बुद्धि के युग में विवेक बुद्धि, अर्थात भीतर के गणपति, को जगाना क्यों ज़रूरी है। | Is AI making us dumber? Acharya Upendra Ji explains how we handed our thinking to machines, and why viveka, the inner Ganapati, must guide AI's use. |
