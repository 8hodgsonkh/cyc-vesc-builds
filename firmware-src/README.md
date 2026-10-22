# Firmware source changes

Every firmware file in the releases is CYC's 5.03 source with only the changes in the
matching `.diff` here. Almost all of them touch one file, `conf_general.h`, where CYC selects
the bike and its options.

| Files | CYC source |
|---|---|
| `CYC_*_250604_*` | CYC commit `7b08350`, "0604 batch update" (2025-06-04), the source of CYC's current update files |
| `CYC_PhotonPro_260610_*`, `CYC_X12_X1ProGen4_260618_140A` | CYC commit `0205653` (2026-06-26), newest |
| `older/cyc503_proton_unlocked`, `older/cyc503_x12_x1pro_gen4_unlocked` | CYC commit `5a7511e` (2026-02-13) |
| `older/cyc_x12_mx_vesctool` | CYC commit `0205653` |

The stock 250604 builds come out byte-identical to CYC's own update files (md5s in the release
notes), which confirms the source and flags match what CYC built.

## Building

GNU Arm Embedded toolchain **7-2018-q2-update** (newer GCC breaks this 5.03-era code base).
In the CYC source tree, apply the diff, then:

```
rm -rf .dep build
make
```

Output: `build/BLDC_4_ChibiOS.bin`. The `.dep` folder in CYC's tree is stale and has to go
before the first build.
