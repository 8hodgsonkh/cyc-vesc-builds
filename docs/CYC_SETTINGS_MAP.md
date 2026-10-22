# Where CYC's settings live in VESC Tool

Written for the X1 Pro Gen 4 (X12 controller) on unlocked CYC 5.03 firmware. The other
CYC bikes use the same fields; the defaults in brackets differ (see `tunes/`).

CYC did not add their own settings to VESC firmware. They reused existing VESC
parameters and gave them new meanings. VESC Tool does not know that, so every CYC
setting shows up under a VESC name. This page is the decoder.

## Use the CYC edition tool

The CYC edition of VESC Tool (7.00 and 3.01, all platforms) has the 5.03 app-config
profile rewritten: every repurposed field is labelled "CYC ..." with its real meaning
and unit, ranges fit CYC's values, and the drop-downs list CYC's options (Street/Race,
wheel sizes, display models, motor types). All of them are together under
**App Settings > ADC > CYC Settings**. Reading and writing App Config is safe with it.
The trainer zones are labelled "CYC Trainer ...".

The tables below give each field's original place, which is where a stock VESC Tool
shows it.

The warnings in "Read this first" about the stock tool still apply if anyone
uses a stock VESC Tool (3.01 or the newest one) on this controller.

## Read this first

1. **Do not press "Write App Config" with a stock VESC Tool.** When the tool reads
   the config it pushes each value into an on-screen spinbox, the spinbox clamps
   it to VESC's normal range, and that clamped value goes straight back into the
   tool's copy of the config. Several CYC values are far outside VESC's ranges
   (1500 W in a field VESC thinks is a rotation angle capped at 360, for example).
   Writing app config back would overwrite those with the clamped numbers.
   Read-only use of the App Settings pages is fine.
2. **Motor Settings are safe to read and write.** CYC did not repurpose motor
   config. But a handful of motor fields are recomputed by CYC's own logic at
   runtime (list at the bottom), so editing those in VESC Tool has no lasting
   effect.
3. **Never take the Firmware page's offered updates.** The tool will offer stock
   VESC firmware for whatever hardware name it guesses. That is not this board.
   Only flash CYC files through Custom File.
4. **The display and the CYC app push their own settings on every boot** (units,
   wheel size, battery class, street/race, display model). Change those on the
   display. VESC Tool edits to them get overwritten.

The tables mark each field with its editor limit in the stock tool:
**ok** = CYC's values fit, **clamped** = the tool cannot enter or hold CYC's
value, **no entry** = a drop-down that is missing the index CYC uses.

## Connecting

- Bluetooth only. USB is turned off in CYC's firmware (`main.c`: "dont use usb on
  GD32F405").
- VESC Tool 3.01: connects in full mode, shows firmware 5.03 and the hardware name
  (for example `X12       20241028UL`) followed by the serial.
- Newest VESC Tool: same, plus a "Firmware Update Available: old but mostly
  compatible" dialog and "limited mode" in the status bar. Config pages still
  work. Ignore the update prompt.

## Street mode power table (X1 Pro Gen 4)

Three anchor values per column. The display's assist levels are derived from
them (level 3 = anchor 1, level 6 = anchor 2, level 9 = anchor 3, the rest are
fractions and blends, as read from `app_control.c`). Torque figures are a
percentage of motor current max. X12 defaults in brackets.

| Anchor | Throttle power (W) | Throttle torque (%) | PAS power (W) | PAS torque (%) |
|---|---|---|---|---|
| 1 | App › IMU › **Accelerometer Confidence Decay** [1000] clamped at 999 | App › IMU › **Mahony KP** [60] ok | App › IMU › **Mahony KI** [500] ok | App › IMU › **Madgwick Beta** [20] ok |
| 2 | App › IMU › **Imu Rotation Roll** [1500] clamped at 360 | App › IMU › **Imu Rotation Pitch** [75] ok | App › IMU › **Imu Rotation Yaw** [750] clamped at 360 | App › IMU › **Accel Offset X** [40] clamped at 16 |
| 3 | App › PPM › General › **TC Max ERPM Difference** [2000] ok | App › PPM › Mapping › **Input Deadband** [90] clamped, shown as % of 1 | App › PPM › Throttle Curve › **Throttle Expo** [1000] clamped at 5 | App › PPM › Throttle Curve › **Throttle Expo Brake** [60] clamped at 5 |

## Race mode power table

| Anchor | Throttle power (W) | Throttle torque (%) | PAS power (W) | PAS torque (%) |
|---|---|---|---|---|
| 1 | App › VESC Remote › **Positive Ramping Time** [3000] clamped at 1000 | App › VESC Remote › **Negative Ramping Time** [75] ok | App › VESC Remote › **ERPM Per Second Cruise Control** [800] ok | App › VESC Remote › **Input Deadband** [35] clamped, shown as % of 1 |
| 2 | App › VESC Remote › **Smart Reverse Max Duty Cycle** [4500] clamped at 1 | App › VESC Remote › **Smart Reverse Ramp Time** [85] ok | App › Balance › Multi ESC › **Roll Steer KP** [1250] ok | App › Balance › Startup › **Brake Current** [50] ok |
| 3 | App › Balance › Multi ESC › **Roll Steer ERPM KP** [6000] ok | App › Balance › Multi ESC › **Yaw Current Clamp** [100] ok | App › PPM › General › **Negative Ramping Time** [2000] clamped at 1000 | App › PPM › General › **Max ERPM for direction switch** [75] ok |

## Speed limits (km/h, regardless of display unit)

| CYC setting | VESC Tool field | Default | Limit |
|---|---|---|---|
| Street throttle speed limit | App › PPM › Mapping › **Pulselength Start** | 32 | ok |
| Race throttle speed limit | App › PPM › Mapping › **Pulselength End** | 100 | ok |
| Street PAS speed limit | App › PPM › General › **Smart Reverse Max Duty Cycle** | 45 | clamped at 1 |
| Race PAS speed limit | App › PPM › Mapping › **Pulselength Center** | 100 | ok |

## Bike setup

| CYC setting | VESC Tool field | Values | Limit |
|---|---|---|---|
| Motor type | App › IMU › **IMU AHRS Mode** | Madgwick = X1 Pro Gen 4, Mahony = X1 Pro Gen 3, Madgwick Fusion = Stealth gen 1 (Stealth gen 3 = index 3, not in the list) | no entry for 3 |
| Region | App › IMU › **Sample Rate** | 0 USA, 1 Canada, 2 EU, 3 Unrestricted, 4 EPAC, 5 Japan | clamped, min 1 (USA unreachable) |
| Wheel size | App › NRF › **Retry Delay** (drop-down index) | 250 µS = 16", 500 = 18", 750 = 20", 1000 = 22", 1250 = 24", 1500 = 26", 1750 = 27.5", 2000 = 28"/700c, 2250 = 29", 2500 = use the mm value below | ok |
| Wheel size in mm (when index 9) | App › Balance › Tune Modifiers › **Constant Tiltback ERPM** | mm | ok |
| Battery class | App › NRF › **Retries** | 8 = 24 V, 10 = 36 V, 12 = 48 V, 14 = 52 V, 16 = 60 V, 20 = 72 V | clamped at 15 |
| Battery min voltage | App › Balance › Tune Modifiers › Torque Tilt › **Current Filter** | volts [54] | ok |
| Battery max voltage | App › Balance › Tune Modifiers › Turn Tilt › **Strength** | volts [77] | ok |
| Display model | App › NRF › **Speed** | 250 Kbit = 750C, 1 MBit = SW102/DS103, 2 MBit = smart display | ok |
| Display model (written by display) | App › NRF › **Address 0** | 0 = 750C, 1 = SW102/DS103, 2 = smart display | ok |
| Torque sensor model | App › PPM › General › **PID Max ERPM** | 0 = Gen 2, 1 = Gen 3 | ok |
| Wheel speed magnets | App › VESC Remote › **TC Max ERPM Difference** | magnets per wheel rev | ok |
| Gen 2 torque baseline voltage | App › PPM › General › **Positive Ramping Time** | volts | ok |
| Torque sensor Nm offset | App › General › **UAVCAN Raw RPM Max** | Nm | ok |
| Invert motor direction | App › General › **Servo Output Enable** | on/off | ok |
| Temperature unit | App › PAS › **Control Type** | Off = °C, Cadence = °F | ok |
| Speed unit | App › PAS › **Invert Pedal Direction** | off = km, on = miles | ok |

## Modes and switches

| CYC setting | VESC Tool field | Values | Limit |
|---|---|---|---|
| Street / race | App › PAS › **Sensor Type** | Quadrature = street; race is index 1, not in the list | no entry (a race bike reads back as blank and would be written as 255, which the firmware treats as race) |
| Display settings lock | App › PPM › General › **Median Filter** | on = locked | ok |
| Mode after reboot | App › NRF › **TX Power** | -18 dBm = remember last, -12 dBm = street, -6 dBm = race | ok |
| Cadence start | App › PPM › General › **Control Type** | Off = off, Current = on | ok |
| Backwards cutout | App › PPM › Throttle Curve › **Throttle Expo Mode** | Exponential = off, Natural = on | ok |
| Motor NTC on/off | App › VESC Remote › **Control Type** | Off = no NTC, Current = NTC on (the display can also write 4 = "battery series bypass", which the list does not have) | no entry for 4 |
| Temperature sensor present | App › PPM › General › **Safe Start** | Disabled = no sensor, Regular = sensor on | ok |
| Brake sensor enable | App › NRF › **Send ACK** | on/off | ok |
| Field weakening current | App › Balance › Tune Modifiers › Booster › **Current Boost** | % of 275 A | ok |
| PAS sensitivity | App › Balance › Startup › **Startup Pitch Axis Angle Tolerance** | [30] | ok |
| PAS power ramp-up time | App › Balance › Startup › **Startup Roll Axis Angle Tolerance** | [75] | ok |
| New motor assist factor | App › Balance › Tiltback › Low Voltage › **Angle** | [50] | clamped at 45 |
| Throttle ramp | App › ADC › **Positive Ramping Time** | seconds | ok |

## Trainer zones (stationary mode, rarely needed)

Heart-rate and human-power zones live in App › Balance (Tune: P, I, D, Loop
Hertz, Loop Time Correction Filter; Fault: every field; Multi ESC: Yaw P/I/D;
Tune Modifiers: Booster Start Angle/Ramp Up, Torque Tilt and Turn Tilt fields)
and App › IMU (Accel Offset Y/Z, Gyro Offset X/Y/Z). Defaults and meanings are
commented in `appconf_x12_x1_pro_gen4_5.03_default.h` in the firmware source.

## Motor Settings fields CYC recomputes at runtime

Editing these in VESC Tool works until CYC's logic next touches them:

- Max Wattage: set from whichever power anchor is active.
- Max Current Scale: set from the active torque anchor.
- Max / Min Input Voltage, Battery Cut Start / End: from battery class, min V, max V.
- Max ERPM and ERPM Start: from the active speed limit.
- Max Duty and Duty Start: CYC's duty limiter, disabled in this unlocked build.
- Motor temp start / end / accel decrease, Invert Direction, motor-type presets
  (flux linkage, current KP/KI, sensor mode, switching frequency).

## Realtime data page

CYC also repurposed the realtime packet, so a few RT Data readouts are not what
they say: "Ah Charged" is trip time, "Wh Charged" is cadence, "Tachometer" is
throttle voltage, "Tachometer ABS" is torque in Nm, "PID Pos" is an input pin
bitmap, and "Temp MOSFET 3" is the MCU temperature. Temps, currents, duty, RPM,
voltage, Ah, Wh and fault code are real. The mobile app's main gauges use a
different packet that CYC left alone.

## Source notes

Field meanings come from CYC's own comments in
`appconf_x12_x1_pro_gen4_5.03_default.h`, the clamp tables in `commands.c`
(SET_APPCONF) and the readers in `applications/app_control.c` and
`mc_interface.c`. VESC Tool page and tab names come from the 5.03
`parameters_appconf.xml` grouping. Editor limits are that XML's min/max.
The clamp-on-read behaviour is from `widgets/parameditdouble.cpp` and
`parameditenum.cpp` in VESC Tool 3.01: `paramChangedDouble` calls
`setValue` on the spinbox, which clamps and re-emits into `updateParamDouble`.
Not tested on hardware.
