-- Mixipelago Batch 11: ILLUSTRATIVE SCHEMA ONLY.
-- NOT a production migration. Requires security and SQL review, FK design, RLS policies, and replay/settlement tests.
-- All player-facing mutations must go through authenticated backend commands and durable audit.
BEGIN;
-- pgcrypto / gen_random_uuid() availability must be checked on target Postgres version.
CREATE TABLE IF NOT EXISTS game_narrative_editions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  content_hash text NOT NULL, edition text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_narrative_editions ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_narrative_editions FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_narrative_scenes (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  edition_id uuid NOT NULL, scene_key text NOT NULL, scene_json jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_narrative_scenes ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_narrative_scenes FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_player_story_flags (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, flag_key text NOT NULL, flag_value text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_player_story_flags ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_player_story_flags FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_player_quests (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, quest_key text NOT NULL, state text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_player_quests ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_player_quests FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_choice_receipts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, scene_key text NOT NULL, choice_key text NOT NULL, source_key text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_choice_receipts ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_choice_receipts FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_story_outbox (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type text NOT NULL, payload jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_story_outbox ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_story_outbox FROM anon, authenticated;

-- Production migration MUST add: precise foreign keys, unique idempotency constraints,
-- actor/tenant SELECT policies for exposed projections, per-table indexes,
-- audited service RPCs, scoped grants, backups and down/forward recovery plan.
COMMIT;
