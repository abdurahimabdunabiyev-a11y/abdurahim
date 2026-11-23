#!/bin/bash
# Ishlatish: render.sh <loyiha.aep> <kompozitsiya nomi> <chiqish.mp4>   (AE 2026, H.264 15 Mbps, MAIN ichidagi ovoz AAC bilan)
# aerender'ni log bilan orqa fonda ishga tushiradi va "Finished" gacha kutadi. Fayl o'smay qolsa (qotib qolgan) — qayta ishga tushir.
AER="${AERENDER:-$(ls -d /Applications/Adobe\ After\ Effects*/aerender 2>/dev/null | sort | tail -1)}"  # AE versiyasi avtomatik topiladi
pkill -f aerendercore 2>/dev/null; pkill -f aerender 2>/dev/null; sleep 2; rm -f "$3"
LOGF="${3%.mp4}.render.log"
(nohup "$AER" -project "$1" -comp "$2" -RStemplate "Best Settings" -OMtemplate "H.264 - Match Render Settings - 15 Mbps" -output "$3" > "$LOGF" 2>&1 &)
for i in $(seq 1 160); do sleep 3; grep -q "Finished composition" "$LOGF" && break; done
sleep 4; grep -E "rror|Unable" "$LOGF" | head -3; ffprobe -v error -show_entries format=duration -of csv=p=0 "$3"
