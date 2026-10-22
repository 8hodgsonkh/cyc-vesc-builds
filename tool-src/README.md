# VESC Tool CYC source

The modded VESC Tool for CYC 5.03 firmware, as changes on upstream
[vedderb/vesc_tool](https://github.com/vedderb/vesc_tool).

## Main build (VESC Tool 7.00 base)

[`vesc_tool_7.00_cyc/`](vesc_tool_7.00_cyc): upstream at the commit in `UPSTREAM_COMMIT`
(release 7.00) plus four patches:

1. **CYC 5.03 edition**: rewrites `res/config/5.03/parameters_appconf.xml` so the 93 settings
   CYC hijacks are labelled by what CYC uses them for, have ranges that fit CYC's values,
   and sit together under ADC > CYC Settings. Because renamed drop-down entries change the
   tool's computed config signature, the XML carries the firmware's real signature
   (`SignatureOverride`), which `ConfigParams` now honours. Also ignores out-of-range drop-down
   values instead of corrupting them, and adds the Android build script.
2. Android build fix (Gradle on TLS 1.2).
3. Desktop: shows the CYC Settings list on the ADC page's General tab.
4. Windows (MinGW/MXE): fixes a link error in Qt's Windows Bluetooth library.

```
git clone https://github.com/vedderb/vesc_tool.git
cd vesc_tool
git checkout $(cat ../tool-src/vesc_tool_7.00_cyc/UPSTREAM_COMMIT)
git am ../tool-src/vesc_tool_7.00_cyc/patches/*.patch
```

Then build as upstream VESC Tool (`CONFIG += build_original`). The macOS build is
[.github/workflows/vesc-tool-macos.yml](../.github/workflows/vesc-tool-macos.yml).

## Classic build (VESC Tool 3.01 base)

[`vesc_tool_3.01_cyc_classic/`](vesc_tool_3.01_cyc_classic): `cyc_classic.diff` against
upstream `release_3_01` (commit in `UPSTREAM_COMMIT`). The same XML rewrite, signature override
and drop-down guard, plus: the CYC Settings list on the desktop ADC page, all app pages shown
whatever app is selected, the config profile loaded at start-up so the menus work offline,
Android 12+ Bluetooth permission requests, Android packaging from the 7.00 tree, and an
`#include <iterator>` for newer GCC.

```
git checkout $(cat ../tool-src/vesc_tool_3.01_cyc_classic/UPSTREAM_COMMIT)
patch -p1 < ../tool-src/vesc_tool_3.01_cyc_classic/cyc_classic.diff
```

## XML scripts

`cyc_xml_patch.py` and `cyc_xml_regroup.py` produce the CYC `parameters_appconf.xml` from
upstream's 5.03 one (`python3 cyc_xml_patch.py <xml>`, then `cyc_xml_regroup.py <xml>`). Both
patch sets already contain their output.
