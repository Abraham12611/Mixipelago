# 32 — Phased Release Strategy and Feature Gates

## Releases are incremental product slices
`v0.1.0` = core playable alpha; Batch 5 is not a launch dependency. `v0.1.1` stabilizes. `v0.1.2` can add a small authored mission picker and result history if ready. `v0.2.0` introduces the first meaningful island map; subsequent `v0.2.x` updates expand verified missions and discovery. A `v1.0.0` designation is reserved for mature readiness, not arbitrary scope completion.

## Phase B5-A — Foundation (can parallelize with v0.1.x)
A1 graph schema and pure evaluator; A2 two-node published-compatible sample; A3 local preview result adapter; A4 validation CLI and CI; A5 basic map scene with buttons to open existing mission content. Gate: MAP-001 through MAP-007 and no regression to gameplay.

## Phase B5-B — First map vertical slice (target v0.2.0)
B1 author a genuinely tested set of ~6–12 missions or 20–40 if team produces proofs; B2 mobile/desktop map pan/zoom/selection; B3 stars and chapter progression; B4 first branch and simple contextual cards; B5 map asset pipeline/chunk loading. Gate: no dead ends, owner manual UX signoff and good performance.

## Phase B5-C — Content expansion (v0.2.1–v0.2.x)
C1 new districts and chapter checkpoints; C2 gateway preview; C3 optional hidden route and one-time demo treasure; C4 map editor prototype; C5 telemetry-based difficulty and navigation polish. Keep first island as priority rather than announcing many unplayable regions.

## Phase B5-D — Trusted sync (when account and economy work lands)
D1 verified session receipt adapter; D2 RLS/authorization; D3 durable progress and idempotent rewards; D4 cross-device reconciliation; D5 safe graph rollback/migrations. Don't couple this to temporary preview coins.

## Phase B5-E — Archipelago expansion (future minors)
E1 second published island with gateway and bundle; E2 district-specific art/audio; E3 large content catalog/editor scaling; E4 secrets and collectibles backed by services; E5 optional stories, shops, events and dynamic world modifiers as other batches ship.

## Gates for every release
- Feature flag resolves against actual deployed client capabilities.
- All published nodes reference playable, tested missions.
- Pure unlock tests and graph validation pass.
- Static image references and content hashes resolve.
- No regression to stars, mission scores or local saves.
- Core map path is usable on target mobile and desktop devices.
- Owner manual testing and main promotion approval completed.
- Release notes, rollback plan and monitoring ready.

## What not to claim
`20–40 nodes` is an optional target, not an acceptance substitute for good levels. Static graph reachability does not prove physics solvability. Local preview progress is not verified leaderboard/rank/economy state.
