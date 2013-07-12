from Qt.GUI.Transaction.TableWidgets.category_table_item import CategoryTableItem

from PySide.QtGui import QTableWidgetItem 

class CategoryColumn:
    """ Represents the Category Column """
    HEADER = "Category"
    
    def getItemForColumn(self, transaction):
        """  """
        return CategoryTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 