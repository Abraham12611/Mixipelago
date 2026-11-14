# 30 — Acceptance, Traceability, Definition of Done and Coordinator Handoff

## Requirement-to-test traceability

| Requirement | Owning docs | Tests | Alpha required? |
|---|---|---|---|
| Stable 8-tier catalog | 02,03,17 | DRK-001 | Yes |
| 2-to-1 same-tier merge | 03,04,11,32 | DRK-002..005 | Yes |
| No duplicated item consumption | 11,32, Batch 2 | DRK-006..008 | Yes |
| Auto-serve priority | 09,32 | DRK-009..012 | Yes |
| Queue stable/rejected launch | 10, Batch 2 | DRK-013..014 | Yes |
| Visual/collider separation | 11,13 | DRK-015..016 | Yes |
| Content pinning | 20 | DRK-017,030 | Yes |
| Local recovery | 17,20 | DRK-018 | Yes |
| Accessibility | 14,23 | DRK-024..026 | Yes |
| Recipe graph ambiguity validation | 04,19 | DRK-019 | Before future recipe launch |
| Trusted discovery/collections | 06..08,17 | DRK-020..023 | Future |
| Max-tier terminal handling | 03,09 | DRK-027..028 | Yes |
| FX doesn't award score | 12,13 | DRK-029 | Yes |

## Definition of Done — docs

All document links resolve in the delivered pack; all declared JSON examples parse and schema checks pass; canonical IDs/names/scores match Batch 1; no alpha doc activates future mechanics; release gates and owner decisions are visible; final package manifest and hashes are generated. A checker should identify missing referenced filenames and malformed fixture keys.

## Definition of Done — v0.1 alpha implementation

A real player can start a mission, aim from desktop and mobile, launch a drink, watch believable collision reactions, merge identical tier-1..7 drinks into higher tiers, see actual next preview, satisfy two orders with deterministic priority, earn correct preview score/coins, win or fail, retry and retain local preview progression. Game runs reliably on supported browsers. Tests pass; owner approves gameplay feel. Nothing should be presented as server-verified money or competitive rank.

## Hard release blockers

Double consumption/duplicate scoring; impossible published tutorial without informed owner waiver; user input consumed on cancelled/rejected launch; crash on missing sprite; active run content mutation; missing order progress; no touch gameplay; no clear win/loss; likely mobile performance collapse; unauthorized claim of persisted trusted rewards.

## Ship quality bar for later systems

A future feature (recipe lab, collections, mastery) cannot be considered finished until it has trusted grant logic, visible fallback states, content migration, accessibility support, API authorization, duplicate request tests, analytics, error recovery, and approved competitive fairness behavior. A UI mockup alone is not a shipped mechanic.

## Coordinator handoff message

> Engineering: Treat Batch 3 docs 01/03/09/10/11/18/22/24/29/32 as immediate alpha contracts. Preserve Batch 2 physics state and queue priorities. Build only linear tier evolution and local preview rewards in v0.1.0. Open small PRs to feature branches, include tests and explicit manual-play instructions for owner. Do not self-merge into main. Anything in recipe branching, pantry, rarity, collections, or mastery requires a separately approved feature gate and later release.

## Release evidence checklist

Record git SHA, app/catalog/rules/physics versions, lint/test commands, expected and actual golden fixture results, real device/browser QA, failed tests, performance observations, asset/license approval, changelog and rollback plan. Mark unexecuted manual tests `PENDING OWNER`, not green.
