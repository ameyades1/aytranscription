competent_guru_activate_chakras_kundalini: SEO fix

The check failed before the fix: neither focus keyword ("गुरु से कुंडलिनी जागरण" / "Kundalini awakening through a Guru") appeared in the body or the meta description, and the English slug (`kundalini-awakening-through-guru`) lacked the keyword's "a". The opening asked why people live their whole lives at one level but gave no direct answer, and "Kundalini" first appeared only in the shaktipat section (report section 4). Each language now has a short direct answer after the two opening paragraphs, built only from the blog's own sections (chakras as levels of consciousness and ways of living, many lifetimes per chakra, a competent Guru raising three or four chakras in one sadhana through shaktipat), and it uses the focus keyword within the first 100 words. Two headings per language are now readers' questions, as report section 4 suggested. Sanskrit review issue 1 (authenticity flag 1, the Lakshman Rekha) is now attributed to the popular telling, for the "No unsupported scriptural claims" item; the example itself is unchanged.

## Hindi (`competent_guru_activate_chakras_kundalini_blog_seo.txt`): 4 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the opening, new paragraph | (none) | संक्षेप में: आचार्य जी के अनुसार गुरु से कुंडलिनी जागरण में कई जन्मों की प्रगति एक साधना में हो सकती है। सात चक्र चेतना के सात स्तर हैं, और हर स्तर जीने का एक अलग ढंग है। एक-एक चक्र ऊपर उठने में कई जन्म लग जाते हैं, पर समर्थ गुरु शक्तिपात द्वारा एक ही साधना में तीन-चार चक्र एक साथ उठा सकता है। | Focus keyword (absent from the body) in the first 100 words; direct answer (report section 5), using only what the blog says. |
| H2 1 | ## एक चक्र, कई जन्म | ## एक चक्र में कितने जन्म लगते हैं? | Heading as the question readers ask (report section 4); the section answers it. |
| "क्या करुणा के साथ मेरे पास विवेक भी है?", paragraph 3 | लक्ष्मण रेखा खींची गई थी, कहा गया था कि बाहर किसी को भिक्षा मत देना। | लोक-परंपरा के अनुसार, लक्ष्मण रेखा खींची गई थी और कहा गया था कि बाहर किसी को भिक्षा मत देना। | Content trust: the Lakshman Rekha is not in the Valmiki Ramayana (review issue 1, flag 1); now attributed to the popular telling. Example unchanged. |
| H2 8 | ## शक्तिपात: जन्मों का फ़ास्ट फ़ॉरवर्ड | ## शक्तिपात क्या है? जन्मों का फ़ास्ट फ़ॉरवर्ड | Question heading for the secondary keyword "शक्तिपात क्या है" (report section 4); the section answers it. |

## English (`competent_guru_activate_chakras_kundalini_blog_seo_en.txt`): 4 changes

| Where | Before | After | Why |
|---|---|---|---|
| After the opening, new paragraph | (none) | In short: Acharya Ji teaches that in Kundalini awakening through a Guru, many lifetimes of progress can happen in one sadhana. The seven chakras are seven levels of consciousness, each a different way of living, and rising from one chakra to the next can take many lifetimes. Through shaktipat, a competent Guru can raise a seeker three or four chakras at once. | Focus keyword (absent from the body) in the first 100 words; direct answer (report section 5), using only what the blog says. |
| H2 1 | ## One Chakra, Many Lifetimes | ## How Many Lifetimes Does One Chakra Take? | Heading as the question readers ask (report section 4); the section answers it. |
| "Does My Compassion Come with Discernment?", paragraph 3 | Lakshmana had drawn the **Lakshman Rekha** (the protective line he drew around her hut) and told her not to give alms to anyone outside it. | In the popular telling, Lakshmana had drawn the **Lakshman Rekha** (a protective line) and told her not to give alms to anyone outside it. | Content trust: review issue 1 (flag 1); attributed to the popular telling, and the detail not in the Hindi ("around her hut") removed, as the review suggests. |
| H2 8 | ## Shaktipat: Fast-Forwarding Through Lifetimes | ## What Is Shaktipat? Fast-Forwarding Through Lifetimes | Question heading for the secondary keyword "what is shaktipat" (report section 4). |

No teaching, example, H1 or order of ideas changed; the blog quotes no verses. The number and order of headings are the same, and the "सात चक्र, सात तरह का जीवन" / "Seven Chakras, Seven Ways of Living" heading near which inline.jpg sits is unchanged. All five `links` phrases and the `also_read` heading ("नेतृत्व से शरणागति तक" / "From Leadership to Surrender") are still in the texts, each found by grep.

## Checklist

- Now met:
  - Focus keyword in the body text and the meta description (both languages), and in the English URL slug. `check_seo.py` failed on these before; it now passes.
  - Focus keyword within the first 100 words (both languages).
  - Focus keyword taken from wording the article uses: the `_seo` texts now contain it.
  - No unsupported scriptural claims: the Lakshman Rekha is attributed to the popular telling.
  - A direct answer (40-60 words) early on; two question H2s per language.
- Section 12 was missing from the report; it has been added, with every item met.
- Still unmet: none.
- Left alone on purpose: review issues 2-6 (Sita Mata "उसके साथ जाना पड़ा", Vishuddhi/Vishuddha, शरणागत/sharanagati, Valya/Ratnakar, "guidance" vs. आज्ञा) are wording and consistency points, not SEO items; they are left for the editor to fix in the original blog. images.txt gives the English inline-image heading as "Seven Chakras, Seven Kinds of Life" (report section 9); images.txt is outside this task.

## seo.json changes

| Field | Before | After |
|---|---|---|
| wordpress.hi.meta_description | एक चक्र ऊपर उठने में कई जन्म लगते हैं। आचार्य जी बताते हैं कि सात चक्र सात तरह के जीवन हैं, और समर्थ गुरु का शक्तिपात यह यात्रा कैसे तेज़ करता है। | गुरु से कुंडलिनी जागरण कैसे होता है? आचार्य जी बताते हैं कि सात चक्र सात तरह के जीवन हैं, और समर्थ गुरु का शक्तिपात जन्मों की यात्रा कैसे तेज़ करता है। (151) |
| wordpress.en.meta_description | One chakra can take lifetimes. Acharya Ji explains the seven chakras as seven ways of living, and how a competent Guru's shaktipat speeds the journey. | Kundalini awakening through a Guru: Acharya Ji explains the seven chakras as seven ways of living, and how a competent Guru's shaktipat speeds the journey. (155) |
| wordpress.en.slug | kundalini-awakening-through-guru | kundalini-awakening-through-a-guru |

The focus keywords (both kept: the body now uses them), secondary keywords, both titles, the Hindi slug (`guru-se-kundalini-jagran`), `links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON; sections 2 (keyword note), 3 (recommended meta descriptions and slugs), 8 (descriptions and suggested English slug) and 12 (checklist, newly added) were updated to match.

## Final seo.json values

| Field | Hindi | English |
|---|---|---|
| slug | guru-se-kundalini-jagran | kundalini-awakening-through-a-guru |
| focus_keyword | गुरु से कुंडलिनी जागरण | Kundalini awakening through a Guru |
| title | गुरु से कुंडलिनी जागरण: सात चक्र, सात तरह का जीवन | Kundalini Awakening Through a Guru: 7 Chakras of Life |
| meta_description | गुरु से कुंडलिनी जागरण कैसे होता है? आचार्य जी बताते हैं कि सात चक्र सात तरह के जीवन हैं, और समर्थ गुरु का शक्तिपात जन्मों की यात्रा कैसे तेज़ करता है। | Kundalini awakening through a Guru: Acharya Ji explains the seven chakras as seven ways of living, and how a competent Guru's shaktipat speeds the journey. |
