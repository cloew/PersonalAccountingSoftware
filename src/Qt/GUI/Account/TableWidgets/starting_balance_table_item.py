from db.accounts import Accounts
from Qt.GUI.Core.kao_table_item import KaoTableItem

from db.transactions import Transactions
from Utilities.balance_helper import TheBalanceHelper
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString
from Qt.GUI.Transaction.TableWidgets.transaction_table_item import TransactionTableItem

from decimal import InvalidOperation

class StartingBalanceTableItem(KaoTableItem):
    """ Represents a Table Widget Item for an Account Starting Balance """
    
    def __init__(self, account):
        """ Initialize the Starting Balance Item """
        #self.table = table
        self.account = account
        KaoTableItem.__init__(self)
        
    def getData(self):
        """ Return the item's data as a string """
        return GetDollarString(self.account.starting_balance)
        
    def saveData(self, value):
        """ Save Data """
        try:
            self.account.starting_balance = GetCentsFromDollarString(value)
            Accounts.save()
            TheBalanceHelper.setupBalancesForAccount(self.account)
            #self.table.updateBalanceColumn()
        except InvalidOperation:
            pass # The cast from the string to a Decimal failed