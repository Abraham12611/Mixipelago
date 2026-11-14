# 28 — Scenario Atlas: What the Player Sees, What the Engine Does, How to Debug

## Why an atlas

This bridges product language and physics engineering. A tester can identify a visible bug and find its likely owner, simulation assertion and instrumented fixture. It is especially useful when multiple AI engineering agents implement renderer, rules, input and physics independently.

## Scenario A — Clean straight launch

**Player sees:** one glass at bottom, guide points up; release sends it smoothly into open board. **Engine:** input produces normalized negative-Y vector; command validates; body created at launch point and `applyImpulse` once; renderer interpolates. **Potential bugs:** shot starts on pointerdown, Next shifts twice, glass leaves foot behind, body stops suddenly. **Diagnose:** log input command step, body initial impulse, linear damping and sprite-to-world projection; run `F001`/`PHY-001`.

## Scenario B — Different glasses, head-on

**Player sees:** orange glass hits blue glass; blue moves, orange slows/rebounds, both remain. **Engine:** same-tier predicate false; Rapier contact solver handles collision; FX plays small clink. **Potential bugs:** drinks merge incorrectly, overlap/pass through, both stop dead, event callback awards coins. **Diagnose:** inspect tiers, collision groups, CCD, contact events and event-to-score isolation; run `F002`/`PHY-002`.

## Scenario C — Different glasses, glancing

**Player sees:** orange clips edge of blue and deflects diagonally. **Engine:** normal contact direction and relative velocity create lateral impulse, low friction preserves glide. **Potential bugs:** straight-line bounce irrespective of angle, huge spin, unpredictable secondary impulse. **Diagnose:** draw collision normal, centers, velocities; inspect whether two physics engines are active or VFX moves authoritative sprite independently; run `F003–F005`/`PHY-003..005`.

## Scenario D — Identical drinks touch

**Player sees:** two matching glasses converge and create next-tier drink with pop. **Engine:** raw contact candidate passes eligibility; arbiter claims exactly two IDs; commit removes them, creates output; reducer awards once. **Potential bugs:** one input remains, wrong tier, score doubled, new drink teleports or appears below line. **Diagnose:** mergeId event log, claimed states, placement search, output velocity and renderer ghost; run `PHY-006`.

## Scenario E — A simultaneously hits B and C

**Player sees:** one collision in a crowded group results in one clear merge. **Engine:** contacts normalized to stable keys; both pairs compete for shared input; first canonical pair wins. **Potential bugs:** duplicated B, two results, object destroyed during event drain, nondeterministic merge outcome. **Diagnose:** capture unordered/raw pair list vs sorted claims, stable IDs, deferred mutations; run `F007`/`PHY-009` with reordered input arrays.

## Scenario F — Chain reaction

**Player sees:** t2+t2→t3, then fresh t3 touches existing t3→t4, escalating FX. **Engine:** result created with lineage; follow-up contact evaluated next fixed step; chain depth increments; no recursive duplicate. **Potential bugs:** chain fails because new result initially overlaps, chain credited to wrong shot, visual FX blocks next collision, score counted twice. **Diagnose:** rootShotId/rootMergeId, state on each step, overlap query, cooldown behavior; `F008`/`PHY-011`.

## Scenario G — Customer requested drink produced

**Player sees:** generated drink shines then flies to oldest matching order, bubble marks completion. **Engine:** result marked serve-claimed after creation phase per alpha priority; removed exactly once; reducer emits `drink_served`, `order_progressed`, preview coins and score; no further physics. **Potential bugs:** matched drink merges again instead, two customers get same glass, item vanishes without explaining reward. **Diagnose:** order priority, serve claim, age/ID tie breaker, reducer idempotency; run `PHY-012`.

## Scenario H — Borderline danger, then rescue

**Player sees:** glass reaches dashed warning zone; warning pulses; another impact returns it to safe area; warning clears. **Engine:** per-body consecutive fixed-step danger counter, reset with hysteresis; no wall collider at line. **Potential bugs:** instant loss, warning flickers, spawn drink triggers loss, pause continues timer. **Diagnose:** foot radius, graceSteps, arming status and pause flag; run `F010`/`PHY-015..019`.

## Scenario I — Fast shot through thin gap

**Player sees:** drink always interacts with expected boundary/target rather than teleporting through. **Engine:** CCD enabled and static collider appropriately thick; fixed-step solver. **Potential bugs:** one-frame tunneling, out-of-bounds, NaN correction, giant bounce. **Diagnose:** max speed, CCD flag, solver timestep, wall thickness; run `F011`/`PHY-013`.

## Scenario J — Mobile accidental second touch

**Player sees:** gesture cancels or continues predictably without firing twice; retry remains available. **Engine:** pointer ownership, capture release, second pointer policy, command ID dedup. **Potential bugs:** two shots at once, launch aim jumps to another finger, browser scroll. **Diagnose:** pointer IDs and aim state transitions; run `INP-005` and manual owner test.

## Scenario K — Low FPS / device pause

**Player sees:** slowed visual frame rate but stable collision trajectory; switching apps pauses game. **Engine:** fixed-step accumulator with maximum catch-up; hidden tab clears delta; render interpolation independent. **Potential bugs:** instant loss on resume, multiple missed merges or speed-up, lost touch capture, audio repeats. **Diagnose:** accumulator metrics, visibility event log, activeTimeSteps, local checkpoint; run `F012`/`PHY-019..020`.

## Scenario L — Retry after winning

**Player sees:** victory screen; retry starts clean new board; no ghosts or duplicated sound. **Engine:** old world disposed, new session ID, empty event queues and stable initialization from mission config. **Potential bugs:** multiple Phaser canvases, stale subscription adds coins to new session, memory leak, ghost glass remains. **Diagnose:** mounted scene count, active listener count, body registry size, session token and game teardown; run `PHY-021..023`.

## Debug packet format

Each reproducible issue should include `scenarioId`, release commit hash, pinned package versions, physics preset hash, mission version/seed, command transcript with steps, device/browser, expected versus actual, screenshot/clip from owner manual test where provided, physics overlay toggle state, first mismatch step and console/CI logs. Do not rely on "sometimes feels wrong" with no fixture; turn every reproducible bug into a regression test.

## Quality triage priority

**P0:** wrong reward/duplicate merge, freezes, broken mobile input, physics world corruption, impossible win/loss. **P1:** frequent inaccurate collision visuals, chain failures, unstable low-end performance. **P2:** cosmetic audio timing, minor shadow mismatch, occasional particle artifacts. Address P0 before release; do not use increased animation intensity to conceal P0 physics defects.
