# 92 — QA, Golden Fixtures and Acceptance Matrix

**No real device, physics playtest, API or production billing verification is claimed.** These tests are engineering acceptance specifications.

## Test levels

- **Static:** schema validation; unique IDs, safe feature flags, source rights, version pins and supported references.
- **Pure rule:** test vectors under `examples/tests/pure-rule-vectors.json`; run `python tools/validate_batch20.py`.
- **Integration:** actual game engine/API/DB or OS capability as needed; do not assume passing fixture means implemented system is safe.
- **Security:** actor/resource matrix, idempotent retry, stale version, race and revoked permissions.
- **Manual:** user-directed gameplay/art/audio/native feel acceptance; engineers report evidence rather than marking it approved themselves.

| ID | Feature scope | Named failure/golden case | Evidence |
|---|---|---|---|
| QA-20-01 | Business model, ethics and player trust | Free player can complete published mainline without ads or purchases. | Automated fixture + owner-directed manual UI when visual |
| QA-20-02 | Monetization option portfolio and phased gates | Disabling checkout does not disable play, already-owned cosmetics or account access. | Automated fixture + owner-directed manual UI when visual |
| QA-20-03 | SKU catalog, price display and regional settings | Stale catalog requests quote refresh before buy, avoiding silent higher charge. | Automated fixture + owner-directed manual UI when visual |
| QA-20-04 | Cosmetic products and zero-power differentiation | Equip paid board skin and replay a golden physics trace with identical score hash. | Automated fixture + owner-directed manual UI when visual |
| QA-20-05 | Optional season pass and premium track | Buy after earning 10 levels; eligible retroactive grants settle once and are visible. | Automated fixture + owner-directed manual UI when visual |
| QA-20-06 | Optional rewarded ads, frequency and consent | Closing/skipping ad returns player to same game state with no penalty or phantom reward. | Automated fixture + owner-directed manual UI when visual |
| QA-20-07 | No-pay-to-win competitive normalization | Paid and unpaid players with same input trace obtain same score/rank. | Automated fixture + owner-directed manual UI when visual |
| QA-20-08 | Payment provider adapters and store compliance | Platform adapter rejects unauthorized billing provider and duplicate transaction ID. | Automated fixture + owner-directed manual UI when visual |
| QA-20-09 | Purchase lifecycle, receipt verification and webhooks | Crash after payment before grant can replay verify and recover item once. | Automated fixture + owner-directed manual UI when visual |
| QA-20-10 | Refunds, chargebacks, support and access policy | Restore Purchases rehydrates valid nonconsumable entitlements across devices. | Automated fixture + owner-directed manual UI when visual |
| QA-20-11 | Virtual coin design and legal distinctions | UI copy never promises real monetary value for virtual rewards. | Automated fixture + owner-directed manual UI when visual |
| QA-20-12 | Economy price balancing and affordability | Zero-purchase cohort can reach first useful upgrade by reasonable mission 3–5 target. | Automated fixture + owner-directed manual UI when visual |
| QA-20-13 | Premium/nonpremium entitlement separation | Account merge reconciles SKU receipts by provider identity and avoids duplicates. | Automated fixture + owner-directed manual UI when visual |
| QA-20-14 | Randomized rewards, odds and purchase restrictions | Flag sweep confirms no paid-random endpoint accessible without explicit approvals. | Automated fixture + owner-directed manual UI when visual |
| QA-20-15 | Children, age ratings, ads and parental considerations | Restricted age profile cannot see unsupported commerce offers. | Automated fixture + owner-directed manual UI when visual |
| QA-20-16 | Pricing localization and transparent currency | Locale change doesn't alter trusted receipt values or product ownership. | Automated fixture + owner-directed manual UI when visual |
| QA-20-17 | Player funnels and north-star metrics | Dashboards show metric definitions and denominator rather than ambiguous rates. | Automated fixture + owner-directed manual UI when visual |
| QA-20-18 | Gameplay telemetry taxonomy and contracts | Event validator rejects missing semantic IDs and duplicate schema fields. | Automated fixture + owner-directed manual UI when visual |
| QA-20-19 | Monetization analytics and revenue reconciliation | Double webhook does not double-count revenue in finance dashboard. | Automated fixture + owner-directed manual UI when visual |
| QA-20-20 | Retention and cohort analytics | Repeat install vs returning account receives consistently defined retention classification. | Automated fixture + owner-directed manual UI when visual |
| QA-20-21 | A/B experimentation and ethics | Experiment with negative guardrail trips automatically disables variant. | Automated fixture + owner-directed manual UI when visual |
| QA-20-22 | Feature flag rollout and live configuration | Emergency disable of monetization immediately prevents new purchases while honoring existing receipts. | Automated fixture + owner-directed manual UI when visual |
| QA-20-23 | Live operations calendar and event handoff | Event ends during an eligible pinned session; signed result follows policy. | Automated fixture + owner-directed manual UI when visual |
| QA-20-24 | Notification and re-engagement policy | Muted player receives no campaign push after disabling preferences. | Automated fixture + owner-directed manual UI when visual |
| QA-20-25 | Customer support, trust and complaints | Missing cosmetic after purchase fixed by reprocessing original receipt without charging again. | Automated fixture + owner-directed manual UI when visual |
| QA-20-26 | Privacy, consent and SDK data inventory | SDK data access audit finds no undisclosed tracking events. | Automated fixture + owner-directed manual UI when visual |
| QA-20-27 | Experimentation measurement and attribution limits | Dashboard differentiates measured purchase, attributed estimate and hypothetical forecast. | Automated fixture + owner-directed manual UI when visual |
| QA-20-28 | Performance and SDK impact budgets | 3G throttling still loads game while analytics endpoint times out. | Automated fixture + owner-directed manual UI when visual |
| QA-20-29 | Analytics warehouse and data quality | Replay same event batch yields stable aggregates and no duplicate sessions. | Automated fixture + owner-directed manual UI when visual |
| QA-20-30 | Dashboards, anomalies and automated alerting | Simulated 10x refund spike triggers alert and commerce kill switch review. | Automated fixture + owner-directed manual UI when visual |
| QA-20-31 | Economy simulation and pricing review board | Economy test verifies affordability for a player who never watches ads. | Automated fixture + owner-directed manual UI when visual |
| QA-20-32 | Content monetization Studio and permissions | Draft bundle never appears in public storefront until reviewed and approved. | Automated fixture + owner-directed manual UI when visual |
| QA-20-33 | Release plan, success gates and rollback | Full payment outage leaves game functional and existing inventory accessible. | Automated fixture + owner-directed manual UI when visual |
| QA-20-34 | Engineering tasks, risk register and glossary | Release checklist maps each product claim to real working integration and test evidence. | Automated fixture + owner-directed manual UI when visual |

## Required failure drills

1. Restart browser or native app between request acceptance and UI confirmation; durable state must recover from canonical receipt.
2. Retry an identical command 10 times and a changed-payload command using the same key; observe one effect and one conflict.
3. Expire or unpublish current content pointer while an old pinned run is in flight; its rules remain consistent or a clear safe rejection is delivered.
4. Switch to narrow mobile viewport, large text/reduced motion, offline and low-quality device profile; required UI text and gameplay remain usable.
5. With the relevant release gate OFF, every future route or action is explicitly unavailable and does not create a hidden write.

## What static validation does *not* prove

Schema and pure vector checks are not proof of licensed source delivery, live reward/financial correctness, deterministic cross-machine Rapier replay, actual web/native performance, store approval, privacy compliance or accessibility conformance. Track these separately on an owner-approved acceptance checklist.
