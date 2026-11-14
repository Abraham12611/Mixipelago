# 22 — QA Matrix, Contract Tests, Property Tests and Regression Fixtures

## Test levels

- **Static content:** schema validation, unique keys, graph reachability, asset refs and locale coverage.
- **Unit:** pure compatibility resolver, score function, order matcher and XP/reward aggregators.
- **Simulation integration:** Rapier contact -> merge -> reducer -> serving -> state transitions.
- **Replay:** same seed, event order, config and inputs yield same logical outputs in supported test environment.
- **UI automation:** evolution strip, order cards, previews, errors, reduced motion and keyboard navigation.
- **Manual owner checks:** tactile gameplay feel, perceived collision realism, visual clarity and sound quality on real desktop/mobile devices.

## Named test plan

| ID | Scenario | Expected outcome |
|---|---|---|
| DRK-001 | Catalog has 8 alpha tiers | Contiguous tiers and 8 unique IDs |
| DRK-002 | Valid `1+1` | One tier-2 output, score base 25 |
| DRK-003 | Valid `7+7` | One tier-8 output, score base 3500 |
| DRK-004 | Invalid `8+8` | No merge, physical collision continues |
| DRK-005 | Invalid `2+3` | No merge |
| DRK-006 | A touches B and C simultaneously | Exactly one pair claims A |
| DRK-007 | Two disjoint simultaneous pairs | Both merge with stable IDs |
| DRK-008 | Result overlaps match | Additional merge only on later step |
| DRK-009 | New output matches oldest order | That order served; no same-object remerge |
| DRK-010 | Two orders same tier | First created order wins, then next |
| DRK-011 | Order quantity two | Reward only on second eligible result |
| DRK-012 | Duplicate merge delivery | Score/order/reward applied once |
| DRK-013 | Rejected shot | Queue unchanged |
| DRK-014 | Fixed seed run | Same tier queue and outcomes |
| DRK-015 | Art skin swap | No change in merge eligibility |
| DRK-016 | Missing art asset | Fallback displayed, simulation preserved |
| DRK-017 | Active session receives catalog publish | Old catalog remains pinned |
| DRK-018 | Corrupt local save | Controlled recovery, no crash |
| DRK-019 | Future recipe ambiguous | Content publish rejected |
| DRK-020 | Future recipe locked | No unauthorized output |
| DRK-021 | New discovery request duplicated | One durable grant |
| DRK-022 | Inventory insufficient | No partial debit |
| DRK-023 | Ranked score with perk | Perks normalized/disabled |
| DRK-024 | Reduced motion | No essential info lost |
| DRK-025 | Mobile thumbnail icons | Distinct at minimum size |
| DRK-026 | Localization changes | IDs/rules unchanged |
| DRK-027 | Max-tier + order target | Can serve only when newly created and eligible |
| DRK-028 | Max-tier duplicates no order | Remain colliding, can cause board pressure |
| DRK-029 | HUD animation repeats | No secondary reward emitted |
| DRK-030 | Rule manifest mismatch | Recoverable compatibility error |

## Property-based invariants

Generate random valid contact graphs and assert unique consumption per step, monotonic output IDs, output tier=source tier+1 for alpha, active-body count delta −1 per merge before serving, no negative score, no unordered duplicate merge, and no automatic order service from untouched resting body. Verify 10,000 synthetic contact graphs as a proposed CI benchmark; actual performance budget can be adjusted based on CI runtime.

## Load and memory test

Run thousands of seeded sessions in a headless simulation (no renderer), then repeated Phaser scene enter/exit to detect image/texture leaks. Mobile browser matrix includes iOS Safari and Android Chrome, plus at least one low-power device. Test intermittent network, tab backgrounding/resume, orientation, zoom, safe areas, low battery, audio interruption and rapid input.

## Quality gate

All DRK-001..018 and 024..030 applicable to alpha must pass before v0.1.x release. Future-feature tests can be marked `not applicable until enabled`, not `passed`. Owner manually signs off visual differentiability, collision feel and intuitive serving. Automated test evidence stored with version hashes and any known exceptions.
