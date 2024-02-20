import sqlite3
import sys
import os

direc = sys.argv[1]

conn = sqlite3.connect('file.db')
cur = conn.cursor()
cur.execute('drop table if exists files')
cur.execute('create table if not exists files (ext text, path text, fname text)')

for root, dirs, files in os.walk(direc):
    for fname in files:
        if fname[0] == '.' or fname[0] == '_':
            continue
        ext = fname.split('.')[-1]
        query = f'insert into files values ("{ext}", "{os.path.abspath(root)}", "{fname}")'
        cur.execute(query)
conn.commit()

rs = cur.execute('select * from files')

with open('files-part1.txt', 'w') as f:
    for row in rs:
        f.write(str(row) + '\n')

cur.close()
