# 19 — Base44 Platform Feasibility Spike

**Goal:** establish within the first engineering checkpoint whether the **new Base44 game itself** can host the real physics puzzle with correct browser controls and documentation of how it was built.

## Research basis

Base44 publishes [CLI docs via GitHub](https://github.com/base44/cli) including create/link/deploy and a React/Vite starter, and [GitHub sync guidance](https://base44.com/blog/news/base44-github-integration). Capabilities, quotas and project wiring can change: test actual service and account, do not infer success from documentation.

## Spike experiment matrix

| Experiment | Steps | Pass criterion |
|---|---|---|
| Project provenance | Create new Base44 project; take screenshot of project age and prompt history | Created within Nov 5–Dec 3; real Base44 editing |
| Public guest access | Publish; open in clean anonymous browser | Public Base44 URL loads without auth/paywall |
| Dependency integration | Try Phaser scene module in Base44 project | Canvas launches on desktop and mobile with no CORS/build errors |
| WASM | Load pinned Rapier WASM in published app | Physics starts, contact event works, no unsupported import |
| Touch | Drag/aim/release/cancel across viewport sizes | No stuck pointer; launching doesn't scroll page |
| Camera/viewport | Resize 320px → desktop | World transform stable, HUD readable |
| Asset loading | PNG/WebP sprites, audio user gesture | No 404/CORS; fallback if audio disabled |
| Persistence | Save mission completion locally, refresh | Versioned save loads or gracefully resets |
| Code sync | Sync specific new contest code to GitHub | No destructive replacement; commits attributable |
| Evidence | Export sanitized creation/edit/deploy history | Owner can show Base44 substantive build |

## Report template

~~~text
Experiment ID:
Environment/date:
Base44 project ID (private if needed):
Base44 public URL:
Pinned dependency versions:
Steps:
Expected:
Actual:
Console errors:
Evidence link:
Pass/fail:
Fallback decision:
Owner acceptance needed:
~~~

## Gate logic

**A: all critical tests pass** — proceed with Phaser + Rapier inside new Base44 app and the original drink/serve rules.

**B: Phaser works but Rapier fails** — implement simple pinned collision mechanics in-project. Revalidate sliding/contact/danger with owner and pure-rule tests; avoid covert change to match older video.

**C: both fail** — build a controlled Canvas physics puzzle within Base44 rather than shipping an iframe from elsewhere. Reduce level count and visual FX. Must still be original and playable.

**D: public Base44 URL or project-build requirement cannot be met** — STOP. Do not submit an ineligible external game as though it qualifies.

## Organizer clarification

Email **base44xnitro@overwolf.com** as soon as custom tooling uncertainty appears:

> I'm creating a new Base44 web game during the contest period, using Base44 for its actual application screens, project and publishing. The gameplay canvas may use a custom Phaser and Rapier integration, with code synchronized via Base44's documented GitHub/CLI workflow. Does this satisfy your requirement that the game be "built using the Base44 platform"? The project is new, with a documented creation/edit history. I want to confirm compliance before submitting.

Do not represent silence as approval. If prior ideation or source references might be construed as pre-existing, include truthful details and ask the organizer directly.
