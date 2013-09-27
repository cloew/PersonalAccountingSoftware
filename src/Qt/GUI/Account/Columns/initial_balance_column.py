from Qt.GUI.Account.TableWidgets.initial_balance_table_item import InitialBalanceTableItem
from Qt.GUI.Core.kao_table_column import KaoTableColumn

class InitialBalanceColumn(KaoTableColumn):
    """ Represents the Initial Balance Column """
    HEADER = "Initial Balance"
    
    def __init__(self, transactionTable):
        """ Initialize the Starting Balance Column """
        self.transactionTable = transactionTable
        KaoTableColumn.__init__(self)
    
    def getItemForColumn(self, account):
        """  """
        return InitialBalanceTableItem(account, self.transactionTable)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 