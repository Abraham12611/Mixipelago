# 05 — Ingredients, Pantry, Suppliers and Sourcing (Future Overview)

**Status:** Deferred. Batch 6 will own economic pricing, shop inventory and procurement; Batch 10 will own weather/supply incidents. Batch 3 defines only the *ingredient domain* and its relationship to recipe discovery.

## Core principle

Ordinary alpha merging should never require a player to buy lemons before a tier-2 drink can be created. That would break the immediate, uncomplicated puzzle loop. Ingredients are later unlockable content for optional crafting, contracts, event missions or shop simulation, not a hidden cost on every shot.

## Ingredient definition

`ingredientId`, localized name, type (`fruit`, `herb`, `syrup`, `base`, `garnish`, `ice`, `special`), icon, source islands, quality grade, optional tags, acquisition channels, trade flags, expiration policy if ever introduced, collection lore, and publication version.

Example ingredients: `citrus`, `mango`, `passion-fruit`, `hibiscus`, `mint`, `coconut`, `berry`, `ginger`, `sea-salt`. These are thematic building blocks, not claims about the actual chemical contents of the abstract evolution ladder. `Citrus Shot` could reference a citrus motif without consuming inventory.

## Two concepts that must remain separate

**Recipe description ingredients:** decorative metadata (a mocktail icon suggests mint/lime) used for art, taste and stories. No quantity is subtracted from inventory.

**Craftable ingredient resources:** inventory ledger quantities actually used by an explicit crafting action in a future mode. Only a server transaction can change the trusted inventory. Never infer consumption from a collision's visual effect.

## Optional pantry flow

Discover supply source → acquire ingredient via mission or shop → inspect pantry → select a recipe at crafting station → show exact cost and output probability/guarantee → confirm → server validates inventory and unlock conditions → atomic ingredient debit + output grant → recipe journal update. For a puzzle-only mode, pantry may be disabled while discovered recipe cards remain visible.

## Quality grades vs luck

Do not introduce covert probabilities that consume rare ingredients with no disclosure. If crafting is randomized, publish odds and pity/protection design before enabling, and do not combine monetized randomness with competitive advantage. Prefer deterministic crafting for ordinary recipes; keep chance-based collection rewards separate from ranked systems.

## Future balance considerations

Supplier restocks, shop inventory, purchases, tradability, inventory caps, expiration, refunds and insurance are outside Batch 3. Hard requirements for future integration: transaction idempotency, provenance, anti-duplication, offline reconciliation, and an accessible recipe cost preview. Content must define ingredient substitution explicitly rather than relying on arbitrary tag intersection.

## Proposed owner decisions

1. Is pantry a permanent optional side mode or central to some island missions?
2. Do ingredients expire? Strong recommendation: no expiry for ordinary collectibles.
3. Can player-to-player trading exist? Defer until fraud/abuse tooling is ready.
4. Are recipe experiments guaranteed outcomes? Prefer yes for baseline discovery.
