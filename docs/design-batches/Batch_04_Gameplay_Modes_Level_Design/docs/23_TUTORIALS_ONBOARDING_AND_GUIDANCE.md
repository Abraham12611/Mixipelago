# 23 — Tutorial Script, Progressive Disclosure and Player Learning

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Tutorial objective
A first-time player understands drag-to-aim, release-to-shoot, same-tier merging, automatic serving, upcoming drink preview and danger line without reading a wall of text. The tutorial is actual interactive game state, not a fake screenshot.

## Suggested teaching sequence
1. **Welcome:** show one prominent next drink, one matching tier on table; lock unrelated buttons. Prompt “Drag toward the matching drink.”
2. **Aim:** dim unrelated UI, highlight launch zone; tutorial acknowledges a valid drag vector without launching by itself.
3. **Release:** player fires; physics genuinely simulates impact.
4. **Merge:** when legal pair commits, explain two matching drinks become one higher tier and point at the upgraded result.
5. **Serve:** if result matches oldest order, highlight order bubble and score/coin animations after reduction, not before.
6. **Preview:** show next item and allow player to plan one more shot.
7. **Pressure:** explain dashed danger line with a controlled example or contextual hint, never deliberately trigger unavoidable failure.
8. **Finish:** show two fulfilled orders, win, results and Replay/Continue.

## No fake deterministic success
Do not script UI to show an animation without actual physics/events. Tutorial must have an authored deterministic seed/starting state and verified successful input path. If the shot misses, give gentle instruction and allow retry, not secretly teleport a glass into contact.

## Mode introductions
Classic: merge + order. Precision: shot counter; final shot resolution. Rush Hour: clock only counts while active. Chain Challenge: connected sequence preview. Survival: wave schedule. VIP: multiple order lines and phased goals. Endless: reset and opt-in no-pressure experience.

## Contextual hints
Signal on first prolonged hesitation, repeated unsuccessful near-misses, or after first failure. Hints must not be punitive, able to be dismissed, and avoid occluding table. Respect reduced motion and lower literacy contexts; tooltips use short action verbs and accessible labels.

## Tutorial state schema
`onboardingVersion`, `stepId`, `completionFlags`, `snoozed`, `inputAllowed`, `featureGate`. Guest preview state local for alpha; trusted profile setting later. Updating tutorial script should not reset completed campaign progression.

## Test cases
Touch 360 CSS px viewport, mouse/keyboard alternative, interruption, dismissed tutorial, failed first shot, replay tutorial, asset load fallback, localization expansion, screen reader focus. Owner performs manual flow approval.
