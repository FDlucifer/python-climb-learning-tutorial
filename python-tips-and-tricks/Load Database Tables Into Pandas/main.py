# pip install pandas

import sqlite3
import pandas as pd

conn = sqlite3.connect("mydb.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS people (
    ssn INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER
)
""")

cur.execute("""
INSERT INTO people (ssn, name, age) VALUES
(1, 'Mike', 25),
(90, 'Anna', 35),
(7193, 'Bob', 76),
(1231, 'John', 55),
(2313, 'Stan', 18)
""")

conn.commit()

sql = pd.read_sql_query("SELECT * FROM people", conn)
df = pd.DataFrame(sql, columns=["ssn", "name", "age"])
df.set_index("ssn", inplace=True)

print(df)

# pandas to SQL
new_df = pd.DataFrame({
    "ssn": [1234, 345, 234],
    "name": ["Fox", "Lion", "Cat"],
    "age": [50, 34, 56]
})

new_df.to_sql("people", con=conn, if_exists="append", index=False)

