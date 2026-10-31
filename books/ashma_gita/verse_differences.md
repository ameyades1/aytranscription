# Ashma Gita: book (slide) readings vs Gita Press

> **Correction (found later):** shlokas 10, 30 and 51 are *not* slide readings. The raw transcripts
> (`raw/Day02_Part03.txt`, `raw/Day03_Part07.txt`, `raw/Day03_Part14.txt`) have the Gita Press readings
> वा, कालनोदित and संगमम्. Our transcript-cleaning step changed them to वै, कालचोदित and सङ्गतम्, and the
> book inherited that. Shloka 21's fragments are what was said aloud. See
> `comparison_v4_vs_unified_v1.md`. The "Where the slide readings may come from" section below is
> superseded for 10, 30 and 51.

Book: version 4 (`book/ashma_gita_04.*`). Gita Press source: Mahabharata with Hindi translation, Khand 5
(Shanti Parva), adhyaya 28, read from the page images of
`references/mahabharata_gita_press_khand5_shanti_parva.pdf` (archive.org item `mahabharata-volume-5`),
PDF pages 178–186.

## The four differences

| Shloka | Chapter | Book (slide) | Gita Press | Effect on meaning |
|---|---|---|---|---|
| 10 | 15 | ये च विंशतिवर्षा **वै** त्रिंशद्वर्षाश्च मानवाः। | ये च विंशतिवर्षा **वा** त्रिंशद्वर्षाश्च मानवाः। | वै is an emphasis word ("indeed"); वा means "or". Gita Press translates "बीस **या** तीस वर्षकी उम्रवाले", which fits वा. |
| 21 | 22 | only fragments: आसनं शयनं … नियतं सर्वभूतानाम् … कालेनैव **भवन्त्युत** | आसनं शयनं यानमुत्थानं पानभोजनम्। नियतं सर्वभूतानां कालेनैव **भवत्युत**॥ | The book has only pieces of the verse; भवन्त्युत ("they happen") vs भवत्युत ("it happens"). Same meaning. |
| 30 | 27 | अहमेतत् करोमीति मन्यते काल**चोदितः**। | अहमेतत् करोमीति मन्यते काल**नोदितः**। | चोदित and नोदित both mean "urged, driven". Same meaning ("driven by time"). |
| 51 | 33 | पथि **सङ्गतम्**अभ्येति दारैरन्यैश्च बन्धुभिः॥ | पथि **संगमम्**अभ्येति दारैरन्यैश्च बन्धुभिः॥ | संगत ("met, together") vs संगम ("a meeting"). Same meaning. |

Spelling only: shloka 28, पतङ्गवत् (book) vs पतंगवत् (Gita Press). Same word; the nasal is written as ङ्
instead of a dot (anusvara).

None of the four changes the teaching: two are synonyms (30, 51), one is a small grammar difference (21),
one is a different particle (10).

## Do Gita Press printings differ among themselves?

Three Gita Press copies of Khand 5 on archive.org were compared (OCR text; the first also by page image):

| | Vol 5 (`mahabharata-volume-5`, used for the book) | 1955 printing (`zozP_…1955…`) | Another Khand 5 scan (`Dkhm_…`) |
|---|---|---|---|
| 21 …भवत्युत | ✔ | ✔ | ✔ |
| 30 …कालनोदितः | ✔ | ✔ | ✔ |
| 51 …सङ्गममभ्येति | ✔ | ✔ | ✔ |
| 10 वा / वै | वा (page image) | not readable (OCR garbled) | not readable (OCR garbled) |

For 21, 30 and 51 the Gita Press printings agree with each other and differ from the slides. Shloka 10 is
confirmed in one printing only.

## Goenka and Swami Ramsukhdas

Those two are Gita Press's **Bhagavad Gita** commentaries: Jayadayal Goyandka's *Tattva-Vivechani* and
Swami Ramsukhdas's *Sadhak-Sanjivani* (the latter is in `references/shrimad_bhagavad_gita.pdf`). Both
comment on the same Sanskrit Gita text. The Ashma Gita is in the **Mahabharata**, whose Gita Press
Hindi translation is by neither of them (archive.org credits the series to Pandit Ramnarayan Datt Shastri
Pandey "Ram"). So that split does not explain these differences.

## Where the slide readings may come from (not confirmed)

- A different edition (for example the Pune Critical Edition, or another printed or online text).
- Slips when the slides were typed. Shloka 51's सङ्गतम् looks like a mix-up with shlokas 39 and 41, which
  both say "पथि संगतमेव…" a few verses earlier.

## Recommendation

If the source of the slide text can be found, it may settle these. Otherwise, CLAUDE.md makes Gita Press
the authority for scripture, so the printed book should use the Gita Press readings; for shloka 21, the
full verse would replace the fragments. Not changed yet.

## Resolved in v5

Version 5 (`book/ashma_gita_05.*`, chapters before it in `chapters_v4/`) uses the Gita Press reading for
shlokas 10 (वा), 30 (कालनोदितः) and 51 (संगममभ्येति), and the full Gita Press text of shloka 21. The cleaning
prompt `tools/prompts/book/01_clean_transcript.txt` now keeps verse wording as given and only fixes form.
