# 36 — Risk Register, Anti-patterns and Engineering Failure Postmortems

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## High-risk implementation failures
| Risk | Player symptom | Root cause | Protection |
|---|---|---|---|
| Event double count | two coins/points from one merge | collision event repeated | unique event IDs + claimed bodies |
| Impossible level | every run fails despite good play | lack of solver + auto-serve conflict | golden playthrough gate |
| Timer unfairness | fail after switching apps | wall-clock timer used | active-tick timer + hidden pause |
| Unfair rankings | premium users dominate | ranked inherits skill perks | standardized mode policy |
| Nondeterministic replay | same seed gives different score | command timing or math differs | pinned WASM/version + golden hashes |
| Lost player progress | content change corrupts session | no manifest pinning | immutable versions + adapter |
| Low-end crash | mobile tab reloads | huge atlases/event log | memory budget + pooling |
| Mystery loss | warning line not visible | presentation disconnected | semantic warning + accessible cue |
| Flaky final shot | lose before merge resolves | instant shot exhaustion | awaiting_resolution state |
| Overloaded backend | every contact sent server | wrong architecture | local sim + server receipt later |

## Anti-pattern examples
“Add a new mode by copying physics code and tweaking arrays” → divergent collision rules. Instead instantiate mode policy with existing simulation.
“Make levels harder by randomly changing damping mid-run” → impossible-to-learn physics. Instead explicit physics preset or announced zone.
“Give diamonds for seeing a rare sprite effect” → exploitable client callback. Instead unique validated gameplay action.
“Precompute a win animation if user misses aim” → breaks player trust. Instead tutorial hints and curated easy geometry.
“Treat a JSON schema pass as proof of solvability” → content can still be unwinnable. Instead reproducible actual engine playthrough.

## Release risk response
Critical issues in live mode: disable new sessions, preserve active pinned runs where safe, publish status, gather crash traces and snapshots, patch, and re-enable behind a rollout flag. Do not force a broken session into success or failure to keep KPI numbers clean. Incident reviews identify failed test and new prevention case.

## Open design questions
Do we want time-up to be arcade completion or loss? Which mode deserves first post-alpha slot? Are stars based on shots, score, or time in each mode? Is Endless reset free and score-only? Should coins be granted repeatedly for replay? What constitutes an allowable hint in ranked mode? Owner answers before public mode release; no need to delay v0.1.0.
