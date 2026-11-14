# 07 — Merge Eligibility, Atomic Arbitration, and Chain Reactions

## Core rule

In v0.1.0 two *active* drinks of the **same tier** (1–7) merge into exactly one drink of the **next tier**. Tier 8 is max and does not evolve. Any incompatible pair behaves as ordinary physical bodies. There are no cross-family recipes, conditional ingredient fusions, or player skill overrides in alpha; these belong in Batch 3/7 and must extend, not corrupt, the base resolver.

## Why arbitration matters

Consider objects A, B and C, all tier 3. At a single physics step, A contacts B, and B contacts C. A naïve callback might merge A+B and then B+C, consuming B twice and generating two tier-4 drinks from three inputs. That is a severe exploit and quickly corrupts score, orders and replay state. **Only one claim per input drink per merge resolution phase.**

## Algorithm

1. Drain contact-start events into `ContactCandidate[]` with collider handles and step.
2. Map handles to immutable logical drink IDs while mappings still exist; skip unknown/stale/fixed/wall contacts.
3. Canonicalize pair key `min(idA,idB) + ':' + max(idA,idB)` and discard duplicates *within this step*.
4. Exclude consumed, merging, serving, not-yet-armed or max-tier drinks.
5. Sort candidates by stable priority: first simulation step, then key. Do not claim an arbitrary substep timestamp if Rapier does not provide one; instead use deterministic handle-independent ID order.
6. For each candidate, if neither input in `claimedThisStep`, verify tier and recipe rule, then claim both synchronously and add `MergeTransaction` to a local transaction list. Otherwise skip.
7. Commit transactions at a safe post-physics boundary in sorted order: mark `merging`, read pre-removal poses/velocities, remove both bodies, create one result body with a new monotonic drink ID, and emit semantic events once.
8. Queue the new result as `active` only after its creation phase/arming rule; it can contact another matching drink on a **later** simulation step. Probe existing overlaps when necessary so chain reactions are not missed because contact-start fired during creation.
9. Score/session reducer processes unique `mergeId`s; listen-only FX and audio consume read-only events.

## Merge transaction data

```ts
interface MergeTransaction {
  mergeId: string;             // session/step/pair identifier
  step: number;
  inputIds: readonly [string, string];
  inputTier: number;
  outputTier: number;
  anchor: Vec2;
  outputVelocity: Vec2;
  chainRootId: string;
  chainDepth: number;
}
```

The merge ID must be stable and unique for the current session; e.g. `m:${sessionId}:${step}:${a}:${b}`. A reused collider handle is never a valid identity. A new output gets a brand-new drink ID, even when visually it resembles one input.

## Result placement

Default anchor is mass-weighted midpoint of source body centers (equal masses simplify to arithmetic midpoint): `p = (mA*pA + mB*pB)/(mA+mB)`. If overlapping fixed objects or outside bounds, resolve with a deterministic local placement search: consider center, then a fixed ordered set of small offsets within radius limit; choose the first legal position. If none is legal, record a controlled fallback and avoid NaN or teleporting into a wall. Position adjustment should be visually covered by a short controlled gather animation, not an unexplained jump.

## Momentum inheritance

Proposed baseline: momentum-aware average velocity `v = clamp((mA*vA+mB*vB)/(mA+mB), maxMergeSpeed)`; angular velocity is bounded or reset. **This is a gameplay rule**, not literal conservation of energy after fusing objects, and should be owner tested. Alternative policies: `keepFastestDirection` or `smallForwardImpulse`. All policies live behind versioned config, not scattered conditional code.

The output should have approximately the same collider radius/density in alpha so chain behavior remains understandable. If result spawn inherits too much speed, it may cause unfair instant losses; cap speed and allow a brief merge grace near the lower line.

## Chain definition

A chain begins when a player-triggered shot causes a merge. A later merge belongs to the same chain if its inputs include a descendant of an earlier merge result and occurs within a bounded number of simulation steps (proposed max: 180 steps / 3 seconds), without another launched shot interrupting. Avoid attaching unrelated background collisions to the same chain merely because they occurred within the time window.

- `rootShotId`: originating shot, if known.
- `rootMergeId`: first merge in chain.
- `chainDepth`: 1 for first, 2 for descendant's second merge, etc.
- `comboMultiplier`: a rule computed by SessionReducer, not physics.
- `maxChainDepth`: configured limit to prevent infinite loops; finite eight-tier ladder naturally caps basic chains but future recipes may not.

Example: two tier-2 drinks merge → tier-3 (depth 1); new tier-3 collides with a resting tier-3 → tier-4 (depth 2). Score events emit once per merge, then a combo update. If chain is disconnected from root, it's a new chain.

## How to detect follow-up contacts

New bodies spawn after the world's previous contact event pass. If already overlapping a resting body, Rapier may produce a started event next step; however, rely on a deliberate test and a bounded contact/overlap query for eligible new results when needed. Do not use sprite overlap or screen pixels as merge eligibility. Resolve at most a configured number of merges per step (e.g., 32) and report overflow as a controlled fault. No recursive `merge()` that can run indefinitely in a single call stack.

## Serving priority

Batch 1 says automatically serve **newly generated eligible results** to the oldest matching outstanding order (created-at and order ID tiebreak). If a newly created drink is needed for an order, choose one deterministic policy: default reserve that drink for service after its short creation phase, preventing it from simultaneously merging again. If no order matches, activate normally and permit chain merge. An owner-approved alternative could prioritize chains first, but not in v0.1.0 without explicit ADR.

This is an important interaction: if auto-serving consumes every new tier-3 that matches a customer, chains into tier-4 may not occur. Missions and order tiers must be designed accordingly, and a transparent user feedback indicator should show the automatic serve.

## No other rewards in the physics engine

`MergeResolver` emits `{inputIds, outputId, inputTier, outputTier, chain...}`. `SessionReducer` applies scoring, order progress and preview coins. FX visual glitches cannot create extra rewards; duplicate event delivery must be idempotently ignored by reducer using `mergeId` or event sequence.

## Edge-case table

| Scenario | Required behavior |
|---|---|
| Same pair starts contact twice | At most one merge |
| A overlaps B+C | Stable one-pair arbitration, other candidate skipped |
| Two disjoint pairs simultaneously | Both merge, stable output ID order |
| Result spawn overlaps next tier | At most one additional merge on later step |
| New result required by customer | Reserve/serve before remerge per alpha priority |
| Pair at max tier | Physical collision, no merge |
| One object is serving | Pair ineligible |
| Pair crosses boundary during merge FX | No premature loss while marked merging; new output evaluated by grace rule |
| Restart while merge queued | Old transaction cannot mutate new world |
| Stale collider event | Ignore and log diagnostic, no phantom score |

## Acceptance tests

Property-based random contact graphs should assert: every input ID appears in at most one transaction per resolution phase; each committed pair reduces active drink count by exactly one; no transaction emits twice; output tier is input tier +1; event sequences and output IDs are stable for identical seeds. 10,000 synthetic candidate graphs should not violate these invariants.
