var GROUPS = eval("(" + '__GROUPS__' + ")");
var comp = null, pop = null, whoosh = null, boom = null;
for (var i = 1; i <= app.project.numItems; i++) {
    var it = app.project.item(i);
    if (it instanceof CompItem && it.name == "Reel_PR") comp = it;
    if (it instanceof FootageItem) {
        if (it.name == "pop.wav") pop = it;
        if (it.name == "whoosh.wav") whoosh = it;
        if (it.name == "boom.wav") boom = it;
    }
}
for (var n = comp.numLayers; n >= 1; n--) { if (/^sfx_(pop|whoosh|boom)_/.test(comp.layer(n).name)) comp.layer(n).remove(); }
var vid = null;
for (var m = 1; m <= comp.numLayers; m++) { if (comp.layer(m).name == "Footage") vid = comp.layer(m); }
var sc = vid.property("Transform").property("Scale");
while (sc.numKeys > 0) sc.removeKey(1);

function ease(prop) {
    for (var k = 1; k <= prop.numKeys; k++) {
        var e = new KeyframeEase(0, 60);
        try { prop.setTemporalEaseAtKey(k, [e, e, e], [e, e, e]); } catch (x) {}
    }
}
function gs(g) { return GROUPS[g][0].s; }
function heroStart(g) { for (var p = 0; p < GROUPS[g].length; p++) { if (GROUPS[g][p].k == "hero") return GROUPS[g][p].s; } return GROUPS[g][0].s; }

var ZI = [1, 5, 8, 12, 16, 19, 23, 25, 29];
var ZOOM = 111;
sc.setValueAtTime(0, [100, 100]);
for (var z = 0; z < ZI.length; z++) {
    var tin = gs(ZI[z]) - 0.05;
    var og = ZI[z] + 2;
    var tout = (og < GROUPS.length) ? gs(og) : comp.duration - 0.5;
    sc.setValueAtTime(tin, [100, 100]);
    sc.setValueAtTime(tin + 0.3, [ZOOM, ZOOM]);
    sc.setValueAtTime(tout - 0.05, [ZOOM, ZOOM]);
    sc.setValueAtTime(tout + 0.35, [100, 100]);
}
ease(sc);

"zoom ok layers=" + comp.numLayers;
