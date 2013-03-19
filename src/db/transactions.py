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
            
    def allForAccount(self, account, order=None):
        """ Returns all transactions from the database """
        transactions = []
        with self.session() as session:
            if order is None:
                transactions = session.query(self.table_class).filter_by(account=account).order_by(Transaction.date).all()
                transactions.reverse()
            else:
                transactions = session.query(self.table_class).filter_by(account=account).order_by(order).all()
        return transactions

    def allUnclearedTransactionsForAccount(self, account):
        """ Returns all Uncleared Transactions """
        unclearedTransactions = []
        with self.session() as session:
            unclearedTransactions_False = session.query(self.table_class).filter_by(cleared=False, account=account)
            unclearedTransactions_None = session.query(self.table_class).filter_by(cleared=None, account=account)
            unionOfUnclearedTransactions = unclearedTransactions_False.union(unclearedTransactions_None)
            unclearedTransactions = unionOfUnclearedTransactions.order_by(desc(Transaction.date)).all()
        return unclearedTransactions

    def allUnreconciledTransactionsForAccount(self, account):
        """ Returns all Unreconciled Transactions """
        unreconciledTransactions = []
        with self.session() as session:
            unreconciledTransactions_False = session.query(self.table_class).filter_by(reconciled=False, account=account)
            unreconciledTransactions_None = session.query(self.table_class).filter_by(reconciled=None, account=account)
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