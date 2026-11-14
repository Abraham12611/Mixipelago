-- Mixipelago Batch 7 SAMPLE DDL. Not a production migration.
-- Requires project-specific auth user table, RLS, privileges, entitlement verification,
-- trusted transaction functions, idempotency conflict hashing and outbox implementation.
CREATE TABLE IF NOT EXISTS player_progression (
 player_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
 xp_total BIGINT NOT NULL DEFAULT 0 CHECK (xp_total >= 0),
 player_level INT NOT NULL DEFAULT 1 CHECK (player_level >= 1),
 earned_points INT NOT NULL DEFAULT 0 CHECK (earned_points >= 0),
 allocated_points INT NOT NULL DEFAULT 0 CHECK (allocated_points >= 0 AND allocated_points <= earned_points),
 revision BIGINT NOT NULL DEFAULT 0,
 xp_policy_version TEXT NOT NULL,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS player_xp_grants (
 id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
 player_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
 source_type TEXT NOT NULL, source_id TEXT NOT NULL,
 policy_version TEXT NOT NULL, amount BIGINT NOT NULL CHECK (amount > 0),
 idempotency_key TEXT NOT NULL, request_hash TEXT NOT NULL,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE (player_id, source_type, source_id),
 UNIQUE (player_id, idempotency_key)
);
CREATE INDEX IF NOT EXISTS player_xp_grants_recent_idx ON player_xp_grants(player_id, created_at DESC);
CREATE TABLE IF NOT EXISTS player_level_milestones (
 player_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
 reached_level INT NOT NULL CHECK (reached_level >= 2),
 points_granted INT NOT NULL DEFAULT 1 CHECK (points_granted >= 0),
 attained_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY (player_id, reached_level)
);
CREATE TABLE IF NOT EXISTS player_skill_allocations (
 player_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
 skill_id TEXT NOT NULL, rank INT NOT NULL CHECK (rank >= 1),
 catalog_version TEXT NOT NULL, updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY (player_id, skill_id)
);
CREATE TABLE IF NOT EXISTS player_skill_events (
 id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
 player_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
 operation_type TEXT NOT NULL, skill_id TEXT,
 previous_rank INT, new_rank INT, points_delta INT NOT NULL,
 request_id TEXT NOT NULL, catalog_version TEXT NOT NULL,
 occurred_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE (player_id, request_id)
);
CREATE TABLE IF NOT EXISTS player_skill_loadouts (
 player_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
 mode_family TEXT NOT NULL, slots JSONB NOT NULL DEFAULT '[]',
 revision BIGINT NOT NULL DEFAULT 0,
 PRIMARY KEY (player_id, mode_family)
);
ALTER TABLE player_progression ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_xp_grants ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_level_milestones ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_skill_allocations ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_skill_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE player_skill_loadouts ENABLE ROW LEVEL SECURITY;
CREATE POLICY progression_select_own ON player_progression FOR SELECT TO authenticated USING (player_id = auth.uid());
CREATE POLICY xp_grants_select_own ON player_xp_grants FOR SELECT TO authenticated USING (player_id = auth.uid());
CREATE POLICY milestones_select_own ON player_level_milestones FOR SELECT TO authenticated USING (player_id = auth.uid());
CREATE POLICY allocations_select_own ON player_skill_allocations FOR SELECT TO authenticated USING (player_id = auth.uid());
CREATE POLICY events_select_own ON player_skill_events FOR SELECT TO authenticated USING (player_id = auth.uid());
CREATE POLICY loadouts_select_own ON player_skill_loadouts FOR SELECT TO authenticated USING (player_id = auth.uid());
-- IMPORTANT: no authenticated client INSERT/UPDATE/DELETE policies: writes through
-- rigorously reviewed server-owned functions only, with authenticated identity checks.
