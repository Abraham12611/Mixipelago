# Engineer Kickoff — Batch 3

**Scope:** Build only the alpha-compatible drink content and merge/serving integration first. Branching recipes, pantry, rarity ownership, albums and mastery are future design proposals and must stay disabled until approved.

## Initial tasks by dependency

1. Contract team: define and validate eight-drink catalog and stable IDs (`docs/03`, `docs/18`, `examples/catalog`).
2. Simulation team: add pure catalog resolver below Batch 2 merge arbiter, never change contact sorting or body lifecycle (`docs/04`, `docs/11`, `docs/32`).
3. Orders team: auto-serve newly merged outputs to oldest matching active order; assert exactly-once output consumption and score (`docs/09`, `docs/12`).
4. Art/UI team: create distinct 2.5D silhouettes/icons, evolution strip and customer card progress; don't let sprite identities drive rules (`docs/13`, `docs/14`, `docs/31`).
5. QA: validate catalog, then run actual collision/replay, order and tutorial tests (`docs/10`, `docs/22`, `docs/29`, `docs/30`).

## Commands for documentation fixtures

```bash
python tools/validate_batch3.py
```

This validator checks content structure and canonical mapping. **It does not simulate Rapier or certify a level as playable.** The first mission sample is deliberately `candidate/unproven` until a real successful trace is recorded.

## Owner/coordinator controls

All gameplay-feel and manual UI tests go to the owner. Engineers open reviewed feature PRs and should not merge into main without owner authorization. Every implementation PR must identify which catalog/rules/replay hashes it changes and attach relevant automated test results.

## Integration notes

Read `docs/33_BATCH_1_2_INTEGRATION_AND_DELTA.md` before changing shared core types or existing server-event payloads. Prefer additive changes with explicit schema versions.
