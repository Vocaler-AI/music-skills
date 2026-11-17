---
name: rhyme-checker
description: "Analyses lyrics for rhyme scheme, rhyme quality, syllable counts and stress, and suggests better rhymes and fixes. Use when the user asks to check rhymes, find a rhyme, fix the flow or meter of lyrics, or count syllables."
license: MIT
metadata:
  author: Vocaler
  version: "1.1.0"
  category: songwriting
  homepage: https://skills.vocaler.ai/rhyme-checker/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Rhyme Checker

Maps the rhyme scheme, counts syllables, flags forced or tired rhymes and offers better options that keep the meaning and the meter.

## When to use

- The user pastes lyrics and asks whether they rhyme, flow or scan.
- The user needs rhymes for a word, with options beyond the obvious.
- A line feels clunky and the user cannot tell why.

## What to look for in the request

- The lyrics or the word to rhyme.
- Genre (rap tolerates and rewards multisyllabic and internal rhyme; folk and country lean on perfect rhyme).
- Language and accent if relevant (rhymes differ between accents).

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Mark each line-end with a scheme letter (A, B, C...) and label the rhyme type: perfect, family, assonance, consonance, multisyllabic, or none.
2. Count syllables per line and mark the stressed syllables. Compare lines that should be parallel.
3. Flag problems: forced rhymes, inverted word order, cliché pairs, identical rhymes (same word), stress landing on a weak syllable.
4. For each flagged line offer 2-3 rewrites that keep the meaning and syllable count.
5. For a single-word request, group rhymes by type and by syllable count, and include near rhymes, which are usually the more interesting choice.

## Rules

- Judge by sound, not spelling: 'love' and 'move' are an eye rhyme, not a rhyme.
- Near rhymes are not mistakes. Only flag them if the style demands perfect rhyme.
- Never change the meaning of a line to win a rhyme without saying so.
- Keep the user's voice. Suggest, don't rewrite the whole song.

## Output format

```markdown
| # | Line | Syll. | Scheme | Rhyme type |
|---|------|-------|--------|------------|

**Scheme:** [e.g. ABAB / AABB]
**Issues:** [numbered, one line each]
**Fixes:** [line #: option 1 / option 2]
```

## Example

**Request:** What rhymes with 'orange' that I could actually use in a song?

**Response (abridged):**

```
Perfect: almost none ('door hinge', 'Blorenge'). Near and multisyllabic: 'four inch', 'porridge', 'storage', 'forage', 'more change'. Best bet: end on 'storage' with a slant match, or move 'orange' mid-line.
```
