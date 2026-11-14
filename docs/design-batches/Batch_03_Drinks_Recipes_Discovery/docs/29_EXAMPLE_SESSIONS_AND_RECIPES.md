# 29 — Worked Gameplay, Recipe and Serving Examples

## Case A: simplest merge

World contains two active tier-1 Citrus Shot glasses A and B, no orders requiring tier-2. They contact at simulation step 120. ContactCollector yields pair `(A,B)`, stable candidate sorting claims them; both removed after safe step; new C tier-2 Sunny Lemon appears. SessionReducer scores **25 base points** (output tier 2); C activates after arming; 1 net less physical body. Visual sparkle and sound are read-only subscribers.

## Case B: different drinks do not merge

A is tier-2 Sunny Lemon moving diagonally; B is tier-3 Sunset Splash resting. Rapier resolves impact with velocity deflection, but resolver returns `none: different-tier`, so both remain active physical objects. Neither score nor customer progress changes. This test demonstrates that recipe compatibility isn't a sprite similarity algorithm.

## Case C: auto-serving overrides remerge

A+B are tier-1 -> C tier-2, and an order explicitly needs tier-2. Reducer reserves C as `serve_claimed`, increments order progress and eventually removes C for serving animation. C cannot collide and become tier-3 even if it briefly overlaps a resting tier-2; player must create another tier-2 later. This is a deliberate, testable tradeoff and must be taught through UI.

## Case D: chain reaction

No tier-2 order is active. First pair of tier-1s -> tier-2 result C. A separate tier-2 D rests nearby. At a later simulation step, C+D -> tier-3 result E, inheriting chain root from the original shot. First merge gets 25 points; second gets `round(60×1.25)=75` with proposed depth-2 multiplier. Total 100 points before any customer order bonus. Event lineage must prove causal ancestry; a different unrelated merge within 3 seconds is not automatically part of this chain.

## Case E: two simultaneous candidate pairs

A, B, C all tier-3. Collision candidates A–B and B–C report in same step. Sort stable by pair key, claim one pair only; B cannot appear in both. The unclaimed third body stays. If there is a fourth D in a disjoint pair, that pair can merge within the same step after deterministic sorting.

## Case F: sample mission economy (conceptual event sequence)

A mission requests order X: one tier-2 for 10 preview coins and order Y: one tier-3 for 20 preview coins. A theoretical logical sequence of six tier-1 equivalents: two make tier-2 (served X); four more make two tier-2 bodies, which combine into tier-3 (served Y). Score = three tier-2 outputs at 25 each + one tier-3 output at 60 before combos + `100+200` for order completion = **435** base points; optional combo uplift depends on causal chain and step timing. Preview order coins = 30; if mission completion bonus = 20, total preview coins = 50. This is a logical resource demonstration, **not a proven tabletop shot trace**; geometry and queue must be tested before labelling a specific mission solvable.

## Case G: future explicit research recipe (disabled)

Player has one `mint` and one `coconut` ingredient, selects Research mode at a workshop, sees `Lagoon Cream` clue, confirms an explicit craft that lists required resources, server atomically consumes ingredients, grants discovered recipe ID and optional cosmetic presentation. Nothing happens on the ordinary tabletop when a tier-3 glass collides unless a separate published recipe rule says so. No arbitrary inventory grant is made from local collisions.

## Case H: max-tier behavior

Two tier-8 Crown of the Isles drinks meet. They bounce/slide; no tier-9 appears and no score is awarded. A newly produced tier-8 could satisfy a tier-8 order if the mission explicitly contains one, but this should not be an ordinary early-game request given 128-unit lower bound from scratch.

## Why these examples matter

Use these exact cases as acceptance narratives in manual tests and machine rule vectors. 'Looks correct' is inadequate; event counts, scores, served quantities, object lifecycle and versions must be asserted.
