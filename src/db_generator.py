from sqlalchemy import create_engine

import ORM.transaction
from ORM.orm_base import Base

def GenerateDatabase():
    """ Generate the Database """
    engine = create_engine('sqlite:///db/pas.db', echo=True)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    GenerateDatabase()