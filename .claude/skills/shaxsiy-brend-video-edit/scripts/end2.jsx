var comp = null, A = null, B = null, pop = null, whoosh = null;
for (var i = 1; i <= app.project.numItems; i++) {
    var it = app.project.item(i);
    if (it instanceof CompItem && it.name == "Reel_PR") comp = it;
    if (it instanceof FootageItem) {
        if (it.name == "card_a2.png") A = it;
        if (it.name == "card_b2.png") B = it;
        if (it.name == "pop.wav") pop = it;
        if (it.name == "whoosh.wav") whoosh = it;
    }
}
for (var n = comp.numLayers; n >= 1; n--) {
    var nm = comp.layer(n).name;
    if (nm.indexOf("ig_") == 0 || nm.indexOf("sfx_ig") == 0 || nm.indexOf("end_") == 0 || nm.indexOf("sfx_end") == 0) comp.layer(n).remove();
}
// Reels safe zone: card 612x333 at y 1193..1527, centre x 512
var S = 56, CX = 512, CY = 1360;
var T0 = 36.1, TP = 38.0;
function ease(prop) {
    for (var k = 1; k <= prop.numKeys; k++) {
        var e = new KeyframeEase(0, 65), d = (prop.value instanceof Array) ? prop.value.length : 1, a = [], b = [];
        for (var j = 0; j < d; j++) { a.push(e); b.push(e); }
        try { prop.setTemporalEaseAtKey(k, a, b); } catch (x) {}
    }
}
function place(L) {
    var tr = L.property("Transform");
    tr.property("Position").setValueAtTime(T0, [CX, CY + 300]);
    tr.property("Position").setValueAtTime(T0 + 0.8, [CX, CY]);
    ease(tr.property("Position"));
    var sc = tr.property("Scale");
    sc.setValueAtTime(T0, [S * 0.88, S * 0.88]);
    sc.setValueAtTime(T0 + 0.55, [S * 1.035, S * 1.035]);
    sc.setValueAtTime(T0 + 0.85, [S, S]);
    sc.setValueAtTime(TP, [S, S]);
    sc.setValueAtTime(TP + 0.12, [S * 0.965, S * 0.965]);
    sc.setValueAtTime(TP + 0.38, [S * 1.03, S * 1.03]);
    sc.setValueAtTime(TP + 0.65, [S, S]);
    ease(sc);
}
var la = comp.layers.add(A); la.name = "end_card_obuna"; place(la);
var oa = la.property("Transform").property("Opacity");
oa.setValueAtTime(0, 0); oa.setValueAtTime(T0, 0); oa.setValueAtTime(T0 + 0.35, 100);
oa.setValueAtTime(TP + 0.16, 100); oa.setValueAtTime(TP + 0.17, 0);
var lb = comp.layers.add(B); lb.name = "end_card_rahmat"; place(lb);
var ob = lb.property("Transform").property("Opacity");
ob.setValueAtTime(0, 0); ob.setValueAtTime(TP + 0.02, 0); ob.setValueAtTime(TP + 0.16, 100);

// ripple on the + button (image px -> comp px)
var k = S / 100;
var bx = CX + (884 - 546.5) * k, by = CY + (446 - 297.5) * k;
var rp = comp.layers.addShape(); rp.name = "end_ripple";
var g = rp.property("Contents").addProperty("ADBE Vector Group");
var el = g.property("Contents").addProperty("ADBE Vector Shape - Ellipse"); el.property("Size").setValue([130 * k, 130 * k]);
var st = g.property("Contents").addProperty("ADBE Vector Graphic - Stroke");
st.property("Color").setValue([0.96, 0.7, 0.95]); st.property("Stroke Width").setValue(4);
rp.property("Transform").property("Position").setValue([bx, by]);
var ro = rp.property("Transform").property("Opacity"), rs = rp.property("Transform").property("Scale");
ro.setValueAtTime(0, 0); ro.setValueAtTime(TP - 0.01, 0); ro.setValueAtTime(TP, 85); ro.setValueAtTime(TP + 0.7, 0);
rs.setValueAtTime(TP, [60, 60]); rs.setValueAtTime(TP + 0.7, [170, 170]); ease(rs);

function sfx(src, t, db, name) {
    var L = comp.layers.add(src); L.name = "sfx_end_" + name; L.startTime = Math.max(0, t);
    L.property("Audio").property("Audio Levels").setValue([db, db]);
}
sfx(whoosh, T0 - 0.15, -12, "whoosh");
sfx(pop, TP - 0.02, -10, "pop");
sfx(pop, TP + 0.26, -14, "check");
"ok layers=" + comp.numLayers + " scale=" + S.toFixed(1);
