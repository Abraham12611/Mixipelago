-- Mixipelago Batch 14: ILLUSTRATIVE SCHEMA ONLY.
-- NOT a production migration. Requires security and SQL review, FK design, RLS policies, and replay/settlement tests.
-- All player-facing mutations must go through authenticated backend commands and durable audit.
BEGIN;
-- pgcrypto / gen_random_uuid() availability must be checked on target Postgres version.
CREATE TABLE IF NOT EXISTS game_friend_edges (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  left_player uuid NOT NULL, right_player uuid NOT NULL, state text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_friend_edges ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_friend_edges FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_friend_requests (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  sender_id uuid NOT NULL, receiver_id uuid NOT NULL, status text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_friend_requests ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_friend_requests FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_block_edges (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  blocker_id uuid NOT NULL, blocked_id uuid NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_block_edges ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_block_edges FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_crew_memberships (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  crew_id uuid NOT NULL, player_id uuid NOT NULL, role text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_crew_memberships ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_crew_memberships FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_crew_projects (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  crew_id uuid NOT NULL, project_key text NOT NULL, goal bigint NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_crew_projects ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_crew_projects FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_contribution_receipts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  crew_id uuid NOT NULL, player_id uuid NOT NULL, source_key text NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_contribution_receipts ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_contribution_receipts FROM anon, authenticated;

CREATE TABLE IF NOT EXISTS game_social_outbox (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type text NOT NULL, payload jsonb NOT NULL,
  revision integer NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE game_social_outbox ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON TABLE game_social_outbox FROM anon, authenticated;

-- Production migration MUST add: precise foreign keys, unique idempotency constraints,
-- actor/tenant SELECT policies for exposed projections, per-table indexes,
-- audited service RPCs, scoped grants, backups and down/forward recovery plan.
COMMIT;
