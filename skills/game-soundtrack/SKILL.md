---
name: game-soundtrack
description: "Designs music for games: a soundtrack plan by location and game state, adaptive layers (explore, tension, combat), seamless loops, stingers and leitmotifs, with prompts for each cue. Use when a game developer or modder needs a music plan, loopable tracks, or a score for a level, menu or boss."
license: MIT
compatibility: "Model-aware: Suno v6, Udio, Google Flow Music (Lyria 3.5), ACE Music and ACE-Step, Mureka, ElevenLabs Eleven Music, MiniMax Music 3 and YuE2. Details per model in references/models.md."
metadata:
  author: Vocaler
  version: "1.1.0"
  category: music-for-creators
  homepage: https://skills.vocaler.ai/game-soundtrack/
  repository: https://github.com/Vocaler-AI/music-skills
---

# Game Soundtrack Designer

Plans a game score: themes per area, adaptive layers for explore, tension and combat, seamless loops and stingers for every event.

## When to use

- Planning a soundtrack for a game or a level.
- Needing loopable music or adaptive layers.
- Writing a cue list for a composer or an AI model.

## What to look for in the request

- Genre of game, art style, setting.
- Areas or levels, key events, engine (Unity, Unreal, Godot).
- Budget: number of cues.

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. Define a main theme (leitmotif) and how it is varied per area.
2. Build the cue list: menu, each area, combat, boss, victory, defeat, stingers.
3. For adaptive cues, describe stems that share tempo and key and can be layered (base, tension, combat).
4. Specify loop length in bars and how to make the loop seamless (no reverb tail at the end, same chord at both ends).
5. Write a prompt per cue.

## Rules

- Loops must not tire: 1-3 minutes for exploration; vary the instrumentation inside the loop.
- Keep all layers of one cue at the same tempo and key.
- Match the game's era and art style (8-bit chiptune, orchestral fantasy, synth noir).

## Model compatibility

Some choices here depend on the music model the user generates with. Look for the model and version in the request (for example "Suno v6", "Flow Music", "ElevenLabs", "Mureka O2", "ACE-Step"). What each model expects is in `references/models.md` (checked 17 Nov 2026); read it when a model is named.

- For loops and cues of exact length, prefer ElevenLabs composition plans or ACE-Step's duration setting.
- Check the plan allows commercial use and downloads (Udio cannot be downloaded); MiniMax Music 3 needs attribution.
- No model named: keep the default approach; mention the model only where it changes the advice.
- A model or version not in the reference: say so, use the model-neutral format, and suggest the user checks that model's current guide.

## Output format

```markdown
**Theme:** ...
| Cue | Trigger | Length / loop | Layers | Prompt |
**Implementation notes:** ...
```

## Example

**Request:** Cozy farming game, spring area.

**Response (abridged):**

```
Spring loop 96 bars at 100 BPM in F major: acoustic guitar + flute melody (theme variation 1), layer 2 adds light percussion when the player runs; rain variant drops to piano.
```
