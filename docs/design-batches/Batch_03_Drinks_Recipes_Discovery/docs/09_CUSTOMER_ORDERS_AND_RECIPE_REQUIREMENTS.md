# 09 — Orders, Serving Rules, Variant Matching and Customer Integration

## Alpha contract (do not change)

The tabletop shows **two active orders**. Each requests a canonical tier (`requestedTier`) and quantity. When a compatible *newly merged output* is created, the SessionReducer automatically reserves it for the **oldest eligible active order**. Tie-break by order ID. Serving produces a short transfer animation, updates progress and removes the drink. Completing the order awards preview coins and score **once**.

A resting identical drink already on the board is *not* retroactively swept up for serving. A launch preview is not a body and cannot satisfy an order. A merge result cannot both serve and chain-merge. These decisions come from Batch 1/2.

## Transaction sequence

1. `MergeArbiter` commits `mergeId`, `outputObjectId`, `outputDrinkId/tier`, pose and chain ancestry.
2. The reducer increments unique merge counters and calculates output-tier base score + bounded combo.
3. It searches active orders in stable oldest-first order for `requestedTier===outputTier` and remaining quantity.
4. If a match exists, mark output `serve_claimed` **before** any next-step chain activation; record one `order_line_progressed` with source `mergeId` and unique service claim ID.
5. Increment served quantity; if complete, mark order `fulfilled` and emit exactly one `order_fulfilled` with configured preview coin reward and order score bonus.
6. Spawn replacement order only according to mission config and terminal-state rules; victory evaluation occurs before unsolicited new orders.
7. Presentation animates transfer, customer acknowledgment, HUD counters, and SFX from read-only semantic events.

## Specific example

Order A (created first): 1 × tier-3 Sunset Splash for 15 preview coins. Order B: 2 × tier-3 Sunset Splash for 25 preview coins. First new tier-3 satisfies A and pays 15 when A is completed. Second and third tier-3 results increment B; its 25 coins pay only on the third result. The same output may not satisfy both A and B.

## Future target requirement schema

`Target = { drinkId?: string; familyId?: string; tier?: number; variantId?: string; tagsAll?: string[]; quantity: number; minimumQuality?: string; matchPolicy: 'exact'|'tier-in-family'|'eligible-variant' }`.

Never use all these fields in v0.1. In later recipe modes, precedence must be explicit: exact drink match > family+tier match > compatible variant; broad tag orders must be constrained and visibly explained. An order cannot request an undiscovered secret without an accessible unlock route or explicit event challenge.

## Customer vs recipe responsibilities

Order generator chooses valid requests. Catalog validates that each request target exists. Spawn director controls available input stream. Merge resolver generates outputs. Order matcher consumes matching outputs. Reward service records fulfilled orders. Customer character portraits, dialog and tip animations are visual consumers. No customer avatar should invoke a physics world mutation.

## Difficulty and feasibility

A naive tier-7 customer request can require 64 tier-1 inputs from scratch, with consumption of intermediate tier output by other orders making it even harder. Before publishing a mission, evaluate a conservative lower bound for required inputs and prove representative seed/queue fixtures. Order replacement pools must be restricted by allowed tier and mission budget. If a mission needs higher-tier orders, seed appropriate bodies or a queue that supports them.

## Future orders

VIP orders, multi-drink bundles, timed patience, recurring guest loyalty, tips and regional flavor preferences belong to customer design in Batch 9. Recipe branches can eventually satisfy named drink requests. But no customer generator should request a recipe rule disabled by the current session catalog hash.

## Acceptance cases

- Duplicate merge event => no duplicate serving.
- Two same-tier orders => oldest gets first result.
- Two outputs in same step => stable input event order, deterministic order progress.
- Serving an output => no subsequent chain merge from that output.
- Win condition reached => no replacement orders after terminal transition.
- Lost/abandoned run => no preview rewards committed as trusted money.
- Art variant on output => same alpha tier order matching if gameplay identity is unchanged.
