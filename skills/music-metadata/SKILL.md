---
name: music-metadata
description: "Prepares and checks release metadata for distribution: titles and versions, artist and featured artist formatting, genres, credits, ISRC and UPC, language, explicit flags and store style rules. Use when the user is filling in a distributor form, preparing a release sheet, or a release was rejected for metadata."
license: MIT
metadata:
  author: Vocaler
  version: "1.1.0"
  category: release-and-publishing
  homepage: https://skills.vocaler.ai/music-metadata/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Music Metadata Assistant

Prepares release metadata that distributors accept: titles, artist formatting, credits, genres, codes and explicit flags, checked against store style rules.

## When to use

- Filling a distributor's upload form.
- A release was rejected or merged into the wrong artist profile.
- Making a complete credits sheet.

## What to look for in the request

- Release type, track list, artists, writers, producers.
- Distributor (DistroKid, TuneCore, CD Baby, etc.), if known.
- Existing codes (ISRC, UPC), release date.

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Build the metadata sheet: release and track level.
2. Apply common store style rules: no extra info in titles (no 'Official', no emojis, no 'prod. by'); versions in parentheses '(Acoustic)', '(Remix)'; featured artists in the feature field, not the title, unless the distributor says otherwise.
3. Check consistency: identical artist spelling across tracks, correct capitalisation (title case or as the artist styles it), language and explicit flags.
4. List what is missing and who usually supplies it (ISRC: distributor or label; UPC: distributor).
5. Flag anything that commonly triggers rejection.

## Rules

- Never invent codes, names or credits.
- Rules vary by distributor and change: say which you applied and suggest checking the distributor's current guide.

## Output format

```markdown
**Release:** title · type · artist · date · UPC · genre / subgenre · label · (P)/(C) lines
| # | Track | Version | Feat. | Writers | Producers | ISRC | Explicit | Language |
**Missing:** ...
**Rejection risks:** ...
```

## Example

**Request:** Track title: 'Night Drive (feat. Lena) [prod. by Kai] - Official'

**Response (abridged):**

```
Title: 'Night Drive' · Featured artist: Lena (in the feature field) · Producer credit: Kai · Remove 'Official' and 'prod. by' from the title.
```
