# 92 — QA, Golden Fixtures and Acceptance Matrix

**No real device, physics playtest, API or production billing verification is claimed.** These tests are engineering acceptance specifications.

## Test levels

- **Static:** schema validation; unique IDs, safe feature flags, source rights, version pins and supported references.
- **Pure rule:** test vectors under `examples/tests/pure-rule-vectors.json`; run `python tools/validate_batch19.py`.
- **Integration:** actual game engine/API/DB or OS capability as needed; do not assume passing fixture means implemented system is safe.
- **Security:** actor/resource matrix, idempotent retry, stale version, race and revoked permissions.
- **Manual:** user-directed gameplay/art/audio/native feel acceptance; engineers report evidence rather than marking it approved themselves.

| ID | Feature scope | Named failure/golden case | Evidence |
|---|---|---|---|
| QA-19-01 | Security vision, scope and trust boundaries | Threat model can trace each persistent state change to one authenticated server command or verified game receipt. | Automated fixture + owner-directed manual UI when visual |
| QA-19-02 | Threat actor inventory and attack tree | Each highest-severity threat has prevention, detection, containment and recovery owner. | Automated fixture + owner-directed manual UI when visual |
| QA-19-03 | Identity, authentication, session rotation and MFA | Stolen/revoked session fails both read and mutation endpoints. | Automated fixture + owner-directed manual UI when visual |
| QA-19-04 | Object-level authorization and RLS | IDOR suite swaps actor identity across all resource IDs and receives denied responses. | Automated fixture + owner-directed manual UI when visual |
| QA-19-05 | Service role, database grants and secrets | Static scan of JS output and source maps detects no secret pattern or live token. | Automated fixture + owner-directed manual UI when visual |
| QA-19-06 | Verified game session protocol and replay hashes | Replaying valid trace produces expected events and rejects reordered/inserted shots. | Automated fixture + owner-directed manual UI when visual |
| QA-19-07 | Rapier determinism prerequisites and cross-runtime tests | Desktop/browser/worker golden replay hash comparison gates ranked launch. | Automated fixture + owner-directed manual UI when visual |
| QA-19-08 | Shot command validation and time/angle bounds | Mutated shot impulse and negative timestep get deterministic rejection code. | Automated fixture + owner-directed manual UI when visual |
| QA-19-09 | Merge and serving anti-duplication | Synthetic duplicate contacts cannot mint double score or order coins. | Automated fixture + owner-directed manual UI when visual |
| QA-19-10 | Reward ledger and payment replay protection | Two parallel award workers for one first clear produce exactly one wallet ledger credit. | Automated fixture + owner-directed manual UI when visual |
| QA-19-11 | XP, skills and modifier abuse | Tampered client skill rank is ignored and flagged. | Automated fixture + owner-directed manual UI when visual |
| QA-19-12 | Achievement, chest and inventory integrity | Duplicate chest claims across devices return one canonical receipt. | Automated fixture + owner-directed manual UI when visual |
| QA-19-13 | Leaderboard integrity and tournament certification | Out-of-window replay cannot alter finalized tournament results or payout. | Automated fixture + owner-directed manual UI when visual |
| QA-19-14 | Social abuse, spam and moderation enforcement | Privacy test ensures cross-block visibility is consistent across APIs. | Automated fixture + owner-directed manual UI when visual |
| QA-19-15 | Rate limiting, bot mitigation and farming quotas | Repeated anonymous mission submission never creates spendable currency. | Automated fixture + owner-directed manual UI when visual |
| QA-19-16 | Input validation, deserialization and query injection | SQLi/XSS payload suites fail to execute and return controlled errors. | Automated fixture + owner-directed manual UI when visual |
| QA-19-17 | Browser CSP, CORS, CSRF and token hygiene | Origin spoof and XSS probe show no token exfiltration or unauthorized mutation. | Automated fixture + owner-directed manual UI when visual |
| QA-19-18 | Webhooks, receipts and external integrations | Forged billing webhook gives no entitlement; valid duplicate delivers one receipt. | Automated fixture + owner-directed manual UI when visual |
| QA-19-19 | Payments, refunds, chargebacks and entitlements | Chargeback transition follows published entitlement policy with consistent account state. | Automated fixture + owner-directed manual UI when visual |
| QA-19-20 | Content and asset supply-chain safety | Altered atlas digest fails integrity check and fallbacks stay safe. | Automated fixture + owner-directed manual UI when visual |
| QA-19-21 | Admin least privilege, approvals and privileged audit | Support compensation requires recorded reason, 2-person review for high amounts and immutable event. | Automated fixture + owner-directed manual UI when visual |
| QA-19-22 | AI-generated content and model output boundaries | Prompt injection in asset metadata cannot modify catalog publication state. | Automated fixture + owner-directed manual UI when visual |
| QA-19-23 | Data privacy, location and minimization | Export and deletion requests do not reveal another player's records. | Automated fixture + owner-directed manual UI when visual |
| QA-19-24 | Youth safety, UGC and reporting | Underage-safe profile suppresses unwanted invites and targeted ad events. | Automated fixture + owner-directed manual UI when visual |
| QA-19-25 | Availability, denial of service and resource constraints | Flood test returns rate limited responses without queue starvation. | Automated fixture + owner-directed manual UI when visual |
| QA-19-26 | Operational monitoring, anomaly detection and signal review | A simulated reward-farming spike emits actionable alert without logging secrets. | Automated fixture + owner-directed manual UI when visual |
| QA-19-27 | Incident severity, containment and communications | Tabletop drill recovers from compromised reward policy with no extra payout. | Automated fixture + owner-directed manual UI when visual |
| QA-19-28 | Penetration testing and coordinated disclosure | Synthetic authorized test produces reproducible finding with minimal evidence and remediation owner. | Automated fixture + owner-directed manual UI when visual |
| QA-19-29 | Security tests in CI and dependency review | Known critical bypass fixture blocks protected branch merge. | Automated fixture + owner-directed manual UI when visual |
| QA-19-30 | RLS and property-based security fixture matrix | RLS test proves authenticated cannot INSERT directly into wallets, XP, scores or receipts. | Automated fixture + owner-directed manual UI when visual |
| QA-19-31 | Security performance tradeoffs and rate-limit tuning | Load test under high concurrency maintains nonnegative wallet balances. | Automated fixture + owner-directed manual UI when visual |
| QA-19-32 | Release gates, independent audits and owner approval | Security checklist documents tested exploit classes and residual risks for each version. | Automated fixture + owner-directed manual UI when visual |
| QA-19-33 | Workstreams, security issue backlog and reviewer separation | Engineer PR names threat ID and includes a negative test. | Automated fixture + owner-directed manual UI when visual |
| QA-19-34 | ADRs, risk register and cross-batch traceability | All high-severity risk entries have compensating control and review date. | Automated fixture + owner-directed manual UI when visual |

## Required failure drills

1. Restart browser or native app between request acceptance and UI confirmation; durable state must recover from canonical receipt.
2. Retry an identical command 10 times and a changed-payload command using the same key; observe one effect and one conflict.
3. Expire or unpublish current content pointer while an old pinned run is in flight; its rules remain consistent or a clear safe rejection is delivered.
4. Switch to narrow mobile viewport, large text/reduced motion, offline and low-quality device profile; required UI text and gameplay remain usable.
5. With the relevant release gate OFF, every future route or action is explicitly unavailable and does not create a hidden write.

## What static validation does *not* prove

Schema and pure vector checks are not proof of licensed source delivery, live reward/financial correctness, deterministic cross-machine Rapier replay, actual web/native performance, store approval, privacy compliance or accessibility conformance. Track these separately on an owner-approved acceptance checklist.
