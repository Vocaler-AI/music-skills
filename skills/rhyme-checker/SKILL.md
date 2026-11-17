---
name: rhyme-checker
description: "Checks lyrics for rhyme, syllable count, stress and flow, or finds rhymes for a word. Use when the user wants a diagnosis or a line-level fix for sound or meter."
license: MIT
metadata:
  author: Vocaler
  version: "1.2.0"
  category: songwriting
  homepage: https://skills.vocaler.ai/rhyme-checker/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Rhyme Checker

Checks rhyme, syllable count, stress and flow, finds rhymes by sound, and fixes a line without losing its meaning, end rhyme or meter.

## When to use

- The user pastes lyrics and asks whether they rhyme, flow or scan.
- The user needs rhymes for a word, with options beyond the obvious.
- A line feels clunky and the user cannot tell why.

## What to look for in the request

- The lyrics or the word to rhyme.
- Language, accent and delivery when relevant. A beat, melody, target count or matching section can give a line its intended shape.
- Any constraints on what the fix must preserve, such as meaning, end word or scheme.

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. For a rhyme search, use the word's pronunciation in context. Group usable words or phrases by rhyme closeness, and give syllable counts or stress where they affect fit.
2. For a draft, map end rhymes by section and note internal rhymes that affect the flow. Describe closeness (perfect or near) separately from span (single or multiple syllables).
3. Count syllables and show natural word stress on the phrases being diagnosed. Use the supplied beat or melody to assess placement. With text alone, compare corresponding phrases and state any pronunciation that changes the diagnosis.
4. Identify whether the problem comes from sound, wording, count or stress placement. Fix that condition at line level. Preserve a working end rhyme when shortening an overlong line, and match the target phrase length when there is one.
5. Keep the user's stated constraints on meaning, rhyme and rhythm. Show the updated count or rhyme for each fix, and identify any tradeoff outside those constraints.

## Rules

- Judge by sound. For example, 'should have read' can rhyme with 'bed', while 'need to read' can rhyme with 'seed'.
- Keep deliberate slant rhymes, repetitions and delivery choices that work in context.
- Point out stock pairs (fire/desire, heart/apart) when they make a line predictable; keep them when the line earns them.
- Match the depth of the review to the request. A count-only request needs counts and relevant pronunciation variants.

## Output format

```markdown
| Line | Syllables | Stress or phrasing | End rhyme |
|------|-----------|--------------------|-----------|

**Diagnosis** — [line and cause]
**Fix** — [replacement, updated count or rhyme, and any tradeoff]

For a rhyme search, list usable matches by rhyme closeness instead.
```

## Example

**Request:** This line has to take eight syllables and rhyme with 'train': 'I left your key outside in the pouring rain.' Help with the meter.

**Response (abridged):**

```
'Rain' and 'train' rhyme. The line has 11 syllables against a target of 8.

Try 'I left your key in driving rain' (8). The main phrase stresses can fall on LEFT, KEY, DRIV- and RAIN. It keeps the end rhyme and the heavy rain.
```
