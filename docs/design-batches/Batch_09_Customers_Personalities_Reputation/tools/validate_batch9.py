#!/usr/bin/env python3
"""Batch 9 static authoring + pure-rule validation. No real backend/physics/browser tests."""
from pathlib import Path
import json, re, math, copy
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def check(c,msg):
    if not c: raise AssertionError(msg)
def clamp(a,b,v): return max(a,min(b,v))
def chance(base,mods,cap):return clamp(0,cap,base+sum(mods))
def sat(v):
    if not v['verified'] or not v['missionWon']:return None
    return clamp(0,10000,5000+(2200 if v['fulfilled'] else 0)+600+clamp(0,400,v['extraBonus'])-clamp(0,1500,v['penalty']))
def rep(score,run):
    per=clamp(-30,30,math.floor((clamp(0,10000,score)-5000)/100))
    return clamp(-60,60,run+per)-run
def visit(first,fave,eligible):return min(220,(100 if first else 180)+(40 if fave else 0)) if eligible else 0
def tier(total):
    return ('island_legend' if total>=1300 else 'friend_of_shop' if total>=700 else 'regular' if total>=300 else 'acquaintance' if total>=100 else 'stranger')
def weighted(entries,draw):
    cumulative=0
    for e in sorted((e for e in entries if e['weight']>0),key=lambda e:e['customerId']):
        cumulative+=e['weight']
        if draw<cumulative:return e['customerId']
    raise ValueError('bad draw')

def validate():
    c=read('examples/catalog/customer-catalog.draft.json')
    schema=read('examples/schemas/customer-catalog.schema.json')
    Draft202012Validator.check_schema(schema)
    errs=list(Draft202012Validator(schema).iter_errors(c))
    check(not errs,'schema errors: '+str([e.message for e in errs[:5]]))
    check(c['releaseState']=='draft','catalog cannot ship live by accident')
    check(not any(c['flagsDefault'].values()),'all flags must default OFF')
    check(c['alphaFixture']['visibleOrderCount']==2 and c['alphaFixture']['winOrderCount']==2,'Batch 4 alpha drift')
    ids=[e['customerId'] for e in c['customers']]
    check(len(ids)==len(set(ids)),'duplicate customer ID')
    segmentids={e['segmentId'] for e in c['segments']}
    check(len(segmentids)==7 and len(c['customers'])==14,'fixture count drift')
    check(all(e['segmentId'] in segmentids for e in c['customers']),'missing segment')
    pools=[p['poolId'] for p in c['pools']]
    check(len(set(pools))==len(pools),'duplicate pool')
    for p in c['pools']:
        check(p['vipBaseBps']<=p['vipCapBps'],'VIP base > cap')
        check(all(e['customerId'] in ids for e in p['entries']),'unknown pool customer')
        check(len(set(e['customerId'] for e in p['entries']))==len(p['entries']),'duplicate weighted entry')
        check(all(e in ids for e in p['fixedCustomers']),'unknown scripted customer')
        check(p['entries'] or p['fixedCustomers'],'empty pool')
        if p['releaseState']=='alpha_scripted':
            check(p['fixedCustomers']==c['alphaFixture']['customerIds'],'alpha fixed customers changed')
            check(p['vipBaseBps']==0 and p['vipCapBps']==0,'VIP in alpha')
        else:
            check(p['featureGate']!='NONE','future pool is ungated')
    check(len([e for e in c['customers'] if e['releaseState']=='alpha_scripted'])==2,'alpha guest count drift')
    policy=c['policies']
    check(all(not p['enabled'] for p in policy.values()),'policy cannot be initially enabled')
    check(policy['satisfaction']['scaleMax']==10000,'score scale drift')
    check(policy['reputation']['perRunMin']==-60 and policy['reputation']['perRunMax']==60,'run cap drift')
    for name in ('guest.mira.cove','guest.kai.cove'):
        check(name in ids,'missing alpha character')
    docs=list((ROOT/'docs').glob('*.md'))
    check(len(docs)==46,'expected 45 chapters plus index, got '+str(len(docs)))
    check({int(d.name[:2]) for d in docs}==set(range(46)),'duplicate or missing chapter numbers')
    index=(ROOT/'docs/00_INDEX_AND_README.md').read_text()
    for f in docs:
        if f.name != '00_INDEX_AND_README.md': check(f.name in index,'index missing '+f.name)
    v=read('examples/tests/customer-rule-vectors.json')
    count=0
    for e in v['vipBps']:
        check(chance(e['base'],e['modifiers'],e['cap'])==e['expected'],'VIP vector '+str(e));count+=1
    for e in v['satisfaction']:
        check(sat(e)==e['expected'],'satisfaction vector '+str(e));count+=1
    for e in v['reputationDelta']:
        check(rep(e['satisfaction'],e['runAccum'])==e['expected'],'rep vector '+str(e));count+=1
    for e in v['loyaltyVisit']:
        check(visit(e['firstVisit'],e['favoriteMatched'],e['eligible'])==e['expected'],'loyalty visit vector');count+=1
    for e in v['loyaltyTier']:
        check(tier(e['points'])==e['expected'],'loyalty tier vector');count+=1
    for e in v['weightedSampling']:
        check(weighted(e['entries'],e['draw'])==e['expected'],'weighted vector');count+=1
    for e in v['orderPriority']:
        match=sorted([o for o in e['orders'] if o['requestedTier']==e['outputTier']],key=lambda o:(o['issuedTick'],o['orderId']))
        check((match[0]['orderId'] if match else None)==e['expected'],'order priority vector');count+=1
    for e in v['duplicateSources']:
        check(len(set(e['sourceKeys']))==e['expectedUnique'],'dedupe vector');count+=1
    # Negative tests: reject invalid/malicious catalogs
    bad=copy.deepcopy(c);bad['flagsDefault']['CUSTOMER_VIP_ENABLED']=True
    check(bool(list(Draft202012Validator(schema).iter_errors(bad))),'positive feature gate escaped schema')
    bad=copy.deepcopy(c);bad['customers'][0]['personality']['energy']=101
    check(bool(list(Draft202012Validator(schema).iter_errors(bad))),'personality out of bound')
    bad=copy.deepcopy(c);bad['pools'][0]['vipCapBps']=3000
    check(bool(list(Draft202012Validator(schema).iter_errors(bad))),'VIP cap out of bound')
    print(f'PASS Batch 9: 45 chapters, {len(c["customers"])} customers, {len(c["segments"])} segments, {len(c["pools"])} pools, {count} pure rule vectors, 3 negative schema fixtures')
if __name__=='__main__':validate()
