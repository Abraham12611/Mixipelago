-- Mixipelago reference SQL only. DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Require schema/RLS/security review and isolated staging migration rehearsal.

create table if not exists art_asset_catalog_draft (
  asset_id text primary key, manifest_version text not null,
  kind text not null, source_uri text, license_state text not null,
  approved_by uuid, digest text, published_at timestamptz
);
-- Public clients read only an approved, immutable content projection.
-- Never expose raw artist source files or privileged drafting tables.
