# 90 — Engineering Implementation Blueprint: Batch 17

**Status:** detailed proposed implementation · Not deployed · 2026-11-14.

## Intended architecture

```text
GameEvent(eventId, type, sourceObjectId)
  -> presentation event router
  -> catalog lookup + bus/priority policy
  -> duplicate eventId guard + per-material cooldown
  -> AudioContext (user-gesture-unlocked) + voice pool
  -> optional pan / mixer ducking / fade
  -> telemetry aggregate (never gameplay state)
```

**Voice priority:** victory/accessible alert > merge > serve > launch > repeated contact > ambience. Select only safe cue IDs in published catalog; unlicensed or missing audio silently becomes a visual-only event, never a game failure. Releasing a Phaser scene must remove listeners and reclaim active sources.

**Interruption policy:** on visibility loss, suspend appropriate buses and freeze active-time simulation via the existing game shell, but audio does not itself decide terminal session state. On resume, restore user preferences only after allowed user interaction; never surprise with loud music.

## Domain contracts that cannot be bypassed

- Every cue uses a versioned semantic event ID, not an arbitrary DOM animation to infer success.
- Playback never influences Rapier simulation, deterministic score, customer auto-serving or durable rewards.
- Web audio starts/resumes through an accepted user interaction when autoplay policies require it.
- All actionable states remain visible/accessibly announced when sound and haptics are disabled.
- Original/commercially licensed audio sources and creator consent are required before production release.

## Proposed typed interface and persistence vocabulary

Candidate fields: `cueId`, `eventName`, `bus`, `priority`, `voiceLimit`, `status`, `rightsState`, `fallback`. Create implementation types in `packages/contracts` and pure helpers in `packages/domain`; do not import production secrets, database clients or browser globals into the simulation rules.

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
