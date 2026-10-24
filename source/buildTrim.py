from pathlib import Path
import os,json,math
ROOT=Path(__file__).resolve().parents[1]
r=Path(os.environ.get('RABBIRACK_OUTPUT',ROOT/'build/trim-v1.0')).resolve();r.mkdir(parents=True,exist_ok=True);os.environ['RABBIRACK_OUTPUT']=str(r)
source=(ROOT/'source/buildRack.py').read_text();exec(source[:source.index('joints=')]);OUT=str(r)
# Parts are modeled assembled on the left edge, then transformed to other edges.
# Half-key stems retain existing V2 0.25 mm polygon clearance and 4.4 mm thickness.
pts=offset(P,.25)
def halfkey(y,z):
 k=poly('Integral half bowtie',[(x,y+v) for x,v in pts],z,z+4.4)
 boolean(k,cube('Remove outer half',-20,-.6,y-10,y+10,z-1,z+6))
 return k

def rail(name,length,depth,centers,keyz,notch=None):
 q=cube(name,-3.5,-.3,0,length,0,depth)
 for y in centers:join(q,halfkey(y,keyz))
 if notch:lo,hi=notch;boolean(q,cube('Preserve control clearance',-4,0,lo,hi,3,depth+1))
 return q
left=rail('rack-left',106,10,[22,84],5.5,(35,75))
right=rail('rack-right',106,10,[22,84],5.5,(48.3,72.3))
# Reflection about x=53 places the same inward half keys on the right edge.
right.matrix_world=Matrix.Translation((106,0,0))@Matrix.Diagonal((-1,1,1,1))@right.matrix_world
top=rail('rack-top',113,10,[25.5,87.5],5.5,(45.5,78.5))
# Local rail length includes 3.5 mm overhang on each end to cap side corners.
top.matrix_world=Matrix(((0,1,0,-3.5),(-1,0,0,106),(0,0,1,0),(0,0,0,1)))@top.matrix_world
bl=rail('base-left',110,14,[25,85],9.1)
br=rail('base-right',110,14,[25,85],9.1);br.matrix_world=Matrix.Translation((106,0,0))@Matrix.Diagonal((-1,1,1,1))@br.matrix_world
k=poly('stack-key',pts,0,4.4,teal)
for x in [-5,5]:boolean(k,cyl('Optional M3 clearance',(x,0,2),1.7,6))
exec(source[source.index('def mesh(o):'):source.index('# Export only')])
# Print each rail on its continuous outside edge: full flat 106x10/110x14 footprint.
for q in [left,right,top,bl,br]:
 saved=q.matrix_world.copy()
 R=Matrix.Rotation(-math.pi/2,4,'X') if q==top else Matrix.Rotation((1 if q in [right,br] else -1)*math.pi/2,4,'Y')
 q.matrix_world=R@saved
 export(q,q.name);q.matrix_world=saved
export(k,'stack-key');bpy.data.objects.remove(k,do_unlink=True)
json.dump(reports,open(r/'mesh-audit.json','w'),indent=2)
bpy.ops.wm.save_as_mainfile(filepath=str(r/'trim-source.blend'));print(json.dumps(reports))
