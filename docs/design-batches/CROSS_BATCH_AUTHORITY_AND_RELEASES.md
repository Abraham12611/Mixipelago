# Mixipelago — Cross-Batch Authority and Release Gates (10–15)

## Domain ownership
| Batch | Authority | Reads/depends on |
|---|---|---|
| 10 | World conditions, forecast snapshots, incident eligibility, individual incident lifecycle and player-world chronicle. | Batch 05 map, Batch 06 wallet/insurance/shops, Batch 09 customer demand, Batch 12 live calendar, Batch 04 gameplay mode rules. |
| 11 | Narrative definitions, dialogue choices and story flags, quest orchestration, approved rival behaviors and the player chronicle. | Batch 05 campaign, Batch 09 customers, Batch 06 shops and rewards, Batch 08 collectibles, Batch 10 incidents and Batch 12 festivals. |
| 12 | Event calendar editions, schedule semantics, activity enrollment, eligibility, participation projections and event orchestration. | Batch 10 weather and world conditions; Batch 11 story quests; Batch 04 missions; Batch 06/08 rewards; Batch 13 tournament rankings; Batch 14 crews. |
| 13 | Score submission/proof validation, ranking materialization, season freeze, divisions and tournament adjudication. | Batch 02 physics/replay; Batch 04 scoring and missions; Batch 06 rewards; Batch 07 normalized skills; Batch 08 prize entitlements; Batch 14 friends and crews. |
| 14 | Friend relationships, crew membership and governance, social challenges, contributions, invitations and multiplayer session orchestration. | Batch 13 rankings and verified replays; Batch 06 wallet; Batch 08 rewards; Batch 09 guest personalities; Batch 12 festival co-op; Batch 02 physics server certification. |
| 15 | Information architecture, token system, UI component API, responsive design, motion, accessibility, app page states and screen-to-domain contracts. | Batch 01 React/Phaser boundary; Batch 02 board; Batch 03 drinks; Batch 04 missions; Batch 05 map; Batches 06–14 screens and projections; Batch 16 art production. |

## Locked earlier contracts
- Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
- Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
- Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
- Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
- Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
- Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

## Proposed release sequence
| Batch | Candidate release and scope |
|---|---|
| 10 | Preview weather overlays after the first campaign (candidate v0.6.0); authored opt-in incidents and recovery (v0.6.1+); shop-economic world effects only after audited server-ledger integration (v0.7+). |
| 11 | Story introduction and one optional quest chain after basic map/player persistence (candidate v0.5.3); branching arcs and simulated rival businesses expand later behind distinct gates. |
| 12 | Candidate first opt-in festival and a single authored event mission after campaign and trusted rewards (v0.6.2); calendar rotation, community goals and seasonal live programs staged later. |
| 13 | One normalized weekly global challenge after verified server replay (candidate v0.5.0); historical seasons/divisions v0.5.1+; tournaments and opt-in regional boards after safeguards. |
| 14 | Candidate v0.7.0 friends + asynchronous ghost challenges; v0.7.1 crew projects; v0.8.0+ real-time matches only after authoritative simulation, reconnect and moderation tests. |
| 15 | Foundational tokens, responsive gameplay shell and core routes affect v0.1.x immediately; campaign/shop/profile views rollout with their systems; social, events and live interfaces are feature-gated until owned backends work. |

## Cross-batch sequencing (architecture, not a calendar)
1. UI core (Batch 15) can move in parallel with base gameplay but must not show nonfunctional commerce/social controls.
2. Verified challenge proof (Batch 13) is prerequisite for fair async challenges (Batch 14) and official tournaments (Batch 12).
3. World conditions (Batch 10) may decorate map before any economic incidents; incident financial effects require Batch 06 ledger.
4. Story quests (Batch 11) use mission and choice receipts; festival quests (Batch 12) reuse them with edition deadlines.
5. Rewards from Batches 10–14 route through Batches 06, 07 and 08 and never direct-write wallet, XP or collection tables.

## Decisions still awaiting owner approval
- Final art palette, route priority and character voice style.
- Live-event scheduling cadence and whether global conditions are shared across islands.
- Competitive attempt limits, appeals and regional visibility defaults.
- Crew size/social discoverability and whether real-time play is worth a separate persistent-server budget.

## Documentation acceptance
These files provide implementation contracts, examples, testing matrices and stages. Production legal, security, physics determinism, accessibility and player approval require implementation evidence before feature gates can be enabled.
