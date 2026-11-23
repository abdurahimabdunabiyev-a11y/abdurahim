// ===== ZONALI REELS MONTAJ KUTUBXONASI (After Effects, ExtendScript) =====
// Tartib: har sahna alohida kompozitsiya, 00 MAIN ularni yig'adi, CAPTIONS alohida.
// Zonalar (1080x1920): TITLE 250-690 | VISUAL 700-1380 | CAPTION y=1500 | o'ng tugmalar x>890,y>960
var W = 1080, H = 1920, FPS = 30;
var SAFE = { x0: 70, y0: 250, x1: 1010, y1: 1380 };     // kontent zonasi (yashil)
var OUTER = { x0: 70, y0: 250, x1: 1010, y1: 1560 };    // umumiy xavfsiz zona (qizil)
var ZN = { titleTop: 250, titleBot: 690, visTop: 700, visBot: 1380, capY: 1500 };
var KICK_Y = 330, TA_Y = 460, TB_Y = 605;               // kicker, A-qator, B-qator (chapga tekislangan, x=70)
var LX = 70;                                           // chap hoshiya
var LOGO = { x0: 820, y0: 260, x1: 1010, y1: 360 };   // tepa o'ng: logo zonasi (bo'sh)
var BTN = { x0: 890, y0: 956 };                        // Instagram tugmalari: x>890 & y>956 (matn kirmasin)
var VIS_CY = 1040, CARD_W = 880, CARD_H = 680;

// SHAXSIY BREND PALITRASI: sariq, to'q sariq, qora, oq (grid Video 3 dan, ranglar brenddan!)
var F_H = "SFProDisplay-Bold", F_D = "SFProDisplay-Semibold";
var YEL = [1.0, 0.722, 0.11];        // #FFB81C sariq
var ORG = [0.941, 0.353, 0.102];     // #F05A1A to'q sariq
var BLACK = [0.043, 0.043, 0.043];   // #0B0B0B
var GRAY = [0.5, 0.5, 0.5];          // ikkilamchi matn (qora 50%)
var WHITE = [1, 1, 1];

var proj = app.project, comp = null, MAIN = null, curScene = "";
var LOG = []; function L(s) { LOG.push(String(s)); }
var REG = [];
var CX = 540;

// ---------- animatsiya ----------
function easeAll(prop, inf, outf) {
    try {
        var pvt = prop.propertyValueType, dims = 1;
        if (pvt == PropertyValueType.ThreeD || pvt == PropertyValueType.TwoD) dims = prop.value.length;
        for (var k = 1; k <= prop.numKeys; k++) {
            var a = [], b = [];
            for (var d = 0; d < dims; d++) { a.push(new KeyframeEase(0, inf)); b.push(new KeyframeEase(0, outf)); }
            prop.setTemporalEaseAtKey(k, a, b);
        }
    } catch (e) { }
}
function kf(prop, times, vals, inf, outf) {
    for (var i = 0; i < times.length; i++) prop.setValueAtTime(times[i], vals[i]);
    easeAll(prop, inf || 70, outf || 70);
}
function S(l, s) { return [s, s, 100]; }
function fadeIn(l, t, d) { kf(l.opacity, [t, t + (d || 0.12)], [0, 100], 60, 60); }
function fadeOut(l, t1, d) { d = d || 0.12; kf(l.opacity, [t1 - d, t1], [100, 0], 60, 60); }
function popIn(l, t, s) { s = s || 100; kf(l.scale, [t, t + 0.2, t + 0.34], [S(l, s * 0.8), S(l, s * 1.04), S(l, s)], 75, 60); }
function slamIn(l, t, s) { s = s || 100; kf(l.scale, [t, t + 0.14, t + 0.26], [S(l, s * 1.6), S(l, s * 0.96), S(l, s)], 80, 60); }
function riseIn(l, t, dy) {
    var p = l.position.value; dy = dy || 46;
    kf(l.position, [t, t + 0.32], [[p[0], p[1] + dy], [p[0], p[1]]], 85, 55);
    fadeIn(l, t, 0.14);
}
function span(l, t0, t1) { l.inPoint = t0; l.outPoint = t1; }

// ---------- ro'yxat (avtomatik tekshiruv uchun) ----------
function R(cx, cy, w, h, t0, t1, tag, name) {
    REG.push({ sc: curScene, cx: cx, cy: cy, w: w, h: h, t0: t0, t1: t1, tag: tag || "T", name: name || "" });
}

// ---------- matn ----------
function mkText(str, o) {
    var l = comp.layers.addText(str);
    l.name = (o.tag || "T") + " " + str.substr(0, 22);
    var tp = l.property("Source Text"), td = tp.value;
    td.resetCharStyle();
    td.font = o.font || F_H; td.fontSize = o.size || 100; td.fillColor = o.color || BLACK;
    td.applyFill = true; td.applyStroke = false;
    td.justification = o.left ? ParagraphJustification.LEFT_JUSTIFY : ParagraphJustification.CENTER_JUSTIFY;
    td.tracking = (o.track !== undefined) ? o.track : 0;
    tp.setValue(td);
    var r0 = l.sourceRectAtTime(0, false), mw = o.maxW || 900;
    if (!o.expr && r0.width > mw) { td.fontSize = (o.size || 100) * mw / r0.width; tp.setValue(td); }
    if (o.expr) tp.expression = o.expr;
    var r = l.sourceRectAtTime(0, false);
    l.anchorPoint.setValue([o.expr ? 0 : (o.left ? r.left : (r.left + r.width / 2)), r.top + r.height / 2]);
    l.position.setValue(o.pos);
    span(l, o.t0, o.t1);
    l._w = o.fixW || r.width; l._h = r.height;
    if (!o.noReg && curScene != "CAPTIONS") R(o.left ? o.pos[0] + l._w / 2 : o.pos[0], o.pos[1], l._w, l._h, o.t0, o.t1, o.tag || "T", str);
    return l;
}
// sarlavha qatorlari
function kicker(str, t0, t1, out) {
    var l = mkText(str, { font: F_D, size: 52, color: GRAY, pos: [LX, KICK_Y], t0: t0, t1: t1, tag: "TT", maxW: 740, left: true });
    riseIn(l, t0, 24); if (out) fadeOut(l, t1, 0.14); return l;
}
function lineA(str, t0, t1, o) {
    o = o || {};
    var l = mkText(str, { font: F_H, size: o.size || 128, color: o.color || BLACK, pos: [LX, o.y || TA_Y], t0: t0, t1: t1, tag: "TT", maxW: 940, left: true });
    riseIn(l, t0, 50); if (o.out) fadeOut(l, t1, 0.14); return l;
}
// sariq -> to'q sariq gradient matn (Ramp + alpha matte), o.left bo'lsa chapga tekislangan
function gradText(str, o) {
    var pos = o.pos, left = !!o.left;
    var ctrl = comp.layers.addNull(); ctrl.name = "G " + str.substr(0, 16);
    ctrl.anchorPoint.setValue([0, 0]); ctrl.position.setValue(pos); span(ctrl, o.t0, o.t1);
    var o2 = {}; for (var k in o) o2[k] = o[k];
    o2.pos = [0, 0]; o2.color = WHITE; o2.noReg = true;
    var tx = mkText(str, o2);
    var w = (o.fixW || tx._w) + 80, h = tx._h + 80;
    var sol = comp.layers.addSolid([1, 1, 1], "grad fill", Math.round(w), Math.round(h), 1);
    span(sol, o.t0, o.t1); sol.moveAfter(tx);
    try {
        var rp = sol.property("ADBE Effect Parade").addProperty("ADBE Ramp");
        rp.property("ADBE Ramp-0001").setValue([w * 0.06, h * 0.25]); rp.property("ADBE Ramp-0002").setValue(YEL);
        rp.property("ADBE Ramp-0003").setValue([w * 0.94, h * 0.75]); rp.property("ADBE Ramp-0004").setValue(ORG);
    } catch (e) { L("ramp err " + e); }
    try { sol.setTrackMatte(tx, TrackMatteType.ALPHA); } catch (e) { sol.trackMatteType = TrackMatteType.ALPHA; }
    sol.parent = ctrl; sol.position.setValue([left ? (o.fixW || tx._w) / 2 : 0, 0]);
    tx.parent = ctrl; tx.position.setValue([0, 0]);
    if (o.rise) riseIn(ctrl, o.t0, 50); else if (o.slam) slamIn(ctrl, o.t0, 100); else popIn(ctrl, o.t0, 100);
    fadeIn(sol, o.t0, 0.14); fadeIn(tx, o.t0, 0.14);
    if (o.out) { fadeOut(sol, o.t1, 0.14); fadeOut(tx, o.t1, 0.14); }
    if (!o.noReg) R(left ? pos[0] + (o.fixW || tx._w) / 2 : pos[0], pos[1], o.fixW || tx._w, tx._h, o.t0, o.t1, o.tag || "TT", str);
    ctrl._w = tx._w; ctrl._h = tx._h;
    return ctrl;
}
function lineB(str, t0, t1, o) {
    o = o || {};
    return gradText(str, { font: F_H, size: o.size || 128, pos: [LX, o.y || TB_Y], t0: t0, t1: t1, tag: "TT", maxW: 940, expr: o.expr, fixW: o.fixW, left: true, rise: true, out: o.out });
}
// butun sarlavha bloki
function titleBlock(o) {
    var r = {};
    if (o.k) r.k = kicker(o.k, o.kt0 !== undefined ? o.kt0 : o.t0, o.kt1 || o.t1, o.out);
    if (o.a) r.a = lineA(o.a, o.at0 !== undefined ? o.at0 : o.t0 + 0.12, o.t1, { out: o.out });
    if (o.b) r.b = lineB(o.b, o.bt0 !== undefined ? o.bt0 : o.t0 + 0.55, o.t1, { out: o.out });
    return r;
}

// ---------- shakllar ----------
function shapeRect(w, h, rad, color, pos, t0, t1, name) {
    var s = comp.layers.addShape(); s.name = name || "rect";
    var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var r = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Rect");
    r.property("ADBE Vector Rect Size").setValue([w, h]);
    r.property("ADBE Vector Rect Roundness").setValue(rad);
    var f = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill");
    f.property("ADBE Vector Fill Color").setValue(color);
    s.position.setValue(pos); span(s, t0, t1);
    return s;
}
function shadow(l, op, dist, soft) {
    try {
        var e = l.property("ADBE Effect Parade").addProperty("ADBE Drop Shadow");
        e.property("ADBE Drop Shadow-0002").setValue(op || 70);
        e.property("ADBE Drop Shadow-0003").setValue(180);
        e.property("ADBE Drop Shadow-0004").setValue(dist || 18);
        e.property("ADBE Drop Shadow-0005").setValue(soft || 50);
    } catch (e) { L("shadow err " + e); }
}
function pill(str, o) {
    var t = mkText(str, { font: o.font || F_H, size: o.size || 56, color: o.color || WHITE, pos: o.pos, t0: o.t0, t1: o.t1, maxW: o.maxW || 760, noReg: true });
    var w = t._w + (o.padX !== undefined ? o.padX : 56) * 2, h = t._h + (o.padY !== undefined ? o.padY : 26) * 2;
    var p = shapeRect(w, h, h / 2, o.bg || BLACK, o.pos, o.t0, o.t1, "pill");
    p.moveAfter(t); t.parent = p; t.position.setValue([0, 0]);
    if (o.shadow) shadow(p, 55, 10, 30);
    popIn(p, o.t0, 100); fadeIn(p, o.t0, 0.1); fadeIn(t, o.t0, 0.1);
    if (o.out) { fadeOut(p, o.t1, 0.12); fadeOut(t, o.t1, 0.12); }
    p._w = w; p._h = h; p._t = t;
    if (curScene != "CAPTIONS") R(o.pos[0], o.pos[1], w, h, o.t0, o.t1, o.tag || "VT", str);
    return p;
}
function chip(str, o) {
    var t = mkText(str, { font: F_H, size: o.size, color: o.color || BLACK, pos: o.pos, t0: o.t0, t1: o.t1, maxW: o.maxW || 700, noReg: true });
    var w = o.w || (t._w + 90), h = o.h || (t._h + 56);
    var p = shapeRect(w, h, o.rad || 36, o.bg || WHITE, o.pos, o.t0, o.t1, "chip");
    p.moveAfter(t); t.parent = p; t.position.setValue([0, 0]);
    shadow(p, 60, 14, 40);
    popIn(p, o.t0, 100); fadeIn(p, o.t0, 0.1); fadeIn(t, o.t0, 0.1);
    if (o.out) { fadeOut(p, o.t1, 0.12); fadeOut(t, o.t1, 0.12); }
    p._w = w; p._h = h; p._t = t;
    R(o.pos[0], o.pos[1], w, h, o.t0, o.t1, o.tag || "VT", str);
    return p;
}
function strike(x0, x1, y, th, color, t0, t1, drawDur) {
    var w = x1 - x0, s = comp.layers.addShape(); s.name = "strike";
    var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var r = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Rect");
    r.property("ADBE Vector Rect Size").setValue([w, th]);
    r.property("ADBE Vector Rect Position").setValue([w / 2, 0]);
    r.property("ADBE Vector Rect Roundness").setValue(th / 2);
    var f = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill");
    f.property("ADBE Vector Fill Color").setValue(color);
    s.anchorPoint.setValue([0, 0]); s.position.setValue([x0, y]); span(s, t0, t1);
    kf(s.scale, [t0, t0 + (drawDur || 0.3)], [[0, 100, 100], [100, 100, 100]], 20, 70);
    return s;
}
function ellipseShape(d, fillc, strokec, strokew, pos, t0, t1) {
    var s = comp.layers.addShape(); s.name = "ellipse";
    var g = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var e = g.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Ellipse");
    e.property("ADBE Vector Ellipse Size").setValue([d, d]);
    if (fillc) { var f = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill"); f.property("ADBE Vector Fill Color").setValue(fillc); }
    if (strokec) {
        var st = g.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
        st.property("ADBE Vector Stroke Color").setValue(strokec); st.property("ADBE Vector Stroke Width").setValue(strokew);
    }
    s.position.setValue(pos); span(s, t0, t1);
    return s;
}
function plane(color, color2, sc, t0, t1) {
    var s = comp.layers.addShape(); s.name = "plane";
    var g1 = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var p1 = g1.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Group");
    var sh = new Shape(); sh.vertices = [[80, 0], [-70, -52], [-34, 0], [-70, 52]];
    sh.inTangents = [[0, 0], [0, 0], [0, 0], [0, 0]]; sh.outTangents = [[0, 0], [0, 0], [0, 0], [0, 0]]; sh.closed = true;
    p1.property("ADBE Vector Shape").setValue(sh);
    g1.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill").property("ADBE Vector Fill Color").setValue(color);
    var g2 = s.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var p2 = g2.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Group");
    var sh2 = new Shape(); sh2.vertices = [[-34, 0], [-70, 52], [-6, 20]];
    sh2.inTangents = [[0, 0], [0, 0], [0, 0]]; sh2.outTangents = [[0, 0], [0, 0], [0, 0]]; sh2.closed = true;
    p2.property("ADBE Vector Shape").setValue(sh2);
    g2.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Fill").property("ADBE Vector Fill Color").setValue(color2);
    s.scale.setValue(S(s, sc)); span(s, t0, t1);
    return s;
}

// ---------- media kartalar ----------
function roundMaskAt(l, x, y, w, h, r) {
    var m = l.property("ADBE Mask Parade").addProperty("ADBE Mask Atom");
    var k = r * 0.5523, sh = new Shape();
    sh.vertices = [[x + r, y], [x + w - r, y], [x + w, y + r], [x + w, y + h - r], [x + w - r, y + h], [x + r, y + h], [x, y + h - r], [x, y + r]];
    sh.inTangents = [[-k, 0], [0, 0], [0, -k], [0, 0], [k, 0], [0, 0], [0, k], [0, 0]];
    sh.outTangents = [[0, 0], [k, 0], [0, 0], [0, k], [0, 0], [-k, 0], [0, 0], [0, -k]];
    sh.closed = true;
    m.property("ADBE Mask Shape").setValue(sh);
}
// clipCard: item'ning (sx,sy) nuqtasini kartaning markaziga qo'yib, w x h oyna ko'rsatadi
function clipCard(item, cx, cy, w, h, r, t0, t1, sc, sx, sy, o) {
    o = o || {};
    var iw = item.width, ih = item.height, k = sc / 100;
    var ctrl = comp.layers.addNull(); ctrl.name = "CARD ctrl";
    ctrl.anchorPoint.setValue([0, 0]); ctrl.position.setValue([cx, cy]); span(ctrl, t0, t1);
    var l = comp.layers.add(item);
    l.startTime = t0; l.inPoint = t0; l.outPoint = t1;
    l.scale.setValue(S(l, sc));
    l.parent = ctrl;
    l.position.setValue([-(sx - iw / 2) * k, -(sy - ih / 2) * k]);
    roundMaskAt(l, sx - w / (2 * k), sy - h / (2 * k), w / k, h / k, r / k);
    shadow(l, 60, 18, 60);
    popIn(ctrl, t0, 100); fadeIn(l, t0, 0.1);
    if (o.out) fadeOut(l, t1, 0.14);
    R(cx, cy, w, h, t0, t1, "V", item.name);
    l._ctrl = ctrl;
    return l;
}

// ---------- guide qatlamlar (renderga chiqmaydi) ----------
function gRect(g, x0, y0, x1, y1, col, sw, dash) {
    var grp = g.property("ADBE Root Vectors Group").addProperty("ADBE Vector Group");
    var r = grp.property("ADBE Vectors Group").addProperty("ADBE Vector Shape - Rect");
    r.property("ADBE Vector Rect Size").setValue([x1 - x0, y1 - y0]);
    r.property("ADBE Vector Rect Position").setValue([(x0 + x1) / 2, (y0 + y1) / 2]);
    var st = grp.property("ADBE Vectors Group").addProperty("ADBE Vector Graphic - Stroke");
    st.property("ADBE Vector Stroke Color").setValue(col); st.property("ADBE Vector Stroke Width").setValue(sw);
    if (dash) { try { var d = st.property("ADBE Vector Stroke Dashes").addProperty("ADBE Vector Stroke Dash 1"); d.setValue(dash); } catch (e) { } }
}
function addGuide(c, dur) {
    var prev = comp; comp = c;
    var g = comp.layers.addShape(); g.name = "ZONA GUIDE (render qilinmaydi)";
    g.position.setValue([0, 0]);
    gRect(g, OUTER.x0, OUTER.y0, OUTER.x1, OUTER.y1, [1, 0.24, 0.24], 3);                 // qizil: umumiy xavfsiz
    gRect(g, SAFE.x0, SAFE.y0, SAFE.x1, SAFE.y1, [0.16, 0.75, 0.35], 2);                  // yashil: kontent
    gRect(g, 70, 1455, 1010, 1545, [1, 0.67, 0], 2);                                      // sariq: caption
    gRect(g, 70, ZN.titleTop, 1010, ZN.titleBot, [0.2, 0.4, 1], 2, 14);                   // ko'k: sarlavha zonasi
    gRect(g, 70, ZN.visTop, 1010, ZN.visBot, [0.2, 0.4, 1], 2, 14);                       // ko'k: vizual zona
    gRect(g, 890, 956, 1080, 1560, [1, 0.24, 0.24], 2, 8);                                // o'ng tugmalar
    gRect(g, LOGO.x0, LOGO.y0, LOGO.x1, LOGO.y1, [0.7, 0.3, 1], 2, 8);                  // logo zonasi
    g.guideLayer = true; g.label = 1; g.outPoint = dur;
    comp = prev;
}
function newScene(name) {
    var c = proj.items.addComp(name, W, H, 1, DUR, FPS);
    c.parentFolder = FSC; c.bgColor = [1, 1, 1];
    comp = c; curScene = name; addGuide(c, DUR);
    return c;
}
function endScene(c, t0, t1) {
    var l = MAIN.layers.add(c);
    l.startTime = 0; l.inPoint = t0; l.outPoint = t1; l.name = c.name;
    return l;
}
function runScene(name, t0, t1, fn) {
    try { var c = newScene(name); fn(c); endScene(c, t0, t1); L("OK " + name); }
    catch (e) { L("ERR " + name + " : " + e.toString() + " @" + e.line); }
}

// ---------- avtomatik tekshiruv ----------
function runChecks() {
    var issues = [], i, j, a, b;
    for (i = 0; i < REG.length; i++) {
        a = REG[i];
        var x0 = a.cx - a.w / 2, x1 = a.cx + a.w / 2, y0 = a.cy - a.h / 2, y1 = a.cy + a.h / 2;
        if (x0 < OUTER.x0 - 2 || x1 > OUTER.x1 + 2 || y0 < OUTER.y0 - 2 || y1 > OUTER.y1 + 2)
            issues.push(a.sc + ": ZONADAN CHIQDI [" + a.name + "] x" + Math.round(x0) + "-" + Math.round(x1) + " y" + Math.round(y0) + "-" + Math.round(y1));
        if ((a.tag == "TT" || a.tag == "T" || a.tag == "VT") && y1 > BTN.y0 && x1 > BTN.x0 + 2) issues.push(a.sc + ": TUGMALAR zonasi [" + a.name + "] x1=" + Math.round(x1));
        if (a.tag == "TT" && y0 < LOGO.y1 && x1 > LOGO.x0 + 2) issues.push(a.sc + ": LOGO zonasi [" + a.name + "]");
        if (a.tag == "TT" && y1 > ZN.titleBot + 2) issues.push(a.sc + ": sarlavha vizual zonaga kirdi [" + a.name + "] y1=" + Math.round(y1));
        if (a.tag == "V" && y0 < ZN.visTop - 2 && a.sc != "CAPTIONS") issues.push(a.sc + ": vizual sarlavha zonasiga kirdi [" + a.name + "] y0=" + Math.round(y0));
    }
    for (i = 0; i < REG.length; i++) for (j = i + 1; j < REG.length; j++) {
        a = REG[i]; b = REG[j];
        if (a.sc != b.sc) continue;
        var ot = Math.min(a.t1, b.t1) - Math.max(a.t0, b.t0);
        if (ot < 0.3) continue;
        var ox = Math.min(a.cx + a.w / 2, b.cx + b.w / 2) - Math.max(a.cx - a.w / 2, b.cx - b.w / 2);
        var oy = Math.min(a.cy + a.h / 2, b.cy + b.h / 2) - Math.max(a.cy - a.h / 2, b.cy - b.h / 2);
        if (ox <= 0 || oy <= 0) continue;
        var ar = ox * oy, small = Math.min(a.w * a.h, b.w * b.h);
        if (ar / small < 0.03) continue;
        // karta ichidagi element (nomida "karta"/"card") — ataylab ustma-ust, xato emas
        var big = (a.w * a.h >= b.w * b.h) ? a : b, sm = (big === a) ? b : a;
        if ((big.name.indexOf("karta") >= 0 || big.name.indexOf("card") >= 0) && Math.abs(ar - sm.w * sm.h) < 4) continue;
        issues.push(a.sc + ": USTMA-UST [" + a.name + "] & [" + b.name + "] " + Math.round(100 * ar / small) + "%");
    }
    L("TEKSHIRUV: " + REG.length + " element, " + issues.length + " muammo");
    for (i = 0; i < issues.length; i++) L("  ! " + issues[i]);
}
