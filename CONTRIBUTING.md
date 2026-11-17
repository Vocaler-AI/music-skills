# Contributing

Thanks for helping musicians and creators get more out of their AI agents.

## Add a skill

1. Pick a name: lowercase words joined by hyphens (`lyric-translator`). Check the planned list in the README
   and open an issue to claim it, so two people don't write the same skill.
2. Add the skill's entry to `site/music_skills_data.py` (title, category, description, workflow, rules,
   output format, one example). `skills/<name>/SKILL.md` and its page on https://skills.vocaler.ai are both generated from it.
3. Run `python3 site/build.py --repo .` to regenerate the `skills/` folder and check the result.
4. Open a pull request. Merged skills go live on https://skills.vocaler.ai automatically.

## What makes a good skill

- **The description decides when it loads.** Say what it does and the words a user would type when they need it.
- **Craft over chatter.** Concrete rules a working musician would agree with; no filler.
- **Deliver, don't interview.** Make sensible assumptions, state them in one line, and produce the result.
- **Honest.** Never invent facts, codes, credits or BPMs of released songs; never quote copyrighted lyrics.
- **No artist names in generation prompts.** Describe the sound instead.

## Code of conduct

Be kind and constructive. Music is for everyone.
