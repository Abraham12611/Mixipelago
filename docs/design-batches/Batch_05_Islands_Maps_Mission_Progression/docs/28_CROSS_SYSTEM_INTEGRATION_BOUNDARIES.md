# 28 — Integration Contracts With Earlier and Future Batches

## Earlier batches
**Batch 1:** retains existing initial web alpha and `mixipelago:save:v1`; map is additive, not a blocker for early release.
**Batch 2:** map uses no Rapier world; gameplay handoff uses stable mission ID and pinned physics config. Collision behavior remains unaffected.
**Batch 3:** drink evolution remains eight linear tiers for alpha; map does not unlock branched recipes by itself until discovery integration is explicitly released.
**Batch 4:** consumes `MissionResult`; preserves auto-service before chain continuation, v1 mission schema and `coconut-cove-001` two-order objective. Published mission schema is not rewritten to add map metadata.

## Future batches
**Batch 6:** shop ownership and economic upgrades can appear as `shop` landmarks; any spendable coin or upgrade receipt is server-authoritative. Do not make mandatory gates depend on a shop system until active.
**Batch 7:** skill unlock flags and mastery can be opt-in node gates only after the skill resolver is live; ranked modes normalize power.
**Batch 8:** treasure collections/achievements own entitlement definitions; map owns only claim locations.
**Batches 9–11:** customer stories, incidents and rivals add quests/flags; no map runtime needs built-in narrative AI.
**Batch 12:** event nodes are time-scoped, separate from permanent critical path.
**Batches 13–14:** competition and co-op use different progress/reward trust policies; global competitive scores never derive from local alpha preview.
**Batches 15–17:** design system, assets and audio can be updated independently through manifests.
**Batches 18–21:** admin content publishing, backend trust, analytics, native optimization and accessibility.

## Event bridge
`mission_result_verified` → `player_result_upserted` → `campaign_progress_recomputed` → `nodes_became_available`/`discovery_revealed` → optional `reward_entitlement_granted` → UI. In local preview, same *pure* progression reducer runs without durable grants.

## Contract tests
Pin example `coconut-cove-001` and `-002` mission refs. No implicit new missions in a graph. Ensure stars from Batch 4 map to gates without score recalculation; auto-serving unchanged; loading map doesn't step physics; server doesn't accept client preview wallet as real.
