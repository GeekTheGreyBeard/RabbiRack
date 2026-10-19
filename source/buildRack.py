# RabbiRack accepted-part generator. Run in Blender background mode.
import bpy,bmesh,math,os,json,struct
from mathutils import Vector,Matrix
OUT=os.path.abspath(os.environ.get('RABBIRACK_OUTPUT', 'build'))
os.makedirs(OUT,exist_ok=True)
import bpy, math, os, json
from mathutils import Vector, Matrix
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
for d in bpy.data.materials: bpy.data.materials.remove(d)
def mat(n,c,metal=0):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=.36;return m
gray=mat('Graphite PLA+',(.065,.085,.105)); trim=mat('Light gray trim',(.50,.59,.63)); orange=mat('r1 envelope — nominal dimensions only',(.96,.16,.025)); teal=mat('Removable joint keys',(.02,.48,.48)); black=mat('Screen placeholder',(.012,.025,.035)); ground=mat('Background',(.80,.83,.85)); white=mat('Labels',(.035,.065,.085))
def box(n,loc,size,ma=None,bev=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=n;o.dimensions=size;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 if ma:o.data.materials.append(ma)
 if bev: mod=o.modifiers.new('Soft edges','BEVEL');mod.width=bev;mod.segments=3;o.modifiers.new('Normals','WEIGHTED_NORMAL')
 return o
def boolean(o,c):
 bpy.context.view_layer.objects.active=o;mod=o.modifiers.new('Machined cavity','BOOLEAN');mod.object=c;mod.operation='DIFFERENCE';bpy.ops.object.modifier_apply(modifier=mod.name);bpy.data.objects.remove(c,do_unlink=True)
def cyl(n,loc,r,depth,verts=32):
 bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc);o=bpy.context.object;o.name=n;return o
def poly(n,pts,z0,z1,ma=None):
 vs=[(x,y,z) for z in [z0,z1] for x,y in pts];k=len(pts);fs=[tuple(reversed(range(k))),tuple(range(k,2*k))]+[(i,(i+1)%k,(i+1)%k+k,i+k) for i in range(k)];me=bpy.data.meshes.new(n);me.from_pydata(vs,[],fs);me.update();o=bpy.data.objects.new(n,me);bpy.context.collection.objects.link(o)
 if ma:o.data.materials.append(ma)
 return o
P=[(-8,-7),(-2,-4),(2,-4),(8,-7),(8,7),(2,4),(-2,4),(-8,7)]

OUT=os.path.abspath(os.environ.get('RABBIRACK_OUTPUT', 'build'))
os.makedirs(OUT,exist_ok=True)
rawpoly=poly
def poly(n,pts,z0,z1,ma=None):
 area=sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(pts,pts[1:]+pts[:1]))
 return rawpoly(n,list(reversed(pts)) if area<0 else pts,z0,z1,ma)
def join(a,b):
 bpy.context.view_layer.objects.active=a;m=a.modifiers.new('Solid union','BOOLEAN');m.operation='UNION';m.solver='EXACT';m.object=b;bpy.ops.object.modifier_apply(modifier=m.name);bpy.data.objects.remove(b,do_unlink=True)
def cube(n,x0,x1,y0,y1,z0,z1):return box(n,((x0+x1)/2,(y0+y1)/2,(z0+z1)/2),(x1-x0,y1-y0,z1-z0),gray)
def offset(pts,d):
 lines=[]
 for p,q in zip(pts,pts[1:]+pts[:1]):
  dx,dy=q[0]-p[0],q[1]-p[1];l=math.hypot(dx,dy);lines.append(((p[0]-dy/l*d,p[1]+dx/l*d),(dx,dy)))
 out=[]
 for i in range(len(pts)):
  (a,u),(b,v)=lines[i-1],lines[i];cross=u[0]*v[1]-u[1]*v[0];t=((b[0]-a[0])*v[1]-(b[1]-a[1])*v[0])/cross;out.append((a[0]+t*u[0],a[1]+t*u[1]))
 return out
joints=[(0,22,False),(0,84,False),(106,22,False),(106,84,False),(22,0,True),(84,0,True),(22,106,True),(84,106,True)]
f=cube('Rack section',0,106,0,106,0,10)
boolean(f,cube('Opening',12,94,12,94,-1,11))
for bounds in [(0,15,35,75),(42,75,91,106),(91,106,48.3,72.3),(48.3,72.3,0,15)]:boolean(f,cube('Access',*bounds,3,11))
for b in [(10,96,49.5,56.5,0,6),(49.5,56.5,10,96,0,6)]:join(f,cube('Rear support',*b))
bpy.ops.mesh.primitive_cone_add(vertices=4,radius1=3.5*math.sqrt(2),radius2=12*math.sqrt(2),depth=8.5,location=(53,53,9.25),rotation=(0,0,math.pi/4));join(f,bpy.context.object)
join(f,cube('Contact pad',41,65,41,65,13.4,14))
for x in [34,76]:
 join(f,cube('Lower shoe',x-4,x+4,8,14,0,27.6))
 boolean(f,cube('Lower cap socket',x-2,x+2,9,12,21.4,28))
for cx,cy,rot in joints:
 pts=[(cx+(y if rot else x),cy+(x if rot else y)) for x,y in P]
 boolean(f,poly('Key socket',pts,5.2,11))
 hx=cx+(5 if cx==0 else -5 if cx==106 else 0);hy=cy+(5 if cy==0 else -5 if cy==106 else 0)
 boolean(f,cyl('Optional M3 through',(hx,hy,5),1.7,12))
 boolean(f,cyl('Rear M3 nut trap',(hx,hy,1.25),5.9/math.sqrt(3),2.7,6))
boolean(f,cube('Keeper socket',30.9,39.1,96.9,103.1,3.8,11))
for lo,hi in [(10,13.4),(92.6,96)]:
 join(f,cube('Side guide',lo,hi,30,34,0,23))
parts={'rack-section':f}
for gap in [.15,.25,.35]:
 k=poly('Joint key '+str(gap),offset(P,gap),0,4.4,teal)
 for x in [-5,5]:boolean(k,cyl('M3 clearance',(x,0,2),1.7,6))
 parts['key-'+str(gap).replace('.','p')]=k
for gap in [.15,.25,.35]:
 k=cube('Keeper',30.9+gap,39.1-gap,92.6,104,10,30)
 join(k,cube('Stem',30.9+gap,39.1-gap,96.9+gap,103.1-gap,4,10.5))
 join(k,cube('Top lip',30.9+gap,39.1-gap,89.5,104,27.6,30))
 # Print on X side so lip and stem grow from a flat silhouette.
 k.matrix_world=Matrix.Rotation(math.pi/2,4,'Y') @ k.matrix_world
 parts['keeper-'+str(gap).replace('.','p')]=k

cap=cube('Square lower cap',30,38,8,16.5,27.6,31)
join(cap,cube('Cap stem',32.2,35.8,9.2,11.8,21.6,27.8))
cap.matrix_world=Matrix.Rotation(math.pi,4,'X')@cap.matrix_world
parts['lower-cap-0p20']=cap

def mesh(o):
 bpy.context.view_layer.update();m=o.to_mesh();vs=[o.matrix_world@v.co for v in m.vertices];faces=[list(p.vertices) for p in m.polygons];o.to_mesh_clear();return vs,faces
reports={}
def export(o,name):
 vs,fs=mesh(o);lo=Vector(tuple(min(v[i] for v in vs) for i in range(3)));vs=[v-lo for v in vs]
 me=bpy.data.meshes.new('Export');me.from_pydata(vs,[],fs);bm=bmesh.new();bm.from_mesh(me);bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=0.0001);bmesh.ops.dissolve_degenerate(bm,edges=list(bm.edges),dist=0.00001);bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bmesh.ops.triangulate(bm,faces=list(bm.faces));bm.verts.ensure_lookup_table();bm.faces.ensure_lookup_table()
 bad=sum(not e.is_manifold for e in bm.edges);seen=set();components=0
 for v in bm.verts:
  if v in seen:continue
  components+=1;todo=[v];seen.add(v)
  while todo:
   a=todo.pop()
   for e in a.link_edges:
    b=e.other_vert(a)
    if b not in seen:seen.add(b);todo.append(b)
 volume=bm.calc_volume(signed=True);assert bad==0 and components==1 and volume>0,(name,bad,components,volume)
 with open(os.path.join(OUT,name+'.stl'),'wb') as out:
  out.write(name.encode().ljust(80,b'\0'));out.write(struct.pack('<I',len(bm.faces)))
  for face in bm.faces:
   v=[x.co for x in face.verts];n=(v[1]-v[0]).cross(v[2]-v[0]).normalized();out.write(struct.pack('<12fH',*n,*v[0],*v[1],*v[2],0))
 reports[name]={'size_mm':[round(max(v[i] for v in vs),3) for i in range(3)],'volume_mm3':volume,'nonmanifold_edges':bad,'connected_solids':components,'triangles':len(bm.faces)};bm.free()
 return lo

# Export only the three accepted parts.
export(f,'corrected-rack-section')
export(cap,'lower-cap-0p20')
export(parts['keeper-0p25'],'keeper-0p25')
json.dump(reports,open(os.path.join(OUT,'geometry-audit.json'),'w'),indent=2)
