# 07 — Data Model and Persistence Strategy

## Principle

**Local alpha ≠ trusted backend.** v0.1.0 uses versioned local saves, with explicitly preview-only currency. When server-based play arrives, PostgreSQL becomes authoritative for economy, mission rewards, upgrades, social results and account-linked progression. Keep migration from local preview to real server state **opt-in and controlled**, never blindly credit manipulated `localStorage` coins to a real wallet.

## 1. Local alpha save

Store under `mixipelago:save:v1`; schema validate on read, treat parse failure as recoverable; keep an optional backup. Do not store full Rapier WASM objects or collider handles. Basic shape:

```ts
type LocalSaveV1 = {
  schemaVersion: 1;
  localPlayerId: string;
  createdAt: string;
  updatedAt: string;
  settings: {
    musicVolume: number; sfxVolume: number;
    reducedMotion: boolean; quality: 'auto'|'low'|'high';
    controlMode: 'drag'|'keyboard';
  };
  tutorialCompleted: boolean;
  unlockedMissionIds: string[];
  bestScoreByMission: Record<string, number>;
  previewCoins: number;
  lastContentVersion: string;
};
```

`localPlayerId` is random, anonymous, not a guaranteed recoverable account. Local score may be manipulated and must never enter ranked leaderboards without verification. If gameplay state snapshots are added, store world positions, velocities, spawn queue, RNG state, step index and content/physics version, then reconstruct physics; test validity before resume.

## 2. Planned persistent entities

| Table / entity | Important fields | Purpose / constraints |
|---|---|---|
| `profiles` | `id(auth.uid)`, `display_name`, `avatar_asset_id`, `created_at`, `status` | Public identity; moderated name; no exposed emails |
| `player_settings` | `player_id`, `preferences jsonb`, `updated_at` | Cross-device preferences |
| `player_progress` | `player_id`, `current_island_id`, `entrepreneur_xp`, `level`, `content_version` | Summary state; can be rebuilt where possible |
| `islands` | `island_id`, `slug`, `content_version`, `published` | Content registry |
| `missions` | `mission_id`, `island_id`, `config jsonb`, `schema_version`, `content_hash` | Versioned published mission catalog |
| `mission_results` | `id`, `player_id`, `mission_id`, `score`, `stars`, `verified`, `run_id` | Durable high scores and completion |
| `game_sessions` | `id`, `player_id`, `mission_id`, `seed`, `rules_version`, `content_hash`, `status`, `started_at`, `completed_at` | Replay/validation metadata |
| `session_events` | `session_id`, `sequence`, `kind`, `payload`, `step` | Optional replay/audit, bounded retention |
| `wallets` | `player_id`, `currency`, `balance`, `version` | Server summary of trusted currency |
| `wallet_ledger` | `entry_id`, `player_id`, `currency`, `delta`, `reason`, `idempotency_key`, `ref_id` | Immutable financial event records |
| `shops` | `id`, `owner_id`, `island_id`, `archetype`, `state`, `reputation`, `version` | Player-owned properties |
| `shop_upgrades` | `shop_id`, `upgrade_id`, `rank`, `purchased_at`, `purchase_id` | Upgrade ownership |
| `inventory_items` | `player_id`, `item_id`, `quantity`, `source` | Consumables/collectibles |
| `skills_unlocked` | `player_id`, `skill_id`, `rank`, `skill_tree_version` | RPG specialization |
| `world_events` | `id`, `player_id`, `event_type`, `status`, `started_at`, `expires_at`, `state jsonb` | Personalized incidents |
| `seasons` | `season_id`, `start_at`, `end_at`, `status`, `rules_hash` | Competitive season registry |
| `leaderboard_entries` | `season_id`, `board_type`, `player_id`, `verified_score`, `updated_at` | Verified rank source |
| `reward_grants` | `id`, `player_id`, `source`, `reference_id`, `payload`, `granted_at` | Idempotent grants, unique source/ref |
| `friend_requests` | `id`, `requester_id`, `addressee_id`, `status` | Social connections, no unsolicited precise location |
| `crews` / `crew_memberships` | `crew_id`, `player_id`, `role`, `joined_at` | Cooperative features (later) |
| `outbox_events` | `id`, `aggregate`, `type`, `payload`, `published_at` | Transactionally emitted async work |

Future-only tables are conceptual. Engineers should write migrations only for features being released.

## 3. Example PostgreSQL migration snippets (illustrative)

```sql
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null check (char_length(display_name) between 2 and 24),
  created_at timestamptz not null default now()
);

create table public.wallets (
  player_id uuid not null references public.profiles(id),
  currency text not null check (currency in ('COINS')),
  balance bigint not null default 0 check (balance >= 0),
  version bigint not null default 0,
  primary key (player_id, currency)
);

create table public.wallet_ledger (
  id uuid primary key default gen_random_uuid(),
  player_id uuid not null references public.profiles(id),
  currency text not null,
  delta bigint not null check (delta <> 0),
  reason text not null,
  idempotency_key text not null,
  reference_id text,
  created_at timestamptz not null default now(),
  unique (player_id, idempotency_key)
);
```

Balance updates and immutable ledger insert happen inside one transaction; **never** allow authenticated browser clients to modify `wallets` or `wallet_ledger` directly. Read-only projections can be exposed with carefully checked grants/RLS. Server service role stays server-side.

## 4. Planned relational invariants

- A player's trusted balance cannot be negative unless a separately modeled debt account permits it.
- A `reward_grants` reason/reference can be redeemed at most once per player.
- Mission result references existing published mission content hash/version.
- Shop purchases require ownership, unlocked island, valid upgrade prerequisite and balance.
- Skill points spent ≤ earned; respec rules versioned.
- A completed incident cannot transition back to pending without explicit admin recovery.
- Private location preference separate from public leaderboard location scope.
- Every client-visible update uses idempotency key and server-derived price/reward.

## 5. RLS and auth

Supabase RLS guards per-user reads. Exposed schema tables require explicit RLS, least-privilege grants, and restrictive policies as appropriate. Anonymous Supabase sign-in may support guest-to-account conversion, but is a **server rollout feature**, not P0 alpha. Anonymous Auth users use the authenticated role; policies must distinguish anonymous claims when relevant.

## 6. Migrations, content hashes, backwards compatibility

- Sequential migration filenames committed to repo and applied with environment-specific migration tooling.
- All shipped content uses immutable `content_hash` / `content_version` to make old sessions interpretable.
- Use additive schema migrations for deployed features and backfill data before dropping columns.
- Never silently modify a published mission while users have active verified runs; create a new content version.
- Rollback of application code must consider database compatibility and reward ledgers.

## 7. Data retention / deletion (future)

Provide user-initiated deletion and export where required, minimize raw session events, aggregate analytics when possible, and never store full precise coordinates unless explicit separate permission and genuine necessity. Account status and moderation details require restricted access.
