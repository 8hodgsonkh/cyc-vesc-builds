#!/bin/bash
# usage: history.sh <cyc git dir> <out dir>
# Dumps every product's default motor/app config at every commit on CYC's main line
# (first parent of training-mode, the branch holding both the 0604 release and the newest code) that
# touched presets, the default-override code or the hw headers. history.py dedupes.
H=$(cd "$(dirname "$0")" && pwd)
G=$1; O=$(mkdir -p "$2" && cd "$2" && pwd)/raw
ZERO="PHOTON_181=0 PHOTON_181_2=0 PROTON_181=0 VSBM=0 VSBM_181=0 VPRO_181=0 MX=0 AM=0 RISTRETTO=0 X1PRO_4=0 X1PRO_3=0 X1STL=0 EPAC=0 JAPAN=0 BFE=0 NK=0 HW_775SE=0 FW_CURRENT=0 CALIBRATION=0"
declare -A PROD=(
	[photon]="PHOTON_181=1"
	[photon_gen2]="PHOTON_181=1 PHOTON_181_2=1"
	[photon_pro]="PROTON_181=1 PHOTON_181_2=1"
	[x12_gen4]="VSBM=1 VPRO_181=1 X1PRO_4=1"
	[x12_gen4_mx]="VSBM=1 VPRO_181=1 X1PRO_4=1 MX=1"
	[x12_gen4_rs]="VSBM=1 VPRO_181=1 X1PRO_4=1 RISTRETTO=1"
	[x12_gen3]="VSBM=1 VPRO_181=1 X1PRO_3=1"
	[x6_x1pro]="VSBM=1 VSBM_181=1 X1PRO_3=1"
	[x6_stealth]="VSBM=1 VSBM_181=1 X1STL=1"
)
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT
git -C "$G" log --reverse --first-parent training-mode --format='%H %ct' -- mcconf appconf conf_general.c conf_general.h confgenerator.c \
	hwconf/photon_181.h hwconf/vpro_181.h hwconf/vsbm_181.h > "$O.commits"
mkdir -p "$O"
while read -r c t; do
	rm -rf "$W/src"; mkdir "$W/src"
	git -C "$G" archive "$c" -- '*.h' '*.c' | tar -x -C "$W/src"
	for p in "${!PROD[@]}"; do
		# shellcheck disable=SC2086
		bash "$H/dump_commit.sh" "$W/src" "$O/$c" "$p" $ZERO ${PROD[$p]} > /dev/null 2>"$W/err"
		r=$?
		[ $r -ne 0 ] && [ $r -ne 3 ] && { echo "FAIL $c $p"; tail -3 "$W/err"; }
	done
	echo "done $c $(ls "$O/$c" 2>/dev/null | wc -l) files"
done < "$O.commits"
