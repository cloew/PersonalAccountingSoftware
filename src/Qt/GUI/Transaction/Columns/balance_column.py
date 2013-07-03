from Qt.GUI.Transaction.Columns.balance_table_item import BalanceTableItem

from PySide.QtGui import QTableWidgetItem 

class BalanceColumn:
    """ Represents the Balance Column """
    HEADER = "Balance"
    
    def getItemForColumn(self, transaction):
        """  """
        return BalanceTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 