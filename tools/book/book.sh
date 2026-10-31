#!/bin/bash

# Make a Hindi book from a multi-day Shibir, one step at a time. Each step is resumable:
# finished outputs are skipped, so a step can be stopped and re-run.
#
# Usage: tools/book/book.sh <book> <step> [chapter numbers...]
#
# The book lives in books/<book>/ and needs a book.json (see .claude/skills/book/SKILL.md).
# Steps, in order:
#   text      transcript/**/*.docx -> raw/DayNN_PartNN.txt (plain text, no changes)
#   clean     raw/*.txt -> text_clean/*.txt with prompt 01   (CLEAN=copy copies raw as-is)
#   digest    text_clean/*.txt -> digests/*.md with prompt 02
#   plan      digests -> book_plan.md, chapters.txt, book.json (title, parts) with prompt 03
#   write     each chapter: prompt 04 -> drafts/NN_chapter.txt, then prompt 05 review -> chapters/NN_chapter.txt
#   verses    all chapters: prompt 06 -> verses_report.md
#   edit      whole book: prompt 07 -> front_matter.txt, back_matter.txt, edit_log.md
#   report    reports/book_report.md (content, length, changes, review, checks)
#   pdf       book/<book>.html, .pdf and .epub
#
# Settings (environment variables):
#   MODEL        claude model (default: claude-opus-5-5)
#   EFFORT       claude effort level (default: low)
#   JOBS         parallel runs for clean, digest and write (default: 5)
#   LIMIT_WAIT   seconds to wait after a usage limit before retrying (default: 1800)
#   MAX_TRIES    other failures allowed per item (default: 2)
#   CLEAN        "copy" to skip prompt 01 for human-typed transcripts (default: run the prompt)
#
# Every step appends its settings, tool versions, the repo commit and hashes of the prompts, scripts
# and inputs to run.json.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
BOOK_NAME="$1"; STEP="$2"; shift 2 2>/dev/null
[ -n "$BOOK_NAME" ] && [ -n "$STEP" ] || { sed -n 3,32p "$0"; exit 1; }
DIR="$ROOT/books/$BOOK_NAME"
[ -f "$DIR/book.json" ] || { echo "missing $DIR/book.json"; exit 1; }
PROMPTS="$ROOT/tools/prompts/book"
LOGDIR="$ROOT/tools/batch_logs/book/$BOOK_NAME"
MODEL="${MODEL:-claude-opus-5-5}"; EFFORT="${EFFORT:-low}"; JOBS="${JOBS:-5}"
LIMIT_WAIT="${LIMIT_WAIT:-1800}"; MAX_TRIES="${MAX_TRIES:-2}"
TOOLS="Read Write Edit Bash(wc:*) Bash(grep:*) Bash(ls:*)"
mkdir -p "$LOGDIR"
cd "$DIR" || exit 1

json() { python3 -c "import json,sys; print(json.load(open('book.json')).get(sys.argv[1],''))" "$1"; }
BOOK_TEXT="$(json book)"; PLACE="$(json place)"

# Fill a prompt's placeholders. Extra pairs: KEY=VALUE.
fill() {
    local prompt=$1; shift
    python3 - "$prompt" "$@" <<'EOF'
import sys
text = open(sys.argv[1], encoding="utf-8").read()
for pair in sys.argv[2:]:
    key, _, value = pair.partition("=")
    text = text.replace("{%s}" % key, value)
print(text)
EOF
}

is_limit() { grep -qiE "usage limit|spend limit|session limit|limit reached|rate limit|limit resets|out of extra usage|429" "$1"; }

# Run claude until the output test passes. Usage-limit waits do not count as tries.
# run_claude <name> <done-test> <prompt text> [stdin-file out-file]
#   With stdin-file, the prompt and file are piped in and the reply is saved to out-file (no tools).
#   Without, claude runs with file tools in the book folder and writes its own outputs.
run_claude() {
    local name=$1 test=$2 task=$3 stdin=$4 out=$5 log="$LOGDIR/$1.log" tries=0
    while ! eval "$test"; do
        [ "$tries" -ge "$MAX_TRIES" ] && { echo "$name: FAILED (see $log)"; return 1; }
        if [ -n "$stdin" ]; then
            { printf '%s\n\n' "$task"; cat "$stdin"; } \
                | claude -p --model "$MODEL" --effort "$EFFORT" > "$log.out" 2> "$log"
            cat "$log.out" >> "$log"
        else
            claude -p "$task" --model "$MODEL" --effort "$EFFORT" --permission-mode acceptEdits \
                --allowedTools "$TOOLS" > "$log" 2>&1
        fi
        if is_limit "$log" && [ "$(wc -c < "$log")" -lt 3000 ]; then
            echo "$name: usage limit, waiting $((LIMIT_WAIT / 60)) min"; sleep "$LIMIT_WAIT"
            continue
        fi
        tries=$((tries + 1))
        [ -n "$stdin" ] && [ -s "$log.out" ] && mv "$log.out" "$out"
    done
    rm -f "$log.out"
    echo "$name: done"
}

# Append what produced this step to run.json: the model and every setting, the claude, python,
# chrome and font versions, the repo commit (and whether the pipeline files had uncommitted
# changes), and hashes of every prompt, script and input, so a book records how it was made.
record_run() {
    STEP="$STEP" MODEL="$MODEL" EFFORT="$EFFORT" JOBS="$JOBS" LIMIT_WAIT="$LIMIT_WAIT" \
    MAX_TRIES="$MAX_TRIES" CLEAN="$CLEAN" TOOLS="$TOOLS" python3 - "$ROOT" "$*" <<'EOF2'
import hashlib, json, os, platform, subprocess, sys, time
from pathlib import Path
root, args = sys.argv[1:]
def out(*cmd):
    try: return subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
    except OSError: return ""
git = lambda *a: out("git", "-C", root, *a)
sha = lambda data: hashlib.sha256(data).hexdigest()[:16]
def tree(folder):  # one hash over a folder's files (names and contents), or "" if missing
    files = sorted(f for f in Path(folder).rglob("*") if f.is_file() and not f.name.endswith(":Zone.Identifier"))
    return sha(b"".join(str(f.relative_to(folder)).encode() + f.read_bytes() for f in files)) if files else ""
font = out("fc-match", "-f", "%{file}", "Noto Serif Devanagari")
pipeline = sorted((Path(root) / "tools/prompts/book").glob("*")) + sorted((Path(root) / "tools/book").glob("*.[ps][yh]")) \
    + [Path(root) / ".claude/skills/book/SKILL.md"]
entry = {
    "step": os.environ["STEP"], "args": args, "time": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    "settings": {"model": os.environ["MODEL"], "effort": os.environ["EFFORT"], "jobs": os.environ["JOBS"],
                 "limit_wait": os.environ["LIMIT_WAIT"], "max_tries": os.environ["MAX_TRIES"],
                 "clean": os.environ["CLEAN"], "allowed_tools": os.environ["TOOLS"],
                 "permission_mode": "acceptEdits"},
    "versions": {"claude_cli": out("claude", "--version"), "python": platform.python_version(),
                 "chrome": out("google-chrome", "--version"), "os": platform.platform(),
                 "font": {"file": font, "sha": sha(Path(font).read_bytes()) if font and Path(font).is_file() else ""}},
    "repo": {"commit": git("rev-parse", "HEAD"),
             "pipeline_uncommitted": bool(git("status", "--porcelain", "tools/book", "tools/prompts/book", ".claude/skills/book"))},
    "pipeline_files": {str(f.relative_to(root)): sha(f.read_bytes()) for f in pipeline if f.is_file()},
    "inputs": {"book.json": sha(Path("book.json").read_bytes()), "transcript": tree("transcript"),
               "raw": tree("raw"), "text_clean": tree("text_clean")},
}
path = Path("run.json")
runs = json.loads(path.read_text()) if path.exists() else []
runs.append(entry)
path.write_text(json.dumps(runs, ensure_ascii=False, indent=1) + "\n")
EOF2
}

session_label() { sed -E 's/^Day0*([0-9]+)_Part0*([0-9]+)$/Day \1, Part \2/' <<< "$1"; }

step_text() {
    mkdir -p raw
    python3 "$ROOT/tools/book/docx_to_text.py" transcript raw
}

clean_one() {
    local part=$1 out="text_clean/$1.txt"
    [ -s "$out" ] && { echo "$part: done"; return; }
    if [ "$CLEAN" = "copy" ]; then cp "raw/$part.txt" "$out"; echo "$part: copied"; return; fi
    local task; task="$(fill "$PROMPTS/01_clean_transcript.txt" "SESSION=$(session_label "$part")" "BOOK=$BOOK_TEXT")"
    run_claude "clean_$part" "[ -s '$out' ]" "$task" "raw/$part.txt" "$out"
}

digest_one() {
    local part=$1 out="digests/$1.md"
    [ -s "$out" ] && { echo "$part: done"; return; }
    local task; task="$(fill "$PROMPTS/02_digest_part.txt" "SESSION=$(session_label "$part")" "BOOK=$BOOK_TEXT")"
    run_claude "digest_$part" "[ -s '$out' ]" "$task" "text_clean/$part.txt" "$out"
}

parallel() {  # parallel <function> <items...>
    local fn=$1; shift
    export -f "$fn" run_claude fill is_limit session_label
    export ROOT DIR PROMPTS LOGDIR MODEL EFFORT LIMIT_WAIT MAX_TRIES TOOLS BOOK_TEXT PLACE CLEAN
    printf '%s\n' "$@" | xargs -P "$JOBS" -I{} bash -c "$fn {}"
}

parts() { ls "$1" 2>/dev/null | sed -E 's/\.(txt|md)$//' | sort; }

chapter_list() {
    if [ $# -gt 0 ]; then printf '%s\n' "$@"; else awk '$1 ~ /^[0-9]+$/ {print $1}' chapters.txt; fi
}

write_one() {
    local n=$1 nn; nn=$(printf %02d "$n")
    local parts_; parts_=$(awk -v n="$n" '$1==n {$1=""; print}' chapters.txt | sed 's/^ *//')
    [ -n "$parts_" ] || { echo "chapter $n: not in chapters.txt"; return 1; }
    local fills=("N=$n" "NN=$nn" "N-1=$((n - 1))" "N+1=$((n + 1))" "PARTS=$parts_" "BOOK=$BOOK_TEXT")
    [ "$n" -eq 1 ] && fills[2]="N-1=0 (none: this is the first chapter)"
    # 1. write
    if [ ! -s "drafts/${nn}_chapter.txt" ]; then
        run_claude "write_$nn" "[ -s chapters/${nn}_chapter.txt ]" "$(fill "$PROMPTS/04_write_chapter.txt" "${fills[@]}")" || return 1
        cp "chapters/${nn}_chapter.txt" "drafts/${nn}_chapter.txt"
    fi
    # 2. review (corrects chapters/NN_chapter.txt in place; drafts/ keeps the version before review)
    run_claude "review_$nn" "[ -s reviews/${nn}_review.md ]" "$(fill "$PROMPTS/05_review_chapter.txt" "${fills[@]}")"
}

case "$STEP" in text|clean|digest|plan|write|verses|edit|report|pdf) record_run "$@" ;; esac

case "$STEP" in
    text)   step_text ;;
    clean)  mkdir -p text_clean; parallel clean_one $(parts raw) ;;
    digest) mkdir -p digests; parallel digest_one $(parts text_clean) ;;
    plan)
        n_sessions=$(ls text_clean/*.txt | wc -l)
        words=$(cat text_clean/*.txt | wc -w)
        days=$(ls text_clean | sed -E 's/_Part.*//' | sort -u | wc -l)
        run_claude plan "[ -s book_plan.md ] && [ -s chapters.txt ]" "$(fill "$PROMPTS/03_book_plan.txt" \
            "BOOK=$BOOK_TEXT" "DAYS=$days" "N_SESSIONS=$n_sessions" "WORDS=$words")"
        ;;
    write)
        mkdir -p chapters drafts reviews stretch
        parallel write_one $(chapter_list "$@")
        python3 "$ROOT/tools/book/book_report.py" "$DIR" ;;
    verses)
        run_claude verses "[ -s verses_report.md ]" "$(fill "$PROMPTS/06_verify_verses.txt" "BOOK=$BOOK_TEXT")" ;;
    edit)
        days=$(ls text_clean | sed -E 's/_Part.*//' | sort -u | wc -l)
        mkdir -p chapters_before_edit
        for f in chapters/*.txt; do [ -e "chapters_before_edit/${f##*/}" ] || cp "$f" chapters_before_edit/; done
        run_claude edit "[ -s edit_log.md ]" "$(fill "$PROMPTS/07_edit_book.txt" "BOOK=$BOOK_TEXT" "DAYS=$days" "PLACE=$PLACE")" ;;
    report) python3 "$ROOT/tools/book/book_report.py" "$DIR" ;;
    pdf)    python3 "$ROOT/tools/book/build_pdf.py" "$DIR" ;;
    *)      echo "unknown step: $STEP"; sed -n 3,32p "$0"; exit 1 ;;
esac
