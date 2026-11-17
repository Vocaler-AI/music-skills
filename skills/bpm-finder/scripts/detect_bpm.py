#!/usr/bin/env python3
"""Estimate the tempo of an audio file.

Usage: python detect_bpm.py path/to/song.mp3
Needs: pip install librosa
Prints the estimated BPM and the half/double-time alternatives.
"""
import sys

try:
    import librosa
except ImportError:
    sys.exit("librosa is not installed: pip install librosa")

if len(sys.argv) != 2:
    sys.exit(__doc__)

y, sr = librosa.load(sys.argv[1], mono=True)
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
bpm = float(tempo[0] if hasattr(tempo, "__len__") else tempo)
print(f"tempo: {bpm:.1f} BPM")
print(f"half-time: {bpm / 2:.1f}  double-time: {bpm * 2:.1f}")
print(f"beats detected: {len(beats)}")
