import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute("SELECT * FROM auth_user_user_permissions")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
