# 02 — World Coordinates, Board Geometry, Rendering Perspective, Camera

## Coordinate authority

The physics world is a **top-down horizontal plane** and uses game-world units rather than CSS pixels. `+x` points right, `+y` points toward the player's lower screen, `0,0` is the top-left of the logical board. Gravity in this plane is zero. Art assets may depict a slanted table, but the collision geometry remains planar.

Illustrative board extent: 10 units wide × 15 units high, with a visible play area, launch region and danger line. These are starting values and must be validated for actual sprite footprint, portrait aspect ratio and comfortable UI spacing. Use config `worldBounds` to avoid hardcoding dimensions.

```
(0,0) +---------------------------------+ (10,0)
      | STATIC TOP WALL               |
      |   o   o              o        |
      |         DRINK FIELD           |
      |   o                             
      |                                 |
      | - - - DANGER LINE y=12.8 - - - |
      |        LAUNCH ORIGIN           |
      +---------------------------------+
(0,15)                              (10,15)
```

The danger line is a game rule, not necessarily a physical collider. Side/top rails can be static colliders. The launch area has its own spawn-overlap/arming rules.

## World-to-screen transform

For a simple unrotated board camera, if `s` is pixels per world unit and `(ox, oy)` is the logical viewport offset:

```
screenX = ox + worldX * s
screenY = oy + worldY * s
worldX  = (screenX - ox) / s
worldY  = (screenY - oy) / s
```

For nested CSS, browser zoom, device pixel ratio, dynamic canvas resizing, and camera zoom, use Phaser's current world-point input transform or invert the canonical camera transform. Avoid duplicating an approximation in DOM code. The conversion must be tested with padded layouts and letterboxing.

## Responsive layout principle

**Mobile:** portrait viewport, board centered and tall, two customer cards/bubbles above, next drink and boosters below. Preserve logical field proportions; crop or scroll cosmetic scenery, not the playable collision region. Larger touch targets. Do not allow UI overlays over the aim corridor.

**Desktop:** landscape browser with optional left customer panel and right goals/boosters; central board occupies fixed or proportionate area with enough empty surrounding space. The physical board world size and mission should remain the same as mobile for fair conditions. Camera scale/viewport may differ, not world collision physics.

## Perspective art warning

A perspective trapezoid tabletop image makes upper objects look smaller. If raw physics `x,y` is mapped linearly to a trapezoid without accounting for changing screen width, the visible edge and actual collision boundary diverge. For alpha, choose a *near-top-down table texture* or map the geometry through a deliberate reversible coordinate transform. Never invent a non-invertible transformation for input. Shadow placement, vertical squash and sprite scale-by-depth can convey perspective without distorting the simulation plane.

## Sprite anchors and collision footprints

Each drink asset has:

```ts
type DrinkVisualMeta = {
  assetId: string;
  renderedWidthPx: number;
  renderedHeightPx: number;
  anchorX: number;        // 0..1, nominal bottom-center base
  anchorY: number;
  contactFootprintRadiusWorld: number;
  shadowOffset: { x: number; y: number };
  visualTiltLimitDeg: number;
};
```

The sprite image might be 130 px high while the collision base is a circle of radius 0.34 world units. Contact positions refer to the foot of the glass, not its top umbrella or flowers. For the base art, render shadows separately or preserve clean separation so wobble does not rotate a flattened shadow implausibly.

## Camera contracts

- `CameraPort.worldToScreen(world)` and `.screenToWorld(screen)` must be pure/testable at fixed layout config.
- `GameWorldViewport` supplies bounds and pixel scale after resize; gameplay code never accesses `window.devicePixelRatio` to calculate collisions.
- Device orientation changes pause launch and recompute transform; an in-progress aim gesture is cancelled.
- Support a debug overlay with world axes, collider centers and table borders in development builds.
- The HUD may update independently at 10–20 Hz; physics renderer updates at display rate.

## Geometry invariants

1. A world coordinate must project to the same semantic point regardless of screen aspect ratio.
2. A sprite's foot and its collider center remain aligned within an explicit allowable visual offset.
3. Launch origin stays inside the board after any resize.
4. A lower danger zone is visually marked and defined using world units; never use `screenY > 900` logic.
5. The camera must be stable during aiming; animated camera moves cancel or suspend input.

## Automated verification

Test round-trip `screen → world → screen` for top-left, center, bottom boundary, and each launch corner, across portrait, narrow Android, desktop ultrawide, browser zoom 125%, and canvas letterbox. Numeric tolerance: <=0.5 physical display pixels for debug geometry; tolerance may be tuned based on rendering resolution but must not conceal systematic drift. Snapshot tests ensure overlay elements do not cover the active shooter field. Owner manually checks perspective fairness on devices.
