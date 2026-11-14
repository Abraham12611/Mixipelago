# 39 — Requirement Traceability, Acceptance Gates and Definition of Done

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Traceability map
| ID | Requirement | Authority | Evidence |
|---|---|---|---|
| PR-01 | XP from verified first clear only | Batch4 result + Batch7 awards | concurrent idempotency integration test |
| PR-02 | Level curve and milestones exact | Batch7 XP policy | integer vector and property tests |
| PR-03 | Skill allocation cannot overspend | Batch7 trusted API | two-device race test |
| PR-04 | All enabled nodes reachable | Batch7 catalog | schema/DAG/feasibility validator |
| PR-05 | Effects source-attributed/capped | Batch6 resolver + Batch7 catalog | modifier golden vectors |
| PR-06 | Ranked unaffected by personal build | Batch4 competition + Batch7 normalization | novice/max account identical standardized snapshot |
| PR-07 | Respec does not remove XP | Batch7 refund service | atomic respec and retry test |
| PR-08 | Mobile and desktop usable | Batch7 UI | owner manual approval, keyboard accessibility |
| PR-09 | Local preview never trusted | Batches1–6 | forged grant negative test |
| PR-10 | Versioned rollback works | Batch7 publishing | staged revert drill |

## Definition of done for v0.4.0
Documentation and fixtures reviewed; six early nodes implemented under guards; trusted XP grant integration with verified mission; points earned and allocated transactionally; server receives no client-supplied XP amounts; profile UI works on desktop and mobile; automated tests cover all P0 scenarios; error states match API contracts; no secret nodes exposed; economy/payout caps documented; owner receives a test build and approves manual UI; deploy and rollback checklists signed.

## Evidence classification
`DOCS_READY` means specification exists. `STATIC_VALIDATED` means schemas and vectors pass. `IMPLEMENTED` means code merged. `QA_VERIFIED` means automated integration and security gates pass. `OWNER_APPROVED` means manual interface acceptance. `RELEASED` means production deployment observed. Do not use one label in place of another.
