// ===== MUSTAFO MONTAJ KUTUBXONASI (After Effects, ExtendScript) =====
// Oldin cfg.jsx bilan PROJECT belgilanadi:  var PROJECT = { base: "/abs/papka/", dur: 35.47, aroll: "cut.mp4", face: "face.js", name: "loyiha" };
// Tartib: cfg.jsx + shu fayl + mustafo_blocks.jsx + scenes.jsx  (scripts/build.sh shuni birlashtiradi)
var base = PROJECT.base;
var DUR = PROJECT.dur;
$.evalFile(new File("~/.claude/skills/reels-zonali-montaj/lib/lib_zonali.jsx"));
var FACE = [[0, 540, 520]];
try { $.evalFile(new File(base + (PROJECT.face || "face.js"))); } catch (e) { }
// ---- shrift va uslub ----
var HEAD = "HelveticaNeue-Medium", LIGHT = "HelveticaNeue-Light", BOLDF = "HelveticaNeue-Bold";
F_H = HEAD; F_D = LIGHT;
shadow = function () { };                       // soyalar butunlay o'chirildi (kesilib qolardi)
var BG = [0.043, 0.035, 0.032];
var ACC = [0.93, 0.42, 0.22];                   // asosiy to'q sariq
var ACC2 = [1.0, 0.58, 0.30];                   // och to'q sariq
var DEEP = [0.40, 0.13, 0.045];                 // chuqur to'q sariq
var CARDF = [0.082, 0.07, 0.064];
var CARDF2 = [0.115, 0.098, 0.09];
var TXT = [0.975, 0.965, 0.955];
var MUTE = [0.66, 0.62, 0.59];
var BLK = [0, 0, 0];

// ---- geometriya ----
var TOP_CY = 540, TOP_H = 590, CW = 940;        // yuqori panel  y 245-835 (video karta bilan BIR XIL o'lcham)
var BOT_CY = 1260, BOT_H = 590;                 // video karta   y 965-1555
var CAP_Y = 900;                                // subtitr: panel va video ORASIDA (o'rtada)

try { app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES); } catch (e) { }
app.newProject();
proj = app.project;
function imp(n) { return proj.importFile(new ImportOptions(new File(base + n))); }
var FAS = proj.items.addFolder("01 ASSETS"), FSC = proj.items.addFolder("02 SCENES");
var A = { aroll: imp(PROJECT.aroll) };
A.aroll.parentFolder = FAS;

MAIN = proj.items.addComp("00 MAIN", W, H, 1, DUR, FPS);
MAIN.bgColor = [0, 0, 0];
comp = MAIN; curScene = "MAIN";

function grade(l) { return;                              // yengil rang ishlovi
    try {
        var bc = l.property("ADBE Effect Parade").addProperty("ADBE Brightness & Contrast 2");
        bc.property("ADBE Brightness & Contrast 2-0001").setValue(-6);
        bc.property("ADBE Brightness & Contrast 2-0002").setValue(16);
    } catch (e) { L("bc err " + e); }
    try {
        var hs = l.property("ADBE Effect Parade").addProperty("ADBE HUE SATURATION");
        hs.property("ADBE HUE SATURATION-0004").setValue(14);
    } catch (e) { L("hs err " + e); }
}
var base_v = MAIN.layers.add(A.aroll); base_v.name = "A-ROLL (asosiy video + ovoz)"; base_v.startTime = 0; grade(base_v);

// ---------------- yordamchilar ----------------
function tx(str, x, y, size, color, t0, t1, o) {
    o = o || {};
    var l = mkText(str, { font: o.font || HEAD, size: size, color: color, pos: [x, y], t0: t0, t1: t1, maxW: o.maxW || 860, left: o.left, noReg: true });
    if (o.still) fadeIn(l, t0, 0.2); else if (o.rise) riseIn(l, t0, 36); else if (o.pop) { popIn(l, t0, 100); fadeIn(l, t0, 0.14); } else fadeIn(l, t0, 0.2);
    if (o.out) fadeOut(l, t1, 0.2);
    return l;
}
function fo(arr, t, d) { for (var i = 0; i < arr.length; i++) fadeOut(arr[i], t, d || 0.2); }
// qirrasiz yumshoq nur: butun kadrli solid + radial Ramp + Screen (blur ham, kesilish ham yo'q)
function radial(cx, cy, r, color, op, t0, t1) {
    var s = comp.layers.addSolid([0, 0, 0], "nur", W, H, 1); span(s, t0, t1);
    try {
        var rp = s.property("ADBE Effect Parade").addProperty("ADBE Ramp");
        rp.property("ADBE Ramp-0001").setValue([cx, cy]); rp.property("ADBE Ramp-0002").setValue(color);
        rp.property("ADBE Ramp-0003").setValue([cx + r, cy]); rp.property("ADBE Ramp-0004").setValue(BLK);
        rp.property("ADBE Ramp-0005").setValue(2); rp.property("ADBE Ramp-0006").setValue(8);
    } catch (e) { L("radial err " + e); }
    s.blendingMode = BlendingMode.SCREEN;
    kf(s.opacity, [t0, t0 + 0.5, t1 - 0.35, t1], [0, op, op, 0], 50, 50);
    return s;
}
function darkBg(t0, t1, o) {
    o = o || {};
    var s = comp.layers.addSolid(BG, "fon", W, H, 1); span(s, t0, t1);
    radial(o.x1 !== undefined ? o.x1 : 120, o.y1 !== undefined ? o.y1 : 1800, o.r1 || 1150, [0.80, 0.30, 0.09], o.o1 || 62, t0, t1);
    radial(o.x2 !== undefined ? o.x2 : 1010, o.y2 !== undefined ? o.y2 : 120, o.r2 || 760, [0.62, 0.22, 0.07], o.o2 || 30, t0, t1);
    return s;
}
function rr(w, h, rad, fill, strokeCol, sop, sw, pos, t0, t1, name) {
    var s = comp.layers.addShape(); s.name = name || "rr";
    var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var r = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Rect");
    r.property("ADBE Vector Rect Size").setValue([w, h]); r.property("ADBE Vector Rect Roundness").setValue(rad);
    if (fill) g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill").property("ADBE Vector Fill Color").setValue(fill);
    if (strokeCol) {
        var st = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
        st.property("ADBE Vector Stroke Color").setValue(strokeCol); st.property("ADBE Vector Stroke Width").setValue(sw || 2);
        st.property("ADBE Vector Stroke Opacity").setValue(sop === undefined ? 100 : sop);
    }
    s.position.setValue(pos); span(s, t0, t1); return s;
}
function oval(d, fill, strokeCol, sop, sw, pos, t0, t1, name) {
    var s = comp.layers.addShape(); s.name = name || "oval";
    var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Ellipse").property("ADBE Vector Ellipse Size").setValue([d, d]);
    if (fill) g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill").property("ADBE Vector Fill Color").setValue(fill);
    if (strokeCol) {
        var st = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
        st.property("ADBE Vector Stroke Color").setValue(strokeCol); st.property("ADBE Vector Stroke Width").setValue(sw || 2);
        st.property("ADBE Vector Stroke Opacity").setValue(sop === undefined ? 100 : sop);
    }
    s.position.setValue(pos); span(s, t0, t1); return s;
}
// gradient panel: solid + Ramp, yumaloq matte bilan kesilgan; ctrl bilan harakatlanadi
function gradPanel(w, h, rad, pos, t0, t1, c0, c1, o) {
    o = o || {};
    var ctrl = comp.layers.addNull(); ctrl.name = "panel ctrl"; ctrl.anchorPoint.setValue([0, 0]); ctrl.position.setValue(pos); span(ctrl, t0, t1);
    var m = rr(w, h, rad, [1, 1, 1], null, 100, 0, [0, 0], t0, t1, "matte");
    var sol = comp.layers.addSolid([1, 1, 1], "panel gradient", Math.round(w), Math.round(h), 1); span(sol, t0, t1);
    try {
        var rp = sol.property("ADBE Effect Parade").addProperty("ADBE Ramp");
        if (o.radial) {
            rp.property("ADBE Ramp-0001").setValue([w * o.radial[0], h * o.radial[1]]); rp.property("ADBE Ramp-0002").setValue(c0);
            rp.property("ADBE Ramp-0003").setValue([w * o.radial[0] + w * o.radial[2], h * o.radial[1]]); rp.property("ADBE Ramp-0004").setValue(c1);
            rp.property("ADBE Ramp-0005").setValue(2);
        } else {
            rp.property("ADBE Ramp-0001").setValue([w * 0.0, h * 1.0]); rp.property("ADBE Ramp-0002").setValue(c0);
            rp.property("ADBE Ramp-0003").setValue([w * 1.0, h * 0.0]); rp.property("ADBE Ramp-0004").setValue(c1);
        }
        rp.property("ADBE Ramp-0006").setValue(6);
    } catch (e) { L("panel ramp err " + e); }
    sol.moveAfter(m);
    try { sol.setTrackMatte(m, TrackMatteType.ALPHA); } catch (e) { sol.trackMatteType = TrackMatteType.ALPHA; }
    sol.parent = ctrl; m.parent = ctrl; sol.position.setValue([0, 0]); m.position.setValue([0, 0]);
    var out = { ctrl: ctrl, sol: sol, m: m, layers: [sol] };
    if (o.border) {
        var b = rr(w, h, rad, null, [1, 1, 1], o.border, 2, [0, 0], t0, t1, "chegara"); b.parent = ctrl; b.position.setValue([0, 0]);
        out.border = b; out.layers.push(b);
    }
    kf(ctrl.scale, [t0, t0 + 0.45], [[95, 95, 100], [100, 100, 100]], 85, 55);
    fadeIn(sol, t0, 0.3); if (out.border) fadeIn(out.border, t0, 0.3);
    return out;
}
function panelOut(p, t, d) { for (var i = 0; i < p.layers.length; i++) fadeOut(p.layers[i], t, d || 0.25); }
// oddiy qora karta (chegara bilan)
function flatCard(w, h, rad, pos, t0, t1, fill, bop) {
    var c = rr(w, h, rad, fill || CARDF, [1, 1, 1], bop === undefined ? 14 : bop, 2, pos, t0, t1, "karta");
    fadeIn(c, t0, 0.25);
    kf(c.scale, [t0, t0 + 0.4], [[96, 96, 100], [100, 100, 100]], 85, 55);
    return c;
}
// vektor ikonkalar (shrift belgilariga bog'lanmaydi)
function strokeLines(parts, color, sw, pos, sc, t0, t1, trimDur) {
    var s = comp.layers.addShape(); s.name = "ikonka";
    for (var i = 0; i < parts.length; i++) {
        var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
        var p = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Group");
        var sh = new Shape(); sh.vertices = parts[i]; sh.closed = false;
        var z = []; for (var q = 0; q < parts[i].length; q++) z.push([0, 0]);
        sh.inTangents = z; sh.outTangents = z; p.property("ADBE Vector Shape").setValue(sh);
        var st = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
        st.property("ADBE Vector Stroke Color").setValue(color); st.property("ADBE Vector Stroke Width").setValue(sw);
        st.property("ADBE Vector Stroke Line Cap").setValue(2); st.property("ADBE Vector Stroke Line Join").setValue(2);
    }
    if (trimDur) {
        try { var tr = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Filter - Trim"); kf(tr.property("ADBE Vector Trim End"), [t0, t0 + trimDur], [0, 100], 30, 70); } catch (e) { L("trim err " + e); }
    }
    s.position.setValue(pos); s.scale.setValue([sc * 100, sc * 100, 100]); span(s, t0, t1); return s;
}
function iCheck(x, y, sc, color, t0, t1) { return strokeLines([[[-22, 2], [-7, 17], [24, -16]]], color, 9, [x, y], sc, t0, t1, 0.35); }
function iDown(x, y, sc, color, t0, t1) { return strokeLines([[[0, -26], [0, 24]], [[-18, 6], [0, 24], [18, 6]]], color, 8, [x, y], sc, t0, t1, 0.4); }
function iUp(x, y, sc, color, t0, t1) { return strokeLines([[[0, 26], [0, -24]], [[-18, -6], [0, -24], [18, -6]]], color, 8, [x, y], sc, t0, t1, 0.4); }
function iSearch(x, y, sc, color, t0, t1) {
    var l = strokeLines([[[10, 10], [27, 27]]], color, 8, [x, y], sc, t0, t1, 0.3);
    var g = l.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var el = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Ellipse");
    el.property("ADBE Vector Ellipse Size").setValue([36, 36]); el.property("ADBE Vector Ellipse Position").setValue([-8, -8]);
    var st = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
    st.property("ADBE Vector Stroke Color").setValue(color); st.property("ADBE Vector Stroke Width").setValue(8);
    return l;
}
function iClock(x, y, d, t0, t1) {
    var ring = oval(d, null, [1, 1, 1], 14, 10, [x, y], t0, t1, "soat halqa"); fadeIn(ring, t0, 0.25);
    var arc = oval(d, null, ACC, 100, 10, [x, y], t0, t1, "soat yoyi"); arc.rotation.setValue(-90);
    try { var tr = arc.property("ADBE Root Vectors Group").addProperty("ADBE Vector Filter - Trim"); kf(tr.property("ADBE Vector Trim End"), [t0, t1 - 0.15], [0, 100], 25, 60); } catch (e) { }
    var h1 = rr(8, d * 0.38, 4, TXT, null, 100, 0, [x, y], t0, t1, "min"); h1.anchorPoint.setValue([0, d * 0.19]); h1.rotation.expression = "(time - " + t0 + ") * 300";
    var h2 = rr(8, d * 0.26, 4, ACC2, null, 100, 0, [x, y], t0, t1, "soat"); h2.anchorPoint.setValue([0, d * 0.13]); h2.rotation.expression = "90 + (time - " + t0 + ") * 25";
    fadeIn(h1, t0, 0.25); fadeIn(h2, t0, 0.25);
    return [ring, arc, h1, h2];
}
// Claude belgisi
function claudeMark(x, y, size, t0, t1) {
    var bgk = gradPanel(size, size, size * 0.26, [x, y], t0, t1, ACC2, [0.80, 0.33, 0.17], {});
    var s = comp.layers.addShape(); s.name = "Claude nurlar";
    var root = s.property("ADBE Root Vectors Group"), n = 12, len = size * 0.3, wd = size * 0.055;
    for (var i = 0; i < n; i++) {
        var g = root.addProperty("ADBE Vector Group");
        var r = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Rect");
        var ln = len * ((i % 3 == 0) ? 1.0 : ((i % 3 == 1) ? 0.82 : 0.92));
        r.property("ADBE Vector Rect Size").setValue([wd, ln]);
        r.property("ADBE Vector Rect Position").setValue([0, -(ln / 2 + size * 0.045)]);
        r.property("ADBE Vector Rect Roundness").setValue(wd / 2);
        g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill").property("ADBE Vector Fill Color").setValue([1, 1, 1]);
        g.property("ADBE Vector Transform Group").property("ADBE Vector Rotation").setValue(i * 30 + 8);
    }
    s.position.setValue([x, y]); span(s, t0, t1);
    kf(s.scale, [t0, t0 + 0.3, t0 + 0.5], [[0, 0, 100], [108, 108, 100], [100, 100, 100]], 70, 60);
    s.rotation.expression = "value + Math.max(0, time - " + t0 + ") * 14";
    return { ctrl: bgk.ctrl, layers: bgk.layers.concat([s]) };
}
// video karta: yumaloq matte + yuzni kuzatib boradigan kadr
function faceCard(cx, cy, w, h, rad, t0, t1) {
    var k = 1.05, iw = A.aroll.width, ih = A.aroll.height;
    var m = rr(w, h, rad, [1, 1, 1], null, 100, 0, [cx, cy], t0, t1, "video matte");
    var v = MAIN === comp ? null : comp.layers.add(A.aroll);
    v.startTime = 0; v.inPoint = t0; v.outPoint = t1; v.audioEnabled = false; v.name = "video karta (yuz kuzatuvi)";
    v.scale.setValue([k * 100, k * 100, 100]); grade(v);
    var hw = (w / 2) / k, hh = (h / 2) / k, i, ts = [], vs = [];
    for (i = 0; i < FACE.length; i++) {
        var ft = FACE[i][0];
        if (ft < t0 - 0.6 || ft > t1 + 0.6) continue;
        var sx = Math.max(hw, Math.min(iw - hw, FACE[i][1]));
        var sy = Math.max(hh, Math.min(ih - hh, FACE[i][2] - 30));
        ts.push(ft); vs.push([cx + (iw / 2 - sx) * k, cy + (ih / 2 - sy) * k]);
    }
    if (ts.length == 0) { ts = [t0]; vs = [[cx, cy]]; }
    for (i = 0; i < ts.length; i++) v.position.setValueAtTime(ts[i], vs[i]);
    for (i = 1; i <= v.position.numKeys; i++) {
        try { v.position.setInterpolationTypeAtKey(i, KeyframeInterpolationType.BEZIER, KeyframeInterpolationType.BEZIER); v.position.setTemporalAutoBezierAtKey(i, true); v.position.setSpatialAutoBezierAtKey(i, true); } catch (e) { }
    }
    v.moveAfter(m);
    try { v.setTrackMatte(m, TrackMatteType.ALPHA); } catch (e) { v.trackMatteType = TrackMatteType.ALPHA; }
    fadeIn(v, t0, 0.3);
    var b = rr(w, h, rad, null, [1, 1, 1], 20, 2, [cx, cy], t0, t1, "video chegara"); fadeIn(b, t0, 0.3);
    return [v, b];
}
function splitBase(t0, t1) {
    darkBg(t0, t1, { x1: 80, y1: 1650, r1: 1100, o1: 55, x2: 1000, y2: 200, r2: 700, o2: 26 });
    var p = gradPanel(CW, TOP_H, 54, [CX, TOP_CY], t0, t1, [0.34, 0.115, 0.04], CARDF, { border: 22 });
    faceCard(CX, BOT_CY, CW, BOT_H, 48, t0, t1);
    return p;
}
function node(icon, label, x, y, t0, t1, hot) {
    var parts = [];
    if (hot) { radial(x, y, 300, ACC, 55, t0, t1); }
    var p = hot ? gradPanel(180, 180, 48, [x, y], t0, t1, ACC2, [0.78, 0.31, 0.15], {}) : gradPanel(180, 180, 48, [x, y], t0, t1, [0.20, 0.09, 0.05], CARDF2, { border: 40 });
    icon(x, y);
    tx(label, x, y + 138, 34, MUTE, t0 + 0.15, t1, { font: LIGHT, rise: true, maxW: 260 });
    return p;
}
function dashLine(x0, y0, x1, y1, t0, t1, dur) {
    var s = comp.layers.addShape(); s.name = "punktir";
    var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var p = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Group");
    var sh = new Shape(); sh.vertices = [[x0, y0], [x1, y1]]; sh.inTangents = [[0, 0], [0, 0]]; sh.outTangents = [[0, 0], [0, 0]]; sh.closed = false;
    p.property("ADBE Vector Shape").setValue(sh);
    var st = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
    st.property("ADBE Vector Stroke Color").setValue(ACC2); st.property("ADBE Vector Stroke Width").setValue(5); st.property("ADBE Vector Stroke Line Cap").setValue(2);
    try { st.property("ADBE Vector Stroke Dashes").addProperty("ADBE Vector Stroke Dash 1").setValue(14); } catch (e) { }
    try { var tr = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Filter - Trim"); kf(tr.property("ADBE Vector Trim End"), [t0, t0 + (dur || 0.4)], [0, 100], 30, 70); } catch (e) { L("trim err " + e); }
    s.position.setValue([0, 0]); span(s, t0, t1); return s;
}
function counter(t0, d, y, size, color, tStart, tEnd, font) {
    var ex = 'var t0=' + t0 + ',d=' + d + ';var p=Math.min(1,Math.max(0,(time-t0)/d));p=1-Math.pow(1-p,3);var s=""+Math.round(1000000*p);s.replace(/\\B(?=(\\d{3})+(?!\\d))/g," ")';
    var n = mkText("1 000 000", { font: font || HEAD, size: size, color: color, pos: [CX, y], t0: tStart, t1: tEnd, maxW: 880, noReg: true });
    n.property("Source Text").expression = ex; fadeIn(n, tStart, 0.25);
    return n;
}
function pressAnim(ctrl, t) { kf(ctrl.scale, [t - 0.1, t, t + 0.14, t + 0.3], [[100, 100, 100], [90, 90, 100], [106, 106, 100], [100, 100, 100]], 60, 60); }


// ---------- yangi animatsiya yordamchilari (referenslardan g'oya) ----------
function iX(x, y, sc, color, t0, t1) { return strokeLines([[[-14, -14], [14, 14]], [[14, -14], [-14, 14]]], color, 8, [x, y], sc, t0, t1, 0.3); }
// punktir egri yo'l: chizilib boradi; unga pointOnPath orqali nur dog'i bog'lanadi
function pathLayer(name, verts, inT, outT, t0, t1, tA, tB) {
    var s = comp.layers.addShape(); s.name = name;
    var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group"); g.name = "G";
    var p = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Group"); p.name = "P";
    var sh = new Shape(); sh.vertices = verts; sh.inTangents = inT; sh.outTangents = outT; sh.closed = false;
    p.property("ADBE Vector Shape").setValue(sh);
    var st = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
    st.property("ADBE Vector Stroke Color").setValue(ACC2); st.property("ADBE Vector Stroke Width").setValue(5); st.property("ADBE Vector Stroke Line Cap").setValue(2);
    try { st.property("ADBE Vector Stroke Dashes").addProperty("ADBE Vector Stroke Dash 1").setValue(14); } catch (e) { }
    try {
        var tr = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Filter - Trim");
        tr.property("ADBE Vector Trim End").expression = "linear(time," + tA + "," + tB + ",0,100)";
    } catch (e) { L("trim err " + e); }
    s.position.setValue([0, 0]); span(s, t0, t1); return s;
}
function pulseDot(pathName, tA, tB, tOut) {
    var ex = 'var L=thisComp.layer("' + pathName + '"); var q=linear(time,' + tA + ',' + tB + ',0,1); L.toComp(L.content("G").content("P").path.pointOnPath(q))';
    var o = oval(74, ACC, null, 100, 0, [0, 0], tA, tOut, "puls nur"); o.position.expression = ex; kf(o.opacity, [tA, tA + 0.2, tOut - 0.3, tOut], [0, 38, 38, 0], 50, 50);
    var d = oval(26, [1, 1, 1], null, 100, 0, [0, 0], tA, tOut, "puls"); d.position.expression = ex; kf(d.opacity, [tA, tA + 0.2, tOut - 0.3, tOut], [0, 100, 100, 0], 50, 50);
}
// orbitada aylanadigan teg (old tomon yirik va yorqin, orqa tomon kichik va xira)
function orbitChip(label, i, n, cx, cy, rx, ry, t0, t1, speed) {
    var ang = (i / n * 6.2832) + " + (time - " + t0 + ") * " + speed;
    var dep = "(Math.sin(" + ang + ") + 1) / 2";
    var c = rr(210, 70, 35, [0.07, 0.06, 0.055], [1, 1, 1], 30, 2, [cx, cy], t0, t1, "orbita teg");
    var l = mkText(label, { font: LIGHT, size: 36, color: TXT, pos: [0, 0], t0: t0, t1: t1, maxW: 180, noReg: true });
    l.parent = c; l.position.setValue([0, 0]);              // avval biriktiramiz, keyin animatsiya (AE teskari kompensatsiya qilmasin)
    c.position.expression = "var a = " + ang + "; [" + cx + " + " + rx + " * Math.cos(a), " + cy + " + " + ry + " * Math.sin(a)]";
    c.scale.expression = "var d = " + dep + "; var k = 62 + 38 * d; [k, k, 100]";
    var op = "var d = " + dep + "; Math.min(1, (time - " + t0 + ") / 0.5) * (30 + 70 * d)";
    c.opacity.expression = op; l.opacity.expression = op;
    return c;
}

// Sahna qatlamlarini ikki yonga uzaytirish: kesishuv paytida sahna bo'sh qolmasin (aks holda ostidagi xom video "xira kadr" bo'lib ko'rinadi)
runScene = function (name, t0, t1, fn) {
    try {
        var c = newScene(name); fn(c);
        for (var q = 1; q <= c.numLayers; q++) {
            var L_ = c.layer(q);
            if (L_.guideLayer) continue;
            if (Math.abs(L_.outPoint - t1) < 0.02) L_.outPoint = t1 + 0.7;
            if (t0 > 0.01 && Math.abs(L_.inPoint - t0) < 0.02) L_.inPoint = Math.max(0, t0 - 0.25);
        }
        endScene(c, t0, t1); L("OK " + name);
    } catch (e) { L("ERR " + name + " : " + e.toString() + " @" + e.line); }
};

