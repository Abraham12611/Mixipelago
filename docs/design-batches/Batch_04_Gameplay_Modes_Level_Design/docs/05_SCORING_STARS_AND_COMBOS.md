# 05 — Scoring, Combos, Stars, Medals and Tie-breakers

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Canonical alpha score rules (Batch 3)
Award base merge points on committed new output tier using scores: t2=25, t3=60, t4=140, t5=320, t6=720, t7=1600, t8=3500. Tier-1 score entry 10 is dormant in ordinary pair-merge gameplay. Example t2+t2→t3 yields 60 base. A fulfilled customer order adds `coinReward × 10` score and `coinReward` alpha-only preview coins. No points for shots, physical impacts, SFX, or hover events.

Proposed chain factor carried from Batch 3:
`mergePoints = round(baseTierScore × min(3, 1 + 0.25 × max(0, chainDepth-1)))`.
- Chain depth 1: ×1.00; depth 2 ×1.25; depth 3 ×1.50; depth 9+ capped ×3.00.
- Chain parent/shot ancestry is stored in semantic event metadata. Independent simultaneous merges are separate depth-1 roots unless linked to one originating shot.
- Use a specified integer rounding mode; JS Math.round for nonnegative finite numbers is an initial proposal. Cross-platform verifier uses equivalent logic.
- `sessionScore` must remain a safe integer; reject or explicitly cap overflow and emit telemetry. Do not wrap.

## Example calculation
A root shot causes a tier-3 output from two tier-2 objects: 60. A subsequent merge from tier-3 to tier-4 would yield 140×1.25 = 175. If a customer auto-serves the tier-3 immediately, that same physical output CANNOT then chain upward; instead the fulfilled order contributes its own score. If the order pays 15 preview coins, add 150 order score and 15 preview coins; no extra persistent coins are minted.

## Victory vs stars
Victory is determined by PRIMARY objective only. Stars are quality ratings based on optional, published thresholds. Suggested three stars: 1 star = complete primary; 2 stars = complete under specified shot or active-time threshold; 3 stars = an even stronger, reachable shot/time threshold. The thresholds must be designed so 3-star run is achievable in a scripted proof and not dependent on a lucky hidden RNG outcome.

## Proposed star DSL
```
starCriteria: {
  one: { kind:'mission_won' },
  two: { kind:'shots_at_most', value: 9 },
  three:{ kind:'shots_at_most', value: 6 }
}
```
For Score Attack, stars may instead be score thresholds. Threshold monotonicity must be validated: 3-star condition implies 2-star condition or explicit independent-star policy; default is nested. Do not overwrite existing best 3 stars with 2 on replay. Save best score, best stars, least shots as independently monotonic fields.

## Separate metrics
Track `shotsFired`, `uniqueMerges`, `ordersCompleted`, `producedByTier`, `maxChainDepth`, `activeTicks`, `dangerWarnings`, `boostersUsed`, `score`, `resultStatus`, and `seed`. These let designers understand difficulty and future competitive eligibility. Do not use coin balance as a proxy for player skill.

## Tie breakers for eventual competitions
For standardized ranked challenges: primary highest validated score; secondary fewer shots; tertiary lower active ticks; final stable server receipt time (only when all else equal). Final choice must be published in Batch 13, versioned, and applied server-side; do not silently alter old seasons.

## Reward separation
`score` is a session number; `previewCoins` is a disposable client-side demonstration tally in v0.1; `trustedCoins` is a future server-ledger amount only. Mission grants require an idempotent server receipt once wallet exists. Leaderboard prizes require season-finalization idempotency; never trust a client score alone.

## Score validation
Property-based test duplicate merge IDs, duplicate order fulfillment, chain loops, unsafe integers, missing tier scores, conflicting same-tick events, and replay with altered scoring rules. Record `scoreRulesVersion` distinct from game app version.
