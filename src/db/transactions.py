from table_wrapper import TableWrapper
from ORM.account import Account
from ORM.transaction import Transaction
from sqlalchemy import desc, sql

class TransactionsWrapper(TableWrapper):
    """ Class to wrap interaction to the Transactions table in the database """
    table_class = Transaction

    def all(self, order=None):
        """ Returns all transactions from the database """
        if order is None:
            return TableWrapper.all(self, order=desc(Transaction.date))
        else:
            return TableWrapper.all(self, order=order)
        
    def allForAccount(self, account, order=None, filters={}):
        """ Return all transactions for the given account with the applied filters """
        transactions = []
        with self.session() as session:
            accountQuery = self.getAccountQuery(session, account)#.join(Account.transfers)
            transfersQuery = session.query(self.table_class).join(Account.transfers).filter(Transaction.transferAccounts.contains(account))
            resultQuery = accountQuery.union(transfersQuery)
            for column in filters:
                unionQuery = session.query(self.table_class).filter(sql.false())
                for value in filters[column]:
                    tempQuery = accountQuery.filter(column==value)
                    unionQuery = unionQuery.union(tempQuery)
                resultQuery = resultQuery.intersect(unionQuery)
            
            if order is None:
                transactions = resultQuery.order_by(Transaction.date).all()
                transactions.reverse()
            else:
                transactions = resultQuery.order_by(order).all()
        return transactions# + account.transfers

    def allUnclearedTransactionsForAccount(self, account):
        """ Returns all Uncleared Transactions """
        unclearedTransactions = []
        with self.session() as session:
            accountQuery = self.getAccountQuery(session, account)
            unclearedTransactions_False = accountQuery.filter_by(cleared=False)
            unclearedTransactions_None = accountQuery.filter_by(cleared=None)
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
            expenseTransactions_False = session.query(self.table_class).filter_by(income=False, category=category)
            expenseTransactions_None = session.query(self.table_class).filter_by(income=None, category=category)
            unionOfExpenseTransactions = expenseTransactions_False.union(expenseTransactions_None)
            expenseTransactions = unionOfExpenseTransactions.all()
        return expenseTransactions
        
    def getAccountQuery(self, session, account):
        """ Return the query for the transactions of the given account """
        return session.query(self.table_class).filter_by(account=account)

Transactions = TransactionsWrapper()