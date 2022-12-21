import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "lucifer11", hashlib.sha256("lucifer11".encode()).hexdigest()
username2, password2 = "lucifer11312", hashlib.sha256("lucifer11312".encode()).hexdigest()
username3, password3 = "lucifer1sdc1", hashlib.sha256("lucifer1sdc1".encode()).hexdigest()
username4, password4 = "ccasd", hashlib.sha256("ccasd".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()

