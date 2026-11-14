# 01 — Product vision, visual goals and first-ship boundaries

> Mixipelago Batch 16/21 · Art Direction, Characters & 2.5D Asset Production · Status: **proposed engineering specification**, not proof of implementation · 2026-11-14

## Intent and concrete player outcome

Establish the tropical, glossy 2.5D casual-game look while prioritizing unmistakable drink silhouettes and a restrained, legible board. This is a player-facing goal and a boundary for implementation: engineers should be able to demonstrate it in a small isolated fixture before integrating with the rest of Mixipelago. Visual / Art Pipeline owns the specification; dependent teams consume a versioned interface, not hidden internal state.

## Required functional behavior

1. Mood-board art is not a usable asset; every shipped element needs an original approved source and a versioned manifest entry.
2. The implementation must expose any missing, unavailable, unauthorized or outdated state explicitly. A failed backend command, missing artwork, browser audio restriction, or unsupported device capability cannot be presented as successful work.
3. Preserve the user-facing contract when moving across desktop and mobile: effect and presentation timing can vary, but the same accepted gameplay commands and trusted content version produce the same rules result.
4. Store stable identities and immutable published revisions. A name, visual skin, translated label, CDN URL, region or price display does not become a durable identity just because it is visible in a screenshot.
5. Record any decision that would affect player fairness, financial entitlement, customer service or ranked scores as an architecture decision rather than adding a local UI special case.

## Proposed state, interfaces and versioning

**Owned domain:** Visual content, export configurations, asset provenance and art presentation; never gameplay physics or ownership.

**Data contract vocabulary:** `assetId`, `kind`, `displayName`, `status`, `sourcePolicy`, `licenseState`, `renderProfile`, `fallbackAssetId`. Only fields meaningful to this specific implementation should be present in runtime messages; this list is a cross-batch checklist, not a requirement to copy every field into every event.

- **Input:** a typed request or event associated with a named actor, source object and published content/rules revision. In local alpha mode the input is marked `local_preview` and cannot request server rewards.
- **Pure decision:** evaluate product vision, visual goals and first-ship boundaries using a published policy snapshot and validated domain identifiers; keep numerical calculations and fallbacks in testable functions.
- **Output:** an explicit success, unavailable, rejected or pending projection containing a stable revision or correlation ID. UI effects can subscribe to this projection but cannot rewrite it.
- **Audit:** if the operation changes persistent ownership, finance, reputation, competitive state or access, the responsible Batch 18 server owner records an immutable receipt and outbox event. Cosmetic-only UI effects do not require a wallet receipt.

### Ownership and integration

Batch 15 responsive UI and token system; Batch 02 collider/body config; Batch 03 drink IDs; Batch 05 island graphs; Batch 08 collectible metadata; Batch 09 fictional customer IDs.

This document must **not** bypass Batch 2's deterministic merge arbitration, Batch 3's order-serving priority, Batch 4's mission result rules, Batch 6's server-owned coin ledger, Batch 7's XP rules, Batch 8's collectible entitlement origin or Batch 13's normalized competition policy. When an interface appears to conflict, pin an ADR and use the earlier owning domain's contract.

## Golden path and exceptional case

**Nominal path:** a player starts with an approved content version, requests or witnesses the relevant product vision, visual goals and first-ship boundaries feature, the owning service validates eligibility and records exactly one permissible state transition, and the presentation layer receives an explanatory result. The player retains accurate status after a reload and can use the feature from an appropriate device class without hidden prerequisites.

**Known failure to prevent:** At 44 CSS pixels each of the eight starter drinks is identifiable without relying on hue alone. A retry must return the original committed result for durable mutations. If the feature is disabled, keep a safe read-only view or a genuine not-available message, not a fake button or a fabricated reward animation.

**Offline/reconnect:** local previews are display-only and clearly marked. Trusted reads may show last-synced values with a timestamp; trusted writes queue only where a signed idempotency protocol supports it, and never mint offline currency, XP, prizes or rank.

## Acceptance criteria and tests

- **Primary golden fixture:** At 44 CSS pixels each of the eight starter drinks is identifiable without relying on hue alone.
- Test incorrect catalog hash, revoked account/permission (when relevant), missing asset or unavailable service, duplicate message delivery, and a stale client revision.
- Test a mobile narrow layout, a desktop input path, accessibility labels and reduced motion/audio where this feature has a visible UI.
- Test concurrent request handling if the chapter touches persistent commands; exactly-once *effects*, not transport delivery, must be proven with database constraints.
- Capture evidence in the engineer PR: fixture ID, command or event schema revision, expected state, observed state and the test artifact. All manual UI, art, listening and gameplay-feel approvals are directed to the user.

## Implementation handoff and release condition

1. Freeze the pure data/contract signature for **Product vision, visual goals and first-ship boundaries** and write the nominal and invalid fixtures from above.
2. Implement the source domain's validation first, then create an isolated adapter and accessible read projection; use explicit `featureGate=ART_PIPELINE_ENABLED` where advanced functionality is involved.
3. Integrate with Manifest validator, Blender render preset, atlas export checks and lazy Phaser loader. Keep fallback behavior documented: low memory texture atlas fallback, missing-art labeled cards.
4. Write tests for idempotence, actor authorization, version pins and safe recovery, then instrument aggregate health without raw personal or secret data.
5. Produce a reviewer packet and owner-directed manual acceptance instructions. This chapter is a **first-release foundation** only if it directly enables the browser alpha; otherwise its feature stays disabled until the relevant backend/asset/system owner signs off.

**Batch release target:** v0.1.x foundational, extended with island/shop releases. **Related chapters:** preceding area `batch overview`; following area `Visual grammar, shapes, silhouettes and material families`.

## Unresolved decisions

Precise animation timings, balance numbers, platform/device limits, public artwork and pricing are **proposed** until a named owner approves them against measured evidence. The engineer should document chosen values, the tradeoff, a migration path and a fallback, not quietly replace the design.
