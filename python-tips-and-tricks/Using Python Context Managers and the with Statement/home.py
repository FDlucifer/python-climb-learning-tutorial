import os
import sys

with os.scandir(sys.argv[1]) as entries:
    for entry in entries:
        print(f"{entry.name:16} -> {entry.stat().st_size} bytes...")