# Engineering Kickoff — Batch 4

## Direct instruction
Build the smallest truly playable Classic Service experience first. Do not attempt every future mode before the alpha launches. Batch 4 specifies the extension architecture so the team can ship incrementally.

## Alpha build contract
1. Ingest unchanged `coconut-cove-001` Batch 3 example and pinned eight-tier drink catalog.
2. Provide one mode policy (`service`), an `orders_served` reducer, Batch 3 score reducer, terminal-state priority, two customer cards, mission-goal HUD and win/loss/retry.
3. Connect to Batch 2 Rapier collisions and auto-serve. Verify no duplicated event, coin or body removal.
4. Add fixed-step + normalized replay trace instrumentation and match existing physics tests.
5. Produce an ACTUAL reproducible winning trace; existing JSON example is not proof. If example is unsolvable in the implemented physics engine, revise it in a new mission version after review; never claim existing fixture won.
6. Test mobile viewport, touch aiming, desktop mouse aiming, pause/retry and browser visibility. **All manual UI testing is directed to owner.**
7. Open scoped PRs with evidence; engineers do not merge into `main`; owner explicitly approves production promotion.

## Parallel lanes
A = domain / objective and scoring; B = React HUD / Phaser bridge; C = JSON schemas & mission tooling; D = integration QA/CI/replay; E = art+audio/future-mode prototype only after Alpha critical path.

## First acceptance artifact
Record `sessionId`, versions/hashes, seed, serialized command trace, result summary, and proof of two unique order fulfillments + one win. No trusted currency ledger or leaderboard claim for alpha.

## Read paths
`docs/01`, `02`, `03`, `04`, `05`, `06`, `15`, `30`, `32`, `33`, `34`, `35`, `38`.
