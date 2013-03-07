from db_generator import GenerateDatabase
from db.database import Database

import os
import resources.resource_manager as resource_manager

def ResetDatabase():
    """ Reset the Database """
    os.remove(resource_manager.GetResourceFilePath('pas.db'))
    GenerateDatabase()
    Database.clearSession()

if __name__ == "__main__":
    ResetDatabase()