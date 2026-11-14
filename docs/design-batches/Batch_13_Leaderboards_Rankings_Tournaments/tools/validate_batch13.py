#!/usr/bin/env python3
"""Batch 13 sample content validator (documentation-only). Requires jsonschema."""
from pathlib import Path
import copy,json,sys
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
NUM=13

def domain_validate(num,c):
    errors=[]
    if c.get('batch')!=num:errors.append('batch identity mismatch')
    if c.get('status') not in ['draft_disabled','draft_tokens']:errors.append('no draft status')
    if num==10:
        cond={x['id'] for x in c['conditions']}
        for w in c['windows']:
            if w['conditionId'] not in cond or not w['startsAt']<w['endsAt']: errors.append('window invalid')
        for i in c['incidents']:
            if i['class'] in ('setback','inconvenience') and not i['hasFreeRecovery']:errors.append('required recovery missing')
            if i['affectsRanked']:errors.append('ranked world effect')
    if num==11:
        chars={x['id'] for x in c['characters']};scenes={x['id'] for x in c['scenes']}
        for s in c['scenes']:
            if s['characterId'] not in chars or any(x not in scenes for x in s['next']):errors.append('unknown scene or character')
        for q in c['quests']:
            if q['startSceneId'] not in scenes:errors.append('unknown quest start')
        graph={s['id']:s['next'] for s in c['scenes']}
        def cycle(x,path):
            if x in path:return True
            return any(cycle(y,path|{x}) for y in graph.get(x,[]))
        if any(cycle(s,set()) for s in graph):errors.append('dialogue cycle')
    if num==12:
        edition_ids={x['id'] for x in c['editions']}
        for e in c['editions']:
            if not(e['startsAt']<e['scoringClosesAt']<=e['claimsCloseAt']<=e['archiveAt']): errors.append('invalid event window')
        for a in c['activities']:
            if a['editionId'] not in edition_ids or a['maxContributionsPerPlayer']<1:errors.append('invalid activity')
    if num==13:
        if c['tieBreak']!=['score_desc','shots_asc','activeTicks_asc','verifiedAt_asc','playerId_asc']:errors.append('comparator drift')
        for p in c['rankedProfiles']:
            if not (p['disableSkillEffects'] and p['disableShopEffects'] and p['disableWorldEffects']):errors.append('unfair profile')
        for comp in c['competitions']:
            if comp['allowSkillModifiers'] or comp['isPublished']:errors.append('unverified published competition')
    if num==14:
        if any(not p['requiresVerifiedReceipt'] for p in c['projects']):errors.append('unverified project')
        if not any(r['id']=='owner' and r['canTransferOwnership'] for r in c['crewRoles']):errors.append('no owner')
        if c['featureGates'].get('LIVE_MATCHES'):errors.append('live matches incorrectly enabled')
    if num==15:
        if c['breakpoints']['mobileMax']>=c['breakpoints']['tabletMax'] or c['breakpoints']['desktopMin']!=c['breakpoints']['tabletMax']+1:errors.append('breakpoint order')
        if any(s['gate']=='always' for s in c['screens'] if s['route'] not in ['/','/play','/help','/settings']):errors.append('unreleased screen visible')
        if len({s['route'] for s in c['screens']})!=len(c['screens']):errors.append('duplicate route')
    return errors

def get_expected(num,name,data,catalog):
    if num==10:
        if name=='no_negative_offline': return (not data['autoCharge'])
        if name=='ranked_ignores_weather':return 0 if data['ranked'] else data['worldModifier']
        if name=='one_choice':return min(1,data['attempts'])
        if name=='free_recovery': return next(i['hasFreeRecovery'] for i in catalog['incidents'] if i['id']==data['incidentId'])
    if num==11:
        if name=='choice_once':return min(1,data['clicks'])
        if name=='skippable':return next(s['isSkippable'] for s in catalog['scenes'] if s['id']==data['sceneId'])
        if name=='no_client_coins':return 0
        if name=='quest_first_clear_once':return min(1,data['verifiedClears'])
    if num==12:
        if name in ('before_start','open_at_start','closed_at_end'):
            e=next(e for e in catalog['editions'] if e['id']==data['editionId'])
            return e['startsAt']<=data['at']<e['scoringClosesAt']
        if name=='once_contribution':return min(1,data['submitCount'])
    if num==13:
        if name.startswith('tie_break'):
            a,b=data['a'],data['b']
            ak=(-a[0],a[1],a[2],a[3],a[4]);bk=(-b[0],b[1],b[2],b[3],b[4]);return 'a' if ak<bk else 'b'
        if name=='pending_never_ranked':return data['status']=='verified'
    if num==14:
        if name=='canonical_friend_pair':return sorted([data['a'],data['b']])
        if name=='block_overrides_accept':return 'blocked' if data['blocked'] else data['requestedState']
        if name=='crew_contribution_once':return min(1,data['sameRunSubmits'])
        if name=='no_live_without_gate':return data['gateEnabled']
    if num==15:
        if name=='route_flagged':
            x=next(x for x in catalog['screens'] if x['route']==data['route'])
            return x['gate']=='always' or x['gate'] in data['enabledFlags']
        if name=='core_route':return True
        if name in ('mobile_width','desktop_width'):
            w=data['width'];b=catalog['breakpoints'];return 'mobile' if w<=b['mobileMax'] else 'tablet' if w<=b['tabletMax'] else 'desktop'
    raise ValueError((num,name))


def mutate(c,m):
    c=copy.deepcopy(c)
    parent=c
    for segment in m['path'][:-1]:parent=parent[segment]
    key=m['path'][-1]
    if m['operation']=='delete':del parent[key]
    elif m['operation']=='set':parent[key]=m['value']
    else:raise ValueError('unknown mutation')
    return c

def check():
    catalog=json.loads((ROOT/'examples/catalog/catalog.draft.json').read_text())
    schema=json.loads((ROOT/'examples/schemas/catalog.schema.json').read_text())
    vectors=json.loads((ROOT/'examples/tests/pure-rule-vectors.json').read_text())
    invalid=json.loads((ROOT/'examples/tests/invalid-case-mutations.json').read_text())
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(catalog)
    assert not domain_validate(NUM,catalog),domain_validate(NUM,catalog)
    ids=[]
    for v in catalog.values():
        if isinstance(v,list) and v and isinstance(v[0],dict) and 'id' in v[0]:ids.extend(x['id'] for x in v)
    assert len(ids)==len(set(ids)), 'duplicate catalog id'
    for v in vectors:
        got=get_expected(NUM,v['name'],v['input'],catalog)
        assert got==v['expected'],f"{v['name']} expected {v['expected']!r}, got {got!r}"
    for mutation in invalid:
        edited=mutate(catalog,mutation)
        failed_schema=not Draft202012Validator(schema).is_valid(edited)
        failed_domain=bool(domain_validate(NUM,edited))
        assert failed_schema or failed_domain, f"invalid fixture erroneously accepted: {mutation['id']}"
    docs=sorted((ROOT/'docs').glob('[0-9][0-9]_*.md'))
    numbered=[p for p in docs if p.name!='00_INDEX_AND_README.md']
    assert len(numbered)==29,f"missing numbered chapter: {len(numbered)}"
    index=(ROOT/'docs/00_INDEX_AND_README.md').read_text()
    for f in numbered:assert f.name in index,f"chapter unlinked: {f.name}"
    assert 'Status' in (ROOT/'RELEASE_NOTES.md').read_text() or 'State' in (ROOT/'RELEASE_NOTES.md').read_text()
    print(f"Batch {NUM} PASS: {len(numbered)} chapters; {len(ids)} stable ids; {len(vectors)} rule vectors; {len(invalid)} invalid fixtures rejected; schema validated.")

if __name__=='__main__':check()
