from Qt.GUI.Transaction.Table.TableWidgets.date_table_item import DateTableItem

class DateColumn:
    """ Represents the Date Column """
    HEADER = "Date"
    
    def __init__(self, table):
        """ Initialize the Date Column """
        self.table = table
    
    def getItemForColumn(self, transaction):
        """  """
        return DateTableItem(transaction, self.table)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 