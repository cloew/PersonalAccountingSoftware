from db.transactions import Transactions
from ORM.transaction import Transaction
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString
from Qt.GUI.Transaction.TableWidgets.transaction_table_item import TransactionTableItem

from decimal import InvalidOperation

from PySide.QtCore import Qt

class BalanceTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Balance """
    
    def __init__(self, transaction):
        """ Initialize the Amount Item """
        TransactionTableItem.__init__(self, transaction)
        
        flags = self.flags()
        self.setFlags(flags and ~Qt.ItemIsEditable)
        
    def getData(self):
        """ Return the balance for the current transaction """
        return GetDollarString(TheBalanceHelper.getBalanceForTransaction(self.transaction))