from db.transactions import Transactions

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class TypeTableItem(QTableWidgetItem):
    """ Represents a Table Widget Item for a Transaction Type """
    
    def __init__(self, transaction):
        """ Initialize the Type Item """
        self.transaction = transaction
        QTableWidgetItem.__init__(self, self.getData())
        
    def getData(self):
        """ Return data for the provided transaction """
        if self.transaction.income is True:
            return "Income"
        else:
            return "Expense"
        
    def setData(self, role, value):
        """ Set Data in Item """
        if role == Qt.EditRole:
            self.transaction.income = value == "Income"
            Transactions.save()
        return QTableWidgetItem.setData(self, role, self.getData())