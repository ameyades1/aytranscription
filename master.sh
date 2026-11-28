#!/bin/bash

set -e

# Master script for YouTube transcription -> cleaning -> book chapter generation

TOOLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/tools" && pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/output"
PROMPTS_DIR="${TOOLS_DIR}/prompts"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

log_step() {
    echo -e "${YELLOW}[STEP]${NC} $1"
}

usage() {
    cat << 'USAGE'
Usage: ./master.sh <input> [output_name]

Arguments:
  input          YouTube URL, local MP3 file, or existing transcript (.txt)
  output_name    (Optional) Base name for output files. Defaults to sanitized video title or filename

Examples:
  ./master.sh "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  ./master.sh "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "my_discourse"
  ./master.sh "tools/power_of_surrendering_to_guru_xXkJCnkCJh4.mp3"
  ./master.sh "tools/power_of_surrendering_to_guru_xXkJCnkCJh4.mp3" "my_chapter"
  ./master.sh "output/my_chapter_raw_transcript.txt"   # skips download + transcription

This script:
  1. Downloads audio from YouTube OR uses local MP3 file
  2. Transcribes with WhisperX
  3. Cleans the transcript
  4. Generates a book chapter
USAGE
    exit 1
}

# Check arguments
if [ $# -lt 1 ]; then
    usage
fi

INPUT="$1"
OUTPUT_NAME="${2:-}"

# Create output directory
mkdir -p "${OUTPUT_DIR}"
log_info "Output directory: ${OUTPUT_DIR}"

if [[ ! "$INPUT" =~ ^https?:// ]] && [ ! -f "$INPUT" ]; then
    log_error "File not found: $INPUT"
    exit 1
fi

# Determine output base name
if [ -z "$OUTPUT_NAME" ]; then
    OUTPUT_NAME=$(basename "$INPUT" | sed 's/\.[^.]*$//; s/_raw_transcript$//')
    if [ "$OUTPUT_NAME" = "audio" ]; then
        OUTPUT_NAME="discourse"
    fi
fi

TRANSCRIPT_CLEAN="${OUTPUT_NAME}_raw_transcript.txt"

if [[ "$INPUT" == *.txt ]]; then
    # Existing transcript: skip download and transcription
    log_step "Using existing transcript, skipping download and transcription..."
    INPUT_ABS="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"
    if [ "$INPUT_ABS" != "${OUTPUT_DIR}/${TRANSCRIPT_CLEAN}" ]; then
        cp "$INPUT" "${OUTPUT_DIR}/${TRANSCRIPT_CLEAN}"
    fi
    log_info "Transcript: ${OUTPUT_DIR}/${TRANSCRIPT_CLEAN}"
else
    if [[ "$INPUT" =~ ^https?:// ]]; then
        log_step "Downloading audio from YouTube..."
        AUDIO_FILE="${OUTPUT_DIR}/audio.mp3"

        cd "${TOOLS_DIR}"
        bash download_ytaudio.sh "${INPUT}" > /dev/null 2>&1

        # Find the downloaded audio file (yt-dlp saves with different names)
        DOWNLOADED_AUDIO=$(find . -maxdepth 1 -name "*.mp3" -o -name "*.m4a" -o -name "*.wav" | head -1)

        if [ -z "$DOWNLOADED_AUDIO" ]; then
            log_error "Failed to download audio from YouTube"
            exit 1
        fi

        mv "$DOWNLOADED_AUDIO" "${AUDIO_FILE}"
        log_info "Audio downloaded: ${AUDIO_FILE}"
    else
        log_step "Using local audio file..."
        AUDIO_FILE="${OUTPUT_DIR}/audio.mp3"
        cp "$INPUT" "${AUDIO_FILE}"
        log_info "Local audio file: ${AUDIO_FILE}"
    fi

    # Step 2: Transcribe with WhisperX
    log_step "Transcribing with WhisperX..."
    cd "${OUTPUT_DIR}"

    # Set up Python path to include venv site-packages (expand glob)
    VENV_SITE_PACKAGES=$(find "${TOOLS_DIR}/whisperx-env/lib" -maxdepth 2 -name "site-packages" -type d | head -1)

    if [ -z "$VENV_SITE_PACKAGES" ]; then
        log_error "WhisperX site-packages not found"
        exit 1
    fi

    export PYTHONPATH="${VENV_SITE_PACKAGES}:${PYTHONPATH}"

    # WhisperX outputs multiple formats by default: json, vtt, srt, tsv, txt
    python3 -m whisperx "${AUDIO_FILE}" --model medium --device cpu --compute_type int8 \
        --initial_prompt "This is a spiritual discourse with Sanskrit mantras, Hindi devotional content, and English explanations." \
        --output_dir . 2>&1 | tail -20 || true

    TRANSCRIPT_FILE=$(find . -name "*.txt" | head -1)

    if [ -z "$TRANSCRIPT_FILE" ] || [ ! -f "$TRANSCRIPT_FILE" ]; then
        log_error "WhisperX transcription failed"
        exit 1
    fi

    mv "$TRANSCRIPT_FILE" "$TRANSCRIPT_CLEAN"
    log_info "Transcription complete: ${TRANSCRIPT_CLEAN}"
fi

# Step 3: Clean transcript
log_step "Cleaning transcript with Gemini..."
CLEANED_FILE="${OUTPUT_NAME}_clean.txt"

cd "${SCRIPT_DIR}"
python3 "${TOOLS_DIR}/process_with_gemini.py" \
    "${PROMPTS_DIR}/legacy/clean_transcript.txt" \
    "${OUTPUT_DIR}/${TRANSCRIPT_CLEAN}" \
    "${OUTPUT_DIR}/${CLEANED_FILE}"

log_info "Transcript cleaned: ${CLEANED_FILE}"

# Step 4: Generate book chapter
log_step "Generating book chapter with Gemini..."
CHAPTER_FILE="${OUTPUT_NAME}_chapter.txt"

python3 "${TOOLS_DIR}/process_with_gemini.py" \
    "${PROMPTS_DIR}/legacy/generate_chapter.txt" \
    "${OUTPUT_DIR}/${CLEANED_FILE}" \
    "${OUTPUT_DIR}/${CHAPTER_FILE}"

log_info "Book chapter generated: ${CHAPTER_FILE}"

# Summary
echo ""
log_info "Process completed successfully!"
echo ""
echo "Output files:"
echo "  Raw transcript:  ${OUTPUT_DIR}/${TRANSCRIPT_CLEAN}"
echo "  Cleaned text:    ${OUTPUT_DIR}/${CLEANED_FILE}"
echo "  Book chapter:    ${OUTPUT_DIR}/${CHAPTER_FILE}"
echo ""
