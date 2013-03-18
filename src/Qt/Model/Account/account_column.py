from db.accounts import Accounts
from PySide.QtCore import QAbstractTableModel, QModelIndex, Qt
from Qt.Model.table_column import TableColumn

class AccountColumn(TableColumn):
    """ Represents a column in the Account Table """
    header_name = "TODO: Replace with real name" # Should be overridden in Sub Class

    def getData(self, row):
        """ Return data for the account in the given row """
        account = self.getAccountForRow(row)
        if account is not None:
            return self.getDataForAccount(account)

    def getDataForAccount(self, account):
        """ Return data for the provided account.
            Should be overridden in sub class """

    def setData(self, row, value):
        """ Set the data in this column of the given account """
        account = self.getAccountForRow(row)
        if account is not None:
            return self.setDataForAccount(account, value)

    def setDataForAccount(self, account, value):
        """ Set data for the provided account.
            Return whether the entry was set.
            Should be overridden in sub class. """

    def getTip(self, row):
        """ Return the Status/Tool Tip for the given row.
            Should be overridden in sub class. """

    def getAccountForRow(self, row):
        """ Returns the Account in the given row """
        accounts = Accounts.all()
        if row < len(accounts):
            return accounts[row]