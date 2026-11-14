# 30 — PostgreSQL Data Model, RLS and Forward-only Migration

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Data domain (proposal)
`customer_catalog_versions`, `customer_definitions`, `customer_pools`, `customer_encounters`, `customer_service_observations`, `customer_relationships`, `customer_relationship_events`, `shop_reputation_events`, `customer_policy_versions`, `customer_outbox` (may integrate with existing Batch 6 outbox rather than create a separate infrastructure). Draft SQL in `examples/sql/customer_schema_draft.sql` documents constraints but is **not a runnable production migration**.

## Keys and constraints
- Unique encounter entitlement `(player_id, shop_id, encounter_source_id)`; server-owned identity; FK to published pool version.
- Unique observation `(player_id, verified_result_receipt_id, encounter_id, observation_policy_version)`.
- Unique relationship source `(player_id, shop_id, customer_id, source_encounter_id)`.
- Shop reputation event source unique across retries; integer reputation bounded `0..10000`.
- No negative loyalty totals; authorized compensating events rather than rewriting historical receipts.
- All mutation tables should include append-only audit references and created timestamps.

## RLS / access
Players read only their journal and reputation projections. Browser writes to encounters, verified service observations, reputation adjustments and relationship events are denied; only tightly scoped backend roles can settle them. Public catalog rows are readable only if published and not secret; secret guest content stays server-side until eligible.

## Migration sequence
1. Create versioned catalogs and read-only endpoint behind OFF gate.
2. Add canonical encounter/source uniqueness and server reservation path.
3. Add verified observation reducer with dry-run reconciliation and no player-facing effect.
4. Enable small read-only reputation UI for trusted users.
5. Add relationship/source events and one named guest pilot once verified.
6. Enable eligible VIP/critic modes only after reward, anti-cheat and feasibility gates.

## Rollback
Turn OFF new encounter issuance and policy application; keep verified receipts and inventory unchanged. Fix forward with audited migration or compensating event; do not drop history during rollback. Backups and restore drill required before economic feature activation.
