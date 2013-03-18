from starting_balance_column import StartingBalanceColumn
from name_column import NameColumn

from db.accounts import Accounts
from PySide.QtCore import Qt
from Qt.Model.table_model import TableModel

class AccountTableModel(TableModel):
    """ Reprsents the Account List as a Table """

    def getColumns(self):
        """ Get the Columns for the table """
        return [StartingBalanceColumn(),
                NameColumn()]

    def rowCount(self, parent):
        """ Returns the number of rows in the table """
        return len(Accounts.all())