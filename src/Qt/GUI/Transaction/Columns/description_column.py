from Qt.GUI.Transaction.TableWidgets.description_table_item import DescriptionTableItem

from PySide.QtGui import QTableWidgetItem 

class DescriptionColumn:
    """ Represents the Description Column """
    HEADER = "Description"
    
    def getItemForColumn(self, transaction):
        """  """
        return DescriptionTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 