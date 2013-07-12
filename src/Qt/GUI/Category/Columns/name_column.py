from Qt.GUI.Category.TableItems.name_table_item import NameTableItem

class NameColumn:
    """ Represents the Category Name Column """
    HEADER = "Name"
    
    def getItemForColumn(self, transaction):
        """  """
        return NameTableItem(category)
    
    def getWidgetForColumn(self, category):
        """  """
        return None 