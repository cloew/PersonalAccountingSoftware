from db.transactions import Transactions

from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

from dateutil import parser
from decimal import InvalidOperation

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class DateTableItem(QTableWidgetItem):
    """ Represents a Table Widget Item for a Transaction Date """
    
    def __init__(self, transaction):
        """ Initialize the Date Item """
        self.transaction = transaction
        QTableWidgetItem.__init__(self, self.getData())
        
    def getData(self):
        """ Get Data """
        date = ""
        if self.transaction.date is not None:
            date = "{0:%m/%d/%Y}".format(self.transaction.date)
        return date
        
    def setData(self, role, value):
        """ Set Data in Item """
        if role == Qt.EditRole:
            try:
                self.transaction.date = parser.parse(value)
            except ValueError:
                pass # Expect it to happen if user enters a bad String for the date
            Transactions.save()
        return QTableWidgetItem.setData(self, role, self.getData())