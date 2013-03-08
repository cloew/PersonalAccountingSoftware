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

    def allExpenseTransactionsForCategory(self, category):
        """ Returns all Expense Transactions with a given category """
        return session.query(self.table_class).filter_by(income=False, category=category)

Transactions = TransactionsWrapper()