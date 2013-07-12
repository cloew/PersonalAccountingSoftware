from Qt.GUI.Category.TableWidgets.name_table_item import NameTableItem

class NameColumn:
    """ Represents the Category Name Column """
    HEADER = "Name"
    
    def getItemForColumn(self, category):
        """  """
        return NameTableItem(category)
    
    def getWidgetForColumn(self, category):
        """  """
        return None 