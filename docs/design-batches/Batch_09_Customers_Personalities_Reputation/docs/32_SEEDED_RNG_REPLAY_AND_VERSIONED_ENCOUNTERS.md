# 32 — Seeded RNG, Replay Verification and Deterministic Sampling

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Determinism requirements
Future dynamic encounters must be reproducible under a pinned `poolVersion`, `policyVersion`, ordered eligible ID list and sample seed/PRNG algorithm. Stable weighted selection is a **pure function** of that state. Avoid `Math.random()` for persistent encounter issuance and avoid relying on object insertion order from a cached JSON map.

## Candidate weighted sampler
Filter and sort by stable `customerId`; require integer positive weights; sum in safe-integer range; draw integer in `[0,totalWeight)` using a versioned PRNG; return the first cumulative weight exceeding draw. Keep segment class selection separate from within-class selection so VIP cap is interpretable. If all weights are zero, reject publication or use an explicitly authored fallback, never a covert shift to VIP.

## Server secret vs replay proof
Do not expose a secret sampling seed that would let players predict or manufacture premium encounters. Store seed commitment and result on server; a public replay may contain a redacted generated encounter ID, not an exploitable future RNG state. For competition, all competitors use an identical published standardized encounter set and seed.

## Idempotency
Encounter reserved once per source entitlement; retries return identical outcome, not another draw. Switching devices, refreshing or manipulating request timing cannot mint a new candidate. A content deployment after reservation cannot mutate the already pinned participant.

## Regression vectors
Zero weights excluded, sorted identifiers stable across JSON ordering, bps VIP cap enforcement, same draw returns same visitor, different eligibility snapshot changes version and refuses old replay, no newly introduced order during finished mission, and no hidden score modification from portrait changes.
