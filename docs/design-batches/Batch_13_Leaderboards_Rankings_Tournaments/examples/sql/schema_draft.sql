-- Mixipelago Batch 13: ILLUSTRATIVE SCHEMA ONLY.
-- NOT a production migration. Requires security and SQL review, FK design, RLS policies, and replay/settlement tests.
-- All player-facing mutations must go through authenticated backend commands and durable audit.
BEGIN;
-- pgcrypto / gen_random_uuid() availability must be checked on target Postgres version.
CREATE TABLE IF NOT EXISTS game_competition_editions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  competition_key text NOT NULL, score_rules_hash text NOT NULL, starts_at timestamptz NOT NULL, ends_at timestamptz NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_competition_editions ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_competition_editions FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_score_submissions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, edition_id uuid NOT NULL, run_id uuid NOT NULL, trust_status text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_score_submissions ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_score_submissions FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_score_verifications (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  submission_id uuid NOT NULL, verdict text NOT NULL, replay_hash text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_score_verifications ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_score_verifications FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_player_best (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, edition_id uuid NOT NULL, score bigint NOT NULL, shots integer NOT NULL, active_ticks integer NOT NULL, verified_at timestamptz NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_player_best ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_player_best FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_frozen_standings (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  edition_id uuid NOT NULL, player_id uuid NOT NULL, rank integer NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_frozen_standings ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_frozen_standings FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_competition_outbox (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type text NOT NULL, payload jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_competition_outbox ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_competition_outbox FROM anon, authenticated;

-- Production migration MUST add: precise foreign keys, unique idempotency constraints,
-- actor/tenant SELECT policies for exposed projections, per-table indexes,
-- audited service RPCs, scoped grants, backups and down/forward recovery plan.
COMMIT;
