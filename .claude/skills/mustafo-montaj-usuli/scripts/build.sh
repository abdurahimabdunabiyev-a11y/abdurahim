#!/bin/bash
# Ishlatish: build.sh LOYIHA_PAPKASI   (papkada cfg.jsx va scenes.jsx bo'lishi kerak)
# cfg.jsx + lib + blocks + scenes.jsx -> build.jsx, AE'da ishga tushiradi, logni chiqaradi.
D="$1"; SK="$HOME/.claude/skills/mustafo-montaj-usuli"
[ -f "$D/cfg.jsx" ] && [ -f "$D/scenes.jsx" ] || { echo "cfg.jsx yoki scenes.jsx topilmadi: $D"; exit 1; }
cat "$D/cfg.jsx" "$SK/lib/mustafo_lib.jsx" "$SK/lib/mustafo_blocks.jsx" "$D/scenes.jsx" > "$D/build.jsx"
"$HOME/.claude/skills/reels-zonali-montaj/scripts/run_ae.sh" "$D/build.jsx" "$D/build_log.txt"
