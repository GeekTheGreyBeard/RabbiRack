# Acceptance and provenance

## Preserved accepted rack

The October 19, 2026 publication contains the owner-accepted Rabbit cell, keeper and lower-cap meshes. Their original bytes remain unchanged. The original source's missing primitive-helper dependency was recovered and inlined, then verified by exact regeneration with Blender 5.0.1.

## October 24, 2026 additions

- **Base v1.0:** the owner reports perfect fitment following a successful single-base print. Source and meshes include the united keyed base, removable rear foot and matching attachment key. This is owner fit acceptance, not a blanket stability or load rating.
- **Phone v1.0 reference:** the owner confirms overall compatibility with RabbiRack but reports retainers too open for secure phone retention. Photos are pending. The design is preserved as a known inadequate-retention reference, with no new correction or reprint.
- **Trim v1.0:** seven rails and two stack bowties for one base and two vertically stacked Rabbit cells. First batch is printing at publication. Digital geometry and toolpath checks passed; completed-print and physical trim-fit acceptance remain pending.

`models/SHA256SUMS` records all published reference mesh bytes. Binary STL files contain part-name headers, geometry and zero attribute fields without trailing payload. New source entry points use repository-relative helper/reference paths and write to ignored `build/` folders by default. Blender 5.0.1 regeneration checks compare the resulting meshes with the preserved local references; other versions may change triangulation.

All exported parts pass one-connected-solid, positive-volume and zero-nonmanifold-edge checks. Base and trim assembly/interference checks are nominal geometric tests, not material strength or real-world retention proof. The phone feedback specifically demonstrates this distinction.

Images are synthetic CAD renders; they are not private photographs or physical validation evidence. No credentials, printer endpoints, printer-specific G-code, slicer profiles/archives, private execution records or unrelated files are distributed. Licensing remains undecided.
