# Batch 14 — Release and Rollback Notes

**State:** proposals only. No release is marked deployed as a result of this documentation.

## Proposed rollout
1. **Contract/fixture stage:** Release privacy settings, block/report and friend graph.
2. **Internal vertical slice:** Add certified asynchronous challenge over Batch 13 verified runs.
3. **Trusted integration stage:** Add crew membership/permissions and one verified project.
4. **Protected expansion:** Test moderation, fairness, replay and recovery under concurrency.
5. **Public gating:** Prove authoritative live match server before any real-time UI launch.

**Version context:** Candidate v0.7.0 friends + asynchronous ghost challenges; v0.7.1 crew projects; v0.8.0+ real-time matches only after authoritative simulation, reconnect and moderation tests.

## Gates (all OFF by default)
See `examples/catalog/catalog.draft.json` for the actual draft gate names. A gate is on only after implementation, staged acceptance, security review (where applicable), and owner authorization. Deploying schema alone does not enable a feature.

## Rollback
Disable new entry/command creation; keep already committed player data and immutable receipts. Rebuild projections from server-owned facts. Do not erase legitimate ownership, achievement badges, score receipts, choices or social blocks. For an incompatible content revision, publish a forward migration or a safe read-only state.

## QA evidence
- Static sample schema validation and pure-rule fixtures.
- Authentication and authorization tests for mutations.
- Duplicate/replay/multi-tab and asynchronous retry behavior.
- No-break smoke tests for v0.1 game board, oldest matching order auto-serve, and offline preview labeling.
- Owner-directed manual UI/gameplay acceptance, not agent-assumed visual approval.
