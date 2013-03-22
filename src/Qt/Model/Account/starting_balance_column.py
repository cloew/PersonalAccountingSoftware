from decimal import InvalidOperation
from Qt.Model.Account.account_column import AccountColumn
from Utilities.dollar_amount_helper import GetDollarString, GetCentsFromDollarString

class StartingBalanceColumn(AccountColumn):
    """ Represents the Account StartingBalance Column """
    header_name = "Starting Balance"

    def getDataForAccount(self, account):
        """ Return data for the provided account """
        if account.starting_balance is not None:
            starting_balance = account.starting_balance
            return GetDollarString(account.starting_balance)

    def setDataForAccount(self, account, value):
        """ Set data for the provided account """
        try:
            account.starting_balance = GetCentsFromDollarString(value)
            return True
        except InvalidOperation:
            pass # The cast from the string to a Decimal

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The Starting Balance of money in the account."