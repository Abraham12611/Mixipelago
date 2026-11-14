/** Mixipelago design reference only. Not shipped code. */
export interface VersionedEnvelope<T> {
  eventId: string; schemaVersion: 1; occurredAt: string;
  rulesHash: string; actorId?: string; payload: T;
}
export type IncidentState = 'offered'|'accepted'|'declined'|'active'|'resolved'|'expired'|'archived';
export interface WorldSnapshot {id:string; islandId:string; conditionId:string; startsAt:string; endsAt:string; contentHash:string;}
export interface IncidentOffer {offerId:string;playerId:string;version:number;state:IncidentState;choices:ReadonlyArray<string>;}
export function canChoose(offer:IncidentOffer,choiceId:string,expectedRevision:number) {
  return offer.state==='offered' && offer.version===expectedRevision && offer.choices.includes(choiceId);
}
export function normalizedWeatherModifier(ranked:boolean, visualOnly:boolean, candidate:number) {
  return ranked || visualOnly ? 0 : candidate;
}
