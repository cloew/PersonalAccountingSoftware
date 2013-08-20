from db.accounts import Accounts

from Qt.GUI.Account.Columns.name_column import NameColumn
from Qt.GUI.Account.Columns.current_balance_column import CurrentBalanceColumn
from Qt.GUI.Account.Columns.initial_balance_column import InitialBalanceColumn
from Qt.GUI.Account.Columns.initial_date_column import InitialDateColumn
from Qt.GUI.Core.kao_table_widget import KaoTableWidget

class AccountTableWidget(KaoTableWidget):
    """ The Account Table Widget View """
    
    def __init__(self, transactionTable):
        """ Initialize the Account Table Widget """
        self.columns = [NameColumn(), InitialBalanceColumn(transactionTable), InitialDateColumn(transactionTable), CurrentBalanceColumn()]
        accounts = Accounts.all()
        KaoTableWidget.__init__(self, accounts, self.columns)
        
    def tabSelected(self):
        """ Update the Current Balance Column """
        balanceColumnIndex = self.getColumnIndex(CurrentBalanceColumn)
        
        for row in range(self.rowCount()):
            item = self.item(row, balanceColumnIndex)
            item.updateData()