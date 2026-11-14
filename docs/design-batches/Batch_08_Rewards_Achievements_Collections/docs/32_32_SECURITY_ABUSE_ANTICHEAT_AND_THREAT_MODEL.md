# 32 — Security, Fraud and Abuse Threat Model

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Threats
Forged session proof, manipulated client event, double claims, multi-device races, reward-policy replacement, asset URL injection, compromised catalog admin, pity counter manipulation, account swapping, timezone spoofing, reward-recursion loops, unfair paid power, and unauthorized operator grant.

## Controls
- Grant authority lives behind authenticated backend/service credentials and audited issuer allowlists.
- Unique claim/source receipt keys plus actor-scoped command idempotency.
- Server-owned versions for source verification, catalog, mission result and policy budgets.
- RLS prevents client writes to economy and inventory authority tables.
- Rate limits protect claims but do not serve as correctness controls.
- Immutable receipts, outbox/inbox audit and reconciliation.
- Compensation restricted to narrow operator workflow with dual approval.
- Rank prizes consume only finalized trusted placement receipts, not client-submitted scores.

## Abuse test fixtures
Simultaneous claim with two keys, same key/different body, replayed producer event, forged `playerId`, stale catalog snapshot, future-dated fake login, expired event, hidden treasure before reveal, unowned cosmetic equip, achievement counter negative update, malformed random weights, reward cycle and unauthorized grant endpoint.

## Privacy and telemetry
Log receipt identifiers and reason codes, not account email, auth tokens, complete location, or private social graph. Retain minimal evidence needed for audit and fraud investigation under written retention policy.

## No false confidence
Passing a JSON validator is not equivalent to penetration testing. Before enabling trusted currency or paid content, perform actual database authorization, API concurrency and fraud-path tests.
