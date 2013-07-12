from db.transactions import Transactions
from Qt.GUI.Transaction.TableWidgets.transaction_table_item import TransactionTableItem

class TypeTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Type """
    
    def __init__(self, transaction):
        """ Initialize the Type Item """
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