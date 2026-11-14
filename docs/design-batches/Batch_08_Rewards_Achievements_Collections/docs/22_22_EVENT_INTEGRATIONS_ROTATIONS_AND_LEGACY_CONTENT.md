# 22 — Events, Live Operations and Retired Content

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Integration
Future Batch 10 incident engine, Batch 12 event calendar, and Batch 13 seasons may publish reward source receipts. Each event has a stable `eventId`, `edition`, `rewardProgramId`, UTC window, content snapshot and eligible player cohorts. Batch 8 never implements the story or economic event logic itself.

## Rotating cosmetics
Time-limited availability may apply to *acquisition*, not permanent ownership. Once an event cosmetic is legitimately granted, it should remain owned and displayed unless a narrowly defined rights/abuse exception is invoked. Show end dates and alternative paths for nonexclusive utility rewards.

## Content retirement
Archiving a program hides new claims unless the published claim grace period remains open. Existing receipts and album edition snapshots stay queryable. Admin tools require side-by-side diff of reward policy scope and active player entitlements before retirement.

## Backfill
If a verified event result arrives late, accept only within the event's documented settlement rules; log any exception and trace owner approval. Never invent awards to 'fix' missing logs without examining durable source evidence.

## Compensation
Support operator-issued grants for verified outages via a dedicated audited service path with two-person approval, maximum grant values, no caller-selected player ID in browser client, and durable source keys such as `(incident,player,compensationBatch)`. `compensation` never masquerades as normal achievement completion.
