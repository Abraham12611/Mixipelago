# Mixipelago — Engineering Documentation Batches 16–21

**Prepared:** 2026-11-14. All packages are implementation specifications, not implemented app features.

These final six batches complete the planned 21-batch design handoff. They can be downloaded as separate packs or together. They do not authorize release, payment processing or application store submission.

## Batches

- **Batch 16 — [Art Direction, Characters & 2.5D Asset Production](../Batch_16_Art_Direction_Characters_2_5D_Assets/docs/00_INDEX_AND_README.md)** — Visual / Art Pipeline; v0.1.x foundational, extended with island/shop releases.
- **Batch 17 — [Music, Sound Effects, Animations & Game Feel](../Batch_17_Music_SFX_Animations_Game_Feel/docs/00_INDEX_AND_README.md)** — Audio / Game Feel; v0.1.x foundational audio, dynamic mix after gameplay proof.
- **Batch 18 — [Backend, Database, Game Services & Admin Studio](../Batch_18_Backend_Database_Services_Admin/docs/00_INDEX_AND_README.md)** — Backend / Data / Admin Platform; trusted foundation v0.3.x+; advanced services by feature.
- **Batch 19 — [Security, Anti-Cheat & Game Integrity](../Batch_19_Security_Anti_Cheat_Game_Integrity/docs/00_INDEX_AND_README.md)** — Application Security / Game Integrity; baseline in v0.1.x; enhanced before each trusted feature.
- **Batch 20 — [Monetization, Analytics, Retention & Live Operations](../Batch_20_Monetization_Analytics_Retention_LiveOps/docs/00_INDEX_AND_README.md)** — Product Analytics / Economy / Commerce; telemetry first; optional cosmetics after trusted commerce; advanced systems later.
- **Batch 21 — [Native Mobile, Performance, Scaling & Release Engineering](../Batch_21_Native_Mobile_Performance_Release_Engineering/docs/00_INDEX_AND_README.md)** — Platform / Mobile / SRE; browser alpha first; Capacitor native after quality and retention gates.

## Source-of-truth boundaries
Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

- Assets and audio (16–17) are presentation only; they cannot grant trusted progression.
- Backend (18) alone coordinates server-owned state, and security (19) independently verifies it.
- Commerce (20) is disabled until a compliant provider-receipt + inventory flow is live and reviewed.
- Native (21) wraps the same pure game, with visual optimization only and fresh store-policy review.
- Batch 15 React semantics and Batch 02/03 gameplay rules remain unchanged.

## Implementation order
1. Visual/audio alpha foundation while the browser gameplay is built and tested.
2. Trusted backend minimum: authenticated account, session verification, one unique entitlement and recovery.
3. Security regression/role tests before any durable grants or ranking.
4. Privacy-aware analytics; optional cosmetics only after billing/reconciliation review.
5. Capacitor native beta after browser retention, touch, performance and owner manual tests.

## Common resources
- [Cross-batch authority and release map](CROSS_BATCH_AUTHORITY_AND_RELEASES.md)
- [Unified integration QA checklist](BATCHES_16_21_INTEGRATION_CHECKLIST.md)
- [Outstanding decisions register](FINAL_ADR_AND_DECISION_REGISTER.md)
- [Full batch catalog](FINAL_21_BATCH_INDEX.md)
