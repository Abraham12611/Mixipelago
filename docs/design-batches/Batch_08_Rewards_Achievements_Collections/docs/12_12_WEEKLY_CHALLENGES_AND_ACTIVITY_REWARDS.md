# 12 — Weekly Challenges, Activity Rewards and Task Boards

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Weekly board
A weekly board can offer three optional tasks using already verified facts: clear three published missions, serve twenty verified orders, reach one new star threshold. Completion is based on server facts within a weekly UTC scope, with visible start/end and accessible task descriptions.

## Rules
- Task progress always comes from trusted event projections; do not credit raw animation events.
- Published task definitions have an eligibility profile, explicit maximum claim count, and server-side terminal status.
- Weekly and first-clear rewards may both be earned if budgets are explicit and deduped by different entitlements.
- Never force simultaneous daily activity to complete an essential weekly reward; design achievable windows for irregular players.

## Consistency
Task counters are event-time anchored but ingestion-time validated; late eligible events may count under a grace window documented in the versioned policy. Define tie-break around event-time trust; no rewards created after finalized scope unless an audited correction.

## User experience
Collapsed board on mobile, expanded detail on desktop. Show progress denominator, reward, exact availability period and disabled reason. Provide keyboard reachable claim controls and a minimal post-claim toast.

## Scaling
Task authoring belongs in internal content studio. Season scheduler publishes immutable task snapshots and finalizes windows; counter processing uses a unique `(player,program,window,task)` projection. A disabled program can be hidden without deleting historical claims.
