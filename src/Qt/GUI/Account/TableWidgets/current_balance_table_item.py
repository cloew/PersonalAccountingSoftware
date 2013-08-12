from db.accounts import Accounts
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetDollarString
from Qt.GUI.Core.kao_table_item import KaoTableItem

from PySide.QtCore import Qt

class CurrentBalanceTableItem(KaoTableItem):
    """ Represents a Table Widget Item for an Account Current Balance """
    
    def __init__(self, account):
        """ Initialize the Starting Balance Item """
        self.account = account
        KaoTableItem.__init__(self)
        
        flags = self.flags()
        self.setFlags(flags and ~Qt.ItemIsEditable)
        
    def getData(self):
        """ Return the item's data as a string """
        return GetDollarString(TheBalanceHelper.getCurrentBalanceForAccount(self.account))
        
    def saveData(self, value):
        """ Do nothing """