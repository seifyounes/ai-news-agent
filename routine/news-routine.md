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

Score on: **Freshness** (last ~24h or newly relevant today), **Impact** (does it affect
developers, freelancers, creators, businesses, users?), **Novelty** (genuinely new, not repeated
hype), **Practicality** (can it be explained with a real example/use case?), and **Source
quality** (reliable?).

**Only keep items scoring ≥ 8.** Keep at most **8**. If fewer than 8 clear the bar, keep fewer —
never pad. Never include an item below 8. Do not fabricate anything; every item must trace to a
real, linkable source.

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
