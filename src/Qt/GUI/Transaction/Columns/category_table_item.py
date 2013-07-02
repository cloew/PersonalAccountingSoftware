from db.categories import Categories
from db.transactions import Transactions

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class CategoryTableItem(QTableWidgetItem):
    """ Represents a Table Widget Item for a Transaction Category """
    
    def __init__(self, transaction):
        """ Initialize the Description Item """
        self.transaction = transaction
        QTableWidgetItem.__init__(self, self.getData())
        
    def getData(self):
        """ Return the Category name """
        if self.transaction.category is not None and self.transaction.category.name is not None:
            return self.transaction.category.name
        return ""
        
    def setData(self, role, value):
        """ Set Data in Item """
        if role == Qt.EditRole:
            category = Categories.findByName(value)
            if category is not None:
                self.transaction.category = category
            Transactions.save()
        return QTableWidgetItem.setData(self, role, value)