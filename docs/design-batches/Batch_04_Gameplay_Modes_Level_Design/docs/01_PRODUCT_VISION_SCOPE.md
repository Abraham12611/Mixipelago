# 01 — Gameplay Modes and Level Design: Vision and Scope

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Product promise
Mixipelago is an accessible physics-driven merge shooter with a deep mission campaign. A player should learn to aim in seconds, enjoy expressive collision physics, and progress through a fair, legible sequence of increasingly varied challenges. Modes should express a different decision problem using the SAME physics and drink logic rather than multiplying disconnected minigames.

## What is already canonical from Batches 1–3
- The alpha table is a top-down, low-damping 2D rigid-body space rendered as 2.5D artwork, with 60 Hz fixed simulation and versioned presets. Phaser renders and handles input; Rapier 2D owns contact physics.
- The initial catalog contains precisely eight drinks, tiers 1–8: `citrus-shot`, `sunny-lemon`, `sunset-splash`, `blossom-fizz`, `coral-martini`, `mint-lagoon`, `ocean-cloud`, `crown-of-isles`.
- Compatible, active, same-tier bodies merge `t+t → t+1` for tiers 1–7. Tier 8 is terminal; unlike tiers physically collide and deflect, never merge.
- A NEW eligible merge output auto-serves to the oldest matching open order BEFORE that result can chain-merge. Existing idle drinks are not retroactively auto-served.
- A merge awards output-tier points; order fulfillment awards score plus alpha-only **preview coins**. Client credits are NOT a trusted wallet. Run seed, physics rules version, content/catalog version, and mission version are recorded.
- The danger line has per-body consecutive-step grace; win is evaluated after merge/order reduction and before same-tick loss. Pause and hidden-tab time do not consume active-time allowance.
- `coconut-cove-001` in Batch 3 is the baseline illustrative mission with two visible orders and `goal.count=2`. Batch 1 also mentioned five-order demo defaults. **Mission configuration is the source of truth**; the two-order authored fixture wins for `coconut-cove-001`. The fixture is NOT a proven solvability certificate.

## Batch 4 delivers
A mode registry; objective language and evaluation order; level and board-content schemas; mission state machine; scoring, stars, failure and recovery rules; seven curated mode designs; hazards; campaign difficulty and fairness analytics; content editor workflow; API and event boundaries; automated test vectors; implementation and release tickets.

## Scope discipline
- **v0.1.0:** one authored Classic Service mission with 2 orders; logical merge/scoring; win/loss/retry; basic objectives HUD. No modes menu promising unimplemented modes.
- **v0.1.1–v0.1.2:** 3–10 handcrafted Classic Service levels, difficulty instrumentation, tutorial polish, alpha tools.
- **v0.2.0+:** Island campaign mission graph (Batch 5), plus Precision and Score Attack when feasibility testing passes.
- **Later feature-gated modes:** Rush Hour, Survival, Chain Challenge, VIP, Endless, Festival and tournament variants. No server-trusted rewards until verified sessions and wallet exist.

## Product and fairness principles
1. A failure must have an understandable cause and a reasonable retry path.
2. Difficulty is authored through visible board/goal constraints rather than invisible mid-run physics changes.
3. Scores only reflect committed semantic events, not presentation animation callbacks.
4. An event is resolved by stable deterministic priority so the exact same run gets the same result.
5. Cosmetic power and paid items cannot contaminate standardized ranked conditions.
6. Content can be added through validated configs, without changing physics code.
7. Every new mode must demonstrate a new player decision and measurable retention/engagement value before shipping.

## Non-goals
Full island storylines, real-time multiplayer netcode, advanced perk trees, shop economy pricing, world incidents and dynamic characters receive integration notes only; later batches own their full designs. Visual mockups remain references, not implemented gameplay or approved final art.

## Ownership
Product/game design owns rules and release acceptance; gameplay engineering owns deterministic evaluators; QA owns reproducible fixtures; content design owns missions; owner performs all subjective/manual interface testing.
