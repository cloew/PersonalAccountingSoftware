from db.accounts import Accounts
from db.transactions import Transactions
from Qt.GUI.Transaction.Table.TableWidgets.transaction_table_item import TransactionTableItem
from Utilities.balance_helper import TheBalanceHelper

class AccountTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Account """
    
    def __init__(self, transaction):
        """ Initialize the Account Item """
        TransactionTableItem.__init__(self, transaction)
        
    def getData(self):
        """ Return data for the provided transaction """
        if self.transaction.account is not None:
            return self.transaction.account.name
        return ""
        
    def saveData(self, value):
        """ Save Data in Item """
        originalAccount = self.transaction.account
        newAccount = Accounts.accountWithName(value)
        if newAccount is not None:
            self.transaction.account = newAccount
            Transactions.save()
            TheBalanceHelper.setupBalancesForAccount(originalAccount)
            TheBalanceHelper.setupBalancesForAccount(newAccount)
            return True 