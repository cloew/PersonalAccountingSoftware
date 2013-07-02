from db.transactions import Transactions

from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

from decimal import InvalidOperation

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class AmountTableItem(QTableWidgetItem):
    """ Represents a Table Widget Item for a Transaction Amount """
    
    def __init__(self, transaction):
        """ Initialize the Amount Item """
        QTableWidgetItem.__init__(self, GetDollarString(transaction.amount))
        self.transaction = transaction
        
    def setData(self, role, value):
        """ Set Data in Item """
        if role == Qt.EditRole:
            try:
                self.transaction.amount = GetCentsFromDollarString(value)
            except InvalidOperation:
                pass # The cast from the string to a Decimal failed
            Transactions.save()
        return QTableWidgetItem.setData(self, role, GetDollarString(self.transaction.amount))