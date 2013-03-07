from table_wrapper import TableWrapper
from ORM.category import Category


class CategoriesWrapper(TableWrapper):
    """ Class to wrap interaction to the Categories table in the database """
    table_class = Category

Categories = CategoriesWrapper()