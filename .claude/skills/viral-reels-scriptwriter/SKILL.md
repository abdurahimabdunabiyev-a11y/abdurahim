---
name: viral-reels-scriptwriter
description: Write high-retention 8-block viral video scripts in Uzbek for Instagram Reels, TikTok, and YouTube Shorts, along with ElevenLabs-optimized voiceover text. Use when the user asks to write, edit, translate, or adapt a video script, scenario (senariy), or ElevenLabs voiceover prompt from any topic, text, image, or video.
---
# Viral Reels Scriptwriter

This skill transforms any topic, raw idea, image, or reference video into a high-retention Uzbek short-form video script using the 8-block viral structure and prepares a phonetic ElevenLabs voiceover script.

## When to Use

- The user asks for a video script or scenario ("senariy yozib ber", "video qilish kerak", "edit qil", "tarjima qilib senariy yoz").
- The user uploads a video, image, or draft text and wants it turned into a viral Instagram Reel, TikTok, or YouTube Short.
- The user asks to prepare or adapt a script for ElevenLabs voice generation ("elevenlabs uchun prompt yozib ber", "ovoz qilishim uchun moslab ber").

## Steps

### 1. Analyze the Source Material and Angle

- Extract the core message, facts, and target audience from the user's prompt, uploaded video, or images.
- When adapting an existing video of the user or client speaking, stay faithful to the actual facts and meaning in the video while removing filler words and hesitation.
- Identify the strongest hook and the primary emotion or curiosity trigger that will make viewers share ("Sends per reach") and subscribe.

### 2. Draft the 8-Block Viral Script

Structure the script into 8 distinct retention blocks so viewers stay until the end:

1. **Hook (0-3 sec):** Stop the scroll immediately with a bold question, counter-intuitive claim, or visual shock. Never waste the first seconds on greetings or asking for likes.
2. **Lead (3-10 sec):** Hold the viewer past the 10-second mark by promising a clear payoff, insider secret, or quick proof.
3. **Body 1 (First Value Block):** Deliver the first concrete fact, problem explanation, or visual demonstration in simple, spoken Uzbek.
4. **Open Loop 1 (First Curiosity Bridge):** Insert a short suspenseful transition sentence (e.g., "Lekin eng qizig'i hali oldinda..." or "Xo'sh, unda nega...?") that opens a new question in the viewer's mind.
5. **Body 2 (Second Value Block):** Reveal the deeper mechanism, psychological trick, or business insight with a relatable example.
6. **Open Loop 2 (Second Curiosity Bridge):** Create a second micro-cliffhanger leading into the final solution or actionable takeaway (e.g., "Xo'sh, buni o'z ishimizda qanday qo'llash mumkin?").
7. **Body 3 (Third Value Block / Solution):** Provide the clear, practical solution, rule, or brand offer so the viewer gets an "Aha!" moment.
8. **CTA (Call to Action):** Prompt the viewer to share the video with a specific friend ("shu holatdagi tanishingizga yuboring") and subscribe to the page ("shunday foydali ma'lumotlar uchun obuna bo'ling"), or use a comment keyword lead magnet if requested.

### 3. Generate the ElevenLabs Voiceover Version

Provide a ready-to-paste ElevenLabs Text-to-Speech block that prevents pronunciation errors in Uzbek:

- Insert pacing and emotion tags in square brackets: `[excited]`, `[pause]`, `[slowly]`, `[softly]`.
- Write emphasized words in `ALL CAPS` so the voice model stresses key points.
- Write all numbers out in Uzbek words (for example, write `o'n besh ming` instead of `15 000`) so ElevenLabs does not read digits in English.
- Transliterate all English, Russian, and international loanwords or brand names into **Cyrillic** wrapped in quotes (for example: `«Инстаграм»`, `«алгоритм»`, `«маркетинг»`, `«бизнес»`, `«Эппл»`, `«Старбакс»`, `«просмотр»`, `«профилимга»`) so the voice model pronounces them smoothly without accent glitches.

## Gotchas

- Avoid putting long intros or "obuna bo'ling" in the first 5 seconds unless specifically requested; the Hook must immediately address the viewer's pain point or curiosity.
- Never leave raw digits (`10`, `2026`, `50%`) or Latin-spelled English brands (`Apple`, `Instagram`, `ChatGPT`) inside the ElevenLabs block, as multilingual TTS models often mispronounce them when reading Uzbek text.
- Match the script length to the user's target duration (typically 110-130 words for a 45-55 second Reel).
