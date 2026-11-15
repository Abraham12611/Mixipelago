# 10 — Test Strategy, Device Matrix and Owner Manual Acceptance

**Owner policy:** All **manual UI and gameplay tests** are directed to the product owner. Engineers run automated unit/integration/smoke suites and provide exact scripts/checklists to owner for manual execution. Never claim manual approval without owner result.

## Automated tests (engineers)

### Pure rules
- Identical tier 1–7 merge only; tier 8 terminal.
- Duplicate contact/merge IDs do not duplicate outputs, score or serving.
- Three-way contact claims each input at most once.
- New matching output serves oldest eligible order before remerge.
- Finish second target order and trigger danger in same tick → win.
- Missed/blocked shots do not consume next queue.
- Pause stops active time/launch commands.
- Mission content versions and scoring hashes guard stale saves.

### Mission fixtures
- Every published stage has valid JSON, assets, fixed-seed queue, feasible objective and saved legal winning replay.
- Unpublished stages absent from map interactive selection.
- No order requires unavailable disabled tier or source-equivalent count.
- Route graph retains a published next mission unless campaign complete.
- Unknown IDs fail gracefully.

### Platform
- Base44 build/deploy succeeds; wasm if used loads under public URL.
- Deep-linked /play works from cold URL; no unexpected sign-in.
- No console fatal error, missing asset, focus loss or unresponsive touch canvas.
- No external iframe substitution; full game delivered as Base44 application.

## Owner-directed manual matrix

| Browser/device | Path | Required outcome |
|---|---|---|
| Android Chrome (representative midrange device) | New guest → tutorial → levels 1–3 | Clear readable aiming and smooth session |
| iOS Safari | New guest → finish/retry → map | Touch release, audio unlock and safe-area support |
| Desktop Chrome/Edge | Mouse/keyboard → pause/resume → retry | Accurate aim and no stuck input |
| Desktop Firefox | New guest → 1 mission | WebGL/canvas compatibility |
| Small 320px viewport | Home, board, results, map | No horizontal clip or blocked controls |
| Slow network/new browser profile | Cold load → assets → play | Loading feedback and retry |
| No localStorage | One session → results | Playable without persistence |
| Muted/reduced motion | Merge chain, win/loss | Equivalent information remains visible |

## Rubric-based QA

- **Gameplay**: clarity of first launch, useful tactical shot, chain satisfaction, retry, fair mission difficulty.
- **Creativity**: distinct art, service fantasy, character presence, original festival finale.
- **Execution**: no crashes, fast input, stable physics cadence, correct resizing, accessible interactions.
- **Compliance**: Base44 public URL, account/payment-free, rights and new-build evidence.

## Severity gates

**P0:** cannot load/play anonymously, login/paywall, illegal/unlicensed asset, data loss preventing restart, crash, false published feature, invalid Base44 URL, deadline missed.  
**P1:** broken mission/progression, consistent poor FPS, unclear aim, mobile collision error, major accessibility blocker.  
**P2:** minor visual inconsistencies or polish.

No P0 or P1 open at final submission. Document device/browser, reproduction sequence, expected/actual, screenshot/screen recording, fixed version and owner retest.

## Owner manual acceptance script

1. Open submitted Base44 URL in **new private window** with no sign-in.
2. Tap Play, complete tutorial, aim and launch repeatedly.
3. Verify tier merge and newly generated customer order service.
4. Win first mission, next/map, replay, pause/resume, lose/retry.
5. Refresh; verify local save and correct available missions.
6. Mute and reduce-motion; verify still playable.
7. Repeat on mobile and desktop; owner explicitly signs off.

If the owner cannot perform tests, do not falsely mark pass; track **awaiting owner validation**.
