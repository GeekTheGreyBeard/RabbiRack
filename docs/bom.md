# Bill of materials and modular layouts

## One supported rack cell

| Part | Quantity | File |
| --- | ---: | --- |
| Rack cell | 1 | `models/corrected-rack-section.stl` |
| Top keeper | 1 | `models/keeper-0p25.stl` |
| Lower cap | 2 | `models/lower-cap-0p20.stl` |
| Base | 1 per supported column | `models/base-v1.0/base-fitment.stl` |
| Rear foot | 1 per base | `models/base-v1.0/rear-foot.stl` |
| Bowtie key | 2 per base-to-rack joint | `models/base-v1.0/attachment-key-0p25.stl` |

A vertical or horizontal cell-to-cell seam has two matching key sockets: use two bowties per joined seam. Adjacent base decks also have two side joining sockets: use two keys per base seam when coupling them. These are joint keys, not the keepers or lower caps that hold devices. Do not double-count the two base attachment keys as extra hardware.

## Layout examples

- One cell: 1 frame, 1 keeper, 2 lower caps, 1 base, 1 foot, 2 bowties.
- One column two high: 2 frames, 2 keepers, 4 caps, 1 base, 1 foot, 4 bowties (2 base attachment + 2 vertical seam).
- Two columns two high, all seams coupled: 4 frames, 4 keepers, 8 caps, 2 bases, 2 feet, 14 bowties (4 base attachments + 4 vertical seams + 4 horizontal cell seams + 2 base-to-base). This is the fully joined design BOM, not a count of every key visible in the owner photos.

The owner photos show the two-by-two arrangement populated. Larger arrays are mechanically conceivable on the 106 mm pitch but are not load-qualified. Add supported base columns and check stability; do not assume arbitrary stack heights are safe.

Trim is optional and does not replace structural keys. Historical notched rails are reference-only in this release; the closed variant was still being printed. For a single two-high column the old perimeter scheme uses 2 left rails, 2 right rails, 1 top cap and 2 base sides. Only exposed edges receive trim; shared seams must remain available for joining. Closed trim uses rear cable routing. Phone retainers are a known unresolved defect and excluded from stable BOM.
