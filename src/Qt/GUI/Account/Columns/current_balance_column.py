from Qt.GUI.Account.TableWidgets.current_balance_table_item import CurrentBalanceTableItem
from Qt.GUI.Core.kao_table_column import KaoTableColumn

class CurrentBalanceColumn(KaoTableColumn):
    """ Represents the Current Balance Column """
    HEADER = "Current Balance"
    
    def getItemForColumn(self, account):
        """  """
        return CurrentBalanceTableItem(account)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 