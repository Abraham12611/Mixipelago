# 37 — QA Matrix: Unit, Integration, Property, Browser and Security

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Unit invariants
- Auto-serve oldest compatible active order; no service of idle board drinks; no double consumer on one merge result.
- `coconut-cove-001` exactly two fixed visible orders; terminal win before same-tick loss; no after-win replacement.
- Satisfaction clamped; inactive timed modifiers are zero; penalties never triggered by background tab or pause.
- VIP probability sums/clamps; zero-weight entries excluded; ordering of input JSON keys irrelevant.
- Repeat receipt/claim same key returns original result; changed command body with same key conflicts.
- Loyalty tier thresholds are monotonic; offline preview never produces trusted relationships or coins.

## Integration tests
Server result verification -> one observation -> one shop reputation update; Batch 6 wallet unaffected by cosmetic guest reaction; skill change mid-reservation does not reroll; Batch 8 gift milestone yields one entitlement; retired NPC history remains queryable; mission order count cannot exceed configured allowed slots.

## Property/fuzz tests
Generate thousands of random order event sequences and assert served quantity never exceeds ordered quantity, no negative counters, one source output consumed once, and all resulting orders are properly terminalized. Generate thousands of reputation/loyalty input vectors to assert bounds and idempotency.

## Browser/device tests (owner-directed manual)
320 px Android Chrome, iPhone Safari, desktop Chromium/Firefox/Safari, high text zoom and reduced motion; customer cards must not obscure tabletop. Compare portraits and dialogue across transition states, customer reaction audio concurrency and tab resume correctness. Engineers provide test instructions/results to owner and **do not assert manual approval** themselves.

## Release gates
No trusted customer feature without authenticated source receipt validation, RLS, per-player uniqueness tests, rate limit, observability, feature gate default OFF, rollback procedure and owner UX signoff.
