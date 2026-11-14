-- Mixipelago Batch 12: ILLUSTRATIVE SCHEMA ONLY.
-- NOT a production migration. Requires security and SQL review, FK design, RLS policies, and replay/settlement tests.
-- All player-facing mutations must go through authenticated backend commands and durable audit.
BEGIN;
-- pgcrypto / gen_random_uuid() availability must be checked on target Postgres version.
CREATE TABLE IF NOT EXISTS game_event_editions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  edition_key text NOT NULL, starts_at timestamptz NOT NULL, ends_at timestamptz NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_event_editions ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_event_editions FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_event_activities (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  edition_id uuid NOT NULL, activity_key text NOT NULL, policy_key text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_event_activities ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_event_activities FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_event_enrollments (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, edition_id uuid NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_event_enrollments ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_event_enrollments FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_event_contributions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, activity_id uuid NOT NULL, source_key text NOT NULL, amount integer NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_event_contributions ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_event_contributions FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_event_claims (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, edition_id uuid NOT NULL, reward_key text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_event_claims ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_event_claims FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_event_outbox (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type text NOT NULL, payload jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_event_outbox ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_event_outbox FROM anon, authenticated;

-- Production migration MUST add: precise foreign keys, unique idempotency constraints,
-- actor/tenant SELECT policies for exposed projections, per-table indexes,
-- audited service RPCs, scoped grants, backups and down/forward recovery plan.
COMMIT;
