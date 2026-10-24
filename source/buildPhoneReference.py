# Historical reference only: owner reports inadequate phone retention. Do not print for use.
from pathlib import Path
import os,json,math,struct
ROOT=Path(__file__).resolve().parents[1]
OUT=str(Path(os.environ.get('RABBIRACK_OUTPUT',ROOT/'build/phone-v1.0-reference')).resolve());os.makedirs(OUT,exist_ok=True);os.environ['RABBIRACK_OUTPUT']=OUT
source=(ROOT/'source/buildRack.py').read_text();exec(source[:source.index('joints=')])
OUT=os.environ['RABBIRACK_OUTPUT']
f=cube('phone-panel-106x212',0,106,0,212,0,10)
boolean(f,cube('Open back',12,94,12,200,-1,11))
joints=[(x,y,False) for x in [0,106] for y in [22,84,128,190]]+[(x,y,True) for y in [0,212] for x in [22,84]]
# Four open corner supports; front insertion with all four caps removed.
for x in [22,84]:
 for top in [False,True]:
  low,high=(191.6,197.6) if top else (14.4,20.4)
  join(f,cube('Corner post',x-4,x+4,low,high,0,30.4))
  join(f,cube('Bed-connected support foot',x-4,x+4,187 if top else 10,202 if top else 25,0,3))
  join(f,cube('Rear corner pad',x-4,x+4,187 if top else 20.2,191.8 if top else 25,2,14))
  sy=195.1 if top else 16.9
  boolean(f,cube('Accepted cap socket',x-2,x+2,sy-1.5,sy+1.5,24.2,31))
# Short guides only near ends; button-height side rails stay below the phone rear.
for top in [False,True]:
 for right in [False,True]:
  x0,x1=(97.5,103) if right else (3,8.5)
  y0,y1=(179,185) if top else (27,33)
  join(f,cube('End lateral guide',x0,x1,y0,y1,8,26))
for cx,cy,rot in joints:
 pts=[(cx+(y if rot else x),cy+(x if rot else y)) for x,y in P]
 boolean(f,poly('V2 socket',pts,5.2,11))
 hx=cx+(5 if cx==0 else -5 if cx==106 else 0);hy=cy+(5 if cy==0 else -5 if cy==212 else 0)
 boolean(f,cyl('M3 through',(hx,hy,5),1.7,12));boolean(f,cyl('M3 nut pocket',(hx,hy,1.25),5.9/math.sqrt(3),2.7,6))
# Key is the existing V2 source variant, not a new connector shape.
k=poly('joint-key-0p25',offset(P,.25),0,4.4,teal)
for x in [-5,5]:boolean(k,cyl('M3 key clearance',(x,0,2),1.7,6))
# Export and audit using existing established mesh routine.
exec(source[source.index('def mesh(o):'):source.index('# Export only')])
export(f,'phone-panel');export(k,'joint-key-0p25');bpy.data.objects.remove(k,do_unlink=True)
json.dump(reports,open(os.path.join(OUT,'mesh-audit.json'),'w'),indent=2)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT,'phone-panel-source.blend'))
