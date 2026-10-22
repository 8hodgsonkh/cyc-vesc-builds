# X6 + X1 Stealth: CYC default settings over time

Each row is a point on CYC's main development line where the default motor configuration for this bike changed, oldest first. Region variants (EU/EPAC, Japan) are excluded. Generated from CYC's own source by compiling their default-setting code on a PC (see `tools/tune-history`). "Changed" counts the settings that differ from the row above. "0604 release" marks the defaults in CYC's current OTA firmware (source 2025-06-04), which is what the stock and unlocked 250604 builds in this repo set.

| Date | Commit | Phase A | Batt A | Abs A | W | R mΩ | L µH | λ mWb | kp | ki | Obs gain | SL ERPM | Changed | File | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-06-25 | `af41657` | 90 | 80 | 300 | 3000 | 30.5 | 15.8 | 5.21 | 0.05 | 1 | 15 | 7500 | first | [mcconf](2024-06-25_af41657_mcconf.xml) |  |
| 2024-09-23 | `ff34b78` | 90 | 80 | 300 | 3000 | 30.5 | 15.8 | 5.21 | 0.05 | 1 | 15 | 7500 | 1 | [mcconf](2024-09-23_ff34b78_mcconf.xml) |  |
| 2024-09-30 | `750c722` | 90 | 80 | 300 | 3000 | 30.5 | 15.8 | 5.21 | 0.05 | 1 | 15 | 7500 | 4 | [mcconf](2024-09-30_750c722_mcconf.xml) |  |
| 2024-10-30 | `cd42782` | 90 | 80 | 300 | 3000 | 42 | 35 | 5.5 | 0.02 | 1 | 20 | 5000 | 9 | [mcconf](2024-10-30_cd42782_mcconf.xml) |  |
| 2024-10-31 | `a9963bf` | 90 | 80 | 300 | 3000 | 42 | 35 | 5.5 | 0.02 | 1 | 20 | 5000 | 1 | [mcconf](2024-10-31_a9963bf_mcconf.xml) |  |
| 2024-11-15 | `10fe432` | 90 | 80 | 300 | 3000 | 40 | 30 | 5.5 | 0.03 | 1 | 20 | 2000 | 5 | [mcconf](2024-11-15_10fe432_mcconf.xml) |  |
| 2025-02-18 | `2764064` | 90 | 80 | 300 | 3000 | 40 | 30 | 5.5 | 0.03 | 1 | 20 | 2000 | 1 | [mcconf](2025-02-18_2764064_mcconf.xml) | **0604 release** |
| 2025-07-21 | `f668c5b` | 90 | 80 | 300 | 3000 | 40 | 30 | 5.5 | 0.03 | 1 | 20 | 2000 | 1 | [mcconf](2025-07-21_f668c5b_mcconf.xml) | newest |

## App configuration versions

CYC stores its power levels, speed limits and display options in the app configuration (see [CYC_SETTINGS_MAP.md](../../docs/CYC_SETTINGS_MAP.md) for what each field means).

| Date | Commit | File |
|---|---|---|
| 2024-06-25 | `af41657` | [appconf](2024-06-25_af41657_appconf.xml) |
| 2024-09-23 | `ff34b78` | [appconf](2024-09-23_ff34b78_appconf.xml) |
| 2024-09-30 | `750c722` | [appconf](2024-09-30_750c722_appconf.xml) |
| 2024-10-30 | `cd42782` | [appconf](2024-10-30_cd42782_appconf.xml) |
| 2024-11-04 | `b550cf0` | [appconf](2024-11-04_b550cf0_appconf.xml) |
| 2025-10-17 | `dd2b758` | [appconf](2025-10-17_dd2b758_appconf.xml) |
| 2025-10-17 | `5fc7ecd` | [appconf](2025-10-17_5fc7ecd_appconf.xml) |
| 2025-12-10 | `8f1b938` | [appconf](2025-12-10_8f1b938_appconf.xml) |
