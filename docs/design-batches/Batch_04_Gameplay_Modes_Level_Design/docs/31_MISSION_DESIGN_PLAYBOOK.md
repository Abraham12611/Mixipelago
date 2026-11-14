# 31 — Level Designer Playbook: Author, Review, Prove and Improve

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## A designer starts with player learning, not a number
Choose one sentence describing the NEW decision: “position a t2 glass so the result auto-serves while keeping a clear next shot.” Pick a mode, goal, constraints and teaching cue. Build a playable physical setup consistent with that sentence; only then add coin/score values or spectacle.

## Step-by-step authoring
1. Pick a unique immutable `missionId` and supported `modeId`; identify current island and target player cohort.
2. State primary objective in plain English and DSL; mark optional star criteria.
3. Select an existing physics preset; changes to friction/bounce are rare and require a special-material tutorial.
4. Lay out starter drinks, rails and launch positions on logical world grid; verify no penetration.
5. Pick authored first items and seeded pool; make demand tiers consistent with available resources.
6. Add initial order list, oldest-order priority and replacement behavior; assess auto-service and chain route interference.
7. Configure loss conditions (danger, shots, active time), intro hint, pause and fail explanation.
8. Generate a candidate winning input sequence; run actual headless sim and record proof.
9. Add increasingly difficult optional star thresholds based on a verified range of outcomes.
10. Validate at narrow portrait and desktop, run automated tests and send manual playthrough to owner.
11. Publish a new pinned content version and record changes.

## Checklist for a good mission
Goal can be read in three seconds. Player sees why current items matter. Important tiers have distinguishable icons. At least one viable strategy exists without paid boosters. Angled collision is physically understandable. A miss is learnable, not purely RNG. Long chains aren't accidentally stolen by an order. Retry is easy. A loss tells the cause. Optional 3-star route is viable.

## Example design cards
**Cove-001:** introductory direct merge and service. Start with two tier1 bodies and authored tier1 shots. Human tutorial proof REQUIRED.
**Cove-004:** angled bank-shot chain. Remove interfering orders or request only unrelated tiers. Capture a golden chain-depth-2 proof.
**Precision-001:** four or six authored shots, at least one guaranteed alternative solution; final collision may finish after last shot. Validate typical mobile gesture tolerance.
**Rush-001:** active-time only, explicit order target and maximum; verify pause does not change outcome.

## Review process
Engineer evaluates feasibility; content QA runs structural and replay tests; UI designer checks HUD affordances; owner manually approves. Track rationale for every difficulty change, especially when an earlier version was widely played.
