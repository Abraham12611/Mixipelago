# 10 — Chain Reaction and Score Attack Modes

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Purpose
Make physics mastery visible: players arrange collisions so one launched drink triggers an escalating sequence of merges. This mode should feel rewarding to experts but be legible to beginners with a chain-path tutorial.

## Two distinct variants
**Score Attack:** hit `score_at_least` within a shot or active-time budget; all valid merge and order scores count by shared scorer, with mode-specific optional bonus only if versioned.
**Chain Challenge:** perform a `combo_depth >= target` in one causally linked shot; `maxChainDepth` is measured from unique merge event ancestry.

## Causal ancestry
A merge event has `mergeId`, `rootShotId`, `parentMergeId?`, `chainDepth`, `inputObjectIds`, `outputObjectId`, `tick`. Two independent pairs contacted by a single shot may have same root shot but different chain branches. `chainDepth` for branch child = max parent depth+1, not sum of all branches. Deduplication prevents repeated collision contacts from inflating depth. Output may merge next tick only if not auto-served.

## Critical order-priority rule
For pure Chain Challenge missions, do not place an active order that consumes the tier the player must use for follow-on merges. The alpha auto-serve rule is immutable in that mode. Offer no orders or only non-interfering orders until the scripted chain is completed. This is a content design responsibility, not a physics modification.

## Scoring
Use Batch 3 formula with a capped multiplier. Show a floating x1.25 / x1.5 chain feedback only when calculation is committed. Avoid granting extra score for every collision contact, as that would reward jitter and create exploits. Player's best chain is tracked separately from total merges.

## Shot strategy examples
- Place tier-1 pair near a tier-2 glass so the resulting tier-2 moves into another tier-2.
- Use wall rebound to redirect the output into compatible target.
- Delay second contact so physically blocked routes clear before chain.
- Choose whether to take a 2-merge sure route or attempt a 3-merge riskier route with tighter board pressure.

## QA and balance
Golden trace must prove ancestry on simultaneous sibling merges, merge event order, auto-serving interruption and output momentum. Score threshold feasibility checked against theoretical max achievable under budget and concrete winning shots. Avoid user-visible precision requirements that are less than one logical pixel of touch control at common device sizes.
