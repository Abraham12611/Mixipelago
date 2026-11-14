# Batch 10 — Release and Rollback Notes

**State:** proposals only. No release is marked deployed as a result of this documentation.

## Proposed rollout
1. **Contract/fixture stage:** Define immutable world condition read model and kill switch.
2. **Internal vertical slice:** Render harmless condition overlay on map, with reduced motion.
3. **Trusted integration stage:** Introduce authored opt-in offers and idempotent incident choice receipts.
4. **Protected expansion:** Integrate verified mission/world consequences through Batch 06 domain.
5. **Public gating:** Enable operator dashboards, audit, recovery and rollback.

**Version context:** Preview weather overlays after the first campaign (candidate v0.6.0); authored opt-in incidents and recovery (v0.6.1+); shop-economic world effects only after audited server-ledger integration (v0.7+).

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
