from Qt.GUI.Account.TableWidgets.name_table_item import NameTableItem
from Qt.GUI.Core.kao_table_column import KaoTableColumn

class NameColumn(KaoTableColumn):
    """ Represents the Name Column """
    HEADER = "Name"
    
    def getItemForColumn(self, account):
        """  """
        return NameTableItem(account)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 