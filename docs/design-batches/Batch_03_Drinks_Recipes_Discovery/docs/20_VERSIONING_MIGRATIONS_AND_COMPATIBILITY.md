# 20 — Catalog Versioning, Session Pinning, Migration and Backward Compatibility

## Four different version axes

- **App release version:** `v0.1.0`, `v0.1.1`, `v0.2.0`; human-facing build milestone.
- **Catalog version/hash:** identities, names, scores, image mappings and evolution chain.
- **Rules/physics version:** gameplay resolver, contact arbitration, scoring and movement settings.
- **Save schema version:** local persistence and later account records.

They serve different purposes and must not be collapsed into one `version` field. A menu hotfix doesn't necessarily change collision rules. An asset art correction doesn't automatically invalidate old score proofs.

## Immutable active session

On session start, resolve the mission ID, mission version, catalog hash, recipe manifest hash (when enabled), physics preset hash, rules version and PRNG algorithm version. Persist those in the session envelope and replay. **A running session never silently switches to newly published drink scores or recipe rules.** On navigation/next mission, a new session can adopt latest content after compatibility validation.

## What changes require what bump?

| Change | Required treatment |
|---|---|
| Drink display name typo | New localization/asset manifest revision; stable drink ID |
| Sprite upgrade only | Asset hash/version changes; keep gameplay hash same if pose/footprint unchanged |
| Swap two tier positions | New catalog version and rules/session compatibility review |
| Change output score | New catalog/rules version and ranking bracket separation |
| Add an optional collection skin | New collection/asset manifest; no alpha gameplay change |
| Add branching recipe | Major recipe rules feature gate and new replay/eligibility contract |
| Change serving priority | Rules version bump and owner approval; replay compatibility |
| Change local save structure | Explicit schema migration with recovery/backup |

## Local alpha migration

Batch 1 key `mixipelago:save:v1` remains canonical. On loading, validate JSON and known mission IDs; quarantine malformed data into an optional recoverable backup. A later `v2` migrator should map old highest-tier statistics only as *local preview*, never into authenticated trusted unlocks without server verification. Preserve best scores if mission identity and scoring rules still match; otherwise label historic/legacy.

## Retired content

Do not delete an old drink definition if a verified replay references it. Store archived content manifests (in R2/CDN or source archive with audit) under hash, and cache the manifest needed to replay ongoing seasons. If the old client is incompatible with current backend, provide an explicit restart/save compatibility notice rather than silently translating tier outputs.

## Multi-device reconciliation

Authenticated sessions should use server-authoritative progression; local preview state can be read as tutorial completion hints after an explicit migration agreement. Never accept client-submitted `previewCoins` as trusted wallet balance. Optimistic UI labels transactions as pending until server confirms.

## Rollback

A broken catalog release can be disabled for new sessions and replaced by known-good manifest. Keep active sessions pinned if safe; offer explicit abandon/retry path if truly incompatible. Audit any rewards from affected versions and issue compensating ledger entries if required rather than manually overwriting balances.

## Deterministic replay boundaries

Replay must include stable inputs, seeds, serialized object order and hashes, fixed step configuration and appropriate WASM engine version. Cross-runtime determinism can still be affected by surrounding app event ordering and content; re-run golden fixtures on supported browsers/builds. Keep score verifiers corresponding to prior ranked season rules.
