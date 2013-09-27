from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Transaction.Table.TableWidgets.description_table_item import DescriptionTableItem

from PySide.QtGui import QTableWidgetItem 

class DescriptionColumn(KaoTableColumn):
    """ Represents the Description Column """
    HEADER = "Description"
    
    def getItemForColumn(self, transaction):
        """  """
        return DescriptionTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 