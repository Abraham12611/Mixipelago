# 03 — Customer Definition, Instance, Encounter and Lifecycle

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Identity rules
Every content customer has a stable `customerId` (`guest.mira.surf-guide`) and `catalogVersion`. A generic procedural visitor uses a stable archetype definition plus an encounter-scoped `encounterId`; avoid pretending every procedural portrait is a unique persistent person. Display names can localize or change without altering stable IDs. Recurring named characters must be authored, consented to in the lore, and versioned; no user-derived names are generated from private data.

## Encounter state machine
`candidate -> reserved -> presented -> order_active -> fulfilled | expired | canceled -> finalized`. `reserved` means the server committed the selection so browser refresh cannot reroll for a better reward. `presented` means the client received its display payload. `finalized` means the verified run/encounter outcome was settled; canceled tutorial sessions never imply a negative reputation mark.

## Data contract
```
CustomerEncounter {
  encounterId, playerId, shopId, sourceRunId?, sourceMissionId?,
  customerId, segmentId, selectionPoolVersion, rngCommitment,
  status, createdAt, expiresAt?, finalizedAt?, resultReceiptId?
}
```
`playerId` and `shopId` come from authenticated context or verified session claims, **not** arbitrary incoming client fields. Encounter source IDs have a uniqueness rule. An encounter can have more than one order in later modes, but each order must be authored and independently counted.

## Lifecycle invariants
- A browser reload displays the already reserved encounter rather than sampling a new one.
- `fulfilled` refers to the session order reducer's state; do not mark a server encounter fulfilled until its receipt is verified.
- Replaced customers in a completed session are queued for a *future tick*, never retroactively used to consume a merge output.
- A mission that has terminalized cannot create a new encounter or customer order.
- Retired content preserves historic name, asset fallback and result links without letting that retirement repeat a first-clear reward.

## Test scenarios
A delayed `reserveEncounter` response and second request must share the same encounter ID. Concurrent mobile and desktop requests should use the same eligible pending encounter. A rejected run must create no trusted loyalty, reward or shop reputation mutation.
