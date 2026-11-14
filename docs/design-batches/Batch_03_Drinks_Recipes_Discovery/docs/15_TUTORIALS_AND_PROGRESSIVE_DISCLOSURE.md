# 15 — Tutorial Design and Progressive Disclosure

## Teaching strategy

First 30 seconds teach shooting and matching; next 2 minutes teach order serving and preview; subsequent missions teach angle planning, combos, and board pressure. Recipe research, collection books and mastery should only appear when the player has mastered basic merges, and should be optional at first.

## Proposed v0.1 tutorial sequence

1. **Observe.** A single tier-1 appears as shooter; an identical tier-1 rests near table center. Gentle highlight says `Aim at a matching drink`.
2. **Aim.** Pointer drag or finger gesture shows trajectory; instructions don't block the playable region.
3. **Launch.** On release, a validated launch moves object. A miss teaches bounce instead of immediate failure; Retry tutorial remains simple.
4. **Merge.** First tier-1 pair becomes tier-2; game calls out `Citrus Shot + Citrus Shot = Sunny Lemon` with minimal animation.
5. **Serve.** A tier-2 order requests a newly produced drink. Show automatic service and reward; emphasize it is consumed by the customer.
6. **Preview.** Highlight `Next` and explain the queue.
7. **Finish.** Complete curated goal, show score, preview coins and Replay/Next.

Use scripted seed and board placements, but **validate a real trace**: preexisting tier-1 and service rules may make an untested tutorial unsolvable. The tutorial should never rely on demo scripting that violates actual collision/merge logic.

## Hint triggers

After N failed attempts, show a subtle suggested trajectory or matching tier highlight, not an autonomous merge. Player can disable hints. Avoid assuming a player is struggling due to disability, age, or financial behavior. Hints must not adjust ranked gameplay or create hidden extra reward chances.

## Future learning gates

- Stage 5–10: first chain reaction teaching.
- Early second island: more complex drink order targets.
- Recipe lab unlock: explain difference between tabletop evolution and off-board ingredient crafting.
- First secret: show clue journal, explicit attempt action, and persistent discovery card.
- First collection milestone: show cosmetic/progress benefit without suggesting real money value.
- Mastery unlock: introduce challenge metrics and separate ranked normalization.

Stage numbers are proposals to validate, not fixed commitments.

## Tutorial-state persistence

Track `tutorialVersion` and step completion; content revisions migrate or restart safely. If the player opens game on another device later, account-linked tutorial progress should sync; local alpha is browser-bound. Dismissing tutorial must not award achievement or preview coin unexpectedly.

## Recovery states

If an asset fails loading, pause tutorial and show Retry. If a shot is rejected due to blocked spawn, retain current step and queue. If a player navigates away mid-tutorial, resume from a safe checkpoint rather than replay the grant. If a guide animation ends before real physics outcome, wait for semantic event rather than guessing.

## Tutorial quality targets

Track first-shot success, time to first merge, time to first customer served, tutorial abandonment, retries, mis-taps by viewport region and first-mission completion; compare mobile vs desktop. Do not set new monetization prompts inside the first learning loop. Manual observation of players who have never seen the game is essential.
