power_of_deities_in_your_life: SEO fix

The report's checklist was already fully met with the broad focus keywords "देव और देवियाँ" / "gods and goddesses". The fix acts on section 2's mismatch note: the queries people search ("त्रिदेव और त्रिदेवियाँ", "ब्रह्मा विष्णु महेश का अर्थ", "Trimurti") were missing from the body. Two small edits per language put them in, and the focus keywords move to them.

## Hindi (`power_of_deities_in_your_life_blog_seo.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, first paragraph | ब्रह्मा, विष्णु, महेश। सरस्वती, लक्ष्मी, काली। ये नाम हम बचपन से सुनते आए हैं, … | ब्रह्मा, विष्णु, महेश। सरस्वती, लक्ष्मी, काली। ये हैं त्रिदेव और त्रिदेवियाँ, जिनके नाम हम बचपन से सुनते आए हैं, … | Searched wording and new focus keyword in the first 100 words (it was only in the H1, which SureRank does not count) |
| First H2 | ## तीन जोड़ियाँ, तीन शक्तियाँ | ## ब्रह्मा विष्णु महेश का अर्थ क्या है? तीन जोड़ियाँ, तीन शक्तियाँ | The section answers this searched question (the three pairs as सृष्टि, पालन, संहार); puts the secondary keyword "ब्रह्मा विष्णु महेश का अर्थ" in a heading |

## English (`power_of_deities_in_your_life_blog_seo_en.txt`): 2 changes

| Where | Before | After | Why |
|---|---|---|---|
| Intro, first paragraph | Brahma, Vishnu, Mahesh. Saraswati, Lakshmi, Kali. We have heard these names since childhood, … | Brahma, Vishnu, Mahesh. Saraswati, Lakshmi, Kali. These are the Trimurti and their consorts, names we have heard since childhood, … | "Trimurti" (searched, never in the body) and "Trimurti and their consorts" in the first 100 words; "consorts" restates the blog's own pairing of each god with a goddess |
| First H2 | ## Three Pairs, Three Powers | ## What Is the Trimurti? Three Pairs, Three Powers | The section answers this question; focus keyword in a heading |

No teaching, example, verse, H1, link phrase or "Also read" heading was changed; all five `links` phrases and the `also_read` heading are still in both texts.

## Checklist

- Now met (newly, with the searched wording): focus keyword is the query people search, in both languages; it appears in the first 100 words and in an H2; the mismatch flagged in section 2 is resolved.
- Already met and still met: every other item in section 12.
- Still unmet: none.
- Not changed, by choice: no separate direct-answer paragraph was added, because the first section already answers the main question right after the intro (the three pairs and the three stages, सृष्टि/पालन/संहार, srishti/palan/samhara). "Brahma Vishnu Mahesh meaning" still cannot match the English body (the names are written with commas, and "meaning" is not used), so it stays a secondary keyword.

## seo.json changes

| Field | Before | After |
|---|---|---|
| title.hi | देव और देवियाँ: ब्रह्मा, विष्णु, महेश आपके जीवन में | त्रिदेव और त्रिदेवियाँ: ब्रह्मा, विष्णु, महेश आपके जीवन में (59) |
| title.en | Gods and Goddesses in Your Life: Brahma, Vishnu, Mahesh | Trimurti and Their Consorts: Three Powers in Your Life (54) |
| wordpress.hi.slug | dev-aur-deviyan | tridev-aur-tridevi |
| wordpress.hi.focus_keyword | देव और देवियाँ | त्रिदेव और त्रिदेवियाँ |
| wordpress.hi.secondary_keywords | ब्रह्मा विष्णु महेश का अर्थ, त्रिदेव और त्रिदेवियाँ, सृष्टि पालन संहार का अर्थ, धन से पहले ज्ञान | ब्रह्मा विष्णु महेश का अर्थ, देव और देवियाँ, सृष्टि पालन संहार का अर्थ, धन से पहले ज्ञान |
| wordpress.hi.meta_description | ब्रह्मा-सरस्वती, विष्णु-लक्ष्मी, महेश-काली केवल कथा नहीं। आचार्य उपेंद्र जी बताते हैं कि ये देव और देवियाँ जीवन में रचना, पालन और त्याग की तीन शक्तियाँ हैं। | ब्रह्मा-सरस्वती, विष्णु-लक्ष्मी, महेश-काली केवल कथा नहीं। आचार्य उपेंद्र जी बताते हैं कि त्रिदेव और त्रिदेवियाँ जीवन में रचना, पालन और त्याग की शक्तियाँ हैं। (157) |
| wordpress.en.slug | gods-and-goddesses-in-your-life | trimurti-three-powers-in-your-life |
| wordpress.en.focus_keyword | gods and goddesses | Trimurti |
| wordpress.en.secondary_keywords | Brahma Vishnu Mahesh meaning, Trimurti and their consorts, Mahakala and Mahakali meaning, knowledge before wealth Saraswati Lakshmi | Trimurti and their consorts, Brahma Vishnu Mahesh meaning, gods and goddesses, knowledge before wealth Saraswati Lakshmi (Mahakala and Mahakali meaning dropped to stay at 4; `real_role_maha_kali` covers Mahakali in depth) |
| wordpress.en.meta_description | Brahma-Saraswati, Vishnu-Lakshmi, Mahesh-Kali: Acharya Upendra Ji explains these gods and goddesses as your powers to create, sustain and let go. | Brahma-Saraswati, Vishnu-Lakshmi, Mahesh-Kali: Acharya Upendra Ji explains the Trimurti and their consorts as your powers to create, sustain and let go. (152) |

`links`, `also_read`, `alt`, `caption`, `related`, category and tags are unchanged. The report's section 11 holds the same JSON, and section 2 is updated; sections 3 and 8 still show the old titles and slugs as originally proposed. `python3 tools/check_seo.py power_of_deities_in_your_life` passes.
