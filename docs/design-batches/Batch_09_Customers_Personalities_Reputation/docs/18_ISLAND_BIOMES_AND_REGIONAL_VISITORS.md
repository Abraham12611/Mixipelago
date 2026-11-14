# 18 — Island Regions, Visitor Pools and Cultural Presentation

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## World integration
Batch 5 owns island identities, nodes and public route graph. Batch 9 exposes `regionPoolId` and optional character localizations; it does not unlock islands or invent missions. A new island may feature distinct visitor clothes, props, order voice lines and recipe preferences. All differences should support readable gameplay, not use culture as an opaque difficulty penalty.

## Regional pool contract
```
RegionCustomerPool {
  regionId, poolVersion, eligibleCustomerIds,
  segmentWeights, requiredPublishedRecipeIds,
  fallbackCustomerId, minimumMissionVersion
}
```
All referenced assets and recipes must be published at the same release cut. Prefer fictional island identities over shallow stereotypes of real national or ethnic cultures. If using real language or culture references, request careful content review and respectful localization.

## Difficulty ownership
The published mission controls tier choices, order quantity and allowed segments. Customer region changes portrait presentation and eligible story flavor only; it cannot produce surprise unplayable high-tier drinks. For competitive mode, use one pinned pool and standardized profile regardless of player region or real-world location.

## Availability and fallback
If an island's hero portrait fails to load, use a clearly labeled neutral character silhouette. If the region pool is invalid, keep the previously validated catalog live and block publishing the broken revision; do not silently reroll against different weights.
