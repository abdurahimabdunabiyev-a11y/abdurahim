var T = eval("(" + '__T__' + ")");
var comp = null, pop = null, whoosh = null;
for (var i = 1; i <= app.project.numItems; i++) {
    var it = app.project.item(i);
    if (it instanceof CompItem && it.name == "Reel_PR") comp = it;
    if (it instanceof FootageItem) { if (it.name == "pop.wav") pop = it; if (it.name == "whoosh.wav") whoosh = it; }
}
for (var n = comp.numLayers; n >= 1; n--) {
    var nm = comp.layer(n).name;
    if (nm.indexOf("gx_") == 0 || nm.indexOf("sfx_gx") == 0) comp.layer(n).remove();
}
// Instagram Reels safe zone (1080x1920): x 64..960, y 270..1540, centre x = 512
var CXS = 512;
function ease(prop) {
    for (var k = 1; k <= prop.numKeys; k++) {
        var e = new KeyframeEase(0, 65), d = (prop.value instanceof Array) ? prop.value.length : 1, a = [], b = [];
        for (var j = 0; j < d; j++) { a.push(e); b.push(e); }
        try { prop.setTemporalEaseAtKey(k, a, b); } catch (x) {}
    }
}
var WHITE = [1, 1, 1], DARK = [0.07, 0.07, 0.07], GREY = [0.42, 0.42, 0.44];
function addFill(g, color, opacity) {
    var f = g.property("Contents").addProperty("ADBE Vector Graphic - Fill");
    f.property("Color").setValue(color);
    if (opacity !== undefined) f.property("Opacity").setValue(opacity);
}
function shapeL(name, kind, w, h, round, color, x, y, opacity) {
    var L = comp.layers.addShape(); L.name = "gx_" + name;
    var g = L.property("Contents").addProperty("ADBE Vector Group");
    var path = g.property("Contents").addProperty(kind == "ellipse" ? "ADBE Vector Shape - Ellipse" : "ADBE Vector Shape - Rect");
    path.property("Size").setValue([w, h]);
    if (kind == "rect") path.property("Roundness").setValue(round);
    addFill(g, color, opacity);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
function personL(name, x, y, color) {
    var L = comp.layers.addShape(); L.name = "gx_" + name;
    var g = L.property("Contents").addProperty("ADBE Vector Group");
    var head = g.property("Contents").addProperty("ADBE Vector Shape - Ellipse");
    head.property("Size").setValue([46, 46]); head.property("Position").setValue([0, -34]);
    var body = g.property("Contents").addProperty("ADBE Vector Shape - Rect");
    body.property("Size").setValue([92, 54]); body.property("Roundness").setValue(27); body.property("Position").setValue([0, 22]);
    addFill(g, color);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
// icon tile: white rounded square + dark glyph (star / play / target)
function tileL(name, glyph, x, y) {
    var L = comp.layers.addShape(); L.name = "gx_" + name;
    var C = L.property("Contents");
    // glyph groups first (they end up on top), tile background last (bottom)
    var g2 = C.addProperty("ADBE Vector Group");
    if (glyph == "target") {
        var e1 = g2.property("Contents").addProperty("ADBE Vector Shape - Ellipse"); e1.property("Size").setValue([78, 78]);
        var st = g2.property("Contents").addProperty("ADBE Vector Graphic - Stroke");
        st.property("Color").setValue(DARK); st.property("Stroke Width").setValue(9);
        var g3 = C.addProperty("ADBE Vector Group");
        var e2 = g3.property("Contents").addProperty("ADBE Vector Shape - Ellipse"); e2.property("Size").setValue([30, 30]);
        addFill(g3, DARK);
    } else {
        var s = g2.property("Contents").addProperty("ADBE Vector Shape - Star");
        if (glyph == "star") {
            s.property("Type").setValue(1); s.property("Points").setValue(5);
            s.property("Outer Radius").setValue(46); s.property("Inner Radius").setValue(21);
        } else {
            s.property("Type").setValue(2); s.property("Points").setValue(3);
            s.property("Outer Radius").setValue(40); s.property("Rotation").setValue(90);
            s.property("Position").setValue([6, 0]);
        }
        addFill(g2, DARK);
    }
    var g1 = C.addProperty("ADBE Vector Group");
    var r = g1.property("Contents").addProperty("ADBE Vector Shape - Rect");
    r.property("Size").setValue([150, 150]); r.property("Roundness").setValue(38);
    addFill(g1, WHITE, 95);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
function textL(name, txt, size, color, just, x, y) {
    var L = comp.layers.addText(txt); L.name = "gx_" + name;
    var tp = L.property("Source Text"), td = tp.value;
    td.resetCharStyle(); td.fontSize = size;
    try { td.font = "HelveticaNeue-Bold"; } catch (e) {}
    td.fillColor = color; td.applyFill = true; td.applyStroke = false; td.justification = just; td.tracking = -10;
    tp.setValue(td);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
function textW(L) { return L.sourceRectAtTime(0, false).width; }
function anim(L, tIn, tOut, dy, sFrom, base) {
    var bk = (base || 100) / 100;
    var tr = L.property("Transform"), pos = tr.property("Position"), p = pos.value;
    var op = tr.property("Opacity");
    op.setValueAtTime(0, 0); op.setValueAtTime(tIn, 0); op.setValueAtTime(tIn + 0.12, 100);
    if (tOut) { op.setValueAtTime(tOut - 0.15, 100); op.setValueAtTime(tOut, 0); }
    if (dy) { pos.setValueAtTime(tIn, [p[0], p[1] + dy]); pos.setValueAtTime(tIn + 0.22, [p[0], p[1]]); ease(pos); }
    if (sFrom) {
        var sc = tr.property("Scale");
        sc.setValueAtTime(tIn, [sFrom * bk, sFrom * bk]); sc.setValueAtTime(tIn + 0.12, [108 * bk, 108 * bk]); sc.setValueAtTime(tIn + 0.24, [100 * bk, 100 * bk]); ease(sc);
    }
}
function sfx(src, t, db, name) {
    var L = comp.layers.add(src); L.name = "sfx_gx_" + name; L.startTime = Math.max(0, t);
    L.property("Audio").property("Audio Levels").setValue([db, db]);
}
var CENTER = ParagraphJustification.CENTER_JUSTIFY, LEFT = ParagraphJustification.LEFT_JUSTIFY;

// ---------- A) 5 kishi
var yA = 1400, tA = T.five, tAm = T.bemalol, tAx = T.oladiEnd;
var icons = [];
for (var a = 0; a < 5; a++) {
    var P = personL("p" + a, CXS + (a - 2) * 150, yA, WHITE);
    var ti = tA + a * 0.1;
    anim(P, ti, (a == 2) ? tAx : 0, 40, 70);
    sfx(pop, ti - 0.02, -20, "p" + a);
    icons.push(P);
    if (a != 2) {
        var pr = P.property("Transform").property("Position");
        var pv = pr.valueAtTime(tAm - 0.01, false);
        pr.setValueAtTime(tAm, pv);
        pr.setValueAtTime(tAm + 0.4, [CXS, yA]);
        ease(pr);
        var op2 = P.property("Transform").property("Opacity");
        op2.setValueAtTime(tAm + 0.25, 100); op2.setValueAtTime(tAm + 0.4, 0);
    }
}
sfx(whoosh, tAm - 0.1, -16, "merge");
var mid = icons[2].property("Transform").property("Scale");
mid.setValueAtTime(tAm, [100, 100]); mid.setValueAtTime(tAm + 0.3, [150, 150]); ease(mid);
var aiBg = shapeL("ai_bg", "rect", 92, 52, 26, WHITE, CXS + 92, yA - 70);
var aiT = textL("ai_txt", "AI", 32, DARK, CENTER, CXS + 92, yA - 70 + 11);
anim(aiBg, tAm + 0.3, tAx, 20, 70); anim(aiT, tAm + 0.3, tAx, 20, 70);
sfx(pop, tAm + 0.3, -14, "ai");

// ---------- B) AI vositalar: oqim chizig'i + tugunlar (nomlar faqat shu yerda)
function glyphNode(name, kind, x, y) {
    var L = comp.layers.addShape(); L.name = "gx_" + name;
    var C = L.property("Contents");
    var g = C.addProperty("ADBE Vector Group");
    var G = g.property("Contents");
    if (kind == "bubble") {
        var rr = G.addProperty("ADBE Vector Shape - Rect");
        rr.property("Size").setValue([58, 44]); rr.property("Roundness").setValue(16); rr.property("Position").setValue([0, -5]);
        var tri = G.addProperty("ADBE Vector Shape - Star");
        tri.property("Type").setValue(2); tri.property("Points").setValue(3); tri.property("Outer Radius").setValue(12);
        tri.property("Rotation").setValue(180); tri.property("Position").setValue([-14, 24]);
    } else if (kind == "burst") {
        var st = G.addProperty("ADBE Vector Shape - Star");
        st.property("Type").setValue(1); st.property("Points").setValue(8);
        st.property("Outer Radius").setValue(32); st.property("Inner Radius").setValue(11);
    } else if (kind == "sparkle") {
        var sp = G.addProperty("ADBE Vector Shape - Star");
        sp.property("Type").setValue(1); sp.property("Points").setValue(4);
        sp.property("Outer Radius").setValue(36); sp.property("Inner Radius").setValue(9);
    } else {
        var bp = G.addProperty("ADBE Vector Shape - Group");
        var sh = new Shape();
        sh.vertices = [[-3, -34], [-21, 6], [-4, 6], [-11, 34], [21, -10], [4, -10], [13, -34]];
        sh.closed = true;
        bp.property("Path").setValue(sh);
    }
    addFill(g, DARK);
    var bgG = C.addProperty("ADBE Vector Group");
    var el = bgG.property("Contents").addProperty("ADBE Vector Shape - Ellipse");
    el.property("Size").setValue([124, 124]);
    addFill(bgG, WHITE, 96);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
function ringL(name, x, y) {
    var L = comp.layers.addShape(); L.name = "gx_" + name;
    var g = L.property("Contents").addProperty("ADBE Vector Group");
    var el = g.property("Contents").addProperty("ADBE Vector Shape - Ellipse");
    el.property("Size").setValue([124, 124]);
    var st = g.property("Contents").addProperty("ADBE Vector Graphic - Stroke");
    st.property("Color").setValue(WHITE); st.property("Stroke Width").setValue(5);
    L.property("Transform").property("Position").setValue([x, y]);
    return L;
}
var tools = [["ChatGPT", "bubble", T.chatgpt], ["Claude", "burst", T.claude], ["Nano Banana Pro", "sparkle", T.nano], ["Flux", "bolt", T.flux]];
var tBout = T.tayyorEnd, yB = 1330, labY = 1462;
var LOGO_FILE = { bubble: "openai.svg", burst: "claude.svg", sparkle: "googlegemini.svg", bolt: "flux_logo.png" };
var LOGO_SCALE = { bubble: 267, burst: 267, sparkle: 267, bolt: 25.6 };
var LOGO_COLOR = { bubble: [0.07, 0.07, 0.07], burst: [0.851, 0.467, 0.341], sparkle: [0.192, 0.525, 1], bolt: [0.07, 0.07, 0.07] };
var LOGO_ITEM = {};
for (var li = 1; li <= app.project.numItems; li++) { var lit = app.project.item(li); if (lit instanceof FootageItem && /^(openai|claude|googlegemini)\.svg$|^flux_logo\.png$/.test(lit.name)) LOGO_ITEM[lit.name] = lit; }
var bx = []; for (var b0 = 0; b0 < 4; b0++) bx.push(CXS + (b0 - 1.5) * 210);
// chiziqlar (tugunlar ostida)
for (var l = 0; l < 3; l++) {
    var ln = comp.layers.addShape(); ln.name = "gx_line" + l;
    var lg = ln.property("Contents").addProperty("ADBE Vector Group");
    var lr = lg.property("Contents").addProperty("ADBE Vector Shape - Rect");
    lr.property("Size").setValue([210, 6]); lr.property("Roundness").setValue(3); lr.property("Position").setValue([105, 0]);
    addFill(lg, WHITE, 90);
    ln.property("Transform").property("Position").setValue([bx[l], yB]);
    var tNext = tools[l + 1][2] - 0.05;
    var lsc = ln.property("Transform").property("Scale");
    lsc.setValueAtTime(0, [0, 100]); lsc.setValueAtTime(tNext - 0.42, [0, 100]); lsc.setValueAtTime(tNext, [100, 100]);
    ease(lsc);
    var lop = ln.property("Transform").property("Opacity");
    lop.setValueAtTime(0, 100); lop.setValueAtTime(tBout - 0.15, 100); lop.setValueAtTime(tBout, 0);
}
for (var b = 0; b < tools.length; b++) {
    var tb = tools[b][2] - 0.05;
    var lname = LOGO_FILE[tools[b][1]], node;
    if (lname && LOGO_ITEM[lname]) {
        node = shapeL("node" + b, "ellipse", 124, 124, 0, WHITE, bx[b], yB, 96);
        anim(node, tb, tBout, 0, 60);
        var LG = comp.layers.add(LOGO_ITEM[lname]);
        LG.name = "gx_logo" + b;
        if (LG.canSetCollapseTransformation) LG.collapseTransformation = true;
        LG.property("Transform").property("Position").setValue([bx[b], yB]);
        var LS = LOGO_SCALE[tools[b][1]];
        LG.property("Transform").property("Scale").setValue([LS, LS]);
        var lfx = LG.property("Effects").addProperty("ADBE Fill");
        lfx.property("Color").setValue(LOGO_COLOR[tools[b][1]]);
        anim(LG, tb, tBout, 0, 60, LS);
    } else {
        node = glyphNode("node" + b, tools[b][1], bx[b], yB);
        anim(node, tb, tBout, 0, 60);
    }
    var ring = ringL("ring" + b, bx[b], yB);
    var rop = ring.property("Transform").property("Opacity"), rsc = ring.property("Transform").property("Scale");
    rop.setValueAtTime(0, 0); rop.setValueAtTime(tb - 0.01, 0); rop.setValueAtTime(tb, 70); rop.setValueAtTime(tb + 0.5, 0);
    rsc.setValueAtTime(tb, [100, 100]); rsc.setValueAtTime(tb + 0.5, [185, 185]); ease(rsc);
    var lab = textL("lab" + b, tools[b][0], 30, WHITE, CENTER, bx[b], labY);
    anim(lab, tb + 0.08, tBout, 24, 0);
    sfx(pop, tb, -16, "tool" + b);
}

// ---------- D) brend / kontent / reklama: 3D vektor ikonkalar
var ICON = {};
for (var ii = 1; ii <= app.project.numItems; ii++) { var iit = app.project.item(ii); if (iit instanceof FootageItem && /^flat_(brand|content|ads|sales|one)\.svg$/.test(iit.name)) ICON[iit.name] = iit; }
var tags = [["flat_brand.svg", T.brend, 190, 1395, 0], ["flat_content.svg", T.kontent, 405, 1395, 0], ["flat_ads.svg", T.reklama, 619, 1395, 0], ["flat_sales.svg", T.sales, 834, 1395, 0]];
var yD = 1395, tConv = T.komandasiz - 0.02, tDout = T.yuritamanEnd, IS = 42;
function icon3d(file, x, y, rot) {
    var L = comp.layers.add(ICON[file]); L.name = "gx_" + file.replace(".svg", "");
    if (L.canSetCollapseTransformation) L.collapseTransformation = true;
    L.property("Transform").property("Position").setValue([x, y]);
    L.property("Transform").property("Rotation").setValue(rot);
    return L;
}
for (var e2 = 0; e2 < tags.length; e2++) {
    var tg = tags[e2][1] - 0.05;
    var tile = icon3d(tags[e2][0], tags[e2][2], tags[e2][3], tags[e2][4]);
    anim(tile, tg, 0, 60, 40, IS);
    var rr = tile.property("Transform").property("Rotation");
    var rb = tags[e2][4];
    rr.setValueAtTime(tg, rb - 14); rr.setValueAtTime(tg + 0.3, rb + 2); rr.setValueAtTime(tg + 0.45, rb); ease(rr);
    var pp = tile.property("Transform").property("Position"), p0 = pp.valueAtTime(tConv - 0.01, false);
    pp.setValueAtTime(tConv, p0); pp.setValueAtTime(tConv + 0.35, [512, yD]); ease(pp);
    rr.setValueAtTime(tConv, rb); rr.setValueAtTime(tConv + 0.35, 0);
    var oo = tile.property("Transform").property("Opacity");
    oo.setValueAtTime(tConv + 0.2, 100); oo.setValueAtTime(tConv + 0.35, 0);
    var ss = tile.property("Transform").property("Scale");
    ss.setValueAtTime(tConv, [IS, IS]); ss.setValueAtTime(tConv + 0.35, [IS * 0.45, IS * 0.45]); ease(ss);
    sfx(pop, tg, -16, "tag" + e2);
}
var one = icon3d("flat_one.svg", 512, yD, 0);
anim(one, tConv + 0.3, tDout, 0, 55, 46);
var orr = one.property("Transform").property("Rotation");
orr.setValueAtTime(tConv + 0.3, -10); orr.setValueAtTime(tConv + 0.6, 0); ease(orr);
sfx(whoosh, tConv - 0.05, -16, "conv"); sfx(pop, tConv + 0.32, -14, "one");
"gx layers=" + comp.numLayers;
