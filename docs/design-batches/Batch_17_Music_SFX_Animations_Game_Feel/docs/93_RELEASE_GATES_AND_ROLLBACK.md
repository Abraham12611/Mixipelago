# 93 — Release Slices, Feature Gates and Rollback

**Target:** v0.1.x foundational audio, dynamic mix after gameplay proof. These are candidates, not production promises.

## Proposed slices

1. **v0.1.x: core launch/clink/merge/serve/win/lose cues and controls** — Acceptance requires owner-directed manual test plus automated evidence.
2. **v0.2+: island music and dynamic layers** — Acceptance requires owner-directed manual test plus automated evidence.
3. **Later: VO, extended ambience and haptics** — Acceptance requires owner-directed manual test plus automated evidence.

## Gate design

- Primary advanced feature gate: `AUDIO_PRESENTATION_ENABLED` (default **OFF**).
- Separate independent gates for any subfeature that can issue money, change competitive eligibility, expose personal/social data or invoke platform billing.
- Turn on in dev/staging first. Admin reviewer signs immutable catalog revision and checks security/permissions. Canary cohorts are not an alternative to first testing real invariants.
- Pin content/physics/rules version at session start and persist grant policy version in authoritative receipt; rollback must not rewrite existing ownership.

## Dependency order and release blocking tests

1. **Foundation:** AudioCue catalog and mixer.
2. **Integration:** Event-to-cue router, one AudioContext lifecycle manager and device interruption handlers.
3. **Fallback:** silence mode and visual-only cues.
4. **Release scope:** core audio in v0.1, dynamic stems/voice after owner listening review.

Block release for missing rights, a failing proof/ledger/RLS test, misleading reward status, unreviewed store/privacy disclosure, inability to restore paid entitlement, a significant visual obstruction, crashes in tutorial or unverifiable score in normalized ranking.

## Rollback runbook

1. Stop new privileged writes or feature enrollments via server gate; preserve active verified receipts and long-running pinned sessions.
2. Redirect new content sessions to previous immutable catalog pointer if safe; never alter historical financial ledger data.
3. Deploy forward fix/reconciliation for failed outbox projections; alert owner and preserve evidence.
4. Update status/support text to communicate unavailable features and expected retry semantics without promising retroactive unverified rewards.
5. Reopen only after staging negative tests, telemetry and owner approval pass.
