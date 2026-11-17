---
name: mixing-feedback
description: "Gives structured mix feedback and fixes: balance, EQ, compression, low end, vocals, stereo, depth and loudness, from a description, a screenshot of meters or a spectrum, or analysis output. Use when the user asks for mix feedback, says their mix sounds muddy, harsh, thin, quiet or amateur, or asks for loudness targets."
license: MIT
metadata:
  author: Vocaler
  version: "1.2.0"
  category: music-production
  homepage: https://skills.vocaler.ai/mixing-feedback/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Mixing Feedback

Gives clear mix notes with fixes: muddy low end, harsh highs, buried vocals and loudness targets, with settings to try.

## When to use

- The user describes how their mix sounds wrong.
- The user shares a spectrum, meter readings or a mix screenshot.
- Loudness questions for streaming.

## What to look for in the request

- Genre and reference (described).
- The complaint in the user's words.
- Any data: LUFS, true peak, spectrum image, DAW and plugins.

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Translate the complaint into a technical cause (muddy = buildup 200-500 Hz; harsh = 2-5 kHz; boomy = 80-200 Hz; thin = lacking 100-250 Hz; buried vocal = level or masking).
2. Work in order: balance, low end, vocal, EQ, dynamics, space, stereo, loudness.
3. For each note: the problem, the likely cause, a fix with starting settings, and how to check it.
4. Give loudness guidance: most streaming services normalise around -14 LUFS integrated; keep true peak below -1 dBTP.
5. If you cannot hear the audio, say your notes are hypotheses based on the description.

## Rules

- Starting values, not rules: give ranges and tell the user to trust ears and references.
- Prioritise: three notes that matter beat fifteen.

## Output format

```markdown
**Top 3 issues**
1. Problem · cause · fix (settings) · how to check
**Loudness:** ...
**Next pass:** ...
```

## Example

**Request:** My mix is muddy and the vocal is lost.

**Response (abridged):**

```
1) Low-mid buildup: high-pass everything but kick and bass at 100-150 Hz; cut 2-4 dB around 300 Hz on pads and guitars. 2) Vocal masking: cut 2-3 dB at 2-4 kHz on guitars, sidechain or dynamic EQ keyed from the vocal.
```
