import sqlite3 

def readSqliteTable():
  try:
    sqliteConnection = sqlite3.connect('Recipes.db')
    cursor = sqliteConnection.cursor()
    print ("Connection to SQLite")

    sqlite_select_query = """SELECT * from Recipe"""
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

    cursor.close()
  
  except sqlite3.Error as error:
  	print("Failed to read data from sqlite table ", error)
  
  finally:
  	if (sqliteConnection):
  		sqliteConnection.close()
  		print("The SQLite connection is closed")
