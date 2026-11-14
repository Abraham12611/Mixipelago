# 42 — Glossary, References and Non-goals

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Key terms
**Achievement:** verified rule completion. **Entitlement:** claimable right to award. **Claim receipt:** durable settlement record. **Grant line:** one item/currency entitlement. **Album edition:** immutable set membership denominator. **Event scope:** once-ever/per-season/per-UTC-window identity. **Outbox:** durable pending publication of committed domain event. **Inbox:** per-consumer dedup table. **Idempotency:** same meaningful command applied once even under retries. **Provenance:** verified source of ownership. **Randomized reward:** reward selected using published odds by server, not client.

## Normative internal source documents
- Batch 3 `03_ALPHA_EIGHT_TIER_DRINK_BIBLE.md`: eight-tier ladder, tier 8 terminal, oldest matching order served before chain continuation.
- Batch 4 `22_REWARDS_PROGRESS_AND_ECONOMY_HANDOFF.md`: scores/stars vs preview rewards and trusted source.
- Batch 5 `18_REWARDS_TREASURE_AND_ECONOMY_HANDOFF.md`: treasure, claim identity, graph evidence.
- Batch 6 `05_LEDGER_TRANSACTION_IDEMPOTENCY.md`: monetary authority, unique ledger source and idempotency.
- Batch 7 `04_04_XP_REWARD_SOURCES_AND_AWARD_POLICY.md`: XP eligibility and point milestones.

## Suggested official engineering references
- PostgreSQL transactions/unique indexes: https://www.postgresql.org/docs/current/transaction-iso.html and https://www.postgresql.org/docs/current/indexes-unique.html
- PostgreSQL RLS: https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- Supabase authorization: https://supabase.com/docs/guides/database/postgres/row-level-security
- JSON Schema: https://json-schema.org/specification
- WCAG guidelines: https://www.w3.org/WAI/standards-guidelines/wcag/
- OWASP API Security: https://owasp.org/API-Security/

## Explicit non-goals in this batch
Full weather/incidents/roleplay, final island lore, player trading, real-money loot box implementation, social-chat moderation, tournament scoring logic, production-ready database migration and an implemented rewards service. The documents define seams so future teams can expand safely.
