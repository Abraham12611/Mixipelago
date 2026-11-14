# 23 — Verified Technical References, Licensing Checklist, and Glossary

**Research checked:** 2026-11-14. These are primary/reference URLs for engineers, not proof that APIs have been implemented or tested in the Mixipelago codebase. Pin exact installed dependency versions and compile against their corresponding types before making assumptions.

## Phaser

- Phaser 4 official release listing: https://phaser.io/download/phaser4 — lists v4.0.0, 4.1.0, 4.2.0 and 4.2.1 (July 9, 2026).
- Phaser 4 changelog: https://github.com/phaserjs/phaser/blob/master/changelog/v4/4.0/CHANGELOG-v4.0.0.md — renderer architecture and migration considerations.
- Phaser docs: https://docs.phaser.io/ — camera, scale, scene/input/game objects. Use docs matching your pinned major/minor version.
- Phaser GitHub: https://github.com/phaserjs/phaser — source/issue tracking.

## Rapier (must-read)

- JavaScript overview: https://rapier.rs/docs/user_guides/javascript/getting_started_js/
- Rigid bodies: https://rapier.rs/docs/user_guides/javascript/rigid_bodies/
- Forces and impulses: https://rapier.rs/docs/user_guides/javascript/rigid_body_forces_and_impulses/
- Colliders, friction/restitution: https://rapier.rs/docs/user_guides/javascript/colliders/
- Advanced collision events and contact graph: https://rapier.rs/docs/user_guides/javascript/advanced_collision_detection_js/
- Integration parameters (fixed steps/CCD): https://rapier.rs/docs/user_guides/javascript/integration_parameters/
- Determinism: https://rapier.rs/docs/user_guides/javascript/determinism/
- Scene queries/raycast and shape cast: https://rapier.rs/docs/user_guides/javascript/scene_queries/
- Rapier source/release: https://github.com/dimforge/rapier
- Rapier npm build variants (`-compat`, `-deterministic`, `-deterministic-compat`): https://www.npmjs.com/package/@dimforge/rapier2d-compat

**Important version nuance:** Rapier's official JavaScript determinism guide describes cross-platform deterministic execution under identical initialization and fixed timestep. NPM also distributes explicitly deterministic builds. The engineering team MUST check which package build is pinned and test its actual replay behavior; do not treat any generic `-compat` package as automatically the strongest guaranteed option. Game-level determinism remains a separate engineering responsibility.

## Browser/web platform

- Pointer events: https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events
- Pointer capture: https://developer.mozilla.org/en-US/docs/Web/API/Element/setPointerCapture
- `touch-action`: https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action
- Page Visibility API: https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API
- Web Audio API: https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API
- Device Pixel Ratio: https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio
- WebGL context loss: https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/webglcontextlost_event
- Web Workers: https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API
- WCAG 2.2 overview: https://www.w3.org/TR/WCAG22/

## Testing and development

- Vitest: https://vitest.dev/
- Playwright: https://playwright.dev/
- Zod: https://zod.dev/
- Fast-check: https://fast-check.dev/ (optional property-based testing)
- TypeScript: https://www.typescriptlang.org/docs/

## Asset/audio references

- FLORA: https://flora.ai/
- Tripo 3D: https://www.tripo3d.ai/
- Meshy: https://www.meshy.ai/
- Blender: https://www.blender.org/
- ElevenLabs: https://elevenlabs.io/
- WeLoveIndies: https://www.weloveindies.com/
- Capacitor: https://capacitorjs.com/docs

Artist/producer must review commercial licensing of all generated/licensed asset families. The first prototype may use original placeholder shapes and curated art; screenshots of Merge Shooter are **not production asset sources**.

## Engine/physics glossary

| Term | Meaning in Mixipelago |
|---|---|
| Rigid body | Simulated moving glass footprint with position/velocity |
| Collider | Shape that participates in collision, alpha uses circles |
| Static body | Immovable boundary/rail |
| Sensor | Overlap detector without physical impulse |
| Restitution | Elasticity of normal collision response |
| Contact friction | Resistance to tangential relative movement during collision |
| Linear damping | Ongoing movement resistance/drag approximation |
| Angular damping | Ongoing rotational resistance |
| CCD | Continuous Collision Detection; reduces tunneling at high speed |
| Fixed timestep | Simulation advances in uniform increments, independent of rendering frames |
| Interpolation | Cosmetic rendering between previous and current physics poses |
| Contact normal | Direction along which two objects push apart at contact |
| Contact manifold | Contact geometry from physics solver, may include multiple points |
| Penetration | Geometric overlap between colliders needing resolution |
| Impulse | Instantaneous momentum change to launch body |
| Mass/density | Physical body inertia properties, scaled to world units |
| Pair arbitration | Choosing nonconflicting merges from simultaneous contacts |
| Chain root | Originating shot/merge ancestry of a multi-step cascade |
| Spawn queue | Seeded order of upcoming drink tiers |
| Danger grace | Fixed-step window during which boundary intrusion is recoverable |
| Snapshot | Captured physics/logical state for rendering/save/replay diagnostics |
| Replay log | Canonical initial state and inputs needed for reproduction |
| Golden test | Approved simulation transcript with expected outcome/hash |
| Domain event | Immutable semantic fact such as `drink_merged` |
| Rendering event | Non-authoritative visual/audio occurrence |
| Idempotency | Reprocessing same command/event doesn't produce a second effect |
| WASM | WebAssembly binary used by Rapier in browsers/Node test runtime |
| 2.5D | 3D-looking illustration presented on 2D physics/render planes |

## License and provenance acceptance checklist

For every imported third-party dependency or asset: record name, version, URL, license, attribution requirements, commercial game usage permissions, modifications, authoring source and update owner. For generated AI assets record tool, model/version if available, input/reference provenance, edits, and usage approval. A logo or screenshot cannot be assumed free to reuse just because it is visible online.
