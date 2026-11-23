var comp = null, seq = null;
for (var i = 1; i <= app.project.numItems; i++) {
    var it = app.project.item(i);
    if (it instanceof CompItem && it.name == "Reel_PR") comp = it;
    if (it instanceof FootageItem && /^f_\[0001-0150\]\.png$/.test(it.name)) seq = it;
    if (!seq && it instanceof FootageItem && it.name.indexOf("f_[") == 0) seq = it;
}
if (!seq) throw new Error("matte sequence topilmadi");
for (var n = comp.numLayers; n >= 1; n--) { if (comp.layer(n).name.indexOf("mil_") == 0) comp.layer(n).remove(); }
var vid = null, shade = null;
for (var m = 1; m <= comp.numLayers; m++) { var nm = comp.layer(m).name; if (nm == "Footage") vid = comp.layer(m); if (nm == "Caption shade") shade = comp.layer(m); }
try { seq.mainSource.conformFrameRate = 50; } catch (e) {}
var T0 = 20.4, T1 = 23.4, TS = 20.5, TE = 23.25;

// 1) text (Reels safe zone: x 64..960)
var tx = comp.layers.addText("MILLION"); tx.name = "mil_text";
var tp = tx.property("Source Text"), td = tp.value;
td.resetCharStyle(); td.fontSize = 360;
try { td.font = "DINCondensed-Bold"; } catch (e) {}
td.fillColor = [1, 1, 1]; td.applyFill = true; td.applyStroke = false;
td.justification = ParagraphJustification.CENTER_JUSTIFY; td.tracking = 20;
tp.setValue(td);
var r = tx.sourceRectAtTime(0, false);
var fs = 360 * 860 / r.width; td = tp.value; td.fontSize = fs; tp.setValue(td);
r = tx.sourceRectAtTime(0, false);
// vertical centre of caps at y=600: text baseline = 600 + capHeight/2 (scaled)
tx.property("Transform").property("Position").setValue([512, 500 - (r.top + r.height / 2) * 1.3]);
tx.inPoint = TS - 0.05; tx.outPoint = TE;
tx.property("Transform").property("Scale").expression =
    'var p = ease(time, ' + TS + ', ' + (TS + 0.5) + ', 0.86, 1);\n' +
    '[100 * p, 130 * p]';
var op = tx.property("Transform").property("Opacity");
op.setValueAtTime(TS - 0.05, 0); op.setValueAtTime(TS + 0.3, 100); op.setValueAtTime(TE - 0.2, 100); op.setValueAtTime(TE, 0);

// 2) person cutout above text, with luma matte from Vision segmentation
var cut = vid.duplicate(); cut.name = "mil_cutout"; cut.audioEnabled = false;
cut.inPoint = T0; cut.outPoint = T1;
var mt = comp.layers.add(seq); mt.name = "mil_matte";
mt.startTime = T0; mt.inPoint = T0; mt.outPoint = T1;
mt.property("Transform").property("Scale").expression = 'thisComp.layer("Footage").transform.scale';
cut.setTrackMatte(mt, TrackMatteType.LUMA);

// 3) stacking: shade, matte, cutout, text, footage (top -> bottom)
tx.moveBefore(vid);
cut.moveBefore(tx);
mt.moveBefore(cut);
if (shade) shade.moveBefore(mt);
mt.moveBefore(cut);
"ok layers=" + comp.numLayers + " font=" + tx.property("Source Text").value.font + " fs=" + fs.toFixed(0);
