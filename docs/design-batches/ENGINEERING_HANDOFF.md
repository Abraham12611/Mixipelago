# Engineering Handoff and Release Discipline

1. Start with Batch 01 for scope and the initial 72-hour alpha plan.
2. For gameplay, read Batch 02 fixed timestep/collisions, Batch 03 drink ladder/order-priority, and Batch 04 mission rules together.
3. For islands, connect Batch 05 graph nodes to published, proven Batch 04 mission fixtures; do not make draft nodes playable.
4. For economies, Batch 06 specifies a server-owned wallet and ledger. Keep it behind feature gates until authenticated and validated receipts exist.
5. Ship progressively. A document being complete does **not** mean its proposed systems are implemented.
6. Never implement nonfunctional paid upgrade controls or grant trusted coins from client preview values.
7. Engineers open isolated branches and PRs; no engineer self-merges. Owner directs manual interface/gameplay acceptance.
8. Test on desktop and mobile browsers with actual gameplay, network interruptions, and safe recovery.

9. For Batch 08, grant durable achievements only from verified receipts; show claimable versus claimed explicitly; use server-owned entitlements, item catalog and inventory. Batch 06 owns wallet credits and Batch 07 owns XP/skill points. Daily/weekly and randomized rewards remain feature-gated proposals.
