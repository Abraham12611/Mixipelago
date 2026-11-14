-- Mixipelago Batch 10: ILLUSTRATIVE SCHEMA ONLY.
-- NOT a production migration. Requires security and SQL review, FK design, RLS policies, and replay/settlement tests.
-- All player-facing mutations must go through authenticated backend commands and durable audit.
BEGIN;
-- pgcrypto / gen_random_uuid() availability must be checked on target Postgres version.
CREATE TABLE IF NOT EXISTS game_world_snapshots (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  island_id text NOT NULL, content_hash text NOT NULL, edition text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_world_snapshots ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_world_snapshots FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_condition_windows (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  island_id text NOT NULL, starts_at timestamptz NOT NULL, ends_at timestamptz NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_condition_windows ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_condition_windows FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_incident_offers (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, incident_definition text NOT NULL, state text NOT NULL DEFAULT 'offered', revision integer NOT NULL DEFAULT 0,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_incident_offers ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_incident_offers FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_incident_choice_receipts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, offer_id uuid NOT NULL, choice_id text NOT NULL, source_key text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_incident_choice_receipts ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_incident_choice_receipts FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_world_outbox (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type text NOT NULL, payload jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_world_outbox ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_world_outbox FROM anon, authenticated;

-- Production migration MUST add: precise foreign keys, unique idempotency constraints,
-- actor/tenant SELECT policies for exposed projections, per-table indexes,
-- audited service RPCs, scoped grants, backups and down/forward recovery plan.
COMMIT;
