# 43 — Requirement Traceability, Acceptance and Definition of Done

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Traceability matrix
| Requirement | Spec owners | Automated proof | Manual acceptance |
|---|---|---|---|
| Exactly-once reward claim | 04–06, 29–31 | Race test + ledger reconciliation | Owner sees one item |
| Verified achievement | 07–09, 32 | Forged-event rejection | Owner understands unlock path |
| Collection progress | 17–18 | Unique-item vectors | Owner checks album states |
| Purely cosmetic equip | 19–20 | Ownership/slot checks | Owner tests visual appearance |
| No duplicate first-clear rewards | 02–06, 14 | Cross-batch receipt test | Owner sees consistent wallet |
| Daily fairness | 11–13 | Time window/DST cases | Owner reviews pressure design |
| Reward transparency | 16, 23–27 | Schema lint + accessible UI | Owner approves copy and presentation |
| Safe rollout | 28, 35–38 | Feature flags + rollback test | Owner approves release gate |

## Minimum documentation DoD
All chapter links resolve; schemas parse; content catalog has unique IDs and valid references; pure vectors pass; sample SQL marked draft; version/prerequisite matrix names correct earlier authority; no text claims production feature implemented. ZIP archives are integrity checked.

## First production slice DoD (later engineering)
A verified mission results in one verified achievement entitlement; claim grants exactly one owned badge; concurrent requests converge; client refresh and multi-device reflect same state; denied RLS writes prove boundary; alerts and reconciliation operate; feature flag can disable new claims without removing earned badges; owner passes mobile and desktop manual flow.

## No false deployment claims
Static script validation cannot prove server replay, economic safety under load, browser usability, store eligibility or app performance. Product engineering must attach actual test evidence and owner signoff before public rollout.
