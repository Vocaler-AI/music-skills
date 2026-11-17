---
name: artist-branding
description: "Builds an artist identity: positioning, story, visual language, tone of voice, bio in three lengths, name checks and a consistency kit across releases and socials. Use when the user is starting an artist project, rebranding, choosing an artist name, writing a bio, or wants their releases to look and sound like one artist."
license: MIT
metadata:
  author: Vocaler
  version: "1.0.0"
  category: release-and-publishing
  homepage: https://skills.vocaler.ai/artist-branding/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Artist Branding

Builds an artist identity: positioning, story, visual language, tone of voice and bios, so every release and post looks like the same artist.

## When to use

- Starting an artist project or alias.
- Rebranding.
- Writing a bio or choosing a name.

## What to look for in the request

- The music (genre, references described, themes).
- The person or project: story, values, audience.
- What exists already (name, logo, past covers).

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Positioning in one line: for whom, what feeling, what makes it different.
2. Three brand words and three words to avoid.
3. Story: the true origin and why it matters (no invented biography).
4. Visual language: palette, type feel, photo and artwork style, recurring motif.
5. Voice: how the artist writes captions and talks to fans, with examples.
6. Bios: 1 line, 50 words, 150 words.
7. For names: 5-10 options, each checked for meaning, pronunciation, search clash (tell the user to search streaming services and socials) and handle availability to verify.

## Rules

- Never invent facts about the artist.
- Do not imitate an existing artist's identity.

## Output format

```markdown
**Positioning:** ...
**Words:** are / are not
**Story:** ...
**Visual language:** ...
**Voice:** ... (examples)
**Bios:** short / medium / long
```

## Example

**Request:** Bedroom-pop project, songs about growing up in a small coastal town.

**Response (abridged):**

```
Positioning: postcards from a town you can't wait to leave and will always miss. Words: salt-faded, honest, wry. Motif: hand-written place names on every cover.
```
