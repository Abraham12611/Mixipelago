# 05 — Gameplay Contract and Pure Engine Interface

## Carry forward, do not silently rewrite

Source contracts: Batch 2 merge arbitration; Batch 3 tier Bible; Batch 4 Classic Service; Batch 5 mission graph.

- **Eight tiers:** Citrus Shot (t1), Sunny Lemon (t2), Sunset Splash (t3), Blossom Fizz (t4), Coral Martini (t5), Mint Lagoon (t6), Ocean Cloud (t7), Crown of the Isles (t8).
- **Only t1–t7 same-tier pairs merge** into one next-tier output; t8+t8 collides but does not merge.
- Score is awarded on **created output tier** (Batch 3: 25, 60, 140, 320, 720, 1,600, 3,500); a tier-1 nominal value does not arise through standard merges.
- Contact arbitration claims each input object at most once per step; new output receives new logical ID.
- If a newly merged output matches an outstanding order, automatically serve the **oldest eligible** order (issuedTick, then ID) **before** any further chain merge.
- **Coconut Cove 001** begins with two active scripted orders and wins at two completed orders. Win beats danger loss on a same-tick tie.
- Physics fixed step, camera/render separate; client event is never a trusted economy or leaderboard receipt.

## Minimal TypeScript domain

~~~ts
type Tier = 1|2|3|4|5|6|7|8;
type Command =
 | {type:'AIM_START'; pointerId:number; x:number;y:number}
 | {type:'AIM_MOVE'; pointerId:number; x:number;y:number}
 | {type:'AIM_RELEASE'; pointerId:number; x:number;y:number}
 | {type:'PAUSE'} | {type:'RESUME'} | {type:'RESTART'};
type GameEvent =
 | {type:'MERGE_COMMITTED'; mergeId:string; outputId:string; tier:Tier; tick:number}
 | {type:'ORDER_PROGRESS'; orderId:string; sourceMergeId:string; amount:number}
 | {type:'ORDER_FULFILLED'; orderId:string; rewardPreviewCoins:number}
 | {type:'MISSION_ENDED'; outcome:'win'|'loss'; reason:string};
~~~

Reducers must be pure where feasible; physics applies queued world mutations at safe post-step boundaries; UI and audio observe events, not write them back. Use a session-scoped event dedupe key.

## Inputs and game feel

- Touch: finger-down on launch zone, drag to aim, release to launch; show arrow preview; cancel on lost pointer capture, route transition, escape or visibility loss.
- Desktop: pointer drag/release; optional keyboard aim/confirm; escape pauses.
- Launch direction is toward target by authored policy; constrain impulse cone and speed by versioned config.
- Fixed dt=1/60; guard max catch-up to avoid runaway work after background.
- Respect pause: clocks, timers and launches remain frozen; resume cannot fire a stored swipe.
- A preview sprite is not a collidable body; blocked launch does not consume queue.
- Keep animated scale/wobble visual only; collisions use stable logical circle fixtures.

## Edge scenarios

- A contacts B and C in one step → at most one claim for A.
- Duplicate merge event → one score and at most one serve.
- An output that serves cannot also remerge.
- Two matching orders → oldest wins; tie ID stable.
- Two max-tier glasses → bounce/slide, no tier 9.
- Danger crosses as second order fulfills → win.
- If guest save fails or assets are missing, show playable restart/reset; never softlock a stage.

## Early acceptance

Pure unit tests for merge identity/tiers, ordered serving and terminal precedence; event replay tests; 3 actual touch/desktop scripted smoke runs; owner manual check of sliding, rebounds, latency and clarity.
