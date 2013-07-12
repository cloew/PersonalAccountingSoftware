from Qt.GUI.Transaction.TableWidgets.date_table_item import DateTableItem

class DateColumn:
    """ Represents the Date Column """
    HEADER = "Date"
    
    def getItemForColumn(self, transaction):
        """  """
        return DateTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 