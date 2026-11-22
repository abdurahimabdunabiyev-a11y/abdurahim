"""Blender (Cycles) — to'liq qora quyosh paneli, studiya: oltin nur ramka bo'ylab, sayoz fokus.
blender -b -P sahna.py -- --kadr 30 --out test_####.png  (yoki --anim)"""
import bpy, math, sys, os
from mathutils import Vector
argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
def arg(k, d): return argv[argv.index(k) + 1] if k in argv else d
D = os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.device = 'CPU'; sc.cycles.samples = int(arg('--samples', 64))
sc.cycles.use_denoising = True
try: sc.cycles.denoiser = 'OPENIMAGEDENOISE'
except Exception: pass
sc.render.resolution_x, sc.render.resolution_y = 1080, 1920; sc.render.resolution_percentage = int(arg('--foiz', 100))
FPS = 25; sc.render.fps = FPS; sc.frame_start, sc.frame_end = 1, int(arg('--oxiri', 250))
sc.view_settings.view_transform = 'AgX'; sc.view_settings.look = 'AgX - Punchy'
sc.cycles.max_bounces = 6; sc.cycles.caustics_reflective = False; sc.cycles.caustics_refractive = False
w = bpy.data.worlds.new('W'); sc.world = w; w.use_nodes = True; wn = w.node_tree.nodes; wl = w.node_tree.links
bgc = wn['Background']; bgc.inputs[0].default_value = (0, 0, 0, 1)
# faqat akslarda ko'rinadigan studiya muhiti (kameraga qora)
tcd = wn.new('ShaderNodeTexCoord'); sep = wn.new('ShaderNodeSeparateXYZ'); ramp = wn.new('ShaderNodeValToRGB')
ramp.color_ramp.elements[0].position = .3; ramp.color_ramp.elements[0].color = (0, 0, 0, 1)
ramp.color_ramp.elements[1].position = .62; ramp.color_ramp.elements[1].color = (1., .72, .45, 1)
env = wn.new('ShaderNodeBackground'); env.inputs[1].default_value = .35
lp = wn.new('ShaderNodeLightPath'); mx = wn.new('ShaderNodeMixShader')
wl.new(tcd.outputs['Generated'], sep.inputs[0]); wl.new(sep.outputs['Z'], ramp.inputs[0]); wl.new(ramp.outputs[0], env.inputs[0])
wl.new(lp.outputs['Is Camera Ray'], mx.inputs[0]); wl.new(env.outputs[0], mx.inputs[1]); wl.new(bgc.outputs[0], mx.inputs[2])
wl.new(mx.outputs[0], wn['World Output'].inputs[0])
ENV = env

def mat(name, base, metal=0., rough=.3, coat=0., img=None, emis=None, es=0.):
    m = bpy.data.materials.new(name); m.use_nodes = True; n = m.node_tree.nodes; b = n['Principled BSDF']
    b.inputs['Base Color'].default_value = (*base, 1); b.inputs['Metallic'].default_value = metal; b.inputs['Roughness'].default_value = rough
    b.inputs['Coat Weight'].default_value = coat; b.inputs['Coat Roughness'].default_value = .02
    if img:
        t = n.new('ShaderNodeTexImage'); t.image = bpy.data.images.load(img); m.node_tree.links.new(t.outputs[0], b.inputs['Base Color'])
    if emis:
        b.inputs['Emission Color'].default_value = (*emis, 1); b.inputs['Emission Strength'].default_value = es
    return m

PW, PH, PT, FW = 1.10, 2.35, .030, .018   # Ronma SKYMAX: 2382 x 1134 x 30 mm
# shisha yuza (hujayralar)
bpy.ops.mesh.primitive_plane_add(size=1); face = bpy.context.object; face.scale = (PW, PH, 1); face.location.z = PT / 2 - .004
face.data.materials.append(mat('shisha', (0, 0, 0), 0, .06, 1., img=os.path.join(D, 'ronma_hujayra.png')))
bpy.ops.object.transform_apply(scale=True)
# orqa list
bpy.ops.mesh.primitive_cube_add(size=1); back = bpy.context.object; back.scale = (PW, PH, PT * .5); back.data.materials.append(mat('orqa', (.01, .01, .01), 0, .6))
# ramka (anodlangan qora alyuminiy, faska bilan)
frm = mat('ramka', (.72, .73, .75), 1., .32)   # kumush anodlangan alyuminiy
parts = [((PW + 2 * FW, FW, PT), (0, PH / 2 + FW / 2, 0)), ((PW + 2 * FW, FW, PT), (0, -PH / 2 - FW / 2, 0)),
         ((FW, PH, PT), (PW / 2 + FW / 2, 0, 0)), ((FW, PH, PT), (-PW / 2 - FW / 2, 0, 0))]
fr = []
for s, l in parts:
    bpy.ops.mesh.primitive_cube_add(size=1, location=l); o = bpy.context.object; o.scale = s; bpy.ops.object.transform_apply(scale=True)
    bv = o.modifiers.new('bv', 'BEVEL'); bv.width = .004; bv.segments = 3; o.data.materials.append(frm); fr.append(o)
bpy.ops.object.empty_add(location=(0, 0, 0)); panel = bpy.context.object
for o in [face, back] + fr: o.parent = panel

# yorug'lik: oltin chiziqli nur (ingichka area light) ramka bo'ylab yuguradi
bpy.ops.object.light_add(type='AREA', location=(0, PH / 2 + .12, .25)); strip = bpy.context.object
strip.data.shape = 'RECTANGLE'; strip.data.size = .5; strip.data.size_y = .015; strip.data.energy = 60; strip.data.color = (1., .62, .28)
strip.rotation_euler = (math.radians(-35), 0, 0); strip.parent = panel; strip.visible_camera = False
# orqa kontur nur (rim) va yumshoq kalit nur
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, -2.2)); wall = bpy.context.object; wall.data.materials.append(mat('devor', (.03, .025, .02), 0, .8))
bpy.ops.object.light_add(type='AREA', location=(0, .2, -.35)); rim = bpy.context.object; rim.data.size = 1.0; rim.data.energy = 0; rim.data.color = (1., .5, .16)
rim.visible_camera = False
bpy.ops.object.light_add(type='AREA', location=(0, 3.0, 5.0)); soft = bpy.context.object; soft.data.size = 4.0; soft.data.energy = 120; soft.data.color = (1., .78, .55)
soft.rotation_euler = (math.radians(-30), 0, 0); soft.visible_camera = False; soft.visible_glossy = False
bpy.ops.object.light_add(type='AREA', location=(1.8, 2.2, 2.4)); key = bpy.context.object; key.data.size = 1.2; key.data.energy = 40; key.data.color = (1., .8, .6)
key.rotation_euler = (math.radians(-40), math.radians(35), 0); key.visible_camera = False; key.visible_glossy = False

# ramka qirrasidagi oltin yaltiroq (emissiv ingichka silindr, ramka ustki tashqi qirrasida sirpanadi)
glintM = bpy.data.materials.new('glint'); glintM.use_nodes = True; gn = glintM.node_tree.nodes; gn.clear()
em = gn.new('ShaderNodeEmission'); em.inputs[0].default_value = (1., .62, .25, 1); em.inputs[1].default_value = 60
out = gn.new('ShaderNodeOutputMaterial'); glintM.node_tree.links.new(em.outputs[0], out.inputs[0])
bpy.ops.mesh.primitive_cylinder_add(radius=.0016, depth=.38, location=(0, PH / 2 + FW, PT / 2), rotation=(0, math.radians(90), 0)); glint = bpy.context.object
glint.data.materials.append(glintM); glint.parent = panel
glint2 = glint.copy(); glint2.data = glint.data.copy(); bpy.context.collection.objects.link(glint2); glint2.parent = panel; glint2.scale = (.6, .6, .5)
bpy.ops.object.shade_smooth()
strip.data.energy = 0; strip.hide_render = True
# yorug'lik tarqalishi (glow) kompozitorda
sc.use_nodes = True; ct = sc.node_tree; rl = ct.nodes['Render Layers']; co = ct.nodes['Composite']
gl = ct.nodes.new('CompositorNodeGlare'); gl.glare_type = 'FOG_GLOW'; gl.quality = 'HIGH'; gl.threshold = .9; gl.size = 8
ct.links.new(rl.outputs['Image'], gl.inputs['Image']); ct.links.new(gl.outputs['Image'], co.inputs['Image'])
# kamera
bpy.ops.object.camera_add(); cam = bpy.context.object; sc.camera = cam; cam.data.lens = 50
cam.data.dof.use_dof = True; cam.data.dof.aperture_fstop = 1.8
bpy.ops.object.empty_add(location=(0, 0, 0)); tgt = bpy.context.object
cam.data.dof.focus_object = tgt

def ease(x): x = min(1, max(0, x)); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
def lerp(a, b, k): return a + (b - a) * k
V = arg('--variant', 'oltin')
if V == 'oq':        # yorug' showroom: och kulrang studiya, neytral oq yorug'lik
    bgc.inputs[0].default_value = (.42, .44, .47, 1); ENV.inputs[1].default_value = 1.0
    ramp.color_ramp.elements[1].color = (1, 1, 1, 1); ramp.color_ramp.elements[0].color = (.25, .26, .28, 1)
    wall.data.materials[0].node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (.55, .56, .58, 1)
    for L in (soft, key): L.data.color = (1, 1, 1)
    glint.hide_render = glint2.hide_render = True; gl.threshold = 1.5
elif V == 'quyosh':  # quyosh botishi: Nishita osmon (Y-yuqori sahnaga burilgan), yer, quyosh nuri
    # qo'lda yasalgan quyosh botishi osmoni (dunyo Y — yuqori): ufqda to'q sariq, tepada to'q ko'k
    wn.remove(mx); sp2 = wn.new('ShaderNodeSeparateXYZ'); wl.new(tcd.outputs['Generated'], sp2.inputs[0])
    rr = wn.new('ShaderNodeValToRGB'); E = rr.color_ramp.elements
    E[0].position, E[0].color = .44, (.05, .03, .02, 1); E[1].position, E[1].color = .95, (.02, .04, .12, 1)
    for pos, col in ((.5, (1., .42, .12, 1)), (.53, (1., .6, .3, 1)), (.6, (.75, .42, .38, 1)), (.72, (.18, .2, .38, 1))):
        e = E.new(pos); e.color = col
    wl.new(sp2.outputs['Y'], rr.inputs[0])
    sb = wn.new('ShaderNodeBackground'); sb.inputs[1].default_value = 1.4; wl.new(rr.outputs[0], sb.inputs[0]); wl.new(sb.outputs[0], wn['World Output'].inputs[0])
    wall.hide_render = True
    bpy.ops.mesh.primitive_plane_add(size=400, location=(0, -PH / 2 - .9, 0), rotation=(math.radians(-90), 0, 0)); grd = bpy.context.object
    grd.data.materials.append(mat('yer', (.035, .04, .025), 0, .9)); grd.hide_render = True
    sc.render.film_transparent = True; sc.render.image_settings.color_mode = 'RGBA'   # fon — haqiqiy quyosh botishi videosi (ffmpeg'da)
    bpy.ops.object.light_add(type='SUN', location=(0, 5, -5)); sun = bpy.context.object; sun.data.energy = 3.5; sun.data.color = (1, .55, .28); sun.data.angle = math.radians(1.5)
    sun.rotation_euler = (math.radians(-170), math.radians(-25), 0)
    glint.hide_render = glint2.hide_render = True; gl.threshold = 1.2
TT = float(arg('--davom', 10))
def at(f):
    t = (f - 1) / FPS
    if t < 3.0:      # A: logo va "RONMA SOLAR" yaqindan
        u = t / 3.0
        panel.rotation_euler = (math.radians(-12), math.radians(32), 0); bpy.context.view_layer.update(); M = panel.matrix_world
        cam.location = M @ Vector((-.05 + .1 * u, .5, 1.0 - .18 * u)); tgt.location = M @ Vector((.12 + .05 * u, .52, 0))
        glint.location = (lerp(-PW / 2 + .19, PW / 2 - .19, ease(u)), PH / 2 + FW, PT / 2); glint2.location = (9, 9, 9)
        rimE, keyE, softE, envE, fs, ln = 0, 6, 30, .25, 2.8, 45
    elif t < 6.0:    # B: texnik yozuvlar bo'ylab pastga sirpanish
        u = (t - 3.0) / 3.0
        panel.rotation_euler = (math.radians(-8), math.radians(-30), 0); bpy.context.view_layer.update(); M = panel.matrix_world
        cam.location = M @ Vector((lerp(-.75, -.35, u), lerp(.32, -.02, u), .55)); tgt.location = M @ Vector((lerp(-.3, -.12, u), lerp(.28, -.06, u), 0))
        glint.location = (9, 9, 9); glint2.location = (lerp(-PW / 2 + .12, PW / 2 - .12, ease(u)), 0, PT / 2 + .001)
        rimE, keyE, softE, envE, fs, ln = 0, 7, 35, .28, 3.2, 45
    else:            # C: kafolat nishonidan orqaga tortilib, butun panel, sekin burilish
        k = ease((t - 6.0) / 2.4); u = (t - 6.0) / (TT - 6.0)
        panel.rotation_euler = (math.radians(lerp(-6, 0, k)), math.radians(lerp(28, -12, k) + 14 * ease(max(0, (t - 8.0) / (TT - 8.0)))), 0)
        bpy.context.view_layer.update(); M = panel.matrix_world
        cam.location = (M @ Vector((-.35, -.42, .7))).lerp(Vector((0, .05, 5.3 - .25 * u)), k); tgt.location = (M @ Vector((-.3, -.43, 0))).lerp(Vector((0, .1, 0)), k)
        glint.location = (lerp(-PW / 2 + .19, PW / 2 - .19, ((t - 6) * .45) % 1), PH / 2 + FW, PT / 2); glint2.location = (9, 9, 9)
        rimE, keyE, softE, envE, fs, ln = lerp(0, 450, k), lerp(6, 22, k), lerp(30, 130, k), .22, lerp(3.2, 6.3, k), 45
    if V == 'oq': rimE, keyE, softE, envE = 0, keyE * 3, softE * 2.5, 1.0
    if V == 'quyosh': rimE, keyE, softE, envE = 0, keyE * 1.6, softE * 1.3, envE
    rim.data.energy, key.data.energy, soft.data.energy, ENV.inputs[1].default_value = rimE, keyE, softE, envE
    cam.data.dof.aperture_fstop, cam.data.lens = fs, ln
    fw = (tgt.location - cam.location).normalized(); zc = -fw; xc = Vector((0, 1, 0)).cross(zc).normalized(); yc = zc.cross(xc)
    from mathutils import Matrix
    cam.rotation_euler = Matrix((xc, yc, zc)).transposed().to_euler()   # dunyo Y — yuqori (matn to'g'ri turadi)

for f in range(sc.frame_start, sc.frame_end + 1):
    at(f)
    for o in (panel, cam, tgt, glint, glint2, rim, key): o.keyframe_insert('location', frame=f); o.keyframe_insert('rotation_euler', frame=f)
    for dta, p in ((strip.data, 'energy'), (rim.data, 'energy'), (key.data, 'energy'), (soft.data, 'energy'), (cam.data.dof, 'aperture_fstop'), (cam.data, 'lens'), (ENV.inputs[1], 'default_value')):
        dta.keyframe_insert(p, frame=f)

sc.render.filepath = os.path.join(D, arg('--out', 'kadr_####'))
sc.render.image_settings.file_format = 'PNG'; sc.render.use_overwrite = False; sc.render.use_placeholder = True
if '--anim' in argv: bpy.ops.render.render(animation=True)
else:
    sc.frame_set(int(arg('--kadr', 30))); bpy.ops.render.render(write_still=True)
