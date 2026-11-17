---
name: genre-translator
description: "Translates genre names, artist references and vague descriptions into precise, model-safe sound descriptions, and re-imagines a song in another genre. Use when the user names an artist or genre the model will not understand, asks what a genre sounds like in production terms, or wants a song flipped into a different genre."
license: MIT
compatibility: "Model-aware: Suno v6, Udio, Google Flow Music (Lyria 3.5), ACE Music and ACE-Step, Mureka, ElevenLabs Eleven Music, MiniMax Music 3 and YuE2. Details per model in references/models.md."
metadata:
  author: Vocaler
  version: "1.2.0"
  category: ai-music-generation
  homepage: https://skills.vocaler.ai/genre-translator/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Genre Translator

Turns 'like that artist' or a niche genre name into the instruments, tempo and production words an AI model or a producer can use.

## When to use

- The user writes 'make it sound like [artist]'.
- A niche or regional genre needs explaining in production terms (e.g. amapiano, hyperpop, phonk, dabke, city pop).
- The user wants a song re-imagined in another genre.

## What to look for in the request

- The genre, artist or description.
- Target genre, if it is a flip.

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Identify the genre's defining traits: tempo range, rhythm signature, core instruments, vocal style, production signature, era.
2. Write a sound description of 25-60 words with no artist names.
3. For a flip: list what to keep (melody, lyrics, title) and what to replace (rhythm, instruments, vocal delivery), then the new description.
4. Offer one adjacent genre if the request is ambiguous.

## Rules

- Never put artist or song names into a generation prompt; describe the sound instead.
- Be specific about rhythm: it defines most genres more than instruments do (e.g. amapiano log drum; reggaeton dembow; drill sliding 808s and triplet hats).
- Respect regional genres: describe them accurately, without stereotypes.

## Model compatibility

Some choices here depend on the music model the user generates with. Look for the model and version in the request (for example "Suno v6", "Flow Music", "ElevenLabs", "Mureka O2", "ACE-Step"). What each model expects is in `references/models.md` (checked 17 Nov 2026); read it when a model is named.

- Shape the final description for the model: comma-separated descriptors for Suno, Mureka and ACE-Step captions; prose for Flow Music; the three-part form for MiniMax Music 3.
- Never pass artist names: ElevenLabs and Flow Music reject them outright, the others ignore or filter them.
- No model named: keep the default approach; mention the model only where it changes the advice.
- A model or version not in the reference: say so, use the model-neutral format, and suggest the user checks that model's current guide.

## Output format

```markdown
**Genre:** ... · **Tempo:** ... · **Rhythm:** ...
**Core sound:** ...
**Model-safe description:**
```
...
```
```

## Example

**Request:** Make it sound like Daft Punk.

**Response (abridged):**

```
"French house, 120-124 BPM, four-on-the-floor kick, filtered disco samples with sidechain pumping, talk-box and vocoder vocals, funky clavinet and slap bass, warm analog synths, 1990s-2000s club production"
```
