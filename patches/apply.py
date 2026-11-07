
from pathlib import Path
import sys

# PMS110 Atom Workspace - experimental patch
# Stage 1: Four native workspace slots

if len(sys.argv) != 2:
    sys.exit("Usage: apply.py SOURCE_DIRECTORY")

root = Path(sys.argv[1]).resolve()

target = root / (
    "app/src/main/kotlin/io/github/"
    "lujinxin/nextep/display/SlotState.kt"
)

if not target.is_file():
    sys.exit("ERROR: NeXtep source file not found")

source = target.read_text(encoding="utf-8")

old = "const val WORKSPACE_SLOT_COUNT = 3"
new = "const val WORKSPACE_SLOT_COUNT = 4"

if source.count(old) != 1:
    sys.exit(
        "ERROR: Upstream source changed. "
        "Patch stopped safely."
    )

target.write_text(
    source.replace(old, new),
    encoding="utf-8"
)

print("PMS110 patch applied.")
print("Workspace slots: 3 -> 4")
print("WARNING: Android compatibility untested.")
