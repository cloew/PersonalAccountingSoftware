from db.transactions import Transactions

class BalanceHelper:
    """ Helper to calculate Balance """
    
    def __init__(self):
        """ Initiliaze the Balance Helper """
        self.balancesForAccounts = {}
        self.setupBalance()
        
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
    
TheBalanceHelper = BalanceHelper()