# 25 — Character Art, Portraits, 2.5D States and Asset Pipeline

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Direction
Customers share Mixipelago's original bright tropical 2.5D visual language: clean silhouettes, expressive eyes/faces, consistent lighting, restrained highlights and clear palette hierarchy. References from competitor screenshots may inform genre polish, **not** exact pose, costume, screen composition or character silhouette.

## Per-customer asset manifest
```
customerId, artVersion, portraitSmall, portraitLarge,
idleState, greetState, happyState, waitingState,
optionalWarningState, optionalDisappointedState,
shadowStyle, speechBubbleAnchor, paletteTags, accessibilityAlt
```
For alpha, portraits + two emotional states are enough. Hero character animations can use layered PNG/WebP frames, spritesheets, Spine/Rive selectively, or 3D rendered turntables if economical. A generated AI image is not automatically a usable clean vector SVG.

## Tool workflow
Concept art / variations in FLORA; optional modeled props in Tripo/Meshy; human consistency review; Photoshop/Krita/Blender refinement; export to WebP/AVIF/PNG atlases; quality-tier and memory checks; publish in versioned CDN manifest. Keep original artwork and license/provenance notes per asset.

## Performance limits
Do not load every island's entire NPC gallery into the gameplay scene. Preload only visible orders and imminent replacement candidates, release textures on scene exit, reuse common animation effects, and provide non-animated static fallback at low graphics quality. Optimize asset sizes via actual mobile-browser memory profiling.

## QA
Verify visual continuity across states, readable orders at 40–64 CSS px, transparent edge halos, correct sprite origins, no portrait texture memory growth across 50 retries, portrait failure fallback, and no watermarks or unauthorized third-party art.
