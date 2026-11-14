# 35 — Risk Register, Abuse Cases and Failure Recovery

| Risk | Symptom | Mitigation | Severity |
|---|---|---|---|
| Inaccessible published path | Player stuck with every node locked | DAG and feasibility validator; rescue action; rollback | Critical |
| Wrong mission bound | Node loads unexpected mode/board | Immutable exact mission reference and compatibility checks | High |
| Duplicate first-clear reward | Multiple coins from repeated submit | Idempotent backend receipt and unique constraints | Critical |
| UI displays local preview as trusted | Player thinks coins/scores are durable | Explicit preview labeling and separate stores | High |
| Map art overwhelms memory | Mobile tab reloads | Chunks, atlases, unload assets, instrumentation | High |
| Secret leaks | Unannounced missions exposed in public JSON | Authorized/filtered graph projection | Medium |
| New graph invalidates old progress | 100% mastery lost, gateway relocked | Stable IDs, migrations, grandfathered receipts | High |
| Timed route blocks critical path | Event expires and no path forward | Critical graph forbids event-only gates | Critical |
| Node tapping fails | Pan gesture activates mission | Pointer threshold + hit testing + list view | High |
| Map ready but game unsupported | Player enters blank puzzle | Runtime capability guard, update-required state | High |
| Hidden score exploit | Player forges stars or clears | Server-verified session receipt; no client writes | Critical |
| Content team races publish | Lost graph changes | Immutable revisions, compare-and-swap pointer | Medium |

## Incident playbooks
**Graph fails publication:** block pointer update; show linter errors by node ID; keep current live graph intact. **Broken graph already live:** rollback active pointer, preserve stored results; add a support advisory if needed. **Missing map texture:** switch to thumbnail/list without blocking missions. **Progress appears lost:** compare cached and server revisions; never overwrite durable verified data with local old state.

## Security and privacy
Public graph assets contain no privileged customer details, secret service keys or unannounced event conditions. RLS/grants and server auth required for saved progress, inventories and rewards once backend live. Don't collect exact device location for the game map or infer region ranking from world progress.

## Launch review
No critical/high risk without a mitigation and test. Include rollback flag and a named engineer on call for content publish. The owner tests visuals and usability; CI verifies proofs and schema; final release requires both.
