-- Mixipelago reference SQL only. DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Require schema/RLS/security review and isolated staging migration rehearsal.

create table if not exists release_compatibility_draft (
  platform text not null, app_version text not null,
  min_schema integer not null, content_hash text not null,
  published_at timestamptz, primary key(platform,app_version)
);
-- Platform releases and client upgrade signals are not reward-grant endpoints.
