import sqlite3
from contextlib import closing

def createDb():
  with closing(sqlite3.connect("Recipes.db")) as sqliteConnection:
    sqlite_create_table_query = '''CREATE TABLE Recipe (
                                   id TEXT PRIMARY KEY,
                                   name TEXT NOT NULL,
                                   description TEXT NOT NULL, 
                                   ingredients TEXT NOT NULL,
                                   instructions TEXT NOT NULL, 
                                   category TEXT NOT NULL);'''

    with closing(sqliteConnection.cursor()) as cursor:
      print("Successfully Connected to SQLite")
      cursor.execute(sqlite_create_table_query)
      sqliteConnection.commit()
      print ("SQLite table created")
