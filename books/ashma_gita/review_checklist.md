# अश्मा गीता: checklist for manual reviewers

**Book under review:** version 5, `book/ashma_gita_05.pdf` (357 pages, 35 chapters in 5 Parts).
The text is in `chapters/NN_chapter.txt`; make corrections there, not in the PDF.

## How to use this checklist

- **Split the work by Part** (भाग १–५); one reviewer per Part works well. Sections A–F apply to every
  chapter. Sections G and H are done once, for the whole book, by one person.
- **Record every finding** in the sheet at the end: chapter, page, the exact text, what is wrong, and
  what you suggest. Do not change the text silently; the editor applies the changes so they can be
  tracked and undone.
- **Mark each box** as you go: ✔ done and fine, ✎ found something (recorded), ? needs a decision.
- **When in doubt, check the source.** Every chapter says which sessions it comes from (see "Where to
  find things" below). The transcript wins over memory, and the Gita Press text wins for scripture.

## Where to find things

| What | File |
|---|---|
| Which sessions each chapter uses | `book_plan.md`, section 2 (chapter table, "Source" column) |
| The cleaned transcript of each session | `text_clean/DayNN_PartNN.txt` (notes on doubtful passages at the end, after `---`) |
| The original typed transcript | `raw/DayNN_PartNN.txt` |
| Teachings of each session, in order | `digests/DayNN_PartNN.md` |
| Material marked for an editorial decision | `book_plan.md`, section 5 |
| Known gaps in the recordings | `book_plan.md`, section 6 |
| What the edit step changed | `edit_log.md` |
| Gita Press Ashma Gita (Shanti Parva, adhyaya 28) | `../../references/mahabharata_gita_press_khand5_shanti_parva.pdf`, PDF pages 178–186 |
| Gita Press Bhagavad Gita (Sadhak-Sanjivani) | `../../references/shrimad_bhagavad_gita.pdf` |
| Verse history and differences | `missing_shlokas.md`, `verse_differences.md`, `verses_report.md` |

## Ground rules

- Nothing may be attributed to Acharya Ji that is not in the transcript: no teaching, story, example
  or quote.
- Gita Press, Gorakhpur is the authority for scripture.
- Acharya Ji's facts and interpretations are not "corrected" in the text. Where one looks wrong, record
  it (section D); the decision is the editor's.
- Format: one `#` title per chapter, `##` sections only (no `###`), no em dashes (—). In English, शिविर is
  "Shibir".

---

## A. Faithful to the transcript (every chapter)

Read the chapter next to its session digest(s), and dip into the transcript wherever something looks
doubtful.

- [ ] Every main teaching in the digest for this chapter's part of the session is in the chapter.
- [ ] The examples and stories are there and told as he told them (who, what happened, the point he
      drew).
- [ ] Nothing has been added: no explanation, example, quote or conclusion he did not give.
- [ ] Meaning is not changed: no softening, sharpening or reversal of what he said; conditions and
      exceptions are kept ("गुरु से पूछकर", "अपनी मर्ज़ी से नहीं").
- [ ] Slide text is distinguished from his own words where it matters (a slide's meaning of a shlok vs.
      his commentary).
- [ ] Participants' words are not presented as his (recap rounds in ch. 12 and ch. 19).
- [ ] Where the recording is cut or unclear (`book_plan.md`, section 6), the chapter does not fill the
      gap with invented text.
- [ ] Ch. 32 only: it comes from a sadhak's handwritten notes (Day 3 Part 13), not a recording. Check it
      reads as his teaching without inventing detail.

## B. Scripture and verses (every chapter)

Every verse is a `>` block: Sanskrit in bold, then the Hindi meaning, then a source line in brackets.

- [ ] Each Ashma Gita block matches the Gita Press text (PDF pages 178–186) letter by letter, including
      visarga, anusvara, halant and ऽ. All 59 shlokas are now in the book.
- [ ] Each source line has the right shlok number, and shlokas 25 and 26 show "२५-२५½" and "२६-२६½".
- [ ] Each Bhagavad Gita verse matches Gita Press, and the chapter.verse number is right.
- [ ] The Hindi meaning in each block fits its verse. For shlokas 22, 25, 39, 41 and 43 the meaning is
      the Gita Press translation; elsewhere it is the slide's meaning as he read it.
- [ ] Inline Sanskrit words and phrases (not in blocks) are spelt correctly.
- [ ] Open verse questions (decide and record):
  - [ ] Ch. 35: the closing पुष्पिका. The book has "…व्यासवाक्ये अश्मगीता सम्पूर्णा"; Gita Press ends the
        adhyaya with "इति श्रीमहाभारते शान्तिपर्वणि राजधर्मानुशासनपर्वणि व्यासवाक्येऽष्टाविंशोऽध्यायः ॥२८॥"
        (PDF page 186). Choose one.
  - [ ] Ch. 11, 15, 17: Chanakya Niti verses and numbers (4.1, 13.13, 15.6, 17.18; "अधः पश्यसि किं
        वृद्धे" vs "बाले"). Gita Press has no standard Chanakya Niti: choose one edition and cite it.
  - [ ] Ch. 2: Gita 8.15, his sandhi reading of "दुःखालयमशाश्वतम्".
  - [ ] Ch. 10: his reading of Gita 3.25–3.26.
  - [ ] Ch. 14: Gita 9.21 (he said 9.20).
  - [ ] Ch. 20: the garbled Brihadaranyaka verse; "जन हिताय स्वयं मोक्षाय" (a misquoted motto).
  - [ ] Ch. 23: Gita ch. 16 or 14 for birth in तमोगुण (he was unsure which).
- Already settled, no need to recheck unless something looks wrong: Ashma Gita shlokas 14, 15, 21
  and 23, and 10, 30 and 51 (all now Gita Press); the shlok numbering (the slides' numbers match Gita
  Press).

## C. Editorial decisions (every chapter)

`book_plan.md`, section 5 lists, chapter by chapter, passages that may not belong in a printed book.
The edit step kept all of them. For each item in your chapters, record **keep**, **soften** (suggest
wording) or **remove**, and a one-line reason. Pay most attention to these kinds:

- [ ] **Highly sensitive:** rape and ऋणानुबंध (ch. 30); "कुछ धर्मों के लोग" with many children (ch. 23);
      remarks on other religions (ch. 9, 11, 12, 34).
- [ ] **Health and medical claims** a reader might act on: vaccines, Covid and the breathing exercise,
      insulin, dialysis, cancer, longevity (ch. 15, 17, 22, 25, 28, 32, 33).
- [ ] **Political remarks:** Pakistan, Bangladesh, Afghanistan (ch. 8); politicians, Trump (ch. 14, 16,
      23, 26).
- [ ] **Identifiable people:** participants, family members, a named astrologer (ch. 6, 12, 28, 30).
- [ ] **Institutional and fundraising** passages: Antar Yog's finances, programmes, courses (ch. 1, 10,
      26, 32, 34).
- [ ] **Self-praise and guru claims** (ch. 5, 16, 18, 25, 35).
- [ ] **Jokes about wives, marriage and gender roles** (ch. 2, 5, 6, 8, 16, 29).
- [ ] **Corporal punishment of children** (ch. 6, 21, 34) and the unsafe wet-feet electricity joke
      (ch. 31).

## D. Factual slips to decide (record, do not fix in the text)

These are his words, kept as spoken. For each, decide: leave as is, add a short note, or reword.

- [ ] Ch. 19: Chitraketu is called "a boy who dies as soon as he is born"; in the Bhagavata, Chitraketu
      is the king and his son dies.
- [ ] Ch. 28: Sthulibhadra and Pingala are run together.
- [ ] Ch. 17: Vivekananda's "31 diseases" and death at 39.
- [ ] Ch. 29: he says "river" where the shlok (36) and slide say "ocean" (महोदधि).
- [ ] Ch. 35: Krishna's three-chapter Narada story told to Yudhishthira (check against the Mahabharata).
- [ ] Ch. 5: "प्रपौत्र" (Janamejaya's relation to Arjuna); "six characters" with fewer named; the 28th
      Vyasa.
- [ ] Any other dates, numbers or names that look wrong (record them).

## E. Language and style (every chapter)

- [ ] Clear, natural written Hindi; no leftover spoken filler ("ठीक है?", "बराबर?", "समझ में आया?") unless
      it carries meaning.
- [ ] No session or day markers left ("कल", "आज के सत्र में") where they no longer make sense in a book.
- [ ] English words: kept only where natural or meaningful, and written consistently (Devanagari, with
      the English in brackets where helpful).
- [ ] Terms spelt the same throughout: शिविर, ऋणानुबंध, दुःख, तत्त्व, अंतर योग, श्री विद्या, युधिष्ठिर,
      जनमेजय, वैशम्पायन, मार्कण्डेय (the plan's "Shared terms", section 3).
- [ ] Bold is used only for his key sayings, not for whole paragraphs.
- [ ] No em dashes (—); no `###` headings; sentences not over-long.
- [ ] Grammar, gender and number agreement, spelling, punctuation (। ? ! , " ").

## F. Structure and flow (every chapter)

- [ ] The chapter title fits the content and differs from the other titles.
- [ ] The opening paragraph sets up the chapter; the last paragraph closes it (not cut mid-thought).
- [ ] Section headings (`##`) describe their sections.
- [ ] Each verse comes right after the sentence that introduces it, and the explanation follows it (the
      v4 rearrangement of the 31 added shlokas: check it reads smoothly).
- [ ] No passage repeats something told in an earlier chapter without a reason (a new example or
      angle is a reason).
- [ ] References to other chapters ("अध्याय १९ में हमने देखा") point to the right chapter.
- [ ] Known order questions (decide): ch. 18 has the Day 3 restart before the Chitraketu chapter it
      refers to; ch. 12 sits in Part 2 but opens Day 2.

## G. Front and back matter (once)

- [ ] समर्पण, आभार, लेखक परिचय, भूमिका, पाठ के विषय में: every fact about Acharya Ji, the Foundation, the
      Shibir (place, dates, number of sessions) is correct and approved.
- [ ] The cover: title, subtitle and author name as approved.
- [ ] The table of contents (विषय-सूची) matches the chapter and Part titles.
- [ ] Back matter, if any, is complete and approved.

## H. Final proof of the PDF and EPUB (once, after all changes)

- [ ] Every Devanagari conjunct and vowel sign renders correctly (look closely at Sanskrit blocks).
- [ ] No verse block is split across pages; no heading is left alone at the bottom of a page.
- [ ] Page numbers are right, and the table of contents links and page order match.
- [ ] Each chapter starts on a new page; Part pages are in place.
- [ ] The EPUB opens in a reader app, its contents list works, and a read-aloud app reads a sample
      page correctly (the PDF's text layer is not usable for read-aloud).
- [ ] For print: trim size, margins, chapters on right-hand pages, running heads and cover spine are
      agreed with the printer.

---

## Findings sheet

Copy this table into a spreadsheet or keep it here, one row per finding.

| # | Reviewer | Ch. | PDF page | Section (A–H) | Text (exact, a few words) | Problem | Suggestion | Decision (editor) |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |

## Sign-off

| Part | Chapters | Reviewer | Date done | Open questions |
|---|---|---|---|---|
| भाग १ | 1–6 | | | |
| भाग २ | 7–12 | | | |
| भाग ३ | 13–19 | | | |
| भाग ४ | 20–28 | | | |
| भाग ५ | 29–35 | | | |
| Front/back matter, final proof | all | | | |
