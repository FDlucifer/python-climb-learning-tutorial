import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS people;""")

cursor.execute("""CREATE TABLE people (
    name VARCHAR(255) NOT NULL,
    job VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    age INT,
    gender CHAR(1));""")

cursor.execute("""INSERT INTO people (name, job, password, age, gender) VALUES
('Mike', 'Programmer', 'mypass123', 45, 'm'),
('Anna', 'Accountant', 'my_secret_pass', 40, 'f'),
('Bob', 'Doctor', '123456789', 29, 'm'),
('Sam', 'Acountant', 'helloworld', 28, 'm'),
('Max', 'Cook', 'you_will_never_know_889', 32, 'f');""")

conn.commit()

name_input = input("what is your login name: ")
pass_input = input("what is your password: ")

cursor.execute(f"""SELECT * FROM people WHERE name = ? AND password = ?""", (name_input, pass_input))

rows = cursor.fetchall()

if len(rows) == 0:
    print("login failed!")
else:
    print(f"success! here is the information of {name_input}")
    for row in rows:
        print(row)

