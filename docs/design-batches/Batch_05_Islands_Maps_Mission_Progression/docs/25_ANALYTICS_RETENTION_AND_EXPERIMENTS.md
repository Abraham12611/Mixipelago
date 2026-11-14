# 25 — Campaign Analytics, Funnels, Difficulty Signals and Experiments

## Questions to answer
Are players finding the next mission? Where do branches confuse them? Which unlock requirements produce abandonment? Which visual assets fail to load on actual phones? Does the first island map improve retention over a simple Next button?

## Event vocabulary (schema-versioned)
`map_opened`, `island_viewed`, `node_selected`, `node_start_requested`, `node_start_rejected`, `mission_clear_recorded`, `stars_best_improved`, `node_unlocked`, `route_revealed`, `treasure_claim_requested`, `treasure_claim_completed`, `gateway_travel_started`, `gateway_travel_completed`, `map_chunk_load_failed`, `next_mission_used`.

## Common properties
`anonymousSessionId/playerId` according to consent policy, `appVersion`, `graphVersion`, `mapLayoutVersion`, `islandId`, `chapterId`, `nodeId`, `missionId`, `nodeStateBefore`, `nodeStateAfter`, `sourceSurface` and performance timing where applicable. Never emit hidden route coordinates or unannounced secret details from public telemetry.

## Useful funnels
Game result → world map → next available mission selected → mission started → cleared. Compare mobile and desktop, new vs returning, and first-time vs established players. Other funnels: lock selected → requirement understood → prerequisite started; secret hint seen → reveal completed; gateway unlocked → new island entered.

## Guardrail metrics
First-clear rate, route navigation errors, time-to-next-play, unexpected locked nodes, abandoned sessions on map, content-download failure, mobile FPS and asset memory. A shiny world map that lowers return-to-game rate is a product regression.

## Experiments
Test first map onboarding, list-versus-map guidance, default camera focus and icon affordances using deterministic audience assignment; don't experiment with the same player's critical unlocking rules without migration and support. Feature flag cohorts must be logged and pinned where they affect receipts.

## Data retention
Minimize personal data, avoid precise geolocation, allow event schema evolution, and don't combine ranking location with map navigation analytics. Product analytics and authoritative progress are separate; losing telemetry must not lose mission completions.
