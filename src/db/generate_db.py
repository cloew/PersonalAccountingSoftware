import ORM.account
import ORM.category
import ORM.transaction
from ORM.orm_base import Base

def GenerateDatabase(engine):
    """ Generate the Database """
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    GenerateDatabase()