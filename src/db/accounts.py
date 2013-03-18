from table_wrapper import TableWrapper
from ORM.account import Account


class CategoriesWrapper(TableWrapper):
    """ Class to wrap interaction to the Accounts table in the database """
    table_class = Account

Accounts = AccountsWrapper()