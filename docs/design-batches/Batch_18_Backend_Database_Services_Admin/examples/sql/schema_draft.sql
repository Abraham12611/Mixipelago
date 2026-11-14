-- Mixipelago reference SQL only. DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Require schema/RLS/security review and isolated staging migration rehearsal.

create table if not exists trusted_receipts_draft (
  id uuid primary key, player_id uuid not null, source_kind text not null,
  source_id text not null, rules_hash text not null, policy_hash text not null,
  created_at timestamptz not null default now(),
  unique (player_id,source_kind,source_id,policy_hash)
);
create table if not exists platform_outbox_draft (
  event_id uuid primary key, aggregate text not null, event_type text not null,
  payload jsonb not null, created_at timestamptz not null default now(),
  published_at timestamptz
);
-- Lock relevant wallet/progression rows and insert receipt+outbox in one transaction.
-- Do not grant access to anon/authenticated direct writes; add scoped RLS to exposed projections.
