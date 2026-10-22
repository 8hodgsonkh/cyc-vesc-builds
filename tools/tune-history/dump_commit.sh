#!/bin/bash
# usage: dump_commit.sh <cyc source dir> <out dir> <product> FLAG=VAL ...
# Writes <out dir>/<product>_{mcconf,appconf}.xml with the defaults that source's firmware
# sets for that product. conf_general.h is restored afterwards.
# Exit 3 = the product didn't exist in that source (a flag it needs is missing).
set -e
H=$(cd "$(dirname "$0")" && pwd)
S=$(cd "$1" && pwd); O=$2; P=$3; shift 3
W=$(mktemp -d)
cp "$S/conf_general.h" "$W/conf_general.h.orig"
trap 'cp "$W/conf_general.h.orig" "$S/conf_general.h"; rm -rf "$W"' EXIT
for a in "$@"; do
	f=${a%%=*}; v=${a#*=}
	if grep -qE "^#define[[:space:]]+$f[[:space:]]+[01]" "$S/conf_general.h"; then
		sed -i -E "s/^(#define[[:space:]]+$f[[:space:]]+)[01]/\1$v/" "$S/conf_general.h"
	elif [ "$v" = 1 ]; then
		exit 3
	fi
	# some commits use a bare "#define EPAC" (tested with #ifdef)
	[ "$v" = 0 ] && sed -i -E "s|^#define[[:space:]]+$f[[:space:]]*(//.*)?$|//&|" "$S/conf_general.h"
done
cd "$W"
python3 -I "$H/gen_dumper2.py" "$S"
gcc -std=gnu99 -O0 -w -D__STM32F4xx_CONF_H -I"$H/stub" -I"$S" -I"$S/mcconf" -I"$S/appconf" -I"$S/hwconf" -I"$S/applications" dumper.c -o dumper -lm
./dumper > defaults.tsv
awk -F'\t' '$2=="l_current_max" && $3+0 > 0 {ok=1} END {exit !ok}' defaults.tsv || exit 3
mkdir -p "$O"
python3 -I "$H/gen_xml.py" defaults.tsv "$H/params-5.03" "$O" "$P" > /dev/null
