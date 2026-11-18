#!/usr/bin/env python3
"""Compare two test runs: python3 tests/compare.py BEFORE_DIR AFTER_DIR [--md report.md]"""
import json
import pathlib
import sys


def load(d):
    return {json.loads(p.read_text())["id"]: json.loads(p.read_text()) for p in pathlib.Path(d).glob("*.json")}


def main():
    a, b = load(sys.argv[1]), load(sys.argv[2])
    rows = ["| Skill | Before | After | Change | Craft before → after | Routed |", "|---|---|---|---|---|---|"]
    tot_a = tot_b = n_both = 0
    for k in sorted(b):
        rb = b[k]
        if "error" in rb:
            rows.append(f"| {k} | | error | | | |")
            continue
        ra = a.get(k)
        if ra and "error" not in ra:
            d = rb["score"] - ra["score"]
            tot_a += ra["score"]
            tot_b += rb["score"]
            n_both += 1
            rows.append(f"| {k} | {ra['score']:.1f} | {rb['score']:.1f} | {d:+.1f} | {ra['craft']} → {rb['craft']} | {'yes' if rb['routed'] else 'NO'} |")
        else:
            rows.append(f"| {k} (new) | | {rb['score']:.1f} | | {rb['craft']} | {'yes' if rb['routed'] else 'NO'} |")
    allb = [r["score"] for r in b.values() if "error" not in r]
    summary = (f"\nCompared skills: {n_both}. Average before {tot_a / max(n_both, 1):.2f}, after {tot_b / max(n_both, 1):.2f}. "
               f"All skills after: {sum(allb) / len(allb):.2f} over {len(allb)}.")
    out = "\n".join(rows) + summary
    print(out)
    if "--md" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--md") + 1]).write_text(out + "\n")


if __name__ == "__main__":
    main()
