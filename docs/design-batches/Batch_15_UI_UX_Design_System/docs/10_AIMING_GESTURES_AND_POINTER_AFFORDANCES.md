# 10 — Aiming, gestures and pointer affordances

**Batch 15/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Make precision aiming approachable on touch and mouse.

## Required behavior and invariants
1. Gesture region maps pointer to world coordinates from Batch 02; aim arrow/trail indicates legal launch, not perfect preview unless feature enabled.
2. Support cancel drag, pointer loss, multi-touch rejection, keyboard nudges and help overlay.
3. Reduced-motion retains aim direction and hit region clarity.

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
Never launch shot when user scrolls the page outside board or presses Settings.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Touchstart-drag-release and mouse-kb path yield equivalent commands.

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
