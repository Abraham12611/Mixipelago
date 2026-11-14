# 35 — Architecture Decisions, Conflicts with Earlier Batches and Proposed Resolutions

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Carry-forward decisions
**ADR-B4-001 (fixed):** Existing same-tier merges, terminal tier8, automatic serving of newly produced eligible output, ordered event stream, danger grace and win-before-same-tick-loss remain unchanged.
**ADR-B4-002 (fixed):** `coconut-cove-001` existing Batch3 fixture defines count2 win objective; older Batch2 prose mentioning a default five served orders is generic demonstration, not override.
**ADR-B4-003 (fixed):** Alpha coins remain client preview only; trusted economy & ranked receipts deferred.
**ADR-B4-004 (fixed):** Every mode uses same simulation layer and immutable content/physics hashes.

## Proposals for owner sign-off
- **ADR-B4-005:** use an additive mode-policy registry instead of branching SessionReducer into separate mode-specific copies.
- **ADR-B4-006:** alpha goal v1 adapter maps `goal:{type:'orders_served',count:2}` into Objective DSL; v2 objective nesting introduced later.
- **ADR-B4-007:** use active simulation ticks for timers, no wall clock when paused.
- **ADR-B4-008:** Precision mode waits for bounded last-shot resolution before losing by shot exhaustion.
- **ADR-B4-009:** nested stars: mission win=1, optional criteria for 2/3 stars; preserve best stars independent of best score.
- **ADR-B4-010:** Endless is sandbox-only initially, and terminal tier8 remains terminal until explicit future clear mechanism approved.
- **ADR-B4-011:** ranked tie-break sequence score > fewer shots > active time > receipt; final approval Batch13.
- **ADR-B4-012:** future board surfaces apply deterministic fixed-step zone controllers; never use CSS animation to modify collision rules.

## Known issues in earlier docs
1. **Default objective 5 vs example count 2:** use per-mission config; `coconut-cove-001` count2, not 5.
2. **Auto-service vs Chain Challenge:** no conflicting customer request for needed chain outputs; authoring proof required.
3. **Tier-1 scoring entry:** exists in catalog but not awarded for ordinary pair merges; use output-tier base.
4. **Preview coins language:** every UI showing coin balance must avoid implying spendable trusted wallet in alpha.
5. **Unverified sample mission:** JSON fixture is a design candidate; no claimed playable golden run until engineers execute it.
6. **Tier-8 terminal vs Endless:** do not invent tier9; later reset/clear action must be explicit and versioned.

## What can change later
Mission order targets, shots, star thresholds, board theme, mode availability and generated seed cohorts may be tuned in new versions. Active runs and historical results cannot be silently reinterpreted. New recipe families remain Batch3 future-gated until branch resolver deployed. Social leaderboards remain Batch13 responsibility.

## Approval tracker
Record decision ID, choice, owner approval timestamp, rationale, affected contracts, rollout flag, migration strategy and test vectors in central ADR index. An unanswered question is a proposed value, never a claim that implementation is confirmed.
