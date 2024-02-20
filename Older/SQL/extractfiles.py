import sys
import os
import zipfile
import re

filepath = sys.argv[1]
regex = re.compile(sys.argv[2])

os.makedirs("cppfiles", exist_ok=True)

count = 0
with zipfile.ZipFile(filepath, 'r') as zf:
    for f in zf.namelist():
        if regex.match(f.split('/')[-1]):
            count += 1
            zf.extract(f, "cppfiles")

print(f'{count} files extracted')
