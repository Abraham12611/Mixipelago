# 23 — Shop & Economy UI/UX: Mobile and Desktop

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Screens
Shop overview, shop detail, upgrade catalog, upgrade detail/confirmation, compare before-after, economy wallet, transaction history, cosmetic inventory, decorate/edit shop, purchase success/error, and future franchise overview. Responsive layout uses one canonical information architecture, not squeezed desktop screenshots.

## Mobile detail
Top: shop name/location, visible balance, quick back. Center: large shop illustration with selectable decoration hotspots. Bottom: three tabs `Utility`, `Decor`, `Prestige`; scrollable cards show required level, cost, benefit, and ownership state. Sticky purchase control appears only after the upgrade detail sheet explains the effect. Respect safe areas and reduced motion.

## Desktop detail
Main 2.5D scene center-left; catalog and comparison panel right; wallet and shop metrics upper-right; transaction confirmation is explicit. Keyboard focus and semantic buttons remain in HTML overlay; game scene hotspots provide accessible alternative list.

## UI states
Loading, empty, no shop owned, locked upgrade, affordable, insufficient funds, stale catalog, pending request, confirmed purchase, already owned, equip, conflict, offline, expired session, and rollback recovery. Avoid green success state until the server's receipt commits.

## Sample microcopy
- `VIP Seating I — Raises eligible VIP appearance chance by 2 percentage points (campaign only)`.
- `Golden Roof — Cosmetic only; does not increase earnings`.
- `You need 300 more coins. You can keep playing Coconut Cove missions.`
- `Purchase could not be confirmed. No coins were deducted.` (only after authoritative failure).

## Manual testing ownership
Engineers automate snapshot, accessibility, and contract tests. All subjective gameplay and manual UI approval are directed to the owner.
