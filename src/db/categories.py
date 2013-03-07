from table_wrapper import TableWrapper
from ORM.category import Category


class CategoriesWrapper(TableWrapper):
    """ Class to wrap interaction to the Categories table in the database """
    table_class = Category

    def findByName(self, name):
        """ Return a Category with the given name """
        db_record = None
        with self.session() as session:
            db_record = session.query(self.table_class).filter_by(name=name).first()
        return db_record

Categories = CategoriesWrapper()