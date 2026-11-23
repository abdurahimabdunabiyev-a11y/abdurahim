// ===== MUSTAFO BLOKLARI: logotip kartasi, qadam tegi, tugun/oqim, hisoblagich, b-roll karta, base2 =====
// mustafo_lib.jsx dan KEYIN ulanadi. base2(t0,t1,[[a,b,'face'|'broll',fy],...]) = fon + tepa panel + pastki video karta.
function imp2(n) { return proj.importFile(new ImportOptions(new File(base + n))); }

// ---------- yordamchilar ----------
function tileLogo(kind, cx, cy, sz, t0, t1) {
    var ctrl = comp.layers.addNull(); ctrl.name = "logo " + kind; ctrl.anchorPoint.setValue([0, 0]); ctrl.position.setValue([cx, cy]); span(ctrl, t0, t1);
    var m = rr(sz, sz, sz * 0.27, [1, 1, 1], null, 100, 0, [0, 0], t0, t1, "logo maska");
    var ft = comp.layers.add(imp2("logos/k/" + kind + "_k.svg.png")); ft.name = "logo " + kind + " belgi"; span(ft, t0, t1);
    ft.moveAfter(m);
    try { ft.setTrackMatte(m, TrackMatteType.ALPHA); } catch (e) { ft.trackMatteType = TrackMatteType.ALPHA; }
    ft.parent = ctrl; m.parent = ctrl;
    ft.position.setValue([0, 0]); ft.scale.setValue([sz / 1024 * 100, sz / 1024 * 100, 100]); m.position.setValue([0, 0]);
    var ring = rr(sz, sz, sz * 0.27, null, [1, 1, 1], 24, 2, [0, 0], t0, t1, "logo chegara"); ring.parent = ctrl; ring.position.setValue([0, 0]);
    kf(ctrl.scale, [t0, t0 + 0.16, t0 + 0.3], [[0, 0, 100], [110, 110, 100], [100, 100, 100]], 70, 60);
    return ctrl;
}
function plus2(x, y, t0, t1, big) {
    var l = strokeLines([[[0, -20], [0, 20]], [[-20, 0], [20, 0]]], ACC2, 9, [x, y], big || 1.0, t0, t1, 0.22); return l;
}
function stepTag(n, t0, t1) {
    var b = rr(206, 58, 29, null, [1, 1, 1], 35, 2, [200, 304], t0, t1, "qadam teg"); fadeIn(b, t0, 0.3);
    tx(n + "-QADAM", 200, 304, 26, MUTE, t0 + 0.05, t1, { font: LIGHT, still: true, maxW: 170 });
}
function panelTitle(str, t0, t1) { return tx(str, CX, 378, 52, TXT, t0 + 0.12, t1, { rise: true }); }
function photoIcon(x, y, sc, t0, t1) {
    var l = strokeLines([[[-46, 34], [-14, -6], [8, 22], [26, 4], [46, 34]]], MUTE, 7, [x, y + 6], sc, t0, t1, 0.4);
    var sun = oval(26 * sc, ACC2, null, 100, 0, [x + 24 * sc, y - 24 * sc], t0 + 0.15, t1, "quyosh"); popIn(sun, t0 + 0.15, 100); fadeIn(sun, t0 + 0.15, 0.1);
    return l;
}
function sparkW(x, y, size, t0, t1) {   // oq Claude uchquni (to'q sariq tugun ichida)
    var s = comp.layers.addShape(); s.name = "uchqun";
    var root = s.property("ADBE Root Vectors Group"), n = 12, len = size * 0.5, wd = size * 0.09;
    for (var i = 0; i < n; i++) {
        var g = root.addProperty("ADBE Vector Group");
        var r = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Rect");
        var ln = len * ((i % 3 == 0) ? 1.0 : ((i % 3 == 1) ? 0.78 : 0.9));
        r.property("ADBE Vector Rect Size").setValue([wd, ln]);
        r.property("ADBE Vector Rect Position").setValue([0, -(ln / 2 + size * 0.06)]);
        r.property("ADBE Vector Rect Roundness").setValue(wd / 2);
        g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill").property("ADBE Vector Fill Color").setValue([1, 1, 1]);
        g.property("ADBE Vector Transform Group").property("ADBE Vector Rotation").setValue(i * 30 + 8);
    }
    s.position.setValue([x, y]); span(s, t0, t1);
    kf(s.scale, [t0, t0 + 0.3, t0 + 0.5], [[0, 0, 100], [108, 108, 100], [100, 100, 100]], 70, 60);
    s.rotation.expression = "value + Math.max(0, time - " + t0 + ") * 14";
    return s;
}
function money(cx, cy, size, tS, d, tE, target, pre) {
    var ex = 'var p=Math.min(1,Math.max(0,(time-' + tS + ')/' + d + '));p=1-Math.pow(1-p,3);"' + pre + '"+Math.round(' + target + '*p)';
    var n = mkText(pre + "100", { font: HEAD, size: size, color: TXT, pos: [cx, cy], t0: tS, t1: tE, maxW: 760, noReg: true, expr: ex });
    fadeIn(n, tS, 0.2); return n;
}
// pastki video karta: rejimlar ro'yxati [a, b, "face"|"broll", fy]
function brollCard(cx, cy, w, h, rad, t0, t1, z0, z1, fy) {
    var m = rr(w, h, rad, [1, 1, 1], null, 100, 0, [cx, cy], t0, t1, "b-roll matte");
    var v = comp.layers.add(A.aroll); v.startTime = 0; v.inPoint = t0; v.outPoint = t1; v.audioEnabled = false; v.name = "b-roll karta";
    v.anchorPoint.setValue([540, fy]); v.position.setValue([cx, cy]);
    kf(v.scale, [t0, t1], [[z0, z0, 100], [z1, z1, 100]], 30, 30);
    v.moveAfter(m);
    try { v.setTrackMatte(m, TrackMatteType.ALPHA); } catch (e) { v.trackMatteType = TrackMatteType.ALPHA; }
    fadeIn(v, t0, 0.3);
    var b = rr(w, h, rad, null, [1, 1, 1], 20, 2, [cx, cy], t0, t1, "video chegara"); fadeIn(b, t0, 0.3);
}
function base2(t0, t1, segs) {
    darkBg(t0, t1, { x1: 80, y1: 1650, r1: 1100, o1: 55, x2: 1000, y2: 200, r2: 700, o2: 26 });
    var p = gradPanel(CW, TOP_H, 54, [CX, TOP_CY], t0, t1, [0.34, 0.115, 0.04], CARDF, { border: 22 });
    for (var i = 0; i < segs.length; i++) {
        var s = segs[i], a = s[0], b = s[1];
        if (s[2] == "face") faceCard(CX, BOT_CY, CW, BOT_H, 48, a, b); else brollCard(CX, BOT_CY, CW, BOT_H, 48, a, b, 108, 118, s[3]);
    }
    return p;
}
function flowPath(name, t0, t1, tA, tB) {
    pathLayer(name, [[225, 665], [540, 505], [855, 665]], [[0, 0], [-170, 0], [-110, -120]], [[110, -120], [170, 0], [0, 0]], t0, t1, tA, tB);
    pulseDot(name, tA, tB, tB + 0.5);
}

