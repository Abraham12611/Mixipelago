-- MIXIPELAGO BATCH 09: ILLUSTRATIVE DRAFT ONLY -- DO NOT APPLY AS A PRODUCTION MIGRATION.
-- Real migrations require existing auth/profile/shop FK reconciliation, RLS review, security-definer audit,
-- verified result issuance, dedicated roles, and review with Batch 6/7/8 schema owners.
CREATE TABLE IF NOT EXISTS customer_catalog_versions (
  catalog_version text PRIMARY KEY,
  content_hash text NOT NULL UNIQUE,
  status text NOT NULL CHECK (status IN ('draft','validated','published','retired')),
  published_at timestamptz
);
CREATE TABLE IF NOT EXISTS customer_encounters (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL,
  shop_id uuid NOT NULL,
  encounter_source_id text NOT NULL,
  customer_id text NOT NULL,
  pool_id text NOT NULL,
  pool_version integer NOT NULL,
  catalog_version text NOT NULL REFERENCES customer_catalog_versions(catalog_version),
  status text NOT NULL CHECK (status IN ('reserved','presented','fulfilled','expired','canceled','finalized')),
  source_run_id text,
  verified_result_receipt_id text,
  created_at timestamptz NOT NULL DEFAULT now(),
  finalized_at timestamptz,
  UNIQUE (player_id,shop_id,encounter_source_id)
);
CREATE TABLE IF NOT EXISTS customer_service_observations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL,
  shop_id uuid NOT NULL,
  encounter_id uuid NOT NULL REFERENCES customer_encounters(id),
  verified_result_receipt_id text NOT NULL,
  satisfaction_policy_version text NOT NULL,
  satisfaction_score integer NOT NULL CHECK (satisfaction_score BETWEEN 0 AND 10000),
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (player_id,verified_result_receipt_id,encounter_id,satisfaction_policy_version)
);
CREATE TABLE IF NOT EXISTS customer_relationships (
  player_id uuid NOT NULL,
  shop_id uuid NOT NULL,
  customer_id text NOT NULL,
  points integer NOT NULL DEFAULT 0 CHECK (points >= 0),
  tier text NOT NULL DEFAULT 'stranger',
  revision bigint NOT NULL DEFAULT 0,
  PRIMARY KEY (player_id,shop_id,customer_id)
);
CREATE TABLE IF NOT EXISTS customer_relationship_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL,
  shop_id uuid NOT NULL,
  customer_id text NOT NULL,
  source_encounter_id uuid NOT NULL REFERENCES customer_encounters(id),
  points_delta integer NOT NULL,
  policy_version text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (player_id,shop_id,customer_id,source_encounter_id)
);
CREATE TABLE IF NOT EXISTS customer_reputation_observations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  shop_id uuid NOT NULL,
  source_observation_id uuid NOT NULL REFERENCES customer_service_observations(id),
  reputation_delta integer NOT NULL CHECK (reputation_delta BETWEEN -30 AND 30),
  policy_version text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (shop_id,source_observation_id,policy_version)
);
-- DO NOT GRANT browser clients mutation privileges on these tables.
-- RLS policies and FK to preexisting shops/auth tables are intentionally NOT supplied here.
-- Integrate with Batch 6 shop reputation and the shared trusted outbox, do not create a second wallet.
