# Batch 13 — Release and Rollback Notes

**State:** proposals only. No release is marked deployed as a result of this documentation.

## Proposed rollout
1. **Contract/fixture stage:** Certify replay worker and normalized profile first.
2. **Internal vertical slice:** Add verified score submit/decision states.
3. **Trusted integration stage:** Materialize one public weekly board and around-me query.
4. **Protected expansion:** Freeze season and settle cosmetic prizes via Batch 08.
5. **Public gating:** Add filters/divisions/tournament only after privacy and moderation.

**Version context:** One normalized weekly global challenge after verified server replay (candidate v0.5.0); historical seasons/divisions v0.5.1+; tournaments and opt-in regional boards after safeguards.

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
