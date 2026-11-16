#!/bin/bash
# Montaj shriftlari: Google Fonts (OFL, fontsource orqali) + Fontshare (ITF FFL). Fayllar gitga kirmaydi.
D="$(cd "$(dirname "$0")" && pwd)"; W=/tmp/montaj-fonts; PY=~/claude-video-kit/.venv/bin/python
mkdir -p $W/x $W/fs && cd $W
for p in space-grotesk anton bebas-neue manrope inter archivo-black unbounded plus-jakarta-sans bricolage-grotesque syne montserrat oswald instrument-serif instrument-sans hanken-grotesk inter-tight michroma; do
  npm pack @fontsource/$p --silent >/dev/null 2>&1 || true; done
npm pack @fontsource-variable/archivo --silent >/dev/null 2>&1 || true
for t in *.tgz; do mkdir -p x/${t%.tgz}; tar xzf $t -C x/${t%.tgz}; done
$PY "$D/fontsource_ornat.py" $W || true
for f in general-sans satoshi clash-display cabinet-grotesk; do
  curl -sSL -o fs/$f.zip "https://api.fontshare.com/v2/fonts/download/$f" && unzip -qo fs/$f.zip -d fs/$f || true; done
$PY "$D/fontshare_ornat.py" $W || true
fc-cache -f ~/.fonts >/dev/null 2>&1 || true
