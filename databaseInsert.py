import sqlite3
from contextlib import closing

# Function for adding a recipe into the database. Function arguments are as follows:
# rid = recipe id, a string
# rname = recipe name, a string
# rdesc = recipe description, a string
# ringred = recipe ingredients, a string
# rcat = recipe category, a string 
def insertIntoDatabase(rid, rname, rdesc, ringred, rinstruct, rcat):
  with closing(sqlite3.connect("Recipes.db")) as sqliteConnection:
    print ("Connected to SQLite")
    with closing(sqliteConnection.cursor()) as cursor:
      sqlite_insert_query = """INSERT INTO Recipe 
                        (id, name, description, ingredients, instructions, category)
                        VALUES ('{0:s}', '{1:s}', '{2:s}', '{3:s}', '{4:s}', '{5:s}');""".format(rid,rname,rdesc,ringred,rinstruct,rcat)
      cursor.execute(sqlite_insert_query)
      sqliteConnection.commit()

    print("Total Rows affected since the database connection was opened:" , sqliteConnection.total_changes)
