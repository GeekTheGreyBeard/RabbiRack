# Printing guidance

Slice the STL files for your printer and material; no ready-to-run machine G-code is provided. Models use millimeters.

The owner's successful PLA baseline used a CR-10 Smart Cartesian printer with a 300 × 300 × 400 mm build volume, 0.4 mm nozzle, 0.2 mm layers, 4 perimeters and 20% infill. Temperatures were 215°C first layer, 210°C thereafter, with a 60°C bed. These are reference settings, not a universal filament profile. Use the filament maker's range and your calibrated printer.

Preserve the supplied mesh orientation: rack on its rear face, lower caps flat top down with stems upward, keeper on its side, base on its deck underside, rear foot inverted with its full tongue silhouette supported, bowties flat. Core parts were sliced without generated supports in PrusaSlicer 2.9.6; inspect your own preview for bridges, overhangs and unsupported starts. Do not auto-rotate parts into unsupported orientations.

Successful later jobs used perimeter-avoidance travel, 0.6 mm retract lift from the first layer and 5 mm/s Z travel. A prior multi-rack job shifted; coplanar travel after roof geometry was a candidate, not a proven unique cause. Lift/avoidance reduces modeled contact risk but does not fix loose mechanics, curled plastic or a sliding bed. Check actual travels, including short unretracted moves. Keep a clean clear bed, adequate part spacing and safe skirt margins; inspect first-layer adhesion rather than trust status flags.

The accepted base + rear foot + two keys used approximately 108.13 g PLA and took about 10h30m on the owner's machine. Long first layers make early byte-based ETA unreliable. Estimates vary with printer, slicer and material. The red closed-trim batch was still running at v1 release preparation; its completion and fit are not claimed here.

Recheck bowtie and retainer fit on a small first set before producing a large array. Do not alter accepted mating geometry simply to compensate for an uncalibrated printer. No leveling, firmware or other machine settings are changed by these files.
