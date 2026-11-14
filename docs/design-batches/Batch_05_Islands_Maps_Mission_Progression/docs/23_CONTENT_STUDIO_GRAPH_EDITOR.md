# 23 — Internal Campaign Graph Editor and Content Studio Workflow

## Editor purpose
Designers must be able to draw island routes, attach missions, create gates, place landmarks and validate reachability without submitting changes to the physics engine. Begin with JSON + validation CLI; upgrade to internal visual authoring as content volume grows.

## Main editor surfaces
1. **World Atlas:** list islands and publication states; duplicate draft template; define entry/gateway.
2. **Island Canvas:** pan/zoom and drag node anchors, curve route control points, edit layer/z-index.
3. **Node Inspector:** stable ID, type, mission ref, localized copy, icon, priority, status, unlock rule and reveal rule.
4. **Route Inspector:** edge kind, source/destination, line style, hidden/reveal policy, content dependencies.
5. **Progress Preview:** emulate player receipts and flags; show available, locked, hidden, mastered projection.
6. **Graph Linter:** missing refs, cycles, unreachable critical nodes, hidden mandatory paths, unsupported modes, duplicate rewards.
7. **Publishing:** review changes by hash, approval status, canary targets, rollback pointer and compatibility reports.

## Authoring workflow
Create draft from existing island → add nodes and paths → attach actual published mission refs → connect prerequisites explicitly → run static/schema checks → run golden-replay proof for new puzzles → artist applies decor and safe-area inspection → owner manual approval → stage and publish immutable graph revision.

## Permissions and audit
Content authors can draft; reviewers can approve; publishers can advance active pointers. Record actor/time/reason/content hash; prohibit ordinary players from loading unpublished graph, premium rewards and editor debug data. A published node can't be silently deleted: retire it or publish a migration mapping.

## Diff tools
Show node additions/deletions, moved anchors, changed gate expressions, changed mission refs, unlocked/more-restrictive paths, and changes to first-clear reward references. Flag any publication that would move an existing player's progress backward.

## Preview fixtures
Provide 'fresh guest', 'after Cove 001', 'after Cove 002', 'branch A only', 'branch B only', '3-star mastery', 'older save version', 'hidden revealed' and 'no available mission' profiles. Preview must display both portrait and desktop card positions.

## Development priorities
A minimal `/dev/map-lab` can be built for v0.2.x, with draft JSON upload and drag anchors. An advanced collaborative editor waits until content throughput demands it. Do not deploy editor endpoints publicly without authorization.
