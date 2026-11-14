# 90 — Engineering Implementation Blueprint: Batch 19

**Status:** detailed proposed implementation · Not deployed · 2026-11-14.

## Intended architecture

```text
Client claim -> authenticate -> authorize resource
  -> validate payload schema and rate budget
  -> pin signed session/catalog profile
  -> replay Rapier simulation with accepted commands
  -> compare certified result and expected hash
  -> issue immutable source receipt
  -> exactly-once reward/score consumers
  -> security monitoring and periodic reconciliation
```

**Threat example:** replaying a genuine successful shot log under a different session ID must fail its source binding. A reused idempotency key with a different request fingerprint conflicts, not duplicates. Service-role secrets never exist in frontend JS or source maps. Support staff can view receipt lineage but cannot directly adjust `wallet.balance`.

**Negative-test program:** permission matrix for cross-account reads, malformed/NaN vectors, collision graph double-claims, missing content hashes, paused-run time manipulation, double credit, forged store receipts, blocklist bypass and privilege escalation. No production verification claim until staging real-provider and DB-role tests pass.

## Domain contracts that cannot be bypassed

- Browser and native clients are untrusted even when running unmodified UI.
- Every data access is authenticated and authorized; exposed DB tables require appropriate RLS/grants.
- Deterministic replay verification, not score upload, gates certified competition and valuable rewards.
- Idempotent grants and compensating ledger entries prevent duplicated and invisible financial changes.
- No security mitigation may disable safe alpha play or quietly invent verified outcomes.

## Proposed typed interface and persistence vocabulary

Candidate fields: `threatId`, `domain`, `controlId`, `severity`, `negativeTest`, `mitigationOwner`, `rolloutGate`. Create implementation types in `packages/contracts` and pure helpers in `packages/domain`; do not import production secrets, database clients or browser globals into the simulation rules.

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
