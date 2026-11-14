# 90 — Engineering Implementation Blueprint: Batch 20

**Status:** detailed proposed implementation · Not deployed · 2026-11-14.

## Intended architecture

```text
Published optional SKU (disabled until approved)
  -> compliant platform/native/web storefront quote
  -> provider checkout with actor/order correlation
  -> backend signed receipt verification
  -> unique (provider, transaction) entitlement settlement
  -> inventory projection (cosmetic only)
  -> refund/restore/reconcile route
```

**Pricing policy:** real money never enters the soft-coin ledger as a raw client amount. Displayed price must come from store/provider quote and match purchaser's platform/region. A blocked or cancelled checkout cannot prevent a mission from being played. Store receipt events are financial facts; `checkout_clicked` is only analytics.

**Experimentation:** consistent bucket hash, pre-registered outcome/guardrails, exclusion of underage/consent restricted cohorts, stopping rules, rollback on economy fairness or access regressions. For analytics, encode event version + consent level, dedup by eventId, and never treat telemetry as an XP or wallet issuer.

## Domain contracts that cannot be bypassed

- Monetization is optional and unnecessary for mainline puzzle progress.
- Paid offers, ads and passes are OFF-by-default until store, privacy and backend checks are complete.
- Normalized ranked play cannot depend on wallet, purchase, cosmetic or shop/skill advantages.
- Financial revenue reports reconcile provider confirmations and refunds; analytics clicks are not receipts.
- Player privacy, age appropriateness and anti-compulsion rules take priority over growth experiments.

## Proposed typed interface and persistence vocabulary

Candidate fields: `skuId`, `category`, `platformPolicy`, `enabled`, `itemId`, `purchaseReceiptId`, `refundable`. Create implementation types in `packages/contracts` and pure helpers in `packages/domain`; do not import production secrets, database clients or browser globals into the simulation rules.

Each durable command requires an authenticated actor, a stable source identity, a published rules/content revision and a unique idempotency key. Source-of-truth services generate their own receipt IDs and return structured `rejected`, `pending` or `confirmed` states. The React UI and Phaser renderer consume projections and events only.

## Suggested package boundaries

```text
apps/web/               # Next.js shell + React controls + Phaser canvas
apps/admin/             # role-checked internal content review (later)
packages/contracts/     # source-versioned event and API payloads
packages/domain/        # pure gameplay/economy/security/capability functions
packages/simulation/    # Rapier, fixed 60Hz, merge arbitration; never backend grants
packages/content/       # approved manifest IDs and schema verification
packages/ui/            # Batch 15 semantic controls and accessible state
services/api/           # trusted actor-scoped commands (not needed for local alpha)
services/workers/       # outbox consumers, reconciliation and scheduled jobs
```

## Incremental integration checkpoints

1. Implement a pure golden-rule fixture and a schema validator for the sample data, storing initial decisions in an ADR.
2. Add feature-gated read-only projections. The game must still load and accept gameplay inputs without this feature enabled.
3. Add one canonical event bridge or command to a test harness. Verify that repeated delivery doesn't duplicate durable effects.
4. Wire UI and telemetry only after the domain adapter is correct and accessibility/low-performance fallbacks are in place.
5. Instrument failure states and rollback. Test offline recovery and stale manifest, then prepare an owner review packet with commands and observed results.

## Explicit exclusions

- Do not treat draft JSON examples as a signed-off production catalog or ready-to-apply SQL migration.
- Do not invent a paid product, unlocked island, real player entitlement or certified competitive score to make a UI look complete.
- Do not conflate local preview achievements, coins, customer happiness animations or audio success with verified backend facts.
- Do not execute real platform store submission or payment setup as part of this documentation task.

## Definition of Done

The owner can reproduce the fixture results, dependency graph is green, one happy path and at least three negative paths pass, the release flag defaults OFF for advanced functionality, rollback preserves published/purchased state, and the engineering PR records exact schema and content digests. Manual art/UI/audio/gameplay review is directed to the user.
