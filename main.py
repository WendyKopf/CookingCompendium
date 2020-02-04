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
  with open(sys.argv[1]) as f:
    newRecipe = json.load(f)
    print (newRecipe)
  insertIntoDatabase(**newRecipe)
  readSqliteTable()