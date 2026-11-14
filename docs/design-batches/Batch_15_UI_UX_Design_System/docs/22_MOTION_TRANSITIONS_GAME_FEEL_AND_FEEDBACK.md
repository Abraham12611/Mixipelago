# 22 — Motion, transitions, game feel and feedback

**Batch 15/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Provide polished feedback without hiding important state.

## Required behavior and invariants
1. Animation hierarchy: gameplay-critical (serve/combo) > status change > decoration.
2. CSS/GSAP for UI movement and Phaser for board VFX; honor prefers-reduced-motion.
3. Duration candidates: press 80–140ms, panel 180–260ms, victory up to 700ms, all tunable.

## Cross-domain contract

**Ownership:** Information architecture, token system, UI component API, responsive design, motion, accessibility, app page states and screen-to-domain contracts.
**Handoffs:** Batch 01 React/Phaser boundary; Batch 02 board; Batch 03 drinks; Batch 04 missions; Batch 05 map; Batches 06–14 screens and projections; Batch 16 art production.

| Interface | Requirement |
|---|---|
| State authority | routeGate, viewModel revision and current responsive breakpoint |
| Input contract | ui.route_entered / game HUD projection update |
| Transition and output | accessible DOM/Phaser visual state |
| Audit/versioning | token edition, screen schema and visual regression snapshot |

The owning service must validate published content IDs and the authenticated actor before a persistent mutation. Every new semantic event includes `eventId`, `schemaVersion`, `sourceId`, `rulesHash`/`catalogHash` where applicable, and correlation metadata. Consumer retries must be idempotent. Avoid undocumented direct writes between domain tables.

## Exceptional states, recovery and fairness
Avoid pulsing all interactive controls simultaneously or long unskippable wins.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Reduced motion shows immediate status text, no spinning fireworks.

Tests must also cover unauthorized actor, duplicate event, stale content version, concurrent request, reload, offline/error recovery and accessibility as appropriate. Manual UI/gameplay feel tests are directed to the owner; unit and integration tests are the engineering team’s responsibility.

## Implementation handoff
1. Freeze the public TypeScript/JSON contract and the feature gate; add a minimal golden fixture.
2. Implement the pure rule or state transition before UI wiring; prove idempotence and safe migration.
3. Add read projection and an accessible view; integrate only with existing service authority.
4. Add telemetry, documented rollback, API error states and a PR description covering dependent batches.

**First-release rule:** Foundational tokens, responsive gameplay shell and core routes affect v0.1.x immediately; campaign/shop/profile views rollout with their systems; social, events and live interfaces are feature-gated until owned backends work.

**Batch-wide invariant:** Phaser owns the visual tabletop and immediate collision effects; React owns accessible application controls and HUD projections. Every route is feature-gated, no fake functionality. User-generated illustrations can be decorative but interactive UI remains semantic and responsive.

## Decisions requiring review
Do not treat numerical values, character/world concepts, scheduling dates or content examples as owner-approved production policy. Mark unresolved choices in the implementation PR, and pin released rule revisions before grant or rank settlement.
