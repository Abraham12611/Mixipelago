# Batch 21 — Native Mobile, Performance, Scaling & Release Engineering

**Status:** Detailed engineering design pack; not an implemented/deployed feature. **Prepared:** 2026-11-14.
**Owner:** Platform / Mobile / SRE. **Candidate release:** browser alpha first; Capacitor native after quality and retention gates. **Advanced gate:** `NATIVE_APP_RELEASE_ENABLED` default OFF.

## Critical earlier rules
Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## Source-of-truth responsibilities
iOS/Android packaging, device-specific behavior, CI/CD, store submission, performance optimization and version compatibility.
Batch 01 Next.js/Phaser/Rapier; Batch 15 UI; Batch 16 assets; Batch 17 audio; Batch 18 backend; Batch 19 security; Batch 20 digital goods and privacy.

## Specification chapters
- [01 — Native expansion philosophy and release prerequisites](./01_NATIVE_EXPANSION_PHILOSOPHY_AND_RELEASE_PREREQUISITES.md)
- [02 — Capacitor architecture and shared code](./02_CAPACITOR_ARCHITECTURE_AND_SHARED_CODE.md)
- [03 — Capacitor versioning, Node and build matrix](./03_CAPACITOR_VERSIONING_NODE_AND_BUILD_MATRIX.md)
- [04 — iOS project setup, signing and entitlements](./04_IOS_PROJECT_SETUP_SIGNING_AND_ENTITLEMENTS.md)
- [05 — Android project setup, AAB and target SDK](./05_ANDROID_PROJECT_SETUP_AAB_AND_TARGET_SDK.md)
- [06 — Platform store accounts, identity and metadata](./06_PLATFORM_STORE_ACCOUNTS_IDENTITY_AND_METADATA.md)
- [07 — WebView rendering and input event compatibility](./07_WEBVIEW_RENDERING_AND_INPUT_EVENT_COMPATIBILITY.md)
- [08 — Display DPI, safe areas and orientation](./08_DISPLAY_DPI_SAFE_AREAS_AND_ORIENTATION.md)
- [09 — Touch ergonomics, gesture conflict and haptics](./09_TOUCH_ERGONOMICS_GESTURE_CONFLICT_AND_HAPTICS.md)
- [10 — Audio focus, interruptions and mobile media](./10_AUDIO_FOCUS_INTERRUPTIONS_AND_MOBILE_MEDIA.md)
- [11 — Lifecycle, suspension and checkpoint safety](./11_LIFECYCLE_SUSPENSION_AND_CHECKPOINT_SAFETY.md)
- [12 — Offline support, manifests and cache eviction](./12_OFFLINE_SUPPORT_MANIFESTS_AND_CACHE_EVICTION.md)
- [13 — Native authentication and secure storage](./13_NATIVE_AUTHENTICATION_AND_SECURE_STORAGE.md)
- [14 — Deep links, invitations and routing](./14_DEEP_LINKS_INVITATIONS_AND_ROUTING.md)
- [15 — Push notifications, consent and OS permissions](./15_PUSH_NOTIFICATIONS_CONSENT_AND_OS_PERMISSIONS.md)
- [16 — App review, privacy labels, data safety and SDK inventory](./16_APP_REVIEW_PRIVACY_LABELS_DATA_SAFETY_AND_SDK_INVENTORY.md)
- [17 — In-app digital goods and native payment policy](./17_IN_APP_DIGITAL_GOODS_AND_NATIVE_PAYMENT_POLICY.md)
- [18 — Performance class matrix, FPS and memory budgets](./18_PERFORMANCE_CLASS_MATRIX_FPS_AND_MEMORY_BUDGETS.md)
- [19 — Asset streaming, texture memory and decode budgets](./19_ASSET_STREAMING_TEXTURE_MEMORY_AND_DECODE_BUDGETS.md)
- [20 — Network resilience, latency and replay submission](./20_NETWORK_RESILIENCE_LATENCY_AND_REPLAY_SUBMISSION.md)
- [21 — Background workers, power, heat and battery](./21_BACKGROUND_WORKERS_POWER_HEAT_AND_BATTERY.md)
- [22 — Memory leaks, crashes and startup health](./22_MEMORY_LEAKS_CRASHES_AND_STARTUP_HEALTH.md)
- [23 — Accessibility across web and native](./23_ACCESSIBILITY_ACROSS_WEB_AND_NATIVE.md)
- [24 — Localization and regional store requirements](./24_LOCALIZATION_AND_REGIONAL_STORE_REQUIREMENTS.md)
- [25 — Native analytics, crash reporting and consent](./25_NATIVE_ANALYTICS_CRASH_REPORTING_AND_CONSENT.md)
- [26 — CI builds, signing and branch governance](./26_CI_BUILDS_SIGNING_AND_BRANCH_GOVERNANCE.md)
- [27 — Test matrix, simulator and physical device testing](./27_TEST_MATRIX_SIMULATOR_AND_PHYSICAL_DEVICE_TESTING.md)
- [28 — Beta distribution, TestFlight and Play tracks](./28_BETA_DISTRIBUTION_TESTFLIGHT_AND_PLAY_TRACKS.md)
- [29 — Version policy and compatibility matrix](./29_VERSION_POLICY_AND_COMPATIBILITY_MATRIX.md)
- [30 — Store approval, launch and rollback playbook](./30_STORE_APPROVAL_LAUNCH_AND_ROLLBACK_PLAYBOOK.md)
- [31 — CDN, edge caching and global performance](./31_CDN_EDGE_CACHING_AND_GLOBAL_PERFORMANCE.md)
- [32 — Autoscaling, load testing and cost controls](./32_AUTOSCALING_LOAD_TESTING_AND_COST_CONTROLS.md)
- [33 — Security review for native bridge and dependencies](./33_SECURITY_REVIEW_FOR_NATIVE_BRIDGE_AND_DEPENDENCIES.md)
- [34 — Engineering rollout, priorities and issue decomposition](./34_ENGINEERING_ROLLOUT_PRIORITIES_AND_ISSUE_DECOMPOSITION.md)
- [35 — Cross-platform ADRs, risks, documentation and DoD](./35_CROSS_PLATFORM_ADRS_RISKS_DOCUMENTATION_AND_DOD.md)

## Implementation and governance
- [90 — Engineering Implementation Blueprint](./90_IMPLEMENTATION_BLUEPRINT.md)
- [91 — Atomic Engineering Issue Backlog](./91_ENGINEERING_ISSUE_BACKLOG.md)
- [92 — QA and Golden Fixtures](./92_QA_GOLDEN_FIXTURES.md)
- [93 — Release Gates and Rollback](./93_RELEASE_GATES_AND_ROLLBACK.md)
- [94 — ADRs and Traceability](./94_ADRS_AND_TRACEABILITY.md)
- [95 — Official Sources and Precedence](./95_OFFICIAL_SOURCES.md)

## Machine-readable materials
- `../examples/catalog/catalog.draft.json` — candidate domain catalog; nothing enabled or production-approved.
- `../examples/schemas/catalog.schema.json` — example JSON schema.
- `../examples/tests/pure-rule-vectors.json` — expected pure behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid catalog mutations.
- `../examples/contracts/reference.ts` — TypeScript reference functions.
- `../examples/contracts/api-examples.json` — sample event/HTTP envelopes.
- `../examples/sql/schema_draft.sql` — illustrative, not a deployable migration.
- `../tools/validate_batch21.py` — Python validator using `jsonschema` for full schema checks.

## Start implementation
1. Read the first six chapters and the implementation blueprint.
2. Pin content and rules versions, prove fixtures and agree on event boundaries.
3. Build a small feature-gated integration slice with accessible fallback.
4. Run negative authorization and replay tests, then owner-directed visual/audio/gameplay acceptance.
5. No engineer self-merges; owner approval required for main/production promotion.

**Next batch/dependency:** post-Batch 21 integration and production readiness.
