---
name: instrument-selector
description: "Chooses the instrumentation for a track: which instruments, which role each plays (rhythm, bass, harmony, lead, texture), registers and articulations, without frequency clashes. Use when the user asks what instruments to use, how to make a genre authentic, or why a mix or arrangement feels crowded."
license: MIT
metadata:
  author: Vocaler
  version: "1.0.0"
  category: ai-music-generation
  homepage: https://skills.vocaler.ai/instrument-selector/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Instrument Selector

Picks the right instruments and gives each a job, register and articulation so the track sounds full without clashing.

## When to use

- Choosing instruments for a genre, mood or culture.
- An arrangement sounds crowded or thin.
- Writing the instrument line of an AI music prompt.

## What to look for in the request

- Genre, mood, use case.
- Instruments already in the track, if any.
- Budget or live constraints (band, solo, orchestra).

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Fill five roles: rhythm, bass, harmony, lead, texture. One instrument can cover two.
2. Assign each a register (low / mid / high) and check no two leads share the same register at the same time.
3. Specify articulation and tone (e.g. palm-muted guitar, pizzicato strings, Rhodes with tremolo).
4. Mark what enters where: not everything plays all the time.
5. Give the prompt-ready instrument line.

## Rules

- Fewer, well-chosen instruments beat many. Three to six is usual.
- Authenticity matters for regional genres: name the traditional instrument (oud, kora, erhu, tar, bandoneon) and say what it plays.

## Output format

```markdown
| Role | Instrument | Register | Articulation / tone | Enters |
**Prompt line:** ...
```

## Example

**Request:** Instruments for a cosy fantasy tavern scene.

**Response (abridged):**

```
Rhythm: bodhrán (low-mid) · Bass: upright bass, plucked · Harmony: cittern strummed · Lead: tin whistle, ornamented · Texture: crowd murmur, hurdy-gurdy drone
```
