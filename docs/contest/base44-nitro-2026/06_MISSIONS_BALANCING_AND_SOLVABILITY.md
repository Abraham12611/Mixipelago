# 06 — Coconut Cove Mission Pack and Solvability

## Content contract

The contest edition targets **12 actual, curated playable levels** in three chapters, not 12 mock buttons. Every published mission must have a pinned ID, mode, seed, board layout, spawn queue, initial drink bodies, target order list, time/shot constraints, star goals, result-reward semantics and **proof it can be completed**. The table below is a *design itinerary*, not proof or a declaration of implemented levels.

## Three-chapter campaign

| ID | Display name | Concept/learning goal | Authoring constraint |
|---|---|---|---|
| cove-001 | First Splash | Basic same-tier merge + two simple orders | Preserve canonical two-order goal and oldest-order serving |
| cove-002 | Twin Orders | Duplicate request priority | Two visible same-tier requests; tie stable |
| cove-003 | Perfect Bounce | Angle a shot off a side rail | Seed enough compatible bodies; avoid random softlocks |
| cove-004 | Sunny Chain | Two-step merge chain | Do not auto-serve intermediate tier that must remerge |
| cove-005 | Busy Pier | More clutter and danger | No instant loss on launch; visible recovery |
| cove-006 | The Big Glass | Make one tier-4 | Seed viable t2/t3 bodies and an appropriate queue |
| cove-007 | Neat Service | Limited shots, multiple ways to clear | At least one robust winning input sequence |
| cove-008 | Island Traffic | Pair selection under simultaneous contacts | Deterministic arbitration test; no unfair randomness |
| cove-009 | Beachside Special | First visually richer order | Keep one linear eight-tier chain |
| cove-010 | Coral Rush | Faster service pacing | Timer only on **active** game ticks and pause-safe |
| cove-011 | Sunset Combo | Score and a bounded chain bonus | Score objective must be feasible under auto-serving |
| cove-012 | Festival Finale | Festive background/music, multi-order challenge | Optional until 1–11 are proven and polished |

**Proposal:** 4-mission Chapter 1 teaches, 4-mission Chapter 2 deepens, 4-mission Chapter 3 celebrates. Mission 12 is a festival finale, not an always-online festival service. Keep the initial visible map to actual published fixtures.

## Model

~~~ts
type Mission = {
  id: string; version: number; title: string; mode: 'service';
  published: boolean; seed: number;
  board: {width:number;height:number;dangerY:number};
  initialBodies: Array<{id:string;tier:1|2|3|4|5|6|7|8;x:number;y:number}>;
  launchQueue: Array<{tier:1|2|3|4|5|6|7|8}>;
  orders: Array<{id:string;requestedTier:number;quantity:number;previewCoins:number}>;
  win: {fulfilledOrders:number};
  limits: {shots?:number;activeTicks?:number};
  scoreProfileId: string;
  stars: Array<{minScore?:number;maxShots?:number}>;
};
~~~

A more complete schema may be reused **only if authored/tested compatibility is established** with Batch 4. A richer mode v2 must not mutate the starter v1 silently.

## Solvability pipeline

1. Static lint: all tiers in 1–8; published assets exist; unique IDs; orders allowed by mission rules; available input equivalents cover a conservative lower bound for every required drink.
2. Serving-aware feasibility: when an intermediate tier matches an order, it may be removed, so do **not** just count total tier-1 equivalents as a proof.
3. Seed replay: save a legal input sequence, run it from a clean state, assert win, non-negative queue and no forced terminal loss.
4. Monte Carlo/heuristic agents: sample alternative inputs to detect extreme fragility; identify cases that require pixel-perfect luck.
5. Owner manual play: record actual touch and desktop solutions, player confusion and pacing.
6. Publish only after test evidence is linked in mission metadata.

## Difficulty guardrails

- First 1–3 levels: no timer, generous board, generous shot opportunities, scripted visible next queue.
- Levels 4–8: gentle tactical complexity, one new concept per level.
- Levels 9–12: faster board pressure, combo planning, original festival atmosphere, never compulsory purchases.
- A player with **no boosters** can win every level. A poor run can fail but never require an ad or money to retry.
- Tier-8 may appear visually as ultimate aspiration but don't force improbable tier-8 crafting on a small queue.

## Result semantics

Stars and preview coins are local demo progress; not real-world value and not spendable trusted balance. Best score is per versioned scoring profile. Replay does not duplicate any unique badge and never issues server-verified coins.

## Fixture acceptance and references

The previous Batch 4 example cove-001 is a design baseline, not necessarily validated solvable. Prefer import only after checking schema/version and recorded solution. Explicitly flag new cove-002–012 as **draft** until implemented. No interactive map nodes for draft missions.
