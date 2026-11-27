# Get the raw transcript

Shared by `/blog` and `/chapter`. `<input>` is the skill's input and `<name>` the talk name; paths
are relative to the repo root, and every file for the talk goes in `output/<name>/`.

**Transcripts already there:** if `output/<name>/<name>_raw_transcript.txt` exists, keep it and skip
the rest of this step; if `<name>_clean.txt` also exists, keep it too and skip the cleaning step.
Only fetch or transcribe again when the user asks for it.

**Input is a `.txt` transcript:** create `output/<name>/` and copy it to
`output/<name>/<name>_raw_transcript.txt` unless it is already there.

**Input is an audio file or YouTube URL:** prefer YouTube's own transcript over WhisperX.

1. Run `python3 tools/fetch_yt_transcript.py "<input>" "<name>"`. It reads the video ID from the
   URL, or from the end of the file name (`..._<11-char ID>.mp3`), and downloads the channel's
   uploaded captions, or else YouTube's auto-generated captions in the original spoken language
   (never an auto-translated track).
   - Exit 0: the transcript is written. Note the `Source:` line and skip WhisperX.
   - Exit 2 (no video ID, or no transcript on YouTube) or exit 1 (error, e.g. no network or a
     private video): say why in one line and fall back to WhisperX.
2. WhisperX fallback: run `tools/transcribe.sh "<input>" "<name>"` in the background (5-20
   minutes) and wait for it to finish.

If the user asks to use WhisperX (or a local transcription), skip the YouTube fetch.

Note the transcript source for the report: YouTube uploaded captions, YouTube auto-generated
captions, WhisperX, or the user's `.txt`.
