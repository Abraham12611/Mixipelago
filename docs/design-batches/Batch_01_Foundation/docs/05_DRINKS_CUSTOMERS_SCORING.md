# 05 — Drink Catalog, Customers, Orders, Scores and Game Session

## 1. Core design

A mission is a short-lived game session with a tabletop, spawn queue, customer demands, goals and a win/loss condition. Drink tiers are **tier IDs**, not arbitrary artwork strings. Art themes, names and scoring are separate data. User-provided screenshots suggest a simple sequential evolution ladder; its exact real-game recipes aren't verified. We will create our own.

## 2. Proposed initial 8-tier evolution chain

| Tier | Working name | Example art treatment | Base merge score |
|---|---|---|---:|
| 1 | Citrus Shot | Small iced orange juice | 10 |
| 2 | Sunny Lemon | Golden citrus cup | 25 |
| 3 | Sunset Splash | Orange-to-pink tumbler | 60 |
| 4 | Blossom Fizz | Pink floral cooler | 140 |
| 5 | Coral Martini | Red cocktail coupe | 320 |
| 6 | Mint Lagoon | Mint/lime margarita | 720 |
| 7 | Ocean Cloud | Blue tall glass with soft foam | 1,600 |
| 8 | Crown of the Isles | Decorative tropical signature drink | 3,500 |

Names, art, scores and colors are **provisional**; final art may differ. v0.1 drinks are one chain, two items of tier N produce one of N+1 (N<8). Don't introduce branching recipes until designers approve clear UI representation.

## 3. Spawn queue

- Use seeded pseudorandom sequence for testable sessions.
- For alpha, spawn tiers 1 and occasionally 2 based on weighted, level-specific rules; reveal exactly the next item.
- Prevent a spawn directly on top of active bodies or beyond launch bounds.
- The RNG and queue are owned by session logic, not `Math.random` calls in rendering.
- For early sessions, ensure first 3–5 shots teach a guaranteed valid merge sequence and an order completion.
- Spawns must always be finite and feasible for their level goal; avoid unwinnable sequences introduced by arbitrary weighting.

## 4. Customers and orders

Two simultaneous orders for alpha. A customer card has `{orderId, customerVisualId, requestedTierId, requestedCount, servedCount, coinReward, createdAtStep, expiresAt?}`. No expiration by default in v0.1. For a customer that requests tier 3 quantity 2: serve 2 eligible tier-3 outputs separately, then fulfill order and award coins exactly once.

**Alpha serving rule:** auto-serve an *eligible newly produced* drink that matches a pending order. If several orders qualify, select oldest active order. Show brief visual transfer/confirmation (150–250 ms) then remove drink. Do not retroactively auto-serve all idle board drinks unless later approved; otherwise players cannot plan merges. Initial order sequence must be curated to align with available tiers.

When a customer is fulfilled: `order_fulfilled` generates score bonus and **preview** coins, triggers SFX/FX, increments session objective count, and optionally replaces order with next generated order. No paid customer impatience or rich-customer probability in the alpha.

Customer characters are visual personas and order sources; dialogues, preferences, VIP behavior and relationship state are future modules.

## 5. Scoring (proposed)

- Every successful merge: tier-based score from table above.
- Consecutive merges within a designer-defined window increment combo level up to capped multiplier; alpha can use simple max 3x.
- Fulfilled order: `orderBonus = coinReward * 10` score points, *once* per order.
- Example: tier 2 + tier 2→tier 3 grants 60 score; if this immediately completes an order worth 15 coins, add 150 bonus and 15 preview coins.
- Never award points for merely launching or for physical collisions without merges.
- Score uses bounded safe integers, not floating-point wallet calculations. Cap combinatorial overflow and reject NaN.

Illustrative calculator:

```ts
function mergePoints(tier: number, combo: number, scores: number[]) {
  const base = scores[tier - 1] ?? 0;
  return Math.round(base * Math.min(3, 1 + 0.25 * Math.max(0, combo - 1)));
}
```

All scores are designer-tunable. The exact score formula is not a historical claim about Merge Shooter.

## 6. Round goals and difficulty

Level JSON controls `goalType` (`orders_served`, `target_score`, future `produce_tier`, `limited_shots`), `goalValue`, allowed spawn tiers, starting board, maxDrinks, dangerLine, friction preset, starting orders, next-order queue and reward tables. First alpha includes one mission; first week may include 3–10 curated missions that reuse the same engine.

Proposed ramp:
- Mission 1: teach matching; 1 required order; plenty of space.
- Mission 2: second order, different tiers; launch angle matters.
- Mission 3: introduce board pressure and danger line.
- Mission 4: chain reaction opportunity.
- Mission 5: slightly faster/complex order sequence.

## 7. State transitions and transaction ordering

After `drink_merged`: increment merge counters → calculate score → evaluate order match → apply order progress → award fulfilled order once → evaluate win goal → if win, stop further session mutations → record summary and local preview progression. All mutations occur in one serial reducer to avoid asynchronous UI callbacks awarding the same transaction twice.

`SessionSummary` includes `sessionId`, `missionId`, `status`, `score`, `ordersServed`, `merges`, `shots`, `previewCoinsEarned`, `bestCombo`, `durationMs`, `physicsVersion`, `contentVersion`.

## 8. Game result and saved progression

On win, show result overlay: completed objective, score, best score, earned preview coins, replay, next. On fail, show reason and retry; no destructive penalty. Local storage can record `bestScoreByMission`, `unlockedMissionIds`, `totalPreviewCoins`, `settings`, `tutorialCompleted`, all with versioned schema.

If a player clears storage or switches browsers, local-only progress may disappear. We must communicate this before claiming cross-device save. Server accounts and durable economy are later milestones.

## 9. Future expansion hooks (overview only)

- Multiple recipe branches and collectible rare drinks.
- Customer segments, loyalty, VIP requests and dynamic order weighting.
- Boosters: wildcard, swap, blast, magnet, spawn modifier; all with separate balance rules.
- Weather/incident rule modifiers and missions with obstacles.
- Special tournament modes with fixed seed and standardized perks.

Do not implement these as hidden alpha mechanics. Define extension interfaces and create content docs after the core loop has been tested.
