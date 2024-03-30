# pip install faker

import sqlite3
from faker import Faker

fake = Faker()

conn = sqlite3.connect("customer_db.db")
c = conn.cursor()

c.execute("""CREATE TABLE customers
(id INTEGER PRIMARY KEY,
name TEXT,
email TEXT,
phone TEXT)
""")

for _ in range(50000):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    c.execute("INSERT INTO customers (name, email, phone) VALUES (?,?,?)",
              (name, email, phone))

conn.commit()
c.close()
conn.close()
