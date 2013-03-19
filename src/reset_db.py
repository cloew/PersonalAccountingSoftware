from db.database import Database
from db.generate_db import GenerateDatabase

import os
import resources.resource_manager as resource_manager

def ResetDatabase():
    """ Reset the Database """
    Database.clearSession()
    os.remove(Database.__database_path__)
    GenerateDatabase(Database.engine)
    Database.clearSession()

if __name__ == "__main__":
    ResetDatabase()