"""How often do I agree with the agent's picks?

Fill in my_score_1_10 and keep_yes_no in ratings.csv, then run:
    python eval/agreement.py
Every story in the sheet was kept by the agent (it scored 8 or more), so this measures
precision: of the stories it chose, how many would I have chosen too.
"""
import csv
import pathlib

rows = list(csv.DictReader(open(pathlib.Path(__file__).with_name("ratings.csv"), encoding="utf-8")))
rated = [r for r in rows if r["keep_yes_no"].strip().lower() in ("yes", "no")]
if not rated:
    raise SystemExit("No ratings yet: fill keep_yes_no (yes/no) in eval/ratings.csv")

kept = sum(r["keep_yes_no"].strip().lower() == "yes" for r in rated)
print(f"Rated {len(rated)} of {len(rows)} stories")
print(f"I would keep {kept} of {len(rated)} ({kept / len(rated):.0%})")

scored = [r for r in rated if r["my_score_1_10"].strip()]
if scored:
    gaps = [abs(int(r["agent_score"]) - int(r["my_score_1_10"])) for r in scored]
    print(f"Average score gap: {sum(gaps) / len(gaps):.1f} points over {len(scored)} stories")
    by_cat = {}
    for r in rated:
        c = by_cat.setdefault(r["category"], [0, 0])
        c[0] += r["keep_yes_no"].strip().lower() == "yes"
        c[1] += 1
    for cat, (k, n) in sorted(by_cat.items()):
        print(f"  {cat}: kept {k} of {n}")
