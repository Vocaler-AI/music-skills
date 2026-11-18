#!/usr/bin/env python3
"""Rate skills from several test runs.

    python3 tests/rate.py --after RUN_A RUN_B [--before RUN_C RUN_D] [--md ratings.md]

Averages every run per skill (a skill with two cases averages both), so one lucky
or unlucky answer does not decide a rating. Score is 0-10; craft is the judge's 1-5.
"""
import argparse
import json
import pathlib
from collections import defaultdict


def load(dirs):
    by = defaultdict(list)
    for d in dirs or []:
        for p in pathlib.Path(d).glob("*.json"):
            r = json.loads(p.read_text())
            if "error" not in r:
                by[r["skill"]].append(r)
    return by


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--after", nargs="+", required=True)
    ap.add_argument("--before", nargs="*")
    ap.add_argument("--md")
    a = ap.parse_args()
    after, before = load(a.after), load(a.before)
    rows = ["| Skill | Rating (0-10) | Craft (1-5) | Before | Change | Runs | Routed | Main remaining issue |",
            "|---|---|---|---|---|---|---|---|"]
    tot_b, tot_a, n = 0, 0, 0
    for skill in sorted(after, key=lambda k: -mean([r["score"] for r in after[k]])):
        rs = after[skill]
        s, c = mean([r["score"] for r in rs]), mean([r["craft"] for r in rs])
        b = mean([r["score"] for r in before.get(skill, [])])
        routed = sum(r["routed"] for r in rs)
        worst = min(rs, key=lambda r: r["score"])["improve"].split(". ")[0][:110]
        if b is not None:
            tot_b, tot_a, n = tot_b + b, tot_a + s, n + 1
        rows.append(f"| {skill} | {s:.1f} | {c:.1f} | {'' if b is None else f'{b:.1f}'} | "
                    f"{'new' if b is None else f'{s - b:+.1f}'} | {len(rs)} | {routed}/{len(rs)} | {worst} |")
    allv = [mean([r["score"] for r in v]) for v in after.values()]
    summary = f"\nAll {len(allv)} skills: average {mean(allv):.2f}."
    if n:
        summary += f" The {n} skills that existed before: {tot_b / n:.2f} -> {tot_a / n:.2f} ({(tot_a - tot_b) / n:+.2f})."
    out = "\n".join(rows) + summary
    print(out)
    if a.md:
        pathlib.Path(a.md).write_text(out + "\n")


if __name__ == "__main__":
    main()
