# 29 — Batch 1 Integration Notes and Required Cross-Document Updates

## Purpose

Batch 2 is a specialized deep dive, not a different game architecture. These notes tell the coordinator which Batch 1 paragraphs may need refinement once the physics lab produces approved behavior. Do not directly mutate the original approved Pack 1 document without owner/coordinator review.

## Carry-forward decisions (no change)

- Browser-first desktop/mobile web; Next.js/React shell and Phaser 4 renderer.
- Rapier 2D WASM proposed for rigid-body physics; one solver owns each glass.
- Near-frictionless gliding via low linear damping; low collider friction for tangential contacts.
- 60 Hz fixed physics stepping; rendering interpolates independently.
- Eight tiers, same-tier merge, max-tier no evolution, two customer orders, automatic serve, one tabletop.
- Short alpha with preview-only local rewards and no online trusted wallet.
- Owner conducts manual UI/feel tests; engineers use automated QA.
- Coordinator controls develop merges; main promotion requires owner's explicit approval.

## Clarifications to incorporate after approval

| Batch 1 document | Existing guidance | Batch 2 refinement |
|---|---|---|
| `04_GAMEPLAY_AND_PHYSICS.md` | General circle collider and drag aim | Define exact fixed-step processing order, input state machine and world mapping |
| `04` | `dangerGraceMs` | Store `dangerGraceSteps` in fixed-step config for deterministic evaluation |
| `04` | Contact events trigger merges | Contact events are transition events; support next-step overlap/contact graph query |
| `04` | Chain merged result inherits bounded momentum | Concrete policy: mass-weighted average + clamp, owner to test |
| `04` | Auto-serve order matches | Explicit priority: matching new result is serve-claimed before next remerge under alpha rules |
| `04` | Replay cross-platform caveat | Rapier JS/WASM official guide supports cross-platform deterministic runs with identical conditions; whole app still requires validation |
| `05_DRINKS_CUSTOMERS_SCORING.md` | Two orders, auto-serve | Order tie-breaker and serve claim idempotency must be tested against merge chain |
| `06_TECH_STACK_AND_ARCHITECTURE.md` | Rapier adapter boundary | Explicit `BodyRegistry`, `ContactCollector`, `MergeArbiter`, `DeferredMutations` |
| `08_API_AND_EVENTS.md` | Event envelope | Add canonical command step, stable merge ID, lineage fields, step-based danger count |
| `15_TESTING_AND_PERFORMANCE.md` | Browser and physics QA | Stable PHY-001..030 and INP test identifiers; goldens and owner test protocol |
| `21_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md` | Proposed options | ADR-PHY-001..011, new risk/owner decision log |
| `28_INTEGRATION_CONTRACTS.md` | Command and snapshot types | Version/serialization constraints, async submission semantics, contract ownership |

## Order of edits

1. Implement/test `domain-contracts` in source first.
2. Approve the physics preset and aim/serve behavior by owner feel test.
3. Create ADRs or mark proposed ADR-PHY entries accepted.
4. Update Batch 1 references in the *same PR* as actual source contract changes.
5. Increment `physicsVersion`, `rulesVersion`, or schema version as appropriate.
6. Rerun golden replay fixtures and compatibility tests.
7. Document any deferred features rather than silently changing the current release scope.

## No unauthorized changes

Batch 2 docs do not create or modify an external GitHub repo, Supabase database, Vercel deployment or any user's actual game code. All files here are source documents and illustrative sample JSON. The owner can supply repo coordinates for implementation later. No direct claims of completed engineering tests or released versions are made.
