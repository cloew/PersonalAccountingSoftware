from Qt.GUI.Transaction.Columns.date_table_item import DateTableItem

class DateColumn:
    """ Represents the Date Column """
    HEADER = "Amount"
    
    def getItemForColumn(self, transaction):
        """  """
        return DateTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 