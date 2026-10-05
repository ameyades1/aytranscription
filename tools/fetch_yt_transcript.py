#!/usr/bin/env python3
"""Download a video's existing YouTube transcript as plain text.

Usage: fetch_yt_transcript.py <youtube_url | file_named_..._VIDEOID.mp3 | VIDEOID> <name>
Writes: output/<name>/<name>_raw_transcript.txt

Track preference: captions uploaded by the channel (video's language first), then YouTube's
auto-generated captions in the original spoken language ("<lang>-orig"). Auto-translated
tracks are never used.

Exit codes: 0 transcript written, 2 no transcript available, 1 error.
"""
import json
import os
import re
import sys

import yt_dlp

ID_RE = r'[A-Za-z0-9_-]{11}'


def video_id(arg):
    m = re.search(rf'(?:v=|youtu\.be/|shorts/|live/)({ID_RE})', arg)
    if m:
        return m.group(1)
    stem = os.path.splitext(os.path.basename(arg))[0]
    if re.fullmatch(ID_RE, stem):
        return stem
    m = re.search(rf'_({ID_RE})$', stem)
    return m.group(1) if m else None


def json3(tracks):
    return next((t for t in tracks if t.get('ext') == 'json3'), None)


def pick_track(info):
    lang = info.get('language')
    manual = {k: v for k, v in (info.get('subtitles') or {}).items() if k != 'live_chat'}
    auto = info.get('automatic_captions') or {}

    candidates = []
    if lang and lang in manual:
        candidates.append((lang, manual[lang], 'uploaded captions'))
    candidates += [(k, v, 'uploaded captions') for k, v in manual.items() if k != lang]
    if lang and f'{lang}-orig' in auto:
        candidates.append((f'{lang}-orig', auto[f'{lang}-orig'], 'auto-generated captions'))
    candidates += [(k, v, 'auto-generated captions') for k, v in auto.items()
                   if k.endswith('-orig') and k != f'{lang}-orig']

    for code, tracks, kind in candidates:
        track = json3(tracks)
        if track:
            return code, track, kind
    return None


def to_text(data):
    lines = []
    for event in data.get('events', []):
        text = ''.join(seg.get('utf8', '') for seg in event.get('segs') or []).replace('\n', ' ').strip()
        if text:
            lines.append(text)
    return '\n'.join(lines) + '\n'


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    vid = video_id(sys.argv[1])
    if not vid:
        print(f'No YouTube video ID found in: {sys.argv[1]}', file=sys.stderr)
        sys.exit(2)

    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output', sys.argv[2])
    out_file = os.path.join(out_dir, f'{sys.argv[2]}_raw_transcript.txt')

    opts = {'quiet': True, 'no_warnings': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False)
        choice = pick_track(info)
        if not choice:
            print(f'No YouTube transcript available for {vid}')
            sys.exit(2)
        code, track, kind = choice
        text = to_text(json.loads(ydl.urlopen(track['url']).read()))

    if not text.strip():
        print(f'YouTube transcript for {vid} is empty')
        sys.exit(2)

    os.makedirs(out_dir, exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Source: YouTube {kind} ({code}) for {vid}')
    print(f'Transcript: {out_file}')


if __name__ == '__main__':
    main()
