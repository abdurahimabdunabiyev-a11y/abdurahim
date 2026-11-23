// NAMUNA: '1 soatda 100$' montaji (v4). Yangi loyihada shuni nusxalab sahnalarni o'zgartiring.
// Kerak: data.js (DATA.CAPS subtitrlar), data2.js (D2.KB kesish vaqtlari, D2.Z zoom), logos/k/*.png, face.js

// ============ "1 soatda 100$" — Mustafo uslubidagi AE montaj namunasi ============
// qora fon + to'q sariq nur, HelveticaNeue, yupqa chegarali kartalar, tepada grafik panel, pastda yuzni kuzatuvchi video karta
$.evalFile(new File(base + "data.js"));    // DATA.CAPS: subtitr chunklari [t0,t1,matn,aksent]
$.evalFile(new File(base + "data2.js"));   // D2.KB: kesish vaqtlari, D2.Z: zoom egri chizig'i
var KB = D2.KB;

// ================= S1: HOOK (yuz kartasi) =================
runScene("S01 hook", 0, KB[1], function () {
    var t1 = KB[1];
    base2(0, t1, [[0, t1, "face"]]);
    tileLogo("claude", 300, 352, 146, 0.10, t1); plus2(420, 352, 0.22, t1);
    tileLogo("higgs", 540, 352, 146, 0.32, t1); plus2(660, 352, 0.44, t1);
    tileLogo("meta", 780, 352, 146, 0.54, t1);
    tx("1 soatda", CX, 482, 50, MUTE, 1.35, t1, { font: LIGHT, rise: true });
    money(CX, 612, 170, 1.76, 0.95, t1, 100, "$");
    var ul = rr(170, 8, 4, ACC, null, 100, 0, [CX, 726], 2.7, t1, "chiziq"); kf(ul.scale, [2.7, 3.05], [[0, 100, 100], [100, 100, 100]], 20, 70);
});

// ================= S2: 1-qadam =================
runScene("S02 rasmlar", KB[1], KB[2], function () {
    var t0 = KB[1], t1 = KB[2];
    base2(t0, t1, [[t0, t1, "broll", 760]]);
    stepTag(1, t0 + 0.1, t1);
    panelTitle("Mijozdan mahsulot rasmlari", t0, t1);
    for (var i = 0; i < 3; i++) {
        var x = 340 + i * 200, ta = t0 + 0.5 + i * 0.2;
        var tl = rr(176, 176, 38, CARDF2, [1, 1, 1], 16, 2, [x, 590], ta, t1, "rasm"); fadeIn(tl, ta, 0.2);
        kf(tl.scale, [ta, ta + 0.4], [[86, 86, 100], [100, 100, 100]], 80, 55);
        photoIcon(x, 590, 1.1, ta + 0.1, t1);
        var ck = oval(54, ACC, null, 100, 0, [x + 64, 515], t0 + 2.2 + i * 0.12, t1, "belgi"); popIn(ck, t0 + 2.2 + i * 0.12, 100); fadeIn(ck, t0 + 2.2 + i * 0.12, 0.1);
        iCheck(x + 64, 515, 0.5, [1, 1, 1], t0 + 2.25 + i * 0.12, t1);
    }
});

// ================= S3: 2-qadam (rasm -> Claude -> Higgsfield) =================
runScene("S03 generatsiya", KB[2], KB[3], function () {
    var t0 = KB[2], t1 = KB[3];
    base2(t0, t1, [[t0, t1, "broll", 860]]);
    stepTag(2, t0 + 0.1, t1);
    panelTitle("Rasmdan video generatsiya", t0, t1);
    flowPath("yolB", 6.9, t1, 7.0, 10.0);
    node(function (x, y) { photoIcon(x, y, 1.0, t0 + 0.35, t1); }, "rasmlar", 225, 665, t0 + 0.3, t1, false);
    var nh = node(function (x, y) { sparkW(x, y, 100, 7.7, t1); }, "Claude", 540, 505, 7.6, t1, true);
    node(function (x, y) { tileLogo("higgs", x, y, 112, 9.0, t1); }, "Higgsfield", 855, 665, 8.9, t1, false);
    var ck = oval(70, [1, 1, 1], null, 100, 0, [925, 580], 10.3, t1, "belgi"); popIn(ck, 10.3, 100); fadeIn(ck, 10.3, 0.1);
    iCheck(925, 580, 1.15, [0.1, 0.07, 0.05], 10.35, t1);
});

// ================= S4: 3-qadam (Claude montaj qiladi) =================
runScene("S04 montaj", KB[3], KB[4], function () {
    var t0 = KB[3], t1 = KB[4];
    base2(t0, t1, [[t0, t1, "broll", 900]]);
    stepTag(3, t0 + 0.1, t1);
    panelTitle("Claude o'zi montaj qiladi", t0, t1);
    var cm = claudeMark(CX, 612, 160, t0 + 0.4, t1);
    var ring = oval(272, null, ACC, 100, 4, [CX, 612], t0 + 0.5, t1, "halqa"); ring.rotation.setValue(-90);
    try { var tr = ring.property("ADBE Root Vectors Group").addProperty("ADBE Vector Filter - Trim"); kf(tr.property("ADBE Vector Trim End"), [t0 + 0.55, t0 + 1.7], [0, 100], 25, 60); } catch (e) { }
    var names = ["kesish", "subtitr", "effekt", "musiqa"];
    for (var i = 0; i < names.length; i++) orbitChip(names[i], i, names.length, CX, 630, 360, 120, t0 + 0.9, t1, 0.9);
});

// ================= S5: 4-qadam (Meta Ads) =================
runScene("S05 reklama", KB[4], KB[5], function () {
    var t0 = KB[4], t1 = KB[5];
    base2(t0, t1, [[t0, t1, "broll", 950]]);
    stepTag(4, t0 + 0.1, t1);
    panelTitle("Meta Ads'da reklama yoqamiz", t0, t1);
    flowPath("yolC", 15.5, t1, 15.6, 18.7);
    node(function (x, y) { iUp(x, y, 1.1, TXT, 15.2, t1); }, "video", 225, 665, 15.1, t1, false);
    node(function (x, y) { tileLogo("meta", x, y, 116, 17.0, t1); }, "Meta Ads", 540, 505, 16.9, t1, false);
    radial(540, 505, 330, ACC, 40, 17.0, t1);
    node(function (x, y) {
        oval(34, null, TXT, 100, 6, [x, y - 26], 18.5, t1, "bosh"); var b = rr(72, 40, 20, null, TXT, 100, 6, [x, y + 28], 18.5, t1, "tana");
    }, "mijozlar", 855, 665, 18.4, t1, true);
});

// ================= S6: 5-qadam (sotuvlar) =================
runScene("S06 sotuvlar", KB[5], KB[6], function () {
    var t0 = KB[5], t1 = KB[6];
    base2(t0, t1, [[t0, t1, "broll", 950]]);
    stepTag(5, t0 + 0.1, t1);
    panelTitle("Sotuvlar kela boshlaydi", t0, t1);
    var hs = [70, 110, 150, 195, 245, 300];
    for (var i = 0; i < hs.length; i++) {
        var x = 215 + i * 122, ta = t0 + 0.4 + i * 0.26;
        var ctrl = comp.layers.addNull(); ctrl.name = "ustun"; ctrl.anchorPoint.setValue([0, 0]); ctrl.position.setValue([x, 800]); span(ctrl, ta, t1);
        var last = (i == hs.length - 1);
        var br = rr(84, hs[i], 22, last ? ACC2 : CARDF2, last ? null : [1, 1, 1], 16, 2, [0, 0], ta, t1, "ustun"); br.parent = ctrl; br.position.setValue([0, -hs[i] / 2]);
        kf(ctrl.scale, [ta, ta + 0.5], [[100, 0, 100], [100, 100, 100]], 85, 50);
    }
    var ck = oval(70, [1, 1, 1], null, 100, 0, [215 + 5 * 122, 800 - 300 - 52], t0 + 2.2, t1, "belgi"); popIn(ck, t0 + 2.2, 100); fadeIn(ck, t0 + 2.2, 0.1);
    iUp(215 + 5 * 122, 800 - 300 - 52, 0.75, [0.1, 0.07, 0.05], t0 + 2.25, t1);
});

// ================= S7: 6-qadam (to'lov: $100) =================
runScene("S07 tolov", KB[6], KB[7], function () {
    var t0 = KB[6], t1 = KB[7];
    base2(t0, t1, [[t0, 24.2, "broll", 950], [24.2, t1, "face"]]);
    stepTag(6, t0 + 0.1, t1);
    panelTitle("Mijozdan to'lov", t0, t1);
    var rg0 = oval(310, null, [1, 1, 1], 14, 3, [CX, 590], t0 + 0.4, t1, "halqa"); fadeIn(rg0, t0 + 0.4, 0.3);
    radial(CX, 590, 420, ACC, 45, 24.3, t1);
    money(CX, 590, 140, 24.3, 0.6, t1, 100, "+$");
    var rg = oval(310, null, ACC2, 100, 6, [CX, 590], 24.3, t1, "puls halqa"); kf(rg.scale, [24.3, 24.9], [[60, 60, 100], [190, 190, 100]], 10, 70); kf(rg.opacity, [24.3, 24.9], [90, 0], 30, 30);
});

// ================= S8: kurs sotmayman =================
runScene("S08 kurs", KB[7], KB[8], function () {
    var t0 = KB[7], t1 = KB[8];
    base2(t0, t1, [[t0, t1, "face"]]);
    var cd = flatCard(520, 190, 54, [CX, 545], 26.0, t1, CARDF2, 18);
    tx("Kurs", CX, 545, 104, TXT, 26.1, t1, { still: true });
    var st = rr(450, 8, 4, ACC, null, 100, 0, [CX, 547], 26.62, t1, "chizilgan"); kf(st.scale, [26.62, 26.95], [[0, 100, 100], [100, 100, 100]], 20, 70);
    var xc = oval(86, ACC, null, 100, 0, [CX + 250, 460], 26.75, t1, "belgi"); popIn(xc, 26.75, 100); fadeIn(xc, 26.75, 0.1);
    iX(CX + 250, 460, 1.0, [1, 1, 1], 26.8, t1);
});

// ================= S9: foydali video darslar =================
runScene("S09 darslar", KB[8], 33.0, function () {
    var t0 = KB[8], t1 = 33.0;
    base2(t0, t1, [[t0, t1, "face"]]);
    tx("o'z blogimda", CX, 322, 46, MUTE, 27.45, t1, { font: LIGHT, rise: true });
    var rows = [["Marketing", 28.7], ["AI vositalari", 29.2], ["Foydali video darslar", 30.95]], ys = [430, 560, 690];
    for (var i = 0; i < rows.length; i++) {
        var hot = (i == 2), ta = rows[i][1], y = ys[i];
        if (hot) { gradPanel(860, 108, 34, [CX, y], ta, t1, ACC2, [0.74, 0.28, 0.12], {}); }
        else { flatCard(860, 108, 34, [CX, y], ta, t1, CARDF2, 16); }
        tx(rows[i][0], 190, y, 44, hot ? [1, 1, 1] : TXT, ta + 0.1, t1, { left: true, still: true, maxW: 640 });
        var ck = oval(62, hot ? [1, 1, 1] : ACC, null, 100, 0, [875, y], ta + 0.25, t1, "belgi"); popIn(ck, ta + 0.25, 100); fadeIn(ck, ta + 0.25, 0.1);
        iCheck(875, y, 0.95, hot ? [0.1, 0.07, 0.05] : [1, 1, 1], ta + 0.3, t1);
    }
});

// ================= S10: obuna =================
runScene("S10 obuna", 33.0, DUR, function () {
    var t0 = 33.0, t1 = DUR;
    base2(t0, t1, [[t0, t1, "face"]]);
    claudeMark(CX, 385, 130, 33.2, t1);
    var sp = gradPanel(600, 134, 67, [CX, 590], 33.8, t1, ACC2, [0.80, 0.31, 0.14], {});
    tx("+ Obuna bo'ling", CX, 590, 54, [1, 1, 1], 33.95, 34.95, { rise: true, out: true });
    pressAnim(sp.ctrl, 34.72);
    var fr = rr(640, 124, 62, [1, 1, 1], null, 100, 0, [CX, 590], 34.95, t1, "obuna bo'ldi"); fadeIn(fr, 34.95, 0.15);
    kf(fr.scale, [34.95, 35.25], [[88, 88, 100], [100, 100, 100]], 85, 55);
    tx("Obuna bo'ldingiz", CX + 34, 590, 46, [0.09, 0.07, 0.06], 35.05, t1, { rise: true, maxW: 460 });
    iCheck(CX - 195, 590, 0.95, ACC, 35.1, t1);
});

// ============ SUBTITRLAR ============
runScene("CAPTIONS", 0, DUR, function () {
    for (var i = 0; i < DATA.CAPS.length; i++) {
        var c = DATA.CAPS[i], s0 = c[0], e0 = c[1];
        var l = mkText(c[2], { font: HEAD, size: 60, color: TXT, pos: [CX, CAP_Y], t0: s0, t1: e0, maxW: 860, noReg: true, tag: "CAP" });
        kf(l.scale, [s0, s0 + 0.16], [S(l, 94), S(l, 100)], 60, 60);
        kf(l.opacity, [s0, s0 + 0.1, e0 - 0.1, e0], [0, 100, 100, 0], 60, 60);
    }
});

// ============ MAIN: kesishuvli yumshoq o'tishlar ============
comp = MAIN; curScene = "MAIN";
var TR = 0.16, FD = 0.32;
var order = ["S01 hook", "S02 rasmlar", "S03 generatsiya", "S04 montaj", "S05 reklama", "S06 sotuvlar", "S07 tolov", "S08 kurs", "S09 darslar", "S10 obuna"];
for (var ii = 1; ii <= MAIN.numLayers; ii++) {
    var ly = MAIN.layer(ii), idx = -1, q;
    for (q = 0; q < order.length; q++) if (order[q] == ly.name) idx = q;
    if (idx < 0) continue;
    var a = ly.inPoint, b = ly.outPoint;
    var fadeIn_ = a > 0.01;
    var a2 = fadeIn_ ? a - TR : a;
    var b2 = (b < DUR - 0.01) ? b + FD + TR : b;
    ly.inPoint = a2; ly.outPoint = b2;
    if (fadeIn_) { kf(ly.opacity, [a2, a2 + FD], [0, 100], 60, 60); kf(ly.scale, [a2, a2 + FD], [[96, 96, 100], [100, 100, 100]], 50, 50); }
}
for (ii = 1; ii <= MAIN.numLayers; ii++) { if (MAIN.layer(ii).name == "CAPTIONS") { MAIN.layer(ii).moveToBeginning(); break; } }
base_v.moveToEnd();
try { MAIN.openInViewer(); } catch (e) { }
proj.save(new File(base + PROJECT.name + ".aep"));
L("DONE MAIN layers=" + MAIN.numLayers);
var f = new File(base + "build_log.txt"); f.open("w"); f.write(LOG.join("\n")); f.close();
