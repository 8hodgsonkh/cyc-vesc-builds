# Photon (Gen 2 hardware): CYC default settings over time

Each row is a point on CYC's main development line where the default motor configuration for this bike changed, oldest first. Region variants (EU/EPAC, Japan) are excluded. Generated from CYC's own source by compiling their default-setting code on a PC (see `tools/tune-history`). "Changed" counts the settings that differ from the row above. "0604 release" marks the defaults in CYC's current OTA firmware (source 2025-06-04), which is what the stock and unlocked 250604 builds in this repo set.

| Date | Commit | Phase A | Batt A | Abs A | W | R mΩ | L µH | λ mWb | kp | ki | Obs gain | SL ERPM | Changed | File | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-03-19 | `d83f62a` | 60 | 60 | 250 | 2000 | 115 | 130 | 12 | 0.08 | 1 | 4 | 2500 | first | [mcconf](2025-03-19_d83f62a_mcconf.xml) |  |
| 2025-06-04 | `7b08350` | 60 | 60 | 250 | 2000 | 115 | 130 | 12 | 0.08 | 1 | 4 | 2500 | 1 | [mcconf](2025-06-04_7b08350_mcconf.xml) | **0604 release** |
| 2025-07-18 | `3323b24` | 83 | 60 | 300 | 2000 | 40 | 80 | 8.5 | 0.04 | 1 | 14 | 2500 | 20 | [mcconf](2025-07-18_3323b24_mcconf.xml) |  |
| 2025-07-24 | `352fe1c` | 83 | 60 | 300 | 2000 | 40 | 90 | 7 | 0.06 | 1.5 | 14 | 2500 | 5 | [mcconf](2025-07-24_352fe1c_mcconf.xml) |  |
| 2025-07-25 | `652aab2` | 83 | 60 | 300 | 2000 | 40 | 90 | 7 | 0.06 | 1.5 | 11 | 2500 | 1 | [mcconf](2025-07-25_652aab2_mcconf.xml) |  |
| 2025-08-12 | `9bbb62c` | 83 | 60 | 300 | 2000 | 39 | 90 | 7 | 0.055 | 1 | 12 | 2500 | 9 | [mcconf](2025-08-12_9bbb62c_mcconf.xml) |  |
| 2025-08-15 | `b32ae11` | 83 | 60 | 300 | 2000 | 39 | 90 | 7 | 0.055 | 1 | 12 | 2500 | 2 | [mcconf](2025-08-15_b32ae11_mcconf.xml) |  |
| 2025-08-22 | `cf7f0d0` | 83 | 60 | 300 | 2000 | 39 | 90 | 7 | 0.055 | 1 | 15 | 2500 | 2 | [mcconf](2025-08-22_cf7f0d0_mcconf.xml) |  |
| 2025-08-25 | `1968893` | 83 | 60 | 300 | 2000 | 39 | 98 | 7 | 0.06 | 4 | 15 | 2500 | 4 | [mcconf](2025-08-25_1968893_mcconf.xml) |  |
| 2025-08-27 | `e30db25` | 77 | 60 | 300 | 2000 | 45 | 98 | 8.5 | 0.06 | 4 | 8 | 2500 | 9 | [mcconf](2025-08-27_e30db25_mcconf.xml) |  |
| 2025-08-28 | `372c26b` | 77 | 60 | 300 | 2000 | 42 | 98 | 8.5 | 0.055 | 1 | 8 | 2500 | 7 | [mcconf](2025-08-28_372c26b_mcconf.xml) |  |
| 2025-12-29 | `cd72791` | 77 | 60 | 300 | 2000 | 45 | 90 | 7 | 0.12 | 1 | 8 | 4000 | 13 | [mcconf](2025-12-29_cd72791_mcconf.xml) | newest |

## App configuration versions

CYC stores its power levels, speed limits and display options in the app configuration (see [CYC_SETTINGS_MAP.md](../../docs/CYC_SETTINGS_MAP.md) for what each field means).

| Date | Commit | File |
|---|---|---|
| 2025-03-19 | `d83f62a` | [appconf](2025-03-19_d83f62a_appconf.xml) |
| 2025-05-30 | `2e2e6f3` | [appconf](2025-05-30_2e2e6f3_appconf.xml) |
| 2025-08-08 | `c1fc6ff` | [appconf](2025-08-08_c1fc6ff_appconf.xml) |
| 2025-08-12 | `9bbb62c` | [appconf](2025-08-12_9bbb62c_appconf.xml) |
| 2025-08-15 | `b32ae11` | [appconf](2025-08-15_b32ae11_appconf.xml) |
| 2025-10-17 | `dd2b758` | [appconf](2025-10-17_dd2b758_appconf.xml) |
| 2025-10-17 | `5fc7ecd` | [appconf](2025-10-17_5fc7ecd_appconf.xml) |
| 2025-12-10 | `8f1b938` | [appconf](2025-12-10_8f1b938_appconf.xml) |
| 2026-06-26 | `0205653` | [appconf](2026-06-26_0205653_appconf.xml) |
