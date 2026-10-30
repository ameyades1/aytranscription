#!/usr/bin/env python3
"""Write a book's progress and quality report: reports/book_report.md and reports/chapters.json.

Usage: python3 book_report.py books/<book>

For every chapter it measures, from the files the book steps leave behind:
- content: the transcript stretch it was written from (stretch/NN.json), its word count, and the
  chapter's word count as a percentage of it (target 65 to 85 percent);
- changes: what the review step changed (drafts/NN_chapter.txt against chapters/NN_chapter.txt),
  saved as a diff in reports/changes/NN_review.diff;
- review: corrections applied per check and left for a human (reviews/NN_review.json);
- checks: sections, verse blocks, तू/तुम outside quotes, dashes, headings;
- Urdu/Persian words: the speaker's are kept, so it reports how many of his uses the chapter kept,
  and flags only words the chapter added (not used anywhere in its source stretch).
For the whole book it adds coverage: transcript text that no chapter's stretch includes.
"""
import difflib
import json
import re
import sys
from pathlib import Path

TARGET = (70, 95)          # chapter words as percent of its clean-transcript source stretch
SECTIONS = (5, 8)
# Urdu/Persian nukta letters (qa, kha, gha, za, fa, yya), precomposed or as letter + nukta sign.
# The Hindi letters U+095C and U+095D (retroflex ra, rha) are not matched.
NUKTA = re.compile("[\u0958\u0959\u095A\u095B\u095E\u095F]|[\u0915\u0916\u0917\u091C\u092B\u092F]\u093C")
URDU = set("""मंजिल मंज़िल जिंदगी ज़िंदगी दुनिया वक्त वक़्त साल हमेशा सिर्फ सिर्फ़ ज्यादा ज़्यादा कोशिश
मुश्किल आसान फायदा फ़ायदा नुकसान नुक़सान फर्क फ़र्क़ हक हक़ हिस्सा सजा सज़ा जेल शादी तलाक तलाक़ खराब
ख़राब खुशी ख़ुशी गम ग़म दर्द दिमाग दिमाग़ इंसान आदमी किस्मत क़िस्मत असर इस्तेमाल जरूरी ज़रूरी जरूर ज़रूर
बिल्कुल शुरू खत्म ख़त्म रास्ता तरीका तरीक़ा मजा मज़ा यानी लेकिन अगर सरकार दवा बाकी बाक़ी""".split())
TU = set("तू तुम तुझे तुझको तेरा तेरी तेरे तुम्हें तुम्हारा तुम्हारी तुम्हारे तुमको".split())
PUNCT = "।॥,.;:!?\"'“”‘’()[]{}-–—…"


def urdu_words(text):
    """Counter of Urdu/Persian words in text, keyed without the nukta so spellings match."""
    from collections import Counter
    out = Counter()
    import unicodedata
    for t in (norm(x) for x in text.split()):
        if t in URDU or NUKTA.search(t):
            # NFD splits precomposed nukta letters (ख़ -> ख + nukta), so ख़र्च and खर्च match
            out[unicodedata.normalize("NFD", t).replace("\u093c", "")] += 1
    return out


def words(text):
    return len(text.split())


def norm(token):
    return token.strip(PUNCT)


def find(tokens, phrase, start=0):
    """Index of the first token of phrase in tokens at or after start, ignoring punctuation."""
    want = [norm(t) for t in phrase.split() if norm(t)]
    if not want:
        return None
    have = [norm(t) for t in tokens]
    for i in range(start, len(have) - len(want) + 1):
        if have[i:i + len(want)] == want:
            return i
    # fall back to the first five words, for phrases copied with small differences
    if len(want) > 5:
        return find(tokens, " ".join(want[:5]), start)
    return None


def stretch_ranges(book, nn):
    """[(part, first_token, last_token_exclusive, exact)] for one chapter, or None."""
    path = book / "stretch" / ("%s.json" % nn)
    if not path.exists():
        return None
    try:
        entries = json.loads(path.read_text(encoding="utf-8"))["parts"]
    except (ValueError, KeyError):
        return None
    ranges = []
    for entry in entries:
        src = book / "text_clean" / ("%s.txt" % entry["part"])
        if not src.exists():
            continue
        tokens = src.read_text(encoding="utf-8").split()
        exact = True
        first = 0
        if entry.get("start"):
            found = find(tokens, entry["start"])
            exact &= found is not None
            first = found or 0
        last = len(tokens)
        if entry.get("end"):
            found = find(tokens, entry["end"], first)
            exact &= found is not None
            if found is not None:
                last = found + len(entry["end"].split())
        ranges.append((entry["part"], first, min(last, len(tokens)), exact))
    return ranges


def stretch_text(book, ranges):
    parts = []
    for part, first, last, _ in ranges:
        tokens = (book / "text_clean" / ("%s.txt" % part)).read_text(encoding="utf-8").split()
        parts.append(" ".join(tokens[first:last]))
    return "\n".join(parts)


def outside_quotes(text):
    """Running text only: no verse or quote blocks, no quoted speech."""
    lines = [l for l in text.splitlines() if not l.startswith(">") and not l.startswith("#")]
    body = "\n".join(lines)
    return re.sub(r"[\"“][^\"”]*[\"”]", " ", body)


def checks(text):
    running = outside_quotes(text)
    tokens = [norm(t) for t in running.split()]
    return {
        "title_ok": bool(re.match(r"^# अध्याय [०-९]+: \S", text)),
        "sections": len(re.findall(r"^## ", text, re.M)),
        "h3": len(re.findall(r"^### ", text, re.M)),
        "verse_blocks": len(re.findall(r"^> \*\*.+\n(?!> \*\*)", text, re.M)),
        "dashes": text.count("—") + text.count(" – "),
        "tu_tum": sum(1 for t in tokens if t in TU),
    }


def review_counts(book, nn):
    path = book / "reviews" / ("%s_review.json" % nn)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except ValueError:
        return None


def change_summary(before, after, out):
    a, b = before.splitlines(), after.splitlines()
    diff = list(difflib.unified_diff(a, b, "before review", "after review", lineterm="", n=0))
    out.write_text("\n".join(diff) + "\n", encoding="utf-8")
    changed = sum(1 for l in diff if l[:1] in "+-" and l[:3] not in ("+++", "---"))
    ratio = difflib.SequenceMatcher(None, before.split(), after.split(), autojunk=False).ratio()
    return {"diff_lines": changed, "words_changed_pct": round(100 * (1 - ratio), 1)}


def chapter_rows(book):
    plan = (book / "chapters.txt").read_text(encoding="utf-8") if (book / "chapters.txt").exists() else ""
    numbers = [int(l.split()[0]) for l in plan.splitlines() if l.strip() and l.split()[0].isdigit()]
    rows, covered = [], {}
    (book / "reports" / "changes").mkdir(parents=True, exist_ok=True)
    for n in numbers:
        nn = "%02d" % n
        row = {"chapter": n, "status": "not written"}
        final = book / "chapters" / ("%s_chapter.txt" % nn)
        draft = book / "drafts" / ("%s_chapter.txt" % nn)
        if final.exists():
            text = final.read_text(encoding="utf-8")
            title = text.splitlines()[0].lstrip("# ").strip() if text.strip() else ""
            row.update(status="reviewed" if review_counts(book, nn) else "written",
                       title=title, words=words(text), **checks(text))
            ranges = stretch_ranges(book, nn)
            if ranges:
                src_words = sum(last - first for _, first, last, _ in ranges)
                row["source"] = ["%s %d-%d" % (p, f, l) for p, f, l, _ in ranges]
                row["source_words"] = src_words
                row["source_exact"] = all(e for *_, e in ranges)
                row["pct"] = round(100 * row["words"] / src_words, 1) if src_words else None
                for part, first, last, _ in ranges:
                    covered.setdefault(part, []).append((first, last, n))
                spoken = urdu_words(stretch_text(book, ranges))
                written = urdu_words(outside_quotes(text))
                row["urdu_speaker"] = sum(spoken.values())
                row["urdu_kept"] = sum(min(written[w], c) for w, c in spoken.items())
                import unicodedata
                src_tokens = {unicodedata.normalize("NFD", norm(t)).replace("\u093c", "")
                              for t in stretch_text(book, ranges).split()}
                row["urdu_added"] = sorted(w for w in written if w not in src_tokens)
            if draft.exists():
                d = draft.read_text(encoding="utf-8")
                row["draft_words"] = words(d)
                row.update(change_summary(d, text, book / "reports" / "changes" / ("%s_review.diff" % nn)))
            row["review"] = review_counts(book, nn)
        rows.append(row)
    return rows, covered


def coverage(book, covered):
    """Per session: words not inside any chapter's stretch, with the gaps."""
    report = []
    for src in sorted((book / "text_clean").glob("*.txt")):
        tokens = src.read_text(encoding="utf-8").split()
        mask = [0] * len(tokens)
        for first, last, _ in covered.get(src.stem, []):
            for i in range(first, min(last, len(tokens))):
                mask[i] += 1
        gaps, i = [], 0
        while i < len(tokens):
            if mask[i] == 0:
                j = i
                while j < len(tokens) and mask[j] == 0:
                    j += 1
                gaps.append((i, j))
                i = j
            else:
                i += 1
        report.append({
            "part": src.stem, "words": len(tokens),
            "uncovered": sum(j - i for i, j in gaps),
            "overlap": sum(1 for m in mask if m > 1),
            "chapters": sorted({n for *_, n in covered.get(src.stem, [])}),
            "gaps": [{"from": i, "to": j, "text": " ".join(tokens[i:min(j, i + 15)])}
                     for i, j in gaps if j - i >= 30],
        })
    return report


def flags(row):
    out = []
    if row.get("pct") is not None and not TARGET[0] <= row["pct"] <= TARGET[1]:
        out.append("length %s%% (target %d-%d%%)" % (row["pct"], *TARGET))
    if row.get("source_exact") is False:
        out.append("stretch boundaries matched only roughly")
    if "sections" in row and not SECTIONS[0] <= row["sections"] <= SECTIONS[1]:
        out.append("%d sections" % row["sections"])
    for key, label in (("h3", "### headings"), ("dashes", "dashes"), ("tu_tum", "तू/तुम outside quotes")):
        if row.get(key):
            out.append("%d %s" % (row[key], label))
    if row.get("urdu_added"):
        out.append("Urdu/Persian added (not in source): " + ", ".join(row["urdu_added"]))
    if row.get("urdu_speaker", 0) >= 10 and row["urdu_kept"] < 0.5 * row["urdu_speaker"]:
        out.append("speaker's Urdu/Persian kept %d of %d" % (row["urdu_kept"], row["urdu_speaker"]))
    if row.get("title_ok") is False:
        out.append("title line format")
    if row.get("review") and row["review"].get("pending"):
        out.append("%d review items for a human" % row["review"]["pending"])
    return out


def markdown(book, rows, cov):
    done = [r for r in rows if "words" in r]
    total_ch = sum(r["words"] for r in done)
    measured = [r for r in done if r.get("source_words")]
    total_ch_m = sum(r["words"] for r in measured)
    total_src = sum(r.get("source_words", 0) for r in done)
    total_tx = sum(c["words"] for c in cov)
    rv = [r["review"] for r in done if r.get("review")]
    keys = ["completeness", "faithfulness", "verses", "language", "format", "pending"]
    sums = {k: sum(int(r.get(k, 0) or 0) for r in rv) for k in keys}
    L = ["# Book report: %s" % book.name, ""]
    L += ["## Summary", "",
          "| | |", "|---|---|",
          "| Chapters written / planned | %d / %d |" % (len(done), len(rows)),
          "| Chapters reviewed | %d |" % len(rv),
          "| Transcript words (all sessions) | %d |" % total_tx,
          "| Source words used by written chapters | %d |" % total_src,
          "| Chapter words | %d |" % total_ch,
          "| Chapter words as %% of source | %s over %d chapters with a stretch record (target %d-%d%%) |" % (
              "%.1f%%" % (100 * total_ch_m / total_src) if total_src else "n/a", len(measured), *TARGET),
          "| Chapters without a stretch record | %s |" % (", ".join(str(r["chapter"]) for r in done
                                                         if not r.get("source_words")) or "none"),
          "| Transcript words in no chapter | %d |" % sum(c["uncovered"] for c in cov),
          "| Review corrections applied | %s |" % ", ".join("%s %d" % (k, sums[k]) for k in keys[:-1]),
          "| Review items left for a human | %d |" % sums["pending"],
          "| Speaker's Urdu/Persian word uses kept | %d of %d |" % (
              sum(r.get("urdu_kept", 0) for r in done), sum(r.get("urdu_speaker", 0) for r in done)),
          "| Chapters with flags | %d |" % sum(1 for r in done if flags(r)), ""]
    vr = book / "verses_report.json"
    if vr.exists():
        try:
            v = json.loads(vr.read_text(encoding="utf-8"))
            L += ["Verse check: %s." % ", ".join("%s %s" % (k, v[k]) for k in v), ""]
        except ValueError:
            pass

    L += ["## Chapters", "",
          "| # | Title | Source words | Draft | Final | % of source | Review changed | Corrections (C/F/V/L/Fm) | Pending | Sections | Verses | Flags |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if "words" not in r:
            L.append("| %d | (%s) | | | | | | | | | | |" % (r["chapter"], r["status"]))
            continue
        rv1 = r.get("review") or {}
        corr = "/".join(str(rv1.get(k, "")) for k in keys[:-1]) if rv1 else ""
        L.append("| %d | %s | %s | %s | %d | %s | %s | %s | %s | %d | %d | %s |" % (
            r["chapter"], r.get("title", ""), r.get("source_words", "?"), r.get("draft_words", ""),
            r["words"], ("%s%%" % r["pct"]) if r.get("pct") is not None else "?",
            ("%s%% of words" % r["words_changed_pct"]) if "words_changed_pct" in r else "",
            corr, rv1.get("pending", "") if rv1 else "", r["sections"], r["verse_blocks"],
            "; ".join(flags(r)) or "ok"))
    L += ["", "Columns: *Source words* is the transcript stretch the chapter was written from "
          "(stretch/NN.json); *Draft* is before review, *Final* after; *Review changed* is the share of "
          "words the review altered (full diff in reports/changes/NN_review.diff); corrections are "
          "Completeness / Faithfulness / Verses / Language / Format, from reviews/NN_review.json.", ""]

    L += ["## Coverage of the transcript", "",
          "| Session | Words | Chapters | Words in no chapter | Words in two chapters |",
          "|---|---|---|---|---|"]
    for c in cov:
        L.append("| %s | %d | %s | %d | %d |" % (c["part"], c["words"], ", ".join(map(str, c["chapters"])) or "none",
                                               c["uncovered"], c["overlap"]))
    gaps = [(c["part"], g) for c in cov for g in c["gaps"] if c["chapters"]]
    if gaps:
        L += ["", "Gaps of 30 or more words inside sessions that chapters use (check whether they were "
              "logistics, or content that was dropped):", ""]
        for part, g in gaps:
            L.append("- %s, words %d-%d: «%s ...»" % (part, g["from"], g["to"], g["text"]))
    L += ["", "Words in two chapters are boundary overlaps, removed in the edit step.", ""]
    return "\n".join(L)


def main(book):
    book = Path(book).resolve()
    rows, covered = chapter_rows(book)
    cov = coverage(book, covered)
    (book / "reports").mkdir(exist_ok=True)
    (book / "reports" / "chapters.json").write_text(
        json.dumps({"chapters": rows, "coverage": cov}, ensure_ascii=False, indent=1), encoding="utf-8")
    md = markdown(book, rows, cov)
    (book / "reports" / "book_report.md").write_text(md, encoding="utf-8")
    print(book / "reports" / "book_report.md")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
