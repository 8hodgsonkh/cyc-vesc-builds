Earlier unlocked builds, kept for anyone already running them. For new installs use the
[current firmware release](https://github.com/8hodgsonkh/cyc-vesc-builds/releases/tag/cyc-firmware-2026-10-22).
Not affiliated with CYC Motor. Flash at your own risk.

| File | Bike | CYC source | Reports | Replaced by |
|---|---|---|---|---|
| `cyc503_proton_unlocked.bin` | Photon Pro | Feb 2026 (`5a7511e`) | `Proton 20250218T` | `CYC_PhotonPro_260610_unlocked.bin` |
| `cyc503_x12_x1pro_gen4_unlocked.bin` | X12 + X1 Pro Gen 4 | Feb 2026 (`5a7511e`) | `X12 20250811UL` | `CYC_X12_X1ProGen4_250604_unlocked.bin` |
| `cyc_x12_mx_vesctool.bin` | Bonnell 775 MX | June 2026 (`0205653`) | `X12 20260623MX` | `CYC_X12_775MX_250604_unlocked.bin` |

All three are CYC's firmware with `DISABLE_HW_LIMITS` on (see the current release for what that
changes), built from newer CYC development source than the 0604 code CYC actually ships. The
current release uses the shipping 0604 source instead, so its unlocked files differ from CYC's
stock firmware by that one switch only.

The changes to CYC's source for each are in
[firmware-src/older/](https://github.com/8hodgsonkh/cyc-vesc-builds/tree/main/firmware-src/older).

`SHA256SUMS.txt` has the checksums of every file in this release.
