# 41 — Architecture Decisions, Trade-offs and Open Questions

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Decisions carried forward
1. Customers are separate from physics and scoring; no customer behavior creates merge events.
2. Orders auto-serve only **new merged outputs** and prioritize oldest eligible active order.
3. `coconut-cove-001` uses two scripted visible orders and two-order win; the first dynamic guest pool does not alter it.
4. Reputation is distinct from prestige/player level and is Batch 6-owned.
5. Persistent satisfaction and relationships derive only from verified service receipts, not visual callbacks.
6. VIP chance uses published absolute bps bonuses and a global cap, disabled in fixed tutorial/ranked modes.
7. VIP/critic, patience and group orders are OFF until the game proves their feasibility and reward integrity.
8. Offline preview progress is not converted into trusted reward or relationship ownership.

## Deliberate proposals requiring owner approval
- Whether service on a lost-but-verified mission counts for reputation (default no).
- Exact satisfaction/reputation point curves and whether low reputation decreases selection eligibility (recommend avoid until modeled).
- Whether encounter reservations are per shop visit, per mission, or per accepted optional contract (recommend explicit `encounterSourceId` policy).
- Which two canonical characters represent the first island and what names to use (sample character IDs are placeholders).
- Whether returning guests can offer nonmonetary story choices before Batch 11 is fully designed.

## Key risks
Complex personalities may distract from physics, live reputation may create anxiety, VIP profitability may distort ranked fairness, and exploding NPC asset count may overwhelm mobile memory. Mitigate via fixed beginner mission, nonpunitive early reputation, gated VIP, shared animation state and per-island streaming.

## Escalation
Any proposed change to scored order behavior, drink tiers, payout formula, competitive normalization or mission clearance requires an ADR cross-reviewed by Batch 3/4/6 owners. Do not resolve by quietly updating the customer catalog alone.
