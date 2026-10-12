---
name: review_blog
description: Review one talk's blog (output/<name>/<name>_blog.txt and _blog_en.txt) as an expert Sanskrit and scripture reviewer, following tools/prompts/sanskrit_review.txt (Gita Press as the authority), and save the report to tools/review/<name>.md. Review only; the blog is not edited.
argument-hint: <talk name>
model: claude-opus-5-5
effort: medium
---

# Review a blog's Sanskrit and scripture content

This command runs on Claude Opus 5.5 at medium effort (the `model` and `effort` fields above).

Talk: `$ARGUMENTS`.

1. Read `tools/prompts/sanskrit_review.txt` and follow it exactly.
2. Read the Hindi blog `output/<name>/<name>_blog.txt`, then the English blog
   `output/<name>/<name>_blog_en.txt`.
3. Write the review to `tools/review/<name>.md`, in the prompt's output format: the first line
   is `<name>: No issues`, `<name>: Minor issues` or `<name>: Needs correction`, then the
   numbered issues, then what was checked and correct, then what could not be verified.
   Write the talk name in the first line exactly as given, without escaping underscores
   (`women_have_right`, not `women\_have\_right`); the batch script checks this line.

Rules:
- Do not edit the blog texts, the pages or any other file; write only the review file.
- Never guess a verse, reference or meaning. Mark anything you cannot verify as "Unverified".
- A blog with no verses is still reviewed for terms, claims, consistency and sensitivity.

Reply with one line: the verdict and the number of issues by severity (Critical / Major / Minor).
