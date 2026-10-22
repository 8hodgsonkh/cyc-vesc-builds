# X12 + X1 Pro Gen 3: CYC default settings over time

Each row is a point on CYC's main development line where the default motor configuration for this bike changed, oldest first. Region variants (EU/EPAC, Japan) are excluded. Generated from CYC's own source by compiling their default-setting code on a PC (see `tools/tune-history`). "Changed" counts the settings that differ from the row above. "0604 release" marks the defaults in CYC's current OTA firmware (source 2025-06-04), which is what the stock and unlocked 250604 builds in this repo set.

| Date | Commit | Phase A | Batt A | Abs A | W | R mΩ | L µH | λ mWb | kp | ki | Obs gain | SL ERPM | Changed | File | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-06-25 | `af41657` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | first | [mcconf](2024-06-25_af41657_mcconf.xml) |  |
| 2024-09-23 | `ff34b78` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2024-09-23_ff34b78_mcconf.xml) |  |
| 2024-11-04 | `b550cf0` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2024-11-04_b550cf0_mcconf.xml) |  |
| 2025-02-18 | `2764064` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2025-02-18_2764064_mcconf.xml) |  |
| 2025-04-25 | `3044771` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2025-04-25_3044771_mcconf.xml) |  |
| 2025-05-27 | `4c615dc` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2025-05-27_4c615dc_mcconf.xml) |  |
| 2025-05-28 | `885a498` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2025-05-28_885a498_mcconf.xml) |  |
| 2025-05-30 | `2e2e6f3` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2025-05-30_2e2e6f3_mcconf.xml) | **0604 release** |
| 2025-06-16 | `88ee94a` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2025-06-16_88ee94a_mcconf.xml) |  |
| 2026-06-11 | `a88f627` | 160 | 120 | 400 | 6000 | 30 | 45 | 4 | 0.07 | 1 | 30 | 5000 | 1 | [mcconf](2026-06-11_a88f627_mcconf.xml) | newest |

## App configuration versions

CYC stores its power levels, speed limits and display options in the app configuration (see [CYC_SETTINGS_MAP.md](../../docs/CYC_SETTINGS_MAP.md) for what each field means).

| Date | Commit | File |
|---|---|---|
| 2024-06-25 | `af41657` | [appconf](2024-06-25_af41657_appconf.xml) |
| 2024-09-20 | `2c5f660` | [appconf](2024-09-20_2c5f660_appconf.xml) |
| 2024-09-23 | `ff34b78` | [appconf](2024-09-23_ff34b78_appconf.xml) |
| 2024-11-04 | `b550cf0` | [appconf](2024-11-04_b550cf0_appconf.xml) |
| 2025-10-17 | `dd2b758` | [appconf](2025-10-17_dd2b758_appconf.xml) |
| 2025-10-17 | `5fc7ecd` | [appconf](2025-10-17_5fc7ecd_appconf.xml) |
| 2025-12-10 | `8f1b938` | [appconf](2025-12-10_8f1b938_appconf.xml) |
| 2025-12-29 | `cd72791` | [appconf](2025-12-29_cd72791_appconf.xml) |
