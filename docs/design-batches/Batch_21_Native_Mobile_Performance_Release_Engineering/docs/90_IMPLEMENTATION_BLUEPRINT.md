# 90 — Engineering Implementation Blueprint: Batch 21

**Status:** detailed proposed implementation · Not deployed · 2026-11-14.

## Intended architecture

```text
Git PR -> lint/typecheck/asset QA/replay golden tests
  -> web preview + owner manual UI acceptance
  -> pinned web export + Capacitor sync
  -> Android AAB + iOS archive with protected signing
  -> native device test matrix + privacy disclosures
  -> internal/closed beta, staged store submission
  -> crash/latency monitoring + safe feature rollback
```

**Native adapter:** `PlatformCapabilities` includes haptics, secureStorage, deepLinks, notifications, billing and appLifecycle with browser stubs. No platform plugin can directly issue a trusted reward. Browser and native call the same pure simulation core at fixed 60 Hz; device quality profiles only change presentation.

**As-of 2026-11-14 policy snapshot:** new Google Play Android phone app submissions and updates target API 36+ (Android 16); Apple App Store Connect uploads require Xcode 26+ and iOS 26 SDK+ (per linked current guidance). Capacitor docs require Node 22+ and Xcode 26+ for current iOS tooling. Reconfirm store policy, Xcode SDK and Capacitor compatibility immediately before submission.

## Domain contracts that cannot be bypassed

- Web game remains source of truth for physics semantics and public feature ordering.
- Native capability plugins cannot bypass backend reward verification or user permissions.
- Stores require real functional review builds, accurate privacy disclosure and owner signoff.
- Frame-quality adaptations affect render only; 60 Hz fixed simulation/replay profile stays pinned.
- Browser-first playable alpha remains a viable fallback if app reviews or native rollout slip.

## Proposed typed interface and persistence vocabulary

Candidate fields: `clientVersion`, `buildNumber`, `platform`, `contentHash`, `minimumSupportedApi`, `policyReviewDate`, `releaseChannel`. Create implementation types in `packages/contracts` and pure helpers in `packages/domain`; do not import production secrets, database clients or browser globals into the simulation rules.

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
