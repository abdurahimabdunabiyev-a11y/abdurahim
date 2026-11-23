var GROUPS = eval("(" + '__GROUPS__' + ")");
var comp = null, foot = null;
for (var i = 1; i <= app.project.numItems; i++) {
    var it = app.project.item(i);
    if (it instanceof CompItem && it.name == "Reel_PR") comp = it;
    if (it instanceof FootageItem && it.name == "Video PR.mp4") foot = it;
}
if (!comp || !foot) { throw new Error("comp/footage topilmadi"); }
while (comp.numLayers > 0) { comp.layer(1).remove(); }
var vid = comp.layers.add(foot);
vid.name = "Footage";
var shade = comp.layers.addSolid([0, 0, 0], "Caption shade", 1080, 1920, 1, comp.duration);
var mk = shade.property("Masks").addProperty("Mask");
var shp = new Shape();
shp.vertices = [[-300, 900], [1400, 900], [1400, 2300], [-300, 2300]];
shp.closed = true;
mk.property("Mask Path").setValue(shp);
mk.property("Mask Feather").setValue([0, 700]);
shade.property("Transform").property("Opacity").setValue(55);

var FONT = "HelveticaNeue-Bold";
var HERO_SIZE = 150, HERO_MAXW = 860, SMALL_PRE = 54, SMALL_POST = 50;
var HERO_Y = 1090;
var CXS = 512; // Reels safe zone centre (x 64..960)
var usedFont = "";

function mkText(name, txt, size, just, tracking) {
    var L = comp.layers.addText(txt);
    L.name = name;
    var tp = L.property("Source Text");
    var td = tp.value;
    td.resetCharStyle();
    td.fontSize = size;
    try { td.font = FONT; } catch (e) {}
    td.fillColor = [1, 1, 1];
    td.applyFill = true;
    td.applyStroke = false;
    td.justification = just;
    td.tracking = tracking;
    tp.setValue(td);
    usedFont = tp.value.font;
    return L;
}
function ease(prop) {
    for (var k = 1; k <= prop.numKeys; k++) {
        var e = new KeyframeEase(0, 70);
        var n = (prop.value instanceof Array) ? prop.value.length : 1;
        var ins = [], outs = [];
        for (var d = 0; d < n; d++) { ins.push(e); outs.push(e); }
        try { prop.setTemporalEaseAtKey(k, ins, outs); } catch (x) {}
    }
}
function shadow(L) {
    return;
    try {
        var fx = L.property("Effects").addProperty("ADBE Drop Shadow");
        fx.property(2).setValue(200);
        fx.property(3).setValue(180);
        fx.property(4).setValue(3);
        fx.property(5).setValue(30);
    } catch (e) {}
}
function animate(L, x, y, t0, t1, isHero) {
    L.startTime = 0;
    L.inPoint = t0;
    L.outPoint = t1;
    var op = L.property("Transform").property("Opacity");
    op.setValueAtTime(t0, 0);
    op.setValueAtTime(t0 + 0.1, 100);
    op.setValueAtTime(Math.max(t0 + 0.12, t1 - 0.04), 100);
    op.setValueAtTime(t1, 0);
    var pos = L.property("Transform").property("Position");
    pos.setValueAtTime(t0, [x, y + (isHero ? 34 : 20)]);
    pos.setValueAtTime(t0 + 0.16, [x, y]);
    ease(pos);
    var sc = L.property("Transform").property("Scale");
    if (isHero) {
        sc.setValueAtTime(t0, [80, 80]);
        sc.setValueAtTime(t0 + 0.09, [106, 106]);
        sc.setValueAtTime(t0 + 0.2, [100, 100]);
    } else {
        sc.setValueAtTime(t0, [88, 88]);
        sc.setValueAtTime(t0 + 0.15, [100, 100]);
    }
    ease(sc);
    shadow(L);
}

var made = 0;
for (var g = 0; g < GROUPS.length; g++) {
    var parts = GROUPS[g];
    var firstS = parts[0].s, lastE = parts[parts.length - 1].e;
    var nextS = (g + 1 < GROUPS.length) ? GROUPS[g + 1][0].s : null;
    var t1 = (nextS !== null) ? Math.min(nextS, lastE + 0.45) : lastE + 0.35;
    var hero = null, heroW = 0, heroSize = HERO_SIZE;
    for (var p = 0; p < parts.length; p++) {
        if (parts[p].k == "hero") {
            var H = mkText("hero_" + g, parts[p].t, HERO_SIZE, ParagraphJustification.CENTER_JUSTIFY, -35);
            var r = H.sourceRectAtTime(0, false);
            if (r.width > HERO_MAXW) {
                heroSize = HERO_SIZE * HERO_MAXW / r.width;
                var tp2 = H.property("Source Text"); var td2 = tp2.value; td2.fontSize = heroSize; tp2.setValue(td2);
                r = H.sourceRectAtTime(0, false);
            }
            heroW = r.width;
            H.property("Transform").property("Position").setValue([CXS, HERO_Y]);
            animate(H, CXS, HERO_Y, parts[p].s - 0.02, t1, true);
            made++;
        }
    }
    var capH = heroSize * 0.72;
    for (var q = 0; q < parts.length; q++) {
        if (parts[q].k == "pre") {
            var x0 = CXS - heroW / 2;
            var yP = HERO_Y - capH - 20;
            var P = mkText("pre_" + g, parts[q].t, SMALL_PRE, ParagraphJustification.LEFT_JUSTIFY, -15);
            P.property("Transform").property("Position").setValue([x0, yP]);
            animate(P, x0, yP, parts[q].s - 0.02, t1, false);
            made++;
        } else if (parts[q].k == "post") {
            var x1 = CXS + heroW / 2;
            var yQ = HERO_Y + SMALL_POST + 12;
            var Q = mkText("post_" + g, parts[q].t, SMALL_POST, ParagraphJustification.RIGHT_JUSTIFY, -15);
            Q.property("Transform").property("Position").setValue([x1, yQ]);
            animate(Q, x1, yQ, parts[q].s - 0.02, t1, false);
            made++;
        }
    }
}
"made=" + made + " font=" + usedFont + " layers=" + comp.numLayers;
