#!/bin/bash
cd "$(dirname "$0")"; B=~/blender-off/blender-4.2.3-linux-x64/blender
for v in oltin oq quyosh; do mkdir -p frames_$v; $B -b -P sahna.py -- --anim --variant $v --out frames_$v/f_#### --samples 14 --foiz 67 > anim_$v.log 2>&1; echo "$v: $(ls frames_$v | wc -l)"; done
