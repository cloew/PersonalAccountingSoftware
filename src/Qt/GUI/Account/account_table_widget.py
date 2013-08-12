from db.accounts import Accounts

from Qt.GUI.Account.Columns.name_column import NameColumn
from Qt.GUI.Account.Columns.current_balance_column import CurrentBalanceColumn
from Qt.GUI.Account.Columns.starting_balance_column import StartingBalanceColumn
from Qt.GUI.Core.kao_table_widget import KaoTableWidget

class AccountTableWidget(KaoTableWidget):
    """ The Account Table Widget View """
    
    def __init__(self, transactionTable):
        """ Initialize the Account Table Widget """
        self.columns = [NameColumn(), StartingBalanceColumn(transactionTable), CurrentBalanceColumn()]
        accounts = Accounts.all()
        KaoTableWidget.__init__(self, accounts, self.columns)
        
    def tabSelected(self):
        """ Do Nothing when this tab is selected """