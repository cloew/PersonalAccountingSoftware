from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseWrapper:
    """ Handles all interaction to the database """
    __database_path__ = "db/pas.db"

    def __init__(self):
        """ Initialize the Database """
        self.engine = create_engine('sqlite:///{0}'.format(self.__database_path__), echo=True)
        self.sessionmaker = sessionmaker(bind=self.engine)
        self.session = None

    def getSession(self):
        """ Return a SQLAlchemy Database Session """
        if self.session is None:
            self.session = self.sessionmaker()
        return self.session

Database = DatabaseWrapper()