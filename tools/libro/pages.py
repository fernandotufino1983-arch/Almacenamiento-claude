# Calcula la página de cada entrada del índice a partir del PDF. Uso: python3 pages.py libro.pdf salida.json idx_entries.json
import json,re,subprocess,sys
pdf,out,entries=sys.argv[1],sys.argv[2],sys.argv[3]
txt=subprocess.run(['pdftotext','-layout',pdf,'-'],capture_output=True,text=True).stdout.split('\f')
norm=lambda s:re.sub(r'\s+',' ',s).strip()
pages=[norm(p) for p in txt]
start=next(i for i,p in enumerate(pages) if 'Durante mucho tiempo el Ecuador' in p)
PG={}; cur=start; ch=None
for e in json.load(open(entries)):
    k=re.match(r'^<<IDX\d>> (.*?)\|',e).group(1)
    if k.startswith('Capítulo'): ch=k
    key=ch+'|Ref' if k=='Referencias' else k
    probe=norm(k)[:45]
    for i in range(cur,len(pages)):
        if probe in pages[i]: PG[key]=i+1; cur=i; break
    else: print('NO',k)
json.dump(PG,open(out,'w'),ensure_ascii=False); print(len(PG),'entradas con página')
