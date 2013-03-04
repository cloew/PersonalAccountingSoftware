from db.database import Database

import ORM.transaction
from ORM.orm_base import Base

def GenerateDatabase():
    """ Generate the Database """
    database = Database()
    Base.metadata.create_all(database.engine)

if __name__ == "__main__":
    GenerateDatabase()