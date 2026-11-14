# 01 — Product Scope, Player Fantasy and Design Tenets

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## The promise
A player begins as a novice beach-bar owner but eventually develops an identifiable playstyle: a precision-focused mixologist, a loved local host, an efficient entrepreneur, a daring explorer, a resilient operator, or a tactical puzzle specialist. A **build** means the combination of persistent player level, invested skill points, equipped active abilities, recipe mastery and situational temporary modifiers. It must not be synonymous with account wealth, time spent, or purchase volume.

## Non-goals and staging
- v0.1.x physics and v0.2.x campaign are unchanged. **No trusted player XP, skill points or unlocked combat-like perks in local alpha.**
- v0.3.0 economy brings a trusted coin ledger and starter shop. v0.4.0 introduces trusted player progression and a small, testable first skill slice.
- A complete six-branch tree, active abilities, prestige, rare mastery, profession identity and event-driven talents are designed here but ship in later gated slices.
- Skill trees do not become a substitute for the eight-tier drink ladder, shop ownership, or campaign mission graph. None can directly invent higher-tier drink identities or bypass published mission requirements.

## Design principles
1. **Immediate game remains simple:** do not show a six-tab talent UI to a new player before their first meaningful success.
2. **Choice, not an obligation:** build diversity arises from tradeoffs and mutually compatible packages; no mandatory talent is required for standard campaign completion.
3. **Power visibility:** display probability changes, caps, duration, conditions and disabled modes; no misleading 'always rich customers' marketing for a chance-based talent.
4. **Fairness:** ranked modes use a canonical competitive loadout or a separate normalized ruleset; purchases and time investment cannot replace puzzle mastery.
5. **Recoverability:** respecialization is available with no permanent trap and no confiscation of previously earned stars or shops.
6. **Accessibility:** aim-assist visibility and reduced-motion settings are baseline accessibility options rather than secret premium abilities; talents may add convenience but not remove fundamental accessibility.
7. **Predictability:** stable effect IDs, version-pinned catalogs, integer/decimal policies, auditable server writes and deterministic evaluation.

## Golden invariants from previous batches
- Batch 2 owns movement, 60 Hz fixed-step simulation, collider materials, collision arbitration and merge life cycle.
- Batch 3 owns the alpha tiers (1–8), the terminal tier 8, and **auto-serving newly created matching drinks to the oldest eligible order before chain continuation**.
- Batch 4 owns mission objectives, score, results, and win-priority over same-tick failure.
- Batch 5 owns island graph and unlocks. A skill may reveal an *optional* path clue but may not silently unlock an unpublished node.
- Batch 6 owns the trusted coin wallet, shop transactions, and modifier handoff. Preview coins do not convert into wallet coins.

## Proposed success metrics
> Early implementation hypotheses, not shipping targets: 50%+ of eligible players open a skill tooltip, 35%+ spend their first point within two eligible sessions, under 5% request involuntary reset support, and no build exceeds 10% win-rate uplift versus peer-skill baseline in standardized challenges. Evaluate by cohorts and accessibility needs, not a single aggregate KPI.

## Ownership
Game director owns the player promise and manual interface/play-feel approval; gameplay lead owns rule compatibility; economy lead owns reward and cost balance; backend owns persistence; content lead owns catalog publication; security reviews all trusted grants. Engineers may automate tests; **manual UI tests go to the owner**.
