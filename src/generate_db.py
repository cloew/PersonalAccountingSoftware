from db.database import Database

import ORM.category
import ORM.transaction
from ORM.orm_base import Base

def GenerateDatabase():
    """ Generate the Database """
    Base.metadata.create_all(Database.engine)

if __name__ == "__main__":
    GenerateDatabase()