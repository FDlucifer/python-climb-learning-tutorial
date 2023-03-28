# apt install sqlite3
# root@DESKTOP-2HA9GOI:/mnt/d/1.program/python/python2/python-practise/advanced-python-tutorial/Encrypt SQLite Databases with SQLCipher# sqlite3 mydb.db
# SQLite version 3.37.2 2022-01-06 13:25:41
# Enter ".help" for usage hints.
# sqlite> CREATE TABLE people (id INT, name TEXT, age INT);
# sqlite> INSERT INTO people (id, name, age) VALUES (1, 'Mike', 30), (2, 'Sara', 40), (3, 'Bob', 70);
# sqlite> select * from people;
# 1|Mike|30
# 2|Sara|40
# 3|Bob|70
# apt install sqlcipher
# sqlite> .out create_script.sql
# sqlite> .dump
# sqlite> .q
# sqlite> PRAGMA key='password';
# sqlite> .read create_script.sql
# sqlite> .q
# root@DESKTOP-2HA9GOI:/mnt/d/1.program/python/python2/python-practise/advanced-python-tutorial/Encrypt SQLite Databases with SQLCipher# sqlcipher enc.db
# SQLCipher version 3.15.2 2016-11-28 19:13:37
# Enter ".help" for instructions
# Enter SQL statements terminated with a ";"
# sqlite> PRAGMA key='password';
# sqlite> select * from people;
# 1|Mike|30
# 2|Sara|40
# 3|Bob|70
# apt-get install libsqlcipher-dev
# pip3 install pysqlcipher3

from pysqlcipher3 import dbapi2 as sqlite

conn = sqlite.connect("enc.db")
cur = conn.cursor()
cur.execute("PRAGMA key='password';")
cur.execute("select * from people;")
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()
