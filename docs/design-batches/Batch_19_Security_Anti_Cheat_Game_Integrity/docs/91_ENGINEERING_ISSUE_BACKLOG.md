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
| MX19-001 | A/Contracts | Security vision, scope and trust boundaries | Contract + negative fixture + accessible fallback; **Threat model can trace each persistent state change to one authenticated server command or verified game receipt.** |
| MX19-002 | A/Contracts | Threat actor inventory and attack tree | Contract + negative fixture + accessible fallback; **Each highest-severity threat has prevention, detection, containment and recovery owner.** |
| MX19-003 | A/Contracts | Identity, authentication, session rotation and MFA | Contract + negative fixture + accessible fallback; **Stolen/revoked session fails both read and mutation endpoints.** |
| MX19-004 | A/Contracts | Object-level authorization and RLS | Contract + negative fixture + accessible fallback; **IDOR suite swaps actor identity across all resource IDs and receives denied responses.** |
| MX19-005 | A/Contracts | Service role, database grants and secrets | Contract + negative fixture + accessible fallback; **Static scan of JS output and source maps detects no secret pattern or live token.** |
| MX19-006 | B/Core | Verified game session protocol and replay hashes | Contract + negative fixture + accessible fallback; **Replaying valid trace produces expected events and rejects reordered/inserted shots.** |
| MX19-007 | B/Core | Rapier determinism prerequisites and cross-runtime tests | Contract + negative fixture + accessible fallback; **Desktop/browser/worker golden replay hash comparison gates ranked launch.** |
| MX19-008 | B/Core | Shot command validation and time/angle bounds | Contract + negative fixture + accessible fallback; **Mutated shot impulse and negative timestep get deterministic rejection code.** |
| MX19-009 | B/Core | Merge and serving anti-duplication | Contract + negative fixture + accessible fallback; **Synthetic duplicate contacts cannot mint double score or order coins.** |
| MX19-010 | B/Core | Reward ledger and payment replay protection | Contract + negative fixture + accessible fallback; **Two parallel award workers for one first clear produce exactly one wallet ledger credit.** |
| MX19-011 | B/Core | XP, skills and modifier abuse | Contract + negative fixture + accessible fallback; **Tampered client skill rank is ignored and flagged.** |
| MX19-012 | B/Core | Achievement, chest and inventory integrity | Contract + negative fixture + accessible fallback; **Duplicate chest claims across devices return one canonical receipt.** |
| MX19-013 | C/Integrations | Leaderboard integrity and tournament certification | Contract + negative fixture + accessible fallback; **Out-of-window replay cannot alter finalized tournament results or payout.** |
| MX19-014 | C/Integrations | Social abuse, spam and moderation enforcement | Contract + negative fixture + accessible fallback; **Privacy test ensures cross-block visibility is consistent across APIs.** |
| MX19-015 | C/Integrations | Rate limiting, bot mitigation and farming quotas | Contract + negative fixture + accessible fallback; **Repeated anonymous mission submission never creates spendable currency.** |
| MX19-016 | C/Integrations | Input validation, deserialization and query injection | Contract + negative fixture + accessible fallback; **SQLi/XSS payload suites fail to execute and return controlled errors.** |
| MX19-017 | C/Integrations | Browser CSP, CORS, CSRF and token hygiene | Contract + negative fixture + accessible fallback; **Origin spoof and XSS probe show no token exfiltration or unauthorized mutation.** |
| MX19-018 | C/Integrations | Webhooks, receipts and external integrations | Contract + negative fixture + accessible fallback; **Forged billing webhook gives no entitlement; valid duplicate delivers one receipt.** |
| MX19-019 | C/Integrations | Payments, refunds, chargebacks and entitlements | Contract + negative fixture + accessible fallback; **Chargeback transition follows published entitlement policy with consistent account state.** |
| MX19-020 | C/Integrations | Content and asset supply-chain safety | Contract + negative fixture + accessible fallback; **Altered atlas digest fails integrity check and fallbacks stay safe.** |
| MX19-021 | C/Integrations | Admin least privilege, approvals and privileged audit | Contract + negative fixture + accessible fallback; **Support compensation requires recorded reason, 2-person review for high amounts and immutable event.** |
| MX19-022 | D/QA-Publish | AI-generated content and model output boundaries | Contract + negative fixture + accessible fallback; **Prompt injection in asset metadata cannot modify catalog publication state.** |
| MX19-023 | D/QA-Publish | Data privacy, location and minimization | Contract + negative fixture + accessible fallback; **Export and deletion requests do not reveal another player's records.** |
| MX19-024 | D/QA-Publish | Youth safety, UGC and reporting | Contract + negative fixture + accessible fallback; **Underage-safe profile suppresses unwanted invites and targeted ad events.** |
| MX19-025 | D/QA-Publish | Availability, denial of service and resource constraints | Contract + negative fixture + accessible fallback; **Flood test returns rate limited responses without queue starvation.** |
| MX19-026 | D/QA-Publish | Operational monitoring, anomaly detection and signal review | Contract + negative fixture + accessible fallback; **A simulated reward-farming spike emits actionable alert without logging secrets.** |
| MX19-027 | D/QA-Publish | Incident severity, containment and communications | Contract + negative fixture + accessible fallback; **Tabletop drill recovers from compromised reward policy with no extra payout.** |
| MX19-028 | D/QA-Publish | Penetration testing and coordinated disclosure | Contract + negative fixture + accessible fallback; **Synthetic authorized test produces reproducible finding with minimal evidence and remediation owner.** |
| MX19-029 | D/QA-Publish | Security tests in CI and dependency review | Contract + negative fixture + accessible fallback; **Known critical bypass fixture blocks protected branch merge.** |
| MX19-030 | D/QA-Publish | RLS and property-based security fixture matrix | Contract + negative fixture + accessible fallback; **RLS test proves authenticated cannot INSERT directly into wallets, XP, scores or receipts.** |
| MX19-031 | D/QA-Publish | Security performance tradeoffs and rate-limit tuning | Contract + negative fixture + accessible fallback; **Load test under high concurrency maintains nonnegative wallet balances.** |
| MX19-032 | D/QA-Publish | Release gates, independent audits and owner approval | Contract + negative fixture + accessible fallback; **Security checklist documents tested exploit classes and residual risks for each version.** |
| MX19-033 | D/QA-Publish | Workstreams, security issue backlog and reviewer separation | Contract + negative fixture + accessible fallback; **Engineer PR names threat ID and includes a negative test.** |
| MX19-034 | D/QA-Publish | ADRs, risk register and cross-batch traceability | Contract + negative fixture + accessible fallback; **All high-severity risk entries have compensating control and review date.** |

## Parallelization policy

- Stream A first freezes IDs and event schema. Pure calculations in stream B can begin simultaneously against fixtures. UI/Content Studio stream C can mock stable read models but cannot invent grant or rank writes.
- Stream D authors negative tests and performance/a11y harness concurrently; avoid waiting until all UI is complete.
- Every PR describes precise files affected, tests run, fixture output, dependent batch contracts, rollout gate and fallback. A migration requires isolated staging verification and an explicit read/write compatibility window.
- If a feature requires another service that is not implemented, merge only its gated read-only contract and document the blocked dependency; never hide placeholder functionality behind a working button.
