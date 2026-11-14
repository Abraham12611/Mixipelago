# Batch 12 — Release and Rollback Notes

**State:** proposals only. No release is marked deployed as a result of this documentation.

## Proposed rollout
1. **Contract/fixture stage:** Publish event read model and UTC clock fixtures.
2. **Internal vertical slice:** Build event hub, single activity and limited calendar.
3. **Trusted integration stage:** Wire verified contribution to existing mission result.
4. **Protected expansion:** Grant one owned cosmetic via Batch 08 trusted entitlement.
5. **Public gating:** Add archive, cancellation operations and community goals later.

**Version context:** Candidate first opt-in festival and a single authored event mission after campaign and trusted rewards (v0.6.2); calendar rotation, community goals and seasonal live programs staged later.

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
