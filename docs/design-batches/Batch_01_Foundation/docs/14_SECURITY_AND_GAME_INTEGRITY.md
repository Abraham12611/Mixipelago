# 14 — Security, Integrity and Anti-Exploit Principles

## Threat model

Browser client is untrusted. An attacker can edit localStorage, replay requests, script input, patch JavaScript, tamper with DOM, intercept API traffic and submit impossible scores. App credentials and API rules must assume this. In alpha, scores and coins are **local preview only** and should not be called verified.

## Critical assets to protect (later)

- Player profile and authentication.
- Trusted wallet, reward/upgrade ownership, skill points, leaderboard standing.
- Season reward distribution.
- Moderation/privacy settings and regional board selection.
- Content publishing/admin accounts.
- API service credentials and asset upload rights.

## Security baseline for v0.1

- No secrets in browser bundles or repository.
- Content-only client save; validate saved payload against schemas to avoid crashes.
- Safe link handling; CSP compatible with assets/analytics; no arbitrary user HTML in game.
- Sanitize dynamic strings and URLs.
- Dependency scanning, lockfile and supply-chain review.
- Disable debug physics lab/secret test controls in production.
- Rate-limit telemetry endpoints if one is used.
- Browser game must degrade gracefully when CDN network fails; no infinite retry loop.

## Trusted backend (when activated)

1. Supabase Auth or equivalent verifies identity; use `auth.uid()` and explicit RLS ownership policies.
2. Role/grants reviewed for every exposed table; deny client wallet writes.
3. Commands validate shape, actor, ownership, version, prerequisites, state and business invariants.
4. Atomic wallet/upgrade/reward changes in SQL transactions.
5. Idempotency keys and uniqueness constraints on reward/mutation references.
6. Action-specific rate limits, abuse alerts, audit trails.
7. Secret keys stored in server/runtime env vault, never `NEXT_PUBLIC_*`.
8. Admin actions require elevated auth and audit logs; no role spoof via user-controllable metadata.
9. Periodic reconciliation compares ledger sum to cached wallet balance.
10. Backups and migration recoverability tested before economy goes live.

## Score verification and physics

Record `sessionId`, server-provided seed, input commands+simulation step, mission hash, physics version, rules version, event checksum. Verification can attempt constrained replay or score plausibility checks. Rapier simulations may not be bit-identical across engines/architectures; validate deterministic behavior empirically, and do not launch prize-bearing rankings before verification is proven. For competitive high-stakes modes, authoritative server execution or tightly controlled runtime may be required.

Do not accept posted `score`, `coins`, `stars` as financial or rank truth. A completed session should be terminal and idempotent.

## Social and moderation

- Report/block users; sanitize usernames; rate limits on invites/chat.
- Privacy-first locality: coarse opt-in region, no public street/city inferred from exact location.
- Anti-sybil controls for prizes and seasonal bots.
- Abuse review and appeal path for false positives.
- Child-friendly content strategy; no uncontrolled chat or adult-themed cocktail prompts.

## Incident handling

Critical exploit found → disable affected server feature with kill switch → preserve audit logs → communicate affected functionality → patch and test → reconcile if appropriate → rollback/restore. Do not silently debit users as a workaround.

## Test matrix

- Double-spend / two simultaneous purchases.
- Duplicate API retries with same idempotency key.
- Swap user ID / shop ID to read or mutate others' records.
- Fake completed mission / impossible score / outdated content version.
- Leaderboard scope changes without consent.
- Unauthorized admin publish or reward grant.
- Broken or manipulated local save should not crash app.
