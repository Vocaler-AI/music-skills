---
name: song-structure
description: "Plans or edits song form, including section order, bar counts, hook timing and runtime. Use when the user asks where sections should go, what to cut, or how to meet a target duration."
license: MIT
compatibility: "Model-aware: Suno v6, Udio, Google Flow Music (Lyria 3.5), ACE Music and ACE-Step, Mureka, ElevenLabs Eleven Music, MiniMax Music 3 and YuE2. Details per model in references/models.md."
metadata:
  author: Vocaler
  version: "1.2.0"
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

- Genre and listening context, tempo, meter and the note value counted by the BPM.
- Existing sections or timestamps, including any pickup, count-in or tail that counts toward runtime.
- Target duration, hook deadline, required sections and any tempo or meter changes.

Do not interview the user. If something is missing, make a sensible assumption, state it in one line, and deliver. Ask only when the answer would change the result completely.

## Workflow

1. For an edit, map the current form and note where it misses the brief. For a new plan, choose a form that serves the genre and the intended payoff.
2. Calculate seconds per bar as beats per bar (counted in the BPM's beat unit) × 60 ÷ BPM. In 6/8 with a dotted-quarter BPM, use two beats per bar. Calculate each constant-tempo and meter span independently. Sum unrounded timings and add any pickup or tail outside the counted bars once.
3. Work back from hard limits. Set aside time for fixed sections and any included pickup or tail, then allocate the remaining bars. Check the first hook at its actual entry, which can fall inside a section.
4. Give every section a purpose. Place the peak where the song needs it. Emotional intensity and arrangement density can diverge, such as in a stripped final chorus.
5. Show the resulting section starts and total. For edits, name the cuts or additions and why they work. If fixed constraints conflict, identify the conflict and the smallest tradeoff that would make the plan fit.

## Rules

- Show the timing calculation and label any assumed meter, beat unit or tempo. For free or changing tempo without enough timing information, label the timestamps as estimates or use supplied section times.
- Use the phrase lengths the music needs. Four-, eight- and sixteen-bar sections are useful defaults in many styles.
- Treat hook timing by listening context as a preference unless the user gives a deadline.

## Model compatibility

Some choices here depend on the music model the user generates with. Look for the model and version in the request (for example "Suno v6", "Flow Music", "ElevenLabs", "Mureka O2", "ACE-Step"). What each model expects is in `references/models.md` (checked 17 Nov 2026); read it when a model is named.

- Check the planned length fits the model: Lyria 3 Clip 30 s, Lyria 3 Pro and 3.5 about 3 min, Mureka and MiniMax Music 3 about 5 min, ElevenLabs and ACE-Step up to 10 min.
- For Lyria 3 Pro and 3.5 the plan can become timestamps; for ElevenLabs, composition-plan sections with exact durations.
- No model named: keep the default approach; mention the model only where it changes the advice.
- A model or version not in the reference: say so, use the model-neutral format, and suggest the user checks that model's current guide.

## Output format

```markdown
| Section | Bars | Start | Purpose and energy |
|---------|------|-------|--------------------|

**Timing** — [meter, BPM beat unit, seconds per bar, total including any tail]
**First hook or chorus** — [time, when present]
**Changes** — [for an edit, cuts or additions and why]
```

## Example

**Request:** Cut a 4/4 song at 100 quarter-note BPM to 45 seconds including a 0.8-second tail. Keep both verses and choruses, with the first chorus by 15 seconds. Current bars are 4 / 8 / 8 / 4 / 8.

**Response (abridged):**

```
At 2.4 s per bar, 44.2 s of music allows 18 full bars.
Intro 2 (0.0 s) → V1 4 (4.8 s) → Chorus 4 (14.4 s) → V2 4 (24.0 s) → Final chorus 4 (33.6 s).
Total 44.0 s with tail. Cut the intro and first verse to reach the first chorus sooner. Use the strongest four-bar phrase of each chorus.
```
