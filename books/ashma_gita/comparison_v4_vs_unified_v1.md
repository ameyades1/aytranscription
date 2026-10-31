# Ashma Gita: our v4 vs AshmaGita_Complete_Unified_V1.docx

- **Ours:** `book/ashma_gita_04.pdf` (chapter files in `chapters/`).
- **Other:** `AshmaGita_Complete_Unified_V1.docx` (OneDrive, BookV1), dated 2 Oct, called "the other book" below.
- **Transcript:** the 36 sessions (Day 1: 11 parts, Day 2: 9, Day 3: 16); raw human transcripts in `raw/`,
  cleaned in `text_clean/`, with per-session digests in `digests/`.

## Summary

| | Ours (v4) | Other (Unified V1) |
|---|---|---|
| Length | ~94,200 words, 35 chapters in Parts, 357 pages | ~48,700 words, 28 chapters + an untitled opening chapter |
| Transcript size | ~104,000 words (cleaned), ~101,000 (raw) | same |
| Structure | by topic; chapters follow the shlokas | one chapter per session; Day 3 Parts 7–14 merged into one chapter of ~10,900 words |
| Teachings covered (digest check, 736 points) | ~95% found automatically; the rest checked by hand and found | ~52% found automatically; ~130 points checked by hand, most truly missing |
| Ashma Gita shlokas in Sanskrit | all 59 (Gita Press) | 21 of 59 |
| Content not in the transcript | none found, except the Gita Press translation in 5 verse blocks | small: one name (शुद्धोधन); a participants' round written as teaching |
| Format problems | none found | ~900 source-citation numbers left in the text, 119 em dashes, 18 Chinese full stops "。", 75 English glosses in brackets |

**In short:** the other book is a condensed version, about half the length. It keeps the main line of
each session but drops most examples, stories, asides and Antar Yog-specific remarks, and prints the
Sanskrit of only 21 shlokas. Nothing important in it is missing from ours. It does have clean-up problems:
AI citation numbers left in the text, em dashes, and stray characters.

## How this was checked

1. Each chapter of the other book was matched to its session by vocabulary overlap with the transcripts.
   The untitled opening is Day 1 Part 1, chapters 1–25 are one session each (Day 1 Part 2 to Day 3 Part 6),
   chapter 26 is Day 3 Parts 7–14, and chapters 27 and 28 are Day 3 Parts 15 and 16.
2. Each of the 736 teachings listed in the session digests was searched for in the matching part of
   both books (key Hindi words). This is a rough first pass: a paraphrase can score low even when the
   point is there.
3. Every point that scored low for ours, and about 130 that scored low for the other book, were then
   checked by reading. Paragraphs in both books with little vocabulary in common with the transcript
   were also read, to look for added material.

Limits: the hand check covered the flagged points, not every sentence. A point can be present in a
weakened form and still pass. Treat the percentages as indicative.

## Coverage by session

"Found" = share of the digest's teachings found by the automatic search (before the hand check).

| Session | Teachings | Ours | Other | | Session | Teachings | Ours | Other |
|---|---|---|---|---|---|---|---|---|
| D1P01 | 19 | 100% | 42% | | D3P01 | 31 | 93% | 29% |
| D1P02 | 20 | 100% | 55% | | D3P02 | 19 | 94% | 68% |
| D1P03 | 23 | 100% | 60% | | D3P03 | 19 | 89% | 57% |
| D1P04 | 21 | 85% | 42% | | D3P04 | 26 | 96% | 34% |
| D1P05 | 20 | 90% | 50% | | D3P05 | 27 | 92% | 40% |
| D1P06 | 14 | 85% | 35% | | D3P06 | 20 | 100% | 40% |
| D1P07 | 23 | 100% | 60% | | D3P07 | 16 | 93% | 81% |
| D1P08 | 23 | 91% | 47% | | D3P08 | 24 | 100% | 83% |
| D1P09 | 20 | 100% | 45% | | D3P09 | 18 | 77% | 77% |
| D1P10 | 20 | 100% | 75% | | D3P10 | 22 | 81% | 59% |
| D1P11 | 16 | 100% | 62% | | D3P11 | 22 | 100% | 86% |
| D2P01 | 18 | 100% | 27% | | D3P12 | 17 | 94% | 82% |
| D2P02 | 22 | 95% | 45% | | D3P13 | 24 | 100% | 62% |
| D2P03 | 21 | 100% | 38% | | D3P14 | 16 | 87% | 50% |
| D2P04 | 25 | 100% | 72% | | D3P15 | 29 | 100% | 37% |
| D2P05 | 23 | 95% | 30% | | D3P16 | 25 | 96% | 48% |
| D2P06 | 19 | 100% | 36% | | | | | |
| D2P07 | 15 | 100% | 46% | | | | | |
| D2P08 | 6 | 66% | 33% | | | | | |
| D2P09 | 13 | 76% | 23% | | | | | |

Every low score for ours was checked and the point was found in ours under other wording (for example
"destiny is pre-written but can be re-written", "अति दुःखी को तत्त्वज्ञान नहीं", the तन्मात्राएँ, "उतना ही मेरा
साथ था"). **No teaching was found that the other book has and ours lacks.**

## What the other book leaves out (checked by reading)

Examples, grouped. Each was looked for in the matching chapter of the other book and not found.

**Examples and stories**
- D1P05: cosmetic surgery gone wrong as a "wrong fight"; the Arjun "eating idli at the Udupi hotel" image
  (Gita 18.78); the court case kept going for thirty years (Gita 2.34); "destiny pre-written but can be
  re-written" with the one-germ advert (only partly).
- D1P06: Yudhishthira acted under the guru's guidance (नरो वा कुंजरो वा, Shikhandi), so why weep; the "eye
  disease" of not seeing God everywhere (वासुदेवः सर्वम्); Shiva's third eye image.
- D1P09: the doctor/testimonial analogy; Shankaracharya's कनकधारा स्तोत्र and सौंदर्य लहरी.
- D1P10: "उसकी कमीज़ मेरी कमीज़ से ज़्यादा सफ़ेद" ending in the कफ़न line.
- D2P03: age and फलश्रुति (the bank manager's scam at 57); the "flirt" label at 25; वाल्या to वाल्मीकि;
  youth addiction and looking old at 40.
- D2P05: mothers making children mimic an old granny; film stars retiring at 30–40; shlok 14's "two
  wolves" with the daughter-in-law's treatment; "कहीं कुछ गया नहीं" and the मृत्यु की साधना.
- D2P06: "पण काय वाढलं?" (what grew besides age); the person divorced three times; kings and billionaires
  also age.
- D3P01: the picnic image in detail (the job "was never yours", hotel staff, "३०००%"); business and
  marriage without counting the कर्तव्य.
- D3P04: pets and working animals as past-life humans; the rich running after उपाय (IVF) versus "children
  are God's gift"; the four things needed to change भाग्य (योजना, "If wishes were horses").
- D3P05: Durga Saptashati, लक्ष्मी and अलक्ष्मी; packing food to the rooms.
- D3P06: the photo garland and Radha-Krishna; the bus incident; "the results are known but means are not".
- D3P13: deaths despite the best doctors, ICU, vaccines; the exhalation exercise and corona.
- D3P15: ब्रह्म चरति इति ब्रह्मचारी; the parents' debt (wheelchair, adult diapers, वृद्धाश्रम); "minus 1000
  to minus 800".
- D3P16: the final six-point summary of the 59 shlokas (only partly); the closing call to wake from sadness.

**Asides and personal or institutional remarks** (mostly left out by the other book)
- D1P02: "एक हाथ में माला, दूसरे हाथ में भाला" and "सनातन धर्म, जागो".
- D1P07: Pakistan, Bangladesh and Afghanistan losing पूजा with the border; lying when the guru says so.
- D1P09: Antar Yog cannot run only on donations; learning श्री विद्या to teach wealth.
- D2P01: becoming विश्वगुरु (feeling what happens in Israel as one's own).
- D2P04: his own temple crowds, no VIP entry ("if he were PM or CM").
- D3P15: "first see God in the guru".

Many of these are the editorial items already listed in `edit_log.md` and `book_plan.md` for a human
decision. The other book's omissions may partly be deliberate editing. The examples and stories,
though, are teaching material, and leaving them out makes the book thinner, not only safer.

**Shlokas.** The other book prints the Sanskrit of 21 shlokas (1–7, 10–12, 18, 19, 24, 28–30, 35, 36,
47–50, 52) and gives the other 38 only as meaning or not at all. Of the 21, about half have small errors
copied from the raw transcript's typing, for example:

| Shloka | Other book | Gita Press |
|---|---|---|
| 1 | प्राणानभ्युत्सिसृक्षत (no visarga) | प्राणानभ्युत्सिसृक्षतः |
| 28 | अकिंचनाश्च … समृद्धे च **कुल** जाता … पतंगवत् | अकिञ्चनाश्च … समृद्धे च **कुले** जाता … पतंगवत् |
| 29 | काष्ठान्यपि **ही** जीर्यन्ते | काष्ठान्यपि **हि** जीर्यन्ते |
| 30 | अहमेतत करो**मिति** … यद् यदिष्टमसंतोषाद दुरात्मा **पाप्माछरेत** | अहमेतत् करो**मीति** … दुरात्मा **पापमाचरेत्** |
| 48 | **दातरो** यज्ञशीलाश्च न तरन्ति **जरांतकौ** | **दातारो** यज्ञशीलाश्च न तरन्ति **जरान्तकौ** |

Its source lines are general, e.g. "(महाभारत, शांति पर्व, अश्मा गीता)", without the shloka number.

## What the other book adds (not in the transcript)

Little. Most of its paragraphs that look unfamiliar turned out to be close paraphrases of the transcript
in more Sanskritised Hindi.
- **Chapter 18 (D2P08):** tells the story from the *Upanishad Ganga* video (the king with several queens).
  This is grounded: Acharya Ji comments on that story in the transcript. But the details of the story
  come from the video, which is not in the transcript, and the chapter does not say so.
- **Chapter 19 (D2P09):** the session is a quick round of participants' answers that he accepts or
  corrects. The other book writes those answers as connected teaching. Our chapter 19 also uses this
  session, as his recap.
- **Small embellishments:** for example the name शुद्धोधन (Buddha's father), which is not in the
  transcript, and phrases like "प्रसिद्ध उद्यमी" for the bankrupt businessman of the interview.

## What ours adds (not in the transcript)

- The Sanskrit of the 31 shlokas that were not recited, and the full text of the ones read in part,
  from Gita Press (marked by their source lines).
- In five verse blocks (shlokas 22, 25, 39, 41, 43), the Hindi meaning is the Gita Press translation,
  because the slide meaning was partial.
- Front and back matter written in the edit step (समर्पण, आभार, लेखक परिचय, भूमिका, पाठ के विषय में). These
  describe the book; they should be checked by a person before printing.

No added teachings, stories or quotes were found.

## Found while checking: three verse errors in ours came from our own cleaning step

The raw transcripts (typed by volunteers from the slides) have the **Gita Press readings** for shlokas
10, 30 and 51. Our cleaning step changed them, and the book inherited the change:

| Shloka | Raw transcript | Cleaned transcript and our book | Gita Press |
|---|---|---|---|
| 10 | ये च विंशतिवर्षा **वा** | विंशतिवर्षा **वै** | **वा** |
| 30 | मन्यते काल**नोदित**: | काल**चोदितः** | काल**नोदितः** |
| 51 | पथि **संगमम**भ्येति | पथि **सङ्गतम**भ्येति | **संगमम्** |

So these three are not slide readings, as `verse_differences.md` first suggested; they are errors
introduced when the transcript was cleaned. The other book, made from the raw transcript, has the right
reading for 30. Shloka 21 is different: the raw transcript has no Sanskrit for it, and the fragments
(…भवन्त्युत) are what he said aloud.

The same cleaning step also fixed real typing errors in the raw verses (कुल → कुले, ही → हि,
पाप्माछरेत → पापमाचरेत्), which is why ours does not have the errors listed above for the other book.

## Recommendations

1. Correct shlokas 10, 30 and 51 in ours to the Gita Press reading (it is also the transcript's), and
   give shloka 21 its full Gita Press text.
2. In the `/book` pipeline, the cleaning prompt should keep scripture exactly as in the raw transcript
   and only flag suspected errors, not change verses from memory.
3. If the other book is used further: remove the citation numbers, em dashes and "。" characters, add
   the missing 38 shlokas, and fix the verse typos above.
4. Decide, as a person, which of the asides and institutional remarks listed above belong in the
   printed book. Ours keeps them; the other book mostly drops them.

## Resolved in v5

Version 5 (`book/ashma_gita_05.*`, chapters before it in `chapters_v4/`) uses the Gita Press reading for
shlokas 10 (वा), 30 (कालनोदितः) and 51 (संगममभ्येति), and the full Gita Press text of shloka 21. The cleaning
prompt `tools/prompts/book/01_clean_transcript.txt` now keeps verse wording as given and only fixes form.
