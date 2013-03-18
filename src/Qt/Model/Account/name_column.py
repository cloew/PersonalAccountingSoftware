from Qt.Model.Account.account_column import AccountColumn

class NameColumn(AccountColumn):
    """ Represents the Account Description Column """
    header_name = "Description"

    def getDataForAccount(self, account):
        """ Return data for the provided account """
        if account.name is not None:
            return account.name

    def setDataForAccount(self, account, value):
        """ Set data for the provided account """
        account.name = value
        return True

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row """
        return "Name of the account."