# sqlite> .index
# email_index
# sqlite> EXPLAIN QUERY PLAN SELECT * FROM customers WHERE email="casdcasdc";
# QUERY PLAN
# `--SEARCH customers USING INDEX email_index (email=?)

import time
import sqlite3

conn = sqlite3.connect("customer_db.db")
c = conn.cursor()

c.execute("CREATE INDEX email_index on customers (email);")

c.close()
conn.close()
