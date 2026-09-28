# Daily AI News routine

You are generating a **Daily AI News** digest for a personal learning website. Run this
end-to-end, autonomously, then stop. Work from the project root.

## Goal

Gather the **strongest AI/tech news from roughly the last 24 hours**, validate each item, keep
only the best, and write them into `content/news/<today>.json` so the site can show them. Quality
over quantity — a short, high-signal digest beats a long one.

## What the reader cares about (tune search + scoring to this)

- **AI dev tools & agents** — Claude Code, Cursor, Copilot, MCP, coding agents, n8n/automation, developer platforms.
- **New models & research** — OpenAI / Google / Anthropic (and serious others) model releases, capabilities, benchmarks, product launches.
- **Business & monetization** — startups, funding, pricing, notable industry moves, the opportunity angle for freelancers/founders.

Skip pure creator/content-tooling news, and skip generic "AI hype" with no substance.

## Gather

Use `WebSearch` (and `WebFetch` to confirm details) to find fresh items. **Prefer reliable
sources:** official company blogs, product release notes, major tech publications, developer
platforms, AI research/product announcements, and credible industry news. Cast a wide-enough net
(several searches across the three areas) to have real candidates to filter.

## Evaluate each candidate (score 1–10)

Score each criterion **separately**, 1–10:

- **Freshness**: announced in the last ~24h (10), this week (6), older and only resurfacing (3).
- **Impact**: changes what a developer, freelancer or small business does or pays (9–10); affects
  a narrow group (5–6); industry gossip or a big company's internal news (2–4).
- **Novelty**: a real launch, release or result (9–10); an update to something already known (5–6);
  a restatement, opinion piece or roundup of old news (1–3).
- **Practicality**: you can name a concrete thing the reader could try, change or decide this week
  (9–10); interesting but no action (5–6); nothing to do with it (1–3).
- **Source quality**: you opened the primary source with `WebFetch` and it says what you claim
  (9–10); a reputable outlet reporting on it (7); a blog, aggregator or social post only (≤ 4).
  If you could not open any source for an item, drop it.

The item's score is the **average of the five, rounded down**. Keep an item only if that score is
**≥ 8 and no single criterion is below 6**. Most days, most candidates should land at 5–7; a day
where everything scores 8+ means you are scoring too generously, so go back and re-score.

Calibration: a new Claude Code release with a feature developers can use today is about 9. A model
release from a major lab with public benchmarks and API access is 8–9. A funding round with no
product change is about 5. An "AI will change everything" op-ed is about 3. A story repeated from
earlier in the week with no new facts is about 4.

Keep at most **8**. If fewer clear the bar, keep fewer — never pad. Do not fabricate anything;
every item must trace to a real, linkable source.

## Write the file

Write (overwrite) `content/news/<YYYY-MM-DD>.json` using **today's date in Africa/Cairo**, exactly
this shape:

```json
{
  "date": "YYYY-MM-DD",
  "generatedAt": "<ISO timestamp with +03:00 offset>",
  "items": [
    {
      "id": "kebab-slug",
      "title": "Concise, specific headline (no hype)",
      "score": 9,
      "category": "dev-tools | models | business",
      "summary": "2–3 sentences: what it is + why it matters. Plain, hype-free English. Shown on the card.",
      "audience": "developers · founders",
      "image": "https://…  (the source article's og:image; null if you can't get one)",
      "sources": [{ "label": "Publisher name", "url": "https://…" }],
      "tldr": "One punchy, fun sentence — the hook at the top of the detail page.",
      "keyPoints": ["3–5 short, scannable takeaways", "one fact each", "no fluff"],
      "whyForYou": "1–3 sentences: concretely how THIS is useful for the reader (see profile below). A real recommendation, not a summary.",
      "deepDive": "2–3 short paragraphs (separated by blank lines) that fully explain it so the reader never needs to open the sources. Plain, a little fun, never overwhelming."
    }
  ]
}
```

### The detail fields (this is the on-site read — make it good)

Every item is now read **on the site**, not at the source. So beyond `summary`, fill:
- **`tldr`** — the one-line hook. Punchy and a little fun; makes the reader want to read on.
- **`keyPoints`** — 3–5 crisp bullets the reader can skim in seconds.
- **`whyForYou`** — the part the reader asked for: *how is this helpful for me?* Give a concrete, honest
  take (or "probably skip unless…"). Don't force relevance — if it's only tangentially useful, say so.
- **`deepDive`** — the fuller explanation (2–3 short paragraphs) so the sources are optional.

Keep everything **fun to read, skimmable, and not overwhelming** — short sentences, concrete
examples, no wall of text, no hype.

### About the reader (ground `whyForYou` in this)

A solo **freelance developer** who builds **Flutter + Supabase** mobile apps and **Next.js** client
websites, **with Claude Code**. Cares about: **applied AI engineering** (APIs, agents, RAG, MCP,
evals, cost), **AI dev tools**, shipping fast, and **monetization** (subscriptions, client work).
Frame usefulness through: "does this change how I build/ship, what I pay, a tool I use, or a way
to make money?"

Rules:
- **English**, clear and **hype-free** (match the course's vendor-neutral voice). No emoji in text.
- `category` must be exactly `dev-tools`, `models`, or `business`.
- 1–3 `sources` per item, most authoritative first.
- For `image`, try to capture the primary source's cover image (`og:image`); if you can't get it
  reliably, set `image` to `null` — the site shows a clean fallback.
- **No scripts, no hooks, no calls to action** — this is a reading digest only.

## Housekeeping

- **Prune** `content/news/`: keep only today + the previous 7 dates; delete older `*.json`.
- Optionally `git add content/news && git commit -m "news: digest for <date>"` for history
  (skip silently if git isn't available; never push).
- If the day yields no item scoring ≥ 8, write a file with an empty `items` array (the site shows
  a graceful empty state) — do not lower the bar.
