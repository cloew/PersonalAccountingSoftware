from db.transactions import Transactions
from Qt.GUI.Transaction.TableWidgets.transaction_table_item import TransactionTableItem
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

from dateutil import parser
from decimal import InvalidOperation

from PySide.QtCore import Qt
from PySide.QtGui import QTableWidgetItem

class DateTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Date """
    
    def __init__(self, transaction, table):
        """ Initialize the Date Item """
        self.table = table
        TransactionTableItem.__init__(self, transaction)
        
    def getData(self):
        """ Get Data """
        date = ""
        if self.transaction.date is not None:
            date = "{0:%m/%d/%Y}".format(self.transaction.date)
        return date
        
    def saveData(self, value):
        """ Save Data in Item """
        try:
            self.transaction.date = parser.parse(value)
            TheBalanceHelper.setupBalancesForAccount(self.transaction.account)
            self.table.updateBalanceColumn()
        except ValueError:
            pass # Expect it to happen if user enters a bad String for the date
        Transactions.save()