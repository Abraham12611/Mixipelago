# 15 — Mission Definition Schema, Identity, Versioning and Compatibility

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Content-first design
An authored mission is immutable by `(missionId, missionVersion, contentHash)` once published. JSON is validated structurally and semantically before import. Each run references the exact pinned manifest, physics preset, catalog and score rules; new content can be published without breaking a saved run.

## Baseline compatibility
Batch 3 uses:
```
{schemaVersion:1, missionId, islandId, missionVersion, mode:'service',
 board:{presetId,width,height,dangerLineY,maxActiveDrinks,startingDrinks},
 spawn:{seedMode,pool,firstItems},
 orders:{maxVisible,initial,replacementPoolId},
 goal:{type:'orders_served',count}, rewards:{previewCoins,stars}, visualThemeId}
```
Do NOT rewrite this baseline merely to support future modes. Define additive optional fields with `schemaVersion=2` only when mode-specific rollout begins, and add a migration from v1 to v2 for internal tooling. Never pretend a v2 runtime can read v1 fields without an adapter.

## Proposed v2 extensions
- `idempotencyKey` not embedded in mission; created per session/reward action.
- `modeRulesVersion`: semantic rules applied independent of app version.
- `objectives.primary` (typed DSL); optional `starCriteria` and `secondary`.
- `budget.shotsMax`, `clock.limitTicks` (active); `waves`, `hazards`, `allowedBoosters`.
- `presentation`: theme/camera/layout/intro rather than physical logic.
- `prerequisites`: island node IDs or unlock flags (Batch 5); not needed by simulation.
- `spawn`: weights, authored firstItems, optional finite future list; all seed-resolved.
- `orders`: authored order lines/weighted pool only after Batch 3 migration, maxVisible constraint.

## Specific field requirements
`missionId` globally stable kebab identifier; `islandId` stable; `missionVersion` semver string; `mode` stable enum; `board` width and height positive finite; all positions inside usable bounds; `dangerLineY` inside board and not through default spawn zone; shot count integer >=1 when supplied; nonempty spawn pool or sufficient authored queue. Unknown mechanics IDs rejected, not silently ignored.

## Hashing
Normalize canonical JSON using stable key sorting and numeric formatting before SHA-256; omit runtime/localized strings not part of authoritative rules only if explicitly specified. Hash catalog, physics preset and mission separately; store digest values on session creation and replay. A mission change affecting a single shot/score/order must bump version and hash.

## External content delivery
`manifest.json` lists active mission IDs/versions and URLs. Browser downloads content from CDN, validates signature/hash where available, and asks runtime feature registry whether the mode is supported. If unsupported, show a clear unavailable/update-required message, not a broken board.

## Ownership and publishing
Content editor drafts → validate schema → run static feasibility and replay smoke → internal review → owner manual test → publish immutable version → canary/audience gate → public. Keep rollback pointer for new sessions while existing pinned sessions finish safely.

## Storage model
`mission_definitions` (immutable versions), `mission_publications` (active pointers), `mission_graph_edges` (Batch 5), `mission_test_receipts`, `mission_run_receipts`. JSON plus selected indexed columns. Database migrations are backend-only after trusted sessions ship; Alpha can serve bundled JSON.

## Reference schema
See `examples/schemas/mission.schema.json`, and v1 example fixtures. The JSON Schema validates shape; `tools/validate_batch4.py` enforces cross-field invariants and catalog compatibility; gameplay feasibility is proven by golden replay, not JSON Schema alone.
