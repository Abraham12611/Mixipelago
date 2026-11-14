# 90 — Engineering Implementation Blueprint: Batch 18

**Status:** detailed proposed implementation · Not deployed · 2026-11-14.

## Intended architecture

```text
Client starts session (no trusted claims)
  -> API authenticates and pins content/physics/scoring
  -> inputs accepted within session rules
  -> replay verifier certifies MissionResult
  -> one immutable verified_result receipt
  -> transactional outbox and unique first-clear entitlement keys
  -> economy/XP/reward/campaign/ranking consumers (each idempotent)
  -> player projections and reconciled read APIs
```

**Canonical transaction:** validate actor and signed session, lock affected rows, insert unique receipt, apply authorized ledger/inventory/XP state changes via owning domain, append outbox event, commit. If a worker crashes after commit, replay original event; do not regrant. `GET /wallet` and profile projections are private and never CDN-shared.

**Migration policy:** preview-only game first. Add auth, read-only profile, session verification, one trusted reward, then wallet and inventory. Separate all privileged Content Studio roles from game players. Test RLS with real `anon`, `authenticated`, and elevated roles before releasing any data endpoint.

## Domain contracts that cannot be bypassed

- Local alpha preview play is independent from login, persistent servers and paid services.
- Only a verified server receipt can issue trusted coins, XP, achievements, ranks or shop entitlements.
- Each domain has one transaction owner; message delivery is at least once with idempotent effects.
- Client-provided player IDs, prices, reward amounts and success flags have no authority.
- Published content is immutable by digest; active runs pin mission/physics/catalog versions.

## Proposed typed interface and persistence vocabulary

Candidate fields: `requestId`, `actorId`, `sourceReceiptId`, `rulesHash`, `catalogHash`, `idempotencyKey`, `resultRevision`. Create implementation types in `packages/contracts` and pure helpers in `packages/domain`; do not import production secrets, database clients or browser globals into the simulation rules.

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
