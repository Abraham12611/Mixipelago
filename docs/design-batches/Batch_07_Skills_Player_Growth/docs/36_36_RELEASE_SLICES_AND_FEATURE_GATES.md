# 36 — Release Roadmap: First Skill Slice Through Full Tree

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Version increments, not one giant launch
| Version | Gated deliverable | Exit criterion |
|---|---|---|
| v0.1.x | no trusted XP/skills; preserve local preview rules | alpha playable, no accidental points |
| v0.2.x | campaign mission receipts and graph integration | verified mission identity and first clears |
| v0.3.x | trusted wallet and one starter shop (Batch 6) | ledger, security and purchase review |
| **v0.4.0** | trusted Entrepreneur XP/level/points; 2 pilot branches and 6 simple published nodes; profile reads, allocation API/UI | concurrency + award + respec gate tests; owner approval |
| v0.4.1 | progressive UX, build planner, respec, better explainability | safe rollback and full keyboard/mobile tests |
| v0.4.2 | all six branches gradually enabled if dependent systems exist; mastery draft preparation | content graph and effect policy approval |
| v0.5.x | competitive normalization and visible skills suspension | replay/proof and fairness validation |
| v0.6+ | event/risk skills, active abilities, mastery and season specials | per-feature proof, not blanket enablement |

## v0.4.0 minimum slice
Trust source XP only from verified first clears (no per-merge farming); level cap 20; grant one point each at levels 2–20; only six early nodes across Mixologist/Hospitality whose effects are implemented. UI shows other branches as `Coming later` or omits them. Do not expose unusable Learn buttons. The catalog fixture labels future nodes `draft` so a release gate cannot accidentally activate them.

## Dependency gates
Shop-affecting skill requires the trusted shop wallet/order reward service and batch6 modifiers; recipe mastery requires Batch3 verified mastery; map secret hint requires Batch5 authorized graph; incident protection requires Batch10 published event system. No feature claims full capability while dependency is stubbed.

## Rollout
Dev → deterministic QA accounts → staff beta → opted-in early cohort → general availability. Each phase has kill switch, migration dry run, telemetry alert thresholds, support playbook and owner approval. Shipping docs or merging a spec PR does **not** constitute deploying gameplay.
