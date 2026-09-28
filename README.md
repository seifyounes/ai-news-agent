# AI news agent

Every morning at 9, a Claude Code agent reads the day's AI news, scores each story and keeps only the
best few for me. It has written 60+ daily digests since July 2026.

I set what it looks for and how it scores; Claude Code does the searching, checking and writing.

## How it works

1. **Search.** A scheduled Claude Code task runs at 9:00 (Cairo time). It searches the web for AI news
   from the last 24 hours in three areas: dev tools and agents, new models and research, and the
   business side (funding, pricing, launches).
2. **Score.** Each story gets a score from 1 to 10 based on five things: how fresh it is, its impact,
   whether it is really new, whether it can be explained with a real example, and how reliable the
   source is.
3. **Filter.** Only stories scoring 8 or more make it, with at most 8 a day. On a slow day it keeps
   fewer, and on an empty day it writes an empty digest instead of lowering the bar.
4. **Write.** It saves the digest as JSON with a short summary, key points, a longer explanation and a
   "why this matters for you" note for each story. My learning site reads that file.
5. **Tidy up.** It keeps the last 8 days of files and commits each digest to git.

The full instructions are in [`routine/news-routine.md`](routine/news-routine.md), and the scheduled
task that starts it is in [`routine/scheduled-task.md`](routine/scheduled-task.md).

## Example

[`samples/2026-09-27.json`](samples/2026-09-27.json) is a real digest: three stories, scored 9, 8 and 8.

## Is it any good?

The agent grades its own picks, so I am checking them by hand. [`eval/ratings.csv`](eval/ratings.csv)
lists the last 50 stories it kept. I rate each one myself, then
[`eval/agreement.py`](eval/agreement.py) reports how many I would have kept too and how far my scores
are from the agent's.

Result: _rating in progress._

## Limits

- It only runs while the Claude app is open on my laptop, so a few days are missing.
- Every story it shows scored 8 or more by its own judgment. The rating sheet above is how I check that.
- The website that shows the digests is private; this repo holds the agent and sample output.
