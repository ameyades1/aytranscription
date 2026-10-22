was_ram_rajya_like_federal_or: SEO fix

The report's checklist (section 12) had no unmet items. Section 2 noted a keyword mismatch: people search "राम राज्य कैसा था" (the video title) and "was Ram Rajya federal or unitary", but the Hindi body never used the first, and the English question appeared only in the H1, which SureRank does not count. The opening also asked its question without answering it early. Each language gets three changes: a short direct answer after the intro, built only from what the blog already says, which puts the searched wording in the first 100 words, and two H2s rephrased as the questions readers search (report section 4's suggestions). The focus keywords move to the searched wording.

## Hindi (`was_ram_rajya_like_federal_or_blog_seo.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…क्या संघीय शासन (फेडरल गवर्नमेंट) से राम राज्य आ सकता है?") | (none) | तो राम राज्य कैसा था? आचार्य जी के अनुसार वह पूर्णतः एकात्मक था: एक ही हाथ, एक ही आवाज़। संघीय शासन में केंद्र और राज्य विरोधी विचार रख सकते हैं, इसलिए उससे राम राज्य नहीं आ सकता। इसका सूत्र है केंद्र की बात के प्रति शरणागति, और हर राज्य को अपनी भाषा में अपने लोगों की सेवा की स्वतंत्रता। | The opening asked its question without answering it. A direct answer of about 55 words (report section 5), restating only the blog's own sections, puts the searched wording "राम राज्य कैसा था" (new focus keyword) in the first 100 words. "आचार्य जी के अनुसार" keeps the "unitary" view as Acharya Ji's (report flag 1). |
| H2 before "श्री राम का राज्य पूर्णतः एकात्मक था।" | ## इतिहास के महान राज्य कैसे चलते थे? | ## राम राज्य कैसा था? इतिहास के महान राज्य | Rephrased as the searched question (report section 4); the section opens with Shri Rama's kingdom and answers it. The rest of the heading keeps the Chandragupta and Shivaji examples in view. |
| H2 before "यदि राम राज्य लाना है…" | ## राम राज्य का सूत्र: शरणागति और स्थानीय सेवा | ## राम राज्य कैसे आएगा? शरणागति और स्थानीय सेवा | Natural question heading matching "ram rajya kaise aayega" (report section 4); the section answers it. "राम राज्य का सूत्र" stays in the body (direct answer and the last takeaway). |

## English (`was_ram_rajya_like_federal_or_blog_seo_en.txt`): 3 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, new third paragraph (after "…can a federal government ever bring about Ram Rajya?") | (none) | So was Ram Rajya federal or unitary? According to Acharya Ji, it was completely unitary: a single hand at the helm and a single voice. In a federal system the centre and the states may hold opposing views, so it cannot bring about Ram Rajya. The formula is surrender to the word of the centre, with each state free to serve its own people in its own language. | Direct answer of about 60 words (report section 5), built only from the blog's own sections. The searched wording "was Ram Rajya federal or unitary" (new focus keyword), previously only in the H1, now sits in the body's first 100 words. Attributed to Acharya Ji (flag 1). |
| H2 before "Shri Rama's kingdom was entirely unitary." | ## How Did History's Great Kingdoms Run? | ## What Was Ram Rajya Like? History's Great Kingdoms | Rephrased as the searched question (report section 4); the section answers it. |
| H2 before "To bring about Ram Rajya…" | ## The Formula for Ram Rajya: Surrender and Local Service | ## How Can We Bring Ram Rajya? Surrender and Local Service | Natural question heading matching the secondary keyword "how to bring Ram Rajya"; the section answers it. "The formula for Ram Rajya" stays in the last takeaway. |

No teaching, example, order of ideas, H1 or Markdown changed, and no claim was added. The blog quotes no scripture verses. All five `links` phrases and the `also_read` heading ("हमारी व्यवस्था की खिचड़ी" / "The Khichdi of Our System") are still in both texts, each confirmed by grep; the inline image's heading ("एक संस्था, अनेक शाखाएं" / "One Organisation, Many Branches") is unchanged. The heading count and order are unchanged.

## Checklist

- Already met and still met: every item in section 12. `check_seo.py` passes.
- Improved: the focus keyword is now the searched wording in both languages, in the first 100 words (inside a direct answer) and in a question H2. This settles the mismatch noted in section 2.
- Still unmet: none.
- Left alone on purpose:
  - The Sanskrit review's minor attribution edits (report flags 1–3: "entirely unitary" stated as fact, Shivaji Maharaj and "foreign travellers", "local employment" in the takeaway) and "बंगाली" → "बांग्ला" (flag 5) are not SEO items; they are left for the editor to apply to the original blog. The new direct answer already frames the view as Acharya Ji's.
  - The report's sections 1, 5 and 7 still mention "राम राज्य" / "Ram Rajya" as the main queries; this fix may only edit sections 2, 3, 8, 11 and 12. Section 7's cannibalization note still holds: no other talk targets the new keywords.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | राम राज्य संघीय था या एकात्मक? शासन का सूत्र | राम राज्य कैसा था? संघीय या एकात्मक शासन (40) |
| title.en | Ram Rajya: Federal or Unitary Rule? Acharya Ji Explains | Was Ram Rajya Federal or Unitary? Acharya Ji Explains (53) |
| wordpress.hi.focus_keyword | राम राज्य | राम राज्य कैसा था |
| wordpress.hi.secondary_keywords | राम राज्य कैसा था, राम राज्य का सूत्र, संघीय शासन, एकात्मक व्यवस्था | राम राज्य, राम राज्य का सूत्र, संघीय शासन, एकात्मक व्यवस्था |
| wordpress.hi.meta_description | राम राज्य संघीय था या एकात्मक? आचार्य जी संस्था और पिज़्ज़ा कंपनी के उदाहरणों से समझाते हैं कि केंद्र के प्रति शरणागति और अपनी भाषा में सेवा ही इसका सूत्र है। | राम राज्य कैसा था, संघीय या एकात्मक? आचार्य जी संस्था व पिज़्ज़ा कंपनी के उदाहरण से बताते हैं कि केंद्र के प्रति शरणागति और अपनी भाषा में सेवा ही इसका सूत्र है। (160) |
| wordpress.hi.slug | ram-rajya-sanghiya-ya-ekatmak | ram-rajya-kaisa-tha |
| wordpress.en.focus_keyword | Ram Rajya | was Ram Rajya federal or unitary |
| wordpress.en.secondary_keywords | was Ram Rajya federal or unitary, federal government, unitary system, how to bring Ram Rajya | Ram Rajya, how to bring Ram Rajya, federal government, unitary system |
| wordpress.en.meta_description | Was Ram Rajya federal or unitary? Acharya Ji shows, with a pizza-company example, why one voice at the centre and local service in each state are the key. | unchanged (154; already contains the new keyword) |
| wordpress.en.slug | ram-rajya-federal-or-unitary | was-ram-rajya-federal-or-unitary (32 characters) |

`links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2, 3 and 8 were updated to match, and section 12's marks are unchanged (all met).

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | ram-rajya-kaisa-tha | was-ram-rajya-federal-or-unitary |
| focus_keyword | राम राज्य कैसा था | was Ram Rajya federal or unitary |
| title | राम राज्य कैसा था? संघीय या एकात्मक शासन | Was Ram Rajya Federal or Unitary? Acharya Ji Explains |
| meta_description | राम राज्य कैसा था, संघीय या एकात्मक? आचार्य जी संस्था व पिज़्ज़ा कंपनी के उदाहरण से बताते हैं कि केंद्र के प्रति शरणागति और अपनी भाषा में सेवा ही इसका सूत्र है। | Was Ram Rajya federal or unitary? Acharya Ji shows, with a pizza-company example, why one voice at the centre and local service in each state are the key. |
