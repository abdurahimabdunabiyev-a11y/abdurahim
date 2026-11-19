import html
S = [
("Target kreativ 1 — Samarqandga bir fura","jaydari, fura oldida",[
("Hook 1",["(Furaning orqa eshigi yopiladi)",'"Mana, bir fura panelimizni Samarqand viloyatiga chiqarib beryapmiz."']),
("Hook 2",["(Furaning orqa eshigi ochiladi, ichi paddonga to'la)",'"Bitta fura panel. Hozir Samarqandga ketyapti."']),
("Hook 3",["(Fura yonida ikki kishi)",'Abdurahim: "G\'olib aka, shu furada nechta mashinaning puli yotibdi?"','G\'olib aka: "10 ta Cobaltning puli. Hozir Samarqandga ketyapti."']),
("Qiziqtirish",['G\'olib aka: "Ketib qolmang, oxirida Xitoy bor."']),
("Body",['G\'olib aka: "Bu fura LONGi Hi-MO X10 panel bilan to\'la. Samarqandlik ustamiz kecha aloqaga chiqdi, ertalab pulni tashladi, mana, obeddan keyin chiqarib yuboryapmiz. Ertaga panel obyektida bo\'ladi.',"Hammasi sifat nazoratidan o'tgan, kafolati va garantiya qog'ozlari bilan ketyapti.","Shuning uchun ustanovkachilar, qo'rqmasdan katta loyihalarni olavering. 100 tami, bir furami — panel hajmiga Premium Solar kompaniyasi turib beradi.\""]),
("Isbot",['G\'olib aka: "Mana, hujjatlari. Paddonlar Xitoy zavodidan qanday kelgan bo\'lsa, shunday ketyapti."']),
("Xitoy",["(G'olib aka baraban yonida)","XITOY_FULL"]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
("Target kreativ 2 — Darz ketgan panel","0.5x, jaydari",[
("Hook 1",['"Mana shu singan joyi butun panelni ishdan chiqaradi."']),
("Hook 2",['"Ustanovkachilar, panel olayotganda yaxshilab qarab oling. Mana shu kichkina singan joy ham sizni pulga tushiradi."']),
("Body",['G\'olib aka: "Darz kichkina bo\'lsa ham, panel ishlagan sari kattalashadi. Shu joyi qizib ketadi, panel tokni kam beradi. Panellar bir-biriga ulangani uchun bitta singan panel yonidagilarni ham sekinlashtiradi. Mijoz esa sotuvchini emas, sizni qidiradi."']),
("Isbot",['G\'olib aka: "Shuning uchun bizda har bir panelni yuklashdan oldin ko\'z oldingizda tekshirib beramiz. Paddon Xitoy zavodidan qanday kelgan bo\'lsa, shunday qo\'lingizga tegadi."']),
("CTA 1",['"Ombordagi panellar va narxlarni bilish uchun pastdagi tugmani bosing."']),
("CTA 2",['"Direct\'ga \'Panel\' deb yozing."'])]),
("Target kreativ 3 — Panel siniq chiqsa, kim javob beradi?","savol → javob → hikoya",[
("Hook",['Abdurahim: "G\'olib aka, panel siniq chiqsa kim javob beradi — sizlarmi yoki ustanovkachimi?"']),
("Javob",['G\'olib aka: "Albatta, biz javob beramiz."']),
("Hikoya",['G\'olib aka: "Bir usta bilan shunaqa voqea bo\'lgan. Bitta stroitel bilan obyekt qilishgan ekan. Panelni o\'rnatib bo\'lgandan keyin bittasi siniq chiqibdi. Stroitel ustani ayblabdi, usta bizga keldi. Tekshirdik — zavoddan shunaqa kelgan ekan. O\'sha kuni yangisiga almashtirib berdik. Bunaqa holatlar o\'zi ko\'p bo\'lib turadi."']),
("Xulosa",['G\'olib aka: "Panel bizdan ketgan bo\'lsa, javobini ham biz beramiz. Usta bir o\'zi qolmaydi."']),
("Xitoy (faqat targetda)",["(G'olib aka baraban yonida)","XITOY_FULL"]),
("CTA (Reels)",['"Ustalar uchun foydali gaplarni o\'tkazib yubormaslik uchun obuna bo\'lib qo\'ying."']),
("CTA (Target)",["CTA1"])]),
("Target kreativ 4 — Men sizga panel sotmoqchiman","to'g'ridan-to'g'ri sotuv",[
("Hook",['G\'olib aka: "Men sizga quyosh paneli sotmoqchiman. Ustanovkachi bo\'lsangiz yoki solar bilan shug\'ullansangiz, sizga rad etib bo\'lmaydigan taklifim bor."']),
("Body — ekspert uchun TZ",["• Maqsad: usta \"bu yerdan olish menga foydali\" deb o'ylashi kerak.","• Nima haqida: nega Premium Solar'dan olish foydali, o'z so'zlari bilan, xuddi tanish ustaga gapirgandek.","• Albatta aytiladi: panelni Xitoydan o'zimiz olib kelamiz, shuning uchun narx ulgurji; omborda bor; kafolati bor.","• Aytilmaydi: \"eng arzon\", \"eng zo'r\", nasiya, o'rnatish.","• Ohang: jaydari, samimiy, shoshilmasdan. Davomiyligi: 10–15 soniya.","• Oxirgi gap: \"Lekin eng zo'ri bu emas…\" — Xitoy qismiga o'tiladi."]),
("Xitoy",["(G'olib aka baraban yonida)","XITOY_FULL2"]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
("Target kreativ 5 — Xitoy tekinmi?","2 kishi",[
("Hook 1",['Abdurahim: "G\'olib aka, rostdanmi, mijozlaringizni Xitoyga tekin olib ketyapsizmi?"']),
("Hook 2",['Abdurahim: "G\'olib aka, Xitoyga borib kelish necha pul turadi?"','G\'olib aka: "Bizning mijozlarga — tekin."']),
("Body",['G\'olib aka: "Ha, rost. Dekabr oxirida mijozlarimizni bir haftaga Xitoyga olib ketyapmiz."','Abdurahim: "Borib nima qilinadi?"','G\'olib aka: "LONGi, ERA, Deye zavodlariga kiramiz, panel qanday yasalishini ko\'rasiz. Kechqurun shaharni aylanamiz, dam olamiz."','Abdurahim: "Pulini kim to\'laydi?"','G\'olib aka: "Samolyot, mehmonxona, ovqat — hammasi bizdan. Siz faqat sumkangizni yig\'asiz."']),
("Xitoy",["(G'olib aka baraban yonida)","XITOY_SHORT"]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
("Target kreativ 6 — Muhim e'lon","0.5x, samimiy",[
("Hook",['G\'olib aka: "Sizga muhim e\'lonim bor."']),
("TZ (ekspert o'zi gapiradi)",["• Mavzu: Xitoy safari e'loni.","• Albatta aytiladi: dekabr oxirida mijozlarimizni Xitoyga tekin olib ketyapmiz; zavodlar va dam olish; samolyot, mehmonxona, ovqat — hammasi bizdan; bitta panel olgan ham barabanga tushadi, omadlilar dekabr oxirida tanlanadi.","• Ohang: do'stiga yangilik aytayotgandek, jilmayib, shoshilmasdan.","• Kadr: telefon 0.5x rejimida, ombor ichida yurib gapiradi, oxirida baraban ko'rinadi.","• Davomiyligi: 20–25 soniya."]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
("Reels 1 — 2000 dollar","2 kishi, ombor oldida",[
("Hook 1",['Abdurahim: "Aka, rostdanmi? Mijozlarga 2000 dollardan bervormoqchimisiz?!"']),
("Hook 2",["(Ekranda katta yozuv: \"XITOYGA 5 TA SAFAR SOVG'A\")",'Abdurahim: "G\'olib aka, rostdanmi, mijozlarga 2000 dollar tarqatyapsizmi?"']),
("Body",['G\'olib aka: "Sal noto\'g\'ri eshitibsiz. Undan ancha qimmat narsa beryapmiz."','Abdurahim: "2000 dollardan qimmat? Nima ekan u, aka?"',"(G'olib aka stolga pasport va chipta qo'yadi)",'G\'olib aka: "Xitoy. 5 ta mijozimizni Xitoyga olib ketyapmiz. Tekinga."','Abdurahim: "Dam olishgami?"','G\'olib aka: "Dam olish ham bor. Lekin asosiysi — LONGi, ERA, Deye zavodlari. Samolyot, mehmonxona, ovqat, 7 kun — hammasi bizdan."','Abdurahim: "Qanday qilib boriladi?"','G\'olib aka: "Premium Solar\'dan bitta panel olsangiz ham — ismingiz mana shu barabanga tushadi."']),
("CTA 1",['"Baraban qachon aylanadi, kim Xitoyga ketadi — hammasini shu sahifada ko\'rsatamiz. O\'tkazib yubormaslik uchun obuna bo\'lib qo\'ying."']),
("CTA 2",['"Quyosh paneli bilan shug\'ullanadigan o\'rtog\'ingiz bo\'lsa, shu videoni unga tashlab qo\'ying. Kim biladi, siz bahona u Xitoyga dam olgani ketar."'])]),
("Reels 2 — Nechta Cobalt","2 kishi, ombor hovlisi, orqada palletlar",[
("Hook 1",['Abdurahim: "G\'olib aka, orqamizda nechta Cobaltning puli turibdi?"']),
("Hook 2",['Abdurahim: "G\'olib aka, shu omborda qancha pul turibdi?"']),
("Body",['G\'olib aka: "Mana shu palletlarning narxini qo\'shsak, 30 ta Cobalt chiqadi."','Abdurahim: "30 ta?! Shuncha panelni kim oladi?"','G\'olib aka: "Ustalar. Bir oyda hammasi ketadi."','Abdurahim: "Nega aynan sizdan?"','G\'olib aka: "Panel bozorga yetguncha 2–3 qo\'ldan o\'tadi. Har biri o\'z foydasini qo\'shadi. Biz to\'g\'ri Xitoy zavodidan olib kelamiz."','G\'olib aka: "Ustaga farqi — bitta furada 30 million so\'m."','Abdurahim: "Shunaqa ekanda…"']),
("CTA 1",['"Har kuni ombordan shunaqa narsalarni ko\'rsatamiz. Obuna bo\'lib qo\'ying."']),
("CTA 2",['"Usta o\'rtog\'ingiz bo\'lsa, unga tashlab qo\'ying."'])]),
("Reels 3 — Bularni kim olib kiradi?","tez montaj: shahar tomlari → ombor → fura",[
("Hook 1",["(Tez-tez almashadigan kadrlar: shahardagi tomlarda panellar)",'Abdurahim: "Hozir har qadamda quyosh paneli. Bularni O\'zbekistonga kim olib kiradi?"']),
("Hook 2",["(Kadrda tomdagi panel)",'Abdurahim: "Tomingizdagi panel qayerdan kelganini bilasizmi?"']),
("Body",["(Fura eshigi ochiladi, ichidan G'olib aka chiqadi)",'G\'olib aka: "Biz."','Abdurahim: "Qayerdan?"','G\'olib aka: "Xitoydan. O\'zbekistondagi panellarning deyarli hammasi Xitoy zavodlarida yasaladi. Zavoddan chiqadi, furaga yuklanadi, keyin mana shu omborga keladi."','Abdurahim: "Keyin-chi?"','G\'olib aka: "Keyin ustalar olib ketadi. Bugun omborda turgan panel ertaga kimningdir tomida svet beradi."','Abdurahim: "Demak, shahardagi panellarning bir qismi shu yerdan o\'tgan?"','G\'olib aka: "Shunaqa."']),
("CTA 1",['"Panel qayerdan kelib, qayerga ketishini shu sahifada ko\'rsatib boramiz. Obuna bo\'lib qo\'ying."']),
("CTA 2",['"Usta o\'rtog\'ingiz bo\'lsa, unga tashlab qo\'ying."'])]),
("Reels 4 — Usta oyiga qancha topadi?","intervyu, obyektda",[
("Hook 1",['Abdurahim: "Usta aka, panel o\'rnatib oyiga qancha topasiz?"']),
("Hook 2",["(Usta tomda panel ko'tarib turibdi)",'Abdurahim: "Bu kasb bilan oyiga necha pul topsa bo\'ladi? To\'g\'ridan-to\'g\'ri so\'raymiz."']),
("Body",['Usta: "Yaxshi oyda 15–20 million chiqadi."','Abdurahim: "Bunga qanday kelgansiz?"','Usta: "Oldin elektrik edim. 3 yil oldin birinchi panelni o\'rnatdim. Hozir haftasiga 2–3 ta obyekt qilaman."','Abdurahim: "Eng qiyin joyi nima?"','Usta: "Yozda tom qizib ketadi, qishda sovuq. Yana bitta narsa — panelni ishonchli joydan olish. Brak chiqsa, o\'zingiz javob berasiz."','Abdurahim: "Panelni qayerdan olasiz?"','Usta: "Premium Solar\'dan. Xitoydan o\'zlari olib keladi, kafolati bor."','Abdurahim: "Yoshlarga nima deysiz, shu kasbga kirsinmi?"','Usta: "Qo\'li ishlaydigan, tomdan qo\'rqmaydigan bo\'lsa — kirsin. Ish ko\'p."']),
("CTA 1",['"Ustalar hayotidan shunaqa suhbatlarni shu sahifada ko\'rsatamiz. Obuna bo\'lib qo\'ying."']),
("CTA 2",['"Bu kasb kimga kerak bo\'lsa, unga tashlab qo\'ying."'])]),

]
R = {
"XITOY_FULL":'"Ha, aytgancha, biz o\'z mijozlarimizni dekabr oyida Xitoyga sayohatga olib ketyapmiz — dam olishga ham, zavodlar bilan tanishishga ham. Bizdan bitta panel olgan bo\'lsangiz ham, ismingizni yozib, shu barabanga tashlaymiz. Dekabr oxirida omadli ishtirokchilarni shu barabandan tanlab olamiz."',
"XITOY_FULL2":'"Biz o\'z mijozlarimizni dekabr oyida Xitoyga sayohatga olib ketyapmiz — dam olishga ham, zavodlar bilan tanishishga ham. Bizdan bitta panel olgan bo\'lsangiz ham, ismingizni yozib, shu barabanga tashlaymiz. Dekabr oxirida omadli ishtirokchilarni shu barabandan tanlab olamiz."',
"XITOY_SHORT":'"Bizdan bitta panel olgan bo\'lsangiz ham, ismingizni yozib, shu barabanga tashlaymiz. Dekabr oxirida omadli ishtirokchilarni shu barabandan tanlab olamiz."',
"CTA1":'"Batafsil ma\'lumot olish uchun pastdagi tugmani bosing, o\'zimiz siz bilan bog\'lanamiz."',
"CTA2":'"Batafsil ma\'lumot uchun Direct\'ga \'Xitoy\' deb yozing."'}
out=['<!doctype html><html lang="uz"><head><meta charset="utf-8"><title>Premium Solar — Target ssenariylar</title><style>@page{size:A4;margin:18mm 16mm}body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1c1c1c;font-size:14pt;line-height:1.55;margin:0}h1{font-size:22pt;margin:0 0 4px}.sub{color:#666;font-size:12pt;margin-bottom:20px}.card{border-top:2px solid #e5e5e5;padding:14px 0 6px;margin-bottom:10px}.card h2{font-size:17pt;margin:0 0 6px}.card h2 small{display:block;font-weight:normal;color:#777;font-size:12pt;margin-top:2px}.lbl{font-weight:bold;color:#b45309;font-size:11.5pt;text-transform:uppercase;letter-spacing:.4px;margin-top:12px}p{margin:3px 0 6px}.note{color:#777;font-style:italic}</style></head><body><h1>Premium Solar — Syomka ssenariylari</h1><div class="sub">Target: 6 ta kreativ · Reels: 4 ta · 19-noyabr 2026</div>']
for t,f,secs in S:
    out.append(f'<div class="card"><h2>{html.escape(t)}<small>{html.escape(f)}</small></h2>')
    for lab,lines in secs:
        out.append(f'<div class="lbl">{html.escape(lab)}</div>')
        for l in lines:
            l=R.get(l,l)
            cls=' class="note"' if l.startswith('(') else ''
            out.append(f'<p{cls}>{html.escape(l)}</p>')
    out.append('</div>')
out.append('</body></html>')
open('syomka_hammasi.html','w').write('\n'.join(out))
