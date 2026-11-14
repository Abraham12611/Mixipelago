# 43 — Requirement Traceability, Acceptance Evidence and Definition of Done

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Requirement mapping
| Requirement | Spec | Evidence |
|---|---|---|
| CUS-R01 Two scripted alpha customers | 01/09/23 | Batch 4 baseline fixture regression |
| CUS-R02 Oldest eligible auto-service | 08/09/31 | duplicate/priority reducer tests |
| CUS-R03 Deterministic selection | 07/32 | seed vectors + stable snapshots |
| CUS-R04 No impossible orders | 06/08 | budget check + recorded winning trace |
| CUS-R05 Server-verified satisfaction | 10/30/31 | signed result receipt integration |
| CUS-R06 Bounded reputation | 13/35 | cap properties and duplicate source tests |
| CUS-R07 Loyalty no inactivity punishment | 12/27 | time-jump + recovery tests |
| CUS-R08 VIP cap and ranked normalization | 15/19/35 | stochastic simulations/seed fixtures |
| CUS-R09 No reward over-issuance | 20/33 | concurrency + ledger receipt evidence |
| CUS-R10 Accessibility and mobile HUD | 23–27 | owner-directed manual UI checks |
| CUS-R11 Versioned content and safe rollback | 28/39 | staging/rollback rehearsal |
| CUS-R12 Privacy/RLS | 27/30/33 | unauthorized cross-user access tests |

## Documentation acceptance
Every proposed API has a source-of-truth, idempotency and error story. Catalog references resolve, no secret or gated customer is accidentally eligible in alpha, v0.1 order invariants are unchanged, and all example tests run.

## Implementation acceptance (future)
Unit + integration + concurrency + security checks pass; mobile and desktop previews are available; performance tests use actual target devices; manual gameplay and interface test approval are obtained from owner; release gate defaults OFF until approved. Avoid conflating documentation QA with deployed feature completion.

## Sign-off artifact
Attach a short PR checklist: affected batch contracts; tested fixture names; migration direction; feature-gate default; rollback strategy; preview URL or build; owner manual steps; evidence that trusted rewards aren't client-issued.
