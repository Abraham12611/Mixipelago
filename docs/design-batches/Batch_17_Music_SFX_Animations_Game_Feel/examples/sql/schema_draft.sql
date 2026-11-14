-- Mixipelago reference SQL only. DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Require schema/RLS/security review and isolated staging migration rehearsal.

create table if not exists audio_cue_catalog_draft (
  cue_id text primary key, manifest_version text not null, event_name text not null,
  bus text not null, max_voices integer not null check (max_voices > 0),
  license_state text not null, published_at timestamptz
);
-- Audio preferences are per-user and do not affect verified gameplay receipts.
