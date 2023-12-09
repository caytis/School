import sqlite3
import sys
import os
import zipfile

dbfile = sys.argv[1]
exts = sys.argv[2:]

conn = sqlite3.connect('file.db')
cur = conn.cursor()

for ext in exts:
    rs = cur.execute(f'select * from files where ext like "{ext}"')

    count = 0
    with zipfile.ZipFile(f'{ext}.zip', 'w', zipfile.ZIP_DEFLATED) as zfile:
        for row in rs:
            count += 1
            zfile.write(os.path.join(row[1], row[2]))
    print(f'{count} {ext} files gathered')

cur.close()
