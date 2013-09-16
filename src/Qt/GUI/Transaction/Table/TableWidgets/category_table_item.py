from db.categories import Categories
from db.transactions import Transactions
from Qt.GUI.Transaction.Table.TableWidgets.transaction_table_item import TransactionTableItem

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class CategoryTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Category """
    
    def __init__(self, transaction):
        """ Initialize the Description Item """
        TransactionTableItem.__init__(self, transaction)
        
    def getData(self):
        """ Return the Category name """
        if self.transaction.category is not None and self.transaction.category.name is not None:
            return self.transaction.category.name
        return ""
        
    def saveData(self, value):
        """ Save Data in Item """
        category = Categories.findByName(value)
        if category is not None:
            self.transaction.category = category
        Transactions.save()