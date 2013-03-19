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

    def allUnclearedTransactions(self):
        """ Returns all Uncleared Transactions """
        unclearedTransactions = []
        with self.session() as session:
            unclearedTransactions_False = session.query(self.table_class).filter_by(cleared=False)
            unclearedTransactions_None = session.query(self.table_class).filter_by(cleared=None)
            unionOfUnclearedTransactions = unclearedTransactions_False.union(unclearedTransactions_None)
            unclearedTransactions = unionOfUnclearedTransactions.order_by(desc(Transaction.date)).all()
        return unclearedTransactions

    def allUnreconciledTransactions(self):
        """ Returns all Unreconciled Transactions """
        unreconciledTransactions = []
        with self.session() as session:
            unreconciledTransactions_False = session.query(self.table_class).filter_by(reconciled=False)
            unreconciledTransactions_None = session.query(self.table_class).filter_by(reconciled=None)
            unionOfUnreconciledTransactions = unreconciledTransactions_False.union(unreconciledTransactions_None)
            unreconciledTransactions = unionOfUnreconciledTransactions.order_by(desc(Transaction.date)).all()
        return unreconciledTransactions

    def allExpenseTransactionsForCategory(self, category):
        """ Returns all Expense Transactions with a given category """
        expenseTransactions = []
        with self.session() as session:
            expenseTransactions = session.query(self.table_class).filter_by(income=False, category=category).all()
        return expenseTransactions

Transactions = TransactionsWrapper()