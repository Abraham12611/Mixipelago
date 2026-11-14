-- Mixipelago reference SQL only. DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Require schema/RLS/security review and isolated staging migration rehearsal.

create table if not exists provider_purchase_receipts_draft (
  id uuid primary key, player_id uuid not null,
  provider text not null, provider_tx_id text not null,
  sku_id text not null, state text not null,
  created_at timestamptz not null default now(),
  unique (provider,provider_tx_id)
);
create table if not exists commercial_offerings_draft (
  sku_id text primary key, catalog_version text not null,
  category text not null, enabled boolean not null default false
);
-- External payment receipt is not an in-game soft coin ledger entry.
