# 92 — QA, Golden Fixtures and Acceptance Matrix

**No real device, physics playtest, API or production billing verification is claimed.** These tests are engineering acceptance specifications.

## Test levels

- **Static:** schema validation; unique IDs, safe feature flags, source rights, version pins and supported references.
- **Pure rule:** test vectors under `examples/tests/pure-rule-vectors.json`; run `python tools/validate_batch21.py`.
- **Integration:** actual game engine/API/DB or OS capability as needed; do not assume passing fixture means implemented system is safe.
- **Security:** actor/resource matrix, idempotent retry, stale version, race and revoked permissions.
- **Manual:** user-directed gameplay/art/audio/native feel acceptance; engineers report evidence rather than marking it approved themselves.

| ID | Feature scope | Named failure/golden case | Evidence |
|---|---|---|---|
| QA-21-01 | Native expansion philosophy and release prerequisites | Browser and native with same input trace produce identical physics outcome under pinned engine profile. | Automated fixture + owner-directed manual UI when visual |
| QA-21-02 | Capacitor architecture and shared code | Browser build typechecks without iOS/Android SDK dependencies. | Automated fixture + owner-directed manual UI when visual |
| QA-21-03 | Capacitor versioning, Node and build matrix | `npx cap sync` from clean checkout produces audited reproducible platform changes. | Automated fixture + owner-directed manual UI when visual |
| QA-21-04 | iOS project setup, signing and entitlements | Clean archive validated with current App Store Connect tooling before submission. | Automated fixture + owner-directed manual UI when visual |
| QA-21-05 | Android project setup, AAB and target SDK | Release AAB metadata inspected, app signed with approved Play signing flow. | Automated fixture + owner-directed manual UI when visual |
| QA-21-06 | Platform store accounts, identity and metadata | Review build can reach playable onboarding with demo content and no missing server credentials. | Automated fixture + owner-directed manual UI when visual |
| QA-21-07 | WebView rendering and input event compatibility | Same tutorial runs on iPhone, mid-range Android and desktop with no double-shot. | Automated fixture + owner-directed manual UI when visual |
| QA-21-08 | Display DPI, safe areas and orientation | Rotate mid-pause and resume board at same coordinates and state. | Automated fixture + owner-directed manual UI when visual |
| QA-21-09 | Touch ergonomics, gesture conflict and haptics | One finger aim/release on small phone produces exactly one shot. | Automated fixture + owner-directed manual UI when visual |
| QA-21-10 | Audio focus, interruptions and mobile media | Incoming call suspends audio and fixed-step gameplay without award duplication. | Automated fixture + owner-directed manual UI when visual |
| QA-21-11 | Lifecycle, suspension and checkpoint safety | Kill app mid-claim, relaunch and fetch canonical result without duplicate balance. | Automated fixture + owner-directed manual UI when visual |
| QA-21-12 | Offline support, manifests and cache eviction | Cold-start offline opens supported training mission and labels its rewards preview-only. | Automated fixture + owner-directed manual UI when visual |
| QA-21-13 | Native authentication and secure storage | App reinstall/logout invalidates inappropriate local auth while trusted account state remains backend-owned. | Automated fixture + owner-directed manual UI when visual |
| QA-21-14 | Deep links, invitations and routing | Forged invite URL cannot join crew or unlock paid inventory. | Automated fixture + owner-directed manual UI when visual |
| QA-21-15 | Push notifications, consent and OS permissions | Unsubscribing on two devices revokes relevant subscription on both. | Automated fixture + owner-directed manual UI when visual |
| QA-21-16 | App review, privacy labels, data safety and SDK inventory | Runtime SDK network capture matches submitted disclosure inventory. | Automated fixture + owner-directed manual UI when visual |
| QA-21-17 | In-app digital goods and native payment policy | Restore Purchases reconciles item once after device transfer. | Automated fixture + owner-directed manual UI when visual |
| QA-21-18 | Performance class matrix, FPS and memory budgets | 30fps render device executes deterministic 60Hz fixed-step without input loss under measured caps. | Automated fixture + owner-directed manual UI when visual |
| QA-21-19 | Asset streaming, texture memory and decode budgets | 20 scene transitions do not show monotonically increasing resident texture memory. | Automated fixture + owner-directed manual UI when visual |
| QA-21-20 | Network resilience, latency and replay submission | Flaky network after committed purchase returns original receipt and inventory once. | Automated fixture + owner-directed manual UI when visual |
| QA-21-21 | Background workers, power, heat and battery | 30-minute device soak remains stable without dangerous heating or uncontrolled battery drain. | Automated fixture + owner-directed manual UI when visual |
| QA-21-22 | Memory leaks, crashes and startup health | Repeated play/retry does not accumulate input listeners or scene references. | Automated fixture + owner-directed manual UI when visual |
| QA-21-23 | Accessibility across web and native | Screen-reader user can launch, pause, identify two orders and retry. | Automated fixture + owner-directed manual UI when visual |
| QA-21-24 | Localization and regional store requirements | Simulated long locale string doesn't clip purchase confirmation or mission goals. | Automated fixture + owner-directed manual UI when visual |
| QA-21-25 | Native analytics, crash reporting and consent | SDK no-network test leaves gameplay functional. | Automated fixture + owner-directed manual UI when visual |
| QA-21-26 | CI builds, signing and branch governance | Release workflow requires owner approval and verified package SHA. | Automated fixture + owner-directed manual UI when visual |
| QA-21-27 | Test matrix, simulator and physical device testing | Device owner confirms manual UI/gameplay acceptance after engineer test logs. | Automated fixture + owner-directed manual UI when visual |
| QA-21-28 | Beta distribution, TestFlight and Play tracks | Migrating beta to store release preserves valid account profile and avoids preview coin conversion. | Automated fixture + owner-directed manual UI when visual |
| QA-21-29 | Version policy and compatibility matrix | App version N-1 gets compatible read response or explicit update-required state. | Automated fixture + owner-directed manual UI when visual |
| QA-21-30 | Store approval, launch and rollback playbook | Simulated rejected app review has documented response and safe web-only fallback. | Automated fixture + owner-directed manual UI when visual |
| QA-21-31 | CDN, edge caching and global performance | Offline/online flip and edge invalidation load only published assets. | Automated fixture + owner-directed manual UI when visual |
| QA-21-32 | Autoscaling, load testing and cost controls | High-load test maintains queue bounds and correct wallet receipts. | Automated fixture + owner-directed manual UI when visual |
| QA-21-33 | Security review for native bridge and dependencies | Malicious deep link or file payload cannot invoke authenticated purchase command. | Automated fixture + owner-directed manual UI when visual |
| QA-21-34 | Engineering rollout, priorities and issue decomposition | First native smoke build demonstrates full tutorial with same score, input and readable layout. | Automated fixture + owner-directed manual UI when visual |
| QA-21-35 | Cross-platform ADRs, risks, documentation and DoD | Every target release has device matrix evidence, privacy review and rollback path. | Automated fixture + owner-directed manual UI when visual |

## Required failure drills

1. Restart browser or native app between request acceptance and UI confirmation; durable state must recover from canonical receipt.
2. Retry an identical command 10 times and a changed-payload command using the same key; observe one effect and one conflict.
3. Expire or unpublish current content pointer while an old pinned run is in flight; its rules remain consistent or a clear safe rejection is delivered.
4. Switch to narrow mobile viewport, large text/reduced motion, offline and low-quality device profile; required UI text and gameplay remain usable.
5. With the relevant release gate OFF, every future route or action is explicitly unavailable and does not create a hidden write.

## What static validation does *not* prove

Schema and pure vector checks are not proof of licensed source delivery, live reward/financial correctness, deterministic cross-machine Rapier replay, actual web/native performance, store approval, privacy compliance or accessibility conformance. Track these separately on an owner-approved acceptance checklist.
