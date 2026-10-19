# Acceptance and provenance

Published geometry: accepted single-unit rack revision, 2026-10-19 publication.

Owner-reported acceptance: one unit fit near-perfectly, close enough to work with. The scope is single-unit geometry. Stack/base stability remains unvalidated; no universal fit or production qualification is claimed.

`models/SHA256SUMS` records the exact accepted mesh bytes. Publication did not modify those files. Binary STL headers contain only part names and zero padding; triangle records contain geometric values and zero attribute fields, with no trailing payload.

The published source is a reduced build entry point derived from the accepted build script. Its missing primitive-helper dependency was recovered from the companion revision, inlined, and verified by exact regeneration of all three accepted mesh hashes with Blender 5.0.1. Outputs are redirected away from source files. Development test plates and gauges are not exported.

Each regenerated part passed the generator checks for one connected solid, positive volume and zero nonmanifold edges. These are digital geometry checks, not physical strength or stability tests.

The image is generated exclusively from the accepted STL files on a synthetic background. No photographs, device screenshots, slicer archives, machine profiles, G-code or private execution records are distributed.
