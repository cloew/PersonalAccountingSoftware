from Qt.GUI.Transaction.TableWidgets.amount_table_item import AmountTableItem

from PySide.QtGui import QTableWidgetItem 

class AmountColumn:
    """ Represents the Amount Column """
    HEADER = "Amount"
    
    def __init__(self, table):
        """ Initialize the Amount Column """
        self.table = table
    
    def getItemForColumn(self, transaction):
        """  """
        return AmountTableItem(transaction, self.table)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 