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
            
    def getBalanceForTransaction(self, transaction, account):
        """ Return balance for Transaction """
        if account not in self.balancesForAccounts:
            self.setupBalancesForAccount(account)
        
        if transaction in self.balancesForAccounts[account]:
            return self.balancesForAccounts[account][transaction]
        return 0
    
TheBalanceHelper = BalanceHelper()