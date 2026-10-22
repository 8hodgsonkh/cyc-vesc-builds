# CYC firmware and VESC Tool

Firmware for CYC controllers (Photon, Photon Pro, X12 and X6), built straight from CYC's own
5.03 source, plus a modded VESC Tool that actually understands CYC's settings.

Everything you download is on the Releases page of this repo (right hand side of the main
page, or the Releases link at the top on a phone).

This isn't from CYC and they don't support it. Flashing can brick a controller, and raising
limits can cook a controller, motor or battery. Your bike, your risk. I have tested Proton firmware and had feedback for the x12/x1 pro gen 4 and they are working.


## Quick start

1. Get the VESC Tool for your phone or computer.
2. Find your bike in the firmware table and download the unlocked file.
3. Flash it with the VESC Tool.


## Firmware

Release: CYC 5.03 firmware (cyc-firmware-2026-10-22)

There are two files for each bike. Stock is exactly what CYC's app installs, byte for byte, so
you can always go back to factory. Unlocked is stock with CYC's own unlock switch turned on:
VESC Tool can connect, and your current and power settings stick instead of being cut back to
CYC's limits.

| Your bike               | Stock file                         | Unlocked file                         |
| ----------------------- | ---------------------------------- | ------------------------------------- |
| Photon (Gen 1 hardware) | CYC_Photon_250604_stock.bin        | CYC_Photon_250604_unlocked.bin        |
| Photon Pro              | CYC_PhotonPro_260610_stock.bin     | CYC_PhotonPro_260610_unlocked.bin     |
| X12 with X1 Pro Gen 4   | CYC_X12_X1ProGen4_250604_stock.bin | CYC_X12_X1ProGen4_250604_unlocked.bin |
| X12 with X1 Pro Gen 3   | CYC_X12_X1ProGen3_250604_stock.bin | CYC_X12_X1ProGen3_250604_unlocked.bin |
| Bonnell 775 MX          | CYC_X12_775MX_250604_stock.bin     | CYC_X12_775MX_250604_unlocked.bin     |
| X6 with X1 Pro Gen 3    | CYC_X6_X1ProGen3_250604_stock.bin  | CYC_X6_X1ProGen3_250604_unlocked.bin  |
| X6 with X1 Stealth      | CYC_X6_X1Stealth_250604_stock.bin  | CYC_X6_X1Stealth_250604_unlocked.bin  |

Photon owners: these are for Gen 1 hardware only, same as CYC's own update. Gen 2 reads
current differently, so if you're not sure which you've got, don't flash.

The same release also has CYC_X12_X1ProGen4_260618_140A.bin, an X12 Gen 4 build with the
battery current raised to 140 A that still works with the CYC app. Older unlocked builds are
in the release called Older unlocked builds.

### What else the unlock changes

Please read this before you flash an unlocked file.

The throttle soft start is off, so the throttle no longer ramps in gently.

Walk assist has no speed cap. Stock limits the motor while you hold walk assist, unlocked
doesn't. The Photon Pro is the exception and keeps its cap.

The max input voltage comes from the motor settings instead of your battery settings, so
check it suits your battery.

Motor temperature shows the real number. Stock fakes it lower once it goes above 45 °C.

Apart from that it rides exactly like stock until you change settings. The release notes on
the firmware release have the full details.


## VESC Tool

Release: VESC Tool CYC, for CYC 5.03 firmware (vesc-tool-cyc-2026-10-22)

CYC firmware hijacks a load of normal VESC settings for its own stuff, like power levels,
speed limits and battery settings. Normal VESC Tool shows them under the wrong names, and
pressing Write corrupts them. This modded VESC Tool shows every hijacked setting under its
real CYC name, all in one list called CYC Settings on the ADC page in App Settings.

| Platform | File                                          |
| -------- | --------------------------------------------- |
| Android  | vesc_tool_cyc_503_android.apk                 |
| Windows  | vesc_tool_cyc_503_windows.zip                 |
| Mac      | vesc_tool_cyc_503_macos.zip                   |
| Linux    | vesc_tool_cyc_503_classic_linux_x86_64.tar.gz |

It only talks to unlocked firmware, stock CYC firmware ignores VESC Tool completely. It
connects over Bluetooth, because CYC turned USB off in their firmware.

On Windows, connection through bluetooth is the method, cyc controllers dont have usb like normal vesc controllers.

On a Mac, the app isn't signed by Apple, so the first time you open it go to System Settings,
Privacy and Security, and click Open Anyway.

The release also has a classic version built on the older VESC Tool 3.01, in case you need it.


## Flashing

Before you start, charge the battery. If you can already connect, save your settings first
(Save XML in the Motor and App config menus) so you've got a backup.

### Already on an unlocked build

1. Connect with the CYC VESC Tool.
2. Open the Firmware page, choose Custom File, pick the .bin for your bike and press Upload.
3. Don't turn anything off until it says it's done. Give it another 10 seconds and the
   controller restarts by itself.

### Coming from stock CYC firmware

Flash the firmware using the CYC app, the unlock code to allow flashing is 32531.

### Going back to stock

Flash the stock file the same way. After that only the CYC app can connect again, not VESC Tool anymore. (i think cyc app still works with the vesc tool firmware)


## CYC's tunes over time

The tunes folder in this repo has CYC's default settings for every bike, at every point CYC
changed them, as XML files you can load into VESC Tool. Each bike has a table of the main
values so you can see how CYC's tune changed. They're generated from CYC's own source, not
typed out by hand. Dont believe the values from foc motor test as they are unstable on mid drives. current ki needs to be low or the motor will bounce the chain off the casette and oscillate.

To put a bike back on one of CYC's tunes, connect first, then Load XML and Write.

Careful though, a motor XML overwrites everything, including your hall sensor table and motor
measurements. If your motor isn't bone stock, run motor and hall detection again afterwards.

## Coming soon

My own firmware for CYC controllers, built on VESC firmware 7.00 instead of CYC's 5.03. It's
already running on the Photon Pro and on the X12 with the X1 Pro Gen 4, and it'll come with
its own matching VESC Tool.

A taste of what's in it:

VESC 7.00 motor control, including the MXLemming flux observers that CYC's 5.03 doesn't have.

A Smart Current throttle that checks road speed, battery voltage headroom and chain slack
before it lets the torque through.

A Duty Target throttle, where the throttle sets a target and the controller ramps to it, so
it rides more like a speed throttle than a torque one.

Gear detection that works out which gear you're in from wheel speed and motor RPM.

Shift assist timed by the cassette: power stays off until the cassette has actually turned
far enough for the chain to land on the new cog, counted on the motor's own rotation, so it
adapts to how fast you're riding. When you shift if duty limits your motors speed to match the next gear instantly to avoid loaded shifts

Assist levels that cap power rather than motor current, so every level still pulls away with
full torque and the cap only bites as speed builds.

CYC's Gen 3 torque sensor maths, rebuilt natively on 7.00.

A boot guard: if the controller can't stay running for 10 seconds three boots in a row, it
starts on default settings and leaves your saved ones untouched, so a bad setting can't lock
you out and nothing gets lost.

CYC's displays spoken natively, with a live terminal command for debugging the display link.

More when it's ready.

## For the nerds

| Folder             | What's in it                                                    |
| ------------------ | --------------------------------------------------------------- |
| tunes              | CYC default settings per bike over time                         |
| docs               | CYC_SETTINGS_MAP.md, which VESC setting holds which CYC setting |
| firmware-src       | The exact changes to CYC's source for every firmware file       |
| tool-src           | The VESC Tool changes, as patches on upstream VESC Tool         |
| tools/tune-history | The scripts that generate the tunes folder                      |
| releases           | Release notes (the files themselves are on the Releases page)   |

The stock files rebuild byte for byte identical to CYC's official updates, so you know they're
the real thing. Each unlocked file is that plus one switch.

License: VESC firmware and VESC Tool are GPL 3.0. The firmware is CYC's 5.03 fork of the VESC
firmware with the changes in the firmware-src folder. The VESC Tool builds are upstream VESC
Tool with the patches in the tool-src folder.
