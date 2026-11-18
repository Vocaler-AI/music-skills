# Skill tests

Each case in `cases.json` is a realistic request plus the checks a good answer must meet.
`run.py` runs every case in a real agent (Claude Code, headless) in a fresh project with **all**
skills installed, so a case tests both routing (the right skill loads) and the answer. A separate
judge model then grades each check (pass / partial / fail) and rates overall craft 1-5.

```bash
python3 tests/run.py --out runs/a          # all cases (needs the `claude` CLI signed in)
python3 tests/run.py --out runs/b          # a second sample: single runs vary by about ±1.5
python3 tests/rate.py --after runs/a runs/b --md ratings.md
python3 tests/run.py --only lyrics-writer  # one case while you work on a skill
```

Score per case (0-10) = 6 × share of checks met + (craft − 1). Ratings average every run of a skill.
A full run costs a few dollars of agent usage. Ratings measure written answers judged by a model,
not generated audio.

## Adding a case

Write the request a real user would type, and 4-6 checks that a working musician would agree
separate a good answer from a weak one. Prefer checks about the skill's job (counts add up, the
title is kept, no artist names reach a prompt) over checks about wording.
