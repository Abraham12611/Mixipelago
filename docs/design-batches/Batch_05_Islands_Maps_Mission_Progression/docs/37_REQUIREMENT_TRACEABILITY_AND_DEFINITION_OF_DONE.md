# 37 — Requirements Traceability and Definition of Done

## Traceability
| Requirement ID | Behavior | Spec | Evidence |
|---|---|---|---|
| B5-R01 | Existing mission IDs unchanged | 03, 15, 28 | Batch 4 fixture byte comparison |
| B5-R02 | Unlock evaluator pure and explainable | 05, 29 | Unit vectors + reason code tests |
| B5-R03 | Published graph has valid path | 03, 24 | Validator + content review |
| B5-R04 | Best stars never decrease | 07, 16 | Monotonic property tests |
| B5-R05 | 2-node Cove map works | 04, 31 | Integration test + owner playback |
| B5-R06 | Mobile map touch/zoom usable | 10,12 | Owner device test |
| B5-R07 | Desktop map keyboard navigable | 11,26 | Accessibility test |
| B5-R08 | Hidden routes reveal correctly | 06,21 | Pure state tests |
| B5-R09 | Replayed mission grants once | 18,17 | Duplicate-receipt backend test |
| B5-R10 | Map stays responsive with chunks | 14,27 | Profiling on low-tier devices |
| B5-R11 | Invalid content cannot publish | 15,23,24 | CI semantic validation |
| B5-R12 | Offline/corrupt save recovers | 16,27 | fault-injection tests |
| B5-R13 | Mission run pinning survives update | 15,28 | old/new manifest integration test |
| B5-R14 | Future feature nodes cannot launch | 04,32 | feature gate e2e tests |

## Acceptance policy
A requirement isn't complete until code is merged into the intended branch, tests run in CI, success/failure flows are documented, deployed preview is available, and any necessary manual interface test has been sent to owner and approved. A static JSON validator passing is not proof of a playable mission.

## Definition of Done — first map vertical slice
- Published starter graph references real existing missions; unknown IDs/versions fail safely.
- `Next Mission` and explicit node selection can launch and return from gameplay.
- Clear first mission unlocks the next; star best is preserved on replay.
- UI handles locked, available, completed, unpublished and offline states.
- Mobile touch and desktop mouse/keyboard navigation tested by owner.
- Content build pipeline validates schema and graph before deployment.
- No durable economic claim derives from local preview progress.
- Release has rollback and manifest-version policy.

## Known non-goals of the fixture pack
The sample draft 26-node Coconut Cove map is **not a catalog of 26 playable puzzles**. Only exact existing mission fixture references are real, and physics win proof still requires execution. No assets in this batch count as a production world map. All proposed values are subject to design and owner approval.
