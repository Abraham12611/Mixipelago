# 10 — Spawn Queue, Deterministic Content Director, Fairness and Reachability

## Source of truth

Batch 2 document `08_SPAWN_NEXT_QUEUE_AND_GAME_DIRECTOR.md` owns actual launch eligibility, queue advancement, PRNG state, cooldown and cancellation. Batch 3 augments it with **drink catalog inputs** and future recipe reachability checks.

## Alpha generation

Current and next tiers are visible. Config includes `spawn.pool` weighted tiers and an optional curated `firstItems` prefix. Initial tutorials should spawn tier 1 only or occasionally tier 2 as mission author explicitly configures. `nextQueue` advances exactly once only on accepted shot. Use a documented fixed PRNG, never rendering-layer randomness. Same session seed + mission config + catalog hash produces identical tier sequence.

## Weighted tables

Store stable arrays with non-negative finite weights and `sum > 0`, sort or preserve canonical serialization order. Normalize deterministically without depending on object-key enumeration across separate runtimes. Do not introduce a random draw to decide visual variants if that draw shifts the gameplay PRNG sequence; use separate cosmetic RNG or deterministic hash.

## Reachability lower bounds

Assuming only tier-1 inputs and no preexisting bodies: `cost(tier n)=2^(n-1)`. Thus one tier-5 requires 16 tier-1 equivalents; one tier-8 requires 128. A mission with 15 total shots and no starting bodies cannot demand production of a tier-5 under this assumption. If the order system auto-consumes intermediate tiers, add *all served quantities* to the resource budget rather than treating input units as reusable. Example: serve one tier-3 and one tier-4 from scratch requires at least 4+8=12 tier-1 equivalents, not 8.

This is a necessary feasibility lower bound, not a sufficient solvability proof: collisions, board space, sequence ordering, boundary limits, and mandatory serving can still block completion.

## Reachability analyzer

Authoring-time tool should: (1) compile immutable catalog; (2) check requested target IDs/tiers exist and are reachable under active family; (3) compute tier-1 equivalent lower bound and any available seeded units; (4) compare to shot budget and spawn pool; (5) run scripted setup solutions or search heuristics; (6) run seeded Monte Carlo agents to estimate completion distribution; (7) flag 'unproven' missions requiring owner manual tests. Never auto-publish an unproven mission solely because a probabilistic bot succeeded once.

## Fairness director proposals (later)

Limit excessively long streaks of unhelpful spawns, or use authored 'bag' generation. Must preserve seed determinism and be displayed consistently in replay. Do not secretly modify odds based on current user's available money, whether they purchased boosters, or inferred frustration. In competitive mode, everyone receives the same initial state and immutable queue seed.

## Queue/collision edge cases

- Rejected shot due to blocked launch -> current/next unchanged.
- Retry same fixed-seed mission -> queue regenerates identically.
- Paused browser tab -> no queue drift.
- Art load failure -> no PRNG draw or queue advancement.
- Future recipe branch selection -> explicit separate command and state, not a random alternate output.
- Tournament with old content -> use pinned catalog and rules versions, or disallow submission with a clear compatibility message.

## Tutorial fixture

Mission `coconut-cove-001` from Batch 1 starts with two tier-1 bodies and has `firstItems` of five tier-1. It requests tier-2 and tier-3 outputs. This is a *candidate fixture*, not automatically proven solvable, because service priority can consume newly formed tier-2 before tier-3 is produced. Test a recorded valid input trace; if none exists, revise seeded setup/order sequence with owner approval.
