# CYC default settings over time

What CYC's firmware sets as its default motor and app configuration for each bike, at every
point CYC changed it on their main development line, as VESC Tool XML files.

| Bike | Folder |
|---|---|
| Photon (Gen 1 hardware) | [photon](photon) |
| Photon (Gen 2 hardware) | [photon_gen2](photon_gen2) |
| Photon Pro | [photon_pro](photon_pro) |
| X12 + X1 Pro Gen 4 | [x12_gen4](x12_gen4) |
| X12 + X1 Pro Gen 4, MX (Bonnell 775 MX) | [x12_gen4_mx](x12_gen4_mx) |
| X12 + X1 Pro Gen 4, RS (Ristretto) | [x12_gen4_rs](x12_gen4_rs) |
| X12 + X1 Pro Gen 3 | [x12_gen3](x12_gen3) |
| X6 + X1 Pro Gen 3 | [x6_x1pro](x6_x1pro) |
| X6 + X1 Stealth | [x6_stealth](x6_stealth) |

Each folder's README has a table of the main motor values (current limits, power, resistance,
inductance, flux linkage, current loop gains, observer gain) per version, with the version in
CYC's current update (0604) marked.

Files are named `<date>_<CYC commit>_mcconf.xml` (motor) and `..._appconf.xml` (app). The
app files hold CYC's power levels, speed limits and display options in repurposed VESC fields;
[CYC_SETTINGS_MAP.md](../docs/CYC_SETTINGS_MAP.md) says which is which.

## How they were made

Not copied by hand. For each CYC commit, CYC's own default-setting code (`confgenerator.c`
plus the per-motor overrides in `conf_general.c`) was compiled on a PC with that bike's build
flags, run, and its output written as XML. Region variants (EU/EPAC, Japan) are excluded.
Scripts: [tools/tune-history](../tools/tune-history).

## Loading one

1. Use the CYC edition of VESC Tool and connect to the bike first.
2. Motor (or App) configuration > Load XML > pick the file.
3. Check the values, then Write.

A motor file replaces every motor setting, including the hall sensor table, resistance,
inductance and flux linkage. If your motor isn't exactly the stock one, run the motor and hall
detection again afterwards.

The battery cutoff voltages in the motor files (10 V) are CYC's placeholders: CYC's firmware
overwrites them while running from the battery settings in the app configuration.
