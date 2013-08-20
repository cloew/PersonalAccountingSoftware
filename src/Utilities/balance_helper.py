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
        balance = 0
        for transaction in Transactions.allForAccount(account, order=Transaction.date):
            if transaction.date > account.initial_date:
                balance += account.initial_balance
        
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
            
        accountTransactions = Transactions.allForAccount(account)
        if len(accountTransactions) > 0:
            lastTransaction = accountTransactions[0]
            return self.balancesForAccounts[account][lastTransaction]
        return account.initial_balance
    
TheBalanceHelper = BalanceHelper()