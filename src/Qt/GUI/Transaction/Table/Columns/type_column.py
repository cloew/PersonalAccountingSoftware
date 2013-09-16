from Qt.GUI.Transaction.Table.TableWidgets.type_table_item import TypeTableItem

from PySide.QtGui import QTableWidgetItem 

class TypeColumn:
    """ Represents the Type Column """
    HEADER = "Type"
    
    def __init__(self, table):
        """ Initialize the Type Column """
        self.table = table
    
    def getItemForColumn(self, transaction):
        """  """
        return TypeTableItem(transaction, self.table)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 