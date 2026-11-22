#!/bin/bash
cd "$(dirname "$0")"; B=~/blender-off/blender-4.2.3-linux-x64/blender
for v in oq quyosh; do mkdir -p frames_$v; $B -b -P sahna.py -- --anim --variant $v --out frames_$v/f_#### --samples 14 --foiz 67 >> anim_$v.log 2>&1; done
echo TUGADI > render_rest.done
