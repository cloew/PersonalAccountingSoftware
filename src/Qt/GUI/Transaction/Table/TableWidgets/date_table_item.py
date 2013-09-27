from db.transactions import Transactions
from Qt.GUI.Transaction.Table.TableWidgets.transaction_table_item import TransactionTableItem
from Utilities.balance_helper import TheBalanceHelper
from Utilities.date_helper import DateToString, StringToDate

from PySide.QtCore import Qt

class DateTableItem(TransactionTableItem):
    """ Represents a Table Widget Item for a Transaction Date """
        
    def getData(self):
        """ Get Data """
        date = ""
        if self.transaction.date is not None:
            date = DateToString(self.transaction.date)
        return date
        
    def saveData(self, value):
        """ Save Data in Item """
        try:
            self.transaction.date = StringToDate(value)
            TheBalanceHelper.setupBalancesForAccount(self.transaction.account)
            Transactions.save()
            return True
        except ValueError:
            pass # Expect it to happen if user enters a bad String for the date
        
    def shouldSetData(self, role):
        """ Returns if the Table Item should call the base classes set Data """
        return not (role == Qt.EditRole)