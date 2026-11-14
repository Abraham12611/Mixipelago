# 16 — Skill Expression, Difficulty Scaling, Puzzle Fairness, Session Pacing

## Primary design claim

Mixipelago should feel skillful rather than arbitrarily random. Physics provides expressive technique (angle selection, bank shots, clustering, setup for chains), while levels define meaningful objectives (orders/score) and constraints (space, shot budget). Difficulty should rise from learnable combinations of these factors, not invisible manipulation of physics coefficients.

## Difficulty dimensions

| Dimension | Easiest | Harder | Controllable by |
|---|---|---|---|
| Board pressure | Sparse initial setup | Crowded field | `startingBodies` |
| Spawn sequence | Curated useful tiers | Mixed weighted tiers | `spawnTable`, seed |
| Order complexity | Tier 2–3 targets | Tier 6–8 targets | `orderTargets` |
| Shot efficiency | Generous/unlimited | Strict budget | `maxShots` |
| Geometry | Wide open | Obstacles, narrow pockets | `boardLayout` (later) |
| Time | Relaxed | Active-time deadline | `activeTimeLimitSteps` (later) |
| Skill challenge | Straight shots | Bank/angled setup | fixture design |
| Chain opportunity | Existing match pairs | Long merge path | `startingBodies` and target |
| Visibility | Full preview | Limited preview | mission rule (later) |
| Surfaces | Standard glide | Ice/sticky zones | materials/zone modifiers (later) |

Alpha should vary primarily **starting bodies, target tiers, spawn seeds, and shot budget only when clearly explained**. Additional modes belong in Batch 4, so advanced constraints are extension hooks rather than active requirements.

## Quantitative difficulty targets (proposed for study)

- Tutorial mission: 85–95% of first attempts should succeed after learning the controls; design hypothesis, not observed target.
- Early normal missions: desired 70–85% first-try completion; avoid monetizing frustration.
- Medium missions: 55–75% first-try completion; maintain retry path.
- Hard optional missions: 25–50% first-try completion, signposted as optional.

These are candidate player experience targets, not evidence-based numbers for a new game. Use beta cohort analytics, not arbitrary force, to tune. Exclude first-time players who have not learned aiming from experienced-skill difficulty estimates.

## Skill expression metrics

- **Hit precision:** aim angle and actual first contact offset.
- **Merge efficiency:** output tier value produced per shot.
- **Chain utilization:** merges caused by a single root shot.
- **Board safety:** time/steps spent in danger zone and rescues.
- **Order alignment:** share of merges that advance customer requests.
- **Recovery:** ability to resolve crowded board after a poor shot.

Metrics inform tutorials and balance; do not publicly rank players by a metric that rewards farming irrelevant actions. Real leaderboard formulas require a separate fairness spec (Batch 13).

## Pacing

A short round should be doable in 2–5 minutes for a familiar player, subject to real-world validation. Shoot-cooldown must not make a five-order mission drag; near-frictionless body motion can run while next shot becomes available. Only gate shooting while the launch area is blocked or a critical transition happens. A clear next preview and two orders give players continuous goals. Between-round summary should be quick, with optional detail on stars/coin preview.

## Spawn fairness

Weighted random streams can produce frustrating runs. Proposed tutorial uses authored queue. Later, a deterministic queue-director can limit longest streak or guarantee useful tier opportunities. **Do not invisibly change spawn odds in response to unspent coins, retention risk or purchases** without careful ethical and game-balance review. For ranked, use identical seeds and queues for everyone.

## Failure recovery

- When board crowded, indicate a rescue angle or entry-level hint rather than surprise loss.
- `Retry` starts a fresh session with same mission config and new session ID.
- If mission uses a fixed seed, retries reuse the seed unless mission explicitly says reroll; this makes practice meaningful.
- No loss of trusted currency in alpha; preview coins can reset with session results and must be labeled preview.
- User can pause and exit without penalty other than abandoned run.

## Skill tree interaction (future)

Later skills may alter collision constants, queue quality, booster capacity or customer probabilities. Such perks can wreck puzzle predictability. Require each modifier to declare phase (`pre-session`, `pre-step`, `on-merge`, etc.), stacking method (additive/multiplicative/capped), conflict precedence and ranked eligibility. Ranked puzzles should fix a standardized skill profile or use equalized modifiers. Batch 7 will specify full trees; Batch 2 only establishes the extension boundary.

## AB experiments

Experiment one variable family at a time: `drag gesture`, `linear damping`, `restitution`, `cooldown`, `aim guide`, `result momentum`. Use stable telemetry/feature flags. Never migrate an in-progress ranked session to a different physics config. Replays and session records must carry version/hash. Analyze by device class to distinguish poor control performance from genuinely difficult levels.

## Mission QA

A content authoring tool should run Monte Carlo samples of seed/queue/aim bots or scripted agents to flag impossible missions and volatile difficulty; these simulations are diagnostic, not proof of fun. Real owner playtests and beta player observations finalize acceptance. Content changes to mission balance are data commits with version bumps and regression suites.
