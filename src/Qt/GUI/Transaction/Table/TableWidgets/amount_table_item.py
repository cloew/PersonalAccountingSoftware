from db.transactions import Transactions
from Qt.GUI.Transaction.Table.TableWidgets.transaction_table_item import TransactionTableItem
from Qt.GUI.Transaction.Transfers.transfer_menu_factory import AddTransferActionsToWidgetContextMenu
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

from decimal import InvalidOperation

class AmountTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Amount """
        
    def getData(self):
        """ Return the item's data as a string """
        return GetDollarString(self.transaction.amount)
        
    def saveData(self, value):
        """ Save Data """
        try:
            self.transaction.amount = GetCentsFromDollarString(value)
            Transactions.save()
            TheBalanceHelper.setupBalancesForAccount(self.transaction.account)
            return True
        except InvalidOperation:
            pass # The cast from the string to a Decimal failed