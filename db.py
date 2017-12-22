import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE People
             (name, surname, age, city)''')
c.execute('drop table People')
conn.close()
