# 07 — Rarity, Collections, Recipe Album and Prestige

**Status:** Planned extensions; alpha catalog is eight standard gameplay tiers with no collectible rarity power.

## Rarity is not the same as tier

A tier-8 drink is difficult to create because of evolution cost, not because it is automatically 'legendary.' `tier` controls evolution and order matching; `rarity` controls collection storytelling/acquisition availability and cosmetic prestige. Using the same field to do both would make balancing impossible once festival skins and event items arrive.

Proposed collection rarity labels: `common`, `uncommon`, `rare`, `epic`, `legendary`. These labels are design vocabulary only until acquisition rates and rewards are approved. Keep displayed color/pattern redundant with text and icon, for accessibility.

## Collection entry vs physical object

If a player merges a tier-6 drink in a normal mission, that *may* qualify as 'seen/created' for a collection milestone later, but it does not mean a permanent copy of the physical glass exists in their shop inventory. A run object is temporary. The collection tracks discovery evidence (`firstCreatedAt`, `countProduced`, `highestChain`, `bestMission`, version). Decorative skins are separate owned items and require trust validation.

## Proposed album hierarchy

**Core Drink Atlas** (all eight introductory tiers); **Island Signatures** (region-specific drinks after islands ship); **Seasonal Specials** (festival cosmetics); **Mastery Showcase** (records and mastery awards); **Hidden Recipes** (spoiler-aware recipe reveals). Each collection is a versioned content set containing entry IDs and reward milestone rules.

## Rewards and balancing

Collection milestone rewards can include profile frames, animated recipe-card borders, shop decals, title labels, album illustrations, island decorations, and capped modest resources. Avoid paid collection bottlenecks and 'finish before date or lose the ability forever' pressure. If a seasonal item rotates out, publish a sensible future path or mark it explicitly time-exclusive.

## User flow

Merge produces a drink → validated session results identify new produced tier → collection service evaluates 'first creation' idempotently → optional post-round notification → album highlights unseen entry → player opens entry → sees lore, recipe family, unlocked skins, production count, and source mission. For alpha, the UI may simply show the evolution strip with locked silhouettes; no permanent reward ledger until server validation exists.

## Set completion calculation

Collection progress = count of owned eligible entries / count of published eligible entries. Do not increase denominator mid-season without a deliberate collection version/notice; otherwise player progress visibly drops after an unrelated content publish. Milestone eligibility must be computed on a snapshot/version of the set; reward ledger enforces once-per-player per milestone.

## Duplicates and provenance

Owning one cosmetic skin can be a boolean grant; tradable duplicates (if ever supported) must have unique inventory IDs and audit trails. Never equate a client's `drink_merged` event with a trusted grant. Backend validates mission result or uses authoritative event sources. Bundle purchases and reward grants in database transactions.

## Edge cases

If an entry is retired, preserve its earned badge; if art is replaced, preserve owner unlock; if player switches languages, localize names without changing keys; if duplicate reward HTTP requests race, return same transaction result. Do not expose rare cosmetic ownership as a gameplay ranking advantage.

## QA coverage

Test collection cardinality across published revisions, acquired/revoked items, alternate skins, online/offline reconciliation, repeated awards, multiple devices, set completion after content retirement, untrusted client attempts, reduced-motion card reveals, and spoiler redaction.
