// NAMUNA builder (Instagram algoritm reels). Yangi loyiha: base ni o'zgartir, timing.js ni gen_timing.py bilan yarat, sahnalarni qayta yoz.
// Reels: Instagram algoritmi sirlari — ZONALI tuzilma (sahna kompozitsiyalari + CAPTIONS + MAIN)
var base = "~/Movies/ae/reels_algoritm/";
var DUR = 88.65;
$.evalFile(new File(base + "timing.js")); // SENTS, SUBS
$.evalFile(new File("~/.claude/skills/reels-zonali-montaj/lib/lib_zonali.jsx")); // kutubxona (skill ichida)

app.newProject();
proj = app.project;
function imp(n) { return proj.importFile(new ImportOptions(new File(base + n))); }
var FAS = proj.items.addFolder("01 ASSETS"), FSC = proj.items.addFolder("02 SCENES");
var A = {
    bg: imp("assets/white_bg.png"), mosA: imp("assets/mosA.mp4"), mosB: imp("assets/mosB.mp4"),
    brain: imp("br_journal.mp4"), village: imp("br_village.mp4"), notif: imp("br_playroom.mp4"),
    phone: imp("br_wedding.mp4"), watch: imp("stopwatch.jpg"), net: imp("network.jpg"),
    cDost: imp("assets/c_dost.png"), cHam: imp("assets/c_hamkasb.png"), cMij: imp("assets/c_mijoz.png"),
    audio: imp("assets/audio_mix.wav")
};
for (var ak in A) { try { A[ak].parentFolder = FAS; } catch (e) { } }

MAIN = proj.items.addComp("00 MAIN", W, H, 1, DUR, FPS);
MAIN.bgColor = [1, 1, 1];
comp = MAIN; curScene = "MAIN";
var bg = MAIN.layers.add(A.bg); bg.position.setValue([540, 960]); bg.name = "BG oq"; span(bg, 0, DUR);

// ---------------- S1 HOOK ----------------
runScene("S01 hook", 0, 5.0, function () {
    var t0 = 0, t1 = 5.0;
    kicker("instagramda rekka chiqish uchun", 0.15, t1);
    lineA("Videoni", 1.7, t1, { y: 405, size: 104 });
    lineB("oxirigacha", 2.45, t1, { y: 510, size: 104 });
    lineA("ko'rish shartmi?", 3.55, t1, { y: 615, size: 104 });
    clipCard(A.watch, CX, VIS_CY, CARD_W, CARD_H, 40, 0.1, t1, 120, 368, 640);
});
// ---------------- S2 ADASHASIZ ----------------
runScene("S02 adashasiz", 5.0, 6.17, function () {
    var t1 = 6.17;
    kicker("yo'q", 5.2, t1);
    var a = lineB("Adashasiz!", 5.28, t1, { y: 480, size: 170 });
    slamIn(a, 5.28, 100);
    a.position.expression = "wiggle(18, 14*Math.max(0,1-(time-5.28)/0.45))";
    var x1 = shapeRect(500, 70, 35, BLACK, [CX, VIS_CY], 5.4, t1, "X1"); x1.rotation.setValue(45); popIn(x1, 5.4, 100);
    var x2 = shapeRect(500, 70, 35, BLACK, [CX, VIS_CY], 5.5, t1, "X2"); x2.rotation.setValue(-45); popIn(x2, 5.5, 100);
    var rg = ellipseShape(640, null, ORG, 16, [CX, VIS_CY], 5.45, t1); popIn(rg, 5.45, 100);
    R(CX, VIS_CY, 640, 640, 5.4, t1, "V", "X belgisi");
});
// ---------------- S3 MIYA ----------------
runScene("S03 algoritm siri", 6.17, 9.80, function () {
    var t1 = 9.80;
    kicker("instagram rahbari", 6.3, t1);
    lineA("Algoritmning", 6.95, t1);
    lineB("haqiqiy siri", 8.0, t1);
    clipCard(A.brain, CX, VIS_CY, CARD_W, CARD_H, 40, 6.3, t1, 122.2, 360, 600);
});
// ---------------- S4 MOSSERI + HISOBLAGICH ----------------
runScene("S04 mosseri", 9.80, 18.45, function () {
    var t1 = 18.45;
    kicker("adam mosseri  ·  instagram rahbari", 10.2, t1);
    lineA("Yangi profil", 10.4, t1);
    lineB("0", 12.0, t1, {
        fixW: 700,
        expr: "var v=Math.round(ease(time,12.4,16.9,0,1000000));var s=''+v;var o='';var c=0;for(var i=s.length-1;i>=0;i--){o=s.charAt(i)+o;c++;if(c%3==0&&i>0)o=' '+o;}o+(v>=1000000?'+':'')"
    });
    clipCard(A.mosA, CX, VIS_CY, 880, 640, 40, 9.9, t1, 100, 440, 320);
});
// ---------------- S5 BITTA KO'RSATKICH ----------------
runScene("S05 bitta", 18.45, 21.65, function () {
    var t1 = 21.65;
    kicker("faqat", 18.6, t1);
    lineA("Bitta", 19.45, t1);
    lineB("ko'rsatkich", 19.75, t1);
    var rg = ellipseShape(640, null, ORG, 16, [CX, VIS_CY], 18.7, t1); popIn(rg, 18.7, 100);
    gradText("1", { font: F_H, size: 560, pos: [CX, VIS_CY], t0: 18.8, t1: t1, tag: "V", maxW: 520, slam: true });
});
// ---------------- S6 LAYK VA KOMMENT ----------------
runScene("S06 layk komment", 21.65, 25.10, function () {
    var t1 = 25.10;
    kicker("ko'pchilik", 21.8, t1);
    lineA("Layk", 22.5, t1);
    lineB("va komment", 23.3, t1);
    clipCard(A.notif, CX, VIS_CY, CARD_W, CARD_H, 40, 21.75, t1, 122.2, 360, 580);
});
// ---------------- S7 KO'RISH VAQTI ----------------
runScene("S07 korish vaqti", 25.10, 31.05, function () {
    var t1 = 31.05;
    kicker("boshqa platformalarga qaraganda", 25.4, t1);
    var a = lineA("Ko'rish vaqti", 28.5, t1);
    strike(CX - a._w / 2 - 10, CX + a._w / 2 + 10, TA_Y + 4, 14, ORG, 29.45, t1, 0.3);
    lineB("kamroq e'tibor", 29.65, t1);
    clipCard(A.mosB, CX, VIS_CY, 880, 640, 40, 25.2, t1, 100, 440, 320);
});
// ---------------- S8 UCHTA SIGNAL ----------------
runScene("S08 signallar", 31.05, 39.2, function () {
    var t1 = 39.2;
    kicker("instagram tekshiradi", 31.3, t1);
    lineA("3 ta signal", 31.55, t1);
    var rows = [["1", "Originallik", 830, 33.65, false], ["2", "Dolzarblik", 1040, 35.6, false], ["3", "?", 1250, 37.6, true]];
    for (var i = 0; i < rows.length; i++) {
        (function (r) {
            var y = r[2], ts = r[3], dark = r[4];
            var c = shapeRect(880, 180, 40, dark ? BLACK : WHITE, [CX, y], ts, t1, "row");
            shadow(c, 55, 14, 40); popIn(c, ts, 100); fadeIn(c, ts, 0.1);
            var ec = ellipseShape(120, dark ? ORG : BLACK, null, 0, [220, y], ts, t1);
            popIn(ec, ts + 0.05, 100); fadeIn(ec, ts + 0.05, 0.1);
            var nt = mkText(r[0], { font: F_H, size: 78, color: WHITE, pos: [220, y], t0: ts, t1: t1, noReg: true });
            fadeIn(nt, ts + 0.05, 0.1);
            var lt = mkText(r[1], { font: F_H, size: dark ? 120 : 92, color: dark ? WHITE : BLACK, pos: [600, y], t0: ts, t1: t1, maxW: 560, noReg: true });
            popIn(lt, ts + 0.08, 100); fadeIn(lt, ts + 0.08, 0.1);
            if (dark) lt.scale.expression = "s=100+4*Math.sin((time-" + ts + ")*7);[s,s]";
            R(CX, y, 880, 180, ts, t1, "V", "qator " + r[0]);
        })(rows[i]);
    }
});
// ---------------- S9 BEGONA ODAMLAR ----------------
runScene("S09 begona odamlar", 39.2, 48.45, function () {
    var t1 = 48.45;
    kicker("obuna bo'lmaganlar", 39.5, t1);
    lineA("Begona odamlar", 39.7, t1);
    lineB("3-signal", 44.3, t1);
    clipCard(A.net, CX, VIS_CY, 706, 680, 40, 39.3, 45.85, 69, 512, 494, { out: true });
    var c1 = chip("Layk", { pos: [CX, 880], t0: 45.85, t1: t1, size: 110, w: 700, h: 190 });
    var c2 = chip("Prosmotr", { pos: [CX, 1140], t0: 46.1, t1: t1, size: 110, w: 700, h: 190 });
    strike(CX - c1._t._w / 2 - 24, CX + c1._t._w / 2 + 24, 884, 14, ORG, 46.3, t1, 0.25);
    strike(CX - c2._t._w / 2 - 24, CX + c2._t._w / 2 + 24, 1144, 14, ORG, 47.0, t1, 0.25);
});
// ---------------- S10 SENDS PER REACH ----------------
runScene("S10 sends per reach", 48.45, 60.55, function () {
    var t1 = 60.55;
    clipCard(A.phone, CX, VIS_CY, CARD_W, CARD_H, 40, 48.55, t1, 122.2, 360, 540);
    titleBlock({ k: "yangi ko'rsatkich", a: "Sends per", b: "reach", t0: 48.7, at0: 48.8, bt0: 49.3, t1: 52.7, out: true });
    titleBlock({ k: "odamlar videongizni", a: "Samolyotcha", b: "orqali jo'natsa", t0: 52.8, at0: 52.9, bt0: 53.5, t1: 55.9, out: true });
    var pl = plane(YEL, ORG, 150, 52.9, 55.7);
    kf(pl.position, [52.9, 55.6], [[-120, 1150], [1250, 850]], 30, 60);
    kf(pl.rotation, [52.9, 55.6], [-6, -14], 40, 40);
    titleBlock({ k: "algoritm buni", a: "Eng qiziq", b: "kontent", t0: 56.0, at0: 56.05, bt0: 56.4, t1: 58.4, out: true });
    titleBlock({ k: "va uni portlatadi", a: "Yangi", b: "auditoriyaga", t0: 58.5, at0: 58.55, bt0: 58.9, t1: t1 });
    for (var i = 0; i < 2; i++) {
        var ts = 59.55 + i * 0.25;
        var rg = ellipseShape(300, null, YEL, 14, [CX, VIS_CY], ts, 60.5);
        kf(rg.scale, [ts, ts + 0.9], [[20, 20, 100], [420, 420, 100]], 10, 70);
        kf(rg.opacity, [ts, ts + 0.9], [100, 0], 30, 30);
    }
});
// ---------------- S11 SAVOL ----------------
runScene("S11 savol", 60.55, 67.35, function () {
    var t1 = 67.35;
    kicker("xo'sh", 61.2, t1);
    lineA("Nima qilish", 61.35, t1);
    lineB("kerak?", 62.0, t1);
    var q = gradText("?", { font: F_H, size: 480, pos: [CX, 890], t0: 61.4, t1: t1, tag: "V", maxW: 400, slam: true });
    q.scale.expression = "s=100+3*Math.sin((time-61.4)*5);[s,s]";
    var a = chip("Ko'rib ketmasdan", { pos: [CX, 1195], t0: 63.3, t1: t1, size: 70, w: 700, h: 110, maxW: 620 });
    strike(CX - a._t._w / 2 - 20, CX + a._t._w / 2 + 20, 1200, 12, ORG, 63.9, t1, 0.3);
    pill("Do'stiga yuborish", { pos: [CX, 1325], t0: 64.7, t1: t1, bg: BLACK, size: 64, padX: 56, padY: 24 });
});
// ---------------- S12 DO'ST, HAMKASB, MIJOZ ----------------
runScene("S12 hayotiy ogriq", 67.35, 73.3, function () {
    var t1 = 73.3;
    kicker("videongizda", 67.5, t1);
    lineA("Hayotiy", 67.7, t1);
    lineB("og'riqni", 68.2, t1);
    var items = [[A.cDost, 215, "Do'st", 69.0], [A.cHam, 495, "Hamkasb", 69.75], [A.cMij, 775, "Mijoz", 70.5]];
    for (var i = 0; i < 3; i++) {
        var it = items[i];
        var c = comp.layers.add(it[0]); c.startTime = it[3]; c.inPoint = it[3]; c.outPoint = t1;
        c.position.setValue([it[1], 930]); c.scale.setValue(S(c, 70));
        shadow(c, 55, 14, 40); popIn(c, it[3], 70); fadeIn(c, it[3], 0.1);
        R(it[1], 930, 252, 252, it[3], t1, "V", it[2] + " rasm");
        pill(it[2], { pos: [it[1], 1130], t0: it[3] + 0.1, t1: t1, bg: BLACK, size: 48, padX: 30, padY: 18 });
    }
    var pl = plane(YEL, ORG, 100, 71.6, 73.2);
    kf(pl.position, [71.6, 73.15], [[-100, 1290], [1180, 1230]], 30, 60);
});
// ---------------- S13 IQTIBOS KARTA ----------------
runScene("S13 iqtibos", 73.3, 77.98, function () {
    var t1 = 77.98;
    kicker("video oxirida", 73.45, t1);
    lineA("Shunday", 73.6, t1);
    lineB("deb ayting", 74.05, t1);
    var c = shapeRect(880, 600, 48, WHITE, [CX, VIS_CY], 73.5, t1, "quote card");
    shadow(c, 55, 16, 50); popIn(c, 73.5, 100); fadeIn(c, 73.5, 0.1);
    R(CX, VIS_CY, 880, 600, 73.5, t1, "V", "iqtibos karta");
    var q = [["Buni aniq shu", 850, 74.5, BLACK], ["holatdagi", 955, 75.45, BLACK], ["tanishingizga", 1060, 76.05, BLACK], ["yuboring", 1165, 76.75, ORG]];
    for (var i = 0; i < q.length; i++) {
        var l = mkText(q[i][0], { font: F_H, size: 96, color: q[i][3], pos: [CX, q[i][1]], t0: q[i][2], t1: t1, maxW: 760, noReg: true });
        riseIn(l, q[i][2], 30);
    }
    var pl = plane(YEL, ORG, 100, 77.1, 77.98);
    kf(pl.position, [77.1, 77.95], [[260, 1315], [1180, 1290]], 30, 60);
});
// ---------------- S14 PROSMOTR CHIQMAYAPTI ----------------
runScene("S14 yuboring", 77.98, 84.0, function () {
    var t1 = 84.0;
    clipCard(A.village, CX, VIS_CY, CARD_W, CARD_H, 40, 78.1, t1, 122.2, 360, 600);
    kicker("reels olaman, lekin", 78.4, 81.85, true);
    lineA("Prosmotr", 79.4, 81.85, { out: true });
    lineB("chiqmayapti?", 80.0, 81.85, { out: true });
    kicker("shu videoni", 82.0, t1);
    lineA("Yuboring", 82.1, t1);
    lineB("hoziroq", 82.5, t1);
    var pl = plane(YEL, ORG, 140, 82.4, 84.0);
    kf(pl.position, [82.4, 83.95], [[-120, 1150], [1220, 850]], 30, 60);
});
// ---------------- S15 OBUNA ----------------
runScene("S15 obuna", 84.0, DUR, function () {
    var t1 = DUR;
    kicker("marketing bilimlari uchun", 84.1, t1);
    var a = lineA("Obuna", 84.2, t1, { size: 140, y: TA_Y - 5 }); slamIn(a, 84.2, 100);
    var b = lineB("bo'ling!", 84.8, t1, { size: 140, y: TB_Y }); slamIn(b, 84.8, 100);
    var btn = pill("Obuna bo'lish", { pos: [CX, VIS_CY], t0: 86.0, t1: t1, bg: BLACK, size: 70, padX: 70, padY: 36, shadow: true });
    kf(btn.scale, [87.3, 87.42, 87.6, 87.8], [S(btn, 100), S(btn, 90), S(btn, 108), S(btn, 100)], 60, 60);
    var rg = ellipseShape(300, null, ORG, 12, [CX, VIS_CY], 87.4, 88.4);
    kf(rg.scale, [87.4, 88.3], [[30, 30, 100], [330, 330, 100]], 10, 70);
    kf(rg.opacity, [87.4, 88.3], [100, 0], 30, 30);
});

// ---------------- CAPTIONS ----------------
runScene("CAPTIONS", 0, DUR, function () {
    for (var i = 0; i < SUBS.length; i++) {
        var u = SUBS[i];
        var t1 = u.e + 0.04; if (t1 > DUR) t1 = DUR;
        var l = mkText(u.t, { font: F_H, size: 56, color: BLACK, pos: [CX, ZN.capY], t0: u.s, t1: t1, maxW: 700, noReg: true, tag: "CAP" });
        kf(l.scale, [u.s, u.s + 0.12], [S(l, 92), S(l, 100)], 60, 60);
        fadeIn(l, u.s, 0.05);
    }
});

// ---------------- MAIN: o'tish chiziqlari, ovoz, guide ----------------
comp = MAIN; curScene = "MAIN";
var wipes = [9.8, 18.45, 25.1, 31.05, 39.2, 48.45, 60.55, 67.35, 77.98, 84.0];
for (var wi = 0; wi < wipes.length; wi++) {
    var tb = wipes[wi];
    var wp = shapeRect(1300, 1920, 0, (wi % 2 == 0) ? BLACK : ORG, [-760, 960], tb - 0.22, tb + 0.22, "wipe");
    kf(wp.position, [tb - 0.2, tb, tb + 0.2], [[-760, 960], [540, 960], [1840, 960]], 60, 60);
}
// CAPTIONS eng tepada
var capLayer = MAIN.layers.add(proj.items[proj.numItems]); // vaqtincha (pastda to'g'rilanadi)
capLayer.remove();
for (var ii = 1; ii <= proj.numItems; ii++) {
    if (proj.item(ii) instanceof CompItem && proj.item(ii).name == "CAPTIONS") {
        var cl = MAIN.layers.add(proj.item(ii)); cl.startTime = 0; cl.inPoint = 0; cl.outPoint = DUR; cl.name = "CAPTIONS"; cl.moveToBeginning();
    }
}
var au = MAIN.layers.add(A.audio); au.startTime = 0; au.name = "AUDIO ovoz+musiqa"; au.moveToEnd();
addGuide(MAIN, DUR);
try { MAIN.openInViewer(); } catch (e) { }

runChecks();
proj.save(new File(base + "reels_algoritm_v3.aep"));
L("DONE MAIN layers=" + MAIN.numLayers);
var f = new File(base + "build_log3.txt"); f.open("w"); f.write(LOG.join("\n")); f.close();
