# Engineer Start Here — Batch 8

1. Read `docs/00_INDEX_AND_README.md` and the cross-batch precedents listed there.
2. Freeze entitlement, policy version, claim receipt, inventory and event envelope interfaces before implementation.
3. Run `python tools/validate_batch8.py` (pure fixture and catalog checks only).
4. First executable slice: **one verified mission → one first-clear badge entitlement → claim once → inventory owned → equip once**, guarded by server feature flags.
5. Require server-owned source proof, authenticated account, idempotency key and stable published content. Batch 6 owns wallet credits; Batch 7 owns XP/points. Never credit preview coins or client raw-physics events.
6. Engineers work in independent branches and open PRs; do not self-merge. Owner handles all manual UI/play-feel testing and approves product merges to `main`.
7. Do not enable optional daily/weekly rewards, random chests or seasonal prizes without the source producers, economic budgets, legal/platform review where needed, and acceptance evidence.
