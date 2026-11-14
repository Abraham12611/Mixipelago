# 42 — Representative Player Journeys and Failure Recoveries

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Journey A — alpha scripted order
Open `coconut-cove-001` -> see two customer portraits and requested tiers -> launch tier-1 -> merge tier-2 -> SessionReducer finds oldest compatible order -> consuming result visibly serves guest -> order progress increments once -> fulfill second order -> win result shows score and **preview-only** coins. No trusted loyalty or reputation. Test duplicate merge and retry.

## Journey B — future recurring guest
Player owns a verified shop -> server reserves eligible returning named guest -> customer appears with pinned order -> player completes verified mission -> one observation and relationship source receipt committed -> loyalty points cross threshold -> guest journal displays tier change -> a Batch 8 souvenir becomes *claimable*, not automatically extra coin. Refresh/retry must not double credit.

## Journey C — VIP offer
A qualified player with a published VIP pool gets a reserved candidate under capped probability -> sees order requirements, time conditions and reward policy -> may accept or decline -> if accepted, a published mission variant is loaded; if completed and verified, Batch 6 processes payout. Decline has no reputation penalty; refresh never rerolls VIP into a new candidate.

## Journey D — outage after commit
Run verifier accepts service; DB transaction commits reputation receipt; network response times out. Client shows `Pending`. Retry fetches the existing source receipt with the same `observationId` and projected value; no double reputation or wallet grant.

## Journey E — low bandwidth mobile
Portrait fails to load. Order card still displays drink name, tier, quantity and preview reward. Merge mechanics proceed and customer display uses silhouette fallback. On reconnect the portrait can appear, but cannot change the pending order or encounter result.

## Journey F — overlapping event modes
An optional festival changes region guest pool eligibility mid-week. Already reserved customers remain unchanged; new reservations use the new published pool after version check. Invalid recipe targets cause publication rejection, not forced session loss.
