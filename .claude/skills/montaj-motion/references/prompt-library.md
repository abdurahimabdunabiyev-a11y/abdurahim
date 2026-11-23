# Promptlar kutubxonasi

Hammasi bitta Claude Code sessiyasida, shu tartibda. [QAVS] ichidagilarni o'zingiznikiga almashtiring.

## 0. Boshlash

**Brif**
> montaj-motion skilli bilan ishla. [BREND] uchun [davomiylik] soniyalik [format] video kerak, maqsad — [lid / tanitish / taqdimot]. Brif shablonini to'ldir. Ma'lumot yetishmasa, avval 3 ta qisqa savol ber.

**Storyboard**
> Brif asosida storyboard yoz: 5 sahna (hook, muammo, yechim, natija, brend + CTA), har birida ekranda nima, harakat, kamera va kadr oralig'i. Kadrlar yig'indisi aniq [jami] bo'lsin. Men tasdiqlamagunimcha animatsiyaga o'tma.

**Aktivlar**
> Storyboard uchun kerakli aktivlar ro'yxatini ber: qaysilari bizda bor (`assets/` papkasini tekshir), qaysilarini yaratish kerak. UI va ikonkalarni SVG sifatida o'zing chiz. Rasm emas, vektor.

## 1. Qurish

> Tasdiqlangan storyboard bo'yicha videoni Remotion'da sahnama-sahna qur. Har sahna alohida komponent, src/lib/motion.ts dagi yordamchilardan foydalan. Avval har sahnadan bittadan still render qil va checklist bo'yicha tekshir.

## 2. Tipik tuzatishlar (birinchi renderdan keyin)

| Muammo | Prompt |
|---|---|
| Elementlar kanvasdan chiqib ketgan | Kanvasni [1920×1080] ga qulfla va hamma narsani chetlardan emas, markazdan joylashtir. |
| Birinchi kadrlarda boshqa shrift | Shriftni birinchi kadrdan oldin to'liq yukla. |
| Raqam bir kadrda sakraydi | [Hisoblagich] sanalishini ~1 soniyaga cho'z: o'qilsin, lekin cho'zilib ketmasin. |
| Kartalar birdaniga chiqadi | [Kartalar]ni birma-bir, 4–6 kadr oraliq bilan chiqar. Har biri to'liq qo'nib bo'lgach belgisi chiqsin. |
| Kamera juda tez | Kamera harakatini sekinlashtir va easy-ease ber: yumshoq boshlanib, yumshoq to'xtasin. |
| Hammasi bir vaqtda harakatlanadi | Kalit kadrlarni 2–4 kadrga siljit, keyingi harakat oldingisi tinchlanmasdan boshlansin. |
| Matn o'qib bo'lmaydi | Bu matnni ekranda kamida 1.5 soniya ushla yoki ikki qismga bo'l. |
| 9:16 da muhim narsa kesilgan | Muhim kontentni markaziy 1080×1080 xavfsiz zonaga ko'chir. |

## 3. Sayqal (polish)

- [Hisoblagich] o'sgan sari unga yumshoq [qizil] glow ber.
- Kursor oynalar orasida ~1 soniya ikkilanib tursin, xuddi nimani ko'chirayotganini unutgandek.
- Har bir [karta] ishlay boshlaganda kichik pulse bersin.
- Belgilarni (✓) hammasini birdaniga emas, ro'yxat bo'ylab kaskad qilib chiqar.
- [Hisoblagich] nolga tushganda kamerani orqaga tort, butun tozalangan maydon ko'rinsin.
- CTA tugmasini oxirgi 1.5 soniyada 2 marta yengil pulse qildir.
- Statik kadrlarga 2% sekin drift qo'sh, hech narsa to'liq qotib qolmasin.
- Fonga juda sekin harakatlanuvchi gradient yoki zarrachalar qo'sh, kontentdan chalg'itmasin.

## 4. Reviziya (mijoz tuzatishi)

> Mijoz [nima o'zgarsin] deyapti. Faqat shu qiymatni o'zgartir va qayta render qil.

Misollar: "narx 2 490 000 emas, 2 190 000", "CTA: Telegram'da yozing", "brend rangini #1A1A2E ga almashtir".

## 5. Render

> Asosiy versiyani [format] da mp4 qilib render qil, musiqa bilan, ovozsiz diktor. Keyin 9:16, 1:1 va 4:5 kesimlarini chiqar. Har kesimdan bittadan still ko'rsat.
