# 38 — Requirement Traceability, Test Evidence and Definition of Done

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Requirement IDs
| Req | Requirement | Owner | Relevant tests | Release |
|---|---|---|---|---|
| M4-R001 | v1 service mission loads | Content/Engine | MOD-001,025 | v0.1.0 |
| M4-R002 | orders served evaluated exactly once | Domain | MOD-001,003,005 | v0.1.0 |
| M4-R003 | committed merge scores by output tier | Domain | MOD-004,017 | v0.1.0 |
| M4-R004 | win before same-tick fail | Domain | MOD-002,010 | v0.1.0 |
| M4-R005 | valid shooting and danger rules from Batch2 | Physics | PHY-001–030 | v0.1.0 |
| M4-R006 | terminal result + retry UI | UI | MOD-018,024 | v0.1.0 |
| M4-R007 | content validator | Content | MOD-013,014,025 | v0.1.1 |
| M4-R008 | manual owner playtest | Product | linked approval | all |
| M4-R009 | mode registry gates future modes | Engine/UI | MOD-019 | v0.1.1 |
| M4-R010 | star policy and best saved result | Domain | score QA | v0.1.2 |
| M4-R011 | Precision final-shot handling | Domain | MOD-007,008 | v0.2+ |
| M4-R012 | active-tick Rush clock | Domain | MOD-009,010 | future |
| M4-R013 | survival wave state machine | Domain | MOD-011 | future |
| M4-R014 | verified competitive challenge | Backend | MOD-023 + security | future |
| M4-R015 | no client-preview currency trust | Backend/QA | MOD-020 | all |

## Definition of done for DOCUMENTATION (this pack)
Each supported mode described in goal, inputs, objective, terminal conditions, fairness, UI, integration and testing. Canonical alpha contracts carried forward. JSON samples schema-checked and semantic fixtures validated. Proprietary gameplay mockups not represented as implemented code. Open questions marked proposed. Packages contain source links, workstreams and release gates.

## Definition of done for IMPLEMENTATION (not claimed by this pack)
Production code built; tests pass with actual Rapier/Phaser integration; a golden winning run recorded and replay hashes checked; low-end mobile FPS measured; errors monitored; account/currency integrity gates appropriate for release; owner manually signs off play feel; owner approves promotion to main. An engineer's “done” message is not evidence absent these artifacts.

## Evidence ledger format
`requirementId`, `commitSHA`, `PR`, `releaseVersion`, `testsExecuted`, `result/coverage`, `browserDevice`, `goldenReplayId`, `manualOwnerDecision`, `knownRisks`, `reviewer`, `timestamp`. Keep evidence links in PR/issue or release manifest; no fictional values.
