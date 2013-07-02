from Qt.GUI.Transaction.Columns.amount_table_item import AmountTableItem

from PySide.QtGui import QTableWidgetItem 

class AmountColumn:
    """ Represents the Amount Column """
    HEADER = "Amount"
    
    def getItemForColumn(self, transaction):
        """  """
        return AmountTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 