import json, sys
from faster_whisper import WhisperModel

audio, out = sys.argv[1], sys.argv[2]
model = WhisperModel("medium", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio, language="uz", word_timestamps=True, vad_filter=True)
words = []
for seg in segments:
    for w in seg.words:
        words.append({"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)})
json.dump(words, open(out, "w"), ensure_ascii=False, indent=1)
print(len(words), "words")
print(" ".join(w["w"] for w in words))
