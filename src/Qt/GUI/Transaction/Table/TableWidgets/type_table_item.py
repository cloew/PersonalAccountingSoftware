from db.transactions import Transactions
from Qt.GUI.Transaction.Table.TableWidgets.transaction_table_item import TransactionTableItem
from Utilities.balance_helper import TheBalanceHelper

class TypeTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Type """
    label_text = {True:"Income",
                  False:"Expense",
                  None:"Expense"} 
    
    def __init__(self, transaction, account=None):
        """ Initialize the Type Item """
        self.account = account
        TransactionTableItem.__init__(self, transaction)
        
    def getData(self):
        """ Return data for the provided transaction """
        return TypeTableItem.label_text[self.transaction.isIncome(account=self.account)]
        
    def saveData(self, value):
        """ Save Data in Item """
        self.transaction.income = value == "Income"
        Transactions.save()
        TheBalanceHelper.setupBalancesForAccount(self.transaction.account)
        return True 