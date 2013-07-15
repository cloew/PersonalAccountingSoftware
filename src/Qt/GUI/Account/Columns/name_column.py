from Qt.GUI.Account.TableWidgets.name_table_item import NameTableItem

class NameColumn:
    """ Represents the Name Column """
    HEADER = "Name"
    
    def getItemForColumn(self, account):
        """  """
        return NameTableItem(account)
    
    def getWidgetForColumn(self, account):
        """  """
        return None 