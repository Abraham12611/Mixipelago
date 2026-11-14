# 28 — Offline preview, sync and conflict resolution

> Mixipelago Batch 18/21 · Backend, Database, Game Services & Admin Studio · Status: **proposed engineering specification**, not proof of implementation · 2026-11-14

## Intent and concrete player outcome

Keep local preview state isolated from trusted profile, with versioned storage schema and explicit reconciliation UX. This is a player-facing goal and a boundary for implementation: engineers should be able to demonstrate it in a small isolated fixture before integrating with the rest of Mixipelago. Backend / Data / Admin Platform owns the specification; dependent teams consume a versioned interface, not hidden internal state.

## Required functional behavior

1. Local achievements and preview coins are not silently promoted to server-verified identity.
2. The implementation must expose any missing, unavailable, unauthorized or outdated state explicitly. A failed backend command, missing artwork, browser audio restriction, or unsupported device capability cannot be presented as successful work.
3. Preserve the user-facing contract when moving across desktop and mobile: effect and presentation timing can vary, but the same accepted gameplay commands and trusted content version produce the same rules result.
4. Store stable identities and immutable published revisions. A name, visual skin, translated label, CDN URL, region or price display does not become a durable identity just because it is visible in a screenshot.
5. Record any decision that would affect player fairness, financial entitlement, customer service or ranked scores as an architecture decision rather than adding a local UI special case.

## Proposed state, interfaces and versioning

**Owned domain:** Accounts, server-verified state, database writes, domain API routes, content publishing, admin controls and durable event delivery.

**Data contract vocabulary:** `requestId`, `actorId`, `sourceReceiptId`, `rulesHash`, `catalogHash`, `idempotencyKey`, `resultRevision`. Only fields meaningful to this specific implementation should be present in runtime messages; this list is a cross-batch checklist, not a requirement to copy every field into every event.

- **Input:** a typed request or event associated with a named actor, source object and published content/rules revision. In local alpha mode the input is marked `local_preview` and cannot request server rewards.
- **Pure decision:** evaluate offline preview, sync and conflict resolution using a published policy snapshot and validated domain identifiers; keep numerical calculations and fallbacks in testable functions.
- **Output:** an explicit success, unavailable, rejected or pending projection containing a stable revision or correlation ID. UI effects can subscribe to this projection but cannot rewrite it.
- **Audit:** if the operation changes persistent ownership, finance, reputation, competitive state or access, the responsible Batch 18 server owner records an immutable receipt and outbox event. Cosmetic-only UI effects do not require a wallet receipt.

### Ownership and integration

Batches 02–04 physics/missions, 05 campaign, 06 ledger, 07 XP, 08 entitlements, 09 guests, 10 world, 11 stories, 12 events, 13 rankings, 14 social and 15 UI.

This document must **not** bypass Batch 2's deterministic merge arbitration, Batch 3's order-serving priority, Batch 4's mission result rules, Batch 6's server-owned coin ledger, Batch 7's XP rules, Batch 8's collectible entitlement origin or Batch 13's normalized competition policy. When an interface appears to conflict, pin an ADR and use the earlier owning domain's contract.

## Golden path and exceptional case

**Nominal path:** a player starts with an approved content version, requests or witnesses the relevant offline preview, sync and conflict resolution feature, the owning service validates eligibility and records exactly one permissible state transition, and the presentation layer receives an explanatory result. The player retains accurate status after a reload and can use the feature from an appropriate device class without hidden prerequisites.

**Known failure to prevent:** Reinstall without account does not claim durable cloud saves; signed-in account restores verified inventory. A retry must return the original committed result for durable mutations. If the feature is disabled, keep a safe read-only view or a genuine not-available message, not a fake button or a fabricated reward animation.

**Offline/reconnect:** local previews are display-only and clearly marked. Trusted reads may show last-synced values with a timestamp; trusted writes queue only where a signed idempotency protocol supports it, and never mint offline currency, XP, prizes or rank.

## Acceptance criteria and tests

- **Primary golden fixture:** Reinstall without account does not claim durable cloud saves; signed-in account restores verified inventory.
- Test incorrect catalog hash, revoked account/permission (when relevant), missing asset or unavailable service, duplicate message delivery, and a stale client revision.
- Test a mobile narrow layout, a desktop input path, accessibility labels and reduced motion/audio where this feature has a visible UI.
- Test concurrent request handling if the chapter touches persistent commands; exactly-once *effects*, not transport delivery, must be proven with database constraints.
- Capture evidence in the engineer PR: fixture ID, command or event schema revision, expected state, observed state and the test artifact. All manual UI, art, listening and gameplay-feel approvals are directed to the user.

## Implementation handoff and release condition

1. Freeze the pure data/contract signature for **Offline preview, sync and conflict resolution** and write the nominal and invalid fixtures from above.
2. Implement the source domain's validation first, then create an isolated adapter and accessible read projection; use explicit `featureGate=TRUSTED_BACKEND_ENABLED` where advanced functionality is involved.
3. Integrate with Typed API, Postgres migrations, outbox consumers and read projections. Keep fallback behavior documented: local preview with explicit unverified labels.
4. Write tests for idempotence, actor authorization, version pins and safe recovery, then instrument aggregate health without raw personal or secret data.
5. Produce a reviewer packet and owner-directed manual acceptance instructions. This chapter is a **first-release foundation** only if it directly enables the browser alpha; otherwise its feature stays disabled until the relevant backend/asset/system owner signs off.

**Batch release target:** trusted foundation v0.3.x+; advanced services by feature. **Related chapters:** preceding area `Realtime, subscriptions and consistency choices`; following area `Auditability, reconciliation and data lineage`.

## Unresolved decisions

Precise animation timings, balance numbers, platform/device limits, public artwork and pricing are **proposed** until a named owner approves them against measured evidence. The engineer should document chosen values, the tradeoff, a migration path and a fallback, not quietly replace the design.
