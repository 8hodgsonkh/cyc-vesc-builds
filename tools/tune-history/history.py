# usage: python3 history.py <cyc git dir> <history.sh out dir> <tunes dir>
# Keeps each product's motor/app defaults only when they differ from the previous
# main-line commit's, copies those XMLs into <tunes dir>/<product>/ and writes
# a README per product with the motor tune values over time.
import hashlib, os, re, shutil, subprocess, sys
import xml.etree.ElementTree as ET

git_dir, work, tunes = sys.argv[1:4]
raw = os.path.join(work, 'raw')
commits = [l.split()[0] for l in open(raw + '.commits')]

NAMES = {
    'photon': 'Photon (Gen 1 hardware)',
    'photon_gen2': 'Photon (Gen 2 hardware)',
    'photon_pro': 'Photon Pro',
    'x12_gen4': 'X12 + X1 Pro Gen 4',
    'x12_gen4_mx': 'X12 + X1 Pro Gen 4, MX (Bonnell 775 MX)',
    'x12_gen4_rs': 'X12 + X1 Pro Gen 4, RS (Ristretto)',
    'x12_gen3': 'X12 + X1 Pro Gen 3',
    'x6_x1pro': 'X6 + X1 Pro Gen 3',
    'x6_stealth': 'X6 + X1 Stealth',
}
# (xml field, column, scale, decimals)
COLS = [('l_current_max', 'Phase A', 1, 0), ('l_in_current_max', 'Batt A', 1, 0),
        ('l_abs_current_max', 'Abs A', 1, 0), ('l_watt_max', 'W', 1, 0),
        ('foc_motor_r', 'R mΩ', 1e3, 1), ('foc_motor_l', 'L µH', 1e6, 1),
        ('foc_motor_flux_linkage', 'λ mWb', 1e3, 2), ('foc_current_kp', 'kp', 1, 3),
        ('foc_current_ki', 'ki', 1, 1), ('foc_observer_gain', 'Obs gain', 1e-6, 1),
        ('foc_sl_erpm', 'SL ERPM', 1, 0)]


def git(*a):
    return subprocess.run(['git', '-C', git_dir, *a], capture_output=True, text=True, check=True).stdout.strip()


def values(path):
    return {e.tag: e.text for e in ET.parse(path).getroot()}


def fmt(v, scale, dec):
    try:
        x = float(v) * scale
    except (TypeError, ValueError):
        return '?'
    return ('%.*f' % (dec, x)).rstrip('0').rstrip('.') if dec else '%d' % round(x)


dates = {c: git('log', '-1', '--format=%ad', '--date=short', c) for c in commits}
pos = {c[:7]: i for i, c in enumerate(commits)}
# 7b08350 = CYC's "0604 batch update", the source of their current OTA files
REL = pos[next(c[:7] for c in commits if c.startswith('7b08350'))]

for prod, title in NAMES.items():
    shutil.rmtree(os.path.join(tunes, prod), ignore_errors=True)
    last = {'mcconf': None, 'appconf': None}
    rows, app_rows, prev = [], [], None
    out = os.path.join(tunes, prod)
    for c in commits:
        for kind in ('mcconf', 'appconf'):
            f = os.path.join(raw, c, f'{prod}_{kind}.xml')
            if not os.path.exists(f):
                continue
            h = hashlib.sha1(open(f, 'rb').read()).hexdigest()
            if h == last[kind]:
                continue
            last[kind] = h
            date = dates[c]
            name = f'{date}_{c[:7]}_{kind}.xml'
            os.makedirs(out, exist_ok=True)
            shutil.copy(f, os.path.join(out, name))
            v = values(f)
            if kind == 'mcconf':
                changed = [k for k in v if prev is None or prev.get(k) != v[k]]
                rows.append((date, c[:7], name, v, len(changed) if prev else None))
                prev = v
            else:
                app_rows.append((date, c[:7], name))
    if not rows:
        continue
    md = [f'# {title}: CYC default settings over time', '',
          'Each row is a point on CYC\'s main development line where the default motor configuration '
          'for this bike changed, oldest first. Region variants (EU/EPAC, Japan) are excluded. '
          'Generated from CYC\'s own source by compiling their default-setting code on a PC '
          '(see `tools/tune-history`). "Changed" counts the settings that differ from the row above. '
          '"0604 release" marks the defaults in CYC\'s current OTA firmware (source 2025-06-04), '
          'which is what the stock and unlocked 250604 builds in this repo set.', '',
          '| Date | Commit | ' + ' | '.join(col for _, col, _, _ in COLS) + ' | Changed | File | |',
          '|' + '---|' * (len(COLS) + 5)]
    at_rel = max((i for i, r in enumerate(rows) if pos[r[1]] <= REL), default=None)
    for i, (date, c, name, v, nchg) in enumerate(rows):
        cells = [fmt(v.get(k), s, d) for k, _, s, d in COLS]
        note = ['**0604 release**'] if i == at_rel else []
        if i == len(rows) - 1:
            note.append('newest')
        md.append(f'| {date} | `{c}` | ' + ' | '.join(cells) +
                  f' | {"first" if nchg is None else nchg} | [mcconf]({name}) | {", ".join(note)} |')
    md += ['', '## App configuration versions', '',
           'CYC stores its power levels, speed limits and display options in the app configuration '
           '(see [CYC_SETTINGS_MAP.md](../../docs/CYC_SETTINGS_MAP.md) for what each field means).', '',
           '| Date | Commit | File |', '|---|---|---|']
    md += [f'| {d} | `{c}` | [appconf]({n}) |' for d, c, n in app_rows]
    open(os.path.join(out, 'README.md'), 'w').write('\n'.join(md) + '\n')
    print(f'{prod}: {len(rows)} motor, {len(app_rows)} app versions')
