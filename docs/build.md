# Build from source and verify

Requires Blender with bundled Python; geometry regeneration was verified with Blender 5.0.1. External Blender software is not included.

From the repository root:

```sh
blender --background --factory-startup --threads 2 --python source/buildRack.py
blender --background --factory-startup --threads 2 --python source/buildBase.py
(cd models && sha256sum -c SHA256SUMS)
```

Rack output defaults to `build/`, base output to `build/base-v1.0/`. Set `RABBIRACK_OUTPUT` to choose another output directory. `source/buildBase.py` consumes the repository's helper definitions and preserved vendor-logo trace. See the artwork exclusion in [notices](attribution.md).

Compare regenerated meshes with the checked-in reference STLs. Blender versions can change Boolean triangulation; byte equality is expected for the verified version, not promised across versions. Generators audit one connected solid, positive volume and no nonmanifold edges. Those checks establish mesh validity, not real-world strength or retention.

`source/buildTrim.py` rebuilds historical notched trim into `build/trim-v1.0/`. It is optional reference work, not a stable-models archive recommendation. `source/buildPhoneReference.py` is investigation-only: its phone retention is inadequate. The source/docs archive and GitHub's automatic source archives retain these clearly labeled references; the stable-models archive excludes them.

Release archives carry SHA256 checksums. No local paths, printer addresses, credentials, execution logs, private photo originals or machine-specific G-code belong in release assets.
