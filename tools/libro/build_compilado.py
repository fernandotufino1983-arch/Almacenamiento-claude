# Arma libro/libro-compilado.md a partir de la portada (cabecera actual), el índice, el prólogo y los capítulos.
# Uso: python3 build_compilado.py [paginas.json] [idx_entries.json]
import re,sys,json,os
L=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','libro')+'/'
PG=json.load(open(sys.argv[1])) if len(sys.argv)>1 and os.path.exists(sys.argv[1]) else {}
IDXOUT=sys.argv[2] if len(sys.argv)>2 else '/tmp/idx_entries.json'
comp=open(L+'libro-compilado.md').read()
head=re.split(r'^## (?:Parte |Prólogo|Plan de temas|Índice)',comp,flags=re.M)[0].rstrip()
head=re.sub(r'(\s*<<PAGEBREAK>>|\s*<<(?:TOC|PLAN)>>|\s*<<IDX.*)+\s*$','',head).rstrip()+'\n\n'
parts=[('## Parte I. El delito de lavado de activos',[('01','capitulo-01-origen-concepto-lavado.md'),('02','capitulo-02-autonomia-lavado.md'),('03','capitulo-03-dolo-eximentes.md'),('04','capitulo-04-prueba-indiciaria.md'),('05','capitulo-05-concursos.md'),('06','capitulo-06-persona-juridica.md'),('07','capitulo-07-extincion-dominio.md')]),
 ('## Parte II. Estrategia de defensa',[('08','capitulo-08-defensa-investigacion-previa.md'),('09','capitulo-09-pericia-contable-de-parte.md'),('10','capitulo-10-litigacion-en-juicio.md'),('11','capitulo-11-recursos.md')])]
idx=['## Índice','','<<IDX1>> Prólogo|'+str(PG.get('Prólogo',''))]
for ptitle,chs in parts:
    pt=ptitle[3:]; idx.append('<<IDX0>> '+pt+'|'+str(PG.get(pt,'')))
    for num,f in chs:
        for ln in open(L+f).read().splitlines():
            m1=re.match(r'^# (Capítulo .*)$',ln); m2=re.match(r'^## (\d+\.\d+\. .*|Referencias)$',ln); m3=re.match(r'^### (\d+\.\d+\.\d+\. .*)$',ln)
            if m1: cur=m1.group(1); idx.append('<<IDX1>> '+cur+'|'+str(PG.get(cur,'')))
            elif m2:
                k=m2.group(1); key=k if k!='Referencias' else cur+'|Ref'
                idx.append('<<IDX2>> '+k+'|'+str(PG.get(key,'')))
            elif m3: idx.append('<<IDX3>> '+m3.group(1)+'|'+str(PG.get(m3.group(1),'')))
json.dump([l for l in idx if l.startswith('<<IDX')],open(IDXOUT,'w'))
out=[head,'<<PAGEBREAK>>\n\n'+'\n'.join(idx)+'\n\n<<PAGEBREAK>>\n\n']
pl=[]
for ln in open(L+'prologo.md').read().splitlines():
    if ln.startswith('> **Borrador'): continue
    ln=re.sub(r'\[\^([\w-]+)\]',lambda m:'[^p0_%s]'%m.group(1),ln)
    if ln.startswith('# '): ln='#'+ln
    pl.append(ln)
out.append('\n'.join(pl).strip()+'\n\n<<PAGEBREAK>>\n\n'); first=True
for ptitle,chs in parts:
    if not first: out.append('<<PAGEBREAK>>\n\n')
    out.append(ptitle+'\n\n'); first=False
    for i,(num,f) in enumerate(chs):
        if i: out.append('<<PAGEBREAK>>\n\n')
        n=str(int(num)); lines=[]
        for ln in open(L+f).read().splitlines():
            if ln.startswith('> **Borrador'): continue
            ln=re.sub(r'\[\^([\w-]+)\]',lambda m:'[^c%s_%s]'%(n,m.group(1).replace('-','_')),ln)
            if re.match(r'^(#{1,3}) ',ln): ln='#'+ln
            lines.append(ln)
        out.append('\n'.join(lines).strip()+'\n\n')
open(L+'libro-compilado.md','w').write(''.join(out))
