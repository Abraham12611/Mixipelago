# Batch 19 — Security, Anti-Cheat & Game Integrity

**Status:** Detailed engineering design pack; not an implemented/deployed feature. **Prepared:** 2026-11-14.
**Owner:** Application Security / Game Integrity. **Candidate release:** baseline in v0.1.x; enhanced before each trusted feature. **Advanced gate:** `CERTIFIED_SESSION_VERIFICATION_ENABLED` default OFF.

## Critical earlier rules
Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## Source-of-truth responsibilities
Cross-service threat models, verification controls, misuse prevention, authorization testing, incident response and audit policy.
All Batches 01–18, especially 02 deterministic Rapier, 04 score proofs, 06 wallet, 08 rewards, 13 ranks, 14 social, 18 backend, 20 payments and 21 native bridge.

## Specification chapters
- [01 — Security vision, scope and trust boundaries](./01_SECURITY_VISION_SCOPE_AND_TRUST_BOUNDARIES.md)
- [02 — Threat actor inventory and attack tree](./02_THREAT_ACTOR_INVENTORY_AND_ATTACK_TREE.md)
- [03 — Identity, authentication, session rotation and MFA](./03_IDENTITY_AUTHENTICATION_SESSION_ROTATION_AND_MFA.md)
- [04 — Object-level authorization and RLS](./04_OBJECT_LEVEL_AUTHORIZATION_AND_RLS.md)
- [05 — Service role, database grants and secrets](./05_SERVICE_ROLE_DATABASE_GRANTS_AND_SECRETS.md)
- [06 — Verified game session protocol and replay hashes](./06_VERIFIED_GAME_SESSION_PROTOCOL_AND_REPLAY_HASHES.md)
- [07 — Rapier determinism prerequisites and cross-runtime tests](./07_RAPIER_DETERMINISM_PREREQUISITES_AND_CROSS_RUNTIME_TESTS.md)
- [08 — Shot command validation and time/angle bounds](./08_SHOT_COMMAND_VALIDATION_AND_TIME_ANGLE_BOUNDS.md)
- [09 — Merge and serving anti-duplication](./09_MERGE_AND_SERVING_ANTI_DUPLICATION.md)
- [10 — Reward ledger and payment replay protection](./10_REWARD_LEDGER_AND_PAYMENT_REPLAY_PROTECTION.md)
- [11 — XP, skills and modifier abuse](./11_XP_SKILLS_AND_MODIFIER_ABUSE.md)
- [12 — Achievement, chest and inventory integrity](./12_ACHIEVEMENT_CHEST_AND_INVENTORY_INTEGRITY.md)
- [13 — Leaderboard integrity and tournament certification](./13_LEADERBOARD_INTEGRITY_AND_TOURNAMENT_CERTIFICATION.md)
- [14 — Social abuse, spam and moderation enforcement](./14_SOCIAL_ABUSE_SPAM_AND_MODERATION_ENFORCEMENT.md)
- [15 — Rate limiting, bot mitigation and farming quotas](./15_RATE_LIMITING_BOT_MITIGATION_AND_FARMING_QUOTAS.md)
- [16 — Input validation, deserialization and query injection](./16_INPUT_VALIDATION_DESERIALIZATION_AND_QUERY_INJECTION.md)
- [17 — Browser CSP, CORS, CSRF and token hygiene](./17_BROWSER_CSP_CORS_CSRF_AND_TOKEN_HYGIENE.md)
- [18 — Webhooks, receipts and external integrations](./18_WEBHOOKS_RECEIPTS_AND_EXTERNAL_INTEGRATIONS.md)
- [19 — Payments, refunds, chargebacks and entitlements](./19_PAYMENTS_REFUNDS_CHARGEBACKS_AND_ENTITLEMENTS.md)
- [20 — Content and asset supply-chain safety](./20_CONTENT_AND_ASSET_SUPPLY_CHAIN_SAFETY.md)
- [21 — Admin least privilege, approvals and privileged audit](./21_ADMIN_LEAST_PRIVILEGE_APPROVALS_AND_PRIVILEGED_AUDIT.md)
- [22 — AI-generated content and model output boundaries](./22_AI_GENERATED_CONTENT_AND_MODEL_OUTPUT_BOUNDARIES.md)
- [23 — Data privacy, location and minimization](./23_DATA_PRIVACY_LOCATION_AND_MINIMIZATION.md)
- [24 — Youth safety, UGC and reporting](./24_YOUTH_SAFETY_UGC_AND_REPORTING.md)
- [25 — Availability, denial of service and resource constraints](./25_AVAILABILITY_DENIAL_OF_SERVICE_AND_RESOURCE_CONSTRAINTS.md)
- [26 — Operational monitoring, anomaly detection and signal review](./26_OPERATIONAL_MONITORING_ANOMALY_DETECTION_AND_SIGNAL_REVIEW.md)
- [27 — Incident severity, containment and communications](./27_INCIDENT_SEVERITY_CONTAINMENT_AND_COMMUNICATIONS.md)
- [28 — Penetration testing and coordinated disclosure](./28_PENETRATION_TESTING_AND_COORDINATED_DISCLOSURE.md)
- [29 — Security tests in CI and dependency review](./29_SECURITY_TESTS_IN_CI_AND_DEPENDENCY_REVIEW.md)
- [30 — RLS and property-based security fixture matrix](./30_RLS_AND_PROPERTY_BASED_SECURITY_FIXTURE_MATRIX.md)
- [31 — Security performance tradeoffs and rate-limit tuning](./31_SECURITY_PERFORMANCE_TRADEOFFS_AND_RATE_LIMIT_TUNING.md)
- [32 — Release gates, independent audits and owner approval](./32_RELEASE_GATES_INDEPENDENT_AUDITS_AND_OWNER_APPROVAL.md)
- [33 — Workstreams, security issue backlog and reviewer separation](./33_WORKSTREAMS_SECURITY_ISSUE_BACKLOG_AND_REVIEWER_SEPARATION.md)
- [34 — ADRs, risk register and cross-batch traceability](./34_ADRS_RISK_REGISTER_AND_CROSS_BATCH_TRACEABILITY.md)

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
- `../tools/validate_batch19.py` — Python validator using `jsonschema` for full schema checks.

## Start implementation
1. Read the first six chapters and the implementation blueprint.
2. Pin content and rules versions, prove fixtures and agree on event boundaries.
3. Build a small feature-gated integration slice with accessible fallback.
4. Run negative authorization and replay tests, then owner-directed visual/audio/gameplay acceptance.
5. No engineer self-merges; owner approval required for main/production promotion.

**Next batch/dependency:** 20 — Monetization, analytics and live operations.
