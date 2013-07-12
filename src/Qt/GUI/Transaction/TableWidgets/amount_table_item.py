from db.transactions import Transactions
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString
from Qt.GUI.Transaction.TableWidgets.transaction_table_item import TransactionTableItem

from decimal import InvalidOperation

class AmountTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Amount """
    
    def __init__(self, transaction, table):
        """ Initialize the Amount Item """
        self.table = table
        TransactionTableItem.__init__(self, transaction)
        
    def getData(self):
        """ Return the item's data as a string """
        return GetDollarString(self.transaction.amount)
        
    def saveData(self, value):
        """ Save Data """
        try:
            self.transaction.amount = GetCentsFromDollarString(value)
            Transactions.save()
            TheBalanceHelper.setupBalancesForAccount(self.transaction.account)
            self.table.updateBalanceColumn()
        except InvalidOperation:
            pass # The cast from the string to a Decimal failed