-- Mixipelago Batch 15: ILLUSTRATIVE SCHEMA ONLY.
-- NOT a production migration. Requires security and SQL review, FK design, RLS policies, and replay/settlement tests.
-- All player-facing mutations must go through authenticated backend commands and durable audit.
BEGIN;
-- pgcrypto / gen_random_uuid() availability must be checked on target Postgres version.
CREATE TABLE IF NOT EXISTS game_ui_publications (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  edition text NOT NULL, content_hash text NOT NULL, published_at timestamptz,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_ui_publications ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_ui_publications FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_ui_preferences (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, revision integer NOT NULL, preferences jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_ui_preferences ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_ui_preferences FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_ui_audit_log (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  actor_id uuid, event_type text NOT NULL, payload jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_ui_audit_log ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_ui_audit_log FROM anon, authenticated;

-- Production migration MUST add: precise foreign keys, unique idempotency constraints,
-- actor/tenant SELECT policies for exposed projections, per-table indexes,
-- audited service RPCs, scoped grants, backups and down/forward recovery plan.
COMMIT;
