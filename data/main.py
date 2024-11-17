import sqlite3
connection=sqlite3.connect("3wr.db")
cursor=connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    t INTEGER NOT NULL,
    w TEXT NOT NULL
);''')
connection.commit()
cursor.execute("INSERT INTO weather (t, w) VALUES (3, 'tuesday');")
cursor.execute("INSERT INTO weather (t, w) VALUES (5, 'wensday');")
cursor.execute("INSERT INTO weather (t, w) VALUES (1, 'thirsday');")
cursor.execute("INSERT INTO weather (t, w) VALUES (0, 'friday');")
cursor.execute("INSERT INTO weather (t, w) VALUES (-1, 'saturday');")
cursor.execute("INSERT INTO weather (t, w) VALUES (0, 'sunday');")
cursor.execute("INSERT INTO weather (t, w) VALUES (5, 'monday');")
connection.commit()
connection.close()
