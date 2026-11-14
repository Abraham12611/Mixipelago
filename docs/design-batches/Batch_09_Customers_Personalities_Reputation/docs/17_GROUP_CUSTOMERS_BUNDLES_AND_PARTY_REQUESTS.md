# 17 — Groups, Families and Multi-line Orders

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Later mode only
A group can request a *bundle* of drinks, but the group illustration should not simulate multiple independent customers without specifying distinct order lines. Use `groupId` plus 1–N `orderLine` entries with explicit `target`, `quantity` and `fulfilledCount`.

## Compatible with existing reducer
For each new merge output, locate the oldest eligible active **order** by `issuedTick` then `orderId`; inside that order, choose the oldest unfilled compatible line by stable `lineIndex` then ID. One output fills exactly one line unit. A group order completes only when **all** required lines meet quantity. If an earlier matching single-customer order exists, that order wins priority unless the published mode explicitly uses a different policy version.

## Resource budget
Tier-equivalent drink cost of bundles can rise exponentially. The level editor must evaluate aggregate availability after automatic serving consumes intermediate results. Optional group bonus objectives must not make required tutorial targets impossible. Group missions require recorded winning traces before publication.

## Presentation
On mobile collapse group members into a single customer card with line progress chips; tapping expands the full order list without covering the table. Show exactly which drink will auto-serve next. Use accessible quantities and names, never only icons.

## No accidental party monetization
No forced table-capacity purchases, paying to join a group, or surprise extra bundle requirement mid-session. Rewards live in authored policy and trusted result settlement. Group interactions remain future content until Batch 4's multi-line reducer is implemented and tested.
