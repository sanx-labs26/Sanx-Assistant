import sqlite3

conn = sqlite3.connect("sanx.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM documents")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()