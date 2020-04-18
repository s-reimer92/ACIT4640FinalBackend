import sqlite3
conn = sqlite3.connect("images.sqlite")

c = conn.cursor()
c.execute('''
    CREATE TABLE url
    (id INTEGER PRIMARY KEY ASC, 
     url VARCHAR(40) NOT NULL)
''')

conn.commit()
conn.close()
