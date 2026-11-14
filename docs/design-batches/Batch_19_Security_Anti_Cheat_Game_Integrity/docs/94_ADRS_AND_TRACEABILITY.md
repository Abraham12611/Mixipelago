# 94 — ADRs, Decisions, Risks and Traceability

## Locked constraints inherited from Batches 1–15

Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

- **1.** Browser and native clients are untrusted even when running unmodified UI.
- **2.** Every data access is authenticated and authorized; exposed DB tables require appropriate RLS/grants.
- **3.** Deterministic replay verification, not score upload, gates certified competition and valuable rewards.
- **4.** Idempotent grants and compensating ledger entries prevent duplicated and invisible financial changes.
- **5.** No security mitigation may disable safe alpha play or quietly invent verified outcomes.

## Design choices proposed in this batch

- **ADR-19-001 — Authority:** Cross-service threat models, verification controls, misuse prevention, authorization testing, incident response and audit policy. This is separate from physical simulation, score reducers, wallet settlement and inventory source of truth.
- **ADR-19-002 — Versioning:** every published document/catalog sample uses immutable digest and review states. A draft entry is not production content.
- **ADR-19-003 — Progressive disclosure:** minimum security from alpha; ranked, wallet, billing add stricter gates. Further systems stay OFF until their dependencies and user approval exist.
- **ADR-19-004 — Recovery:** read-only fallback and conservative reject, with explicit error/result states and no fabricated success.
- **ADR-19-005 — Integrity:** actor identity and any durable grant/competition result come from a verified source receipt; presentation cannot mutate authoritative records.

## Cross-batch traceability

| Neighbor | Contract owner and integration |
|---|---|
| Batch 02 / 03 | Fixed 60 Hz Rapier, exact merge semantics, eight-tier ladder, oldest-compatible order auto-serving |
| Batch 04 / 05 | Verified mission results, immutable content versions, published island graph |
| Batch 06 / 07 / 08 | Trusted coins/ledger, first-clear XP/skills and collectible entitlements |
| Batch 09 / 10 / 11 / 12 | Customer models, world incidents, narrative and festivals as independently feature-gated projections |
| Batch 13 / 14 | Normalized verified ranking, social consent/blocking and anti-abuse |
| Batch 15 / 16 / 17 | Semantic React UI, Phaser presentation, licensed art and original audio |
| Batch 18 / 19 / 20 / 21 | Trusted commands and admin, security, commerce/analytics and native platform lifecycle |

## Open owner decisions

1. Approve final creative direction and measured default values after real-device manual testing.
2. Decide on first shipping content boundaries; don't let later monetization/social features block the playable first week.
3. Approve any native store payment and age-rating behavior only after current policy/legal review.
4. Approve server hosting strategy and operating budget after traffic/latency evidence; do not preemptively overengineer.
5. Set owner signoff for content/legal provenance, security review and promotion to `main`/production.

## Risk response

An unavailable service shows a safe read-only projection. A broken catalog rolls back its published pointer. A disputed financial grant is settled by compensating entry, not balance surgery. A suspected score is withheld pending reproducible proof. A compromised credential is rotated and account sessions revoked with a written incident record. Platform submission failure leaves browser-first play available.
