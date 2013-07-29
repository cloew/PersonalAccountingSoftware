from db.transactions import Transactions
from Qt.GUI.Transaction.TableWidgets.transaction_table_item import TransactionTableItem
from Utilities.balance_helper import TheBalanceHelper

class TypeTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Type """
    
    def __init__(self, transaction, table):
        """ Initialize the Type Item """
        self.table = table
        TransactionTableItem.__init__(self, transaction)
        
    def getData(self):
        """ Return data for the provided transaction """
        if self.transaction.income is True:
            return "Income"
        else:
            return "Expense"
        
    def saveData(self, value):
        """ Save Data in Item """
        self.transaction.income = value == "Income"
        Transactions.save()
        TheBalanceHelper.setupBalancesForAccount(self.transaction.account)
        self.table.updateBalanceColumn()