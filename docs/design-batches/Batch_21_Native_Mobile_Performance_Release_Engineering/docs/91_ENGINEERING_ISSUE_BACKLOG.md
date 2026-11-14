# 91 — Atomic Engineering Issue Backlog and Ownership

Engineers create independent branches, open PRs against integration branch, and **do not merge their own PRs**. The coordinator reviews compatibility; `main` promotion requires owner approval. Manual UI, audio and gameplay feel tests are directed to the user.

## Workstreams

- **A — Contracts and fixtures:** freeze source IDs, JSON schema, typed event contracts and rules.
- **B — Pure core services:** implement business constraints and deterministic reference behaviors, no UI grants.
- **C — Integration adapters:** connect game/React/backend/native service through domain-owning APIs.
- **D — Tests, authoring, rollout:** automated proof, accessibility, owner acceptance guide and rollback.

## Issue map (35 atomic tickets)

| Issue ID | Stream | Deliverable | Acceptance proof |
|---|---|---|---|
| MX21-001 | A/Contracts | Native expansion philosophy and release prerequisites | Contract + negative fixture + accessible fallback; **Browser and native with same input trace produce identical physics outcome under pinned engine profile.** |
| MX21-002 | A/Contracts | Capacitor architecture and shared code | Contract + negative fixture + accessible fallback; **Browser build typechecks without iOS/Android SDK dependencies.** |
| MX21-003 | A/Contracts | Capacitor versioning, Node and build matrix | Contract + negative fixture + accessible fallback; **`npx cap sync` from clean checkout produces audited reproducible platform changes.** |
| MX21-004 | A/Contracts | iOS project setup, signing and entitlements | Contract + negative fixture + accessible fallback; **Clean archive validated with current App Store Connect tooling before submission.** |
| MX21-005 | A/Contracts | Android project setup, AAB and target SDK | Contract + negative fixture + accessible fallback; **Release AAB metadata inspected, app signed with approved Play signing flow.** |
| MX21-006 | B/Core | Platform store accounts, identity and metadata | Contract + negative fixture + accessible fallback; **Review build can reach playable onboarding with demo content and no missing server credentials.** |
| MX21-007 | B/Core | WebView rendering and input event compatibility | Contract + negative fixture + accessible fallback; **Same tutorial runs on iPhone, mid-range Android and desktop with no double-shot.** |
| MX21-008 | B/Core | Display DPI, safe areas and orientation | Contract + negative fixture + accessible fallback; **Rotate mid-pause and resume board at same coordinates and state.** |
| MX21-009 | B/Core | Touch ergonomics, gesture conflict and haptics | Contract + negative fixture + accessible fallback; **One finger aim/release on small phone produces exactly one shot.** |
| MX21-010 | B/Core | Audio focus, interruptions and mobile media | Contract + negative fixture + accessible fallback; **Incoming call suspends audio and fixed-step gameplay without award duplication.** |
| MX21-011 | B/Core | Lifecycle, suspension and checkpoint safety | Contract + negative fixture + accessible fallback; **Kill app mid-claim, relaunch and fetch canonical result without duplicate balance.** |
| MX21-012 | B/Core | Offline support, manifests and cache eviction | Contract + negative fixture + accessible fallback; **Cold-start offline opens supported training mission and labels its rewards preview-only.** |
| MX21-013 | C/Integrations | Native authentication and secure storage | Contract + negative fixture + accessible fallback; **App reinstall/logout invalidates inappropriate local auth while trusted account state remains backend-owned.** |
| MX21-014 | C/Integrations | Deep links, invitations and routing | Contract + negative fixture + accessible fallback; **Forged invite URL cannot join crew or unlock paid inventory.** |
| MX21-015 | C/Integrations | Push notifications, consent and OS permissions | Contract + negative fixture + accessible fallback; **Unsubscribing on two devices revokes relevant subscription on both.** |
| MX21-016 | C/Integrations | App review, privacy labels, data safety and SDK inventory | Contract + negative fixture + accessible fallback; **Runtime SDK network capture matches submitted disclosure inventory.** |
| MX21-017 | C/Integrations | In-app digital goods and native payment policy | Contract + negative fixture + accessible fallback; **Restore Purchases reconciles item once after device transfer.** |
| MX21-018 | C/Integrations | Performance class matrix, FPS and memory budgets | Contract + negative fixture + accessible fallback; **30fps render device executes deterministic 60Hz fixed-step without input loss under measured caps.** |
| MX21-019 | C/Integrations | Asset streaming, texture memory and decode budgets | Contract + negative fixture + accessible fallback; **20 scene transitions do not show monotonically increasing resident texture memory.** |
| MX21-020 | C/Integrations | Network resilience, latency and replay submission | Contract + negative fixture + accessible fallback; **Flaky network after committed purchase returns original receipt and inventory once.** |
| MX21-021 | C/Integrations | Background workers, power, heat and battery | Contract + negative fixture + accessible fallback; **30-minute device soak remains stable without dangerous heating or uncontrolled battery drain.** |
| MX21-022 | D/QA-Publish | Memory leaks, crashes and startup health | Contract + negative fixture + accessible fallback; **Repeated play/retry does not accumulate input listeners or scene references.** |
| MX21-023 | D/QA-Publish | Accessibility across web and native | Contract + negative fixture + accessible fallback; **Screen-reader user can launch, pause, identify two orders and retry.** |
| MX21-024 | D/QA-Publish | Localization and regional store requirements | Contract + negative fixture + accessible fallback; **Simulated long locale string doesn't clip purchase confirmation or mission goals.** |
| MX21-025 | D/QA-Publish | Native analytics, crash reporting and consent | Contract + negative fixture + accessible fallback; **SDK no-network test leaves gameplay functional.** |
| MX21-026 | D/QA-Publish | CI builds, signing and branch governance | Contract + negative fixture + accessible fallback; **Release workflow requires owner approval and verified package SHA.** |
| MX21-027 | D/QA-Publish | Test matrix, simulator and physical device testing | Contract + negative fixture + accessible fallback; **Device owner confirms manual UI/gameplay acceptance after engineer test logs.** |
| MX21-028 | D/QA-Publish | Beta distribution, TestFlight and Play tracks | Contract + negative fixture + accessible fallback; **Migrating beta to store release preserves valid account profile and avoids preview coin conversion.** |
| MX21-029 | D/QA-Publish | Version policy and compatibility matrix | Contract + negative fixture + accessible fallback; **App version N-1 gets compatible read response or explicit update-required state.** |
| MX21-030 | D/QA-Publish | Store approval, launch and rollback playbook | Contract + negative fixture + accessible fallback; **Simulated rejected app review has documented response and safe web-only fallback.** |
| MX21-031 | D/QA-Publish | CDN, edge caching and global performance | Contract + negative fixture + accessible fallback; **Offline/online flip and edge invalidation load only published assets.** |
| MX21-032 | D/QA-Publish | Autoscaling, load testing and cost controls | Contract + negative fixture + accessible fallback; **High-load test maintains queue bounds and correct wallet receipts.** |
| MX21-033 | D/QA-Publish | Security review for native bridge and dependencies | Contract + negative fixture + accessible fallback; **Malicious deep link or file payload cannot invoke authenticated purchase command.** |
| MX21-034 | D/QA-Publish | Engineering rollout, priorities and issue decomposition | Contract + negative fixture + accessible fallback; **First native smoke build demonstrates full tutorial with same score, input and readable layout.** |
| MX21-035 | D/QA-Publish | Cross-platform ADRs, risks, documentation and DoD | Contract + negative fixture + accessible fallback; **Every target release has device matrix evidence, privacy review and rollback path.** |

## Parallelization policy

- Stream A first freezes IDs and event schema. Pure calculations in stream B can begin simultaneously against fixtures. UI/Content Studio stream C can mock stable read models but cannot invent grant or rank writes.
- Stream D authors negative tests and performance/a11y harness concurrently; avoid waiting until all UI is complete.
- Every PR describes precise files affected, tests run, fixture output, dependent batch contracts, rollout gate and fallback. A migration requires isolated staging verification and an explicit read/write compatibility window.
- If a feature requires another service that is not implemented, merge only its gated read-only contract and document the blocked dependency; never hide placeholder functionality behind a working button.
