#!/usr/bin/env python3
"""Minimal dependency-free content/fixture validation for Mixipelago Batch 3 docs.
Not a game runtime test, a source content contract test only.
"""
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(cond, message):
    if not cond: errors.append(message)
def j(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
cat=j('examples/catalog/core-drinks-alpha.json')
rows=cat['tiers']
check(cat['schemaVersion']==1 and len(rows)==8, 'Catalog must contain eight alpha tiers')
check([r['tier'] for r in rows]==list(range(1,9)), 'Tiers must be ordered 1..8')
check(len({r['id'] for r in rows})==8, 'IDs must be unique')
check(len({r['assetId'] for r in rows})==8, 'Board asset IDs must be unique')
check(all(r['familyId']=='core' for r in rows), 'Alpha family must be core')
check([r['mergeScore'] for r in rows]==[10,25,60,140,320,720,1600,3500], 'Batch 1 canonical scores changed')
for i,r in enumerate(rows):
    check(r['nextTierId']==(rows[i+1]['id'] if i<7 else None), f'Bad evolution edge for tier {i+1}')
    check(bool(re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',r['id'])),f'Bad slug {r["id"]}')
lookup={r['id']:r for r in rows}
tests=j('examples/tests/drink-rule-vectors.json')['vectors']
for v in tests:
    a,b=[lookup[x] for x in v['input']]
    permitted=a['tier']==b['tier'] and a['tier']<8 and a['familyId']=='core'
    check(permitted==v['eligible'],f'Unexpected eligibility {v["id"]}')
    if permitted:
        output=lookup[a['nextTierId']]
        check(v['output']==output['id'] and v['baseScore']==output['mergeScore'],f'Bad output {v["id"]}')
mission=j('examples/missions/coconut-cove-001.json')
check(mission['orders']['maxVisible']==2,'Two active orders in alpha')
check(all(1<=x['requestedTier']<=8 for x in mission['orders']['initial']),'Invalid order target tier')
check(all(1<=x['tier']<=8 for x in mission['board']['startingDrinks']),'Invalid starting body tier')
check(mission['goal']['type']=='orders_served','Unexpected tutorial goal')
concept=j('examples/catalog/future-research-recipe.disabled.json')
check(concept['enabled'] is False,'Future recipe must be disabled')
for p in (ROOT/'examples').rglob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'Invalid JSON: {p.name}: {e}')
files=sorted((ROOT/'docs').glob('*.md'))
check(len(files)==35,'Expected 35 Markdown files')
check([int(p.name[:2]) for p in files]==list(range(35)),'Document numbering must be 00..34')
for f in files:
    text=f.read_text(encoding='utf-8')
    check(text.startswith('# '),f'Document missing header: {f.name}')
    check(len(text.split())>180,f'Document is too short: {f.name}')
if errors:
    print('ERRORS:'); [print(' -',v) for v in errors]; sys.exit(1)
print(f'PASS: {len(files)} docs, {len(rows)} canonical tiers, {len(tests)} rule vectors, JSON valid, future research disabled.')
print('NOTE: No physics/replay/visual/manual gameplay tests were executed.')
