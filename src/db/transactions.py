from table_wrapper import TableWrapper
from ORM.transaction import Transaction
from sqlalchemy import desc


class TransactionsWrapper(TableWrapper):
    """ Class to wrap interaction to the Transactions table in the database """
    table_class = Transaction

    def all(self, order=None):
        """ Returns all transactions from the database """
        if order is None:
            return TableWrapper.all(self, order=desc(Transaction.date))
        else:
            return TableWrapper.all(self, order=order)

Transactions = TransactionsWrapper()