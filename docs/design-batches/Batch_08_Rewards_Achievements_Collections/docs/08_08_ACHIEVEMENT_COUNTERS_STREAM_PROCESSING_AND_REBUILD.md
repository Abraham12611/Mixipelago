# 08 — Counters, Projections and Replay-safe Evaluation

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Counter model
Maintain a source fact table/inbox keyed by trusted `eventId`. Aggregate per player, achievement definition and scope. Prefer counters derived from authoritative events or tables, not user-submitted `progress` numbers. A counter revision increases monotonically within a scope; never increment directly from a browser click.

## Count semantics
- `orders_served_verified`: number of **distinct committed order IDs** from accepted sessions, not number of repeated events.
- `missions_first_cleared`: distinct mission entitlements, not total accepted attempts.
- `three_star_missions`: distinct mission IDs whose best verified stars >= 3, with max-star updates idempotent.
- `unique_drinks_discovered`: distinct published recipe IDs with verified discovery, not merged sprite counts.
- `shop_cosmetics_owned`: count of distinct eligible durable item IDs, not equip actions.

## Ingestion flow
Authenticate service event → check schema and signature/producer → insert event into consumer inbox with unique event ID → update aggregate only on first delivery → check threshold crossings → create achievement achievement-stage rows and entitlements → emit outbox. Put source event and consumer checkpoint in same transaction or use a durable replay offset with idempotent processing.

## Late data and replay
Events may arrive out of order. Commutative counts can converge if uniqueness is maintained. Best-star projection uses `MAX` per mission; collection counts use inventory ownership. When policy logic changes, rebuild projections from immutable authoritative facts under a **new** definition epoch, without reissuing old claims. Always preserve prior verified achievements as historical awards unless fraud adjudication justifies revocation.

## Backfill rule
Only backfill from server-verified durable receipts and a declared time range. Do not backfill from alpha preview cookies, local leaderboard screenshots or unverified import logs. Every batch backfill must be dry-run and include exact sampled count, divergence report, and rollback controls.

## Performance
Use indexed source facts and materialized aggregates; avoid scanning all mission results on every screen render. Use a bounded batch process for backfills and an outbox for notifications. Cache public definitions by catalog version, never cache mutable entitlement authority across actors.
