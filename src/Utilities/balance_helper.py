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
                if transaction.isIncome(account):
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
        
    def getCurrentBalanceForAccount(self, account):
        """ Returns the Current Balance for the given account """
        if account not in self.balancesForAccounts:
            self.setupBalancesForAccount(account)
            
        transactionsForAccount = Transactions.allForAccount(account)
        
        if len(transactionsForAccount) > 0:
            lastTransaction = transactionsForAccount[0]
            return self.balancesForAccounts[account][lastTransaction]
        return account.starting_balance
    
TheBalanceHelper = BalanceHelper()