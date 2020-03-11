import sqlite3
from contextlib import closing

def readSqliteTable(queryType, value):
  if (queryType):
    sqlite_select_query = """SELECT * from Recipe WHERE {0:s} = '{1:s}'""".format(queryType, value)
  else:
    sqlite_select_query = """SELECT * from Recipe"""
        
  with closing(sqlite3.connect("Recipes.db")) as sqliteConnection:
    with closing(sqliteConnection.cursor()) as cursor:
      print ("Connection to SQLite")
      cursor.execute(sqlite_select_query)
      records = cursor.fetchall()
      print("Total rows are: ", len(records))
      print("Printing each row")
      for row in records:
        print("ID", row[0])
        print("Name", row[1])
        print("Description", row[2])
        print("Ingredients", row[3])
        print("Instructions", row[4])
        print("Category", row[5])   