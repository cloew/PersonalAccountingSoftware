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
        
        self.setupTransactionsBeforeAccount(account)
        self.setupTransactionsAfterAccount(account)
                    
    def setupTransactionsBeforeAccount(self, account):
        """ Setup Transactions before the account initial date """
        balance = account.initial_balance
        for transaction in Transactions.allForAccount(account, before=account.initial_balance_date):
            self.balancesForAccounts[account][transaction] = balance
            if transaction.amount is not None:
                balance -= transaction.getValue(account)
            
    def setupTransactionsAfterAccount(self, account):
        """ Setup Transactions after the account initial date """
        balance = account.initial_balance
        for transaction in Transactions.allForAccount(account, order=Transaction.date, onOrAfter=account.initial_balance_date):
            if transaction.amount is not None:
                balance += transaction.getValue(account)
                    
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