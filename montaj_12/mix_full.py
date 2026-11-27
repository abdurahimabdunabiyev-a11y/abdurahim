import subprocess, os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, '.')
P = json.load(open('plan.json')); TOTAL = P['total']; ph = P['phrases']
T = '../montaj_08_tanlov/sfx/'; POP = '../montaj_11/pop-2359.mp3'
S = []
# B-roll/karta kirishida juda yengil whoosh (har ikkinchisida, ortiqcha bo'lmasin)
k = 0
for i, p in enumerate(ph):
    if p['kind'] in ('broll', 'card') and i > 0 and ph[i - 1]['kind'] not in ('broll', 'card'):
        S.append((T + 'm1491.mp3', p['t0'] - .12, -30)); k += 1
# katta raqam / karta paydo bo'lganda yumshoq pop
for t in (ph[4]['words'][2][1], ph[5]['words'][3][1], ph[7]['t0'] + .3, ph[7]['words'][4][1], ph[8]['words'][8][1] - .2, ph[18]['words'][2][1] - .1,
          ph[21]['words'][2][1], ph[21]['words'][8][1], ph[26]['t0'] + .05):
    S.append((POP, t, -29))
S.append((T + 'impact-2182.mp3', ph[1]['t0'], -27))
ins, fl = [], []
for j, (f, t, db) in enumerate(S):
    ins += ['-i', f]; ms = max(0, int(t * 1000)); fl.append(f'[{j+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{j}]')
n = len(S)
fc = (f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo[vo];[1:a]apad,atrim=start=0:duration={TOTAL},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
      f"volume=-17dB,afade=t=in:d=0.6,afade=t=out:st=99.0:d=2.0[mu];"
      + ';'.join(fl) + ';' + ''.join(f'[s{j}]' for j in range(n)) + f'amix=inputs={n}:normalize=0[fx];'
      f"[vo]asplit[a][b];[mu][b]sidechaincompress=threshold=0.03:ratio=5:attack=15:release=350[md];[a][md][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5,atrim=duration={TOTAL}[x]")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'ovoz_full.wav', '-i', os.path.expanduser('~/montaj-musiqa/mixkit_music_175.mp3')] + ins + ['-filter_complex', fc, '-map', '[x]', '-ar', '48000', 'mix_full.wav'], check=True)
print('OK', n, 'SFX')
