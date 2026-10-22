# Photon Pro: CYC default settings over time

Each row is a point on CYC's main development line where the default motor configuration for this bike changed, oldest first. Region variants (EU/EPAC, Japan) are excluded. Generated from CYC's own source by compiling their default-setting code on a PC (see `tools/tune-history`). "Changed" counts the settings that differ from the row above. "0604 release" marks the defaults in CYC's current OTA firmware (source 2025-06-04), which is what the stock and unlocked 250604 builds in this repo set.

| Date | Commit | Phase A | Batt A | Abs A | W | R mΩ | L µH | λ mWb | kp | ki | Obs gain | SL ERPM | Changed | File | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-03-19 | `d83f62a` | 95 | 80 | 250 | 5000 | 35 | 40 | 6 | 0.03 | 1 | 12 | 2500 | first | [mcconf](2025-03-19_d83f62a_mcconf.xml) | **0604 release** |
| 2025-12-10 | `0f8ff93` | 95 | 80 | 250 | 5000 | 35 | 40 | 6 | 0.03 | 1 | 12 | 2500 | 6 | [mcconf](2025-12-10_0f8ff93_mcconf.xml) |  |
| 2025-12-29 | `cd72791` | 83 | 80 | 300 | 8000 | 33 | 50 | 7.5 | 0.07 | 1 | 5 | 2500 | 10 | [mcconf](2025-12-29_cd72791_mcconf.xml) |  |
| 2026-03-25 | `24d0a4a` | 83 | 80 | 300 | 4000 | 33 | 50 | 7.5 | 0.07 | 1 | 5 | 2500 | 1 | [mcconf](2026-03-25_24d0a4a_mcconf.xml) | newest |

## App configuration versions

CYC stores its power levels, speed limits and display options in the app configuration (see [CYC_SETTINGS_MAP.md](../../docs/CYC_SETTINGS_MAP.md) for what each field means).

| Date | Commit | File |
|---|---|---|
| 2025-03-19 | `d83f62a` | [appconf](2025-03-19_d83f62a_appconf.xml) |
| 2025-05-30 | `2e2e6f3` | [appconf](2025-05-30_2e2e6f3_appconf.xml) |
| 2025-08-08 | `c1fc6ff` | [appconf](2025-08-08_c1fc6ff_appconf.xml) |
| 2025-08-12 | `9bbb62c` | [appconf](2025-08-12_9bbb62c_appconf.xml) |
| 2025-10-17 | `dd2b758` | [appconf](2025-10-17_dd2b758_appconf.xml) |
| 2025-10-17 | `5fc7ecd` | [appconf](2025-10-17_5fc7ecd_appconf.xml) |
| 2025-12-10 | `8f1b938` | [appconf](2025-12-10_8f1b938_appconf.xml) |
| 2025-12-10 | `0f8ff93` | [appconf](2025-12-10_0f8ff93_appconf.xml) |
| 2025-12-29 | `cd72791` | [appconf](2025-12-29_cd72791_appconf.xml) |
| 2026-03-25 | `24d0a4a` | [appconf](2026-03-25_24d0a4a_appconf.xml) |
| 2026-04-01 | `cf30c1f` | [appconf](2026-04-01_cf30c1f_appconf.xml) |
