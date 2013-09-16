from Qt.GUI.Transaction.Table.TableWidgets.category_table_item import CategoryTableItem

class CategoryColumn:
    """ Represents the Category Column """
    HEADER = "Category"
    
    def getItemForColumn(self, transaction):
        """  """
        return CategoryTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 