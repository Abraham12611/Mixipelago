/** Mixipelago reference-only pure rules. No network, wallet grant or production integration. */
export type Decision<T> = { ok: true; value: T } | { ok: false; code: string };
export type DeviceProfile = { ramMiB:number; gpuBudgetMiB:number };
export function visualTier(d:DeviceProfile):'low'|'mid'|'high' {
 if(d.ramMiB < 2500 || d.gpuBudgetMiB < 64) return 'low';
 return d.ramMiB >= 5000 && d.gpuBudgetMiB >= 160 ? 'high' : 'mid';
}
export function offlineIsVerified():false { return false; }
export function requiresUpdate(clientSchema:number,minSchema:number):boolean {return clientSchema < minSchema;}
// Real device support and budget thresholds require owner-approved hardware testing.
