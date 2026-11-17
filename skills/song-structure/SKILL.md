---
name: song-structure
description: "Designs and diagnoses song structure: section order, lengths in bars, timing of the first chorus, energy curve. Use when the user asks how to structure a song, whether their song is too long, where to put the bridge, or for a genre's typical form."
license: MIT
metadata:
  author: Vocaler
  version: "1.0.0"
  category: songwriting
  homepage: https://skills.vocaler.ai/song-structure/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Song Structure Architect

Plans the form of a song bar by bar: when the chorus hits, how energy rises and where a bridge or drop earns its place.

## When to use

- Planning a song before writing it.
- A song feels long, flat or slow to get going.
- Adapting a song to a target length (radio edit, 60-second short, extended mix).

## What to look for in the request

- Genre, tempo, target length.
- Existing lyrics or section list, if any.
- Where it will be heard (streaming, radio, short-form video, live, club).

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Pick the reference form for the genre and context (pop, hip-hop, EDM, rock, ballad, folk, K-pop each have conventions).
2. Lay out sections with bar counts and timestamps calculated from the tempo (bars x 4 beats x 60 / BPM seconds, in 4/4).
3. Draw the energy curve 1-10 per section. Every chorus should be at least as high as the last; the final chorus highest.
4. Check key timings: the hook or chorus within 30-45 seconds for streaming, 10-15 seconds for short-form.
5. Suggest cuts or additions and give the new total length.

## Rules

- Always show your timing math; do not guess durations.
- Section lengths are usually 4, 8 or 16 bars. Odd lengths need a reason.
- Contrast beats repetition: the second verse can be shorter; a bridge can drop instruments.
- Respect the genre: a drill track and a folk ballad do not share a form.

## Output format

```markdown
| Section | Bars | Starts | Energy | Purpose |
|---------|------|--------|--------|---------|

**Total:** [m:ss at N BPM]
**First chorus at:** [m:ss]
**Notes:** ...
```

## Example

**Request:** Pop song at 120 BPM, I want it under 3 minutes.

**Response (abridged):**

```
Intro 4 bars (0:00) · V1 8 (0:08) · Pre 4 (0:24) · Ch 8 (0:32) · V2 8 (0:48) · Pre 4 (1:04) · Ch 8 (1:12) · Bridge 8 (1:28) · Ch x2 16 (1:44) · Outro 4 (2:16) — 2:24 total, first chorus at 0:32.
```
