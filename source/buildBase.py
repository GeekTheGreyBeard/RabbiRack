from pathlib import Path
import os,json,math
ROOT=Path(__file__).resolve().parents[1]
r=Path(os.environ.get('RABBIRACK_OUTPUT',ROOT/'build/base-v1.0')).resolve();r.mkdir(parents=True,exist_ok=True);os.environ['RABBIRACK_OUTPUT']=str(r)
source=(ROOT/'source/buildRack.py').read_text();exec(source[:source.index('joints=')]);OUT=str(r)
T=Matrix.Translation((0,55,25))@Matrix.Rotation(math.radians(77.5),4,'X')
def tilted(o):o.matrix_world=T@o.matrix_world;return o
base=cube('Base 106 pitch',0,106,0,110,0,14)
# Structural saddle solid reaches below deck; rear buttresses reach the bed.
for x in [22,84]:
 s=tilted(cube('Keyed inclined saddle',x-10,x+10,-12,12,-4,13))
 boolean(s,tilted(cube('Module rim clearance',x-11,x+11,0,30,-.3,10.3)))
 boolean(s,tilted(cube('Clear accepted shoes',x-11,x+11,6,30,10,15)))
 join(base,s)
 join(base,cube('Bed-connected saddle pedestal',x-10,x+10,38,62,0,18))
 # Back gusset with 45 degree taper from base to saddle rear.
 pts=[(56,0),(78,0),(78,14),(62,37),(56,37)]
 # yz polygon extruded along x, built as poly then cyclic axis transform
 g=poly('Rear structural gusset',pts,x-7,x+7)
 g.matrix_world=Matrix(((0,0,1,0),(1,0,0,0),(0,1,0,0),(0,0,0,1)))
 # Trim it against module envelope and all contact clearances after union.
 join(base,g)
 boolean(base,tilted(cube('Rear rim clearance',x-11,x+11,0,35,-.3,10.3)))
 # Accepted bottom-edge bowtie pocket remains half in module, half in base.
 pts=[(x+y,xx) for xx,y in P]
 boolean(base,tilted(poly('Accepted bottom joint socket',pts,5.2,20)))
# Expandable base side joints use unchanged V2 shape, accessible from above.
for x in [0,106]:
 for y in [25,85]:boolean(base,poly('Expansion socket',[(x+a,y+b) for a,b in P],8.8,15))
# Removable rear foot: open-top dovetail, no unsupported socket roof.
foot_pts=[(39,94),(67,94),(67,102),(65,110.3),(41,110.3),(39,102)]
boolean(base,poly('Rear foot socket',offset(foot_pts,-.3),3,15))
foot=cube('Rear foot',26,80,110.3,158.3,0,14)
join(foot,poly('Integrated foot tongue',foot_pts,3.3,14))
# Authentic emblem from previously captured official source, no redrawing.
logo=json.loads((ROOT/'source/references/official_logo_trace.json').read_text())
bx0,by0,bx1,by1=logo['bounds_px'];scale=32/(by1-by0)
def emblem(points):return poly('Official rabbit emblem',[(53+(x-(bx0+bx1)/2)*scale,24+((by0+by1)/2-y)*scale) for x,y in points],14-3.175,15)
for c in logo['contours']:
 if c['parent']!=-1:continue
 cut=emblem(c['points'])
 for child in logo['contours']:
  if child['parent']==c['index']:boolean(cut,emblem(child['points']))
 boolean(base,cut)
k=poly('V2 base attachment key',offset(P,.25),0,4.4,teal)
for x in [-5,5]:boolean(k,cyl('Optional M3 clearance',(x,0,2),1.7,6))
# Existing exporter checks a single connected positive-volume manifold solid.
exec(source[source.index('def mesh(o):'):source.index('# Export only')])
export(base,'base-fitment');saved=foot.matrix_world.copy();foot.matrix_world=Matrix.Rotation(math.pi,4,'X')@foot.matrix_world;export(foot,'rear-foot');foot.matrix_world=saved;export(k,'attachment-key-0p25');bpy.data.objects.remove(k,do_unlink=True)
json.dump(reports,open(r/'mesh-audit.json','w'),indent=2)
bpy.ops.wm.save_as_mainfile(filepath=str(r/'base-source.blend'))
print(json.dumps(reports))
