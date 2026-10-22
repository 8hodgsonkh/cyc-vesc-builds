CYC 5.03 firmware for each CYC controller, built from CYC's own source: a **stock** and an
**unlocked** file per bike. Not affiliated with CYC Motor. Flash at your own risk.

## Which file

| Bike | Stock | Unlocked | Name the controller reports |
|---|---|---|---|
| Photon (Gen 1 hardware) | `CYC_Photon_250604_stock.bin` | `CYC_Photon_250604_unlocked.bin` | `Photon 20250604` |
| Photon Pro | `CYC_PhotonPro_260610_stock.bin` | `CYC_PhotonPro_260610_unlocked.bin` | `Proton 20260610` |
| X12 controller + X1 Pro Gen 4 | `CYC_X12_X1ProGen4_250604_stock.bin` | `CYC_X12_X1ProGen4_250604_unlocked.bin` | stock `X12 20250604`, unlocked `X12 20241028UL` |
| X12 controller + X1 Pro Gen 3 | `CYC_X12_X1ProGen3_250604_stock.bin` | `CYC_X12_X1ProGen3_250604_unlocked.bin` | stock `X12 20250604`, unlocked `X12 20241028UL` |
| Bonnell 775 MX (X12) | `CYC_X12_775MX_250604_stock.bin` | `CYC_X12_775MX_250604_unlocked.bin` | `X12 20250604MX` |
| X6 controller + X1 Pro Gen 3 | `CYC_X6_X1ProGen3_250604_stock.bin` | `CYC_X6_X1ProGen3_250604_unlocked.bin` | `X6 20250604` |
| X6 controller + X1 Stealth | `CYC_X6_X1Stealth_250604_stock.bin` | `CYC_X6_X1Stealth_250604_unlocked.bin` | `X6 20250604` |

`250604` / `260610` is the date of CYC's source the file was built from.

**Photon: Gen 1 hardware only.** CYC's own update file for the Photon is built for the Gen 1
hardware, and so is this one. Gen 2 hardware measures current differently, so a Gen 1 file
reads current wrong on it. Not sure which you have? Don't flash.

## Stock

Byte-for-byte the file CYC's app installs for that bike: each one was rebuilt from CYC's source
and its md5 matches the one in CYC's own update list.

| File | md5 (same as CYC's update) |
|---|---|
| `CYC_Photon_250604_stock.bin` | `88711a3e5da4e5e3813a693f59d58c82` |
| `CYC_X12_X1ProGen4_250604_stock.bin` | `1aee089037f856407a7968995e028a9e` |
| `CYC_X12_X1ProGen3_250604_stock.bin` | `8b50347bd8b700ffd6aae8009ffefa54` |
| `CYC_X12_775MX_250604_stock.bin` | `e09b1a349a69eb33840dfbecfb52473b` |
| `CYC_X6_X1ProGen3_250604_stock.bin` | `5e52ff311ac8cc37bcba0aaf30aadce5` |
| `CYC_X6_X1Stealth_250604_stock.bin` | `3d4bbe3837d5c7e3d53f3cdbbe9c8d1b` |

The Photon Pro has no entry in CYC's update list, so its stock file comes from CYC's newer
source (June 2026) with the settings of CYC's own last Photon Pro build. It can't be checked
against a CYC file.

With stock firmware only the CYC app connects. VESC Tool can't.

## Unlocked

The stock file with one line changed: CYC's own `DISABLE_HW_LIMITS` switch. What it does in
this source:

- **VESC Tool connects.** Stock firmware doesn't answer VESC Tool's connection request.
- **Settings aren't clamped.** Stock firmware cuts current, power and per-level values back to
  CYC's limits whenever settings are written to the controller. Unlocked keeps what you write.
- **No throttle soft start.** Stock ramps the duty limit up after you open the throttle (CYC's
  soft start setting) and keeps Max Duty at CYC's value. Unlocked has no ramp and takes Max Duty
  and Duty Start from the motor configuration (defaults 0.95 and 1, the same as stock).
- **No walk assist speed cap** (all except the Photon Pro). Stock caps the motor at 5000 ERPM
  while walk assist is held; the unlocked 250604 files don't. CYC's newer source used for the
  Photon Pro keeps the cap even when unlocked.
- **Max input voltage from the motor configuration.** Stock sets the overvoltage limit from the
  battery settings (always 72 V on the Photon Gen 1 and the Stealth). Unlocked uses Motor
  Settings > General > Advanced > Maximum Input Voltage, default 72 V (Photon), 84 V (Photon
  Pro), 85 V (X6) or 90 V (X12). Check it suits your battery.
- **Real motor temperature.** Stock shows motor temperatures above 45 °C squashed
  (45–130 °C displays as 45–100 °C). Unlocked shows the real value. The derate isn't affected.

Nothing else changes. The defaults are the same as stock, so apart from the soft start and walk
assist, the bike rides the same until you change settings.

The X12 unlocked files report CYC's own unlocked name, `X12 20241028UL`. The 775 MX one keeps
the MX name so the Bonnell app still recognises it.

Use the CYC edition of VESC Tool, not normal VESC Tool. Normal VESC Tool clamps CYC's values
when it reads them and writes the wrong numbers back.

## X12 + X1 Pro Gen 4, 140 A

`CYC_X12_X1ProGen4_260618_140A.bin`: stock X12 firmware (CYC's June 2026 source, reports
`X12 20260618`) with the battery current limit raised from 120 A to 140 A, and the power cap
per assist level raised from 6000 W to 12000 W (6000 W at 72 V is only about 83 A). It still
works with the CYC app and doesn't let VESC Tool connect. Your battery and BMS must handle
140 A. If the app offers a stock update and you take it, the 120 A / 6000 W limits come back.

## Flashing

See the [README](https://github.com/8hodgsonkh/cyc-vesc-builds#flashing). Charge the battery
first, save your settings (Save XML) if you can connect, and don't power off during the upload.

## Default settings

What each firmware sets as defaults, and how CYC's tunes changed over time:
[tunes/](https://github.com/8hodgsonkh/cyc-vesc-builds/tree/main/tunes). The rows marked
"0604 release" are the defaults in these 250604 files.

## Source

The exact changes to CYC's source for each file are in
[firmware-src/](https://github.com/8hodgsonkh/cyc-vesc-builds/tree/main/firmware-src).
Toolchain: GNU Arm Embedded 7-2018-q2-update.

`SHA256SUMS.txt` has the checksums of every file in this release.
