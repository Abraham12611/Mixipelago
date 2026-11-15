# 03 — Base44-first Architecture and Project Provenance

## The eligibility-critical constraint

Build **a new app in Base44 in the contest window** and publish that app on a Base44-hosted URL. Base44 should be a substantive part of the actual game application: shell, screens, game session wiring, responsive controls and published build, not a proxy page to externally hosted gameplay.

**Platform facts, not eligibility guarantees:** Base44 documents GitHub sync, a CLI for project creation/link/deploy, React/Vite templates and managed hosting. These tools suggest a plausible development path but do not independently certify that a custom engine integration satisfies section 6.1(b/c). Obtain written organizer confirmation if in doubt.

References: [Base44 CLI](https://github.com/base44/cli), [GitHub integration](https://base44.com/blog/news/base44-github-integration), [Contest terms](https://nitropay.com/base44webgame/terms-and-conditions/).

## Proposed runtime layout

~~~text
New Base44 contest project (public Base44-hosted app)
  /            Guest launch/home
  /play        React game shell + embedded in-app Phaser scene
  /map         Coconut Cove missions, local progress
  /results     Session result UI; no trusted payout
  /settings    Audio, reduced-motion, local data controls
  assets       Original game sprites, SFX, music and fonts
  game/
    input/     Pointer/touch/keyboard to simulation command
    physics/   Rapier (conditional on Base44 compatibility)
    core/      Pure TypeScript score/order/merge reducers
    content/   Versioned mission and drink catalogs
    render/    Phaser scene, input hit testing and FX
    save/      Versioned guest storage
~~~

- **React** owns navigation, accessible HUD controls, settings and results.
- **Phaser** renders board and animation; **Rapier** proposes physical contact semantics. Pin tested versions, not unverified imports.
- Fixed 60Hz simulation with accumulation cap, independent of render rate. Freeze state on pause; use deterministic commands, not click-driven reward mutations.
- Use pure reducer layers for scoring, orders, terminal outcomes; avoid React state being the physics authority.
- Local first version persists mission bests and settings in localStorage/IndexedDB, with schema migration and corruption recovery.
- No account or trusted economy service is needed. If an optional Base44 entity function is used, it must not become a login dependency.

## Essential feasibility spike — before feature coding

1. Create new Base44 project and save creation timestamp, project ID and prompts.
2. Build genuine Base44 game/home/map UI; verify public anonymous access on a **Base44 URL**.
3. Add tiny in-project playable canvas: drag → launch → physics collision → one merge and reset.
4. Test memory/performance, touch pointer capture, wasm loading, static assets and built site under Base44 hosting.
5. Test CLI/GitHub sync from that Base44 project; record whether it preserves Base44 edit history.
6. Contact organizers about Phaser/Rapier and any external-source linkage if use is substantial. Record response.
7. Only then decide to retain the original engine or simplify, and document reasons.

## Fallback decisions

**A:** Phaser + Rapier in Base44 if fully functional and acceptable.  
**B:** Phaser Arcade/handwritten simple deterministic circular physics for a smaller board if Rapier WASM fails, with explicit new physics tuning.  
**C:** pure Canvas 2D, authored collision/merge loop and responsive UI if both integrations fail.  

Never frame a third-party hosted iframe as the fallback. Changes to collision semantics require new tests and owner gameplay acceptance.

## Build evidence

Capture creation timestamp (UTC); Base44 prompt and edit history (export securely); linked source commit SHAs; live deployment ID/URL; a screen recording showing the Base44 editor and playable URL. Do not upload private tokens/session cookies to GitHub.
