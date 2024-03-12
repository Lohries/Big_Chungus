import sqlite3

con = sqlite3.connect('Brain.db')

cursor = con.cursor()

cursor.execute("CREATE TABLE person (images, name, id)")

responde = cursor.execute("SELECT name FROM sqlite_master")
responde.fetchone()