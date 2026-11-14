# 29 — TypeScript Domain Types, Public API and Campaign Events

## Domain contracts (illustrative, additive to Batch 4)
```ts
type NodeType = 'mission'|'checkpoint'|'treasure'|'gateway'|'discovery'|'shop'|'event'|'landmark';
type PublicationStatus = 'draft'|'staged'|'published'|'retired';
type UnlockExpr =
  | {op:'always'}
  | {op:'missionCleared'; missionId:string; minStars?:1|2|3}
  | {op:'minStars'; missionIds:string[]; count:number}
  | {op:'nodeClaimed'; nodeId:string}
  | {op:'flagEquals'; flagId:string; value:boolean|string}
  | {op:'allOf'|'anyOf'; rules:UnlockExpr[]};
interface MissionRef {missionId:string; missionVersion:string; contentHash?:string}
interface CampaignNode {
  nodeId:string; islandId:string; chapterId:string; type:NodeType;
  status:PublicationStatus; position:{x:number;y:number};
  unlock:UnlockExpr; visibility:'visible'|'hidden'|'rumored';
  mission?:MissionRef; priority?:number; themeId?:string;
}
interface CampaignEdge { edgeId:string; from:string; to:string;
  kind:'route'|'shortcut'|'secret'|'gateway'|'scenic'; }
```
These are *interface sketches*; implement the authoritative version in a shared package with schema validators, type generation and version tags. Existing Batch 4 MissionDefinition stays independent.

## Client query endpoints (proposed for authenticated stage)
`GET /v1/campaign/manifest` returns active graph ID/hash, supported content versions and eligible island summaries. `GET /v1/campaign/islands/:islandId` returns authorized published graph projection (no hidden secrets unless revealed). `GET /v1/campaign/progress` returns best-result projection and revision. `POST /v1/campaign/claims` idempotently claims eligible treasure. `POST /v1/campaign/travel` validates gateway and records last visited island. These endpoints are future contracts, not required in preview-local alpha.

## Trusted writes
Mission completion is not submitted as `POST /campaign/mark-complete`; it is derived from the existing Batch 4 verified session pipeline. Treasure claims require a unique `claimId`/idempotency key. Server must re-evaluate requirement state and enforce caller identity.

## Canonical events
`campaign.mission_cleared.v1`, `campaign.best_stars_improved.v1`, `campaign.node_unlocked.v1`, `campaign.route_revealed.v1`, `campaign.treasure_claimed.v1`, `campaign.island_entered.v1`. Common envelope: `eventId`, `playerId`/preview identity, `occurredAt`, `graphVersion`, `sourceReceiptId?`, `payload`. Events are facts for presentation and analytics; **their receipt/transaction is the authority**.

## Projection algorithm
```ts
function deriveProjection(graph: Graph, progress: Progress): Projection {
  const completed = buildMissionResultIndex(progress);
  return graph.nodes.map(node => {
    const canUnlock = evaluateRule(node.unlock, completed, progress.flags);
    const visible = evaluateVisibility(node, progress);
    return {nodeId:node.nodeId, visible, eligible:canUnlock && node.status==='published'};
  });
}
```
This is deliberately skeletal; production adds explainability, trust gating, version checks, claim state and node-type behavior.

## API failure contracts
`CONTENT_VERSION_MISMATCH`, `MISSION_UNPUBLISHED`, `REQUIREMENT_NOT_MET`, `CLAIM_ALREADY_COMPLETED`, `UNAUTHORIZED`, `UNSUPPORTED_FEATURE`, `OFFLINE_REQUIRES_SYNC`; return stable machine codes plus localized UI action. No leaked hidden-mission identifiers in unauthorized errors.
