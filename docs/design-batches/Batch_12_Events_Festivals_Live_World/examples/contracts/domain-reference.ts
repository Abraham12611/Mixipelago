/** Mixipelago design reference only. Not shipped code. */
export interface VersionedEnvelope<T> {
  eventId: string; schemaVersion: 1; occurredAt: string;
  rulesHash: string; actorId?: string; payload: T;
}
export interface EventEdition {id:string; startsAt:string; scoringClosesAt:string; claimsCloseAt:string;archiveAt:string;}
export function scoringIsOpen(e:EventEdition,serverUtcIso:string):boolean {
  return e.startsAt <= serverUtcIso && serverUtcIso < e.scoringClosesAt;
}
export function claimWindowOpen(e:EventEdition,serverUtcIso:string):boolean {
  return e.startsAt <= serverUtcIso && serverUtcIso < e.claimsCloseAt;
}
