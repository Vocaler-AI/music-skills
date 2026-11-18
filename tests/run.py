#!/usr/bin/env python3
"""Run the skill tests in a real agent and grade the answers.

Every case is run in a fresh project with ALL skills installed, so the test
covers both parts of a skill's job: being picked for the request (routing) and
answering it well. A separate judge model then scores each check.

    python3 tests/run.py                       # all cases, results in tests/results/
    python3 tests/run.py --only lyrics-writer  # one case
    python3 tests/run.py --skills skills --agent-model sonnet --judge-model opus -j 6

Needs the Claude Code CLI (`claude`) signed in. Each case costs a few cents.
Scores per case:
  routed   the expected skill was loaded (yes / no)
  checks   share of checks met (pass = 1, partial = 0.5)
  craft    the judge's 1-5 rating of overall quality for a working musician
  score    0-10 = 6 x checks + craft (craft 1-5 mapped to 0-4)
"""

import argparse
import concurrent.futures as cf
import json
import pathlib
import shutil
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent

JUDGE = """You are grading one answer from an AI assistant that used a music skill. Be strict and fair; you are
a working songwriter and producer. Grade only what is in the answer.

REQUEST:
{prompt}

ANSWER:
{answer}

CHECKS (grade each: "pass", "partial" or "fail", with a one-line reason):
{checks}

Then rate overall craft 1-5 (5 = what a top professional would hand a client; 3 = usable but generic or with a
notable flaw; 1 = wrong or unusable), and name the single most important improvement.

Reply with ONLY this JSON:
{{"checks":[{{"check":"...","grade":"pass|partial|fail","why":"..."}}],"craft":N,"improve":"..."}}"""


def run_agent(case, skills, model, workdir):
    proj = pathlib.Path(workdir) / case["id"]
    (proj / ".claude").mkdir(parents=True)
    shutil.copytree(skills, proj / ".claude" / "skills")
    out = subprocess.run(
        ["claude", "-p", case["prompt"], "--model", model, "--output-format", "stream-json", "--verbose",
         "--allowedTools", "Skill Read Glob Grep Bash(python3:*)"],
        cwd=proj, capture_output=True, text=True, timeout=600)
    used, answer, cost = [], "", 0.0
    for line in out.stdout.splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("type") == "assistant":
            for c in d["message"]["content"]:
                if c.get("type") == "tool_use" and c["name"] == "Skill":
                    used.append(c["input"].get("skill"))
        if d.get("type") == "result":
            answer, cost = d.get("result", ""), d.get("total_cost_usd") or 0.0
    return used, answer, cost


def judge(case, answer, model):
    checks = "\n".join(f"{i}. {c}" for i, c in enumerate(case["checks"], 1))
    with tempfile.TemporaryDirectory() as empty:  # no skills: the judge must not load any
        out = subprocess.run(
            ["claude", "-p", JUDGE.format(prompt=case["prompt"], answer=answer, checks=checks),
             "--model", model, "--output-format", "json", "--allowedTools", ""],
            cwd=empty, capture_output=True, text=True, timeout=600)
    res = json.loads(out.stdout)
    text = res["result"]
    g = json.loads(text[text.index("{"): text.rindex("}") + 1])
    return g, res.get("total_cost_usd") or 0.0


def one(case, args, workdir):
    used, answer, c1 = run_agent(case, args.skills, args.agent_model, workdir)
    g, c2 = judge(case, answer, args.judge_model)
    pts = {"pass": 1.0, "partial": 0.5}
    share = sum(pts.get(x["grade"], 0) for x in g["checks"]) / max(len(g["checks"]), 1)
    craft = int(g["craft"])
    return {
        "id": case["id"], "skill": case["skill"], "routed": case["skill"] in used, "skills_used": used,
        "checks": round(share, 3), "craft": craft, "score": round(6 * share + (craft - 1), 1),
        "improve": g["improve"], "grades": g["checks"], "answer": answer, "cost": round(c1 + c2, 3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills", default=str(HERE.parent / "skills"))
    ap.add_argument("--cases", default=str(HERE / "cases.json"))
    ap.add_argument("--out", default=str(HERE / "results"))
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--agent-model", default="sonnet")
    ap.add_argument("--judge-model", default="opus")
    ap.add_argument("-j", type=int, default=6)
    args = ap.parse_args()
    cases = [c for c in json.load(open(args.cases)) if not args.only or c["id"] in args.only]
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as workdir, cf.ThreadPoolExecutor(args.j) as pool:
        futs = {pool.submit(one, c, args, workdir): c for c in cases}
        for f in cf.as_completed(futs):
            c = futs[f]
            try:
                r = f.result()
            except Exception as ex:  # keep going; report the failure
                r = {"id": c["id"], "skill": c["skill"], "error": repr(ex)}
            (out / f"{c['id']}.json").write_text(json.dumps(r, indent=2, ensure_ascii=False))
            print(f"{r['id']:28} " + (f"routed={'Y' if r['routed'] else 'N'} checks={r['checks']:.2f} craft={r['craft']} "
                                      f"score={r['score']:4.1f}  {r['improve'][:90]}" if "error" not in r else r["error"][:120]),
                  flush=True)


if __name__ == "__main__":
    main()
