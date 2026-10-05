#!/bin/bash

# Download best quality audio from YouTube video
# Usage: ./download_audio.sh <youtube_url>

if [ -z "$1" ]; then
  echo "Usage: $0 <youtube_url>"
  exit 1
fi

yt-dlp -f "ba" -x --audio-format mp3 --postprocessor-args "-b:a 320k" --no-playlist "$1"
