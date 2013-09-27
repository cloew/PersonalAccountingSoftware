from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Transaction.Table.TableWidgets.amount_table_item import AmountTableItem

class AmountColumn(KaoTableColumn):
    """ Represents the Amount Column """
    HEADER = "Amount"
    
    def getItemForColumn(self, transaction):
        """  """
        return AmountTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 