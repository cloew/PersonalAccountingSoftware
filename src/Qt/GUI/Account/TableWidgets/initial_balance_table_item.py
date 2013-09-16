from db.accounts import Accounts
from Qt.GUI.Core.kao_table_item import KaoTableItem

from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

from decimal import InvalidOperation

class InitialBalanceTableItem(KaoTableItem):
    """ Represents a Table Widget Item for an Account Starting Balance """
    
    def __init__(self, account, transactionTable):
        """ Initialize the Starting Balance Item """
        self.transactionTable = transactionTable
        self.account = account
        KaoTableItem.__init__(self)
        
    def getData(self):
        """ Return the item's data as a string """
        return GetDollarString(self.account.initial_balance)
        
    def saveData(self, value):
        """ Save Data """
        try:
            self.account.initial_balance = GetCentsFromDollarString(value)
            Accounts.save()
            TheBalanceHelper.setupBalancesForAccount(self.account)
            self.transactionTable.updateBalanceColumn()
        except InvalidOperation:
            pass # The cast from the string to a Decimal failed