# 29 — Architecture Decisions, Risks and Owner Questions

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## ADR-06-01: Server-owned persistent coins
Decision: no persistent wallet until verified receipt, ledger and purchase service exist. Reason: browser-origin values are untrusted. Risk: slower first shop rollout. Mitigation: preview-only feedback in alpha.

## ADR-06-02: No global wealth inflation formula
Decision: price by authored upgrade, island phase and content version; not arbitrary dynamic price escalation tied to current wealth. Reason: avoid punishing savers and unpredictable UX.

## ADR-06-03: Normalized competitive modes
Decision: economic modifiers disabled unless entire competition declares equal equipment loadout. Reason: puzzle rankings should measure puzzle skill.

## ADR-06-04: Starter shop preserved
Decision: one permanently accessible starter shop and free core missions, even after later incidents or debt. Reason: avoid irreversible softlocks.

## ADR-06-05: No passive earnings at first launch
Decision: defer idle income, operating costs and staff salary loops until balancing instrumentation exists.

## Open for owner workshop
1. Are shop utility upgrades puzzle-strength, service-management-only, or both? Proposed: service-management-only in campaign, standardized rankings.
2. Can cosmetics be resold? Proposed: no, but free equip/unequip.
3. Should VIP probability be shown exactly? Proposed: yes whenever a percentage is sold.
4. Will players manage a single active shop or several? Proposed: one v0.3, several later.
5. Should there ever be energy limits? Proposed: do not paywall basic gameplay behind harsh energy.
6. Are debts allowed to affect reputation? Proposed: only bounded, opt-in future event policies.

## Risk register
Currency inflation; item purchase that does nothing; exploit from repeated low-tier missions; reward duplication via concurrent writes; inconsistent shop effects across modes; false UI purchase success; developer test accounts polluting metrics; content author publishing extreme prices; fragile migrations; regulatory challenges if future tokens become real-money exchangeable. Each requires test/monitoring and rollback owner.
