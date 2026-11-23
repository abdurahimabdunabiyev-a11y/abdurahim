var comp = null, pop = null, whoosh = null;
for (var i = 1; i <= app.project.numItems; i++) {
    var it = app.project.item(i);
    if (it instanceof CompItem && it.name == "Reel_PR") comp = it;
    if (it instanceof FootageItem) { if (it.name == "pop.wav") pop = it; if (it.name == "whoosh.wav") whoosh = it; }
}
for (var n = comp.numLayers; n >= 1; n--) { var nm = comp.layer(n).name; if (nm.indexOf("gm_") == 0 || nm.indexOf("sfx_gm") == 0 || nm.indexOf("fs_") == 0 || nm.indexOf("sfx_fs") == 0) comp.layer(n).remove(); }
var T0 = 19.6, TOUT = 23.3;
var BLUE_TXT = [0.66, 0.8, 1], WHITE = [1, 1, 1];
function ease(prop) {
    for (var k = 1; k <= prop.numKeys; k++) {
        var e = new KeyframeEase(0, 65), d = (prop.value instanceof Array) ? prop.value.length : 1, a = [], b = [];
        for (var j = 0; j < d; j++) { a.push(e); b.push(e); }
        try { prop.setTemporalEaseAtKey(k, a, b); } catch (x) {}
    }
}
function span(L, tIn, tOut) { L.inPoint = tIn; L.outPoint = tOut; }
function show(L, tIn, tOut, dy, sFrom, fade) {
    var f = fade || 0.2;
    var tr = L.property("Transform"), pos = tr.property("Position"), p = pos.value, op = tr.property("Opacity");
    op.setValueAtTime(tIn, 0); op.setValueAtTime(tIn + f, 100);
    op.setValueAtTime(tOut - 0.2, 100); op.setValueAtTime(tOut, 0);
    if (dy) { pos.setValueAtTime(tIn, [p[0], p[1] + dy]); pos.setValueAtTime(tIn + 0.5, [p[0], p[1]]); ease(pos); }
    if (sFrom) {
        var sc = tr.property("Scale");
        sc.setValueAtTime(tIn, [sFrom, sFrom]); sc.setValueAtTime(tIn + 0.32, [102, 102]); sc.setValueAtTime(tIn + 0.52, [100, 100]); ease(sc);
    }
    span(L, tIn, tOut);
}
function rectL(name, w, h, round, color, op, x, y) {
    var L = comp.layers.addShape(); L.name = "fs_" + name;
    var g = L.property("Contents").addProperty("ADBE Vector Group");
    var r = g.property("Contents").addProperty("ADBE Vector Shape - Rect");
    r.property("Size").setValue([w, h]); r.property("Roundness").setValue(round);
    var f = g.property("Contents").addProperty("ADBE Vector Graphic - Fill");
    f.property("Color").setValue(color); f.property("Opacity").setValue(op);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
function glassL(name, w, h, round, fillColor, fillOp, x, y) {
    var L = rectL(name, w, h, round, fillColor, fillOp, x, y);
    var g = L.property("Contents").property(1);
    var sk = g.property("Contents").addProperty("ADBE Vector Graphic - Stroke");
    sk.property("Color").setValue([0.7, 0.82, 1]); sk.property("Stroke Width").setValue(2.5); sk.property("Opacity").setValue(45);
    return L;
}
function textL(name, txt, size, color, just, x, y) {
    var L = comp.layers.addText(txt); L.name = "fs_" + name;
    var tp = L.property("Source Text"), td = tp.value;
    td.resetCharStyle(); td.fontSize = size;
    try { td.font = "HelveticaNeue-Bold"; } catch (e) {}
    td.fillColor = color; td.applyFill = true; td.applyStroke = false; td.justification = just; td.tracking = -15;
    tp.setValue(td);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
function sfx(src, t, db, name) {
    var L = comp.layers.add(src); L.name = "sfx_fs_" + name; L.startTime = Math.max(0, t);
    L.property("Audio").property("Audio Levels").setValue([db, db]);
}
var FMT = 'var v = Math.round(effect("Slider Control")("Slider")) * 1000;\nvar s = String(v), r = "";\nfor (var i = 0; i < s.length; i++) { if (i > 0 && (s.length - i) % 3 == 0) r += " "; r += s.charAt(i); }\nr';
function counterL(name, size, just, x, y, t0, t1, val) {
    var L = textL(name, "0", size, WHITE, just, x, y);
    var sl = L.property("Effects").addProperty("ADBE Slider Control"); sl.name = "Slider Control";
    var sp = sl.property("Slider"); sp.setValueAtTime(t0, 0); sp.setValueAtTime(t1, val); ease(sp);
    L.property("Source Text").expression = FMT;
    return L;
}

// ---------- background (blue gradient world)
var bg = comp.layers.addSolid([0.015, 0.04, 0.17], "fs_bg", 1080, 1920, 1, comp.duration);
span(bg, T0, TOUT);
var bo = bg.property("Transform").property("Opacity");
bo.setValueAtTime(T0, 0); bo.setValueAtTime(T0 + 0.22, 100); bo.setValueAtTime(TOUT - 0.2, 100); bo.setValueAtTime(TOUT, 0);
function glow(name, cx, cy, rad, col, op, dx, dy) {
    var L = comp.layers.addSolid([0, 0, 0], "fs_" + name, 1080, 1920, 1, comp.duration);
    var fx = L.property("Effects").addProperty("ADBE Ramp");
    fx.property("ADBE Ramp-0002").setValue(col);
    fx.property("ADBE Ramp-0004").setValue([0, 0, 0, 1]);
    fx.property("ADBE Ramp-0005").setValue(2);
    var st = fx.property("ADBE Ramp-0001"), en = fx.property("ADBE Ramp-0003");
    st.setValueAtTime(T0, [cx, cy]); st.setValueAtTime(TOUT, [cx + dx, cy + dy]);
    en.setValueAtTime(T0, [cx + rad, cy]); en.setValueAtTime(TOUT, [cx + dx + rad, cy + dy]);
    L.blendingMode = BlendingMode.SCREEN;
    var o = L.property("Transform").property("Opacity");
    o.setValueAtTime(T0, 0); o.setValueAtTime(T0 + 0.3, op); o.setValueAtTime(TOUT - 0.2, op); o.setValueAtTime(TOUT, 0);
    span(L, T0, TOUT);
    return L;
}
glow("glow1", 250, 420, 900, [0.12, 0.38, 1, 1], 100, 180, 160);
glow("glow2", 880, 1180, 760, [0.2, 0.52, 1, 1], 85, -200, -180);
glow("glow3", 540, 1780, 620, [0.5, 0.76, 1, 1], 65, 100, -240);

// ---------- title
var tt = textL("title", "Marketing jamoasi", 66, WHITE, ParagraphJustification.CENTER_JUSTIFY, 512, 345);
var ts = textL("sub", "oyiga ketadigan xarajat", 38, BLUE_TXT, ParagraphJustification.CENTER_JUSTIFY, 512, 405);
show(tt, T0 + 0.15, TOUT, 50, 92); show(ts, T0 + 0.28, TOUT, 40, 0);

// ---------- rows
var rows = [["Montajor", 10], ["Targetolog", 5], ["Dizayner", 5], ["Kopirayter", 4], ["SMM menejer", 10]];
var RY0 = 520, RS = 140, R0 = T0 + 0.3, RG = 0.3;
for (var r = 0; r < rows.length; r++) {
    var ry = RY0 + r * RS, tr0 = R0 + r * RG, val = rows[r][1] * 1000;
    var card = glassL("row" + r, 832, 120, 40, [0.05, 0.15, 0.45], 66, 512, ry);
    show(card, tr0, TOUT, 70, 92);
    var nm2 = textL("name" + r, rows[r][0], 44, WHITE, ParagraphJustification.LEFT_JUSTIFY, 134, ry - 6);
    show(nm2, tr0 + 0.05, TOUT, 70, 0);
    var track = rectL("track" + r, 380, 10, 5, [1, 1, 1], 16, 134 + 190, ry + 32);
    show(track, tr0 + 0.05, TOUT, 70, 0);
    var bw = 380 * rows[r][1] / 10;
    var bar = rectL("bar" + r, bw, 10, 5, [0.62, 0.8, 1], 100, 134, ry + 32 + 70);
    bar.property("Contents").property(1).property("Contents").property(1).property("Position").setValue([bw / 2, 0]);
    // bar anchored at layer origin (left edge): slide with the row, grow left to right
    var bpos = bar.property("Transform").property("Position");
    bpos.setValueAtTime(tr0 + 0.05, [134, ry + 32 + 70]); bpos.setValueAtTime(tr0 + 0.55, [134, ry + 32]); ease(bpos);
    var bs = bar.property("Transform").property("Scale");
    bs.setValueAtTime(tr0 + 0.3, [0, 100]); bs.setValueAtTime(tr0 + 1.0, [100, 100]); ease(bs);
    var bop = bar.property("Transform").property("Opacity");
    bop.setValueAtTime(tr0 + 0.05, 0); bop.setValueAtTime(tr0 + 0.25, 100); bop.setValueAtTime(TOUT - 0.2, 100); bop.setValueAtTime(TOUT, 0);
    span(bar, tr0 + 0.05, TOUT);
    var am = counterL("amt" + r, 54, ParagraphJustification.RIGHT_JUSTIFY, 898, ry + 18, tr0 + 0.15, tr0 + 0.95, val);
    show(am, tr0 + 0.05, TOUT, 70, 0);
    sfx(pop, tr0 - 0.02, -17, "row" + r);
}
// ---------- total
var tT = R0 + rows.length * RG + 0.25;
var tc = glassL("total", 832, 260, 52, [0.1, 0.32, 0.95], 80, 512, 1335);
show(tc, tT, TOUT, 80, 90);
var tl = textL("tlabel", "Jami", 38, BLUE_TXT, ParagraphJustification.CENTER_JUSTIFY, 512, 1262);
show(tl, tT + 0.1, TOUT, 40, 0);
var tn = counterL("tcount", 124, ParagraphJustification.CENTER_JUSTIFY, 512, 1382, tT + 0.2, tT + 1.2, 34000);
show(tn, tT + 0.1, TOUT, 60, 90);
var tm = textL("tsom", "so'm", 42, BLUE_TXT, ParagraphJustification.CENTER_JUSTIFY, 512, 1443);
show(tm, tT + 0.3, TOUT, 30, 0);
sfx(whoosh, T0 - 0.1, -14, "in");
sfx(whoosh, tT - 0.1, -16, "total");
sfx(pop, tT + 1.2, -12, "done");
"ok layers=" + comp.numLayers + " tT=" + tT.toFixed(2);
