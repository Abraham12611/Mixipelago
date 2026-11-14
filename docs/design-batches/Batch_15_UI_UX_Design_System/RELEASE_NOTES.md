# Batch 15 — Release and Rollback Notes

**State:** proposals only. No release is marked deployed as a result of this documentation.

## Proposed rollout
1. **Contract/fixture stage:** Establish tokens, text hierarchy and component contract.
2. **Internal vertical slice:** Ship title/play/help/settings/pause/results with Phaser boundary.
3. **Trusted integration stage:** Build responsive map, shop, progression and collection slices with their gates.
4. **Protected expansion:** Add leaderboard/events/social pages only with real backend projections.
5. **Public gating:** Maintain accessibility, screen snapshots and owner manual approval with every slice.

**Version context:** Foundational tokens, responsive gameplay shell and core routes affect v0.1.x immediately; campaign/shop/profile views rollout with their systems; social, events and live interfaces are feature-gated until owned backends work.

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
