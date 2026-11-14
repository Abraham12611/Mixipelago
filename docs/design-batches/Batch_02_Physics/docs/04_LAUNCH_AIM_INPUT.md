# 04 — Shooting, Aiming, Input Gestures, and Trajectory Preview

## Primary alpha gesture

The proposed alpha input is **drag toward intended direction, release to fire**. The player starts a gesture near the launch area, drags toward an intended point within the aim cone, and releases. Shot force is fixed in v0.1.0. The alternative pull-back slingshot gesture should be implemented in the physics lab, not automatically shipped. One canonical `AimVector` reaches SimulationCore regardless of mouse, touch, keyboard or optional gamepad.

## Public flow

1. Display active drink and separate `Next` queue preview; user understands which item will move.
2. On pointer down in eligible aim zone and session `ready`, capture pointer ID. Reject secondary pointer, modal overlap, or disabled state.
3. Convert client coordinates to world using canonical camera input mapping. Record `start` and `current`; show preview arrow only after drag passes `minAimDragWorld`.
4. Aim direction = normalized `(current - start)`; clamp direction to configured forward-facing cone (up-screen is negative Y). In alpha shots must have `dy < 0` after clamp and cannot fire backward into controls.
5. Optional aim ray shows direction and a **clearly approximate** first impact if using ray/shape cast; do not indicate a guaranteed final resting place on a dynamic board.
6. On pointer release, validate session state, pointer ID, drag threshold, normalized magnitude and spawn clearance. Enqueue `LaunchCommand` for next fixed-step boundary.
7. Advance pending-aim state to committed; show a shot FX frame and fire confirmation; consume next queue item exactly once only after command is accepted.
8. Cancel or reject cleanly; no coins, shots or inventory consumed on cancelled input.

## Gesture edge cases

- Repeated `pointerdown` while aiming: ignore non-owner pointer; optionally show gentle feedback once.
- Two-finger pinch, second finger or OS gesture: cancel current aim; don't send a shot.
- `pointercancel`, loss of focus, browser tab hidden, orientation change, menu opens: cancel with reason and release capture.
- Tap without drag: not a shot by default; show one-time hint. Later setting may allow tap-to-aim and tap-to-shoot accessible mode.
- Drag into browser chrome or off canvas: cancel consistently; do not accidentally launch on pointer leave.
- Rapid double-release or duplicate events: rejected by command ID/state; no double shot.
- Press while FX in progress: if `ready`, input may be allowed after clear cooldown. During `launched/resolving`, show next-preview disabled state and do not silently queue unbounded shots.
- Left-handed players: any symmetrical launch control position; do not force controls on right side.

## Aim geometry

Let `p0` = gesture start in world units, `p1` = current pointer world position, `v=p1-p0`, `n=v/|v|`. If `|v| < minDrag`, no shot. Determine an angular limit around forward vector `(0,-1)`. Rather than trusting a visual polar-angle sign, use vector dot and orientation rules with unit tests:

```
forward = {x: 0, y: -1}
allowed = dot(normalize(v), forward) >= cos(maxAimAngle)
```

Proposal: `maxAimAngle=75°` from forward (don't allow near-horizontal hits at spawn until tested). Clamp the direction onto the nearest admissible boundary if pointer exits the cone; render the clamped direction so the player isn't surprised. `Math.cos` is fine for *visual interaction* but for cross-platform deterministic ranked replays record a canonical quantized direction and let the simulation consume that, not re-run untrusted browser trig.

## Quantizing launch commands for replay

The committed command uses normalized and quantized direction components, e.g. signed int16 `(-32767..32767)` with explicit round-to-nearest rule, or a compact discrete angle index. The server/physics converts the command to a unit vector in a deterministic, tested way. A canonical directional representation ensures different pixel layouts don't alter game state. `power` is omitted or fixed in alpha. Proposals for variable power must specify min/max, drag-to-power curve and accessibility implications.

Example command:

```json
{
  "type": "launch",
  "commandId": "local-52",
  "sessionId": "session-demo",
  "step": 180,
  "aim": { "x": 0.24, "y": -0.970772 },
  "shotMode": "fixed",
  "nextQueueIndex": 4
}
```

This JSON uses decimals for readability; a strict replay protocol will use canonical integer/decimal encoding rather than a casual float string.

## Preview options

- Alpha: short line from launch point in aim direction, 1–2 projected table units, with low-opacity arrowhead. No collider prediction necessary.
- v0.1.1: optional shape-cast first-collision marker. It predicts geometry at the current instant and must update as objects move. It is not a perfect multi-bounce trajectory; display as suggestion.
- Later: full trajectory simulation in copied physics world, but only if performance and fairness allow; a high-accuracy guide may become a player skill/booster and must not unfairly leak competitive outcomes.

## Desktop controls

Pointer hold-and-drag is primary. Keyboard alternative for accessibility and QA: Left/Right adjust aim by a fixed degree step, Up resets forward, Space/Enter fires when eligible, Escape pauses; key repeats at controlled intervals. Prevent scroll when game canvas is focused and shortcuts are active. Do not capture keyboard shortcuts in text inputs. Map tooltips and help text clearly.

## Mobile controls

On game canvas only, `touch-action: none`. Outside the canvas, ordinary page navigation remains usable. Aim region must be usable around gesture bars and safe areas. Support landscape and portrait changes by cancelling in-progress aim. Address passive listener behavior where direct DOM handlers are used. Use pointer events as a unified API when practical and verify on iOS Safari and Android Chrome.

## Accessibility fallback

Offer an "Aim Assist" option that uses keyboard/on-screen angle arrows and a separate large fire button, avoiding a precision drag gesture for players with limited dexterity. It must not change the physics outcome for the same chosen angle. Aim marker should have contrast in bright and dark scenes; do not rely on color alone. Reduced-motion mode removes nonessential trajectory wobble, not aiming information.

## Acceptance

Release 20 consecutive shots on each desktop/mobile target without accidental double fire, broken pointer capture, layout-dependent aim offset, or off-screen launch. Keyboard input can perform every required alpha action. Owner tests feel manually; automation covers the geometry and state machine.
