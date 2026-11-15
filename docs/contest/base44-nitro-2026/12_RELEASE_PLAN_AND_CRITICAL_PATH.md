# 12 — Contest Delivery Plan and Critical Path

**Planning date:** 2026-11-15. **Hard submission deadline:** 2026-12-03 23:59 UTC, subject to organizer updates. This is a *proposed internal plan*, not a completion estimate or deadline guarantee.

## Principle

The game must be enjoyable and fully playable. We schedule for a **November 30 internal content freeze** with days left to fix platform/compatibility issues and enter the contest manually. We do not use the deadline to justify copied assets or bypassing Base44.

| Window (UTC) | Core goal | Exit gate | Owner |
|---|---|---|---|
| Nov 15–17 | New Base44 app, rules/rights review, public URL and Phaser/Rapier feasibility | Guest play and one working shot in public app; unresolved platform legality escalated | Platform + owner |
| Nov 18–21 | Eight-tier physics/serving, first mission, tutorial, responsive HUD | Automated merge/order invariants; owner first-play approval | Gameplay + UI |
| Nov 22–25 | Build and prove first 8 missions, map progress, all assets | Each published mission has a legal solution and owner walkthrough | Content + QA |
| Nov 26–28 | Finish up to 12 missions, visual/audio polish, results, settings | Mobile/desktop P0/P1 list clear; distinct original art | Art + QA |
| Nov 29–30 | Release candidate, cold-browser test, licence and launch assets | Complete owner-directed acceptance checklist; platform eligibility evidence | Coordinator + owner |
| Dec 1–2 | Manual submission, record URL/confirmation and Launchpad listing | Official confirmation / screenshot retained | Entrant |
| Dec 3 before 23:59 | Contingency only, valid vote outreach, fix disqualifying issues before cutoff | No unfinished critical issues; commit/publish freeze | Release + owner |
| Dec 4–9 | Judging stability; avoid material changes | Monitor availability; only consult organizer for emergency patches | Release |
| Dec 10 onward | Track actual announcement and 90-day uptime obligation | Deadline computed from actual announcement | Release |

All timelines may change if official rules are amended. Do not rush an invalid submission.

## Hard dependencies

- New Base44 app → platform integration proof → final engine choice.
- Physics engine → authoritative order reducer → first complete mission → content proofs.
- Art/rights inventory → release candidate → submission screenshot/media.
- Guest/public URL → owner manual gameplay → verified publish.
- Manual form → submission confirmation → no prohibited change after cutoff.

## Stop-the-line criteria

- Base44 URL requires login or in-app purchase to play.
- App was built as a rehosted/embedded older game.
- No proof of new Base44 project creation in submission window.
- Unsupported wasm/physics crashes on target browser.
- Stage cannot be finished or player is stranded.
- Art/music rights uncertain.
- P0/P1 issue lacks fix or safe rollback.
- Inability to keep app live for required period.

## Suggested cadence

Brief engineering sync each day, one source-of-truth issue board; review PRs twice daily if parallel work justifies it. The user/owner handles **manual** UI/gameplay validation; engineers provide exact test instructions, recordings, and seed fixtures, not claims of subjective approval.

## Scope fallback under pressure

Stage A: 8 excellent missions, one island, beautiful original board. Stage B: 12 missions. Stage C: polished festival moment. Strip scope in reverse order whenever a milestone slips. Do not cut eligibility, guest access, originality, or controls.
