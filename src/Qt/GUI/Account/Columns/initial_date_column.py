from Qt.GUI.Account.TableWidgets.initial_date_table_item import InitialDateTableItem
from Qt.GUI.Core.kao_table_column import KaoTableColumn

class InitialDateColumn(KaoTableColumn):
    """ Represents the Initial Date Column """
    HEADER = "as of"
    
    def __init__(self, transactionTable):
        """ Initialize the Starting Balance Column """
        self.transactionTable = transactionTable
        KaoTableColumn.__init__(self)
    
    def getItemForColumn(self, account):
        """  """
        return InitialDateTableItem(account, self.transactionTable)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 