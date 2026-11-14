# 22 — Architecture Decisions, Risks, Unanswered Questions, Approvals

## Batch 1 compatibility register

| Concern | Batch 1 baseline | Batch 2 status |
|---|---|---|
| Renderer | Phaser 4 | Retained; verify current 4.x API with pinned lockfile |
| Physics | Rapier 2D WASM proposed | Retained; contact/determinism specs expanded |
| Simulation tick | Fixed 60Hz | Retained; 120Hz lab only |
| Body footprint | Equal radius circle | Retained for all 8 alpha tiers |
| Aim gesture | Drag toward direction, fixed impulse | Retained as proposed alpha; compare slingshot in lab |
| Score serving | Automatic on newly merged result | Retained; auto-serve before chain for matching order by default |
| Customers | 2 active slots | Retained |
| Danger | Dashed line + grace | Retained, clarified step counting and priority |
| Score trust | Local preview-only | Retained; ranked deferred |
| Replays | Do not assume cross-browser determinism | Refined: Rapier WASM docs and deterministic package variants document determinism conditions; verify installed build and *whole-app* pipeline |
| Manual testing | Owner performs manual UI tests | Retained |
| PR merge | Coordinator controls, main owner approval | Retained |

## Proposed ADRs to finalize in prototype

**ADR-PHY-001 Input gesture**: default drag-toward-target release; alternative slingshot. Decision after owner trial. **ADR-PHY-002 Mass model**: equal density and equal radius for all tiers in alpha. **ADR-PHY-003 Momentum on merge**: mass-weighted average with cap. **ADR-PHY-004 Merge order**: stable pair key; result candidates on next step. **ADR-PHY-005 Serving priority**: newly created drink needed by oldest order is auto-served after creation phase, before remerge. **ADR-PHY-006 Danger geometry**: footprint intrusion vs center point; proposed footprint. **ADR-PHY-007 Rails**: static top+side; lower dashed line is nonphysical. **ADR-PHY-008 Shot cooldown**: fixed step interval plus spawn-clearance check, not whole-board sleep. **ADR-PHY-009 Replay**: authoritative verifier only after cross-platform golden test. **ADR-PHY-010 Physics versioning**: immutable per active session. **ADR-PHY-011 Render interpolation**: renderer only; physics independent.

## High-risk items

| Risk | Severity | Detection | Mitigation |
|---|---|---|---|
| Unpleasant/floaty feel | Critical | owner tests preset A/B | physics lab, compare damping/restitution |
| Browser input misalignment | Critical | mobile pointer E2E | camera conversion tests, explicit resize cancel |
| Duplicate merge/rewards | Critical | property-based multigraph tests | deterministic arbitration + idempotent reducer |
| Very long sliding/no clear turns | High | session length metrics | tune drag/sleep/cooldown; board pressure |
| Late-stage chain not triggering | High | overlap fixture | next-step graph/overlap probe |
| Glass spinning visually wrong | Medium | owner UX review | decouple sprite tilt from body angle |
| Performance crash on iOS | Critical | device QA | low tier, smaller textures, simple colliders |
| Replay mismatch | High, future ranked | cross-platform hashes | canonical command encoding & pinned version |
| Physics version changes midrun | High | replay/seed assertions | freeze preset per session |
| AI art inconsistent silhouettes | Medium | tier side-by-side review | unified Blender camera and style sheets |
| Overscoped v0.1.0 | Critical | delivery board | defer all non-core systems |

## Important open questions (owner input only after first playable)

1. Should shot angle be restricted to a forward cone or allow nearly horizontal bank shots?
2. Which feels better: drag toward target, pull-back slingshot, or tap target to aim and button fire?
3. Should touching a matching drink merge immediately or only after visible collision response?
4. Should tier-based mass grow and larger drinks push smaller ones more strongly in later missions?
5. Should a successful result match an order immediately auto-serve, or should the player choose manual serving?
6. How much momentum should a newly merged result inherit?
7. At what danger warning duration does pressure feel fair but compelling?
8. How bright should glows/particles be on a small phone under sunlight?
9. Should boosts affecting physics be available in normal campaign, and disabled in ranked?
10. Should the top-tier drink auto-cash out to clear board or remain as obstacle? Alpha: remains.

These don't block initial engineering because working defaults are defined; owner feedback can revise through versioned ADR before production.

## ADR template

```md
### ADR-PHY-### — Title
Status: proposed / accepted / superseded
Owner: ...
Context and problem: ...
Options compared: ...
Decision: ...
Affected versions/contracts: ...
Migration/replay impact: ...
Tests: ...
Evidence: ...
Date/approval: ...
```

## Change control

A change to core collision or serving rules requires: new ADR or ADR update, config/rules version bump, golden replay review, owner feel-test if visible, test fixture update, rollout/rollback plan and docs update. A shader/asset/SFX-only change should not alter physical trajectory and usually needs no physics version bump; verify by replay hash.
