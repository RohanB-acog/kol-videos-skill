import json, re, pathlib, sys, glob
slug, disease = sys.argv[1], sys.argv[2]
R = pathlib.Path(f'run_{slug}')
tx = {p.stem: json.loads(p.read_text()) for p in (R/'tx').glob('*.json') if p.stem!='_digest'}
kols = {}
for v in json.load(open(R/'videos.json')):
    kols.setdefault(v['video_id'], v['kol_name'])
usable = [v for v,d in tx.items() if d.get('transcript_available')]
usable.sort(key=lambda v: -(len(tx[v].get('transcript') or '')))
(R/'batches').mkdir(exist_ok=True)
B = 10
for i in range(0, len(usable), B):
    out=[]
    for v in usable[i:i+B]:
        d=tx[v]; t=re.sub(r'\s+',' ', d.get('transcript') or '')
        out.append(f"### {v} | {kols.get(v)} | {d.get('channel_name')} | len={len(t)}\n"
                   f"TITLE: {d.get('title')}\n"
                   f"DESC: {re.sub(chr(10),' ',(d.get('description') or ''))[:220]}\n"
                   f"TX: {t[:3400]}\n")
    (R/'batches'/f'b{i:03d}.txt').write_text("\n".join(out))
print(f"{slug}: {len(usable)} usable -> {len(glob.glob(str(R/'batches'/'*.txt')))} batches")
