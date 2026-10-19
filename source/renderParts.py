"""Render only accepted meshes. Run from repository root with Blender."""
import bpy, os
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
material=bpy.data.materials.new('Graphite');material.diffuse_color=(0.12,0.18,0.23,1)
for name,location in [('corrected-rack-section',(0,0,0)),('keeper-0p25',(116,60,0)),('lower-cap-0p20',(116,20,0)),('lower-cap-0p20',(132,20,0))]:
 bpy.ops.wm.stl_import(filepath=os.path.abspath('models/'+name+'.stl'))
 obj=bpy.context.object;obj.location=location;obj.data.materials.append(material)
bpy.ops.object.camera_add(location=(210,-220,240))
camera=bpy.context.object;camera.rotation_euler=(Vector((70,53,10))-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.type='ORTHO';camera.data.ortho_scale=190
scene=bpy.context.scene;scene.camera=camera;scene.render.engine='BLENDER_WORKBENCH'
scene.display.shading.light='STUDIO';scene.display.shading.color_type='MATERIAL';scene.display.shading.show_shadows=True;scene.display.shading.show_cavity=True;scene.display.shading.cavity_type='BOTH';scene.display.shading.background_type='WORLD';scene.world.color=(0.75,0.75,0.75)
scene.render.resolution_x=1400;scene.render.resolution_y=1100;scene.render.resolution_percentage=100;scene.render.image_settings.file_format='PNG';scene.render.use_stamp=False
os.makedirs('images',exist_ok=True);scene.render.filepath=os.path.abspath('images/acceptedParts.png');bpy.ops.render.render(write_still=True)

# Retain pixels and standard display metadata only, never EXIF or text fields.
import struct
with open(scene.render.filepath,'rb') as handle: data=handle.read()
clean=data[:8];offset=8
while offset<len(data):
 length=struct.unpack_from('>I',data,offset)[0];kind=data[offset+4:offset+8]
 if kind in (b'IHDR',b'IDAT',b'IEND',b'sRGB',b'gAMA',b'cHRM',b'pHYs'): clean+=data[offset:offset+length+12]
 offset+=length+12
with open(scene.render.filepath,'wb') as handle: handle.write(clean)
