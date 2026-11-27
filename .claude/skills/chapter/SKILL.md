---
name: chapter
description: Turn a spiritual discourse (local audio file, YouTube URL, or existing raw transcript .txt) into a book chapter in Hindi and English, output/<name>/<name>_chapter.txt and _chapter_en.txt. The chapter follows tools/prompts/transcript_to_chapter.txt and the English version tools/prompts/hindi_to_english.txt. Reuses the talk's transcripts when /blog has already made them. No blog (that is /blog).
argument-hint: <audio.mp3 | youtube_url | raw_transcript.txt | talk name> [name]
model: claude-opus-5-5
effort: low
---

# Discourse → book chapter

This command runs on Claude Opus 5.5 at low effort (set in the `model` and `effort` fields
above), whichever model and effort the session uses. Change those two fields to change it.

Arguments: `$ARGUMENTS`. The first is the input; the optional second is the output name.
If the first is the name of an existing talk folder (`output/<name>/` with a raw or clean
transcript), use that talk. Otherwise, if no name is given, use the input's file name without
extension and without a trailing `_raw_transcript` (for a YouTube URL, ask the user for a short
snake_case name).

All paths are relative to the repo root. Files, all in `output/<name>/`:

| File | Content |
|------|---------|
| `<name>_raw_transcript.txt` | YouTube transcript or WhisperX output, untouched (shared with `/blog`) |
| `<name>_clean.txt` | Cleaned transcript (shared with `/blog`) |
| `<name>_chapter.txt` / `_chapter_en.txt` | Book chapter (prompt `tools/prompts/transcript_to_chapter.txt`), Hindi; English via `tools/prompts/hindi_to_english.txt` |

This skill touches no blog file and no page.

## Step 1: Get the raw transcript

Read `tools/prompts/get_transcript.md` and follow it. When `/blog` has already run for the talk,
both transcripts are there and are reused.

## Step 2: Clean the transcript

Unless `output/<name>/<name>_clean.txt` already exists, read `tools/prompts/clean_transcript.txt`
and follow it with the raw transcript, and write the result to `output/<name>/<name>_clean.txt`.

## Step 3: Write the Hindi chapter

Read `tools/prompts/transcript_to_chapter.txt` and follow it, with the cleaned transcript as the
transcript it refers to. Write the result to `output/<name>/<name>_chapter.txt`. The prompt
decides content, tone and style; the format below decides the layout.

## Step 4: Write the English chapter

Read `tools/prompts/hindi_to_english.txt` and follow it to translate the Hindi chapter into
`output/<name>/<name>_chapter_en.txt`. Same title, sections, order and quotes; add nothing that
is not in the Hindi. Where the prompt and this skill differ, this skill's format wins.

## Format for both texts

- Title line `# अध्याय: <Title>` in Hindi, `# Chapter: <Title>` in English
- `## <Section heading>` only: no subheadings (`###`)
- Quotes of Acharya Ji's words, where used: `> "..."` lines, faithful to the transcript
- Scripture verses: a `>` block whose first line is `**bold**` (Devanagari in Hindi, IAST in
  English; the English block also has the quoted meaning), ending with the reference in
  parentheses as its own line, e.g. `> (श्रीमद्भगवद्गीता १८.६६)` / `> (Bhagavad Gita 18.66)`
- `- ` for bullet lists; `१. ` / `1. ` for numbered lists
- `**bold**` for key ideas, `*text*` for emphasis
- No em dashes (—)

## Step 5: Report

List the two chapter files, the transcript source (or that existing transcripts were reused), and
anything in the transcript that was unclear or that you had to interpret.
