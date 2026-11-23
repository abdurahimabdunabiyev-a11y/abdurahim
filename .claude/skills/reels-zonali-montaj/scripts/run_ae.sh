#!/bin/bash
# Ishlatish: run_ae.sh <builder.jsx> <log_fayl>
# Builder'ni try/catch ichida ishga tushiradi: xato bo'lsa logga "FATAL ... line N" yoziladi (aks holda log umuman chiqmaydi!)
# Bridge paneli KERAK EMAS (osascript DoScriptFile). Eski aerendercore osilib qolgan bo'lsa AE sekinlashadi — o'ldiriladi.
JSX="$1"; LOG="$2"
pkill -f aerendercore 2>/dev/null
rm -f "$LOG"
W="/tmp/_run_ae_wrap_$$.jsx"
cat > "$W" <<EOF
var out = new File("$LOG");
try { \$.evalFile(new File("$JSX")); }
catch (e) { out.open("w"); out.write("FATAL " + e.toString() + " line " + e.line + " file " + e.fileName); out.close(); }
EOF
(osascript -e "tell application \"${AE_APP:-$(basename "$(ls -d /Applications/Adobe\ After\ Effects\ 20* 2>/dev/null | sort | tail -1)")}\" to DoScriptFile \"$W\"" >/dev/null 2>&1 &)
for i in $(seq 1 120); do sleep 3; [ -f "$LOG" ] && break; done
sleep 3; tr '\r' '\n' < "$LOG"
