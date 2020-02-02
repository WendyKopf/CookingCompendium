import sqlite3

try:
  sqliteConnection = sqlite3.connect('Recipes.db')
  cursor = sqliteConnection.cursor()
  print ("Connected to SQLite")

  sqlite_insert_query = """INSERT INTO Recipe 
                        (id, name, description, ingredients, instructions, category)
                        VALUES ('testRecipe', 'testName', 'testDescription', 'testIngredients', 'testInstructions', 'testCategory');"""
  cursor.execute(sqlite_insert_query)

  sqliteConnection.commit()
  cursor.close()

except sqlite3.Error as error:
  print("Error while working with SQLite", error)
finally:
  if (sqliteConnection):
    print("Total Rows affected since the database connection was opened:" , sqliteConnection.total_changes)
    sqliteConnection.close()
    print("sqlite connection is closed")
