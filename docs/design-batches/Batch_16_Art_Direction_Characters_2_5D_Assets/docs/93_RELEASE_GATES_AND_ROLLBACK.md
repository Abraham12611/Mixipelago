# 93 — Release Slices, Feature Gates and Rollback

**Target:** v0.1.x foundational, extended with island/shop releases. These are candidates, not production promises.

## Proposed slices

1. **v0.1.0/0.1.1: eight drink sprites, table and fallback icons** — Acceptance requires owner-directed manual test plus automated evidence.
2. **v0.2+: island atlas and shop decor** — Acceptance requires owner-directed manual test plus automated evidence.
3. **Later: 3D variants and advanced weather/particle suites** — Acceptance requires owner-directed manual test plus automated evidence.

## Gate design

- Primary advanced feature gate: `ART_PIPELINE_ENABLED` (default **OFF**).
- Separate independent gates for any subfeature that can issue money, change competitive eligibility, expose personal/social data or invoke platform billing.
- Turn on in dev/staging first. Admin reviewer signs immutable catalog revision and checks security/permissions. Canary cohorts are not an alternative to first testing real invariants.
- Pin content/physics/rules version at session start and persist grant policy version in authoritative receipt; rollback must not rewrite existing ownership.

## Dependency order and release blocking tests

1. **Foundation:** Asset ID and provenance registry.
2. **Integration:** Manifest validator, Blender render preset, atlas export checks and lazy Phaser loader.
3. **Fallback:** low memory texture atlas fallback, missing-art labeled cards.
4. **Release scope:** v0.1 eight drink sprites and one table first; islands/shop/new recipes gated.

Block release for missing rights, a failing proof/ledger/RLS test, misleading reward status, unreviewed store/privacy disclosure, inability to restore paid entitlement, a significant visual obstruction, crashes in tutorial or unverifiable score in normalized ranking.

## Rollback runbook

1. Stop new privileged writes or feature enrollments via server gate; preserve active verified receipts and long-running pinned sessions.
2. Redirect new content sessions to previous immutable catalog pointer if safe; never alter historical financial ledger data.
3. Deploy forward fix/reconciliation for failed outbox projections; alert owner and preserve evidence.
4. Update status/support text to communicate unavailable features and expected retry semantics without promising retroactive unverified rewards.
5. Reopen only after staging negative tests, telemetry and owner approval pass.
