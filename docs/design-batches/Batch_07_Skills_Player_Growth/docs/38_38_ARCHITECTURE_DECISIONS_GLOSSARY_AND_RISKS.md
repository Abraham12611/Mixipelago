# 38 — Architecture Decisions, Risks, Open Questions and Glossary

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Decisions proposed for approval
- ADR-07-001: XP/points are separate from coins; no local-preview migration into trusted XP.
- ADR-07-002: Player skill ownership and allocation are server-authoritative; UI previews are not proof.
- ADR-07-003: Skill effects are typed and applied through Batch 6's published modifier system.
- ADR-07-004: Ranked modes use a canonical profile independent of personal talents and shop investments.
- ADR-07-005: Respec is accessible and cannot destroy previously earned campaign progress.
- ADR-07-006: Mastery and full active skill loadouts are later-gated features, not alpha requirements.

## Open product questions
Should early points always be granted at every level or include non-XP achievements? What is the exact ratio of UI-information skills to direct coin benefits? Should the first respec be permanently free? How many skills should display by default on a narrow phone? Which hints are baseline accessibility versus optional knowledge aid? Resolve through user testing and written owner approval, not unilateral engineering decisions.

## Risks and mitigations
- **Runaway payout snowball:** hard caps, independent simulation, transaction receipts, rollback gate.
- **Obvious best build:** diversify utility, context restrictions, telemetry cohort comparisons.
- **Unfair ranked advantage:** canonical profile before session begins, replay verification.
- **Unsatisfying XP grind:** first-clear pacing tests, multiple accessible missions, never require endless repeat farming.
- **Opaque graph:** precise locked-state explanations, planner, accessible list view.
- **Catalog migrations invalidate player choices:** point refund, suspension, version-pinned grants, reversible flag.
- **Cross-system code coupling:** pure rules package and typed event handoffs.

## Glossary
**Entitlement**: a uniquely validated grant source. **Skill rank**: an invested position within a node. **Loadout**: active abilities selected for a particular mode. **Modifier snapshot**: derived context-specific effects pinned to a session or quote. **Normalized competitive profile**: standardized set of assists and bonuses for fair comparison. **Respec**: refund/realignment of current skill allocations, not a reset of earned XP. **Grandfathered benefit**: a supported legacy entitlement preserved across a content revision.
