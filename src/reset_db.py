from db_generator import GenerateDatabase

import os

def ResetDatabase():
    """ Reset the Database """
    os.remove('db/pas.db')
    GenerateDatabase()

if __name__ == "__main__":
    ResetDatabase()