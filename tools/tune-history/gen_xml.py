import sys,re,struct,xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
tsv,pdir,outdir,prefix=sys.argv[1:5]
SKIP={'controller_id'}
def f32(v):
    t=struct.unpack('<f',struct.pack('<f',v))[0]
    for n in range(1,10):
        s='%.*g'%(n,t)
        if struct.unpack('<f',struct.pack('<f',float(s)))[0]==t:
            r=repr(float(s))
            if 'e' in r: return s
            return r[:-2] if r.endswith('.0') else r
    return repr(t)
vals={'mcconf':{},'appconf':{}}
for line in open(tsv):
    k,f,v=line.rstrip('\n').split('\t')
    vals[k][re.sub(r'\[(\d+)\]',r'__\1',f)]=float(v)
for kind,root in (('mcconf','MCConfiguration'),('appconf','APPConfiguration')):
    r=ET.parse(f'{pdir}/parameters_{kind}.xml').getroot()
    params={c.tag:c for c in r.find('Params')}
    order=[e.text for e in r.find('SerOrder')]+[n for n in params if n not in [e.text for e in r.find('SerOrder')]]
    out=['<?xml version="1.0" encoding="UTF-8"?>','<%s>'%root,'    <ConfigVersion>2</ConfigVersion>']
    used=set()
    for n in order:
        if n in SKIP or n not in vals[kind] or n in used: continue
        t=int(params[n].find('type').text)
        v=vals[kind][n]
        s=f32(v) if t==1 else str(int(round(v)))
        out.append('    <%s>%s</%s>'%(n,escape(s),n)); used.add(n)
    out.append('</%s>'%root)
    open(f'{outdir}/{prefix}_{kind}.xml','w').write('\n'.join(out)+'\n')
    missing=[n for n in vals[kind] if n not in params]
    unset=[n for n in r.find('SerOrder') if n.text not in vals[kind]]
    print(kind,'written',len(used),'| fw fields not in tool XML:',missing,'| tool params with no fw default:',[e.text for e in unset])
