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
sc.render.fps = 30; sc.frame_start, sc.frame_end = 1, int(arg('--oxiri', 180))
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

PW, PH, PT, FW = 1.134, 2.278, .035, .028
# shisha yuza (hujayralar)
bpy.ops.mesh.primitive_plane_add(size=1); face = bpy.context.object; face.scale = (PW, PH, 1); face.location.z = PT / 2 - .004
face.data.materials.append(mat('shisha', (0, 0, 0), 0, .06, 1., img=os.path.join(D, 'hujayra.png')))
bpy.ops.object.transform_apply(scale=True)
# orqa list
bpy.ops.mesh.primitive_cube_add(size=1); back = bpy.context.object; back.scale = (PW, PH, PT * .5); back.data.materials.append(mat('orqa', (.01, .01, .01), 0, .6))
# ramka (anodlangan qora alyuminiy, faska bilan)
frm = mat('ramka', (.015, .015, .016), 1., .28)
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
soft.rotation_euler = (math.radians(-30), 0, 0); soft.visible_camera = False
bpy.ops.object.light_add(type='AREA', location=(1.8, 2.2, 2.4)); key = bpy.context.object; key.data.size = 1.2; key.data.energy = 40; key.data.color = (1., .8, .6)
key.rotation_euler = (math.radians(-40), math.radians(35), 0); key.visible_camera = False

# ramka qirrasidagi oltin yaltiroq (emissiv ingichka silindr, ramka ustki tashqi qirrasida sirpanadi)
glintM = bpy.data.materials.new('glint'); glintM.use_nodes = True; gn = glintM.node_tree.nodes; gn.clear()
em = gn.new('ShaderNodeEmission'); em.inputs[0].default_value = (1., .62, .25, 1); em.inputs[1].default_value = 60
out = gn.new('ShaderNodeOutputMaterial'); glintM.node_tree.links.new(em.outputs[0], out.inputs[0])
bpy.ops.mesh.primitive_cylinder_add(radius=.0016, depth=.38, location=(0, PH / 2 + FW, PT / 2), rotation=(0, math.radians(90), 0)); glint = bpy.context.object
glint.data.materials.append(glintM); glint.parent = panel
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
tc = cam.constraints.new('TRACK_TO'); tc.target = tgt; tc.track_axis = 'TRACK_NEGATIVE_Z'; tc.up_axis = 'UP_Y'
cam.data.dof.focus_object = tgt

def ease(x): x = min(1, max(0, x)); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2
def lerp(a, b, k): return a + (b - a) * k
def at(f):
    t = (f - 1) / 30; k = ease((t - 2.4) / 2.6)
    panel.rotation_euler = (math.radians(lerp(-72, 0, k)), math.radians(lerp(28, -16 + 3 * math.sin(t * .6), k)), math.radians(lerp(10, 0, k)))
    # yaqin: chap-yuqori burchak; uzoq: butun panel
    bpy.context.view_layer.update()
    M = panel.matrix_world
    near_cam = M @ Vector((float(arg('--kx', -.95)) + t * .03, PH / 2 + float(arg('--ky', .35)), float(arg('--kz', .8))))   # burchak ustida, yuzaga past (sirpanuvchi) burchak
    near_tgt = M @ Vector((-PW / 2 + .25 + t * .05, PH / 2 - .35, 0))
    far_cam = Vector((.0, .1, 5.3))
    cam.location = near_cam.lerp(far_cam, k)
    tgt.location = near_tgt.lerp(Vector((0, .15, 0)), k)
    glint.location.x = lerp(-PW / 2 - .1, PW / 2 + .1, (t * .45) % 1)
    strip.data.energy = lerp(40, 12, k); rim.data.energy = lerp(0, 450, k); key.data.energy = lerp(4, 25, k); soft.data.energy = lerp(25, 140, k)
    ENV.inputs[1].default_value = lerp(.22, .2, k)
    cam.data.dof.aperture_fstop = lerp(2.8, 5.6, k); cam.data.lens = lerp(40, 45, k)

for f in range(sc.frame_start, sc.frame_end + 1):
    at(f)
    for o in (panel, cam, tgt, glint, rim, key): o.keyframe_insert('location', frame=f); o.keyframe_insert('rotation_euler', frame=f)
    for dta, p in ((strip.data, 'energy'), (rim.data, 'energy'), (key.data, 'energy'), (soft.data, 'energy'), (cam.data.dof, 'aperture_fstop'), (cam.data, 'lens'), (ENV.inputs[1], 'default_value')):
        dta.keyframe_insert(p, frame=f)

sc.render.filepath = os.path.join(D, arg('--out', 'kadr_####'))
sc.render.image_settings.file_format = 'PNG'
if '--anim' in argv: bpy.ops.render.render(animation=True)
else:
    sc.frame_set(int(arg('--kadr', 30))); bpy.ops.render.render(write_still=True)
