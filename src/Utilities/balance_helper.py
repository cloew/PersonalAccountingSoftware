from db.transactions import Transactions
from ORM.transaction import Transaction

class BalanceHelper:
    """ Helper to calculate Balance """
    
    def __init__(self):
        """ Initiliaze the Balance Helper """
        self.balancesForAccounts = {}
        
    def setupBalancesForAccount(self, account):
        """ Setup the Balance """
        self.balancesForAccounts[account] = {}
        balance = account.starting_balance
        for transaction in Transactions.allForAccount(account, order=Transaction.date):
            if transaction.amount is not None:
                if transaction.income:
                    balance += transaction.amount
                else:
                    balance -= transaction.amount
            self.balancesForAccounts[account][transaction] = balance
            
    def getBalanceForTransaction(self, transaction):
        """ Return balance for Transaction """
        if transaction.account not in self.balancesForAccounts:
            self.setupBalancesForAccount(transaction.account)
        
        if transaction in self.balancesForAccounts[transaction.account]:
            return self.balancesForAccounts[transaction.account][transaction]
        return 0
    
TheBalanceHelper = BalanceHelper()