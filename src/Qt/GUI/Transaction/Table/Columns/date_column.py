from Qt.GUI.Core.kao_table_column import KaoTableColumn
from Qt.GUI.Transaction.Table.TableWidgets.date_table_item import DateTableItem

class DateColumn(KaoTableColumn):
    """ Represents the Date Column """
    HEADER = "Date"
    
    def getItemForColumn(self, transaction):
        """  """
        return DateTableItem(transaction)
    
    def getWidgetForColumn(self, transaction):
        """  """
        return None 