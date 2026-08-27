import json, re, pathlib, sys, glob
slug, pattern = sys.argv[1], sys.argv[2]
R = pathlib.Path(f'run_{slug}')
tx = {p.stem: json.loads(p.read_text()) for p in (R/'tx').glob('*.json') if p.stem!='_digest'}
kols = {}
for v in json.load(open(R/'videos.json')): kols.setdefault(v['video_id'], v['kol_name'])
done = {x['video_id'] for f in glob.glob(str(R/'dec'/'d*.json')) for x in json.load(open(f))}
DIS = re.compile(pattern, re.I)
usable = [v for v,d in tx.items() if d.get('transcript_available') and v not in done]
def score(v):
    d=tx[v]; t=f"{d.get('title') or ''} {d.get('description') or ''}"
    body=(d.get('transcript') or '')[:4000]
    return -(3*len(DIS.findall(t)) + len(DIS.findall(body)))
usable.sort(key=score)
(R/'batches2').mkdir(exist_ok=True)
for f in (R/'batches2').glob('*.txt'): f.unlink()
B=10
for i in range(0, len(usable), B):
    out=[]
    for v in usable[i:i+B]:
        d=tx[v]; t=re.sub(r'\s+',' ', d.get('transcript') or '')
        out.append(f"### {v} | {kols.get(v)} | {d.get('channel_name')} | hits={-score(v)}\n"
                   f"TITLE: {d.get('title')}\nDESC: {re.sub(chr(10),' ',(d.get('description') or ''))[:170]}\n"
                   f"TX: {t[:3000]}\n")
    (R/'batches2'/f'b{i:03d}.txt').write_text("\n".join(out))
print(f"{slug}: {len(usable)} remaining -> {len(list((R/'batches2').glob('*.txt')))} batches, relevance-ordered")
print("  top 12 by relevance:", [(tx[v].get('title') or '')[:44] for v in usable[:12]])
