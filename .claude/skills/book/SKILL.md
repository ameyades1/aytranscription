---
name: book
description: Make a Hindi book from a multi-day Shibir (many recorded sessions) in books/<book>/, using the prompts in tools/prompts/book/ and the runner tools/book/book.sh. Steps - convert or clean the transcripts, digest each session, plan the chapters, write and review each chapter, check verses, edit the whole book, build a PDF - each resumable, with a report of content, length against the source, review changes and corrections in reports/book_report.md.
argument-hint: <book> [step] [chapter numbers...]
---

# Shibir → Hindi book

Arguments: `$ARGUMENTS`. The first is the book's folder name under `books/`; the optional second is a
single step to run (otherwise run from the first unfinished step); any further arguments are
chapter numbers for the `write` step.

The book is Hindi only. An English edition is translated later from the finished Hindi book.

## The book folder

`books/<book>/` must contain:

- `book.json`:
  ```json
  {"book": "Ashma Gita (Mahabharata, Shanti Parva)", "place": "near Jagannath Puri, Odisha",
   "author": "आचार्य उपेन्द्र जी", "title": "", "subtitle": "", "parts": {}}
  ```
  `book` and `place` are filled into the prompts; the plan step fills `title`, `subtitle` and `parts`.
  If it is missing, write it yourself from the folder name, the transcript file names and this
  example (the author is आचार्य उपेन्द्र जी), and tell the user what you used. Do not ask.
- The source, one of:
  - `transcript/`: human-typed `.docx` files, one per session, with day and part in the path
    (`Day01/... Day 01 Part 03.docx`);
  - `raw/DayNN_PartNN.txt`: machine transcripts. Get them per session with
    `python3 tools/fetch_yt_transcript.py "<url>" <name>` or `tools/transcribe.sh <audio> <name>`
    and save each as `raw/DayNN_PartNN.txt`.

Everything else is generated.

## Steps

Run each with `tools/book/book.sh <book> <step>` from the repo root. Long steps go in the
background (`run_in_background`), and you wait for the notification; do not poll. Every step skips
finished outputs, so re-running continues where it stopped. Usage-limit waits do not count as
failures. Logs: `tools/batch_logs/book/<book>/`.

| Step | Prompt | Output | Before moving on |
|---|---|---|---|
| `text` | none | `raw/` from `transcript/*.docx` | Session count matches the recordings. Skip if `raw/` came from audio. |
| `clean` | `01_clean_transcript.txt` | `text_clean/` | Spot-check one session: verses restored, English in Latin script, slides marked `[स्लाइड]`, nothing summarised. `CLEAN=copy` skips the prompt and copies `raw/` as-is. |
| `digest` | `02_digest_part.txt` | `digests/` | Every session has a digest. |
| `plan` | `03_book_plan.txt` | `book_plan.md`, `chapters.txt`, `book.json` | Check every session appears in `chapters.txt`, then go straight on to `write`; the user reviews the whole book at the end, not the plan. |
| `write` | `04_write_chapter.txt`, then `05_review_chapter.txt` | `drafts/NN_chapter.txt` (before review), `chapters/NN_chapter.txt` (after), `stretch/NN.json`, `reviews/NN_review.md` and `.json` | Read `reports/book_report.md` (built at the end of the step). `chapters/` fills before review, so count progress by `reviews/*.json`. Most flags are mechanical (length a little over 95%, loanwords counted as Urdu); re-run a chapter only for a real problem (under 65% of source, or a failed or missing review) by deleting its `drafts/`, `chapters/`, `stretch/` and `reviews/` files. List the rest in the summary. |
| `verses` | `06_verify_verses.txt` | `verses_report.md`, `.json`; certain fixes applied | Keep the "needs human check" list for the end-of-book summary and go on. |
| `edit` | `07_edit_book.txt` | edited chapters (originals kept in `chapters_before_edit/`), `front_matter.txt`, `back_matter.txt`, `edit_log.md` | The editorial items (personal remarks, institutional points, health remarks) are left for the user; list them in the end-of-book summary and go on. |
| `report` | none | `reports/book_report.md`, `reports/chapters.json`, `reports/changes/NN_review.diff` | Run any time. |
| `pdf` | none | `book/<book>.html`, `book/<book>.pdf` | Uses `book.json` for the cover and Part pages; includes front and back matter if present. |

Settings: `MODEL` (default `claude-opus-5-5`), `EFFORT` (default `low`), `JOBS` (parallel runs,
default 5), `LIMIT_WAIT`, `MAX_TRIES`, `CLEAN`.

Requirements: the `claude` CLI, `python3` (standard library only), `google-chrome` (headless,
for `pdf`) and the Noto Serif Devanagari font (`fc-list | grep "Noto Serif Devanagari"`).

## Repeatability

Every step appends a record to `books/<book>/run.json`: step, arguments and time; every setting
(model, effort, jobs, limit wait, tries, clean mode, allowed tools, permission mode); the claude CLI,
python, chrome, OS and font versions; the repo commit and whether the pipeline files had uncommitted
changes; a hash of every prompt, script and this skill; and hashes of the inputs (`book.json`,
`transcript/`, `raw/`, `text_clean/`). Commit `run.json` and `book.json` with the book. Commit
the prompts, scripts and this skill before a run so the commit identifies them. The same settings
give the same files, structure and checks; the wording, title and chapter boundaries come from the
model and differ between runs. To keep a book exactly, keep its generated files: steps skip
finished outputs, so a re-run never overwrites them, and only the files you delete are redone.

## Files in `books/<book>/`

| File | Made by | Contents |
|---|---|---|
| `book.json` | you, then `plan` | `book`, `place`, `author`; `plan` adds `title`, `subtitle` (Hindi) and `parts` (first chapter number as a string → Hindi Part title, e.g. `"7": "भाग २: ..."`) |
| `run.json` | every step | list of run records (see Repeatability) |
| `transcript/DayNN/*.docx` | source | human-typed sessions |
| `raw/DayNN_PartNN.txt` | `text`, or you | plain text per session |
| `text_clean/DayNN_PartNN.txt` | `clean` | faithful Hindi transcript: first line `Day N, Part N`; `[स्लाइड]` slide lines, `[व्यवस्था]` logistics, speakers labelled; ends with a `--- टिप्पणियाँ:` notes block |
| `digests/DayNN_PartNN.md` | `digest` | English digest with positions; sections as in prompt 02 |
| `book_plan.md` | `plan` | sections 1 Header, 2 Chapter table (one per Part), 3 Shared terms, 4 Repeated material, 5 Material for editorial review, 6 Known gaps, 7 Next steps |
| `chapters.txt` | `plan` | `#` header line, then one line per chapter: number, then its sessions in order (`4  Day01_Part03 Day01_Part04`) |
| `drafts/NN_chapter.txt` | `write` | chapter before review |
| `chapters/NN_chapter.txt` | `write`, then `verses` and `edit` | final chapter: `# अध्याय N: title`, 5 to 8 `##` sections, `>` verse blocks (bold Sanskrit, meaning, source line) |
| `stretch/NN.json` | `write` | per source stretch: part, first and last 8 to 12 words, or null for a session's start or end |
| `reviews/NN_review.md`, `.json` | `write` | review notes; counts per check and items left for a human |
| `verses_report.md`, `.json` | `verses` | every verse with status, corrections applied, "needs human check" list; `.json` totals |
| `chapters_before_edit/` | `edit` | chapters as they were before `edit` |
| `front_matter.txt` | `edit` | `#` title, `##` subtitle, author; `# समर्पण`, `# आभार`, `# लेखक परिचय` (placeholders); `# भूमिका` (600 to 1,000 words); `# पाठ के विषय में` (150 to 250 words); one `# भाग N: ...` page per Part |
| `back_matter.txt` | `edit` | `# शब्दावली` (Devanagari order, meaning, chapter) and `# श्लोक-सूची` (main-text verses in number order, then other texts grouped by text) |
| `edit_log.md` | `edit` | every change by chapter, enough to undo it; "Left for the human editor" |
| `reports/` | `write`, `report` | `book_report.md`, `chapters.json`, `changes/NN_review.diff` |
| `book/<book>.html`, `.pdf` | `pdf` | A5 book: cover, contents, front matter, Part pages, chapters, back matter, page numbers |

## The report

`reports/book_report.md` is the main way to judge the book. For each chapter:

- **Source words:** the transcript stretch the chapter was written from, measured from the
  boundaries the writer recorded in `stretch/NN.json`.
- **Draft / Final words** and **% of source**, against the 70 to 95 percent target (measured against the clean transcript,
  which has already lost its fillers). Below 65 percent suggests dropped content; above 100 suggests
  additions or repetition.
- **Review changed:** the share of words the review altered; the full diff is in
  `reports/changes/NN_review.diff`.
- **Corrections** applied by the review per check (completeness, faithfulness, verses, language,
  format) and items left for a human.
- **Urdu/Persian:** how many of the speaker's Urdu or Persian word uses the chapter kept (they should
  be kept), and any such words it added that are not in its source stretch (there should be none).
- **Checks:** sections (5 to 8), verse blocks, तू/तुम outside quotes, dashes,
  `###`, title format.

For the whole book: totals, and **coverage**: transcript words that no chapter's stretch includes,
per session, with each gap of 30 or more words quoted so it can be checked for dropped content.

## When reporting to the user

Run all the steps through to the PDF without stopping for the user's review; the user reviews
the whole finished book. Stop only for failures you cannot fix. At the end, give one summary with
the PDF path, the flagged chapters, coverage gaps, the verses needing a human check, and the
editorial items.


After each step, say in a few lines what was produced and what needs their attention: failed items,
flagged chapters (from the report), coverage gaps, and the next step. Give full paths. Never claim a
step finished without checking its outputs exist.

## Rules that apply throughout

From CLAUDE.md: never attribute to Acharya Ji a teaching, story or quote not in the transcript;
Gita Press is the authority for scripture; one `#` title, `##` sections only, no em dashes. The
prompts add: keep everything in the first draft (editorial cuts happen later, by a human); keep the
speaker's own Urdu and Persian words but add none (headings, titles and linking sentences are in
Hindi); a flowing literary register that never costs content; the reader is addressed as आप.
