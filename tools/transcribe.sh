#!/bin/bash
# Transcribe a local audio file or YouTube URL with WhisperX (runs locally, no API).
# Usage: tools/transcribe.sh <audio_file|youtube_url> <name>
# Writes: output/<name>/<name>_raw_transcript.txt

set -e

if [ $# -ne 2 ]; then
    echo "Usage: $0 <audio_file|youtube_url> <name>" >&2
    exit 1
fi

INPUT="$1"
NAME="$2"
TOOLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$(dirname "$TOOLS_DIR")/output/${NAME}"
OUT_FILE="${OUTPUT_DIR}/${NAME}_raw_transcript.txt"
WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT

mkdir -p "$OUTPUT_DIR"

if [[ "$INPUT" =~ ^https?:// ]]; then
    echo "Downloading audio..."
    yt-dlp -f "ba" -x --audio-format mp3 --postprocessor-args "-b:a 320k" --no-playlist \
        -o "${WORK_DIR}/audio.%(ext)s" "$INPUT" > /dev/null
    AUDIO="${WORK_DIR}/audio.mp3"
else
    [ -f "$INPUT" ] || { echo "File not found: $INPUT" >&2; exit 1; }
    AUDIO="$(cd "$(dirname "$INPUT")" && pwd)/$(basename "$INPUT")"
fi

VENV_SITE_PACKAGES=$(find "${TOOLS_DIR}/whisperx-env/lib" -maxdepth 2 -name "site-packages" -type d | head -1)
[ -n "$VENV_SITE_PACKAGES" ] || { echo "WhisperX site-packages not found" >&2; exit 1; }
export PYTHONPATH="${VENV_SITE_PACKAGES}:${PYTHONPATH}"

echo "Transcribing with WhisperX (this can take 5-20 minutes)..."
python3 -m whisperx "$AUDIO" --model medium --device cpu --compute_type int8 \
    --initial_prompt "This is a spiritual discourse with Sanskrit mantras, Hindi devotional content, and English explanations." \
    --output_format txt --output_dir "$WORK_DIR" 2>&1 | tail -5

TRANSCRIPT="${WORK_DIR}/$(basename "${AUDIO%.*}").txt"
[ -s "$TRANSCRIPT" ] || { echo "WhisperX transcription failed" >&2; exit 1; }

mv "$TRANSCRIPT" "$OUT_FILE"
echo "Transcript: $OUT_FILE"
