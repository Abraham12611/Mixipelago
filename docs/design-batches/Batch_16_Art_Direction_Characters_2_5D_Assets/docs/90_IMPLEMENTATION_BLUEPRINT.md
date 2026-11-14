# 90 — Engineering Implementation Blueprint: Batch 16

**Status:** detailed proposed implementation · Not deployed · 2026-11-14.

## Intended architecture

```text
asset source (.blend/.kra/.svg)
  -> license/provenance review
  -> orthographic Blender render + transparent passes
  -> image cleanup / trim / atlas export
  -> metadata + digest validator
  -> staged visual QA & owner approval
  -> immutable asset catalog/CDN URL
  -> Phaser manifest loader with labeled placeholders
```

**Renderer recipe (candidate):** orthographic view, stable key light, consistent color space and pivot; 256×320 source pixels for eight board drinks; 1×/2× export tiers after device review. Every texture source has a distinct `assetId` and versioned digest. Keep physical radius only in Batch 2 physics preset; a tall garnish must not enlarge a rigid-body collider by implication.

**Publish algorithm:** validate all required asset IDs and references, verify license/creator permissions, compute source/delivery hashes, ensure no unapproved files, run visual QA, stage pointer to immutable manifest, obtain owner approval, then switch published pointer. If CDN upload partially fails, retain previous pointer. Cache bust by digest, never by mutating files at a published URL.

## Domain contracts that cannot be bypassed

- Every publishable asset has a semantic ID distinct from filename, format and CDN URL.
- Art must be original or appropriately licensed; genre screenshots are reference only, not redistributable sources.
- Collider and 60 Hz simulation inputs are owned by Batch 02; sprite shapes never silently change game physics.
- Art is a lower-trust presentation layer; all reward, inventory, shop and map permissions come from their domain owners.
- Eight alpha drink IDs are stable and tier 8 remains terminal; color, garnish or cosmetic edition do not change merging.

## Proposed typed interface and persistence vocabulary

Candidate fields: `assetId`, `kind`, `displayName`, `status`, `sourcePolicy`, `licenseState`, `renderProfile`, `fallbackAssetId`. Create implementation types in `packages/contracts` and pure helpers in `packages/domain`; do not import production secrets, database clients or browser globals into the simulation rules.

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
