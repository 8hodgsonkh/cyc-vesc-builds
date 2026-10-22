# Photon (Gen 1 hardware): CYC default settings over time

Each row is a point on CYC's main development line where the default motor configuration for this bike changed, oldest first. Region variants (EU/EPAC, Japan) are excluded. Generated from CYC's own source by compiling their default-setting code on a PC (see `tools/tune-history`). "Changed" counts the settings that differ from the row above. "0604 release" marks the defaults in CYC's current OTA firmware (source 2025-06-04), which is what the stock and unlocked 250604 builds in this repo set.

| Date | Commit | Phase A | Batt A | Abs A | W | R mΩ | L µH | λ mWb | kp | ki | Obs gain | SL ERPM | Changed | File | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-06-25 | `af41657` | 60 | 60 | 250 | 2000 | 75 | 55 | 13 | 0.1 | 1 | 5 | 5000 | first | [mcconf](2024-06-25_af41657_mcconf.xml) |  |
| 2024-09-20 | `2c5f660` | 60 | 60 | 250 | 2000 | 75 | 110 | 13 | 0.1 | 1 | 5 | 5000 | 3 | [mcconf](2024-09-20_2c5f660_mcconf.xml) |  |
| 2024-09-23 | `ff34b78` | 60 | 60 | 250 | 2000 | 75 | 110 | 13 | 0.1 | 1 | 5 | 5000 | 1 | [mcconf](2024-09-23_ff34b78_mcconf.xml) |  |
| 2024-10-28 | `248e633` | 60 | 60 | 250 | 2000 | 115 | 130 | 12 | 0.08 | 1 | 4 | 2500 | 7 | [mcconf](2024-10-28_248e633_mcconf.xml) |  |
| 2024-10-28 | `1e7b547` | 60 | 60 | 250 | 2000 | 75 | 110 | 13 | 0.1 | 1 | 5 | 5000 | 7 | [mcconf](2024-10-28_1e7b547_mcconf.xml) |  |
| 2024-10-28 | `420cea9` | 60 | 60 | 250 | 2000 | 115 | 130 | 12 | 0.08 | 1 | 4 | 2500 | 7 | [mcconf](2024-10-28_420cea9_mcconf.xml) | **0604 release**, newest |

## App configuration versions

CYC stores its power levels, speed limits and display options in the app configuration (see [CYC_SETTINGS_MAP.md](../../docs/CYC_SETTINGS_MAP.md) for what each field means).

| Date | Commit | File |
|---|---|---|
| 2024-06-25 | `af41657` | [appconf](2024-06-25_af41657_appconf.xml) |
| 2024-09-20 | `2c5f660` | [appconf](2024-09-20_2c5f660_appconf.xml) |
| 2024-09-23 | `ff34b78` | [appconf](2024-09-23_ff34b78_appconf.xml) |
| 2024-09-30 | `750c722` | [appconf](2024-09-30_750c722_appconf.xml) |
| 2024-10-28 | `248e633` | [appconf](2024-10-28_248e633_appconf.xml) |
| 2024-10-28 | `1e7b547` | [appconf](2024-10-28_1e7b547_appconf.xml) |
| 2024-10-28 | `420cea9` | [appconf](2024-10-28_420cea9_appconf.xml) |
| 2024-10-31 | `a9963bf` | [appconf](2024-10-31_a9963bf_appconf.xml) |
| 2025-08-08 | `c1fc6ff` | [appconf](2025-08-08_c1fc6ff_appconf.xml) |
| 2025-08-12 | `9bbb62c` | [appconf](2025-08-12_9bbb62c_appconf.xml) |
| 2025-10-17 | `dd2b758` | [appconf](2025-10-17_dd2b758_appconf.xml) |
| 2025-10-17 | `5fc7ecd` | [appconf](2025-10-17_5fc7ecd_appconf.xml) |
| 2025-12-10 | `8f1b938` | [appconf](2025-12-10_8f1b938_appconf.xml) |
