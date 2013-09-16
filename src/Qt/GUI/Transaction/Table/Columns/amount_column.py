from Qt.GUI.Transaction.Table.TableWidgets.amount_table_item import AmountTableItem

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