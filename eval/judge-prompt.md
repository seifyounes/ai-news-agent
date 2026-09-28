# Blind second-judge check

A fresh model, with no web access and no view of the agent's scores, re-scores stories the agent
kept, reading only each story's date, title, category, summary and source name. It uses the same
five criteria. The share it would also keep (8 or more) is the agreement rate.

This is a model checking a model, not a human rating. It measures how generous the agent's own
scoring is.

## Prompt used

> You are an independent judge for an AI-news digest. [...] Score each item from 1 to 10 overall,
> judging it as of its own date, on these five criteria: Freshness (new that day), Impact (does it
> affect developers, freelancers, businesses or users), Novelty (genuinely new, not repeated hype),
> Practicality (can it be explained with a real example or use), and Source quality (how reliable
> the named source is). A digest keeps only items scoring 8 or more, so be strict: give 8+ only to
> items you would really keep.

The reader profile given to the judge: a solo freelance developer who builds Flutter + Supabase apps
and Next.js client websites with Claude Code, and cares about AI dev tools and agents, new models
and research, and the business side. Generic AI hype and creator-tooling news are out of scope.

## Results

| Run | Stories | Judge kept (8+) | Judge average |
|---|---|---|---|
| Before tightening (digests 2026-09-09 to 09-27) | 50 | 10 (20%) | 6.3 |
| After tightening (from 2026-09-29) | pending | | |

The first run showed the agent scored its own picks too generously. On 2026-09-28 the scoring
rules were tightened: each criterion scored separately with anchors, the item's score is the
average rounded down, no criterion may be below 6, the primary source must be opened, and a day
where everything scores 8+ is treated as a sign of over-scoring.
