# 17 — Trusted Campaign Persistence, Database Schema and Security

## When this is needed
`v0.2.x` can launch with local-preview map state if trusted rewards are not available. Once account-backed progression and economy ship, the server becomes authoritative. This chapter defines the target backend without forcing it into the first map iteration.

## Proposed relational model
- `campaign_graph_versions(id, version, hash, status, published_at)` immutable content releases.
- `campaign_islands(id, graph_version_id, theme_id, initial_node_id, status)` catalog.
- `campaign_nodes(id, graph_version_id, island_id, type, mission_id, mission_version, unlock_rule_json, flags, status)` immutable release rows.
- `campaign_edges(id, graph_version_id, from_node_id, to_node_id, type, display_order, reveal_rule_json)`.
- `player_mission_results(player_id, mission_id, score_profile_hash, best_stars, best_score, best_shots, best_ticks, verified_receipt_id, updated_at)`.
- `player_discoveries(player_id, discovery_id, trusted_receipt_id, discovered_at)`.
- `player_node_claims(player_id, node_id, reward_grant_key, claimed_at)` unique `(player_id,node_id)` where one-time.
- `player_campaign_state(player_id, active_island_id, selected_node_id, revision)` for UI convenience only; not authoritative unlocks.
- `progress_receipts(id, player_id, run_id, mission_id, mission_version, proof_status, created_at)` immutable audit.

## Critical transaction
On verified session win: lock unique `run_id`/receipt; ensure no prior grant; upsert monotonic mission bests; record first-clear if applicable; enqueue projection/notification; grant any eligible durable economy reward through ledger **once**. Publishing a new graph does not rewrite old receipts.

## API authorization
Use the authenticated session identity, never a user ID supplied freely by the browser. Admin publish methods are server-only with separate roles. In Supabase, enforce grants and RLS on any exposed tables; service-role/secret key stays on server. Prefer a dedicated Fastify service for verified mutations; no client direct updates of scores/stars/claims.

## Isolation and concurrency
A transaction must prevent two simultaneous results from both claiming first-clear rewards. Unique indexes on `(player_id, run_id)` and durable idempotency keys; monotonic updates with `GREATEST`, carefully tracking best score under matching score rules. If score formula changed, separate score profiles.

## Indexing
Indexes for `(player_id,mission_id)`, `(player_id,updated_at)`, graph version ID and island ID. Do not run entire graph joins on every camera pan; cache authorized progression projection by `(playerId,graphVersion,progressRevision)`.

## Security tests
Foreign player result update denied; unauthenticated reward claim denied; duplicate run accepted only as idempotent repeat; retired mission start refused; client preview coin ignored; stale graph revision handled with safe retry; read-only public catalog excludes unannounced secrets.
