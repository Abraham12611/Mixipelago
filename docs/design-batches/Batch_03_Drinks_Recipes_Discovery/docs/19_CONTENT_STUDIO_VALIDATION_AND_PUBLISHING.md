# 19 — Drink Catalog Content Studio, Authoring Workflow and Publication Safety

## Purpose

Avoid relying on engineers editing dozens of scattered objects when we eventually introduce hundreds of drinks. Build a structured authoring and review pipeline, but start alpha with JSON committed to Git and validated by CI.

## Alpha authoring workflow

Designer proposes change -> edits `examples/catalog/core-drinks-alpha.json` equivalent in source repo -> schema lint -> logic tests (contiguous ladder, unique IDs, valid score) -> sprite link verification -> golden mission replay tests -> PR review and owner approval -> increment catalog version/hash -> deploy -> pin new sessions to new catalog.

## Future Content Studio screens

- Catalog overview with search/filter by family, tier, publish status and asset completeness.
- Drink editor: stable ID, localized name, silhouette/gallery, tier, family, score, art/audio IDs and collection tags.
- Recipe graph visualizer: inputs/outputs, context gating, collision ambiguity warnings, unreachable-node report.
- Spawn/order preview: which missions request a drink, whether it is obtainable, best/worst-case required source equivalents.
- Asset validation: image transparency, dimensions, anchor, texture pack, fallback, rights/provenance.
- Preview sandbox: physics session started with unpublished content in test environment, excluded from rankings and trusted rewards.
- Publish history: immutable manifest hashes, diff, approvers, rollbacks.

## Publication lifecycle

`draft` -> `ready_for_review` -> `approved` -> `published` -> `retired`. Published manifests immutable. Editing published content creates a new version. Rollback republishes an older compatible manifest or disables new-session selection; it does not rewrite past session hashes.

## Automated publication gates

Unique IDs; localized name key exists; numerical values finite and within approved ranges; no accidental graph cycle; no ambiguous recipe match; no active mission dangling target; all assets available and licensed; all sources valid; no spoiler leakage in public manifests beyond permitted visibility; all needed versions retained for running sessions; simulation fixture compatibility preserved.

## Multiple editors and conflict safety

If two agents edit the same drink, optimistic version checks reject stale save. Avoid silent last-write-wins on published data. Keep author, reviewer and publisher roles separate; changes to coin rewards and availability can require additional approval. Owner controls manual art/game feel approvals.

## Security considerations

Studio is admin-only, CSRF protected, validates asset uploads and input JSON, logs changes, checks published permissions on server, and never accepts executable script from content fields. Content manifests must be treated as untrusted configuration at runtime despite authoring approval. Do not render raw markup or arbitrary code from ingredient descriptions.

## Operational cadence

Before each content release: generate preview build, run automated validator, simulate representative missions, compare score/reward delta, review localization and accessibility, obtain approval, publish feature flag to small audience, monitor error and completion rate, then expand. Rollback runbook must include asset CDN cache behavior and old manifest retention.
