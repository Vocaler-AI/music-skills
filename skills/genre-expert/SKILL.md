---
name: genre-expert
description: "Explains any music genre or subgenre: origins, defining sound, tempo and instruments, key records by era, subgenres, and how to make or recognise it. Use when the user asks what a genre is, how two genres differ, what to listen to, or how to make music in a style."
license: MIT
metadata:
  author: Vocaler
  version: "1.1.0"
  category: music-knowledge
  homepage: https://skills.vocaler.ai/genre-expert/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Genre Expert

Explains any genre or subgenre: where it came from, what defines the sound, the records to hear and how to make it yourself.

## When to use

- What is a genre, how is it different from another, what should I listen to.
- How to make music in a style.

## What to look for in the request

- The genre(s).
- The user's angle: listening, making, writing about it.

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Define it in one sentence.
2. Origins: place, time, the scenes and the technologies that made it.
3. Sound: tempo range, rhythm, instruments, vocals, production, structure.
4. Lineage: parents, siblings, children (subgenres).
5. Listening path: 5-8 essential records in order, across eras.
6. If making: the five things to get right first.

## Rules

- Say when you are unsure about a fact or a date; do not invent records or release years.
- Credit the communities a genre came from.
- Genre borders are fuzzy; say so when they are.

## Output format

```markdown
**In one line:** ...
**Origins:** ... · **Sound:** ...
**Family tree:** parents → [genre] → children
**Listen:** 1. ... (year) ...
**Make it:** ...
```

## Example

**Request:** What's the difference between house and techno?

**Response (abridged):**

```
Both come from 1980s Black American club culture (house: Chicago; techno: Detroit), share four-on-the-floor kicks around 120-130 BPM; house leans on soul, disco and vocals, techno on machine rhythm, repetition and futurism.
```
