import sys
from pathlib import Path


if len(sys.argv) != 2:
    print("Usage: <path>  not given")
    sys.exit(1)

target_dir = Path(sys.argv[1])
target_dir.mkdir(parents=True,exist_ok=True)   
