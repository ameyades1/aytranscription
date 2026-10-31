# Missing Ashma Gita shlokas: placeholders in version 2, filled in version 3

**Version 3 (`book/ashma_gita_03.*`):** all 31 placeholders are filled from the Gita Press Mahabharata, Khand 5
(Shanti Parva), adhyaya 28, PDF pages 178–186 of `references/mahabharata_gita_press_khand5_shanti_parva.pdf`
(archive.org item `mahabharata-volume-5`). Each verse was read from the page image and compared with the
OCR text (`references/mahabharata_gita_press_khand5_shanti_parva_ocr.txt`); every difference was an OCR
error, settled from the image. Gita Press numbers 25 and 26 as one and a half verses each (२५½, २६½), so
those blocks have three and two half-lines. Shloka 55 is printed as `पितृदेवमनुष्याणानृण्यादनसूयकः`.
Chapters before the fill: `chapters_v2/`.

**Version 4 (`book/ashma_gita_04.*`):** the flow around the 31 verses. Each introducing paragraph is split
into the lead-in (ending with a colon), the verse block (Sanskrit, Hindi meaning, source line) and the rest
of the explanation, unchanged. The Hindi meaning is the book's own prose meaning, moved into the block;
for 22, 25, 39, 41 and 43, where the prose gave only part of it, the block has the Gita Press translation.
For 25 the second half of the meaning moved in from the next paragraph. Chapters before: `chapters_v3/`.

## Existing verses that differ from Gita Press (not changed)

These came from the slides; the book still has the slide reading.

| Shloka | Chapter | Book (slide) | Gita Press |
|---|---|---|---|
| 10 | 15 | `ये च विंशतिवर्षा वै` | `ये च विंशतिवर्षा वा` |
| 21 | 22 | fragments only, `…भवन्त्युत` | `आसनं शयनं यानमुत्थानं पानभोजनम्। नियतं सर्वभूतानां कालेनैव भवत्युत॥` |
| 30 | 27 | `मन्यते कालचोदितः` | `मन्यते कालनोदितः` |
| 51 | 33 | `पथि सङ्गतमभ्येति` | `पथि संगममभ्येति` |

Spelling only: 28 `पतङ्गवत्` (Gita Press `पतंगवत्`). Shlokas 14, 15 and 23, written from memory earlier,
match Gita Press.

## Version 2 placeholders

31 shlokas have their meaning in the book but no Sanskrit text. Each has a placeholder block in its chapter file:

```
> **[संस्कृत श्लोक यहाँ जोड़ें: गीता प्रेस, महाभारत, शान्तिपर्व २८.८]**
> (अश्मा गीता, श्लोक ८)
```

Replace the first line with the two Sanskrit lines from the Gita Press Mahabharata (Shanti Parva, adhyaya 28), each as `> **…**`, ending the first half with `।` and the second with `॥`. Keep the source line. Then rebuild with `tools/book/book.sh ashma_gita pdf`.

Page = page of `book/ashma_gita_02.pdf`. Line = line of the placeholder's first line in the chapter file; line numbers further down the same file move by one for each line you add.

| Shloka | PDF page | Chapter file | Line | Chapter |
|---|---|---|---|---|
| 8 | 131 | `chapters/14_chapter.txt` | 7 | अध्याय १४: भोग से पतन और राजदंड |
| 9 | 134 | `chapters/14_chapter.txt` | 42 | अध्याय १४: भोग से पतन और राजदंड |
| 13 | 157 | `chapters/16_chapter.txt` | 84 | अध्याय १६: मानसिक दुःख के दो कारण |
| 16 | 173 | `chapters/18_chapter.txt` | 7 | अध्याय १८: जो आए उसे सहना |
| 17 | 189 | `chapters/20_chapter.txt` | 7 | अध्याय २०: आनंद का घर और यह परदेस |
| 20 | 209 | `chapters/22_chapter.txt` | 7 | अध्याय २२: नियति और समय का उलटफेर |
| 22 | 213 | `chapters/22_chapter.txt` | 50 | अध्याय २२: नियति और समय का उलटफेर |
| 25 | 230 | `chapters/25_chapter.txt` | 7 | अध्याय २५: मृत्यु का सेतु और प्रबल पुरुषार्थ |
| 26 | 236 | `chapters/25_chapter.txt` | 70 | अध्याय २५: मृत्यु का सेतु और प्रबल पुरुषार्थ |
| 27 | 241 | `chapters/26_chapter.txt` | 7 | अध्याय २६: आज को श्रेष्ठ बनाओ |
| 31 | 252 | `chapters/27_chapter.txt` | 36 | अध्याय २७: असंतोष से अपराध, ज्ञान होते हुए भी पाप |
| 32 | 257 | `chapters/28_chapter.txt` | 7 | अध्याय २८: काल, अदृष्ट और औषध की सीमा |
| 33 | 259 | `chapters/28_chapter.txt` | 36 | अध्याय २८: काल, अदृष्ट और औषध की सीमा |
| 34 | 264 | `chapters/28_chapter.txt` | 85 | अध्याय २८: काल, अदृष्ट और औषध की सीमा |
| 37 | 277 | `chapters/30_chapter.txt` | 7 | अध्याय ३०: काल की समदृष्टि और पथिकों का साथ |
| 38 | 279 | `chapters/30_chapter.txt` | 32 | अध्याय ३०: काल की समदृष्टि और पथिकों का साथ |
| 39 | 282 | `chapters/30_chapter.txt` | 61 | अध्याय ३०: काल की समदृष्टि और पथिकों का साथ |
| 40 | 287 | `chapters/30_chapter.txt` | 107 | अध्याय ३०: काल की समदृष्टि और पथिकों का साथ |
| 41 | 290 | `chapters/31_chapter.txt` | 7 | अध्याय ३१: संसार चक्र और शास्त्र पर श्रद्धा |
| 42 | 294 | `chapters/31_chapter.txt` | 50 | अध्याय ३१: संसार चक्र और शास्त्र पर श्रद्धा |
| 43 | 300 | `chapters/32_chapter.txt` | 7 | अध्याय ३२: रोना नहीं, श्राद्ध और यज्ञ |
| 44 | 304 | `chapters/32_chapter.txt` | 48 | अध्याय ३२: रोना नहीं, श्राद्ध और यज्ञ |
| 45 | 306 | `chapters/32_chapter.txt` | 71 | अध्याय ३२: रोना नहीं, श्राद्ध और यज्ञ |
| 46 | 306 | `chapters/32_chapter.txt` | 76 | अध्याय ३२: रोना नहीं, श्राद्ध और यज्ञ |
| 53 | 319 | `chapters/34_chapter.txt` | 24 | अध्याय ३४: गृहस्थ, तीन ऋण और दोषदृष्टि का त्याग |
| 54 | 320 | `chapters/34_chapter.txt` | 33 | अध्याय ३४: गृहस्थ, तीन ऋण और दोषदृष्टि का त्याग |
| 55 | 322 | `chapters/34_chapter.txt` | 61 | अध्याय ३४: गृहस्थ, तीन ऋण और दोषदृष्टि का त्याग |
| 56 | 326 | `chapters/34_chapter.txt` | 110 | अध्याय ३४: गृहस्थ, तीन ऋण और दोषदृष्टि का त्याग |
| 57 | 328 | `chapters/35_chapter.txt` | 7 | अध्याय ३५: शोक छोड़कर उठो |
| 58 | 329 | `chapters/35_chapter.txt` | 24 | अध्याय ३५: शोक छोड़कर उठो |
| 59 | 330 | `chapters/35_chapter.txt` | 33 | अध्याय ३५: शोक छोड़कर उठो |

