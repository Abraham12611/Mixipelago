# 93 — Release Slices, Feature Gates and Rollback

**Target:** trusted foundation v0.3.x+; advanced services by feature. These are candidates, not production promises.

## Proposed slices

1. **v0.1.x: local preview with contract fixtures** — Acceptance requires owner-directed manual test plus automated evidence.
2. **v0.3.0: auth, receipt verification, first trusted reward and wallet** — Acceptance requires owner-directed manual test plus automated evidence.
3. **v0.4+: XP/inventory; later rankings/social/admin** — Acceptance requires owner-directed manual test plus automated evidence.

## Gate design

- Primary advanced feature gate: `TRUSTED_BACKEND_ENABLED` (default **OFF**).
- Separate independent gates for any subfeature that can issue money, change competitive eligibility, expose personal/social data or invoke platform billing.
- Turn on in dev/staging first. Admin reviewer signs immutable catalog revision and checks security/permissions. Canary cohorts are not an alternative to first testing real invariants.
- Pin content/physics/rules version at session start and persist grant policy version in authoritative receipt; rollback must not rewrite existing ownership.

## Dependency order and release blocking tests

1. **Foundation:** Server-owned entitlement and session receipt.
2. **Integration:** Typed API, Postgres migrations, outbox consumers and read projections.
3. **Fallback:** local preview with explicit unverified labels.
4. **Release scope:** auth + one verified reward before wallets, XP, social.

Block release for missing rights, a failing proof/ledger/RLS test, misleading reward status, unreviewed store/privacy disclosure, inability to restore paid entitlement, a significant visual obstruction, crashes in tutorial or unverifiable score in normalized ranking.

## Rollback runbook

1. Stop new privileged writes or feature enrollments via server gate; preserve active verified receipts and long-running pinned sessions.
2. Redirect new content sessions to previous immutable catalog pointer if safe; never alter historical financial ledger data.
3. Deploy forward fix/reconciliation for failed outbox projections; alert owner and preserve evidence.
4. Update status/support text to communicate unavailable features and expected retry semantics without promising retroactive unverified rewards.
5. Reopen only after staging negative tests, telemetry and owner approval pass.
