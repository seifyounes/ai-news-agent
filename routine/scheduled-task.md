---
name: daily-ai-news
description: Generate the Daily AI News digest for the AI Learning Website (runs 9am daily)
---

Generate today's "Daily AI News" digest for the learning website. Work autonomously and stop when the file is written.

1. Read `scripts/news-routine.md` in the project and follow it EXACTLY — it is the full spec: the topics the reader cares about (AI dev tools & agents, new models & research, business/monetization), the reliable-source guidance, the 1–10 scoring on Freshness / Impact / Novelty / Practicality / Source quality, the rule to keep ONLY items scoring 8 or higher (max 8, never pad), the exact JSON schema, English + hype-free + digest-only (no scripts/hooks), and the housekeeping/pruning steps.
2. Use WebSearch (and WebFetch to confirm details / capture each source's og:image) to gather fresh news from roughly the last 24 hours across those three areas.
3. Score every candidate; keep only those ≥ 8 (at most 8). Write them to `content/news/<YYYY-MM-DD>.json` using today's date in Africa/Cairo, in the exact schema from the spec. Overwrite the file if it already exists.
4. Prune `content/news/`: keep only today + the previous 7 dates; delete older *.json files.
5. Never fabricate — every item must trace to a real, linkable source. If nothing clears the ≥8 bar, write the file with an empty "items" array (do not lower the bar).