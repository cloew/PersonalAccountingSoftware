from db.transactions import Transactions
from Qt.GUI.Transaction.Table.TableWidgets.transaction_table_item import TransactionTableItem

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class DescriptionTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Description """
    
    def __init__(self, transaction):
        """ Initialize the Description Item """
        TransactionTableItem.__init__(self, transaction)
        
    def getData(self):
        """ Return the Transaction's Description """
        return self.transaction.description
        
    def saveData(self, value):
        """ Save Data in Item """
        self.transaction.description = value
        Transactions.save()
        return True 