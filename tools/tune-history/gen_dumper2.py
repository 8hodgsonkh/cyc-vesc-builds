# Emit dumper.c: CYC's default-config functions from confgenerator.c plus the
# "if (!is_ok) { ... }" fallback blocks of conf_general_read_{mc,app}_configuration,
# which is where CYC layers the Gen 3 / X6 / Stealth overrides on top.
# The dumper prints every field those bodies assign, as the firmware would set them.
import re, sys

src = sys.argv[1]
cg = open(f'{src}/confgenerator.c', encoding='latin-1').read().replace('\r', '')
cgen = open(f'{src}/conf_general.c', encoding='latin-1').read().replace('\r', '')

funcs = re.findall(r'\nvoid (\w*confgenerator_set_defaults_(?:mc|app)conf)\(((?:mc|app)_configuration) \*conf\) \{(.*?)\n\}', cg, re.S)
# From the first defaults function to EOF CYC's file holds only these functions and the
# #if VSBM_181 guard around the Stealth (s_) pair, so copy it verbatim to keep the guard.
tail = cg[cg.index('\nvoid confgenerator_set_defaults_mcconf('):]

def fallback_block(fn):
    m = re.search(r'\nvoid %s\([^)]*\) \{' % fn, cgen)
    i = cgen.index('if (!is_ok) {', m.end())
    j = cgen.index('{', i)
    depth = 0
    for k in range(j, len(cgen)):
        if cgen[k] == '{':
            depth += 1
        elif cgen[k] == '}':
            depth -= 1
            if depth == 0:
                return cgen[j + 1:k]
    raise SystemExit('unbalanced block in ' + fn)

ov = {'mc': fallback_block('conf_general_read_mc_configuration'),
      'app': fallback_block('conf_general_read_app_configuration')}

fields = {'mc': [], 'app': []}
for name, typ, body in funcs:
    fields[typ[:-len('_configuration')]] += re.findall(r'conf->([\w\.\[\]]+)\s*=', body)
for k in ov:
    fields[k] += re.findall(r'conf->([\w\.\[\]]+)\s*=', ov[k])

out = ['#include <stdio.h>', '#include "conf_general.h"', '#include "confgenerator.h"',
       'uint8_t hw_id_from_uuid(void){return 0;}']
out.append(tail)
out.append('static void ov_mc(mc_configuration *conf) { bool is_motor_2 = false; (void)is_motor_2;%s\n}' % ov['mc'])
out.append('static void ov_app(app_configuration *conf) {%s\n}' % ov['app'])
out.append('int main(void) {')
for k, typ, kind in (('mc', 'mc_configuration', 'mcconf'), ('app', 'app_configuration', 'appconf')):
    out.append(' { static %s c; ov_%s(&c);' % (typ, k))
    for f in dict.fromkeys(fields[k]):
        out.append('  printf("%s\\t%s\\t%%.9g\\n", (double)c.%s);' % (kind, f, f))
    out.append(' }')
out.append(' return 0; }')
open('dumper.c', 'w').write('\n'.join(out) + '\n')
