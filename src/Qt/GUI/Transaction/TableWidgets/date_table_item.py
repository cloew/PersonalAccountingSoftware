from db.transactions import Transactions
from Qt.GUI.Transaction.TableWidgets.transaction_table_item import TransactionTableItem
from Utilities.balance_helper import TheBalanceHelper

from dateutil import parser

from PySide.QtCore import Qt

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
            self.table.updateTransactions()
        except ValueError:
            pass # Expect it to happen if user enters a bad String for the date
        Transactions.save()
        
    def shouldSetData(self, role):
        """ Returns if the Table Item should call the base classes set Data """
        return not (role == Qt.EditRole)