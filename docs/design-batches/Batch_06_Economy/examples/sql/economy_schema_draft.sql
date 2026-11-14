-- Draft schema to guide review only. Not a production migration.
-- Requires pre-existing auth identity references, migrations, RLS policies and role grants.
CREATE TABLE wallets (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, currency text NOT NULL DEFAULT 'COINS',
  balance bigint NOT NULL DEFAULT 0 CHECK (balance >= 0),
  revision bigint NOT NULL DEFAULT 0,
  UNIQUE(player_id,currency)
);
CREATE TABLE wallet_ledger (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, wallet_id uuid NOT NULL REFERENCES wallets(id),
  delta bigint NOT NULL CHECK(delta <> 0),
  source_kind text NOT NULL, source_id text NOT NULL,
  economy_rules_version text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(player_id,source_kind,source_id)
);
CREATE TABLE economy_commands (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, request_key uuid NOT NULL, fingerprint text NOT NULL,
  command_kind text NOT NULL, result jsonb, state text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(player_id,request_key)
);
CREATE TABLE player_shops (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_id uuid NOT NULL, location_id text NOT NULL, shop_archetype_id text NOT NULL,
  operating_status text NOT NULL DEFAULT 'operational'
);
CREATE TABLE owned_shop_upgrades (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  player_shop_id uuid NOT NULL REFERENCES player_shops(id),
  upgrade_id text NOT NULL, level integer NOT NULL CHECK(level > 0),
  purchase_receipt_id uuid NOT NULL, UNIQUE(player_shop_id,upgrade_id,level)
);
CREATE TABLE economy_outbox (
  event_id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  topic text NOT NULL, payload jsonb NOT NULL, created_at timestamptz NOT NULL DEFAULT now(),
  published_at timestamptz
);
-- TODO: grants/RLS policies, refund rules, cross-table uniqueness, trusted receipt foreign keys,
-- transactional SQL functions and idempotent DB implementation are required before deployment.
