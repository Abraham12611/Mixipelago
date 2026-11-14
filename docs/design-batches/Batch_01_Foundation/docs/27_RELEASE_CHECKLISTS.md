# 27 — Release Go/No-Go Checklists and Definition of Done

## Issue-level Definition of Done

- [ ] Meets acceptance in issue and relevant spec.
- [ ] Shared contracts are validated and versioned; no cross-module breaking change without review.
- [ ] New/modified paths have tests and fixtures.
- [ ] Typecheck, lint, build, unit/physics tests pass.
- [ ] No leaked keys, copied source-game artwork or unlicensed audio.
- [ ] Mobile/desktop impact described; device/performance risks noted.
- [ ] Manual UI test steps for product owner attached.
- [ ] PR into `develop`; coordinator review; engineer did not merge.

## v0.1.0 release checklist

### Core play
- [ ] `Play` opens game on production-like URL.
- [ ] Zero-gravity, fixed-step simulation stable.
- [ ] Angle-dependent collisions and low-friction glide are credible.
- [ ] Matching pair creates exactly one next tier; different tiers do not merge.
- [ ] Chain merge, top-tier and danger boundary handled safely.
- [ ] Touch and mouse aim launch reliably.
- [ ] Two order cards, score, preview coins and goals behave as specified.
- [ ] Win/fail/retry and pause/resume operate without state corruption.

### UX/audio
- [ ] Mobile portrait and desktop landscape are usable.
- [ ] No clipped critical buttons or severe text overflow at target viewports.
- [ ] SFX/mute work after interaction, no crashing on mobile audio permission.
- [ ] Settings and tutorial persistence work.
- [ ] Screen loading/error fallbacks present; alpha limitations clear.
- [ ] Original, reviewed visual and sound assets only.

### Engineering
- [ ] Content schemas and local save migrations pass tests.
- [ ] No duplicated rewards or impossible negative preview balance.
- [ ] Build deploys reproducibly; production env is isolated.
- [ ] Source maps/error reporting and performance baselines gathered.
- [ ] No admin/test physics lab accidentally exposed in production.
- [ ] Owner manual UI validation completed or documented risk explicitly accepted.
- [ ] `main` merge authorized by owner; release tag and notes created.

## v0.1.1 checklist

- [ ] Highest-impact touch/control issues resolved.
- [ ] 3–10 curated missions are solvable and versioned.
- [ ] Asset bundle and memory improvements measured on target devices.
- [ ] Additional tutorial/keyboard/reduced-motion improvements shipped.
- [ ] Local save compatibility from v0.1.0 confirmed.
- [ ] Clear change log, updated acceptance tests and rollback plan.

## Trusted economy release gate (future)

- [ ] Auth and server wallet implement proper ownership.
- [ ] Balance+ledger writes atomic with duplicate-request protection.
- [ ] Content/reward validation and exploit tests pass.
- [ ] RLS grants/policies audited; no direct client wallet mutation.
- [ ] Restoring a failed purchase or partial network request does not duplicate debit.
- [ ] Backups and reconciliation available.

## Leaderboard release gate (future)

- [ ] Score verification rejects impossible/tampered runs.
- [ ] Ranking criteria/tie-break/public privacy documented.
- [ ] Seasonal rewards distributed exactly once.
- [ ] Abuse moderation and opt-in region policies operational.
- [ ] Ranked perk normalization enforced.

## Owner validation record template

```
Release candidate:
Staging URL:
Device/browser:
Steps executed:
Visual/physics/audio feedback:
Blocking issues:
Approval to merge main? yes/no:
Known risks accepted:
```

If release gate fails, ship smaller scope (with accurate UI labels) instead of pretending feature works.
