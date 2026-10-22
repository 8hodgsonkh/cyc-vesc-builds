# tune-history

Generates [`tunes/`](../../tunes) from CYC's git repository.

```
./history.sh <CYC git repo> <work dir>          # dump every bike at every main-line commit
python3 history.py <CYC git repo> <work dir> ../../tunes   # keep the changes, write READMEs
```

- `history.sh`: walks the first-parent history of CYC's `training-mode` branch (their main
  line; it holds both the 0604 release and the newest code) and, for every commit touching
  presets or default code, runs `dump_commit.sh` once per bike.
- `dump_commit.sh <source dir> <out dir> <bike> FLAG=VAL...`: sets the bike's flags in
  `conf_general.h` (region flags off), builds and runs the dumper, writes the XMLs.
  Exit 3 means that bike didn't exist yet at that commit.
- `gen_dumper2.py`: writes the dumper C file: CYC's default functions from `confgenerator.c`
  verbatim, plus the fallback blocks of `conf_general_read_{mc,app}_configuration` in
  `conf_general.c` (where CYC applies the Gen 3, X6 and Stealth overrides).
- `gen_xml.py`: turns the dumper output into VESC Tool XML using the 5.03 parameter list in
  `params-5.03/`.
- `stub/`: empty ChibiOS headers so the firmware headers compile on a PC.

Needs `gcc`, `python3` and `git`.
