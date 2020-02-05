from retrieveData import readSqliteTable
from databaseInsert import insertIntoDatabase
from create_db import createDb
import os.path
import json
import sys

# Main function to call the functions as needed by the user.
if __name__ == "__main__":
  if (not os.path.exists("Recipes.db")):
    createDb()
  if (sys.argv[1] == 'insert'):
    with open(sys.argv[2]) as f:
      newRecipe = json.load(f)
      insertIntoDatabase(**newRecipe)
  elif (sys.argv[1] == 'select'):
    selectType = sys.argv[2]
    userCategory = sys.argv[3]
    readSqliteTable(selectType, userCategory)