---
name: arrangement-advisor
description: "Advises on arrangement: what plays in each section, builds and drops, ear candy, counter-melodies, and fixing a song that feels static or crowded. Use when a track feels repetitive, flat, too busy or too empty, or when the user asks how to arrange a demo into a full production."
license: MIT
metadata:
  author: Vocaler
  version: "1.2.0"
  category: music-production
  homepage: https://skills.vocaler.ai/arrangement-advisor/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Arrangement Advisor

Turns a loop or a demo into an arrangement: what plays where, how sections build and drop, and the small moves that stop it feeling static.

## When to use

- A track is a good loop but not a song.
- It sounds flat, repetitive, crowded or empty.
- Taking a voice-memo demo to a full production plan.

## What to look for in the request

- Song form and tempo, instruments in use.
- What feels wrong.
- Genre and references (described).

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Map the current arrangement as a grid: sections across, instruments down.
2. Find the problem: no contrast between sections, everything starting at once, nothing new in the second half, register clashes.
3. Prescribe changes per section: add, remove, change part, change register.
4. Add transitions: risers, fills, reverse cymbals, a bar of silence, a drop to vocal only.
5. Add one or two ear-candy moments per minute that reward listening.

## Rules

- Subtraction is the strongest tool: removing the drums for 4 bars makes the return land.
- Each repeat of a section should change something.

## Output format

```markdown
| Instrument | Intro | V1 | Ch1 | V2 | Ch2 | Bridge | Ch3 |
**Diagnosis:** ...
**Changes:** ...
**Transitions & ear candy:** ...
```

## Example

**Request:** My chorus doesn't hit harder than the verse.

**Response (abridged):**

```
Pull bass and kick out of the last 2 bars of the pre-chorus, add a riser, then bring in a wider pad, doubled vocals and an octave-up lead on the chorus downbeat.
```
