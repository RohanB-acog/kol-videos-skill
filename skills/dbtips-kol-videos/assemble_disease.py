import json, glob, pathlib, urllib.parse, re, sys
slug, search_name, field = sys.argv[1], sys.argv[2], sys.argv[3]
R = pathlib.Path(f'run_{slug}')
cand = {e['name']: e for e in json.load(open(R/'candidates.json'))['experts']}
# Optional aliases.json maps the display spelling used in dec/ to the
# candidates.json key for the SAME person, where canonical() mangled the key
# ("Chang Won Won" -> "Won Won"). Identity resolution only: never point a
# display name at a different person's candidate record.
if (R/'aliases.json').exists():
    for display, key in json.load(open(R/'aliases.json')).items():
        if key in cand: cand[display] = cand[key]
TXDIR = (R/'tx_all') if (R/'tx_all').exists() else (R/'tx')
tx = {p.stem: json.loads(p.read_text()) for p in TXDIR.glob('*.json') if p.stem!='_digest'}
dec = [x for f in sorted(glob.glob(str(R/'dec'/'d*.json'))) for x in json.load(open(f))]
INST=('universit','hospital','center','centre','clinic','institut','school','college','medical','health','division','department','foundation')
def sane(a):
    if not a: return None
    # PubMed author strings append the corresponding author's address, sometimes
    # twice ("...Spain. a@b.org <a@b.org>"). Strip every address, not only a
    # single trailing one, then the punctuation the removal leaves behind.
    a = re.sub(r'<[^<>@]+@[^<>]+>','',a)
    a = re.sub(r'[\w.+-]+@[\w.-]+\.\w+\.?','',a)
    a = re.sub(r'[\s.,;]+$','',a).strip()
    a = re.sub(r',?\s*\d{5}(-\d{4})?\s*,?',', ',a)
    a = re.sub(r'\s*,\s*',', ',a).strip(' ,.')
    return a if any(w in a.lower() for w in INST) else None
def pubmed(e):
    ids=(e or {}).get('pmids') or []
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + urllib.parse.quote(" OR ".join(ids[:60])) if ids else None
def expertise(e):
    s=(e or {}).get('signals') or {}
    bits=[]
    if s.get('trials'): bits.append(f"{s['trials']} clinical trial(s)")
    if s.get('guidelines'): bits.append(f"{s['guidelines']} guideline(s)")
    if s.get('grants'): bits.append(f"{s['grants']} NIH grant(s)")
    return field + (" — " + "; ".join(bits) if bits else "")
# Optional affiliations.json: kol_name -> affiliation stated explicitly in the
# transcript or description, used ONLY where the candidate stage carried none.
# The candidate record always wins when it has one -- this fills a null, it
# never overrides an upstream reading.
AFF = json.load(open(R/'affiliations.json')) if (R/'affiliations.json').exists() else {}
FIELDS=["search_name","video_id","title","kol_name","affiliation","expertise",
        "current_practice","stance","unmet_needs","video","publications",
        "published_date","view_count","channel_name","duration_seconds"]
recs=[]
for d in dec:
    if not (d['discusses_disease'] and d.get('current_practice')): continue
    m=tx.get(d['video_id'])
    if not m or not m.get('metadata_available'): continue
    e=cand.get(d['kol_name']); s=lambda v: None if v is None else str(v)
    recs.append({"search_name":search_name,"video_id":s(m['video_id']),"title":s(m.get('title')),
        "kol_name":s(d['kol_name']),"affiliation":s(sane((e or {}).get('affiliation')) or AFF.get(d['kol_name'])),
        "expertise":s(expertise(e)),"current_practice":s(d.get('current_practice')),
        "stance":s(d.get('stance')),"unmet_needs":s(d.get('unmet_needs')),
        "video":f"https://www.youtube.com/watch?v={m['video_id']}","publications":pubmed(e),
        "published_date":s(m.get('published_date')),"view_count":s(m.get('view_count')),
        "channel_name":s(m.get('channel_name')),"duration_seconds":s(m.get('duration_seconds'))})
recs.sort(key=lambda r: (r['kol_name'] or '', -(int(r['view_count'] or 0))))
for r in recs: assert list(r.keys())==FIELDS
json.dump(recs, open(R/'records_final.json','w'), ensure_ascii=False, indent=1)
print(f"{slug}: {len(recs)} records | {len({r['kol_name'] for r in recs})} KOLs")
print("  nulls:", {k: sum(1 for r in recs if not r[k]) for k in ('affiliation','stance','unmet_needs','publications')})
for r in recs: print(f"   {r['kol_name']:<24} {(r['channel_name'] or '')[:28]:<28} {r['title'][:44]}")
