# 07 — Customer Director: Eligibility, Deterministic Selection and Reservations

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Responsibilities
The Customer Director chooses eligible customer **identities and encounters**, never adjudicates physical merges or directly settles wallet rewards. It operates on a versioned snapshot of `{missionId, modeId, publishedPoolVersion, shopId, reputationBand, effectiveSkills, eventContext, seed}`. Scripted tutorial guests bypass random selection.

## Selection algorithm
1. Verify player/shop ownership and the published mission/segment pool.
2. Filter disabled characters, wrong region, unavailable art, prerequisite failures and non-eligible encounter types.
3. Resolve customer class probability: starting VIP base + approved absolute modifier points, clamp to the published cap (`0.20` candidate, not a guaranteed default), and apply normalized-ranked profile overrides.
4. Within the selected segment, sort eligible customer IDs, normalize integer weights and draw using a persisted deterministic PRNG stream.
5. Persist `EncounterReserved` with pool hash, seed commitment and all chosen customer/order identities in a transaction **before** returning the response.
6. Create orders only through the Batch 3/4 order generator, constrained by mission feasibility and remaining resource budget.

## No reroll vulnerability
Refresh, cancel/restart, multiple tabs, reconnect or retries with the same entitlement cannot sample again. Reservation identity scopes to a published allowed encounter slot or verified session transition. A client cannot request `segmentId=vip_guest` to force a premium visitor. Retries return the original response under idempotency.

## Order of precedence
Fixed mission customer/order -> published encounter slot -> allowed regional/event pool -> effective customer distribution. A shop cosmetic without an explicit published economic modifier must be ignored. A VIP-skill bonus never changes already visible orders or active encounters.

## Predictability and audit
Persist `poolVersion`, `rulesVersion`, selection outcome and hashed/committed RNG context for diagnostics. Do not log secret server seed in public telemetry. Probability sums and caps are validated offline before publication; zero-eligible pools fail closed to a safe, authored fallback or stop publication.
