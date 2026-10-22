Modded VESC Tool that shows the VESC settings CYC hijacked under their real CYC names. For
CYC 5.03 firmware that lets VESC Tool connect (the **unlocked** files in the firmware
release). Stock CYC firmware ignores VESC Tool.

## Why not normal VESC Tool

CYC firmware stores its own settings (power and torque per assist level, speed limits,
battery, display options) in VESC settings meant for other things. Normal VESC Tool:

- shows them under the wrong names, so you can't tell what you're changing, and
- clamps them to VESC's normal ranges when it reads them, so pressing Write sends the
  clamped numbers back and corrupts CYC's settings.

This tool puts all 93 CYC settings under **App Settings > ADC > CYC Settings**, labelled
by what CYC uses them for, with ranges that fit CYC's values. Everything else is normal
VESC Tool. Field-by-field map:
[CYC_SETTINGS_MAP.md](https://github.com/8hodgsonkh/cyc-vesc-builds/blob/main/docs/CYC_SETTINGS_MAP.md).

## Files

| File | Platform | Notes |
|---|---|---|
| `vesc_tool_cyc_503_android.apk` | Android 6+, 64-bit | Shows up as "VESC Tool CYC"; installs next to normal VESC Tool |
| `vesc_tool_cyc_503_windows.zip` | Windows | Single exe, no install |
| `vesc_tool_cyc_503_macos.zip` | macOS | Intel and Apple Silicon (runs through Rosetta) |
| `vesc_tool_cyc_503_classic_linux_x86_64.tar.gz` | Linux | Needs Qt 5.15 installed |
| `vesc_tool_cyc_503_classic_android.apk` | Android | Classic, shows up as "X1 Gen 4 VESC Tool" |
| `vesc_tool_cyc_503_classic_windows.zip` | Windows | Classic |

The main files are built on VESC Tool 7.00, the "classic" ones on the older VESC Tool 3.01,
with the same CYC changes. Both talk to CYC's 5.03 firmware. Use the main ones unless you have
a reason not to; the classic phone app can't load XML files.

## Connecting

VESC Tool reaches CYC controllers over Bluetooth. USB is turned off in CYC's firmware.

- **Phone:** turn Bluetooth and location on, open the app, connect.
- **Windows:** this build uses Qt's older Windows Bluetooth support, which as far as I know only
  finds devices already paired in Windows Bluetooth settings. Pair the controller there first.
  Not yet tested with a CYC controller.
- **Mac:** allow Bluetooth access when macOS asks.

## Loading a configuration XML

Connect to the bike **first**. VESC Tool only switches to the CYC 5.03 settings once it is
connected, and a file loaded before that is thrown away. Then Motor or App configuration >
Load XML, check the values, and Write.

Loading a file replaces every setting in it. CYC's default XMLs are in
[tunes/](https://github.com/8hodgsonkh/cyc-vesc-builds/tree/main/tunes).

## Installing

- **Android:** download the apk on the phone and open it; allow installing from your browser
  or file manager when asked.
- **Windows:** unzip, run the exe. SmartScreen may warn about an unknown publisher: More info >
  Run anyway.
- **Mac:** unzip and move "VESC Tool" to Applications. The app isn't signed by Apple, so the
  first time macOS blocks it: open System Settings > Privacy & Security and click Open Anyway,
  or run `xattr -dr com.apple.quarantine "/Applications/VESC Tool.app"` in Terminal.
- **Linux:** `tar xzf vesc_tool_cyc_503_classic_linux_x86_64.tar.gz && ./vesc_tool_cyc_503_classic`.
  Built on Arch against Qt 5.15; older distributions may be missing the libraries.

## Source

Upstream VESC Tool (7.00, and 3.01 for classic) plus the changes in
[tool-src/](https://github.com/8hodgsonkh/cyc-vesc-builds/tree/main/tool-src). The macOS build
is made by this repository's GitHub Actions workflow from that source.

`SHA256SUMS.txt` has the checksums of every file in this release.
