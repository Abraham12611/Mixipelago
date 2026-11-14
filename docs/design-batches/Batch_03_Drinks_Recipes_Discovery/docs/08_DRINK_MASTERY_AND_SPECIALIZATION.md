# 08 — Drink Mastery, Expertise and Skill-Tree Hooks

**Status:** Future progression proposal. Batch 7 owns complete character skills, points, passive abilities, profession trees and respec economics. This document defines the drink-mastery inputs and constraints only.

## Concept

Every drink family may eventually have its own mastery track, rewarding knowledgeable and precise players for *playing well* with that family. A tier-6 produced through a 3-link chain is a different skill expression from a tier-6 produced inefficiently across many launches. Mastery should reflect both achievement and consistent use, not simply grinding repeated tier-1 shots.

## Mastery dimensions

- `firstCreation`: first verified creation of canonical drink.
- `creationCount`: bounded tally of successful output creation events.
- `chainTechnique`: best verified chain depth using that drink.
- `precision`: optional contribution derived from verified first contact geometry; avoid unreliable raw pointer timings across devices.
- `orderService`: verified customer orders satisfied with that drink.
- `challengeCompletion`: standardized mastery challenges, ideally fixed seed and rules.
- `discoveries`: qualifying research recipes from the family.

## XP proposal (not final)

A first creation receives a one-time mastery bonus. Subsequent productions earn small XP with daily/session diminishing returns; harder tiers and verified challenges earn more. Example candidate: `baseMasteryXp = 2 * tier`, +10 first creation, +3 per descendant chain depth capped at 12; apply daily XP soft cap after 100 eligible productions. These numbers are deliberately illustrative and must be simulation-tested before releasing persistent XP.

## Levels and perks

Proposed milestone names: `Novice`, `Learner`, `Craftsperson`, `Artisan`, `Virtuoso`, `Legend`. Mastery grants could initially be cosmetic (title, animated drink card, custom splash FX, journal border), then carefully bounded utility perks (e.g. extra hint in a non-ranked crafting mode). A character skill tree may read mastery thresholds as prerequisites but cannot mutate the saved mastery record directly.

## Competition fairness

All ranked physics sessions use a standardized rule-set and should not grant a gameplay advantage based on mastery. Cosmetic mastery visuals may be displayed but must not obscure target visibility or add input latency. A competitor's skill comes from aiming and planning, not having completed 5,000 low-level sessions.

## Trust and idempotency

Only validated runs contribute durable mastery XP. One run can trigger multiple merge records, each with stable event ID and unique `objectId` lineage; process each exactly once. Aggregate ledgers should allow correction/recalculation if a physics or reward exploit is discovered, with admin audit trails.

## UX flow

A recipe card shows progress bar, next meaningful milestone, current title, and eligible challenges. The end-of-round summary can display +mastery XP beside score if and only if the corresponding server grant is confirmed. In local alpha, optional preview metrics may be shown but explicitly labeled local and not transferrable to trusted mastery.

## Anti-grind balance

Never encourage intentionally failing missions or refusing orders just to farm high-tier events. XP should favor validated completion, breadth of drink types, and capped duplicate actions. Consider excluding immediately restarted identical seed farming from certain rewards; tie decisions to transparent policies. Offline progress must not silently mint authoritative mastery.

## Future API seam

`MasteryService.recordValidatedActivity({playerId, runId, drinkId, activityType, evidenceId})` -> unique event ledger -> aggregate progress -> milestone grants. Player-facing queries use cached aggregates; source events retained under privacy/retention policy. This API is proposed, not implemented.
