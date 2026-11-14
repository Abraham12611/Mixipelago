# 25 — Desktop UI: Skill Tree, Comparison and Planning

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Layout
Desktop route `/profile/skills` uses a left sidebar for archetypes, central expandable graph with relationship lines, right information panel for selected skill details, and a top level/points header. Use React for UI and SVG/Canvas only as necessary for graph edges; there is no reason to run a full 3D engine for a tree editor.

## Interaction
Hover reveals concise details; click selects a node; keyboard Tab/arrow navigation accesses the same controls. Show level gates and missing prerequisites in plain language. A comparison mode can preview `current build` versus `proposed build`, including exact monetary/probability contributions and caps.

## Build planner
Changes remain **local drafts** until an explicit Apply action. Simulate cost, incompatible nodes, active-slot capacity and effective-stat differences; the server validates every applied change atomically. Export/import of build strings is permissible only as untrusted preference data; no privileges or points are granted from imported data.

## Responsive behavior
At tablet widths, collapse the right panel into a slide-over. At narrow widths, use the same list/tree state machine as mobile. All Graph dependencies can be serialized as a text list and compared for accessibility.

## QA
A player switching between laptop and phone sees the same rank allocations. Cursor hover is not the only way to reveal details. The UI is resilient to load latency and stale profile revisions.
