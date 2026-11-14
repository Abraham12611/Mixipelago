# 21 — Architectural Decisions, Risks and Open Questions

## Approved/working decisions (based on current direction)

| ADR | Decision | Rationale | Revisit when |
|---|---|---|---|
| ADR-001 | Browser-first, TS monorepo | Fast launch, shared logic and mobile future | Browser perf proves inadequate |
| ADR-002 | Phaser 4 primary renderer | Game scenes/input/FX appropriate for 2D/2.5D | Integration benchmark contradicts |
| ADR-003 | Rapier 2D proposed physics | Angular collisions, low damping, WASM, CCD | Compare Matter benchmark |
| ADR-004 | 2.5D art pre-render preferred | High quality without full 3D runtime cost | Interactive 3D feature requires real mesh |
| ADR-005 | React for app UI, not physics loop | Responsive DOM menus, reusable components | Proven rendering/perf issue |
| ADR-006 | Local preview-only alpha rewards | 72-hour feasibility; avoid fake trusted economy | Auth/wallet backend ready |
| ADR-007 | Automatic serve on generated drink | Reduces first-loop complexity | Owner playtest prefers manual serving |
| ADR-008 | Two simultaneous customer orders initially | Readable alpha | Player research supports more |
| ADR-009 | One evolution chain, eight tiers | Test core before branch complexity | Mission design expands |
| ADR-010 | Server-authoritative persistent economy | Anti-cheat, transactions, integrity | Never remove |
| ADR-011 | Future data-driven missions & island graph | Content scaling without engine rebuild | Content editor research |
| ADR-012 | Coordinator controls PR merges; main requires owner approval | Integration safety | Owner changes policy |
| ADR-013 | All manual UI tests to user | Owner testing policy | Owner changes policy |

These are **proposed technical baselines**, not proof that code exists. Need engineering/owner confirmation at kickoff.

## Important open design decisions

1. **Aim gesture:** drag direction to target vs pull-back slingshot. Default proposal: drag toward target, release. Owner to test both in physics lab.
2. **Shot strength:** fixed for alpha vs adjustable by drag length. Default fixed.
3. **Serving:** automatic output consumption vs tap-to-serve. Default automatic new merges only.
4. **Danger boundary:** crossing/time grace vs maximum board capacity. Default explicit grace.
5. **Board perspective:** perspective illustration must preserve world-coordinate intuitive aiming.
6. **Collision scale:** all glass collider radii identical vs tier-dependent footprint. Default identical initially to avoid balance surprises.
7. **Animation style:** 2.5D pre-render vs selective 3D; use prototypes on low-end phones.
8. **Audio personality:** tropical acoustic/electronic score or separate motifs by island.
9. **Business economy order:** trusted account/wallet must precede real shop purchases (despite optional release version labels).
10. **Rank verification:** replay feasibility must be proven before global rewards.
11. **Precise leaderboard scope definitions:** opt-in country/region/city, fairness and privacy rules.
12. **Original character art style:** choose coherent Mixipelago direction, not source lookalikes.

## Key risks and mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| WebGL/WASM fails on mobile Safari | Critical | Early iOS smoke, init fallback and error screen |
| Physics feels floaty/unpredictable | Critical | Physics lab, owner feel testing, fixed configs |
| Merge duplicates from concurrent contacts | Critical | Atomic merge locks, ordered event queue, tests |
| Render/physics coordinate mismatch | High | Explicit mapping tests and debug overlay |
| Alpha scope balloons into MMO | High | P0 scope freeze and no future UI fake functionality |
| AI art inconsistency | High | Style sheet, master renders, paintover, asset review |
| Over-heavy textures | High | Scene budgets, atlases, memory profiling, lazy load |
| Future rewards cheated | Critical | Server validation, ledger, no trusting local scores |
| Ledger/debit race | Critical | DB transactions, uniqueness/idempotency |
| Localization/privacy/social abuse | High | Explicit consent, moderation, separate legal work |
| Unlicensed generated assets/audio | High | Provenance/license registry |
| Too many engineers touching shared files | High | File ownership, typed interfaces, integration rhythm |

## Decision log template

```
ADR-### Title
Status: proposed / accepted / superseded
Context:
Options considered:
Decision:
Consequences:
Tests/benchmarks required:
Owner + date:
```

No engineer may silently rewrite accepted physics or economy semantics in a UI PR. Raise an ADR or explicit contract-change PR.
