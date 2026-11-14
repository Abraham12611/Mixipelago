-- Mixipelago reference SQL only. DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Require schema/RLS/security review and isolated staging migration rehearsal.

create table if not exists security_audit_draft (
  event_id uuid primary key, actor_id uuid, request_id text,
  action_type text not null, decision text not null,
  reason_code text, created_at timestamptz not null default now()
);
-- Never put JWTs, credit-card numbers, device fingerprint or precise location in payload.
-- Defense-in-depth includes API auth + RLS + immutable domain receipts.
