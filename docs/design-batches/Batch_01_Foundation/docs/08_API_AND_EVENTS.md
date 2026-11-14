# 08 — API, Domain Events, Save Sync and Transaction Contracts

## 1. Current versus future APIs

For `v0.1.0`, `GameShell` calls a **local adapter**, not a fake remote API. It provides `startSession`, `fireShot`, `pause`, `resume`, `completeRound`, `loadLocalProfile`, `saveLocalResult`. Server endpoints may be stubbed with interfaces but must not be represented as deployed.

Once server persistence launches, use `/api/v1` under the dedicated API gateway. User identity from verified access tokens, never from raw posted `playerId` claims. Define OpenAPI contracts from Zod schemas in `packages/domain-contracts` and generate a checked spec.

## 2. API proposal (future activation)

| Method | Route | Action | Trust note |
|---|---|---|---|
| GET | `/v1/me` | Profile/progress summary | Authenticated |
| PATCH | `/v1/me/settings` | Update preferences | Validated user-owned |
| GET | `/v1/content/manifest` | Published missions, assets, versions | Public/cacheable |
| GET | `/v1/missions/:id` | Retrieve mission definition | Published content only |
| POST | `/v1/sessions` | Create canonical session and seed | Server chooses rules |
| POST | `/v1/sessions/:id/complete` | Submit session outcome/input log | **Do not trust score** |
| GET | `/v1/progress` | Mission/island unlock status | User-owned read |
| GET | `/v1/wallet` | Authoritative coins | Server-derived |
| POST | `/v1/shops/:id/upgrades` | Purchase eligible upgrade | Idempotent transaction |
| GET | `/v1/leaderboards` | Verified rank list by scope/season | Public filtered |
| POST | `/v1/friends/requests` | Invite friend | Consent/rate limits |
| POST | `/v1/events/:id/choices` | Choose incident resolution | Eligibility server checked |

## 3. Consistent envelopes

Successful command example:

```json
{
  "data": {
    "sessionId": "run_abc",
    "status": "accepted",
    "pendingVerification": true
  },
  "requestId": "req_example",
  "schemaVersion": 1
}
```

Error example:

```json
{
  "error": {
    "code": "INSUFFICIENT_COINS",
    "message": "Not enough coins for this upgrade.",
    "retryable": false
  },
  "requestId": "req_example"
}
```

Business errors use stable codes (`UNAUTHENTICATED`, `NOT_OWNER`, `INVALID_MISSION_VERSION`, `CONFLICT`, `RATE_LIMITED`, `SESSION_ALREADY_COMPLETE`, `UNVERIFIED_SCORE`, `INSUFFICIENT_COINS`). Localize user messages in UI, not in backend.

## 4. Commands/events split

**Commands** request a mutation: `LaunchDrink`, `PauseSession`, `ResumeSession`, `PurchaseUpgrade`, `SelectEventChoice`. **Events** record facts after validation: `drink_launched`, `drink_merged`, `order_fulfilled`, `round_won`, `upgrade_purchased`, `reward_granted`. Events must be immutable payloads with versions, IDs and causation references.

```ts
type DomainEvent<TName extends string, TPayload> = {
  eventId: string;
  name: TName;
  schemaVersion: 1;
  sessionId?: string;
  aggregateId: string;
  sequence: number;
  occurredAt: string;
  payload: TPayload;
  causationId?: string;
};
```

For physics events, also include `simulationStep` and rule/content/physics versions. Event names must have one exact spelling across teams (use shared enum/constants, no arbitrary strings).

## 5. Typical cross-system flows

**Drink merge**  
Physics collider pair → MergeResolver approves → `drink_merged` → SessionReducer applies tier score → OrderEngine matches → `order_fulfilled` (possibly) → AudioDirector/FX display → game UI updates.

**Round rewards (later)**  
Session terminal state → submit input log/level hash → validation service verifies → transaction inserts `mission_results`, `reward_grants`, `wallet_ledger`, updates `wallets` & unlocks → transactional outbox event → leaderboard worker.

**Shop purchase (later)**  
Player selects upgrade → API checks auth/ownership/prerequisites → transaction reserves row, derives cost, debits wallet, inserts upgrade and ledger → publishes `upgrade_purchased` → UI invalidates cached profile/shop read model.

**Dynamic incident choice (later)**  
World director schedules event → event appears → user chooses → server checks active status and deadline → commits exactly one resolution → grants tasks/rewards/penalties → updates shop + world state.

## 6. Idempotency

All commands with durable side effects require `Idempotency-Key` and a unique constraint anchored to player/action. Retry with same key returns prior outcome. Never simply repeat a coin debit or prize grant after timeout. Browser requests use exponential backoff only for safe requests or idempotent commands; never replay an unsafe operation without the same key.

## 7. Offline/sync behavior

Alpha: fully local gameplay with best-effort browser persistence. Future synced play: local simulation continues, but **unverified rewards remain pending** until backend validation; if sync fails, keep event log and retry. Do not claim cross-device permanence until verified reconciliation is implemented. Never let client-local boosts or currency modify authoritative state by themselves.

## 8. Transport choices

HTTP/JSON for most interactions. WebSocket or managed realtime only for live duels or special crew features, not basic collisions. Server events/queue for workers, not a permanent physics loop per campaign player. Carefully budget event telemetry; sending all collision contacts over HTTP would be expensive and unnecessary.

## 9. Versioning rules

- Route `/v1` for major API contract stability.
- Content config `schemaVersion` independent of app SemVer.
- Simulation version + content hash attached to every ranked run.
- Keep compatibility readers for local save schema revisions.
- Publish event schema changes as new versions or backward-compatible additions.
