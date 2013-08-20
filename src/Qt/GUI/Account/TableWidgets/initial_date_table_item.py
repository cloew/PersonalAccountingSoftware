from db.accounts import Accounts
from Qt.GUI.Core.kao_table_item import KaoTableItem

from Utilities.balance_helper import TheBalanceHelper
from Utilities.date_helper import DateToString, StringToDate

class InitialDateTableItem(KaoTableItem):
    """ Represents a Table Widget Item for an Account Initial Date """
    
    def __init__(self, account, transactionTable):
        """ Initialize the Inital Date Item """
        self.transactionTable = transactionTable
        self.account = account
        KaoTableItem.__init__(self)
        
    def getData(self):
        """ Return the item's data as a string """
        return DateToString(self.account.initial_date)
        
    def saveData(self, value):
        """ Save Data """
        try:
            self.account.initial_date = StringToDate(value)
            Accounts.save()
            TheBalanceHelper.setupBalancesForAccount(self.account)
            self.transactionTable.updateBalanceColumn()
        except ValueError:
            pass # Expect it to happen if user enters a bad String for the date
            
    def shouldSetData(self, role):
        """ Returns if the Table Item should call the base classes set Data """
        return not (role == Qt.EditRole)