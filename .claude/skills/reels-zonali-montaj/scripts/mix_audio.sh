#!/bin/bash
# Ishlatish: mix_audio.sh <ovoz.mp3> <musiqa.mp3> <chiqish.wav> <davomiylik s>
# Ovoz ustida musiqa sidechain ducking (-14 dB), 0.8 s fade-in, oxirida 3.2 s fade-out, loudnorm -14 LUFS
V="$1"; M="$2"; O="$3"; D="${4:-88.65}"; FO=$(python3 -c "print(max(0,$D-3.25))")
ffmpeg -v error -y -i "$V" -i "$M" -filter_complex "[0:a]aresample=44100,apad=pad_dur=1,atrim=0:$D,asplit=2[v1][v2];[1:a]aresample=44100,atrim=0:$D,asetpts=PTS-STARTPTS,volume=0.20,afade=t=in:d=0.8,afade=t=out:st=$FO:d=3.2[m];[m][v2]sidechaincompress=threshold=0.012:ratio=6:attack=15:release=350:makeup=1[md];[v1][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[mix]" -map "[mix]" -ac 2 -ar 44100 -c:a pcm_s16le "$O"
