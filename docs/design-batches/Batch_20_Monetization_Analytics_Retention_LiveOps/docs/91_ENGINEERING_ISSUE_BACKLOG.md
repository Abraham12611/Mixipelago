# 91 — Atomic Engineering Issue Backlog and Ownership

Engineers create independent branches, open PRs against integration branch, and **do not merge their own PRs**. The coordinator reviews compatibility; `main` promotion requires owner approval. Manual UI, audio and gameplay feel tests are directed to the user.

## Workstreams

- **A — Contracts and fixtures:** freeze source IDs, JSON schema, typed event contracts and rules.
- **B — Pure core services:** implement business constraints and deterministic reference behaviors, no UI grants.
- **C — Integration adapters:** connect game/React/backend/native service through domain-owning APIs.
- **D — Tests, authoring, rollout:** automated proof, accessibility, owner acceptance guide and rollback.

## Issue map (34 atomic tickets)

| Issue ID | Stream | Deliverable | Acceptance proof |
|---|---|---|---|
| MX20-001 | A/Contracts | Business model, ethics and player trust | Contract + negative fixture + accessible fallback; **Free player can complete published mainline without ads or purchases.** |
| MX20-002 | A/Contracts | Monetization option portfolio and phased gates | Contract + negative fixture + accessible fallback; **Disabling checkout does not disable play, already-owned cosmetics or account access.** |
| MX20-003 | A/Contracts | SKU catalog, price display and regional settings | Contract + negative fixture + accessible fallback; **Stale catalog requests quote refresh before buy, avoiding silent higher charge.** |
| MX20-004 | A/Contracts | Cosmetic products and zero-power differentiation | Contract + negative fixture + accessible fallback; **Equip paid board skin and replay a golden physics trace with identical score hash.** |
| MX20-005 | A/Contracts | Optional season pass and premium track | Contract + negative fixture + accessible fallback; **Buy after earning 10 levels; eligible retroactive grants settle once and are visible.** |
| MX20-006 | B/Core | Optional rewarded ads, frequency and consent | Contract + negative fixture + accessible fallback; **Closing/skipping ad returns player to same game state with no penalty or phantom reward.** |
| MX20-007 | B/Core | No-pay-to-win competitive normalization | Contract + negative fixture + accessible fallback; **Paid and unpaid players with same input trace obtain same score/rank.** |
| MX20-008 | B/Core | Payment provider adapters and store compliance | Contract + negative fixture + accessible fallback; **Platform adapter rejects unauthorized billing provider and duplicate transaction ID.** |
| MX20-009 | B/Core | Purchase lifecycle, receipt verification and webhooks | Contract + negative fixture + accessible fallback; **Crash after payment before grant can replay verify and recover item once.** |
| MX20-010 | B/Core | Refunds, chargebacks, support and access policy | Contract + negative fixture + accessible fallback; **Restore Purchases rehydrates valid nonconsumable entitlements across devices.** |
| MX20-011 | B/Core | Virtual coin design and legal distinctions | Contract + negative fixture + accessible fallback; **UI copy never promises real monetary value for virtual rewards.** |
| MX20-012 | B/Core | Economy price balancing and affordability | Contract + negative fixture + accessible fallback; **Zero-purchase cohort can reach first useful upgrade by reasonable mission 3–5 target.** |
| MX20-013 | C/Integrations | Premium/nonpremium entitlement separation | Contract + negative fixture + accessible fallback; **Account merge reconciles SKU receipts by provider identity and avoids duplicates.** |
| MX20-014 | C/Integrations | Randomized rewards, odds and purchase restrictions | Contract + negative fixture + accessible fallback; **Flag sweep confirms no paid-random endpoint accessible without explicit approvals.** |
| MX20-015 | C/Integrations | Children, age ratings, ads and parental considerations | Contract + negative fixture + accessible fallback; **Restricted age profile cannot see unsupported commerce offers.** |
| MX20-016 | C/Integrations | Pricing localization and transparent currency | Contract + negative fixture + accessible fallback; **Locale change doesn't alter trusted receipt values or product ownership.** |
| MX20-017 | C/Integrations | Player funnels and north-star metrics | Contract + negative fixture + accessible fallback; **Dashboards show metric definitions and denominator rather than ambiguous rates.** |
| MX20-018 | C/Integrations | Gameplay telemetry taxonomy and contracts | Contract + negative fixture + accessible fallback; **Event validator rejects missing semantic IDs and duplicate schema fields.** |
| MX20-019 | C/Integrations | Monetization analytics and revenue reconciliation | Contract + negative fixture + accessible fallback; **Double webhook does not double-count revenue in finance dashboard.** |
| MX20-020 | C/Integrations | Retention and cohort analytics | Contract + negative fixture + accessible fallback; **Repeat install vs returning account receives consistently defined retention classification.** |
| MX20-021 | C/Integrations | A/B experimentation and ethics | Contract + negative fixture + accessible fallback; **Experiment with negative guardrail trips automatically disables variant.** |
| MX20-022 | D/QA-Publish | Feature flag rollout and live configuration | Contract + negative fixture + accessible fallback; **Emergency disable of monetization immediately prevents new purchases while honoring existing receipts.** |
| MX20-023 | D/QA-Publish | Live operations calendar and event handoff | Contract + negative fixture + accessible fallback; **Event ends during an eligible pinned session; signed result follows policy.** |
| MX20-024 | D/QA-Publish | Notification and re-engagement policy | Contract + negative fixture + accessible fallback; **Muted player receives no campaign push after disabling preferences.** |
| MX20-025 | D/QA-Publish | Customer support, trust and complaints | Contract + negative fixture + accessible fallback; **Missing cosmetic after purchase fixed by reprocessing original receipt without charging again.** |
| MX20-026 | D/QA-Publish | Privacy, consent and SDK data inventory | Contract + negative fixture + accessible fallback; **SDK data access audit finds no undisclosed tracking events.** |
| MX20-027 | D/QA-Publish | Experimentation measurement and attribution limits | Contract + negative fixture + accessible fallback; **Dashboard differentiates measured purchase, attributed estimate and hypothetical forecast.** |
| MX20-028 | D/QA-Publish | Performance and SDK impact budgets | Contract + negative fixture + accessible fallback; **3G throttling still loads game while analytics endpoint times out.** |
| MX20-029 | D/QA-Publish | Analytics warehouse and data quality | Contract + negative fixture + accessible fallback; **Replay same event batch yields stable aggregates and no duplicate sessions.** |
| MX20-030 | D/QA-Publish | Dashboards, anomalies and automated alerting | Contract + negative fixture + accessible fallback; **Simulated 10x refund spike triggers alert and commerce kill switch review.** |
| MX20-031 | D/QA-Publish | Economy simulation and pricing review board | Contract + negative fixture + accessible fallback; **Economy test verifies affordability for a player who never watches ads.** |
| MX20-032 | D/QA-Publish | Content monetization Studio and permissions | Contract + negative fixture + accessible fallback; **Draft bundle never appears in public storefront until reviewed and approved.** |
| MX20-033 | D/QA-Publish | Release plan, success gates and rollback | Contract + negative fixture + accessible fallback; **Full payment outage leaves game functional and existing inventory accessible.** |
| MX20-034 | D/QA-Publish | Engineering tasks, risk register and glossary | Contract + negative fixture + accessible fallback; **Release checklist maps each product claim to real working integration and test evidence.** |

## Parallelization policy

- Stream A first freezes IDs and event schema. Pure calculations in stream B can begin simultaneously against fixtures. UI/Content Studio stream C can mock stable read models but cannot invent grant or rank writes.
- Stream D authors negative tests and performance/a11y harness concurrently; avoid waiting until all UI is complete.
- Every PR describes precise files affected, tests run, fixture output, dependent batch contracts, rollout gate and fallback. A migration requires isolated staging verification and an explicit read/write compatibility window.
- If a feature requires another service that is not implemented, merge only its gated read-only contract and document the blocked dependency; never hide placeholder functionality behind a working button.
