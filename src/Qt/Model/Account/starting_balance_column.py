from decimal import Decimal, InvalidOperation
from Qt.Model.Account.account_column import AccountColumn

class StartingBalanceColumn(AccountColumn):
    """ Represents the Account StartingBalance Column """
    header_name = "Starting Balance"

    def getDataForAccount(self, account):
        """ Return data for the provided account """
        if account.starting_balance is not None:
            starting_balance = account.starting_balance
            cents = starting_balance%100
            dollars = starting_balance/100
            return "${0:,}.{1:{fill}2}".format(dollars, cents, fill=0)

    def setDataForAccount(self, account, value):
        """ Set data for the provided account """
        try:
            cleanedValue = value
            if cleanedValue.startswith('$'):
                cleanedValue = cleanedValue[1:]
            newStartingBalance = Decimal(cleanedValue)
            account.starting_balance = int(newStartingBalance*100)
            return True
        except InvalidOperation:
            pass # The cast from the string to a Decimal

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "The Starting Balance of money in the account."