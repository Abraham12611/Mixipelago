# 30 — Campaign QA Matrix, Golden Fixtures and Owner Manual Checks

## Static/unit cases (automate)
| ID | Given | Expected |
|---|---|---|
| MAP-001 | Empty progress on 2-node graph | Cove 001 available, Cove 002 locked |
| MAP-002 | Cove 001 cleared with one star | Cove 002 available |
| MAP-003 | Replay Cove 001 at fewer stars | Best stars never decreases |
| MAP-004 | Missing mission reference | Publication validator fails |
| MAP-005 | Dependency cycle | Validator fails |
| MAP-006 | Dangling edge endpoint | Validator fails |
| MAP-007 | Future draft mission at published node | Validator fails |
| MAP-008 | `anyOf` unlock with branch A cleared | Downstream node available |
| MAP-009 | `allOf` unlock with one missing | Node locked with explanation |
| MAP-010 | Hidden secret eligible but undiscovered | Not shown until reveal |
| MAP-011 | Event route expires | Critical permanent path remains |
| MAP-012 | Old graph publish replaces anchors only | Completion IDs remain intact |
| MAP-013 | Two concurrent first-clear receipts | One durable grant |
| MAP-014 | Local preview coins submitted as wallet | Backend ignores/rejects |
| MAP-015 | Unsupported mission mode | Play disabled, actionable message |
| MAP-016 | Map assets 404 | Accessible list fallback works |
| MAP-017 | Browser resume after interrupted unlock animation | Correct stable node state |
| MAP-018 | Travel target download fails | Current island remains usable |

## Pure rule vectors
`examples/tests/unlock-rule-vectors.json` provides expected outputs for always, missionCleared, minStars, allOf, anyOf and nodeClaimed. `tools/validate_batch5.py` checks static examples and these vectors. Add property-based tests for monotonic unlocks, idempotent receipts and dependency DAGs in TypeScript CI.

## UI/interaction tests (owner-directed)
1. Narrow phone: tap node versus pan movement, sheets don't hide selected node, two-finger zoom, safe areas.
2. Desktop: wheel zoom, trackpad inertia, browser scroll behavior, keyboard route access, hover tooltips.
3. Return from winning: one unlock celebration, no duplicate rewards, correct focus, Resume/Next/Map controls.
4. Locked route: requirement explanation understandable and link reaches prerequisite.
5. Low connectivity: placeholders, retry, cached map, no loss of progress.
6. Reduced motion and screen reader list: no inaccessible mission path.

## Performance checks
A map pan shouldn't step Rapier, rendering should not allocate repeated large atlases, chunk manager should release distant textures and retain progress metadata. Measure browser main-thread work, decoded texture memory, input latency and crash rate on real phones.

## Content acceptance
Every live gameplay mission needs Batch 4 golden winning replay. Every published critical path has an eligible route from entry to defined published endpoint. Every published manifest passes schema/static graph lint, semantic reward checks, visual preview and owner manual signoff.

## Evidence packet
Automated CI report, schema+graph validation logs, replay proof links, test device observations, owner manual signoff notes, content hash manifest, release checklist and screenshots/video of actual gameplay—not just marketing mockups.
