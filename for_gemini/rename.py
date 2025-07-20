import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: python rename_dir.py <old_dir_path> <new_dir_path>")
    sys.exit(1)

old_path = Path(sys.argv[1])
new_path = Path(sys.argv[2])

try:
    old_path.rename(new_path)
    print(f"Renamed: '{old_path}' → '{new_path}'")
except Exception as e:
    print(f"Failed to rename: {e}")
    sys.exit(1)