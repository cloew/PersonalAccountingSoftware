from db.transactions import Transactions

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class DescriptionTableItem(QTableWidgetItem):
    """ Represents a Table Widget Item for a Transaction Description """
    
    def __init__(self, transaction):
        """ Initialize the Description Item """
        QTableWidgetItem.__init__(self, transaction.description)
        self.transaction = transaction
        
    def setData(self, role, value):
        """ Set Data in Item """
        if role == Qt.EditRole:
            self.transaction.description = value
            Transactions.save()
        return QTableWidgetItem.setData(self, role, value)