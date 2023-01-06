import sqlite3

connection = sqlite3.connect('sqlite.db')
cur = connection.cursor()

response = cur.execute('SELECT name FROM fastapi_simple_security')
hesla = response.fetchall()
for i in hesla:
    print(i)