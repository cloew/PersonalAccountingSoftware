from .table_wrapper import TableWrapper
from ORM.category import Category

from sqlalchemy import asc
from sqlalchemy.sql import collate

class CategoriesWrapper(TableWrapper):
    """ Class to wrap interaction to the Categories table in the database """
    table_class = Category

    def all(self, order=None):
        """ Returns all transactions from the database """
        if order is None:
            return TableWrapper.all(self, order=collate(Category.name, 'NOCASE'))
        else:
            return TableWrapper.all(self, order=order)
    
    def findByName(self, name):
        """ Return a Category with the given name """
        db_record = None
        with self.session() as session:
            db_record = session.query(self.table_class).filter_by(name=name).first()
        return db_record

Categories = CategoriesWrapper()