# Book prompts: from recordings to a finished book

These prompts turn a multi-day Shibir, starting from audio only, into a Hindi book, in the style of the approved rewrite of chapter 1. They do not assume a human-typed transcript.

Run them with the `/book` skill or `tools/book/book.sh <book> <step>` (see `.claude/skills/book/SKILL.md`). Placeholders in `{BRACES}` are filled by the runner: `{BOOK}`, `{SESSION}`, `{N}`, `{NN}`, `{PARTS}`, `{DAYS}`, `{PLACE}`, `{N_SESSIONS}`, `{WORDS}`.

## The flow

| Step | Prompt | Runs | Input → output | Notes |
|---|---|---|---|---|
| 0 | none | once per session | audio or YouTube URL → `raw/DayNN_PartNN.txt` | `tools/fetch_yt_transcript.py` (YouTube captions) or `tools/transcribe.sh` (WhisperX) |
| 1 | `01_clean_transcript.txt` | once per session | `raw/` → `text_clean/DayNN_PartNN.txt` | Faithful clean transcript: punctuation, Hindi/English script, Sanskrit restored, slides and speakers marked, logistics marked but kept. No style changes. |
| 2 | `02_digest_part.txt` | once per session | `text_clean/` → `digests/DayNN_PartNN.md` | English digest with positions, used only for planning and finding material. |
| 3 | `03_book_plan.txt` | once | all `digests/` → `book_plan.md` | Chapters, boundaries, shlokas, shared terms, repeated material, editorial items, gaps. Also writes `chapters.txt` and fills `book.json`. |
| 4 | `04_write_chapter.txt` | once per chapter | plan + `text_clean/` parts → `chapters/NN_chapter.txt` (copied to `drafts/`), `stretch/NN.json` | Writes the Hindi chapter directly in final book style (the v3 style), keeping everything. Needs file tools. |
| 5 | `05_review_chapter.txt` | once per chapter | chapter + plan + transcript → `reviews/NN_review.md` and `.json`, chapter corrected in place | Completeness, faithfulness, verses, language, format; applies certain fixes. |
| 6 | `06_verify_verses.txt` | once | all chapters → `verses_report.md` and `.json`, corrected chapters | Every verse against Gita Press; uncertain ones listed for a human. |
| 7 | `07_edit_book.txt` | once | whole book → edited chapters, front and back matter, `edit_log.md` | Cross-chapter duplicates, continuity, introduction, glossary, verse index. |
| 8 | none | once | chapters + front/back matter → `book/<book>.html` and `.pdf` | `tools/book/build_pdf.py` |

Human review comes once, on the finished book: the flagged verses from step 6 (against the printed Gita Press edition) and the editorial items from the plan's section 5 (personal remarks, institutional points, health remarks). The plan is not reviewed before writing.

## Notes

- `chapters/NN_chapter.txt` appears as soon as a chapter is drafted, before its review; a chapter is finished when `reviews/NN_review.md` exists.
- Every step appends its settings, the repo commit and the prompt and script hashes to `books/<book>/run.json`.
- Steps 1 and 2 run once per session; 4 and 5 once per chapter; the rest once per book.
- The writer records its source stretch in `stretch/NN.json`, and the review writes `reviews/NN_review.json`, so `tools/book/book_report.py` can measure each chapter's length against its source and count the corrections.
- No English edition here. The English book is translated later from the finished Hindi book, with `tools/prompts/hindi_to_english.txt`.

If a single writing pass loses content on long chapters, write a faithful draft first (step 4 without its Step 3 style rules), then rewrite it in book style with step 4's language, structure and format rules applied to the draft.
