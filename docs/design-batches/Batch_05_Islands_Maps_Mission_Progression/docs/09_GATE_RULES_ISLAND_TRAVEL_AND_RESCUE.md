# 09 — Island Unlocks, Travel, and Progression Rescue Policies

## Unlock policy
To enter a new island, clear the gateway's authored required milestone(s). Optional mastery stars may unlock decorative shortcuts but should not hard-block basic access without careful difficulty analysis. Exact gates belong in versioned campaign data, not `if level > 120` code.

## Travel experience
Selecting a gateway displays destination name, visual preview, unlock requirements and `Travel` action. The transition loads target bundle, verifies node content and moves camera to `spawnAnchor`. Persist the last visited island and node separately from the **recommended next mission**; users may browse a location without changing campaign progress.

## Rescue mechanics
The UI always offers `Find Next Mission`, which finds a reachable published node with a supported mission. If no node is available, distinguish among: campaign complete; content not downloaded; next chapter unpublished; corrupted local save; retired mission; manifest mismatch; blocked prerequisites. Each gets a specific message and action.

## Never strand a player
A graph publication preflight must find a feasible path through critical content. Optional secrets, closed shops and expired events cannot be the only bridge. If a published mission is retired, provide a replacement edge/mission or recognize existing clear receipts and keep traversal available.

## Returning players
A player may return after six months. Show a short "Welcome back" progress summary and allow resuming from the last playable mission or opening the map. No forced recap of every unlocked feature; use optional archive summaries.

## Partial/unsupported content
If `v0.2.0` only includes Coconut Cove, other islands can appear as far-off art silhouettes without interactive false promises. Don't create unfinishable named missions for future releases. Content status `draft|preview|published|retired` governs render and interaction policy.

## Backend trust transition
Before verified accounts, gate locally from `mixipelago:save:v1` projected progress. After trusted accounts, server enforces new-island entitlement. Client pathfinding or tampered local save must never grant server assets or wallet prizes. Travel UI state is optimistic only for nonvaluable transitions.
