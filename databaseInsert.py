import sqlite3
from contextlib import closing

def insertIntoDatabase():
  with closing(sqlite3.connect("Recipes.db")) as sqliteConnection:
    print ("Connected to SQLite")
    with closing(sqliteConnection.cursor()) as cursor:

      sqlite_insert_query = """INSERT INTO Recipe 
                          (id, name, description, ingredients, instructions, category)
                          VALUES ('testRecipe', 'testName', 'testDescription', 'testIngredients', 'testInstructions', 'testCategory');"""
      cursor.execute(sqlite_insert_query)

      sqliteConnection.commit()
      cursor.close()

      print("Total Rows affected since the database connection was opened:" , sqliteConnection.total_changes)

insertIntoDatabase()
