import html
S = [
("1. Samarqandga bir fura","jaydari, fura oldida",[
("Hook 1",["(Furaning orqa eshigi yopiladi)",'"Mana, bir fura panelimizni Samarqand viloyatiga chiqarib beryapmiz."']),
("Hook 2",["(Furaning orqa eshigi ochiladi, ichi paddonga to'la)",'"Bitta fura panel. Hozir Samarqandga ketyapti."']),
("Hook 3",["(Fura yonida ikki kishi)",'Abdurahim: "G\'olib aka, shu furada nechta mashinaning puli yotibdi?"','G\'olib aka: "10 ta Cobaltning puli. Hozir Samarqandga ketyapti."']),
("Qiziqtirish",['G\'olib aka: "Ketib qolmang, oxirida Xitoy bor."']),
("Body",['G\'olib aka: "Bu fura LONGi Hi-MO X10 panel bilan to\'la. Samarqandlik ustamiz kecha aloqaga chiqdi, ertalab pulni tashladi, mana, obeddan keyin chiqarib yuboryapmiz. Ertaga panel obyektida bo\'ladi.',"Hammasi sifat nazoratidan o'tgan, kafolati va garantiya qog'ozlari bilan ketyapti.","Shuning uchun ustanovkachilar, qo'rqmasdan katta loyihalarni olavering. 100 tami, bir furami — panel hajmiga Premium Solar kompaniyasi turib beradi.\""]),
("Isbot",['G\'olib aka: "Mana, hujjatlari. Paddonlar Xitoy zavodidan qanday kelgan bo\'lsa, shunday ketyapti."']),
("Xitoy",["(G'olib aka baraban yonida)","XITOY_FULL"]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
("2. Darz ketgan panel","0.5x, jaydari",[
("Hook 1",['"Mana shu singan joyi butun panelni ishdan chiqaradi."']),
("Hook 2",['"Ustanovkachilar, panel olayotganda yaxshilab qarab oling. Mana shu kichkina singan joy ham sizni pulga tushiradi."']),
("Body",['G\'olib aka: "Darz kichkina bo\'lsa ham, panel ishlagan sari kattalashadi. Shu joyi qizib ketadi, panel tokni kam beradi. Panellar bir-biriga ulangani uchun bitta singan panel yonidagilarni ham sekinlashtiradi. Mijoz esa sotuvchini emas, sizni qidiradi."']),
("Isbot",['G\'olib aka: "Shuning uchun bizda har bir panelni yuklashdan oldin ko\'z oldingizda tekshirib beramiz. Paddon Xitoy zavodidan qanday kelgan bo\'lsa, shunday qo\'lingizga tegadi."']),
("CTA 1",['"Ombordagi panellar va narxlarni bilish uchun pastdagi tugmani bosing."']),
("CTA 2",['"Direct\'ga \'Panel\' deb yozing."'])]),
("3. Panel siniq chiqsa, kim javob beradi?","savol → javob → hikoya",[
("Hook",['Abdurahim: "G\'olib aka, panel siniq chiqsa kim javob beradi — sizlarmi yoki ustanovkachimi?"']),
("Javob",['G\'olib aka: "Albatta, biz javob beramiz."']),
("Hikoya",['G\'olib aka: "Bir usta bilan shunaqa voqea bo\'lgan. Bitta stroitel bilan obyekt qilishgan ekan. Panelni o\'rnatib bo\'lgandan keyin bittasi siniq chiqibdi. Stroitel ustani ayblabdi, usta bizga keldi. Tekshirdik — zavoddan shunaqa kelgan ekan. O\'sha kuni yangisiga almashtirib berdik. Bunaqa holatlar o\'zi ko\'p bo\'lib turadi."']),
("Xulosa",['G\'olib aka: "Panel bizdan ketgan bo\'lsa, javobini ham biz beramiz. Usta bir o\'zi qolmaydi."']),
("Xitoy (faqat targetda)",["(G'olib aka baraban yonida)","XITOY_FULL"]),
("CTA (Reels)",['"Ustalar uchun foydali gaplarni o\'tkazib yubormaslik uchun obuna bo\'lib qo\'ying."']),
("CTA (Target)",["CTA1"])]),
("4. Men sizga panel sotmoqchiman","to'g'ridan-to'g'ri sotuv",[
("Hook",['G\'olib aka: "Men sizga quyosh paneli sotmoqchiman. Ustanovkachi bo\'lsangiz yoki solar bilan shug\'ullansangiz, sizga rad etib bo\'lmaydigan taklifim bor."']),
("Body — ekspert uchun TZ",["• Maqsad: usta \"bu yerdan olish menga foydali\" deb o'ylashi kerak.","• Nima haqida: nega Premium Solar'dan olish foydali, o'z so'zlari bilan, xuddi tanish ustaga gapirgandek.","• Albatta aytiladi: panelni Xitoydan o'zimiz olib kelamiz, shuning uchun narx ulgurji; omborda bor; kafolati bor.","• Aytilmaydi: \"eng arzon\", \"eng zo'r\", nasiya, o'rnatish.","• Ohang: jaydari, samimiy, shoshilmasdan. Davomiyligi: 10–15 soniya.","• Oxirgi gap: \"Lekin eng zo'ri bu emas…\" — Xitoy qismiga o'tiladi."]),
("Xitoy",["(G'olib aka baraban yonida)","XITOY_FULL2"]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
("5. Xitoy tekinmi?","2 kishi",[
("Hook 1",['Abdurahim: "G\'olib aka, rostdanmi, mijozlaringizni Xitoyga tekin olib ketyapsizmi?"']),
("Hook 2",['Abdurahim: "G\'olib aka, Xitoyga borib kelish necha pul turadi?"','G\'olib aka: "Bizning mijozlarga — tekin."']),
("Body",['G\'olib aka: "Ha, rost. Dekabr oxirida mijozlarimizni bir haftaga Xitoyga olib ketyapmiz."','Abdurahim: "Borib nima qilinadi?"','G\'olib aka: "LONGi, ERA, Deye zavodlariga kiramiz, panel qanday yasalishini ko\'rasiz. Kechqurun shaharni aylanamiz, dam olamiz."','Abdurahim: "Pulini kim to\'laydi?"','G\'olib aka: "Samolyot, mehmonxona, ovqat — hammasi bizdan. Siz faqat sumkangizni yig\'asiz."']),
("Xitoy",["(G'olib aka baraban yonida)","XITOY_SHORT"]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
("6. Muhim e'lon","0.5x, samimiy",[
("Hook",['G\'olib aka: "Sizga muhim e\'lonim bor."']),
("TZ (ekspert o'zi gapiradi)",["• Mavzu: Xitoy safari e'loni.","• Albatta aytiladi: dekabr oxirida mijozlarimizni Xitoyga tekin olib ketyapmiz; zavodlar va dam olish; samolyot, mehmonxona, ovqat — hammasi bizdan; bitta panel olgan ham barabanga tushadi, omadlilar dekabr oxirida tanlanadi.","• Ohang: do'stiga yangilik aytayotgandek, jilmayib, shoshilmasdan.","• Kadr: telefon 0.5x rejimida, ombor ichida yurib gapiradi, oxirida baraban ko'rinadi.","• Davomiyligi: 20–25 soniya."]),
("CTA 1",["CTA1"]),("CTA 2",["CTA2"])]),
]
R = {
"XITOY_FULL":'"Ha, aytgancha, biz o\'z mijozlarimizni dekabr oyida Xitoyga sayohatga olib ketyapmiz — dam olishga ham, zavodlar bilan tanishishga ham. Bizdan bitta panel olgan bo\'lsangiz ham, ismingizni yozib, shu barabanga tashlaymiz. Dekabr oxirida omadli ishtirokchilarni shu barabandan tanlab olamiz."',
"XITOY_FULL2":'"Biz o\'z mijozlarimizni dekabr oyida Xitoyga sayohatga olib ketyapmiz — dam olishga ham, zavodlar bilan tanishishga ham. Bizdan bitta panel olgan bo\'lsangiz ham, ismingizni yozib, shu barabanga tashlaymiz. Dekabr oxirida omadli ishtirokchilarni shu barabandan tanlab olamiz."',
"XITOY_SHORT":'"Bizdan bitta panel olgan bo\'lsangiz ham, ismingizni yozib, shu barabanga tashlaymiz. Dekabr oxirida omadli ishtirokchilarni shu barabandan tanlab olamiz."',
"CTA1":'"Batafsil ma\'lumot olish uchun pastdagi tugmani bosing, o\'zimiz siz bilan bog\'lanamiz."',
"CTA2":'"Batafsil ma\'lumot uchun Direct\'ga \'Xitoy\' deb yozing."'}
out=['<!doctype html><html lang="uz"><head><meta charset="utf-8"><title>Premium Solar — Target ssenariylar</title><style>@page{size:A4;margin:16mm 14mm}body{font-family:"DejaVu Sans",Arial,sans-serif;color:#1c1c1c;font-size:12pt;line-height:1.5}h1{font-size:20pt;margin:0 0 4px}.sub{color:#666;font-size:10.5pt;margin-bottom:18px}.card{border:1px solid #e3e3e3;border-radius:10px;padding:14px 16px;margin-bottom:16px;page-break-inside:avoid}.card h2{font-size:15pt;margin:0 0 8px}.card h2 span{font-weight:normal;color:#777;font-size:11pt}.lbl{font-weight:bold;color:#b45309;font-size:10pt;text-transform:uppercase;letter-spacing:.4px;margin-top:8px}p{margin:2px 0 5px}.note{color:#777;font-style:italic}</style></head><body><h1>Premium Solar — Target ssenariylar</h1><div class="sub">6 ta ssenariy · 10 ta video (hooklar bo\'yicha) · 18-noyabr 2026</div>']
for t,f,secs in S:
    out.append(f'<div class="card"><h2>{html.escape(t)} <span>({html.escape(f)})</span></h2>')
    for lab,lines in secs:
        out.append(f'<div class="lbl">{html.escape(lab)}</div>')
        for l in lines:
            l=R.get(l,l)
            cls=' class="note"' if l.startswith('(') else ''
            out.append(f'<p{cls}>{html.escape(l)}</p>')
    out.append('</div>')
out.append('</body></html>')
open('target_hammasi.html','w').write('\n'.join(out))
