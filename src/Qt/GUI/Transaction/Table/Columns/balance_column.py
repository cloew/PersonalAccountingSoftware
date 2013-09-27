from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Transaction.Table.TableWidgets.balance_table_item import BalanceTableItem

class BalanceColumn(KaoTableColumn):
    """ Represents the Balance Column """
    HEADER = "Balance"
    
    def __init__(self, account):
        """ Initialize the Balance Column """
        self.account = account
        KaoTableColumn.__init__(self)
    
    def getItemForColumn(self, transaction):
        """  """
        return BalanceTableItem(transaction, self.account)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 