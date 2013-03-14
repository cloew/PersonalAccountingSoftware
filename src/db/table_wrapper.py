from contextlib import contextmanager
from database import Database


class TableWrapper:
    """ Class to wrap interaction to tables in the database """
    table_class = None # Should be overridden by sub class

    def __init__(self):
        """ Initialize the Table Wrapper """

    def add(self, record):
        """ Add Record to the database """
        with self.session() as session:
            session.add(record)

    def save(self):
        """ Update the given transaction """
        with self.session() as session:
            pass

    def find(self, record):
        """ Returns the matching entry in the database """
        db_record = None
        with self.session() as session:
            db_record = session.query(self.table_class).filter_by(id=record.id).first()
        return db_record

    def delete(self, record):
        """ Remove the provided record """
        with self.session() as session:
            session.delete(record)

    def all(self, order=None):
        """ Returns all records from the database """
        records = None
        with self.session() as session:
            if order is None:
                records = session.query(self.table_class).all()
            else:
                records = session.query(self.table_class).order_by(order).all()
        return records

    @contextmanager
    def session(self):
        """ Returns the session """ # Need to add Exception handling
        session = Database.getSession()
        yield session
        session.commit()