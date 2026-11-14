# Final Six Batches — System-Wide Integration Checklist

**Prepared 2026-11-14.** This is a release acceptance tool, not evidence that checks have already run.

## Alpha gameplay invariants

- [ ] 8 canonical drinks; tier 8 does not merge; new drink serves oldest eligible order before chain.
- [ ] Two scripted visible orders and two-order win condition for Coconut Cove 001.
- [ ] Fixed simulation at 60Hz irrespective of render FPS, audio or native display quality.
- [ ] No account required for first playable browser build; preview coins clearly nonspendable.

## Art and audio

- [ ] Every required sprite/cue has original source, rights/consent and manifest ID.
- [ ] 2048px atlas memory budget measured on target low-end hardware.
- [ ] Missing assets/audio do not block critical controls; visual labels replace missing drink sprites.
- [ ] With music muted, reduced motion and disabled particles, gameplay scores remain identical.

## Trusted backend and security

- [ ] Real DB roles tested: anon/authenticated cannot mutate wallets or receipts.
- [ ] Certified session proof pins mission/score/physics content hash and rejects alterations.
- [ ] Worker crash/retry yields one source reward, one ledger adjustment, one entitlement.
- [ ] Secret scanning shows no keys in bundled browser/native JS.
- [ ] RLS / IDOR / CSRF / replay negative test matrix passes.
- [ ] Incident response can disable new grants while preserving ledger history.

## Analytics and optional commerce

- [ ] Player can play full mainline without paying or watching ads.
- [ ] Store receipt verified server-side before item grant; purchase/restore/refund checked on each platform.
- [ ] Paid cosmetics have no effect on ranked results or simulation.
- [ ] Analytics SDK and privacy disclosures match observed data flows; minors/consent respected.
- [ ] Store/paywall disabled state does not prevent game launch.

## Native and release

- [ ] Current Apple/Google store upload requirements rechecked at actual submission date.
- [ ] Physical device gesture, pause/resume, call interruption, low-memory, offline and accessibility tests.
- [ ] AAB, iOS archive, signing provenance and build hashes recorded; no unapproved store publishing.
- [ ] Protected main branch and production approvals; engineers do not merge their own PRs.
- [ ] Owner directs all manual gameplay, UI, art and audio acceptance.

## Final status

**None of these checkboxes are pre-approved by documentation generation.** Engineering teams must attach test recordings/logs, artifact hashes, versions, failing-case reproductions and owner feedback before claiming release readiness.
