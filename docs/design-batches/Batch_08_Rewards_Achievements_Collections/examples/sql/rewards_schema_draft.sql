-- MIXIPELAGO BATCH 8: ILLUSTRATIVE SCHEMA SKETCH ONLY.
-- Do NOT apply directly to production: missing RLS, users FKs, policies,
-- authenticated issuer enforcement, migration locks and audit tooling.
CREATE TABLE reward_entitlements_draft (
  id uuid PRIMARY KEY,
  player_id uuid NOT NULL,
  program_id text NOT NULL,
  source_scope text NOT NULL,
  source_id text NOT NULL,
  reward_stage text NOT NULL,
  policy_id text NOT NULL,
  policy_version int NOT NULL,
  status text NOT NULL CHECK (status IN ('claimable','claiming','claimed','expired','revoked')),
  revision bigint NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now(),
  claimed_at timestamptz,
  UNIQUE (player_id,program_id,source_scope,source_id,reward_stage)
);
CREATE TABLE reward_claim_commands_draft (
  player_id uuid NOT NULL,
  request_key uuid NOT NULL,
  fingerprint text NOT NULL,
  entitlement_id uuid NOT NULL,
  receipt_id uuid,
  status text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (player_id,request_key)
);
CREATE TABLE reward_claim_receipts_draft (
  id uuid PRIMARY KEY,
  player_id uuid NOT NULL,
  entitlement_id uuid NOT NULL UNIQUE,
  source_id text NOT NULL,
  policy_id text NOT NULL,
  policy_version int NOT NULL,
  claimed_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE player_inventory_entitlements_draft (
  player_id uuid NOT NULL,
  item_id text NOT NULL,
  provenance_receipt_id uuid NOT NULL,
  acquired_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (player_id,item_id)
);
CREATE TABLE reward_consumer_inbox_draft (
  consumer_name text NOT NULL,
  event_id uuid NOT NULL,
  consumed_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (consumer_name,event_id)
);
-- Production design must preserve Batch 6 wallet ledger and Batch 7 XP tables.
