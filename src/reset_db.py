from db_generator import GenerateDatabase
from db.database import Database

import os

def ResetDatabase():
    """ Reset the Database """
    os.remove('db/pas.db')
    GenerateDatabase()
    Database.clearSession()

if __name__ == "__main__":
    ResetDatabase()