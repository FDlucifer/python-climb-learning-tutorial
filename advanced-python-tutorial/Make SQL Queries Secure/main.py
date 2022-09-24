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

age_input = input("Enter an age: ")

cursor.execute(f"""SELECT * FROM people WHERE age > {age_input}""")
rows = cursor.fetchall()
for row in rows:
    print(row)

