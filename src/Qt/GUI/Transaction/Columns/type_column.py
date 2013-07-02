from Qt.GUI.Transaction.Columns.type_table_item import TypeTableItem

from PySide.QtGui import QTableWidgetItem 

class TypeColumn:
    """ Represents the Type Column """
    HEADER = "Type"
    
    def getItemForColumn(self, transaction):
        """  """
        return TypeTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 