import sqlite3

conn = sqlite3.connect("database.db")

with open("create_database.sql", "r") as f:
    sql = f.read()

conn.executescript(sql)
conn.commit()
conn.close()