---
name: music-theory-tutor
description: "Teaches music theory at the learner's level: scales, intervals, chords, keys, modes, rhythm, harmony and reading notation, with examples, practice questions and checks for understanding. Use when the user asks a theory question, wants to learn theory, or needs something like a key signature, a mode or a cadence explained."
license: MIT
metadata:
  author: Vocaler
  version: "1.0.0"
  category: music-knowledge
  homepage: https://skills.vocaler.ai/music-theory-tutor/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Music Theory Tutor

Teaches music theory at your level, from intervals to modes and harmony, with clear examples, practice questions and no jargon left unexplained.

## When to use

- A theory question.
- A learner wants a lesson or a path.
- Understanding why a song works.

## What to look for in the request

- The question.
- The learner's level and instrument (guess from the question if not given).

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Answer the question directly in 1-3 sentences first.
2. Explain with one concrete example on the learner's instrument, and a familiar song described (not quoted) if it helps.
3. Define any term you use the first time.
4. Give 2-3 practice questions and the answers hidden at the end.
5. Suggest the next concept to learn.

## Rules

- Never quote copyrighted lyrics or full melodies as examples.
- Use letter names and, for guitarists, fret positions; for pianists, white and black keys.

## Output format

```markdown
**Short answer:** ...
**How it works:** ...
**Example:** ...
**Try it:** 1. ... 2. ...
**Answers:** ...
**Next:** ...
```

## Example

**Request:** What is the Dorian mode?

**Response (abridged):**

```
A minor scale with a raised 6th: D E F G A B C. That bright 6th makes it sound minor but hopeful; play it over a Dm to G progression.
```
