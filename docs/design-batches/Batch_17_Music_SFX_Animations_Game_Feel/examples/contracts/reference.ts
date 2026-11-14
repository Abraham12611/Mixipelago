/** Mixipelago reference-only pure rules. No network, wallet grant or production integration. */
export type Decision<T> = { ok: true; value: T } | { ok: false; code: string };
export type Cue = { id: string; event: string; maxVoices: number; bus: string; enabled: boolean };
export function shouldPlay(eventId: string, seen: ReadonlySet<string>, activeVoices: number, cue: Cue, audioUnlocked: boolean): boolean {
  return audioUnlocked && cue.enabled && Number.isInteger(cue.maxVoices) && cue.maxVoices > 0 && activeVoices < cue.maxVoices && !seen.has(eventId);
}
export function effectiveGain(master: number, bus: number): number { return Math.min(1,Math.max(0,master)) * Math.min(1,Math.max(0,bus)); }
// AudioContext creation/resume must happen in a real user gesture; never in the simulation reducer.
